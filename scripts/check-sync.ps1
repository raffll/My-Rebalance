# check-sync.ps1
# Checks that README target values are in sync with JSON effect values.
#
# Usage:
#   .\check-sync.ps1
#   .\check-sync.ps1 -Verbose
#   .\check-sync.ps1 -File "R3 - Magic.json"

param(
    [string]$File    = "",
    [switch]$Verbose
)

# ---------------------------------------------------------------------------
# Parse README entries that have a target value (contain "->")
# Returns a list of hashtables: Name, VanillaStr, TargetStr, Section
# ---------------------------------------------------------------------------
function Parse-ReadmeEntries {
    param([string]$Path)

    $entries = New-Object System.Collections.Generic.List[hashtable]
    $inBlock = $false
    $currentSection = ""

    foreach ($line in (Get-Content $Path -Encoding UTF8)) {
        if ($line -match '^###\s+(.+)') {
            $currentSection = $Matches[1].Trim()
        }

        if ($line -match '^```') {
            $inBlock = -not $inBlock
            continue
        }

        if (-not $inBlock) { continue }

        $t = $line.Trim()
        if ($t -eq "")                                    { continue }
        if ($t -match '^Base Cost\s')                     { continue }
        if ($t -match '^f[A-Z]|^i[A-Z]|^s[A-Z]')         { continue }
        if ($t -notmatch '->')                            { continue }
        if ($t -match '->\s*TODO')                        { continue }

        # Skip pure rename lines (no digits before the arrow)
        $beforeArrow = ($t -split '->')[0]
        if ($beforeArrow -notmatch '\d')                  { continue }

        # Match: "Name    vanilla -> target   comment"
        if ($t -match '^(.+?)\s{2,}(.+?)\s*->\s*(.+?)(\s{2,}.*)?$') {
            $rawName   = $Matches[1].Trim()
            $vanStr    = $Matches[2].Trim()
            $tgtStr    = $Matches[3].Trim()
            $comment   = if ($Matches[4]) { $Matches[4].Trim() } else { "" }

            # If name itself contains " -> " it is a rename; use the right side
            if ($rawName -match '^.+?\s*->\s*(.+)$') {
                $rawName = $Matches[1].Trim()
            }

            # Extract enchantment ID from trailing comment (last whitespace-separated token
            # that looks like an ID: lowercase, may contain underscores, apostrophes, spaces)
            # IDs are the last word-group after the last run of spaces in the comment,
            # but only if they don't look like scale comments (x2/x1) or notes
            $enchId = ""
            if ($comment -ne "" -and $comment -notmatch '^x\d|^used|^!\s') {
                # The ID is the whole comment if it contains no spaces, or matches known patterns
                $candidate = $comment -replace '\s+', ' '
                # Accept as ID if it looks like a record ID (no spaces, or known multi-word IDs)
                if ($candidate -match "^[a-zA-Z0-9_'\. -]+$" -and $candidate -notmatch '\s') {
                    $enchId = $candidate.ToLower()
                } elseif ($candidate -match "^[a-zA-Z0-9_'\. ]+$") {
                    # Multi-word IDs like "ulms juicedaw's feather_en" or "Crescent Moon"
                    $enchId = $candidate.ToLower()
                }
            }

            $entry = @{
                Name       = $rawName
                VanillaStr = $vanStr
                TargetStr  = $tgtStr
                Section    = $currentSection
                EnchId     = $enchId
            }
            $entries.Add($entry)
        }
    }

    return $entries
}

# ---------------------------------------------------------------------------
# Parse a target value string into numeric components
# ---------------------------------------------------------------------------
function Parse-TargetValues {
    param([string]$s)

    $r = @{ MinMag = $null; MaxMag = $null; Duration = $null; Area = $null }

    # Strip cost override [N]
    $s = $s -replace '\[\d+\]', '' 
    $s = $s.Trim()

    # Strip area Nft
    if ($s -match '(\d+)ft') {
        $r.Area = [int]$Matches[1]
        $s = $s -replace '\d+ft', ''
        $s = $s.Trim()
    }

    # Duration-only: "30s"
    if ($s -match '^(\d+)s$') {
        $r.Duration = [int]$Matches[1]
        return $r
    }

    # Magnitude-only: "100"
    if ($s -match '^(\d+)$') {
        $r.MinMag = [int]$Matches[1]
        $r.MaxMag = [int]$Matches[1]
        return $r
    }

    # Range/duration: "60-120/50s" or "50/40s"
    if ($s -match '^(\d+)(?:-(\d+))?/(\d+)s') {
        $r.MinMag   = [int]$Matches[1]
        $r.MaxMag   = if ($Matches[2] -and $Matches[2] -ne "") { [int]$Matches[2] } else { [int]$Matches[1] }
        $r.Duration = [int]$Matches[3]
        return $r
    }

    return $r
}

# ---------------------------------------------------------------------------
# Build lookup tables from JSON:
#   $byName : display name (lowercase) -> list of Spell/Alchemy objects
#   $byId   : id (lowercase)           -> object (any type with effects)
# ---------------------------------------------------------------------------
function Build-JsonLookups {
    param([string]$JsonPath)

    $data   = Get-Content $JsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $byName = @{}
    $byId   = @{}

    foreach ($obj in $data) {
        # Index by ID for all types that have effects
        if ($obj.id -and $obj.effects) {
            $key = $obj.id.ToLower().Trim()
            if (-not $byId.ContainsKey($key)) {
                $byId[$key] = New-Object System.Collections.Generic.List[object]
            }
            $byId[$key].Add($obj)
        }

        # Index Spell/Alchemy by display name too
        if ($obj.type -eq "Spell" -or $obj.type -eq "Alchemy") {
            if (-not $obj.name) { continue }
            $key = $obj.name.ToLower().Trim()
            if (-not $byName.ContainsKey($key)) {
                $byName[$key] = New-Object System.Collections.Generic.List[object]
            }
            $byName[$key].Add($obj)
        }
    }

    return $byName, $byId
}

# ---------------------------------------------------------------------------
# Get all effect value sets from a JSON object
# ---------------------------------------------------------------------------
function Get-EffectValues {
    param($obj)

    $list = New-Object System.Collections.Generic.List[hashtable]
    foreach ($eff in $obj.effects) {
        $list.Add(@{
            MinMag   = [int]$eff.min_magnitude
            MaxMag   = [int]$eff.max_magnitude
            Duration = [int]$eff.duration
            Area     = [int]$eff.area
        })
    }
    return $list
}

# ---------------------------------------------------------------------------
# Check if a JSON object matches the target values
# Checks effect magnitudes/durations AND spell cost (for cost-only entries)
# ---------------------------------------------------------------------------
function Test-Match {
    param([hashtable]$target, $jsonObj)

    $effects = Get-EffectValues -obj $jsonObj

    # If target has duration, it must match an effect
    if ($null -ne $target.Duration) {
        foreach ($eff in $effects) {
            $ok = $true
            if ($null -ne $target.MinMag   -and $target.MinMag   -ne $eff.MinMag)   { $ok = $false }
            if ($null -ne $target.MaxMag   -and $target.MaxMag   -ne $eff.MaxMag)   { $ok = $false }
            if ($null -ne $target.Duration -and $target.Duration -ne $eff.Duration) { $ok = $false }
            if ($null -ne $target.Area     -and $target.Area     -ne $eff.Area)     { $ok = $false }
            if ($ok) { return $true }
        }
        return $false
    }

    # No duration: could be a cost-only entry (e.g. trap costs)
    # Check data.cost first
    if ($null -ne $target.MinMag -and $jsonObj.data -and $null -ne $jsonObj.data.cost) {
        if ($target.MinMag -eq [int]$jsonObj.data.cost) { return $true }
    }

    # Also check magnitude-only against effects (e.g. Dispel potion)
    foreach ($eff in $effects) {
        $ok = $true
        if ($null -ne $target.MinMag -and $target.MinMag -ne $eff.MinMag) { $ok = $false }
        if ($null -ne $target.MaxMag -and $target.MaxMag -ne $eff.MaxMag) { $ok = $false }
        if ($ok) { return $true }
    }

    return $false
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

$pairs = @(
    @{ Readme = "README - Magic.md";              Json = "R3 - Magic.json" },
    @{ Readme = "README - Races & Birthsigns.md"; Json = "R3 - Races & Birthsigns.json" },
    @{ Readme = "README - Core.md";               Json = "R3 - Core.json" }
)

if ($File -ne "") {
    $pairs = $pairs | Where-Object { $_.Json -eq $File -or $_.Readme -eq $File }
    if ($pairs.Count -eq 0) {
        Write-Error "No matching pair found for: $File"
        exit 1
    }
}

$totalOk         = 0
$totalMismatches = 0
$totalSkipped    = 0

foreach ($pair in $pairs) {
    $readmePath = $pair.Readme
    $jsonPath   = $pair.Json

    if (-not (Test-Path $readmePath)) { continue }
    if (-not (Test-Path $jsonPath))   { continue }

    Write-Host ""
    Write-Host "=== $readmePath <-> $jsonPath ===" -ForegroundColor Cyan

    $entries          = Parse-ReadmeEntries -Path $readmePath
    $byName, $byId    = Build-JsonLookups  -JsonPath $jsonPath

    $ok         = 0
    $mismatches = 0
    $skipped    = 0

    foreach ($entry in $entries) {
        $name    = $entry.Name
        $nameKey = $name.ToLower().Trim()
        $enchId  = $entry.EnchId
        $target  = Parse-TargetValues -s $entry.TargetStr

        # Resolve which JSON objects to check
        $jsonObjs = $null
        $lookupBy = ""

        if ($enchId -ne "") {
            if ($byId.ContainsKey($enchId)) {
                # Found by ID (Alchemy, Spell, or Enchanting)
                $jsonObjs = $byId[$enchId]
                $lookupBy = "id:$enchId"
            } else {
                # ID specified but not found in JSON
                $mismatches++
                $totalMismatches++
                Write-Host ("  MISSING  [{0}] {1}  (id: {2} not in JSON)" -f $entry.Section, $name, $enchId) -ForegroundColor Red
                continue
            }
        } elseif ($byName.ContainsKey($nameKey)) {
            $jsonObjs = $byName[$nameKey]
            $lookupBy = "name"
        } else {
            # Not found in JSON — only skip generic potion rule lines (e.g. "Bargain...", "Cheap...")
            if ($name -match '\.\.\.') {
                $skipped++
                Write-Host ("  SKIP  [{0}] {1} -- general rule" -f $entry.Section, $name) -ForegroundColor DarkGray
            } else {
                $mismatches++
                $totalMismatches++
                Write-Host ("  MISSING  [{0}] {1} -- not in JSON" -f $entry.Section, $name) -ForegroundColor Red
            }
            continue
        }

        $matched = $false
        foreach ($jobj in $jsonObjs) {
            if (Test-Match -target $target -jsonObj $jobj) {
                $matched = $true
                break
            }
        }

        if ($matched) {
            $ok++
            $tag = if ($lookupBy -like "id:*") { " [$($entry.EnchId)]" } else { "" }
            Write-Host ("  OK    [{0}] {1}{2} = {3}" -f $entry.Section, $name, $tag, $entry.TargetStr) -ForegroundColor Green
        } else {
            $mismatches++
            $totalMismatches++

            $actualParts = New-Object System.Collections.Generic.List[string]
            foreach ($jobj in $jsonObjs) {
                $effs = Get-EffectValues -obj $jobj
                foreach ($e in $effs) {
                    $min = $e.MinMag; $max = $e.MaxMag; $dur = $e.Duration
                    $vs  = if ($min -eq $max) { "$min/$($dur)s" } else { "$min-$max/$($dur)s" }
                    if (-not $actualParts.Contains($vs)) { $actualParts.Add($vs) }
                }
            }
            $actualStr = $actualParts -join " | "

            $idNote = if ($enchId -ne "") { "  (id: $enchId)" } else { "" }
            Write-Host ("  MISMATCH [{0}] {1}{2}" -f $entry.Section, $name, $idNote) -ForegroundColor Red
            Write-Host ("           README target : {0}" -f $entry.TargetStr) -ForegroundColor Yellow
            Write-Host ("           JSON actual   : {0}" -f $actualStr) -ForegroundColor Yellow
        }
    }

    $totalOk      += $ok
    $totalSkipped += $skipped

    $color = if ($mismatches -gt 0) { "Red" } else { "Green" }
    Write-Host ""
    Write-Host ("  Results: {0} OK, {1} mismatch(es), {2} skipped (not in JSON)" -f $ok, $mismatches, $skipped) -ForegroundColor $color
}

Write-Host ""
$color = if ($totalMismatches -gt 0) { "Red" } else { "Green" }
Write-Host ("=== TOTAL: {0} OK, {1} mismatch(es), {2} skipped ===" -f $totalOk, $totalMismatches, $totalSkipped) -ForegroundColor $color

if ($totalMismatches -gt 0) { exit 1 } else { exit 0 }

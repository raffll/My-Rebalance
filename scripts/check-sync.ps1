# check-sync.ps1
# Checks README <-> JSON sync in both directions:
#   1. README entries missing or mismatched in JSON
#   2. JSON Spell/Alchemy entries missing from README
#
# Usage:
#   .\check-sync.ps1
#   .\check-sync.ps1 -Verbose

param(
    [switch]$Verbose
)

# ---------------------------------------------------------------------------
# Parse README entries that have a target value (contain "->")
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

            # Extract record ID from trailing comment using "id: <value>" format
            $enchId = ""
            if ($comment -ne "") {
                $parts = $comment -split ';'
                foreach ($part in $parts) {
                    $p = $part.Trim()
                    if ($p -match '^id:\s*(.+)$') {
                        $enchId = $Matches[1].Trim().ToLower()
                        break
                    }
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
# Parse ALL README spell/potion names (including non-arrow entries)
# Returns a set of (name_lower) and (id_lower) that appear in README
# ---------------------------------------------------------------------------
function Parse-ReadmeAllNames {
    param([string]$Path)

    $names = New-Object System.Collections.Generic.HashSet[string]
    $ids   = New-Object System.Collections.Generic.HashSet[string]
    $inBlock = $false

    foreach ($line in (Get-Content $Path -Encoding UTF8)) {
        if ($line -match '^```') {
            $inBlock = -not $inBlock
            continue
        }
        if (-not $inBlock) { continue }

        $t = $line.Trim()
        if ($t -eq "")                                    { continue }
        if ($t -match '^Base Cost\s')                     { continue }
        if ($t -match '^f[A-Z]|^i[A-Z]|^s[A-Z]')         { continue }
        if ($t -match '^\.\.\.')                          { continue }

        # Extract name (first token before 2+ spaces)
        if ($t -match '^(.+?)\s{2,}') {
            $rawName = $Matches[1].Trim()
            # Handle renames: add both sides
            if ($rawName -match '^(.+?)\s*->\s*(.+)$') {
                [void]$names.Add($Matches[1].Trim().ToLower())
                [void]$names.Add($Matches[2].Trim().ToLower())
            } else {
                [void]$names.Add($rawName.ToLower())
            }
        } elseif ($t -match '^([A-Z].+)$') {
            # Single-word entries without values (rare)
            [void]$names.Add($t.ToLower())
        }

        # Extract IDs
        if ($t -match 'id:\s*(\S+)') {
            [void]$ids.Add($Matches[1].ToLower())
        }

        # Handle general rules with "..." — mark the prefix as a pattern
        if ($t -match '^(.+?)\.\.\.\s') {
            [void]$names.Add($Matches[1].Trim().ToLower() + "...")
        }
    }

    return $names, $ids
}

# ---------------------------------------------------------------------------
# Parse target values
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
# Build JSON lookups
# ---------------------------------------------------------------------------
function Build-JsonLookups {
    param([string]$JsonPath)

    $data   = Get-Content $JsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $byName = @{}
    $byId   = @{}
    $allSpellAlchemy = New-Object System.Collections.Generic.List[object]

    foreach ($obj in $data) {
        if ($obj.id -and $obj.effects) {
            $key = $obj.id.ToLower().Trim()
            if (-not $byId.ContainsKey($key)) {
                $byId[$key] = New-Object System.Collections.Generic.List[object]
            }
            $byId[$key].Add($obj)
        }

        if ($obj.type -eq "Spell" -or $obj.type -eq "Alchemy") {
            if (-not $obj.name) { continue }
            $key = $obj.name.ToLower().Trim()
            if (-not $byName.ContainsKey($key)) {
                $byName[$key] = New-Object System.Collections.Generic.List[object]
            }
            $byName[$key].Add($obj)
            $allSpellAlchemy.Add($obj)
        }
    }

    return $byName, $byId, $allSpellAlchemy
}

# ---------------------------------------------------------------------------
# Get effect values from JSON object
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
# Check if JSON object matches target values
# ---------------------------------------------------------------------------
function Test-Match {
    param([hashtable]$target, $jsonObj)

    $effects = Get-EffectValues -obj $jsonObj

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

    if ($null -ne $target.MinMag -and $jsonObj.data -and $null -ne $jsonObj.data.cost) {
        if ($target.MinMag -eq [int]$jsonObj.data.cost) { return $true }
    }

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
    @{ Readme = "README - Spells & Potions.md"; Json = "R3 - Spells & Potions.json" }
)

$totalOk         = 0
$totalMismatches = 0
$totalMissing    = 0
$totalSkipped    = 0

foreach ($pair in $pairs) {
    $readmePath = $pair.Readme
    $jsonPath   = $pair.Json

    if (-not (Test-Path $readmePath)) { continue }
    if (-not (Test-Path $jsonPath))   { continue }

    Write-Host ""
    Write-Host "=== $readmePath <-> $jsonPath ===" -ForegroundColor Cyan

    $entries                        = Parse-ReadmeEntries -Path $readmePath
    $readmeNames, $readmeIds        = Parse-ReadmeAllNames -Path $readmePath
    $byName, $byId, $allSpellAlch   = Build-JsonLookups -JsonPath $jsonPath

    # --- Part 1: README -> JSON (value mismatches and missing in JSON) ---
    Write-Host ""
    Write-Host "  --- README -> JSON ---" -ForegroundColor White

    $ok         = 0
    $mismatches = 0
    $skipped    = 0

    foreach ($entry in $entries) {
        $name    = $entry.Name
        $nameKey = $name.ToLower().Trim()
        $enchId  = $entry.EnchId
        $target  = Parse-TargetValues -s $entry.TargetStr

        $jsonObjs = $null
        $lookupBy = ""

        if ($enchId -ne "") {
            if ($byId.ContainsKey($enchId)) {
                $jsonObjs = $byId[$enchId]
                $lookupBy = "id:$enchId"
            } else {
                $mismatches++
                Write-Host ("  MISSING  [{0}] {1}  (id: {2} not in JSON)" -f $entry.Section, $name, $enchId) -ForegroundColor Red
                continue
            }
        } elseif ($byName.ContainsKey($nameKey)) {
            $jsonObjs = $byName[$nameKey]
            $lookupBy = "name"
        } else {
            if ($name -match '\.\.\.') {
                $skipped++
                if ($Verbose) { Write-Host ("  SKIP  [{0}] {1} -- general rule" -f $entry.Section, $name) -ForegroundColor DarkGray }
            } else {
                $mismatches++
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
            if ($Verbose) {
                $tag = if ($lookupBy -like "id:*") { " [$($entry.EnchId)]" } else { "" }
                Write-Host ("  OK    [{0}] {1}{2} = {3}" -f $entry.Section, $name, $tag, $entry.TargetStr) -ForegroundColor Green
            }
        } else {
            $mismatches++

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
    $totalMismatches += $mismatches

    Write-Host ""
    $color = if ($mismatches -gt 0) { "Red" } else { "Green" }
    Write-Host ("  README->JSON: {0} OK, {1} mismatch(es), {2} skipped" -f $ok, $mismatches, $skipped) -ForegroundColor $color

    # --- Part 2: JSON -> README (entries in JSON missing from README) ---
    Write-Host ""
    Write-Host "  --- JSON -> README ---" -ForegroundColor White

    $missingFromReadme = 0

    foreach ($obj in $allSpellAlch) {
        $id      = $obj.id.ToLower().Trim()
        $nameKey = $obj.name.ToLower().Trim()

        # Check if this JSON entry is referenced in README (by id or by name)
        $found = $false
        if ($readmeIds.Contains($id)) { $found = $true }
        if ($readmeNames.Contains($nameKey)) { $found = $true }

        # Check against general rule patterns (e.g. "masterful..." matches "masterful red wisdom")
        if (-not $found) {
            foreach ($pattern in $readmeNames) {
                if ($pattern.EndsWith("...")) {
                    $prefix = $pattern.Substring(0, $pattern.Length - 3)
                    if ($nameKey.StartsWith($prefix)) {
                        $found = $true
                        break
                    }
                }
            }
        }

        if (-not $found) {
            $missingFromReadme++
            $totalMissing++
            Write-Host ("  MISSING  {0} (id: {1}) -- not in README" -f $obj.name, $obj.id) -ForegroundColor Magenta
        }
    }

    if ($missingFromReadme -eq 0) {
        Write-Host "  All JSON entries found in README." -ForegroundColor Green
    } else {
        Write-Host ""
        Write-Host ("  JSON->README: {0} missing from README" -f $missingFromReadme) -ForegroundColor Magenta
    }
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
$color = if (($totalMismatches + $totalMissing) -gt 0) { "Red" } else { "Green" }
Write-Host ("TOTAL: {0} OK, {1} value mismatch(es), {2} missing from README, {3} skipped" -f $totalOk, $totalMismatches, $totalMissing, $totalSkipped) -ForegroundColor $color

if (($totalMismatches + $totalMissing) -gt 0) { exit 1 } else { exit 0 }

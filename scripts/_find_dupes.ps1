$data = Get-Content 'R3 - Spells & Potions.json' -Raw -Encoding UTF8 | ConvertFrom-Json

# Check for duplicate IDs
$ids = @{}
foreach ($obj in $data) {
    if (-not $obj.id) { continue }
    if ($obj.type -notin @("Spell", "Alchemy", "Enchanting")) { continue }
    $key = $obj.id.ToLower().Trim()
    if (-not $ids.ContainsKey($key)) { $ids[$key] = 0 }
    $ids[$key]++
}

$found = $false
foreach ($key in ($ids.Keys | Sort-Object)) {
    if ($ids[$key] -gt 1) {
        Write-Host ("DUPE ID: " + $key + " (x" + $ids[$key] + ")") -ForegroundColor Red
        $found = $true
    }
}

# Check for duplicate names (different IDs, same display name)
$names = @{}
foreach ($obj in $data) {
    if ($obj.type -notin @("Spell", "Alchemy", "Enchanting")) { continue }
    if (-not $obj.name) { continue }
    $key = $obj.name.ToLower().Trim()
    if (-not $names.ContainsKey($key)) { $names[$key] = @() }
    $names[$key] += $obj.id
}

foreach ($key in ($names.Keys | Sort-Object)) {
    if ($names[$key].Count -gt 1) {
        Write-Host ("DUPE NAME: " + $key) -ForegroundColor Yellow
        foreach ($id in $names[$key]) { Write-Host ("  id: " + $id) }
        $found = $true
    }
}

if (-not $found) {
    Write-Host "No duplicates found." -ForegroundColor Green
}

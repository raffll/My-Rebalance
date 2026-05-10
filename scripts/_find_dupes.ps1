$data = Get-Content 'R3 - Magic.json' -Raw -Encoding UTF8 | ConvertFrom-Json

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
        Write-Host ("DUPE: " + $key)
        foreach ($id in $names[$key]) { Write-Host ("  id: " + $id) }
    }
}

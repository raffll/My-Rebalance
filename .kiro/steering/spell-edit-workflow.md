# Spell Edit Workflow

When asked to modify a spell:

## 1. README update
Find the spell's section in the relevant `README - *.md` file and add or update its entry using this format:

```
Spell Name                                  [default mag/dur from vanilla] -> [new mag/dur]
```

- Values are `magnitude/duration` (e.g. `20/10s -> 50/40s`)
- Range spells use `min-max/duration` (e.g. `30-60/10s -> 60-120/50s`)
- If there is an area, append it after duration: `50/10s 10ft`
- If there is a cost override, append it in brackets: `50/10s [25]`
- Anything after the values (notes, flags) goes in a comment at the end of the line, with multiple comments separated by `;`: `50/10s               used by Aryon; !`
- Add the scale as a comment on the first spell that uses it, e.g. `x2.5/x4`. Skip the comment on subsequent spells if the scale is the same.
- Always use `xMAG/xDUR` format (e.g. `x10/x1` for magnitude-only, `x1/x4` for duration-only). Never write `x10 dur` or `x4 mag`.
- Do not add scale comments to potions.
- If the scale follows directly from the base cost change (opposite direction, same factor — e.g. base cost ÷2 → spells ×2), omit the scale comment entirely since it is implied.
- If the user writes a scale like `-> 5x/2x` as a trailing comment on a README entry (with `->` but no target value after it), it means: apply that scale to all entries in that section (until an empty line or a new `->` appears), compute and write the new target values in README and JSON, then remove the scale comment.
- The `->` means: left side is the vanilla/default value, right side is the new target value

## 2. JSON update
Find the spell entry in the relevant ESP JSON (e.g. `R3 - Magic.json`).

- If the spell **already exists** in the ESP JSON: update `min_magnitude`, `max_magnitude`, `duration`, `area` as needed.
- If the spell **does not exist** in the ESP JSON: copy the full entry from the appropriate default reference JSON in `tes3conv/` (Morrowind.json, Tribunal.json, Bloodmoon.json, or Tamriel_Data.json), then apply the new values.

## README IDs
Only add JSON IDs as comments in the README for:
- **Enchantments** (scrolls, weapons, clothing with enchantments)
- **Tamriel Data potions** (duplicate names that need disambiguation)

Do NOT add IDs for regular spells, vanilla potions, or base cost entries.

## JSON value scaling
The user will specify the scale to use each time. Wait for the user to provide the scale before writing JSON values.

The scale is applied to the **vanilla default values** (left of `->` in README) to produce the new values:
- `new_magnitude = vanilla_magnitude × scale_mag`
- `new_duration = vanilla_duration × scale_dur`

The JSON and README store the same new values — no conversion needed between them.

## Base Cost and spell compensation rule
When a magic effect's base cost is changed, spells of that school must be adjusted in the **opposite direction** to keep their effective cost roughly the same:
- If base cost is multiplied by X, then spell mag×dur must be divided by X (and vice versa)
- Example: base cost ÷2 → spell mag×dur ×2 (e.g. double magnitude, or double duration, or split between both)
- The split between magnitude and duration is chosen per spell as appropriate

## 3. Convert JSON back to ESP
After updating the JSON, convert to a temp filename (tes3conv creates numbered files if destination exists, so use a unique temp name to avoid that):
```
& "tes3conv/tes3conv.exe" "R3 - Magic.json" "R3 - Magic.new.esp"
```

Then overwrite the original ESP in place using WriteAllBytes (preserves git tracking), and clean up:
```
$b = "c:\Users\rafal\OneDrive\OMEN\Morrowind\MO2\mods\Remastered Rebalance Redux"
[System.IO.File]::WriteAllBytes("$b\R3 - Magic.esp", [System.IO.File]::ReadAllBytes("$b\R3 - Magic.new.esp"))
Remove-Item "$b\R3 - Magic.new.esp"
```

Use the matching filenames for whichever ESP was modified (Core, Magic, Races & Birthsigns, or optional files).

## Notes
- Never modify files inside `tes3conv/` — those are read-only vanilla references.
- README, JSON, and ESP must always be updated together.

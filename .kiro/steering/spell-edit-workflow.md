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
- Anything after the values (notes, flags) goes in a comment at the end of the line: `50/10s               used by Aryon`
- The `->` means: left side is the vanilla/default value, right side is the new target value

## 2. JSON update
Find the spell entry in the relevant ESP JSON (e.g. `R3 - Magic.json`).

- If the spell **already exists** in the ESP JSON: update `min_magnitude`, `max_magnitude`, `duration`, `area` as needed.
- If the spell **does not exist** in the ESP JSON: copy the full entry from the appropriate default reference JSON in `tes3conv/` (Morrowind.json, Tribunal.json, Bloodmoon.json, or Tamriel_Data.json), then apply the new values.

## JSON value scaling
The user will specify the scale to use each time. Wait for the user to provide the scale before writing JSON values.

The scale is applied to the **vanilla default values** (left of `->` in README) to produce the new values:
- `new_magnitude = vanilla_magnitude × scale_mag`
- `new_duration = vanilla_duration × scale_dur`

The JSON and README store the same new values — no conversion needed between them.

## Notes
- Never modify files inside `tes3conv/` — those are read-only vanilla references.
- Both README and JSON must always be updated together.

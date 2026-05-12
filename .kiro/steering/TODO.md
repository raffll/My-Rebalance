# TODO

## Creatures Magicka
Copy creature entries from default and modify their magicka values.

Creatures to copy and modify:
- `atronach_flame` — Flame Atronach (Morrowind.json)
- `atronach_flame_az` — Flame Atronach (Morrowind.json)
- `atronach_flame_summon` — Flame Atronach (Morrowind.json)
- `atronach_flame_ttmk` — Flame Atronach (Morrowind.json)
- Frost Atronachs — find IDs in Morrowind.json
- `ascended_sleeper` — Ascended Sleeper (Morrowind.json), current magicka: 300
- Hungers — find IDs in Morrowind.json
- Scribs — find IDs in Morrowind.json

Target magicka values: TBD

## Optional Files — Review
- `sMagicInsufficientCharge` stored as Float in JSON — should be String `""`, verify tes3conv handles it correctly
- **Morag Tong Polished**: no README entry in `optional/README - Optional.md` — add one
- **Morag Tong Polished**: script hardcodes `murdercost = -5200` — needs adjustment to match current crime values in R3 - Core
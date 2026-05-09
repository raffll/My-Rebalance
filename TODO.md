# TODO

## Starting Spells
Remove `PC_START_SPELL` from old spells, add to new spells.

| Old (remove flag) | New (add flag) |
|---|---|
| `shield` | `first barrier` ✓ already has flag |
| `exhausting touch` | `weariness` — copy from vanilla, add flag |
| `detect_creature` | `detect enchantment` |
| `feet of notorgo` | `skylamp's shadow` |

- `weariness` not yet in R3 - Magic.json — copy from Morrowind.json
- `feet of notorgo` not yet in R3 - Magic.json — copy from Morrowind.json (just to remove flag)
- `detect_creature` not yet in R3 - Magic.json — copy from Morrowind.json (just to remove flag)

---

## Creatures Magicka
Copy creature entries from default and modify their magicka values.

Creatures to copy and modify:
- `atronach_flame` — Flame Atronach (Morrowind.json)
- `atronach_flame_az` — Flame Atronach (Morrowind.json)
- `atronach_flame_summon` — Flame Atronach (Morrowind.json)
- `atronach_flame_ttmk` — Flame Atronach (Morrowind.json)
- Frost Atronachs — find IDs in Morrowind.json
- `ascended_sleeper` — Ascended Sleeper (Morrowind.json), current magicka: 300

Target magicka values: TBD

---

## Fortify Skill — Masterful Spells
All 28 Masterful spells are documented in README - Magic.md.
Current vanilla values: 15/60s each.
Target values: TBD — decide new magnitude/duration.
Copy all from Morrowind.json and add to R3 - Magic.json once values are decided.

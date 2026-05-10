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

---

## Fortify Skill — Masterful Spells
All 28 Masterful spells documented in README - Magic.md as one entry: `Masterful... 15/60s -> 15/15s`.
All 28 copied from Morrowind.json into R3 - Magic.json with `duration: 15`. ✓

---

## Sound Spells — Flatten & Fix Range
Flatten min/max to single values and make all OnTarget (Noise and Cruel Noise are currently OnTouch).

| Spell | Current | Proposed |
|---|---|---|
| Earwig | 9-24/20s | 15/20s |
| Cruel Earwig | 15-33/20s | 25/20s |
| Dire Earwig | 24-45/20s | 35/20s |
| Wild Earwig | 3-90/20s | 50/20s |
| Noise | 3-8/60s | 5/60s |
| Cruel Noise | 10-22/60s | 15/60s |
| Dire Noise | 2-60/60s | 30/60s |

---

## Optional Files — Review
- `sMagicInsufficientCharge` stored as Float in JSON — should be String `""`, verify tes3conv handles it correctly
- **Morag Tong Polished**: no README entry in `optional/README - Optional.md` — add one
- **Morag Tong Polished**: script hardcodes `murdercost = -5200` — needs adjustment to match current crime values in R3 - Core

---

## Mages Guild — Attribute Requirements
In README - Factions.md, update attribute columns (Int/Wil) to increment by 5 per rank starting at 30:
30, 35, 40, 45, 50, 55, 60, 65, 70, 75

Also create R3 - Factions.json with the Mages Guild entry copied from tes3conv/TR_Factions.json, applying the new attribute values.

---

## Scrib Paralysis — Duration
Change `scrib_paralysis` duration from 6s to 12s in R3 - Magic.json.
Update README entry: `6s [auto -> 6] -> 12s [auto -> 12]`.

---

## Paralyze Spells — Split Entry
In README - Magic.md, under `### Paralyze`, replace the single `Paralysis` entry with two separate lines:
- `paralysis` — revert to vanilla (5s, cost auto). Remove from R3 - Magic.json entirely (or keep with vanilla values if already present).
- `scrib_paralysis` — keep as-is (6s, cost 6). Add ID comment `[scrib_paralysis]` since both share the name "Paralysis".

README result should look like:
```
Paralysis                                   5s                              used by players/merchants
Paralysis                                   6s [auto -> 6]                  used by Scribs [scrib_paralysis]
```

JSON: remove `paralysis` entry from R3 - Magic.json (revert to vanilla). Keep `scrib_paralysis` entry unchanged.

---

## Masterful Spells — In-Game Verification
Verify all 28 Masterful spells appear correctly in-game with the new duration (15s) and that costs feel right at base cost ×4.

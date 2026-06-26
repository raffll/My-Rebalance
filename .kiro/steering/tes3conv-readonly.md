# tes3conv JSON Files — Read Only

The JSON files inside the `tes3conv/` folder are **default/vanilla reference files** and must **never be modified**.

These files are:
- `tes3conv/Morrowind.json`
- `tes3conv/Tribunal.json`
- `tes3conv/Bloodmoon.json`
- `tes3conv/Tamriel_Data.json`
- `tes3conv/Patch for Purists.json`

They serve as the source of truth for original game data. All edits must be made to the ESP-derived JSON files in the workspace root or `optional/` folder, never to these reference files.

## Reference Docs

When looking up vanilla spell data, check `docs/` reference files **first** before searching the large JSON files:
- `docs/Vanilla-Alteration-Spells.md`
- `docs/Vanilla-Conjuration-Spells.md`
- `docs/Vanilla-Destruction-Spells.md`
- `docs/Vanilla-Illusion-Spells.md`
- `docs/Vanilla-Mysticism-Spells.md`
- `docs/Vanilla-Restoration-Spells.md`
- `docs/Vanilla-Potions-Reference.md`
- `docs/Vanilla-Scrolls-Reference.md`
- `docs/Vanilla-Summon-Reference.md`
- `docs/TD-Destruction-Spells-Analysis.md`
- `docs/TD-Potions-Reference.md`

Only fall back to the tes3conv JSON files when the docs don't cover the needed data.

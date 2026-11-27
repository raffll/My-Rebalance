# Remastered Rebalance Redux — Mod Rules

Project rules for R3 (OpenMW). Plugin-specific math lives in
`spell-conversion-rules.md` and `spell-rounding-rules.md`.

## 1. Layout

| Path                   | Contents                                                                            |
|------------------------|-------------------------------------------------------------------------------------|
| root                   | plugins: `R3 - *.omwscripts` (+ `.omwscripts.esp` MO2 stub), `R3 - *.esp` + `.json` |
| `optional/`            | optional ESP plugins + JSON                                                         |
| `scripts/R3<Name>Lua/` | Lua plugin code and data (OpenMW loads Lua from `scripts/`)                         |
| `l10n/R3Core/`         | menu text for the Core settings page                                                |
| `tools/`               | Python generators, checks and build scripts                                         |
| `docs/`                | every README (`R3 - *.md`); generated analysis docs are not committed               |
| `.kiro/steering/`      | these rules                                                                         |

Never put Python or other non-Lua files under `scripts/`.

## 2. Plugins

### Lua plugins (preferred)

`R3 - Core`, `R3 - Spells`, `R3 - Rounding`, `R3 - Potions`. Use Lua for any
change the OpenMW Lua content API can make (`openmw.content`: game settings,
skills, magic effects, spells, enchantments, potions, books, apparatus, ...).

- One `LOAD:` script per plugin, working in `onContentFilesLoaded`. A plugin is
  on when its `.omwscripts` is enabled. The only settings are the Core menu options
  (spell effect base costs, movement speed, merchant gold reset, hidden
  "not enough charge" message; `R3CoreLua/menu.lua`, read by `load.lua` from
  `storage.playerSection`; applies after a restart).
- **Dynamic** plugins (Spells, Rounding, Potions) read the base costs and
  records from the game, never from another R3 plugin's files. They must work
  with R3 - Core enabled or not (vanilla base costs then); a missing plugin
  must never break them. Spells and Potions need Core listed before them and
  log a warning otherwise.
- **Absolute** plugin (Core) sets the R3 value outright, including all spell
  effect base costs (`R3CoreLua/data.lua`, `EFFECTS`).
- Wrap each record change in `pcall`, count results, and end with one log line
  `[R3 - <Name>] ...` (applied / renamed / failed).
- Record ids are lowercase in data tables; ranges use `content.RANGE`.
- Data files: hand-maintained (`R3CoreLua/data.lua`, `R3SpellsLua/vanilla.lua`,
  `names.lua`) or generated (`spells.lua` by `tools/gen_spells.py`; never edit
  generated files by hand).
- Check every Lua file with `luac -p` before finishing.

### ESP plugins

`optional/*` and `R3 - Core.esp` for the records Lua cannot reach (creatures,
NPCs, scripts, dialogue). New changes go to Lua when possible. Enchantments,
Creatures, Factions and Races & Birthsigns are removed until ported to Lua; see
`docs/TODO.md`.

- Edit the JSON (root or `optional/`), then build: `python tools/build_esps.py`
  (tes3conv `"in.json" "out.esp" --overwrite`).
- JSON must be UTF-8 without BOM (tes3conv rejects a BOM).
- Masters: only what the records need. Plugins must load on vanilla Morrowind +
  Tribunal + Bloodmoon unless they change Tamriel Data records.

### Record integrity

- Never change a record `id`; only `name` and data fields.
- Never add records that do not exist in vanilla or Tamriel Data.
- Tamriel Data spells in an ESP must not use `AUTO_CALCULATE`: set
  `"flags": ""` and an explicit `"cost"`.

## 3. READMEs

All READMEs are in `docs/`.

- **Explain what a change does in game**, with the mechanism and formula taken
  from the OpenMW source (`C:\OMEN\Morrowind\sources\openmw`), naming the source
  file in brackets. Never describe a mechanism from memory or assumption.
- **Lua plugin READMEs** are hand-written. Dynamic plugins describe rules, not
  per-record results (results depend on the load order). Core lists its
  absolute values and marks ESP-only records *(ESP)*.
- **Value lists in Lua READMEs mirror the data files**: Core Spell Effect Base Costs
  (`R3CoreLua/data.lua`, with the vanilla value from `R3SpellsLua/vanilla.lua`), Spells and Potions Names (`names.lua`), Core values
  (`R3CoreLua/data.lua`). Update the README in the same change as the data.
- **ESP plugin READMEs** are generated from the JSON by `tools/gen_*.py`
  (`python tools/gen_all.py`); edit the JSON or the generator, not the README.
  Check with `python tools/check_readme_coverage.py`.
- Layout: `# Remastered Rebalance Redux - <Name>`, short intro, sections
  separated by a 60-dash divider, values in code blocks aligned at column 44
  (name at 80), short prose under a block where the effect needs explaining.

### Effect value tokens (generated READMEs)

Rendered as `mag/dur/ft/range [cost]`: magnitude (`n` or `min-max`), `/<n>s`,
`/<n>ft`, `/Touch|/Target|/Self`, cost bracket. In an `A -> B` pair, range, area
and cost are shown on both sides when they differ and on neither when equal;
magnitude and duration are always shown.

## 4. Data Sources

- `C:\OMEN\Morrowind\tes3conv\*.json`: read-only master references. Never edit.
  Full load order, later files win: Morrowind, Tribunal, Bloodmoon, Patch for
  Purists, Tamriel_Data, TR_Mainland, TR_Factions, Cyr_Main, Sky_Main.
  These are the only source for vanilla and Tamriel Data values; do not copy
  them into docs.
- OpenMW source: engine formulas and the Lua API (`apps/openmw/mwlua/`,
  `files/lua_api/`).

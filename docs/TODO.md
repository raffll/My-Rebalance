# Remastered Rebalance Redux - TODO

Four ESP plugins were removed from the mod until they are ported to Lua. Their
JSON and ESP files are in git history (last commit that has them: `3ad4af2`,
branch `3.0`). Their old READMEs, with every value, are kept in `docs/todo/`.
Port each one as a Lua plugin following `.kiro/steering/mod-rules.md`
(one `LOAD:` script, `onContentFilesLoaded`, `pcall` per record, one log line).

Before starting, check each record type against the `openmw.content` API of the
target OpenMW build (`files/lua_api/openmw/content.lua`). The version read when
this was written (master) lists: activators, apparatuses, attributes, books,
classes, doors, enchantments, factions, game settings, globals, ingredients,
levelled lists, lights, lockpicks, magic effects, miscs, potions, probes, races,
repairs, skills, spells, statics, sounds, weathers. It has no creatures, NPCs or
birthsigns.

------------------------------------------------------------

## R3 - Enchantments

19 enchanting records (vanilla and Tamriel Data scrolls and item enchantments)
kept in line with the spell changes (new magnitudes and durations).
Reference: `docs/todo/R3 - Enchantments.md`.

- API: `content.enchantments` exists, so this can be ported now.
- Depends on the spell effect base costs. The values assume the R3 base costs,
  so apply them only when R3 - Core's base cost toggle is on, or better, compute
  them like R3 - Spells does: factor = vanilla base cost / base cost in the game
  (`scripts/R3SpellsLua/vanilla.lua`), so Core off changes nothing.
- Decide: a fixed value table (as the ESP) or a rule (dynamic, covers other
  mods' enchantments like Spells does for buyable spells).
- Tamriel Data records only when Tamriel Data is loaded (skip missing ids).

------------------------------------------------------------

## R3 - Factions

11 factions with changed rank requirements.
Reference: `docs/todo/R3 - Factions.md`.

- API: `content.factions` exists, so this can be ported now.
- Masters in the old ESP: Morrowind, Tribunal, Bloodmoon, Tamriel Data and
  TR Mainland. Skip factions that are not loaded.
- Absolute values, like R3 - Core.

------------------------------------------------------------

## R3 - Creatures

8 creatures with more magicka, so they can cast their spells at the new base
costs (for example the flame and frost atronachs and the Ascended Sleeper).
Reference: `docs/todo/R3 - Creatures.md`.

- API: blocked. `openmw.content` has no creature records. Options: wait for the
  API, or add the values with a local script (not at load time), or keep a
  small ESP for this one.
- Only needed when R3 - Core's base costs are on. If it stays an ESP it cannot
  follow the toggle; a Lua version can.

------------------------------------------------------------

## R3 - Races & Birthsigns

8 races and 10 birthsigns rebalanced, plus 29 new `raffll_*` ability spells.
Reference: `docs/todo/R3 - Races & Birthsigns.md`.

- API: `content.races` and `content.spells` exist; birthsigns do not, so the
  birthsign half is blocked. Check whether race records expose their spell list
  and skill bonuses before starting.
- New spells are records that do not exist in vanilla: the record integrity
  rule in `mod-rules.md` ("never add records that do not exist in vanilla or
  Tamriel Data") needs an exception for them.
- Possible split: races now (Lua), birthsigns later.

------------------------------------------------------------

## Tools and docs when a plugin returns

- Add its section to `docs/README.md` (plugin table) and write the README by
  hand (Lua plugin READMEs are hand-written).
- Remove the matching `docs/todo/` file, and the old generator in `tools/`
  (`gen_enchantments.py`, `gen_factions.py`, `gen_creatures.py`,
  `gen_races.py`) once nothing needs it. They are no longer run by
  `gen_all.py` or checked by `check_readme_coverage.py`.

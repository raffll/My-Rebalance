# Remastered Rebalance Redux

A rebalance of Morrowind for OpenMW. The goal is to make more options worth
using, so specialised characters are fun to play: disable and defence magic
competes with raw damage, stealth and security skills stay useful at high
levels, and crime, money and crafting carry real weight.

The mod is split into small plugins. Each one can be enabled on its own, and
each has its own README in `docs/` with the exact rules and values.

------------------------------------------------------------

## Plugins

| Plugin                       | Type      | What it covers                                                                |
|------------------------------|-----------|-------------------------------------------------------------------------------|
| `R3 - Core`                  | Lua + ESP | game settings and spell effect base costs (menu toggle)                       |
| `R3 - Spells`                | Lua       | buyable spells adjusted to match the effect base costs                        |
| `R3 - Rounding`              | Lua       | tidier spell magnitude ranges                                                 |
| `R3 - Potions`               | Lua       | graded potions set to a consistent tier table                                 |
| `optional/R3 - Optional - *` | ESP       | small standalone tweaks                                                       |

------------------------------------------------------------

## How it works

- **Lua plugins** change records when the game starts, through the OpenMW Lua
  content API. Spells, Rounding and Potions work from whatever the load order
  provides, so other mods' spells and potions are treated by the same rules,
  including Tamriel Data and Tamriel Rebuilt content.
- **ESP plugins** cover records Lua cannot change (creatures, scripts,
  dialogue) and hand-tuned records.
- A plugin is on when it is enabled in the content list. The only settings are
  the R3 - Core options: spell effect base costs, movement speed, merchant
  gold reset and hiding the "not enough charge" message (Options > Scripts).
  Changes apply at startup.

------------------------------------------------------------

## Requirements

- OpenMW with the `openmw.content` Lua package (development builds; written
  against Lua API revision 166). Not for the original Morrowind engine.
- Morrowind, Tribunal and Bloodmoon. Tamriel Data and Tamriel Rebuilt are
  optional.

------------------------------------------------------------

## Installation

Add the mod folder as a data path (or install it with Mod Organizer 2) and
enable the plugins you want. Load `R3 - Core.omwscripts` before
`R3 - Spells.omwscripts` and `R3 - Potions.omwscripts`, so they see the base
costs Core sets. Enable
`R3 - Core.esp` together with `R3 - Core.omwscripts`.

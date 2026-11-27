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
| `R3 - Core`                  | Lua + ESP | game settings: movement, crime, barter, thievery, alchemy, enchanting, skills |
| `R3 - Spells`                | Lua       | spell effect costs, with buyable spells adjusted to match                     |
| `R3 - Rounding`              | Lua       | tidier spell magnitude ranges                                                 |
| `R3 - Potions`               | Lua       | graded potions set to a consistent tier table                                 |
| `R3 - Enchantments`          | ESP       | enchantments and scrolls kept in line with the spell changes                  |
| `R3 - Creatures`             | ESP       | creatures that need more magicka for their spells                             |
| `R3 - Races & Birthsigns`    | ESP       | races and birthsigns rebalanced so every choice is viable                     |
| `R3 - Factions`              | ESP       | faction rank requirements                                                     |
| `optional/R3 - Optional - *` | ESP       | small standalone tweaks                                                       |

------------------------------------------------------------

## How it works

- **Lua plugins** change records when the game starts, through the OpenMW Lua
  content API. Spells, Rounding and Potions work from whatever the load order
  provides, so other mods' spells and potions are treated by the same rules,
  including Tamriel Data and Tamriel Rebuilt content.
- **ESP plugins** cover records Lua cannot change (creatures, scripts,
  dialogue) and hand-tuned records.
- No menus or settings: a plugin is on when it is enabled in the content list.
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
enable the plugins you want. Load `R3 - Spells.omwscripts` before
`R3 - Potions.omwscripts`, so potion tiers use the new spell costs. Enable
`R3 - Core.esp` together with `R3 - Core.omwscripts`.

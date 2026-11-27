# Remastered Rebalance Redux

The idea is to make more options usable, especially for the fun of role-playing more specialized characters. This mod includes changes to spell effects, spells, potions, lockpicking, traps, alchemy, enchanting, and many more!

Every change is listed in detail in the reference files in `docs/` (`R3 - *.md`). This page is just the overview of *what* changed and *why*.

## Core

- **Movement**
  - Walk speed raised 25%.
- **Crime**
  - Much harsher bounties, for a more medieval justice system.
  - Prison time is unchanged.
- **Barter**
  - Merchant gold restocks far more slowly to keep less money on the market.
  - Creeper and Mudcrab no longer carry broken amounts of gold.
- **Pickpocket**
  - 100% max chance and a 300× smaller value penalty.
  - A maxed thief can steal items worth up to ~15,500 gold.
- **Lockpicking**
  - Lockpicking and Open are harder.
  - In vanilla the skill was pointless past 50 and magic trivialized locks.
- **Traps**
  - A real threat again.
  - Vanilla left their cost at 0, so they were free to ignore.
- **Alchemy**
  - Homemade potion strength halved.
  - Secret Master apparatus made rare and expensive.
- **Enchanting**
  - Far more reliable to enchant.
  - Magic items no longer recharge on their own — soul gems required.
- **Skills**
  - Armorer governed by Endurance.
  - Endurance grants less health per level.

Lua plugin plus a small ESP (merchant gold, Morag Tong writs, guard greeting).

Details: `R3 - Core.md`

## Spells & Potions

Lua plugins: they work from the base costs the load order provides, so they
follow other mods.

- **R3 - Spells**: new effect base costs. Balance shifted from damage-dealing to
  disable and defense spells: casters will use Burden, Drain Fatigue and Paralyze
  first, and you can prepare with cheap Resist or Feather.
  - Buyable spells are compensated by duration when the base cost change is a
    whole multiple (base cost /10 -> duration x10) and gives whole seconds.
  - Otherwise the spell keeps its values and its cost follows the new base cost
    (elemental damage, Lock/Open, rounding cases).
  - Old R3 spell names (Shock/Lightning Shield swap, Weak Frost Shield...).
- **R3 - Rounding**: magnitude ranges of buyable spells rounded to 1 or multiples
  of 5.
- **R3 - Potions**: graded potions (Bargain to Exclusive) set to a tier table
  chosen from the effect base cost; Exclusive equals a self-made potion with 100
  Alchemy and mortar quality 1. Old R3 potion names. Multi-effect potions keep
  their values.
- Tamriel Data and Tamriel Rebuilt spells and potions follow the same rules.

Details: `R3 - Spells.md`, `R3 - Rounding.md`, `R3 - Potions.md`

## Enchantments

- Mostly fine-tuned to stay consistent with the reworked spell/effect balance.
- Elemental scroll damage kept close to vanilla (no spell compensation), like spells.

Details: `R3 - Enchantments.md`

## Creatures

- Atronachs and Ascended Sleepers given more magicka to offset the increased cost of their elemental damage spells, so they can still cast as often.

Details: `R3 - Creatures.md`

## Races & Birthsigns

- Every race rebalanced so they are all worth picking — no clearly dominant or weak choice.
- Ability and power kits reworked for stronger, more distinct identity.
- Province-accurate race names (Dunmer, Altmer, Orsimer, Bosmer).

Details: `R3 - Races & Birthsigns.md`

## Factions

- Higher-rank attribute requirements raised slightly, making faction advancement a little more demanding.

Details: `R3 - Factions.md`

## Optional

Separate plugins for standalone tweaks (barter reset delay, charge messagebox, Morag Tong). See `R3 - Optional.md`.

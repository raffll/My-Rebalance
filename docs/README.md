# Remastered Rebalance Redux

The idea is to make more options usable, especially for the fun of role-playing more specialized characters. This mod includes changes to spell effects, spells, potions, lockpicking, traps, alchemy, enchanting, and many more!

Every change is listed in detail in the generated reference files (`R3 - *.md`). This page is just the overview of *what* changed and *why*.

## Core

- **Movement**
  - Base walk speed raised 25%.
- **Crime**
  - Much harsher bounties, for a more realistic medieval-style justice system.
  - The days-in-prison divisor is scaled up to match, so jail time stays the same — only the gold you owe goes up.
- **Barter**
  - Merchant gold restocks far more slowly, keeping less money circulating to fix the economy.
  - Creeper and Mudcrab no longer carry absurd amounts of gold — that broken easter-egg economy is reined in.
- **Pickpocket**
  - Max chance raised to 100% and the item-value penalty cut 300×.
  - A maxed thief (100 Agility/Luck/Sneak) can reliably steal items worth up to ~15,500 gold off an average target.
- **Lockpicking**
  - Harder on purpose: in vanilla, lockpicking skill was pointless past ~50 and the Open spell was so strong that magic trivialized every lock.
  - Both manual lockpicking and the Open effect/spell line are made more demanding, so skill and magic each stay relevant at higher levels.
- **Traps**
  - In vanilla the trap cost multiplier was 0, leaving traps effectively broken and free to ignore.
  - It is now a real penalty, so traps actually threaten the player and disarming matters.
- **Alchemy**
  - Homemade potion strength halved.
  - Secret Master apparatus made rare and expensive.
- **Enchanting**
  - No passive magic-item recharge.
  - Much lower enchant success multiplier — enchanting is a bigger commitment.
- **Skills**
  - Armorer governed by Endurance instead of Strength.
  - Less free health per level from Endurance.

Details: `R3 - Core.md`

## Spells & Potions

- Balance shifted from damage-dealing to disable and defense spells.
- Casters will use Burden, Drain Fatigue, and Paralyze first — you can prepare with cheap Resist or Feather.
- Potions are scaled by a tier system determined by the spell effect's base cost.
- Exclusive potion is equivalent to a self-made potion with 100 Alchemy and mortar quality 1.
- Spells are scaled inversely to base cost changes (base cost ÷2 → spell mag×dur ×2).
- Exceptions to spell scaling:
  - Duplicate spells (consolidated or removed).
  - Spells that are too powerful or too weak for their tier.
- Elemental damage (Fire, Frost, Shock, Poison) does not get spell compensation — base cost change affects cost directly.
- All spell magnitudes rounded to multiples of 5 (minimum floor is 1).
- Tamriel Data spells and potions follow the same rules.

### Potion Tiers

Potion magnitude/duration is set by a tier, chosen from the effect's R3 base cost
(the column headers). Vanilla potion values are tier 1 (base cost 1); a higher or
lower base cost shifts the potion up or down the table. Base cost above 8 uses tier 8.
Duration-only effects (Paralyze, Silence) use the duration column of the matching tier.

| Mag | Dur |  8  |  5  |  2  |  1  | 0.5 | 0.2 | 0.1 |
|----:|----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|   1 |   3 |  ●  |     |     |     |     |     |     |
|   2 |   6 |  ●  |  ●  |     |     |     |     |     |
|   3 |   9 |  ●  |  ●  |  ●  |     |     |     |     |
|   4 |  12 |  ●  |  ●  |  ●  |     |     |     |     |
|   6 |  18 |  ●  |  ●  |  ●  |  ●  |     |     |     |
|   8 |  24 |     |  ●  |  ●  |  ●  |     |     |     |
|  10 |  30 |     |     |  ●  |  ●  |  ●  |     |     |
|  15 |  45 |     |     |     |  ●  |  ●  |     |     |
|  20 |  60 |     |     |     |  ●  |  ●  |  ●  |     |
|  30 |  90 |     |     |     |     |  ●  |  ●  |     |
|  40 | 120 |     |     |     |     |  ●  |  ●  |     |
|  60 | 180 |     |     |     |     |     |  ●  |  ●  |
|  80 | 240 |     |     |     |     |     |  ●  |  ●  |
| 100 | 300 |     |     |     |     |     |     |  ●  |
| 150 | 450 |     |     |     |     |     |     |  ●  |
| 200 | 600 |     |     |     |     |     |     |  ●  |

Details: `R3 - Spells & Potions.md`

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

Separate plugins for standalone tweaks (barter reset delay, charge messagebox, Morag Tong). See `optional/R3 - Optional.md`.

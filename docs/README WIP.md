# Remastered Rebalance Redux

A rebalance of Morrowind for OpenMW.

------------------------------------------------------------

## R3 - Core.omwscripts

Sets game settings and records at startup. Every change can be turned off in
Options > Scripts > R3 - Core. Restart the game to apply.

### Health

Setting: Slower Health Gain (Yes/No, default Yes).

```
fLevelUpHealthEndMult                       0.1 -> 0.05
```

- Each level-up adds 5% of Endurance to health instead of 10%.

### Skills

Setting: Skill Changes (Yes/No, default Yes).

*Armorer*
```
Governing Attribute                         Strength -> Endurance
Successful Repair                           0.4 -> 1.0
```

- Armorer counts toward Endurance at level-up.
- Repairs train Armorer 2.5 times faster.

*Enchant*
```
Recharge                                    5.0 -> 2.0
```

- Recharging items trains Enchant 2.5 times slower.

### Movement

Setting: Movement Speed (Vanilla, +25% or +50%, default +25%).

```
                                            Vanilla     +25%        +50%
fMinWalkSpeed                               100         125         150
fMaxWalkSpeed                               200         250         300
fMinWalkSpeedCreature                       5           6.25        7.5
fMaxWalkSpeedCreature                       300         375         450
```

- Everyone walks, runs and swims 25% faster. Adjustable in menu: Vanilla, +25%, +50%.

### Barter

Setting: Merchant Gold Reset (Hour, Day or Month, default Month).

```
                                            Hour        Day         Month
fBarterGoldResetDelay                       1           24          720
```

- Merchant gold returns after 30 days instead of 1. Adjustable in menu: Hour, Day, Month.

### Travel

Setting: Pricier Guild Travel (Yes/No, default Yes).

```
fMagesGuildTravel                           10 -> 50
```

- Guild guide travel costs 5 times more.

### Crime

Setting: Harsher Crime (Yes/No, default Yes).

```
iCrimeKilling                               1000 -> 5000
iCrimeAttack                                40 -> 1000
iCrimePickPocket                            25 -> 250
iCrimeTresspass                             5 -> 500
```

- Bounties: murder x5, assault x25, pickpocketing x10, trespassing x100.

```
iDaysinPrisonMod                            100 -> 500
```

- Prison days are unchanged, except assault: 1 -> 2 days.
- Theft: 1 prison day per 500 gold of item value instead of 100.

### Pickpocket

Setting: Easier Pickpocket (Yes/No, default Yes).

```
iPickMaxChance                              75 -> 100
fPickPocketMod                              0.3 -> 0.001
```

- Pickpocket chance cap 100% instead of 75%.
- Item value barely matters: a 100 gold item costs 1% of chance instead of
  300%.

### Lockpicking

Setting: Harder Locks (Yes/No, default Yes).

```
fPickLockMult                               -1 -> -1.25
```

- Each lock level costs 1.25% of chance instead of 1%.

Setting: Open Spell Changes (Yes/No, default Yes).

*Spell Effects*
```
Open                                        6 -> 12
```

*Spell Magnitudes*
```
ondusi's open door                          50 -> 40                            Ondusi's Open Door
strong open                                 50 -> 60                            Strong Open
great open                                  50 -> 80                            Great Open
```

*Scrolls*
```
sc_ondusisunhinging                         73 -> 173                           Scroll of Ondusi's Unhinging
sc_ekashslocksplitter_en                    100 -> 80-100                       Scroll of Ekash's Lock Splitter
```

- Open spells cost twice the magicka and come in three strengths.

### Traps

Setting: Harder Traps (Yes/No, default Yes).

```
fTrapCostMult                               0 -> -0.75
```

*Common Trap Costs*
```
trap_fire00                                 3 -> 8                              Fire Trap
trap_frost00                                3 -> 8                              Frost Trap
trap_shock00                                5 -> 12                             Shock Trap
trap_health00                               8 -> 13                             Lifeforce Trap
trap_poison00                               16 -> 81                            Poison Trap
trap_paralyze00                             13 -> 21                            Paralysis Trap
trap_silence00                              37 -> 61                            Silence Trap
trap_fire_killer                            3 -> 63                             Master Fire Trap
trap_frost_killer                           3 -> 63                             Master Frost Trap
trap_shock_killer                           5 -> 88                             Master Shock Trap
trap_poison_killer                          16 -> 169                           Master Poison Trap
```

- Trap spell cost lowers the disarm chance (0.75 per point), and common trap
  spells cost more.

### Alchemy

Setting: Weaker Potions (Yes/No, default Yes).

```
fPotionStrengthMult                         0.5 -> 0.25
```

- Brewed potions have half the magnitude, duration and value.

Setting: Pricier Master Apparatus (Yes/No, default Yes).

```
apparatus_sm_mortar_01                      6000 -> 30000                       Secret Master's Mortar & Pestle
apparatus_sm_alembic_01                     1600 -> 8000                        Secret Master's Alembic
apparatus_sm_calcinator_01                  3200 -> 16000                       Secret Master's Calcinator
apparatus_sm_retort_01                      1000 -> 5000                        Secret Master's Retort
```

### Enchant

Setting: No Item Recharge (Yes/No, default Yes).

```
fMagicItemRechargePerSecond                 0.05 -> 0
```

- Enchanted items no longer recharge over time.

Setting: Easier Self-Enchanting (Yes/No, default Yes).

```
fEnchantmentChanceMult                      3 -> 0.6
```

- Each enchant point lowers the self-enchant chance by 0.6 instead of 3.

Setting: Hide "Not Enough Charge" (Yes/No, default Yes).

```
sMagicInsufficientCharge                    "Item does not have enough charge." -> ""
```

- No message when an item lacks charge.

### Spell Effect Base Costs

Setting: Rebalanced Spell Costs (Yes/No, default Yes).

```
Absorb Fatigue                              4 -> 6
Absorb Health                               8 -> 16
Burden                                      1 -> 0.1
Charm                                       5 -> 2.5
Damage Attribute                            8 -> 24
Damage Fatigue                              4 -> 2
Damage Magicka                              8 -> 4
Detect Animal                               0.75 -> 0.15
Detect Enchantment                          1 -> 0.2
Detect Key                                  1 -> 0.2
Disintegrate Armor                          6 -> 0.6
Disintegrate Weapon                         6 -> 1.2
Drain Fatigue                               2 -> 0.2
Drain Magicka                               4 -> 0.4
Feather                                     1 -> 0.1
Fire Damage                                 5 -> 8
Fortify Fatigue                             0.5 -> 0.25
Fortify Skill                               1 -> 4
Frost Damage                                5 -> 8
Lock                                        2 -> 24
Open                                        6 -> 12
Paralyze                                    40 -> 80
Poison                                      9 -> 8
Reflect                                     10 -> 2.5
Resist Blight Disease                       5 -> 0.25
Resist Common Disease                       2 -> 0.1
Resist Fire                                 2 -> 0.5
Resist Frost                                2 -> 0.5
Resist Magicka                              2 -> 0.5
Resist Poison                               2 -> 0.5
Resist Shock                                2 -> 0.5
Restore Attribute                           1 -> 8
Restore Fatigue                             1 -> 2.5
Shield                                      2 -> 1
Shock Damage                                7 -> 8
Sound                                       3 -> 1
Spell Absorption                            10 -> 2.5
Swift Swim                                  2 -> 0.5
```

- Spell, scroll and enchantment costs follow the new base costs.

### Magic

Setting: Stronger Elemental Shields (Yes/No, default Yes).

```
fElementalShieldMult                        0.1 -> 1
```

- Elemental shields deal 10 times more damage to attackers.

```
sEffectSlowFall                             SlowFall -> Slowfall
```

------------------------------------------------------------

## R3 - Spells.omwscripts

Converts buyable spells to the effect base costs. Durations
scale with the base cost change when the result is a whole number of seconds.
Stored costs are rescaled by the engine cost formula.

------------------------------------------------------------

## R3 - Rounding.omwscripts

Rounds buyable spell magnitude ranges to 1 or multiples of 5. Stored costs are
rescaled by the engine cost formula.

------------------------------------------------------------

## R3 - Potions.omwscripts

Sets graded potions (Bargain to Exclusive) to a magnitude and duration tier
table. The tier column comes from the effect base cost in the game.

------------------------------------------------------------

## R3 - Crime.esp

```
Guard attack-on-sight bounty                5000 -> 20000
Bounty removed per Morag Tong writ          1080 -> 6000
```
Use together with the Crime settings of R3 - Core.

------------------------------------------------------------

## R3 - Merchants.esp

```
Creeper gold                                5000 -> 500
Mudcrab merchant gold                       10000 -> 1000
```

------------------------------------------------------------

## Load Order

```
R3 - Core.omwscripts
R3 - Spells.omwscripts
R3 - Rounding.omwscripts
R3 - Potions.omwscripts
R3 - Crime.esp
R3 - Merchants.esp
```
- R3 - Spells and R3 - Rounding cover the buyable spells of vanilla, Tamriel
  Data and Tamriel Rebuilt.
- R3 - Potions covers potions with a grade suffix (_b, _c, _s, _q, _e).
- R3 - Spells and R3 - Potions log a warning when R3 - Core loads after them.

------------------------------------------------------------

## Requirements

- OpenMW with the openmw.content Lua package (development builds, written
  against Lua API revision 166). Not for the original Morrowind engine.
- Morrowind, Tribunal and Bloodmoon. Tamriel Data and Tamriel Rebuilt are
  optional.

------------------------------------------------------------

## Installation

Add the mod folder as a data path (or install it with Mod Organizer 2) and
enable the plugins you want, in the load order above.
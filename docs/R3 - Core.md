# Remastered Rebalance Redux - Core

Core game settings and records. `R3 - Core.omwscripts` sets the values at
startup (absolute values, overriding the load order). Records Lua cannot change
stay in `R3 - Core.esp`, marked *(ESP)*: merchant gold, the Morag Tong writ
script and the guard greeting. Enable both. Formulas below are taken from the
OpenMW source (file names in brackets).

------------------------------------------------------------

## Health

```
fLevelUpHealthEndMult                       0.1 -> 0.05
```

Health gained per level = base Endurance x `fLevelUpHealthEndMult`, using
Endurance after that level's increases. Vanilla gives 10% of Endurance per
level, R3 5% (60 Endurance: 6 -> 3 per level). Not retroactive; starting health
((Strength + Endurance) / 2) is unchanged. [`mwmechanics/npcstats.cpp`]

------------------------------------------------------------

## Skills

*Armorer*
```
Governing Attribute                         Strength -> Endurance
Successful Repair                           0.4 -> 1.0
```

- Governing attribute: Armorer increases now count toward the Endurance bonus
  at level-up instead of Strength.
- Successful Repair: skill experience per successful repair with a hammer,
  x2.5. [`mwmechanics/repair.cpp`, `scripts/omw/skillhandlers.lua`]

*Enchant*
```
Recharge                                    5.0 -> 2.0
```

Skill experience per successful soul gem recharge, x0.4.
[`mwmechanics/recharge.cpp`]

------------------------------------------------------------

## Movement

```
fMinWalkSpeed                               100 -> 125
fMaxWalkSpeed                               200 -> 250
fMinWalkSpeedCreature                       5 -> 6.25
fMaxWalkSpeedCreature                       300 -> 375
```

Walk speed = min + Speed / 100 x (max - min). Both ends x1.25, so every NPC,
the player and every creature walk 25% faster at any Speed. Running and
swimming build on walk speed, so they are 25% faster too; levitation speed has
its own settings and is unchanged.
[`mwclass/npc.cpp`, `mwclass/creature.cpp`]

------------------------------------------------------------

## Barter

```
fBarterGoldResetDelay                       24 -> 720
```

Hours before a merchant's gold returns to its base amount: 1 day -> 30 days.
Selling drains merchants for a month. [`mwgui/dialogue.cpp`]

*Merchants Gold (ESP)*
```
scamp_creeper                               5000 -> 500                         Creeper
mudcrab_unique                              10000 -> 1000                       Mudcrab
```

The two richest merchants keep 10% of their gold.

------------------------------------------------------------

## Travel

```
fMagesGuildTravel                           10 -> 50
```

Flat price of guild guide teleport (any travel service in an interior cell),
before followers and the barter adjustment. Silt strider and boat prices
(distance based) are unchanged. [`mwgui/travelwindow.cpp`]

------------------------------------------------------------

## Crime

```
iCrimeKilling                               1000 -> 5000
iCrimeAttack                                40 -> 1000
iCrimePickPocket                            25 -> 250
iCrimeTresspass                             5 -> 500
```

Bounty added per crime: murder x5, assault x25, pickpocketing x10, trespassing
x100. Theft (item value x fCrimeStealing) is unchanged.
[`mwmechanics/mechanicsmanagerimp.cpp`]

```
iDaysinPrisonMod                            100 -> 500
```

Days in prison = bounty / `iDaysinPrisonMod` (at least 1). Bounty 1000:
10 days -> 2 days. With the higher bounties, prison time per crime stays close
to vanilla: one murder is 10 days in both. [`mwworld/worldimp.cpp`]

*Guard Greeting (ESP)*
```
58028831233554797                           5000 -> 20000
```

Guards attack on sight ("You've earned a death warrant...") from crime level
20000 instead of 5000, i.e. after 4 murders instead of 5.

*Morag Tong Writs (ESP)*
```
BILL_MT_calc_legit_kills                    -1080 -> -6000
```

Bounty removed per redeemed Morag Tong writ. The script note says the value
should equal one assault and one murder: R3 1000 + 5000 = 6000.

------------------------------------------------------------

## Pickpocket

```
iPickMaxChance                              75 -> 100
fPickPocketMod                              0.3 -> 0.001
```

Success chance = 2 x thief term - victim term, where each term is
(0.2 Agility + 0.1 Luck + Sneak) x fatigue, and the victim term also adds
10 x `fPickPocketMod` x item value. [`mwmechanics/pickpocket.cpp`]

- `iPickMaxChance`: cap on the chance, 75% -> 100%.
- `fPickPocketMod`: item value penalty, 3 per gold -> 0.01 per gold. A 100 gold
  item costs 1% instead of 300%, so value barely matters.

------------------------------------------------------------

## Lockpicking

```
fPickLockMult                               -1 -> -1.25
```

Chance = (0.2 Agility + 0.1 Luck + Security) x pick quality x fatigue +
`fPickLockMult` x lock level. Each lock level now costs 1.25% instead of 1%;
a level 80 lock: -80 -> -100. [`mwmechanics/security.cpp`]

*Spell Effects*
```
Open                                        6 -> 12
```

Open spells and scrolls cost twice the magicka; enchanting Open costs twice.

*Spell Magnitudes*
```
ondusi's open door                          50 -> 40                            Ondusi's Open Door
strong open                                 50 -> 60                            Strong Open
great open                                  50 -> 80                            Great Open
```

The three vanilla 50-point Open spells become three steps.

*Scrolls*
```
sc_ondusisunhinging                         73 -> 173                           Scroll of Ondusi's Unhinging
sc_ekashslocksplitter_en                    100 -> 80-100                       Scroll of Ekash's Lock Splitter
```

------------------------------------------------------------

## Traps

```
fTrapCostMult                               0 -> -0.75
```

Disarm chance = (0.2 Agility + 0.1 Luck + Security + `fTrapCostMult` x trap
spell cost) x probe quality x fatigue. Vanilla ignores the trap spell; now each
point of trap spell cost lowers the chance by 0.75 before the probe multiplier.
[`mwmechanics/security.cpp`]

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

Stored trap spell costs, which the disarm penalty now reads (Master Fire Trap:
63 x -0.75 = -47 before the probe multiplier).

------------------------------------------------------------

## Alchemy

```
fPotionStrengthMult                         0.5 -> 0.25
```

Brewed potion strength = alchemy factor x mortar quality x
`fPotionStrengthMult`; magnitude and duration are that strength / base cost,
and the potion value follows it. Player-made potions are half as strong and
worth half as much. [`mwmechanics/alchemy.cpp`]

*Apparatus Prices*
```
apparatus_sm_mortar_01                      6000 -> 30000                       Secret Master's Mortar & Pestle
apparatus_sm_alembic_01                     1600 -> 8000                        Secret Master's Alembic
apparatus_sm_calcinator_01                  3200 -> 16000                       Secret Master's Calcinator
apparatus_sm_retort_01                      1000 -> 5000                        Secret Master's Retort
```

Secret Master's apparatus x5.

------------------------------------------------------------

## Enchant

```
fMagicItemRechargePerSecond                 0.05 -> 0
```

Enchanted items no longer recharge over time; only soul gems (or a recharge
service) refill them. [`mwmechanics/recharge.cpp`]

```
fEnchantmentChanceMult                      3 -> 0.6
```

Self-enchant chance = (Enchant - enchant points x `fEnchantmentChanceMult` x
type multiplier x item count + 0.2 Intelligence + 0.1 Luck) x fatigue. Each
enchantment point lowers the chance by 0.6% instead of 3%. Only when enchanting
yourself; enchanter services always succeed.
[`mwmechanics/enchanting.cpp`]

------------------------------------------------------------

## Magic

```
fElementalShieldMult                        0.1 -> 1
```

Damage to an attacker whose weapon, fists or projectile hits someone with Fire,
Frost or Lightning Shield = `fElementalShieldMult` x shield magnitude x (1 - resist),
resist from the attacker's Destruction, Willpower, Luck, fatigue, a random roll
and elemental resistance. Shields hit back 10 times harder. [`mwmechanics/combat.cpp`]

```
sEffectSlowFall                             SlowFall -> Slowfall
```

Effect name spelling.

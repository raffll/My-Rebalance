# Remastered Rebalance Redux - Hand Changes in main

Spell and potion changes in `R3 - Spells.esp` and `R3 - Potions.esp` on the
`main` branch (commit `8af8af0`) that the 3.0 rules do not reproduce. Changes
that R3 - Spells (duration x clean factor), R3 - Rounding (ranges to 1 or
multiples of 5) or `names.lua` already give are left out. Not all of these are
wanted; pick the ones worth porting.

Each entry: main value, then the reasons and, for single-effect spells, what
3.0 gives instead (`3.0: ...`). Values are `magnitude/duration [cost]`.
Generated from main's README and JSON, assuming vanilla base costs
(`scripts/R3SpellsLua/vanilla.lua`) and R3 - Core's Rebalanced Spell Costs on.

Reasons: **not buyable** (not in the 3.0 spell list, so 3.0 leaves it as is),
**hand value** (main's magnitude, duration or range differ from the 3.0 rule),
**multi-effect** (several effects, not compared), **autocalc switch** (3.0 never
changes the flag), **rename** (not in `names.lua`).

------------------------------------------------------------

## Starting Spells

Main swapped four starting spells. 3.0 does not.

```
detect_creature -> detect enchantment       50-150/5s -> 50/10s                 Detect Creature -> Detect Enchantment
exhausting touch -> first barrier           5-20/60s/Touch -> 10/30s/Self       Exhausting Touch -> First Barrier
feet of notorgo -> skylamp's shadow         10/90s -> 5-20/30s                  Feet of Notorgo -> Skylamp's Shadow
shield -> weariness                         5/30s/Self -> 10-100/20s/Target     Shield -> Weariness
```

------------------------------------------------------------

## Spells

### Feather
```
ulms juicedaw's feather                     50/10s -> 50/100s                   Ulms's Juicedaw's Feather -> Ulms' Juicedaw Feather
    rename
```

### Fire Shield
```
strong fire shield                          12/30s -> 15/30s                    Strong Fire Shield
    hand value; 3.0: 12/30s
```

### Frost Shield
```
frost barrier                               3/10s -> 1-10/10s                   Frost Barrier
    hand value; 3.0: 3/10s
frost_shield                                6/30s -> 5/30s                      Frost Shield -> Weak Frost Shield
    hand value; 3.0: 6/30s
strong frost shield                         12/30s -> 15/30s                    Strong Frost Shield
    hand value; 3.0: 12/30s
```

### Lightning Shield
```
strong shock shield                         12/30s -> 15/30s                    Strong Shock Shield
    hand value; 3.0: 12/30s
```

### Shield
```
T_Nor_Alt_TsunsWard                         20/20s -> 40/20s                    Tsun's Ward
    not buyable, hand value; 3.0: 20/20s
T_Com_Alt_ForceWall                         50/5s -> 100/5s                     Force Wall
    hand value; 3.0: 50/10s
```

### Swift Swim
```
buoyancy                                    1/20s -> 20/20s                     Buoyancy
    hand value; 3.0: 1/80s
Swimmer's_Blessing                          5/30s -> 50/30s                     Swimmer's Blessing
    hand value; 3.0: 5/120s
T_Com_Alt_DreughsGrace                      30/20s -> 120/20s                   Dreugh's Grace
    not buyable, hand value; 3.0: 30/20s
```

### Damage Fatigue
```
fleabite                                    1-10/1s -> 1-20/1s                  Fleabite
    hand value; 3.0: 1-10/2s
doze                                        1-20/1s -> 1-40/1s                  Doze
    hand value; 3.0: 1-20/2s
hornhand                                    15-36/1s -> 30-70/1s                Hornhand
    hand value; 3.0: 15-35/2s
```

### Damage Magicka
```
soulpinch                                   1-20/1s -> 1-40/1s                  Soulpinch
    hand value; 3.0: 1-20/2s
```

### Disintegrate Armor
```
disintegrate armor                          6-25/1s -> 60-250/1s                Disintegrate Armor
    hand value; 3.0: 5-25/10s
armor eater                                 10-30/1s -> 200-600/1s              Armor Eater
    hand value; 3.0: 10-30/10s
T_Com_Des_FractureArmor                     100/2s -> 1000/2s                   Fracture Armor
    not buyable, hand value; 3.0: 100/2s
```

### Disintegrate Weapon
```
disintegrate weapon                         6-25/1s -> 30-125/1s                Disintegrate Weapon
    hand value; 3.0: 5-25/5s
weapon eater                                6-25/1s -> 100-300/1s               Weapon Eater
    hand value; 3.0: 5-25/5s
T_Rea_Des_IronEater                         1-25/2s -> 5-125/2s                 Iron Eater
    hand value; 3.0: 1-25/10s
T_Rea_Des_SteelEater                        5-30/3s -> 25-150/3s                Steel Eater
    not buyable, hand value; 3.0: 5-30/3s
```

### Drain Fatigue
```
weariness                                   1-10/1s -> 10-100/20s               Weariness
    not buyable, hand value; 3.0: 1-10/1s
sleep                                       5-15/30s -> 25-75/60s               Sleep
    hand value; 3.0: 5-15/300s
wild exhaustion                             5-15/60s -> 25-75/120s              Wild Exhaustion
    hand value; 3.0: 5-15/600s
wearying touch                              5-20/30s -> 25-100/60s              Wearying Touch
    hand value; 3.0: 5-20/300s
exhausting touch                            5-20/60s -> 25-100/120s             Exhausting Touch
    hand value; 3.0: 5-20/600s
ordeal of st. olms                          5-20/60s -> 50-200/60s              Ordeal of St. Olms
    hand value; 3.0: 5-20/600s
exhaustion                                  5-20/90s -> 25-100/180s             Exhaustion
    not buyable, hand value; 3.0: 5-20/90s
dagoth's bosom                              20/30s -> 200/30s                   Dagoth's Bosom
    not buyable, hand value; 3.0: 20/30s
T_Com_Des_Duck                              200/2s -> 2000/2s                   Duck
    not buyable, hand value; 3.0: 200/2s
```

### Drain Health
```
ash feast                                   3/30s -> 30/3s                      Ash Feast
    hand value; 3.0: 3/30s
```

### Drain Magicka
```
magicka leech                               6-15/60s -> 5-15/60s                Magicka Leech
    hand value; 3.0: 5-15/600s
T_Com_Des_RageOfMagnus                      60/10s -> 300/20s                   Rage of Magnus
    not buyable, hand value; 3.0: 60/10s
```

### Shock Damage
```
shockball                                   2-40/1s -> 1-20/1s                  Shockball
    hand value; 3.0: 1-40/1s
```

### Blind
```
crying eye                                  1-10/5s -> 1-10/20s                 Crying Eye
    hand value; 3.0: 1-10/5s
erelvam's wild sty                          1-40/10s -> 1-40/20s                Erelvam's Wild Sty
    hand value; 3.0: 1-40/10s
```

### Chameleon
```
shadow form                                 6-15/30s -> 10-30/30s               Shadow Form
    hand value; 3.0: 5-15/30s
```

### Invisibility
```
invisibility                                30s -> 60s                          Invisibility
    hand value; 3.0: 30s
```

### Paralyze
```
scrib_paralysis                             6s -> 12s [auto -> 6]               Paralysis
    not buyable, hand value, autocalc switch; 3.0: 6s
```

### Sanctuary
```
sotha's grace                               1-20/5s -> 1-20/10s                 Sotha's Grace
    hand value; 3.0: 1-20/5s
father's hand                               1-40/5s -> 1-40/10s                 Father's Hand
    hand value; 3.0: 1-40/5s
```

### Sound
```
wild earwig                                 1-30/5s -> 1-90/5s                  Wild Earwig
    hand value; 3.0: 1-30/15s
earwig                                      3-8/5s -> 10-25/5s                  Earwig
    hand value; 3.0: 5-10/15s
noise                                       3-8/5s -> 1-10/15s                  Noise
    hand value; 3.0: 5-10/15s
cruel earwig                                5-11/5s -> 15-35/5s                 Cruel Earwig
    not buyable, hand value; 3.0: 5-11/5s
dire earwig                                 8-15/5s -> 25-45/5s                 Dire Earwig
    hand value; 3.0: 10-15/15s
T_Com_Ilu_Voices                            50/20s -> 50/60s [100 -> 50]        Voices
    not buyable, hand value; 3.0: 50/20s
```

### Absorb Attribute
```
absorb intelligence [ranged]                5-51/30s -> 5-50/30s                Absorb Intelligence [Ranged]
    not buyable, hand value; 3.0: 5-51/30s
```

### Absorb Fatigue
```
absorb fatigue                              5-20/30s -> 5-20/3s                 Absorb Fatigue
    hand value; 3.0: 5-20/30s
absorb fatigue [ranged]                     5-20/30s -> 5-20/3s                 Absorb Fatigue [Ranged]
    hand value; 3.0: 5-20/30s
energy leech                                5-20/30s -> 5-20/6s                 Energy Leech
    hand value; 3.0: 5-20/30s
Tap Energy                                  20/30s -> 20/3s                     Tap Energy
    not buyable, hand value; 3.0: 20/30s
```

### Detect Enchantment
```
detect enchantment                          10/10s -> 50/10s                    Detect Enchantment
    hand value; 3.0: 10/50s
```

### Detect Key
```
tevral's hawkshaw                           10/10s -> 50/10s                    Tevral's Hawkshaw
    hand value; 3.0: 10/50s
detect_key                                  50/5s -> 250/5s                     Detect Key
    hand value; 3.0: 50/25s
```

### Reflect
```
T_Imp_Res_SothasMirror                      10/5s -> 40/5s                      St. Naharine's Shield
    hand value; 3.0: 10/20s
T_Com_Mys_DistortedReflect                  20/15s -> 40/30s                    Distorted Reflection
    not buyable, hand value; 3.0: 20/15s
```

### Spell Absorption
```
vivec's feast                               10/5s -> 10/40s                     Vivec's Feast
    hand value; 3.0: 10/20s
T_Imp_Mys_VivecsFeast                       10/5s -> 40/5s                      St. Horuscia's Alms
    hand value; 3.0: 10/20s
```

### Fortify Fatigue
```
vigor                                       5-20/30s -> 10-40/30s               Vigor
    hand value; 3.0: 5-20/60s
```

### Fortify Skill
```
masterful balanced armor                    15/60s -> 15/15s                    Masterful Balanced Armor
    not buyable, hand value; 3.0: 15/60s
masterful deep biting                       15/60s -> 15/15s                    Masterful Deep Biting
    not buyable, hand value; 3.0: 15/60s
masterful denial                            15/60s -> 15/15s                    Masterful Denial
    not buyable, hand value; 3.0: 15/60s
masterful enterprise                        15/60s -> 15/15s                    Masterful Enterprise
    not buyable, hand value; 3.0: 15/60s
masterful fleetness                         15/60s -> 15/15s                    Masterful Fleetness
    not buyable, hand value; 3.0: 15/60s
masterful glib speech                       15/60s -> 15/15s                    Masterful Glib Speech
    not buyable, hand value; 3.0: 15/60s
masterful hewing                            15/60s -> 15/15s                    Masterful Hewing
    not buyable, hand value; 3.0: 15/60s
masterful horny fist                        15/60s -> 15/15s                    Masterful Horny Fist
    not buyable, hand value; 3.0: 15/60s
masterful impaling thrust                   15/60s -> 15/15s                    Masterful Impaling Thrust
    not buyable, hand value; 3.0: 15/60s
masterful leaping                           15/60s -> 15/15s                    Masterful Leaping
    not buyable, hand value; 3.0: 15/60s
masterful martial craft                     15/60s -> 15/15s                    Masterful Martial Craft
    not buyable, hand value; 3.0: 15/60s
masterful nimble armor                      15/60s -> 15/15s                    Masterful Nimble Armor
    not buyable, hand value; 3.0: 15/60s
masterful safekeeping                       15/60s -> 15/15s                    Masterful Safekeeping
    not buyable, hand value; 3.0: 15/60s
masterful smiting                           15/60s -> 15/15s                    Masterful Smiting
    not buyable, hand value; 3.0: 15/60s
masterful stalking                          15/60s -> 15/15s                    Masterful Stalking
    not buyable, hand value; 3.0: 15/60s
masteful stolid armor                       15/60s -> 15/15s                    Masterful Stolid Armor
    not buyable, hand value; 3.0: 15/60s
masterful stolid armor                      15/60s -> 15/15s                    Masterful Stolid Armor
    not buyable, hand value; 3.0: 15/60s
masterful sureflight                        15/60s -> 15/15s                    Masterful Sureflight
    not buyable, hand value; 3.0: 15/60s
masterful swiftblade                        15/60s -> 15/15s                    Masterful Swiftblade
    not buyable, hand value; 3.0: 15/60s
masterful transcendant wisdom               15/60s -> 15/15s                    Masterful Transcendant Wisdom -> Masterful Transcendent Wisdom
    rename
masterful transfiguring wisdom              15/60s -> 15/15s                    Masterful Transfiguring Wisdom
    not buyable, hand value; 3.0: 15/60s
```

### Resist Blight Disease
```
poet's whim                                 1-30/10s -> 1-30/200s [auto -> 39]  Poet's Whim
    autocalc switch
vivec's mercy                               20/10s -> 50/80s [auto -> 50]       Vivec's Mercy
    hand value, autocalc switch; 3.0: 20/200s
shield of the armiger                       30/10s -> 100/60s [auto -> 75]      Shield of the Armiger
    hand value, autocalc switch; 3.0: 30/200s
```

### Resist Common Disease
```
variable resist common disease              1-30/10s -> 1-30/200s [auto -> 16]  Variable Resist Common Disease
    autocalc switch
resist common disease                       10/5s -> 50/20s [auto -> 5]         Resist Common Disease
    hand value, autocalc switch; 3.0: 10/100s
seryn's blessing                            20/10s -> 50/80s [auto -> 20]       Seryn's Blessing
    hand value, autocalc switch; 3.0: 20/200s
great resist common disease                 30/10s -> 100/60s [auto -> 30]      Great Resist Common Disease
    hand value, autocalc switch; 3.0: 30/200s
T_Imp_Res_SerynsBlessing                    20/10s -> 100/40s                   Pilgrimage of St. Rosunius
    hand value; 3.0: 20/200s
```

### Resist Frost
```
T_Nor_Res_WinteryMantle                     20/60s -> 80/60s                    Wintery Mantle
    not buyable, hand value; 3.0: 20/60s
```

### Resist Paralysis
```
resist paralysis                            50/30s [300 -> auto]                Resist Paralysis
    autocalc switch
```

### Restore Attribute
```
restore agility                             5-20/30s -> 5-20/4s                 Restore Agility
    hand value; 3.0: 5-20/30s
restore endurance                           5-20/30s -> 5-20/4s                 Restore Endurance
    hand value; 3.0: 5-20/30s
restore intelligence                        5-20/30s -> 5-20/4s                 Restore Intelligence
    hand value; 3.0: 5-20/30s
restore luck                                5-20/30s -> 5-20/4s                 Restore Luck
    hand value; 3.0: 5-20/30s
restore personality                         5-20/30s -> 5-20/4s                 Restore Personality
    hand value; 3.0: 5-20/30s
restore speed                               5-20/30s -> 5-20/4s                 Restore Speed
    hand value; 3.0: 5-20/30s
restore strength                            5-20/30s -> 5-20/4s                 Restore Strength
    hand value; 3.0: 5-20/30s
restore willpower                           5-20/30s -> 5-20/4s                 Restore Willpower
    hand value; 3.0: 5-20/30s
```

### Restore Fatigue
```
rest of st. merris                          1-10/20s -> 1-10/8s                 Rest of St. Merris -> Rest of St. Meris
    hand value, rename; 3.0: 1-10/20s
stamina                                     10-30/30s -> 10-30/12s              Stamina
    hand value; 3.0: 10-30/30s
T_Com_Res_WeaponResartus                    42-78/30s -> 40-80/12s              Greater Stamina
    hand value; 3.0: 40-80/30s
```

### Multi-Effect Spells
```
bm_draugr_curse                             [200 -> auto]                       Eddard's Wrath
    not buyable, autocalc switch
```

------------------------------------------------------------

## Multi-Effect Potions

Main tiered these by hand; the 3.0 tier rule skips potions with more than one
effect.

*Vanilla*
```
p_drain_agility_q                                                               Spoiled SlowFall Potion -> Spoiled Slowfall Potion
    Drain Attribute: Agility                15/40s
    SlowFall                                1/15s
p_drain_endurance_q                                                             Spoiled SlowFall Potion -> Spoiled Slowfall Potion
    Drain Attribute: Endurance              15/40s
    SlowFall                                10/15s -> 1/15s
```

*Tamriel Data*
```
T_Com_Potion_FortifyCasting_B                                                   Bargain Fortify Casting
    Fortify Skill: Alteration               5/8s -> 6/18s
    Fortify Skill: Conjuration              5/8s -> 6/18s
    Fortify Skill: Destruction              5/8s -> 6/18s
    Fortify Skill: Illusion                 5/8s -> 6/18s
    Fortify Skill: Mysticism                5/8s -> 6/18s
    Fortify Skill: Restoration              5/8s -> 6/18s
T_Com_Potion_FortifyCasting_C                                                   Cheap Fortify Casting
    Fortify Skill: Alteration               8/15s -> 8/24s
    Fortify Skill: Conjuration              8/15s -> 8/24s
    Fortify Skill: Destruction              8/15s -> 8/24s
    Fortify Skill: Illusion                 8/15s -> 8/24s
    Fortify Skill: Mysticism                8/15s -> 8/24s
    Fortify Skill: Restoration              8/15s -> 8/24s
T_Nor_Potion_DrainAgility_Q                                                     Spoiled SlowFall Potion -> Spoiled Slowfall Potion
    Drain Attribute: Agility                15/40s
    SlowFall                                1/15s
T_Nor_Potion_DrainEndurance_Q                                                   Spoiled SlowFall Potion -> Spoiled Slowfall Potion
    Drain Attribute: Endurance              15/40s
    SlowFall                                10/15s -> 1/15s
```

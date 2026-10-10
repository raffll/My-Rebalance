# Remastered Rebalance Redux - Spells (Explained)

Generated companion to `R3 - Spells.md`. Same layout, with an extra
explanation column noting which rule produced each change. Only spells
that differ from vanilla are listed. Rules: see
`docs/Spell-Rules-Reference.md`. Do not hand-edit; regenerate with
`python scripts/gen_spells_explained.py`.

------------------------------------------------------------

## Alteration

------------------------------------------------------------

### Burden

```
Base Cost                                   1.0 -> 0.1
```

```
burden                                      20/10s -> 20/100s                   Burden                                                                mag x1, dur x10 = x10 compensated ✓
burden touch                                20/10s -> 20/100s                   Burden Touch                                                          mag x1, dur x10 = x10 compensated ✓
weary                                       30-60/10s -> 30-60/100s             Weary                                                                 mag x1, dur x10 = x10 compensated ✓
great burden of sin                         40/10s -> 40/100s                   Great Burden of Sin -> Burden of Sin                                  mag x1, dur x10 = x10 compensated ✓; renamed
heavy burden                                40/10s -> 40/100s                   Heavy Burden                                                          mag x1, dur x10 = x10 compensated ✓
heavy burden touch                          40/10s -> 40/100s                   Heavy Burden Touch                                                    mag x1, dur x10 = x10 compensated ✓
burden of sin                               40-60/20s -> 40-60/200s             Burden of Sin -> Great Burden of Sin                                  mag x1, dur x10 = x10 compensated ✓; renamed
cruel weary                                 50-70/10s -> 50-70/100s             Cruel Weary                                                           mag x1, dur x10 = x10 compensated ✓
crushing burden                             60/10s -> 60/100s                   Crushing Burden                                                       mag x1, dur x10 = x10 compensated ✓
crushing burden touch                       60/10s -> 60/100s                   Crushing Burden Touch                                                 mag x1, dur x10 = x10 compensated ✓
crushing burden of sin                      60-80/30s -> 60-80/300s             Crushing Burden of Sin                                                mag x1, dur x10 = x10 compensated ✓
dire weary                                  60-90/10s -> 60-90/100s             Dire Weary                                                            mag x1, dur x10 = x10 compensated ✓
```

*Tamriel Data*
```
T_Com_Alt_WeightOfGuilt                     500/3s -> 500/30s                   Weight of Guilt                                                       mag x1, dur x10 = x10 compensated ✓
```

------------------------------------------------------------

### Feather

```
Base Cost                                   1.0 -> 0.1
```

```
feather                                     20/10s -> 20/100s                   Feather                                                               mag x1, dur x10 = x10 compensated ✓
strong feather                              50/10s -> 50/100s                   Strong Feather                                                        mag x1, dur x10 = x10 compensated ✓
ulms juicedaw's feather                     50/10s -> 50/100s                   Ulms's Juicedaw's Feather -> Ulms' Juicedaw Feather                   mag x1, dur x10 = x10 compensated ✓; renamed
great feather                               100/10s -> 100/100s                 Great Feather                                                         mag x1, dur x10 = x10 compensated ✓
```

*Tamriel Data*
```
T_Imp_Alt_UlmsJuicedawsFeather              50/10s -> 50/100s                   Zenithar's Arms                                                       mag x1, dur x10 = x10 compensated ✓
T_Com_Alt_Fling                             500/3s -> 500/30s                   Fling                                                                 mag x1, dur x10 = x10 compensated ✓
```

------------------------------------------------------------

### Fire Shield

```
fire_fathasa_unique                         1-10/10s                            Fire Barrier -> Fathasa's Fire Barrier                                renamed
fierce fire shield                          5-11/10s -> 5-10/10s                Fierce Fire Shield                                                    rounded
strong fire shield                          12/30s -> 15/30s                    Strong Fire Shield                                                    rescaled mag x1
```

------------------------------------------------------------

### Frost Shield

```
frost barrier                               3/10s -> 1-10/10s                   Frost Barrier                                                         rescaled mag x2
fierce frost shield                         5-11/10s -> 5-10/10s                Fierce Frost Shield                                                   rounded
frost_shield                                6/30s -> 5/30s                      Frost Shield -> Weak Frost Shield                                     rounded; renamed
strong frost shield                         12/30s -> 15/30s                    Strong Frost Shield                                                   rescaled mag x1
```

------------------------------------------------------------

### Lightning Shield

```
shock shield                                3/20s                               Shock Shield -> Lightning Shield                                      renamed
fierce shock shield                         5-11/10s -> 5-10/10s                Fierce Shock Shield                                                   rounded
lightning shield                            10/30s                              Lightning Shield -> Shock Shield                                      renamed
strong shock shield                         12/30s -> 15/30s                    Strong Shock Shield                                                   rescaled mag x1
```

------------------------------------------------------------

### Lock

```
Base Cost                                   2.0 -> 24.0
```

*Tamriel Data*
```
T_Com_Alt_WizardLock                        20 [2 -> 24]                        Wizard Lock                                                           mag/dur held; cost x12 compensated via cost ✓
T_Com_Alt_DalgorsEntwining                  100 [8 -> 96]                       Dalgor's Entwining                                                    mag/dur held; cost x12 compensated via cost ✓
```

------------------------------------------------------------

### Shield

```
Base Cost                                   2.0 -> 1.0
```

*Tamriel Data*
```
T_Nor_Alt_TsunsWard                         20/20s -> 40/20s                    Tsun's Ward                                                           mag x2, dur x1 = x2 compensated ✓
T_Com_Alt_ForceWall                         50/5s -> 100/5s                     Force Wall                                                            mag x2, dur x1 = x2 compensated ✓
```

------------------------------------------------------------

### Swift Swim

```
Base Cost                                   2.0 -> 0.5
```

```
buoyancy                                    1/20s -> 20/20s                     Buoyancy                                                              mag x20, dur x1 = x20 ✗ (expected x4)
Swimmer's_Blessing                          5/30s -> 50/30s                     Swimmer's Blessing                                                    mag x10, dur x1 = x10 ✗ (expected x4)
```

*Tamriel Data*
```
T_Com_Alt_DreughsGrace                      30/20s -> 120/20s                   Dreugh's Grace                                                        mag x4, dur x1 = x4 compensated ✓
```

------------------------------------------------------------

## Destruction

------------------------------------------------------------

### Damage Fatigue

```
Base Cost                                   4.0 -> 2.0
```

```
fleabite                                    1-10/1s -> 1-20/1s                  Fleabite                                                              mag x2, dur x1 = x2 compensated ✓
doze                                        1-20/1s -> 1-40/1s                  Doze                                                                  mag x2, dur x1 = x2 compensated ✓
hornhand                                    15-36/1s -> 30-70/1s                Hornhand                                                              mag x2, dur x1 = x2 compensated ✓
```

------------------------------------------------------------

### Damage Magicka

```
Base Cost                                   8.0 -> 4.0
```

```
soulpinch                                   1-20/1s -> 1-40/1s                  Soulpinch                                                             mag x2, dur x1 = x2 compensated ✓
```

*Tamriel Data*
```
T_Com_Des_Magefire                          10-30/1s -> 10-30/2s                Thimble of Magefire                                                   mag x1, dur x2 = x2 compensated ✓
```

------------------------------------------------------------

### Disintegrate Armor

```
Base Cost                                   6.0 -> 0.6
```

```
disintegrate armor                          6-25/1s -> 60-250/1s                Disintegrate Armor                                                    mag x10, dur x1 = x10 compensated ✓
armor eater                                 10-30/1s -> 200-600/1s              Armor Eater                                                           mag x20, dur x1 = x20 ✗ (expected x10)
```

*Tamriel Data*
```
T_Com_Des_FractureArmor                     100/2s -> 1000/2s                   Fracture Armor                                                        mag x10, dur x1 = x10 compensated ✓
```

------------------------------------------------------------

### Disintegrate Weapon

```
Base Cost                                   6.0 -> 1.2
```

```
disintegrate weapon                         6-25/1s -> 30-125/1s                Disintegrate Weapon                                                   mag x5, dur x1 = x5 compensated ✓
weapon eater                                6-25/1s -> 100-300/1s               Weapon Eater                                                          mag x12, dur x1 = x12 ✗ (expected x5)
```

*Tamriel Data*
```
T_Rea_Des_IronEater                         1-25/2s -> 5-125/2s                 Iron Eater                                                            mag x5, dur x1 = x5 compensated ✓
T_Rea_Des_SteelEater                        5-30/3s -> 25-150/3s                Steel Eater                                                           mag x5, dur x1 = x5 compensated ✓
```

------------------------------------------------------------

### Drain Attribute

```
blood despair                               7-14/60s -> 5-15/60s                Blood Despair                                                         rounded
```

------------------------------------------------------------

### Drain Fatigue

```
Base Cost                                   2.0 -> 0.2
```

```
weariness                                   1-10/1s -> 10-100/20s               Weariness                                                             mag x10, dur x20 = x200 ✗ (expected x10)
sleep                                       5-15/30s -> 25-75/60s               Sleep                                                                 mag x5, dur x2 = x10 compensated ✓
wild exhaustion                             5-15/60s -> 25-75/120s              Wild Exhaustion                                                       mag x5, dur x2 = x10 compensated ✓
exhausting touch                            5-20/60s -> 25-100/120s             Exhausting Touch                                                      mag x5, dur x2 = x10 compensated ✓
exhaustion                                  5-20/90s -> 25-100/180s             Exhaustion                                                            mag x5, dur x2 = x10 compensated ✓
ordeal of st. olms                          5-20/60s -> 50-200/60s              Ordeal of St. Olms                                                    mag x10, dur x1 = x10 compensated ✓
wearying touch                              5-20/30s -> 25-100/60s              Wearying Touch                                                        mag x5, dur x2 = x10 compensated ✓
dagoth's bosom                              20/30s -> 200/30s                   Dagoth's Bosom                                                        mag x10, dur x1 = x10 compensated ✓
```

*Tamriel Data*
```
T_Com_Des_Duck                              200/2s -> 2000/2s                   Duck                                                                  mag x10, dur x1 = x10 compensated ✓
```

------------------------------------------------------------

### Drain Health

```
ash feast                                   3/30s -> 30/3s                      Ash Feast                                                             rescaled mag x10 dur /10
```

------------------------------------------------------------

### Drain Magicka

```
Base Cost                                   4.0 -> 0.4
```

```
magicka leech                               6-15/60s -> 5-15/60s                Magicka Leech                                                         mag /1, dur x1 = /1 ✗ (expected x10)
```

*Tamriel Data*
```
T_Com_Des_RageOfMagnus                      60/10s -> 300/20s                   Rage of Magnus                                                        mag x5, dur x2 = x10 compensated ✓
```

------------------------------------------------------------

### Fire Damage

```
Base Cost                                   5.0 -> 8.0
```

```
cruel firebloom                             10-16/1s -> 10-15/1s                Cruel Firebloom                                                       no-scale
god's fire                                  11-60/10s -> 10-60/10s              God's Fire                                                            no-scale
```

------------------------------------------------------------

### Frost Damage

```
Base Cost                                   5.0 -> 8.0
```

```
god's frost                                 11-60/10s -> 10-60/10s              God's Frost                                                           no-scale
```

------------------------------------------------------------

### Poison

```
Base Cost                                   9.0 -> 8.0
```

```
poison_powerful                             2-15/10s -> 1-15/10s                Toxic Cloud                                                           no-scale
poison                                      2-20/1s -> 1-20/1s                  Poison                                                                no-scale
```

------------------------------------------------------------

### Shock Damage

```
Base Cost                                   7.0 -> 8.0
```

```
lightning storm                             2-10/10s -> 1-10/10s                Lightning Storm                                                       no-scale
spark                                       2-20/1s -> 1-20/1s                  Spark                                                                 no-scale
shockball_large                             2-40/1s -> 1-40/1s                  Greater Shockball                                                     no-scale
shockball                                   2-40/1s -> 1-20/1s                  Shockball                                                             no-scale
```

------------------------------------------------------------

### Weakness to Fire

```
dire weakness to fire                       2-60/10s -> 1-60/10s                Dire Weakness to Fire                                                 rounded
```

------------------------------------------------------------

### Weakness to Frost

```
dire weakness to frost                      2-60/10s -> 1-60/10s                Dire Weakness to Frost                                                rounded
```

------------------------------------------------------------

### Weakness to Magicka

```
dire weakness to magicka                    2-60/10s -> 1-60/10s                Dire Weakness to Magicka                                              rounded
```

------------------------------------------------------------

### Weakness to Poison

```
dire weakness to poison                     2-60/10s -> 1-60/10s                Dire Weakness to Poison                                               rounded
```

------------------------------------------------------------

### Weakness to Shock

```
dire weakness to shock                      2-60/10s -> 1-60/10s                Dire Weakness to Shock                                                rounded
```

------------------------------------------------------------

## Illusion

------------------------------------------------------------

### Blind

```
crying eye                                  1-10/5s -> 1-10/20s                 Crying Eye                                                            rescaled dur x4
erelvam's wild sty                          1-40/10s -> 1-40/20s                Erelvam's Wild Sty                                                    rescaled dur x2
```

------------------------------------------------------------

### Chameleon

```
shadow form                                 6-15/30s -> 10-30/30s               Shadow Form                                                           rescaled mag x2
```

------------------------------------------------------------

### Charm

```
Base Cost                                   5.0 -> 2.5
```

*Tamriel Data*
```
T_Com_Ilu_AlluringSpeech                    15-20/20s [80 -> 40]                Alluring Speech                                                       mag/dur held; cost /2 compensated via cost ✓
```

------------------------------------------------------------

### Invisibility

```
invisibility                                30s -> 60s                          Invisibility                                                          rescaled dur x2
```

------------------------------------------------------------

### Paralyze

```
Base Cost                                   40.0 -> 80.0
```

```
scrib_paralysis                             6s -> 12s [auto -> 6]               Paralysis                                                             mag x1, dur x2 = x2 ✗ (expected /2)
```

*Tamriel Data*
```
T_Com_Ilu_Paralysis                         3s [6 -> 12]                        Paralysis                                                             mag/dur held; cost x2 compensated via cost ✓
T_Com_Ilu_LivingStatue                      20s [30 -> 60]                      Living Statue                                                         mag/dur held; cost x2 compensated via cost ✓
```

------------------------------------------------------------

### Sanctuary

```
sotha's grace                               1-20/5s -> 1-20/10s                 Sotha's Grace                                                         rescaled dur x2
father's hand                               1-40/5s -> 1-40/10s                 Father's Hand                                                         rescaled dur x2
```

------------------------------------------------------------

### Sound

```
Base Cost                                   3.0 -> 1.0
```

```
wild earwig                                 1-30/5s -> 1-90/5s                  Wild Earwig                                                           mag x3, dur x1 = x3 compensated ✓
dire noise                                  2-60/5s -> 1-60/15s                 Dire Noise                                                            mag /1, dur x3 = x3 compensated ✓
earwig                                      3-8/5s -> 10-25/5s                  Earwig                                                                mag x3, dur x1 = x3 compensated ✓
noise                                       3-8/5s -> 1-10/15s                  Noise                                                                 mag x1, dur x3 = x3 compensated ✓
cruel earwig                                5-11/5s -> 15-35/5s                 Cruel Earwig                                                          mag x3, dur x1 = x3 compensated ✓
dire earwig                                 8-15/5s -> 25-45/5s                 Dire Earwig                                                           mag x3, dur x1 = x3 compensated ✓
cruel noise                                 10-22/5s -> 10-20/15s               Cruel Noise                                                           mag /1, dur x3 = x2.5 compensated ✓
```

*Tamriel Data*
```
T_Com_Ilu_Voices                            50/20s -> 50/60s [100 -> 50]        Voices                                                                mag x1, dur x3 = x3 compensated ✓
```

------------------------------------------------------------

## Mysticism

------------------------------------------------------------

### Absorb Attribute

```
absorb intelligence [ranged]                5-51/30s -> 5-50/30s                Absorb Intelligence [Ranged]                                          rounded
```

------------------------------------------------------------

### Absorb Fatigue

```
Base Cost                                   4.0 -> 6.0
```

```
absorb fatigue                              5-20/30s -> 5-20/3s                 Absorb Fatigue                                                        mag x1, dur /10 = /10 ✗ (expected /1.5)
absorb fatigue [ranged]                     5-20/30s -> 5-20/3s                 Absorb Fatigue [Ranged]                                               mag x1, dur /10 = /10 ✗ (expected /1.5)
energy leech                                5-20/30s -> 5-20/6s                 Energy Leech                                                          mag x1, dur /5 = /5 ✗ (expected /1.5)
Tap Energy                                  20/30s -> 20/3s                     Tap Energy                                                            mag x1, dur /10 = /10 ✗ (expected /1.5)
```

------------------------------------------------------------

### Absorb Health

```
Base Cost                                   8.0 -> 16.0
```

```
absorb health                               5-52/1s -> 5-50/1s                  Absorb Health                                                         mag /1, dur x1 = /1 ✗ (expected /2)
```

*Tamriel Data*
```
T_Com_Mys_Lifesteal                         40/1s [24 -> 48]                    Lifesteal                                                             mag/dur held; cost x2 compensated via cost ✓
```

------------------------------------------------------------

### Detect Animal

```
Base Cost                                   0.75 -> 0.15
```

*Tamriel Data*
```
T_Com_Mys_DetectHumanoid                    100-300/5s [38 -> 8]                Greater Detect Creature                                               mag/dur held; cost /5 compensated via cost ✓
```

------------------------------------------------------------

### Detect Enchantment

```
Base Cost                                   1.0 -> 0.2
```

```
detect enchantment                          10/10s -> 50/10s                    Detect Enchantment                                                    mag x5, dur x1 = x5 compensated ✓
```

*Tamriel Data*
```
T_Com_Mys_Insight                           150/10s [75 -> 15]                  Greater Detect Enchantment                                            mag/dur held; cost /5 compensated via cost ✓
```

------------------------------------------------------------

### Detect Key

```
Base Cost                                   1.0 -> 0.2
```

```
tevral's hawkshaw                           10/10s -> 50/10s                    Tevral's Hawkshaw                                                     mag x5, dur x1 = x5 compensated ✓
detect_key                                  50/5s -> 250/5s                     Detect Key                                                            mag x5, dur x1 = x5 compensated ✓
```

------------------------------------------------------------

### Reflect

```
Base Cost                                   10.0 -> 2.5
```

```
wild reflect                                1-40/10s -> 1-40/40s                Wild Reflect                                                          mag x1, dur x4 = x4 compensated ✓
sotha's mirror                              10/5s -> 10/20s                     Sotha's Mirror                                                        mag x1, dur x4 = x4 compensated ✓
reflect                                     10-20/5s -> 10-20/20s               Reflect                                                               mag x1, dur x4 = x4 compensated ✓
shalidor's mirror                           10-30/10s -> 10-30/40s              Shalidor's Mirror                                                     mag x1, dur x4 = x4 compensated ✓
llivam's reversal                           20-30/10s -> 20-30/40s              Llivam's Reversal                                                     mag x1, dur x4 = x4 compensated ✓
strong reflect                              20-30/5s -> 20-30/20s               Strong Reflect                                                        mag x1, dur x4 = x4 compensated ✓
```

*Tamriel Data*
```
T_Com_Mys_ReflectDamage                     1-5/50s -> 1-5/200s                 Minor Reflect                                                         mag x1, dur x4 = x4 compensated ✓
T_Imp_Res_SothasMirror                      10/5s -> 40/5s                      St. Naharine's Shield                                                 mag x4, dur x1 = x4 compensated ✓
T_Com_Mys_DistortedReflect                  20/15s -> 40/30s                    Distorted Reflection                                                  mag x2, dur x2 = x4 compensated ✓
```

------------------------------------------------------------

### Spell Absorption

```
Base Cost                                   10.0 -> 2.5
```

```
wild spelldrinker                           1-40/5s -> 1-40/20s                 Wild Spelldrinker                                                     mag x1, dur x4 = x4 compensated ✓
spell absorption                            10/5s -> 10/20s                     Spell Absorption                                                      mag x1, dur x4 = x4 compensated ✓
vivec's feast                               10/5s -> 10/40s                     Vivec's Feast                                                         mag x1, dur x8 = x8 ✗ (expected x4)
weak spelldrinker                           10-20/5s -> 10-20/20s               Weak Spelldrinker                                                     mag x1, dur x4 = x4 compensated ✓
strong spelldrinker                         20-30/5s -> 20-30/20s               Strong Spelldrinker                                                   mag x1, dur x4 = x4 compensated ✓
tranasa's spelltrap                         20-30/10s -> 20-30/40s              Tranasa's Spelltrap                                                   mag x1, dur x4 = x4 compensated ✓
```

*Tamriel Data*
```
T_Imp_Mys_VivecsFeast                       10/5s -> 40/5s                      St. Horuscia's Alms                                                   mag x4, dur x1 = x4 compensated ✓
```

------------------------------------------------------------

## Restoration

------------------------------------------------------------

### Fortify Fatigue

```
Base Cost                                   0.5 -> 0.25
```

```
vigor                                       5-20/30s -> 10-40/30s               Vigor                                                                 mag x2, dur x1 = x2 compensated ✓
```

------------------------------------------------------------

### Fortify Skill

```
Base Cost                                   1.0 -> 4.0
```

```
masterful balanced armor                    15/60s -> 15/15s                    Masterful Balanced Armor                                              mag x1, dur /4 = /4 compensated ✓
masterful deep biting                       15/60s -> 15/15s                    Masterful Deep Biting                                                 mag x1, dur /4 = /4 compensated ✓
masterful denial                            15/60s -> 15/15s                    Masterful Denial                                                      mag x1, dur /4 = /4 compensated ✓
masterful enterprise                        15/60s -> 15/15s                    Masterful Enterprise                                                  mag x1, dur /4 = /4 compensated ✓
masterful fleetness                         15/60s -> 15/15s                    Masterful Fleetness                                                   mag x1, dur /4 = /4 compensated ✓
masterful fluid evasion                     15/60s -> 15/15s                    Masterful Fluid Evasion                                               mag x1, dur /4 = /4 compensated ✓
masterful glib speech                       15/60s -> 15/15s                    Masterful Glib Speech                                                 mag x1, dur /4 = /4 compensated ✓
masterful golden wisdom                     15/60s -> 15/15s                    Masterful Golden Wisdom                                               mag x1, dur /4 = /4 compensated ✓
masterful green wisdom                      15/60s -> 15/15s                    Masterful Green Wisdom                                                mag x1, dur /4 = /4 compensated ✓
masterful hewing                            15/60s -> 15/15s                    Masterful Hewing                                                      mag x1, dur /4 = /4 compensated ✓
masterful horny fist                        15/60s -> 15/15s                    Masterful Horny Fist                                                  mag x1, dur /4 = /4 compensated ✓
masterful impaling thrust                   15/60s -> 15/15s                    Masterful Impaling Thrust                                             mag x1, dur /4 = /4 compensated ✓
masterful leaping                           15/60s -> 15/15s                    Masterful Leaping                                                     mag x1, dur /4 = /4 compensated ✓
masterful martial craft                     15/60s -> 15/15s                    Masterful Martial Craft                                               mag x1, dur /4 = /4 compensated ✓
masterful nimble armor                      15/60s -> 15/15s                    Masterful Nimble Armor                                                mag x1, dur /4 = /4 compensated ✓
masteful red wisdom                         15/60s -> 15/15s                    Masterful Red Wisdom                                                  mag x1, dur /4 = /4 compensated ✓
masterful red wisdom                        15/60s -> 15/15s                    Masterful Red Wisdom                                                  mag x1, dur /4 = /4 compensated ✓
masterful safekeeping                       15/60s -> 15/15s                    Masterful Safekeeping                                                 mag x1, dur /4 = /4 compensated ✓
masterful silver wisdom                     15/60s -> 15/15s                    Masterful Silver Wisdom                                               mag x1, dur /4 = /4 compensated ✓
masterful smiting                           15/60s -> 15/15s                    Masterful Smiting                                                     mag x1, dur /4 = /4 compensated ✓
masterful stalking                          15/60s -> 15/15s                    Masterful Stalking                                                    mag x1, dur /4 = /4 compensated ✓
masteful stolid armor                       15/60s -> 15/15s                    Masterful Stolid Armor                                                mag x1, dur /4 = /4 compensated ✓
masterful stolid armor                      15/60s -> 15/15s                    Masterful Stolid Armor                                                mag x1, dur /4 = /4 compensated ✓
masterful sublime wisdom                    15/60s -> 15/15s                    Masterful Sublime Wisdom                                              mag x1, dur /4 = /4 compensated ✓
masterful sureflight                        15/60s -> 15/15s                    Masterful Sureflight                                                  mag x1, dur /4 = /4 compensated ✓
masterful swiftblade                        15/60s -> 15/15s                    Masterful Swiftblade                                                  mag x1, dur /4 = /4 compensated ✓
masterful transcendant wisdom               15/60s -> 15/15s                    Masterful Transcendant Wisdom -> Masterful Transcendent Wisdom        mag x1, dur /4 = /4 compensated ✓; renamed
masterful transfiguring wisdom              15/60s -> 15/15s                    Masterful Transfiguring Wisdom                                        mag x1, dur /4 = /4 compensated ✓
masterful unseen wisdom                     15/60s -> 15/15s                    Masterful Unseen Wisdom                                               mag x1, dur /4 = /4 compensated ✓
```

*Tamriel Data*
```
T_Nor_Res_EagleEye                          10-15/40s [25 -> 100]               Eagle Eye                                                             mag/dur held; cost x4 compensated via cost ✓
T_Nor_Res_TreefellersRage                   10-15/40s [25 -> 100]               Treefellers Rage                                                      mag/dur held; cost x4 compensated via cost ✓
T_Com_Res_DeftSecurity                      15/30s [23 -> 92]                   Deft Security                                                         mag/dur held; cost x4 compensated via cost ✓
```

------------------------------------------------------------

### Resist Blight Disease

```
Base Cost                                   5.0 -> 0.25
```

```
poet's whim                                 1-30/10s -> 1-30/200s [auto -> 39]  Poet's Whim                                                           mag x1, dur x20 = x20 compensated ✓
vivec's mercy                               20/10s -> 50/80s [auto -> 50]       Vivec's Mercy                                                         mag x2.5, dur x8 = x20 compensated ✓
shield of the armiger                       30/10s -> 100/60s [auto -> 75]      Shield of the Armiger                                                 mag x3, dur x6 = x20 compensated ✓
```

------------------------------------------------------------

### Resist Common Disease

```
Base Cost                                   2.0 -> 0.1
```

```
variable resist common disease              1-30/10s -> 1-30/200s [auto -> 16]  Variable Resist Common Disease                                        mag x1, dur x20 = x20 compensated ✓
resist common disease                       10/5s -> 50/20s [auto -> 5]         Resist Common Disease                                                 mag x5, dur x4 = x20 compensated ✓
seryn's blessing                            20/10s -> 50/80s [auto -> 20]       Seryn's Blessing                                                      mag x2.5, dur x8 = x20 compensated ✓
great resist common disease                 30/10s -> 100/60s [auto -> 30]      Great Resist Common Disease                                           mag x3, dur x6 = x20 compensated ✓
```

*Tamriel Data*
```
T_Imp_Res_SerynsBlessing                    20/10s -> 100/40s                   Pilgrimage of St. Rosunius                                            mag x5, dur x4 = x20 compensated ✓
```

------------------------------------------------------------

### Resist Fire

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist fire                        1-30/10s -> 1-30/40s                Variable Resist Fire                                                  mag x1, dur x4 = x4 compensated ✓
resist fire                                 10/5s -> 10/20s                     Resist Fire                                                           mag x1, dur x4 = x4 compensated ✓
strong resist fire                          20/10s -> 20/40s                    Strong Resist Fire                                                    mag x1, dur x4 = x4 compensated ✓
flameguard                                  20-40/30s -> 20-40/120s             Flameguard                                                            mag x1, dur x4 = x4 compensated ✓
great resist fire                           30/10s -> 30/40s                    Great Resist Fire                                                     mag x1, dur x4 = x4 compensated ✓
```

------------------------------------------------------------

### Resist Frost

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist frost                       1-30/10s -> 1-30/40s                Variable Resist Frost                                                 mag x1, dur x4 = x4 compensated ✓
resist frost                                10/5s -> 10/20s                     Resist Frost                                                          mag x1, dur x4 = x4 compensated ✓
strong resist frost                         20/10s -> 20/40s                    Strong Resist Frost                                                   mag x1, dur x4 = x4 compensated ✓
frostguard                                  20-40/30s -> 20-40/120s             Frostguard                                                            mag x1, dur x4 = x4 compensated ✓
great resist frost                          30/10s -> 30/40s                    Great Resist Frost                                                    mag x1, dur x4 = x4 compensated ✓
```

*Tamriel Data*
```
T_Nor_Res_WinteryMantle                     20/60s -> 80/60s                    Wintery Mantle                                                        mag x4, dur x1 = x4 compensated ✓
```

------------------------------------------------------------

### Resist Magicka

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist magicka                     1-30/10s -> 1-30/40s                Variable Resist Magicka                                               mag x1, dur x4 = x4 compensated ✓
resist magicka                              10/5s -> 10/20s                     Resist Magicka                                                        mag x1, dur x4 = x4 compensated ✓
strong resist magicka                       20/10s -> 20/40s                    Strong Resist Magicka                                                 mag x1, dur x4 = x4 compensated ✓
magickguard                                 20-40/10s -> 20-40/40s              Magickguard                                                           mag x1, dur x4 = x4 compensated ✓
great resist magicka                        30/10s -> 30/40s                    Great Resist Magicka                                                  mag x1, dur x4 = x4 compensated ✓
```

------------------------------------------------------------

### Resist Paralysis

```
resist paralysis                            50/30s [300 -> auto]                Resist Paralysis                                                      cost
```

------------------------------------------------------------

### Resist Poison

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist poison                      1-30/10s -> 1-30/40s                Variable Resist Poison                                                mag x1, dur x4 = x4 compensated ✓
resist poison                               20/5s -> 20/20s                     Resist Poison                                                         mag x1, dur x4 = x4 compensated ✓
strong resist poison                        20/10s -> 20/40s                    Strong Resist Poison                                                  mag x1, dur x4 = x4 compensated ✓
poisonguard                                 20-40/30s -> 20-40/120s             Poisonguard                                                           mag x1, dur x4 = x4 compensated ✓
greater resist poison                       30/10s -> 30/40s                    Greater Resist Poison                                                 mag x1, dur x4 = x4 compensated ✓
```

------------------------------------------------------------

### Resist Shock

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist shock                       1-30/10s -> 1-30/40s                Variable Resist Shock                                                 mag x1, dur x4 = x4 compensated ✓
resist shock                                20/5s -> 20/20s                     Resist Shock                                                          mag x1, dur x4 = x4 compensated ✓
strong resist shock                         20/10s -> 20/40s                    Strong Resist Shock                                                   mag x1, dur x4 = x4 compensated ✓
shockguard                                  20-40/30s -> 20-40/120s             Shockguard                                                            mag x1, dur x4 = x4 compensated ✓
great resist shock                          30/10s -> 30/40s                    Great Resist Shock                                                    mag x1, dur x4 = x4 compensated ✓
```

------------------------------------------------------------

### Restore Attribute

```
Base Cost                                   1.0 -> 8.0
```

```
restore agility                             5-20/30s -> 5-20/4s                 Restore Agility                                                       mag x1, dur /8 = /8 compensated ✓
restore endurance                           5-20/30s -> 5-20/4s                 Restore Endurance                                                     mag x1, dur /8 = /8 compensated ✓
restore intelligence                        5-20/30s -> 5-20/4s                 Restore Intelligence                                                  mag x1, dur /8 = /8 compensated ✓
restore luck                                5-20/30s -> 5-20/4s                 Restore Luck                                                          mag x1, dur /8 = /8 compensated ✓
restore personality                         5-20/30s -> 5-20/4s                 Restore Personality                                                   mag x1, dur /8 = /8 compensated ✓
restore speed                               5-20/30s -> 5-20/4s                 Restore Speed                                                         mag x1, dur /8 = /8 compensated ✓
restore strength                            5-20/30s -> 5-20/4s                 Restore Strength                                                      mag x1, dur /8 = /8 compensated ✓
restore willpower                           5-20/30s -> 5-20/4s                 Restore Willpower                                                     mag x1, dur /8 = /8 compensated ✓
```

------------------------------------------------------------

### Restore Fatigue

```
Base Cost                                   1.0 -> 2.5
```

```
rest of st. merris                          1-10/20s -> 1-10/8s                 Rest of St. Merris -> Rest of St. Meris                               mag x1, dur /2.5 = /2.5 compensated ✓; renamed
stamina                                     10-30/30s -> 10-30/12s              Stamina                                                               mag x1, dur /2.5 = /2.5 compensated ✓
```

*Tamriel Data*
```
T_Com_Res_WeaponResartus                    42-78/30s -> 40-80/12s              Greater Stamina                                                       mag x1, dur /2.5 = /2.5 compensated ✓
```

------------------------------------------------------------

### Restore Health

```
balyna's soothing balm                      3-12/1s -> 5-10/1s                  Balyna's Soothing Balm                                                rounded
balyna's efficacious balm                   3-22/1s -> 5-20/1s                  Balyna's Efficacious Balm                                             rounded
balyna's perfect balm                       3-30/1s -> 5-30/1s                  Balyna's Perfect Balm                                                 rounded
heal companion                              6-15/1s -> 5-15/1s                  Heal Companion                                                        rounded
```

------------------------------------------------------------

## Multi-Effect Spells

```
bm_draugr_curse                             [200 -> auto]                       Eddard's Wrath                                                        mag x10, dur x1 = x10 compensated ✓
    Disintegrate Armor                      4-9/15s -> 40-90/15s
    Disintegrate Weapon                     4-9/15s -> 40-90/15s
black hand                                                                      Black Hand                                                            rounded
    Damage Health                           5-12/1s -> 5-10/1s
    Poison                                  5-12/1s -> 5-10/1s
stormhand                                                                       Stormhand                                                             rounded
    Damage Health                           5-12/1s -> 5-10/1s
    Shock Damage                            5-12/1s -> 5-10/1s
Aryon_rest                                                                      Aryon's Rest                                                          mag x1, dur x1 = x1 ✗ (expected x2)
    Damage Fatigue                          10/10s
    Burden                                  10/10s -> 100/10s
brittlewind                                                                     Brittlewind                                                           no-scale
    Frost Damage                            10/10s
    Disintegrate Armor                      20/10s -> 200/10s
BM_paralyze_hirc                            [46 -> 50]                          Hunter's Venom                                                        mag x1, dur x1 = x1 ✗ (expected /2)
    Paralyze                                10s
    Burden                                  50/10s -> 500/10s
hand of odros                                                                   Hand of Odros                                                         mag x1, dur x1 = x1 ✗ (expected x2); rounding ✗ (3-6)
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3-6/120s
    Burden                                  30-40/60s -> 300-400/60s
wrath of odros                                                                  Wrath of Odros                                                        mag x1, dur x1 = x1 ✗ (expected x2)
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3/120s
    Burden                                  20-30/50s -> 200-300/50s
heavy_eyes_unique                                                               Harthoon's Heavy Eyes                                                 changed
    Blind                                   100/10s
    Burden                                  100/10s -> 1000/10s
```

*Tamriel Data*
```
T_Rea_Mys_SoulWither                                                            Dhamcka's Soul-Withering                                              mag x10, dur x1 = x10 compensated ✓
    Drain Magicka                           1/30s -> 10/30s
    Soul Trap                               1/30s
T_Rea_Des_ShadowRust                                                            Shadow Rust                                                           mag x10, dur x1 = x10 compensated ✓
    Disintegrate Armor                      1-5/20s -> 10-50/20s
    Burden                                  1-15/20s -> 10-150/20s
T_Com_Alt_Falling1stBarrier                                                     Falling First Barrier                                                 mag x2, dur x1 = x2 compensated ✓
    Shield                                  8/40s -> 16/40s
    Shield                                  5/20s -> 10/20s
T_Com_Alt_DaedraFireEye                                                         Fire Eye                                                              rounded
    Fire Shield                             10-23/20s -> 10-25/20s
    Night Eye                               20/20s
T_Com_Trp_Acid                                                                  Acid Trap                                                             mag x1, dur x10 = x10 compensated ✓; rounding ✗ (2-4)
    Disintegrate Armor                      20-40/1s -> 20-40/10s
    Disintegrate Weapon                     20-40/1s -> 20-40/5s
    Poison                                  2-4/5s
T_Com_Trp_AcidMaster                                                            Master Acid Trap                                                      mag x1, dur x10 = x10 compensated ✓
    Disintegrate Armor                      150-300/1s -> 150-300/10s
    Disintegrate Weapon                     150-300/1s -> 150-300/5s
    Poison                                  10-20/5s
```
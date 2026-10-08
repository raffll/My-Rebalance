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
burden                                      20/10s -> 50/40s                    Burden                                [COMPENSATED] base /10 via mag x2.5 & dur x4; effective cost kept ~same; auto-calc cost
burden touch                                20/10s -> 50/40s                    Burden Touch                          [COMPENSATED] base /10 via mag x2.5 & dur x4; effective cost kept ~same; auto-calc cost
weary                                       30-60/10s -> 60-120/50s             Weary                                 [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
great burden of sin                         40/10s -> 80-120/100s               Great Burden of Sin                   [COST RAISED] base /10 via mag x2.5 & dur x10; effective cost x2.5 (intended pricier); auto-calc cost
heavy burden                                40/10s -> 100/40s                   Heavy Burden                          [COMPENSATED] base /10 via mag x2.5 & dur x4; effective cost kept ~same; auto-calc cost
heavy burden touch                          40/10s -> 100/40s                   Heavy Burden Touch                    [COMPENSATED] base /10 via mag x2.5 & dur x4; effective cost kept ~same; auto-calc cost
burden of sin                               40-60/20s -> 80/50s                 Burden of Sin                         [COST REDUCED] base /10 via mag x1.6 & dur x2.5; effective cost /2.5 (intended cheaper); auto-calc cost
cruel weary                                 50-70/10s -> 100-140/50s            Cruel Weary                           [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
crushing burden                             60/10s -> 150/40s                   Crushing Burden                       [COMPENSATED] base /10 via mag x2.5 & dur x4; effective cost kept ~same; auto-calc cost
crushing burden touch                       60/10s -> 150/40s                   Crushing Burden Touch                 [COMPENSATED] base /10 via mag x2.5 & dur x4; effective cost kept ~same; auto-calc cost
crushing burden of sin                      60-80/30s -> 120-160/150s           Crushing Burden of Sin                [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
dire weary                                  60-90/10s -> 120-180/50s            Dire Weary                            [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Com_Alt_WeightOfGuilt                     500/3s -> 5000/3s                   Weight of Guilt                       [COMPENSATED] base /10 via mag x10; effective cost kept ~same
```

------------------------------------------------------------

### Feather

```
Base Cost                                   1.0 -> 0.1
```

```
feather                                     20/10s -> 40/50s                    Feather                               [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
strong feather                              50/10s -> 100/50s                   Strong Feather                        [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
ulms juicedaw's feather                     50/10s -> 250/20s                   Ulms's Juicedaw's Feather -> Ulms' Juicedaw Feather [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same; auto-calc cost; renamed
great feather                               100/10s -> 200/50s                  Great Feather                         [COMPENSATED] base /10 via mag x2 & dur x5; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Imp_Alt_UlmsJuicedawsFeather              50/10s -> 500/10s                   Zenithar's Arms                       [COMPENSATED] base /10 via mag x10; effective cost kept ~same
T_Com_Alt_Fling                             500/3s -> 5000/3s                   Fling                                 [COMPENSATED] base /10 via mag x10; effective cost kept ~same
```

------------------------------------------------------------

### Fire Shield

```
fire_fathasa_unique                         1-10/10s                            Fire Barrier -> Fathasa's Fire Barrier auto-calc cost; renamed
fierce fire shield                          5-11/10s -> 5-10/10s                Fierce Fire Shield                    [RESCALED] mag /1.06667 (no base-cost change); auto-calc cost
strong fire shield                          12/30s -> 15/30s                    Strong Fire Shield                    [RESCALED] mag x1.25 (no base-cost change); auto-calc cost
```

*Tamriel Data*
```
T_Com_Alt_DaedraFireEye                                                         Fire Eye                              [RESCALED] mag x1.06061 (no base-cost change)
    Fire Shield                             10-23/20s -> 10-25/20s
    Night Eye                               20/20s
```

------------------------------------------------------------

### Frost Shield

```
frost barrier                               3/10s -> 1-10/10s                   Frost Barrier                         [RESCALED] mag x1.83333 (no base-cost change); auto-calc cost
fierce frost shield                         5-11/10s -> 5-10/10s                Fierce Frost Shield                   [RESCALED] mag /1.06667 (no base-cost change); auto-calc cost
frost_shield                                6/30s -> 5/30s                      Frost Shield -> Weak Frost Shield     [RESCALED] mag /1.2 (no base-cost change); auto-calc cost; renamed
strong frost shield                         12/30s -> 15/30s                    Strong Frost Shield                   [RESCALED] mag x1.25 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Lightning Shield

```
shock shield                                3/20s                               Shock Shield -> Lightning Shield      auto-calc cost; renamed
fierce shock shield                         5-11/10s -> 5-10/10s                Fierce Shock Shield                   [RESCALED] mag /1.06667 (no base-cost change); auto-calc cost
lightning shield                            10/30s                              Lightning Shield -> Shock Shield      auto-calc cost; renamed
strong shock shield                         12/30s -> 15/30s                    Strong Shock Shield                   [RESCALED] mag x1.25 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Lock

```
Base Cost                                   2.0 -> 24.0
```

*Tamriel Data*
```
T_Com_Alt_WizardLock                        20 [2 -> 24]                        Wizard Lock                           [COST RAISED] base x12 (mag/dur unchanged); effective cost x12 (intended pricier)
T_Com_Alt_DalgorsEntwining                  100 [8 -> 96]                       Dalgor's Entwining                    [COST RAISED] base x12 (mag/dur unchanged); effective cost x12 (intended pricier)
```

------------------------------------------------------------

### Shield

```
Base Cost                                   2.0 -> 1.0
```

*Tamriel Data*
```
T_Com_Alt_Falling1stBarrier                                                     Falling First Barrier                 [COMPENSATED] base /2 via mag x2; effective cost kept ~same
    Shield                                  8/40s -> 16/40s
    Shield                                  5/20s -> 10/20s
T_Nor_Alt_TsunsWard                         20/20s -> 40/20s                    Tsun's Ward                           [COMPENSATED] base /2 via mag x2; effective cost kept ~same
T_Com_Alt_ForceWall                         50/5s -> 100/5s                     Force Wall                            [COMPENSATED] base /2 via mag x2; effective cost kept ~same
```

------------------------------------------------------------

### Swift Swim

```
Base Cost                                   2.0 -> 0.5
```

```
buoyancy                                    1/20s -> 20/20s                     Buoyancy                              [COST RAISED] base /4 via mag x20; effective cost x5 (intended pricier); auto-calc cost
Swimmer's_Blessing                          5/30s -> 50/30s                     Swimmer's Blessing                    [COST RAISED] base /4 via mag x10; effective cost x2.5 (intended pricier); auto-calc cost
```

*Tamriel Data*
```
T_Com_Alt_DreughsGrace                      30/20s -> 120/20s                   Dreugh's Grace                        [COMPENSATED] base /4 via mag x4; effective cost kept ~same
```

------------------------------------------------------------

## Destruction

------------------------------------------------------------

### Damage Fatigue

```
Base Cost                                   4.0 -> 2.0
```

```
fleabite                                    1-10/1s -> 1-20/1s                  Fleabite                              [COMPENSATED] base /2 via mag x1.90909; effective cost kept ~same; auto-calc cost
doze                                        1-20/1s -> 1-40/1s                  Doze                                  [COMPENSATED] base /2 via mag x1.95238; effective cost kept ~same; auto-calc cost
Aryon_rest                                                                      Aryon's Rest                          [COST REDUCED] base /2 (mag/dur unchanged); effective cost /2 (intended cheaper)
    Damage Fatigue                          10/10s
    Burden                                  10/10s -> 100/10s
hornhand                                    15-36/1s -> 30-70/1s                Hornhand                              [COMPENSATED] base /2 via mag x1.96078; effective cost kept ~same; auto-calc cost
hand of odros                                                                   Hand of Odros                         [COST REDUCED] base /2 (mag/dur unchanged); effective cost /2 (intended cheaper); [ROUNDING] 3-6 has a non-1/5 value
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3-6/120s
    Burden                                  30-40/60s -> 300-400/60s
wrath of odros                                                                  Wrath of Odros                        [COST REDUCED] base /2 (mag/dur unchanged); effective cost /2 (intended cheaper)
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3/120s
    Burden                                  20-30/50s -> 200-300/50s
```

------------------------------------------------------------

### Damage Health

```
black hand                                                                      Black Hand                            [RESCALED] mag /1.13333 (no base-cost change); auto-calc cost
    Damage Health                           5-12/1s -> 5-10/1s
    Poison                                  5-12/1s -> 5-10/1s
stormhand                                                                       Stormhand                             [RESCALED] mag /1.13333 (no base-cost change); auto-calc cost
    Damage Health                           5-12/1s -> 5-10/1s
    Shock Damage                            5-12/1s -> 5-10/1s
```

------------------------------------------------------------

### Damage Magicka

```
Base Cost                                   8.0 -> 4.0
```

```
soulpinch                                   1-20/1s -> 1-40/1s                  Soulpinch                             [COMPENSATED] base /2 via mag x1.95238; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Com_Des_Magefire                          10-30/1s -> 10-30/2s                Thimble of Magefire                   [COMPENSATED] base /2 via dur x2; effective cost kept ~same
```

------------------------------------------------------------

### Disintegrate Armor

```
Base Cost                                   6.0 -> 0.6
```

```
bm_draugr_curse                             [200 -> auto]                       Eddard's Wrath                        [COMPENSATED] base /10 via mag x10; effective cost kept ~same; auto-calc cost
    Disintegrate Armor                      4-9/15s -> 40-90/15s
    Disintegrate Weapon                     4-9/15s -> 40-90/15s
disintegrate armor                          6-25/1s -> 60-250/1s                Disintegrate Armor                    [COMPENSATED] base /10 via mag x10; effective cost kept ~same; auto-calc cost
armor eater                                 10-30/1s -> 200-600/1s              Armor Eater                           [COST RAISED] base /10 via mag x20; effective cost x2 (intended pricier); auto-calc cost
```

*Tamriel Data*
```
T_Rea_Des_ShadowRust                                                            Shadow Rust                           [COMPENSATED] base /10 via mag x10; effective cost kept ~same
    Disintegrate Armor                      1-5/20s -> 10-50/20s
    Burden                                  1-15/20s -> 10-150/20s
T_Com_Trp_Acid                                                                  Acid Trap                             [COMPENSATED] base /10 via dur x10; effective cost kept ~same; [ROUNDING] 2-4 has a non-1/5 value
    Disintegrate Armor                      20-40/1s -> 20-40/10s
    Disintegrate Weapon                     20-40/1s -> 20-40/5s
    Poison                                  2-4/5s
T_Com_Des_FractureArmor                     100/2s -> 1000/2s                   Fracture Armor                        [COMPENSATED] base /10 via mag x10; effective cost kept ~same
T_Com_Trp_AcidMaster                                                            Master Acid Trap                      [COMPENSATED] base /10 via dur x10; effective cost kept ~same
    Disintegrate Armor                      150-300/1s -> 150-300/10s
    Disintegrate Weapon                     150-300/1s -> 150-300/5s
    Poison                                  10-20/5s
```

------------------------------------------------------------

### Disintegrate Weapon

```
Base Cost                                   6.0 -> 1.2
```

```
disintegrate weapon                         6-25/1s -> 30-125/1s                Disintegrate Weapon                   [COMPENSATED] base /5 via mag x5; effective cost kept ~same; auto-calc cost
weapon eater                                6-25/1s -> 100-300/1s               Weapon Eater                          [COST RAISED] base /5 via mag x12.9032; effective cost x2.58065 (intended pricier); auto-calc cost
```

*Tamriel Data*
```
T_Rea_Des_IronEater                         1-25/2s -> 5-125/2s                 Iron Eater                            [COMPENSATED] base /5 via mag x5; effective cost kept ~same
T_Rea_Des_SteelEater                        5-30/3s -> 25-150/3s                Steel Eater                           [COMPENSATED] base /5 via mag x5; effective cost kept ~same
```

------------------------------------------------------------

### Drain Attribute

```
blood despair                               7-14/60s -> 5-15/60s                Blood Despair                         [RESCALED] mag /1.05 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Drain Fatigue

```
Base Cost                                   2.0 -> 0.2
```

```
weariness                                   1-10/1s -> 10-100/20s               Weariness                             [COST RAISED] base /10 via mag x10 & dur x20; effective cost x20 (intended pricier); auto-calc cost
sleep                                       5-15/30s -> 25-75/60s               Sleep                                 [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same; auto-calc cost
wild exhaustion                             5-15/60s -> 25-75/120s              Wild Exhaustion                       [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same; auto-calc cost
exhausting touch                            5-20/60s -> 25-100/120s             Exhausting Touch                      [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same; auto-calc cost
exhaustion                                  5-20/90s -> 25-100/180s             Exhaustion                            [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same; auto-calc cost
ordeal of st. olms                          5-20/60s -> 50-200/60s              Ordeal of St. Olms                    [COMPENSATED] base /10 via mag x10; effective cost kept ~same; auto-calc cost
wearying touch                              5-20/30s -> 25-100/60s              Wearying Touch                        [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same; auto-calc cost
dagoth's bosom                              20/30s -> 200/30s                   Dagoth's Bosom                        [COMPENSATED] base /10 via mag x10; effective cost kept ~same
```

*Tamriel Data*
```
T_Com_Des_Duck                              200/2s -> 2000/2s                   Duck                                  [COMPENSATED] base /10 via mag x10; effective cost kept ~same
```

------------------------------------------------------------

### Drain Health

```
ash feast                                   3/30s -> 30/3s                      Ash Feast                             [RESCALED] mag x10, dur /10 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Drain Magicka

```
Base Cost                                   4.0 -> 0.4
```

```
magicka leech                               6-15/60s -> 5-15/60s                Magicka Leech                         [COST REDUCED] base /10 via mag /1.05; effective cost /10.5 (intended cheaper); auto-calc cost
```

*Tamriel Data*
```
T_Rea_Mys_SoulWither                                                            Dhamcka's Soul-Withering              [COMPENSATED] base /10 via mag x10; effective cost kept ~same
    Drain Magicka                           1/30s -> 10/30s
    Soul Trap                               1/30s
T_Com_Des_RageOfMagnus                      60/10s -> 300/20s                   Rage of Magnus                        [COMPENSATED] base /10 via mag x5 & dur x2; effective cost kept ~same
```

------------------------------------------------------------

### Fire Damage

```
Base Cost                                   5.0 -> 8.0
```

```
cruel firebloom                             10-16/1s -> 10-15/1s                Cruel Firebloom                       [NO-SCALE] magnitude kept vanilla; base 5.0->8.0, cost absorbs it
god's fire                                  11-60/10s -> 10-60/10s              God's Fire                            [NO-SCALE] magnitude kept vanilla; base 5.0->8.0, cost absorbs it
```

------------------------------------------------------------

### Frost Damage

```
Base Cost                                   5.0 -> 8.0
```

```
brittlewind                                                                     Brittlewind                           [NO-SCALE] magnitude kept vanilla; base 5.0->8.0, cost absorbs it
    Frost Damage                            10/10s
    Disintegrate Armor                      20/10s -> 200/10s
god's frost                                 11-60/10s -> 10-60/10s              God's Frost                           [NO-SCALE] magnitude kept vanilla; base 5.0->8.0, cost absorbs it
```

------------------------------------------------------------

### Poison

```
Base Cost                                   9.0 -> 8.0
```

```
poison_powerful                             2-15/10s -> 1-15/10s                Toxic Cloud                           [NO-SCALE] magnitude kept vanilla; base 9.0->8.0, cost absorbs it
poison                                      2-20/1s -> 1-20/1s                  Poison                                [NO-SCALE] magnitude kept vanilla; base 9.0->8.0, cost absorbs it
```

------------------------------------------------------------

### Shock Damage

```
Base Cost                                   7.0 -> 8.0
```

```
lightning storm                             2-10/10s -> 1-10/10s                Lightning Storm                       [NO-SCALE] magnitude kept vanilla; base 7.0->8.0, cost absorbs it
spark                                       2-20/1s -> 1-20/1s                  Spark                                 [NO-SCALE] magnitude kept vanilla; base 7.0->8.0, cost absorbs it
shockball_large                             2-40/1s -> 1-40/1s                  Greater Shockball                     [NO-SCALE] magnitude kept vanilla; base 7.0->8.0, cost absorbs it
shockball                                   2-40/1s -> 1-20/1s                  Shockball                             [NO-SCALE] magnitude kept vanilla; base 7.0->8.0, cost absorbs it
```

------------------------------------------------------------

### Weakness to Fire

```
dire weakness to fire                       2-60/10s -> 1-60/10s                Dire Weakness to Fire                 [RESCALED] mag /1.01639 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Weakness to Frost

```
dire weakness to frost                      2-60/10s -> 1-60/10s                Dire Weakness to Frost                [RESCALED] mag /1.01639 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Weakness to Magicka

```
dire weakness to magicka                    2-60/10s -> 1-60/10s                Dire Weakness to Magicka              [RESCALED] mag /1.01639 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Weakness to Poison

```
dire weakness to poison                     2-60/10s -> 1-60/10s                Dire Weakness to Poison               [RESCALED] mag /1.01639 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Weakness to Shock

```
dire weakness to shock                      2-60/10s -> 1-60/10s                Dire Weakness to Shock                [RESCALED] mag /1.01639 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

## Illusion

------------------------------------------------------------

### Blind

```
crying eye                                  1-10/5s -> 1-10/20s                 Crying Eye                            [RESCALED] dur x4 (no base-cost change); auto-calc cost
erelvam's wild sty                          1-40/10s -> 1-40/20s                Erelvam's Wild Sty                    [RESCALED] dur x2 (no base-cost change); auto-calc cost
heavy_eyes_unique                                                               Harthoon's Heavy Eyes                 changed
    Blind                                   100/10s
    Burden                                  100/10s -> 1000/10s
```

------------------------------------------------------------

### Chameleon

```
shadow form                                 6-15/30s -> 12-30/30s               Shadow Form                           [RESCALED] mag x2 (no base-cost change); auto-calc cost; [ROUNDING] 12-30 has a non-1/5 value
```

------------------------------------------------------------

### Charm

```
Base Cost                                   5.0 -> 2.5
```

*Tamriel Data*
```
T_Com_Ilu_AlluringSpeech                    15-20/20s [80 -> 40]                Alluring Speech                       [COST REDUCED] base /2 (mag/dur unchanged); effective cost /2 (intended cheaper)
```

------------------------------------------------------------

### Invisibility

```
invisibility                                30s -> 60s                          Invisibility                          [RESCALED] dur x2 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Paralyze

```
Base Cost                                   40.0 -> 80.0
```

```
scrib_paralysis                             6s -> 12s [auto -> 6]               Paralysis                             [COST RAISED] base x2 via dur x2; effective cost x4 (intended pricier)
BM_paralyze_hirc                            [46 -> 50]                          Hunter's Venom                        [COST RAISED] base x2 (mag/dur unchanged); effective cost x2 (intended pricier)
    Paralyze                                10s
    Burden                                  50/10s -> 500/10s
```

*Tamriel Data*
```
T_Com_Ilu_Paralysis                         3s [6 -> 12]                        Paralysis                             [COST RAISED] base x2 (mag/dur unchanged); effective cost x2 (intended pricier)
T_Com_Ilu_LivingStatue                      20s [30 -> 60]                      Living Statue                         [COST RAISED] base x2 (mag/dur unchanged); effective cost x2 (intended pricier)
```

------------------------------------------------------------

### Sanctuary

```
sotha's grace                               1-20/5s -> 1-20/10s                 Sotha's Grace                         [RESCALED] dur x2 (no base-cost change); auto-calc cost
father's hand                               1-40/5s -> 1-40/10s                 Father's Hand                         [RESCALED] dur x2 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Sound

```
Base Cost                                   3.0 -> 1.0
```

```
wild earwig                                 1-30/5s -> 1-90/5s                  Wild Earwig                           [COMPENSATED] base /3 via mag x2.93548; effective cost kept ~same; auto-calc cost
dire noise                                  2-60/5s -> 1-60/15s                 Dire Noise                            [COMPENSATED] base /3 via mag /1.01639 & dur x3; effective cost kept ~same; auto-calc cost
earwig                                      3-8/5s -> 10-25/5s                  Earwig                                [COMPENSATED] base /3 via mag x3.18182; effective cost kept ~same; auto-calc cost
noise                                       3-8/5s -> 1-10/15s                  Noise                                 [COMPENSATED] base /3 via dur x3; effective cost kept ~same; auto-calc cost
cruel earwig                                5-11/5s -> 15-35/5s                 Cruel Earwig                          [COMPENSATED] base /3 via mag x3.125; effective cost kept ~same; auto-calc cost
dire earwig                                 8-15/5s -> 25-45/5s                 Dire Earwig                           [COMPENSATED] base /3 via mag x3.04348; effective cost kept ~same; auto-calc cost
cruel noise                                 10-22/5s -> 10-20/15s               Cruel Noise                           [COMPENSATED] base /3 via mag /1.06667 & dur x3; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Com_Ilu_Voices                            50/20s -> 50/60s [100 -> 50]        Voices                                [COMPENSATED] base /3 via dur x3; effective cost kept ~same
```

------------------------------------------------------------

## Mysticism

------------------------------------------------------------

### Absorb Attribute

```
absorb intelligence [ranged]                5-51/30s -> 5-50/30s                Absorb Intelligence [Ranged]          [RESCALED] mag /1.01818 (no base-cost change); auto-calc cost
```

------------------------------------------------------------

### Absorb Fatigue

```
Base Cost                                   4.0 -> 6.0
```

```
absorb fatigue                              5-20/30s -> 5-20/3s                 Absorb Fatigue                        [COST REDUCED] base x1.5 via dur /10; effective cost /6.66667 (intended cheaper); auto-calc cost
absorb fatigue [ranged]                     5-20/30s -> 5-20/3s                 Absorb Fatigue [Ranged]               [COST REDUCED] base x1.5 via dur /10; effective cost /6.66667 (intended cheaper); auto-calc cost
energy leech                                5-20/30s -> 5-20/6s                 Energy Leech                          [COST REDUCED] base x1.5 via dur /5; effective cost /3.33333 (intended cheaper); auto-calc cost
Tap Energy                                  20/30s -> 20/3s                     Tap Energy                            [COST REDUCED] base x1.5 via dur /10; effective cost /6.66667 (intended cheaper); auto-calc cost
```

------------------------------------------------------------

### Absorb Health

```
Base Cost                                   8.0 -> 16.0
```

```
absorb health                               5-52/1s -> 5-50/1s                  Absorb Health                         [COST RAISED] base x2 via mag /1.03636; effective cost x1.92982 (intended pricier); auto-calc cost
```

*Tamriel Data*
```
T_Com_Mys_Lifesteal                         40/1s [24 -> 48]                    Lifesteal                             [COST RAISED] base x2 (mag/dur unchanged); effective cost x2 (intended pricier)
```

------------------------------------------------------------

### Detect Animal

```
Base Cost                                   0.75 -> 0.15
```

*Tamriel Data*
```
T_Com_Mys_DetectHumanoid                    100-300/5s [38 -> 8]                Greater Detect Creature               [COST REDUCED] base /5 (mag/dur unchanged); effective cost /5 (intended cheaper)
```

------------------------------------------------------------

### Detect Enchantment

```
Base Cost                                   1.0 -> 0.2
```

```
detect enchantment                          10/10s -> 50/10s                    Detect Enchantment                    [COMPENSATED] base /5 via mag x5; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Com_Mys_Insight                           150/10s -> 50/10s [75 -> auto]      Greater Detect Enchantment -> Detect Enchantment VIOLATION: TD spell must not be AUTO_CALCULATE; [COST REDUCED] base /5 via mag /3; effective cost /15 (intended cheaper); auto-calc cost; renamed
```

------------------------------------------------------------

### Detect Key

```
Base Cost                                   1.0 -> 0.2
```

```
tevral's hawkshaw                           10/10s -> 50/10s                    Tevral's Hawkshaw                     [COMPENSATED] base /5 via mag x5; effective cost kept ~same; auto-calc cost
detect_key                                  50/5s -> 250/5s                     Detect Key                            [COMPENSATED] base /5 via mag x5; effective cost kept ~same; auto-calc cost
```

------------------------------------------------------------

### Reflect

```
Base Cost                                   10.0 -> 2.5
```

```
wild reflect                                1-40/10s -> 1-40/40s                Wild Reflect                          [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
sotha's mirror                              10/5s -> 10/20s                     Sotha's Mirror                        [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
reflect                                     10-20/5s -> 10-20/20s               Reflect                               [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
shalidor's mirror                           10-30/10s -> 10-30/40s              Shalidor's Mirror                     [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
llivam's reversal                           20-30/10s -> 20-30/40s              Llivam's Reversal                     [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
strong reflect                              20-30/5s -> 20-30/20s               Strong Reflect                        [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Com_Mys_ReflectDamage                     1-5/50s -> 15/30s [76 -> 56]        Minor Reflect -> Reflect Damage       [COST REDUCED] base /4 via mag x5 & dur /1.66667; effective cost /1.33333 (intended cheaper); renamed
T_Imp_Res_SothasMirror                      10/5s -> 40/5s                      St. Naharine's Shield                 [COMPENSATED] base /4 via mag x4; effective cost kept ~same
T_Com_Mys_DistortedReflect                  20/15s -> 40/30s                    Distorted Reflection                  [COMPENSATED] base /4 via mag x2 & dur x2; effective cost kept ~same
```

------------------------------------------------------------

### Spell Absorption

```
Base Cost                                   10.0 -> 2.5
```

```
wild spelldrinker                           1-40/5s -> 1-40/20s                 Wild Spelldrinker                     [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
spell absorption                            10/5s -> 10/20s                     Spell Absorption                      [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
vivec's feast                               10/5s -> 10/40s                     Vivec's Feast                         [COST RAISED] base /4 via dur x8; effective cost x2 (intended pricier); auto-calc cost
weak spelldrinker                           10-20/5s -> 10-20/20s               Weak Spelldrinker                     [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
strong spelldrinker                         20-30/5s -> 20-30/20s               Strong Spelldrinker                   [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
tranasa's spelltrap                         20-30/10s -> 20-30/40s              Tranasa's Spelltrap                   [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Imp_Mys_VivecsFeast                       10/5s -> 40/5s                      St. Horuscia's Alms                   [COMPENSATED] base /4 via mag x4; effective cost kept ~same
```

------------------------------------------------------------

## Restoration

------------------------------------------------------------

### Fortify Fatigue

```
Base Cost                                   0.5 -> 0.25
```

```
vigor                                       5-20/30s -> 10-40/30s               Vigor                                 [COMPENSATED] base /2 via mag x2; effective cost kept ~same; auto-calc cost
```

------------------------------------------------------------

### Fortify Skill

```
Base Cost                                   1.0 -> 4.0
```

```
masterful balanced armor                    15/60s -> 15/15s                    Masterful Balanced Armor              [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful deep biting                       15/60s -> 15/15s                    Masterful Deep Biting                 [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful denial                            15/60s -> 15/15s                    Masterful Denial                      [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful enterprise                        15/60s -> 15/15s                    Masterful Enterprise                  [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful fleetness                         15/60s -> 15/15s                    Masterful Fleetness                   [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful fluid evasion                     15/60s -> 15/15s                    Masterful Fluid Evasion               [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful glib speech                       15/60s -> 15/15s                    Masterful Glib Speech                 [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful golden wisdom                     15/60s -> 15/15s                    Masterful Golden Wisdom               [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful green wisdom                      15/60s -> 15/15s                    Masterful Green Wisdom                [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful hewing                            15/60s -> 15/15s                    Masterful Hewing                      [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful horny fist                        15/60s -> 15/15s                    Masterful Horny Fist                  [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful impaling thrust                   15/60s -> 15/15s                    Masterful Impaling Thrust             [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful leaping                           15/60s -> 15/15s                    Masterful Leaping                     [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful martial craft                     15/60s -> 15/15s                    Masterful Martial Craft               [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful nimble armor                      15/60s -> 15/15s                    Masterful Nimble Armor                [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masteful red wisdom                         15/60s -> 15/15s                    Masterful Red Wisdom                  [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful red wisdom                        15/60s -> 15/15s                    Masterful Red Wisdom                  [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful safekeeping                       15/60s -> 15/15s                    Masterful Safekeeping                 [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful silver wisdom                     15/60s -> 15/15s                    Masterful Silver Wisdom               [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful smiting                           15/60s -> 15/15s                    Masterful Smiting                     [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful stalking                          15/60s -> 15/15s                    Masterful Stalking                    [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masteful stolid armor                       15/60s -> 15/15s                    Masterful Stolid Armor                [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful stolid armor                      15/60s -> 15/15s                    Masterful Stolid Armor                [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful sublime wisdom                    15/60s -> 15/15s                    Masterful Sublime Wisdom              [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful sureflight                        15/60s -> 15/15s                    Masterful Sureflight                  [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful swiftblade                        15/60s -> 15/15s                    Masterful Swiftblade                  [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful transcendant wisdom               15/60s -> 15/15s                    Masterful Transcendant Wisdom -> Masterful Transcendent Wisdom [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost; renamed
masterful transfiguring wisdom              15/60s -> 15/15s                    Masterful Transfiguring Wisdom        [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
masterful unseen wisdom                     15/60s -> 15/15s                    Masterful Unseen Wisdom               [COMPENSATED] base x4 via dur /4; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Nor_Res_EagleEye                          10-15/40s [25 -> 100]               Eagle Eye                             [COST RAISED] base x4 (mag/dur unchanged); effective cost x4 (intended pricier)
T_Nor_Res_TreefellersRage                   10-15/40s [25 -> 100]               Treefellers Rage                      [COST RAISED] base x4 (mag/dur unchanged); effective cost x4 (intended pricier)
T_Com_Res_DeftSecurity                      15/30s [23 -> 92]                   Deft Security                         [COST RAISED] base x4 (mag/dur unchanged); effective cost x4 (intended pricier)
```

------------------------------------------------------------

### Resist Blight Disease

```
Base Cost                                   5.0 -> 0.25
```

```
poet's whim                                 1-30/10s -> 1-30/200s [auto -> 39]  Poet's Whim                           [COMPENSATED] base /20 via dur x20; effective cost kept ~same
vivec's mercy                               20/10s -> 50/80s [auto -> 50]       Vivec's Mercy                         [COMPENSATED] base /20 via mag x2.5 & dur x8; effective cost kept ~same
shield of the armiger                       30/10s -> 100/60s [auto -> 75]      Shield of the Armiger                 [COMPENSATED] base /20 via mag x3.33333 & dur x6; effective cost kept ~same
```

------------------------------------------------------------

### Resist Common Disease

```
Base Cost                                   2.0 -> 0.1
```

```
variable resist common disease              1-30/10s -> 1-30/200s [auto -> 16]  Variable Resist Common Disease        [COMPENSATED] base /20 via dur x20; effective cost kept ~same
resist common disease                       10/5s -> 50/20s [auto -> 5]         Resist Common Disease                 [COMPENSATED] base /20 via mag x5 & dur x4; effective cost kept ~same
seryn's blessing                            20/10s -> 50/80s [auto -> 20]       Seryn's Blessing                      [COMPENSATED] base /20 via mag x2.5 & dur x8; effective cost kept ~same
great resist common disease                 30/10s -> 100/60s [auto -> 30]      Great Resist Common Disease           [COMPENSATED] base /20 via mag x3.33333 & dur x6; effective cost kept ~same
```

*Tamriel Data*
```
T_Imp_Res_SerynsBlessing                    20/10s -> 100/40s                   Pilgrimage of St. Rosunius            [COMPENSATED] base /20 via mag x5 & dur x4; effective cost kept ~same
```

------------------------------------------------------------

### Resist Fire

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist fire                        1-30/10s -> 1-30/40s                Variable Resist Fire                  [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
resist fire                                 10/5s -> 10/20s                     Resist Fire                           [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
strong resist fire                          20/10s -> 20/40s                    Strong Resist Fire                    [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
flameguard                                  20-40/30s -> 20-40/120s             Flameguard                            [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
great resist fire                           30/10s -> 30/40s                    Great Resist Fire                     [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

------------------------------------------------------------

### Resist Frost

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist frost                       1-30/10s -> 1-30/40s                Variable Resist Frost                 [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
resist frost                                10/5s -> 10/20s                     Resist Frost                          [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
strong resist frost                         20/10s -> 20/40s                    Strong Resist Frost                   [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
frostguard                                  20-40/30s -> 20-40/120s             Frostguard                            [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
great resist frost                          30/10s -> 30/40s                    Great Resist Frost                    [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Nor_Res_WinteryMantle                     20/60s -> 80/60s                    Wintery Mantle                        [COMPENSATED] base /4 via mag x4; effective cost kept ~same
```

------------------------------------------------------------

### Resist Magicka

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist magicka                     1-30/10s -> 1-30/40s                Variable Resist Magicka               [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
resist magicka                              10/5s -> 20/20s                     Resist Magicka                        [COST RAISED] base /4 via mag x2 & dur x4; effective cost x2 (intended pricier); auto-calc cost
strong resist magicka                       20/10s -> 20/40s                    Strong Resist Magicka                 [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
magickguard                                 20-40/10s -> 20-40/120s             Magickguard                           [COST RAISED] base /4 via dur x12; effective cost x3 (intended pricier); auto-calc cost
great resist magicka                        30/10s -> 30/40s                    Great Resist Magicka                  [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

------------------------------------------------------------

### Resist Paralysis

```
resist paralysis                            50/30s [300 -> auto]                Resist Paralysis                      auto-calc cost
```

------------------------------------------------------------

### Resist Poison

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist poison                      1-30/10s -> 1-30/40s                Variable Resist Poison                [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
resist poison                               20/5s -> 20/20s                     Resist Poison                         [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
strong resist poison                        20/10s -> 20/40s                    Strong Resist Poison                  [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
poisonguard                                 20-40/30s -> 20-40/120s             Poisonguard                           [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
greater resist poison                       30/10s -> 30/40s                    Greater Resist Poison                 [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

------------------------------------------------------------

### Resist Shock

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist shock                       1-30/10s -> 1-30/40s                Variable Resist Shock                 [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
resist shock                                20/5s -> 20/20s                     Resist Shock                          [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
strong resist shock                         20/10s -> 20/40s                    Strong Resist Shock                   [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
shockguard                                  20-40/30s -> 20-40/120s             Shockguard                            [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
great resist shock                          30/10s -> 30/40s                    Great Resist Shock                    [COMPENSATED] base /4 via dur x4; effective cost kept ~same; auto-calc cost
```

------------------------------------------------------------

### Restore Attribute

```
Base Cost                                   1.0 -> 8.0
```

```
restore agility                             5-20/30s -> 5-20/1s                 Restore Agility                       [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore endurance                           5-20/30s -> 5-20/1s                 Restore Endurance                     [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore intelligence                        5-20/30s -> 5-20/1s                 Restore Intelligence                  [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore luck                                5-20/30s -> 5-20/1s                 Restore Luck                          [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore personality                         5-20/30s -> 5-20/1s                 Restore Personality                   [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore speed                               5-20/30s -> 5-20/1s                 Restore Speed                         [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore strength                            5-20/30s -> 5-20/1s                 Restore Strength                      [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
restore willpower                           5-20/30s -> 5-20/1s                 Restore Willpower                     [COST REDUCED] base x8 via dur /30; effective cost /3.75 (intended cheaper); auto-calc cost
```

------------------------------------------------------------

### Restore Fatigue

```
Base Cost                                   1.0 -> 2.5
```

```
rest of st. merris                          1-10/20s -> 1-10/8s                 Rest of St. Merris -> Rest of St. Meris [COMPENSATED] base x2.5 via dur /2.5; effective cost kept ~same; auto-calc cost; renamed
stamina                                     10-30/30s -> 10-30/12s              Stamina                               [COMPENSATED] base x2.5 via dur /2.5; effective cost kept ~same; auto-calc cost
```

*Tamriel Data*
```
T_Com_Res_WeaponResartus                    42-78/30s -> 30-60/12s [90 -> 68]   Greater Stamina                       [COST REDUCED] base x2.5 via mag /1.33333 & dur /2.5; effective cost /1.33333 (intended cheaper)
```

------------------------------------------------------------

### Restore Health

```
balyna's soothing balm                      3-12/1s -> 5-10/1s                  Balyna's Soothing Balm                [RESCALED] magnitude/duration (no base-cost change); auto-calc cost
balyna's efficacious balm                   3-22/1s -> 5-20/1s                  Balyna's Efficacious Balm             [RESCALED] magnitude/duration (no base-cost change); auto-calc cost
balyna's perfect balm                       3-30/1s -> 5-30/1s                  Balyna's Perfect Balm                 [RESCALED] mag x1.06061 (no base-cost change); auto-calc cost
heal companion                              6-15/1s -> 5-15/1s                  Heal Companion                        [RESCALED] mag /1.05 (no base-cost change); auto-calc cost
```
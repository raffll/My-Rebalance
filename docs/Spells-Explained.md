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
burden                                      20/10s -> 50/40s                    Burden                                base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
burden touch                                20/10s -> 50/40s                    Burden Touch                          base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
weary                                       30-60/10s -> 60-120/50s             Weary                                 base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
great burden of sin                         40/10s -> 80-120/100s               Great Burden of Sin                   base 1.0->0.1 (/10) -> compensation; spell mag·dur x25
heavy burden                                40/10s -> 100/40s                   Heavy Burden                          base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
heavy burden touch                          40/10s -> 100/40s                   Heavy Burden Touch                    base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
burden of sin                               40-60/20s -> 80/50s                 Burden of Sin                         base 1.0->0.1 (/10) -> compensation; spell mag·dur x4
cruel weary                                 50-70/10s -> 100-140/50s            Cruel Weary                           base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
crushing burden                             60/10s -> 150/40s                   Crushing Burden                       base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
crushing burden touch                       60/10s -> 150/40s                   Crushing Burden Touch                 base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
crushing burden of sin                      60-80/30s -> 120-160/150s           Crushing Burden of Sin                base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
dire weary                                  60-90/10s -> 120-180/50s            Dire Weary                            base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
```

*Tamriel Data*
```
T_Com_Alt_WeightOfGuilt                     500/3s -> 5000/3s                   Weight of Guilt                       base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
```

------------------------------------------------------------

### Feather

```
Base Cost                                   1.0 -> 0.1
```

```
feather                                     20/10s -> 40/50s                    Feather                               base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
strong feather                              50/10s -> 100/50s                   Strong Feather                        base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
ulms juicedaw's feather                     50/10s -> 250/20s                   Ulms's Juicedaw's Feather -> Ulms' Juicedaw Feather base 1.0->0.1 (/10) -> compensation; spell mag·dur x10; renamed
great feather                               100/10s -> 200/50s                  Great Feather                         base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
```

*Tamriel Data*
```
T_Imp_Alt_UlmsJuicedawsFeather              50/10s -> 500/10s                   Zenithar's Arms                       base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
T_Com_Alt_Fling                             500/3s -> 5000/3s                   Fling                                 base 1.0->0.1 (/10) -> compensation; spell mag·dur x10
```

------------------------------------------------------------

### Fire Shield

```
fire_fathasa_unique                         1-10/10s                            Fire Barrier -> Fathasa's Fire Barrier renamed
fierce fire shield                          5-11/10s -> 5-10/10s                Fierce Fire Shield                    rebalanced magnitude/duration
strong fire shield                          12/30s -> 15/30s                    Strong Fire Shield                    rebalanced magnitude/duration
```

*Tamriel Data*
```
T_Com_Alt_DaedraFireEye                                                         Fire Eye                              rebalanced magnitude/duration
    Fire Shield                             10-23/20s -> 10-25/20s
    Night Eye                               20/20s
```

------------------------------------------------------------

### Frost Shield

```
frost barrier                               3/10s -> 1-10/10s                   Frost Barrier                         rebalanced magnitude/duration
fierce frost shield                         5-11/10s -> 5-10/10s                Fierce Frost Shield                   rebalanced magnitude/duration
frost_shield                                6/30s -> 5/30s                      Frost Shield -> Weak Frost Shield     rebalanced magnitude/duration; renamed
strong frost shield                         12/30s -> 15/30s                    Strong Frost Shield                   rebalanced magnitude/duration
```

------------------------------------------------------------

### Lightning Shield

```
shock shield                                3/20s                               Shock Shield -> Lightning Shield      renamed
fierce shock shield                         5-11/10s -> 5-10/10s                Fierce Shock Shield                   rebalanced magnitude/duration
lightning shield                            10/30s                              Lightning Shield -> Shock Shield      renamed
strong shock shield                         12/30s -> 15/30s                    Strong Shock Shield                   rebalanced magnitude/duration
```

------------------------------------------------------------

### Lock

```
Base Cost                                   2.0 -> 24.0
```

*Tamriel Data*
```
T_Com_Alt_WizardLock                        20 [2 -> 24]                        Wizard Lock                           base 2.0->24.0 (x12) -> compensation; spell mag·dur x1
T_Com_Alt_DalgorsEntwining                  100 [8 -> 96]                       Dalgor's Entwining                    base 2.0->24.0 (x12) -> compensation; spell mag·dur x1
```

------------------------------------------------------------

### Shield

```
Base Cost                                   2.0 -> 1.0
```

*Tamriel Data*
```
T_Com_Alt_Falling1stBarrier                                                     Falling First Barrier                 base 2.0->1.0 (/2) -> compensation; spell mag·dur x2
    Shield                                  8/40s -> 16/40s
    Shield                                  5/20s -> 10/20s
T_Nor_Alt_TsunsWard                         20/20s -> 40/20s                    Tsun's Ward                           base 2.0->1.0 (/2) -> compensation; spell mag·dur x2
T_Com_Alt_ForceWall                         50/5s -> 100/5s                     Force Wall                            base 2.0->1.0 (/2) -> compensation; spell mag·dur x2
```

------------------------------------------------------------

### Swift Swim

```
Base Cost                                   2.0 -> 0.5
```

```
buoyancy                                    1/20s -> 20/20s                     Buoyancy                              base 2.0->0.5 (/4) -> compensation; spell mag·dur x20
Swimmer's_Blessing                          5/30s -> 50/30s                     Swimmer's Blessing                    base 2.0->0.5 (/4) -> compensation; spell mag·dur x10
```

*Tamriel Data*
```
T_Com_Alt_DreughsGrace                      30/20s -> 120/20s                   Dreugh's Grace                        base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

## Destruction

------------------------------------------------------------

### Damage Fatigue

```
Base Cost                                   4.0 -> 2.0
```

```
fleabite                                    1-10/1s -> 1-20/1s                  Fleabite                              base 4.0->2.0 (/2) -> compensation; spell mag·dur x1.90909
doze                                        1-20/1s -> 1-40/1s                  Doze                                  base 4.0->2.0 (/2) -> compensation; spell mag·dur x1.95238
Aryon_rest                                                                      Aryon's Rest                          base 4.0->2.0 (/2) -> compensation; spell mag·dur x1
    Damage Fatigue                          10/10s
    Burden                                  10/10s -> 100/10s
hornhand                                    15-36/1s -> 30-70/1s                Hornhand                              base 4.0->2.0 (/2) -> compensation; spell mag·dur x1.96078
hand of odros                                                                   Hand of Odros                         base 4.0->2.0 (/2) -> compensation; spell mag·dur x1; rounding: 3-6 has non-5 value
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3-6/120s
    Burden                                  30-40/60s -> 300-400/60s
wrath of odros                                                                  Wrath of Odros                        base 4.0->2.0 (/2) -> compensation; spell mag·dur x1
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3/120s
    Burden                                  20-30/50s -> 200-300/50s
```

------------------------------------------------------------

### Damage Health

```
black hand                                                                      Black Hand                            rebalanced magnitude/duration
    Damage Health                           5-12/1s -> 5-10/1s
    Poison                                  5-12/1s -> 5-10/1s
stormhand                                                                       Stormhand                             rebalanced magnitude/duration
    Damage Health                           5-12/1s -> 5-10/1s
    Shock Damage                            5-12/1s -> 5-10/1s
```

------------------------------------------------------------

### Damage Magicka

```
Base Cost                                   8.0 -> 4.0
```

```
soulpinch                                   1-20/1s -> 1-40/1s                  Soulpinch                             base 8.0->4.0 (/2) -> compensation; spell mag·dur x1.95238
```

*Tamriel Data*
```
T_Com_Des_Magefire                          10-30/1s -> 10-30/2s                Thimble of Magefire                   base 8.0->4.0 (/2) -> compensation; spell mag·dur x2
```

------------------------------------------------------------

### Disintegrate Armor

```
Base Cost                                   6.0 -> 0.6
```

```
bm_draugr_curse                             [200 -> auto]                       Eddard's Wrath                        base 6.0->0.6 (/10) -> compensation; spell mag·dur x10
    Disintegrate Armor                      4-9/15s -> 40-90/15s
    Disintegrate Weapon                     4-9/15s -> 40-90/15s
disintegrate armor                          6-25/1s -> 60-250/1s                Disintegrate Armor                    base 6.0->0.6 (/10) -> compensation; spell mag·dur x10
armor eater                                 10-30/1s -> 200-600/1s              Armor Eater                           base 6.0->0.6 (/10) -> compensation; spell mag·dur x20
```

*Tamriel Data*
```
T_Rea_Des_ShadowRust                                                            Shadow Rust                           base 6.0->0.6 (/10) -> compensation; spell mag·dur x10
    Disintegrate Armor                      1-5/20s -> 10-50/20s
    Burden                                  1-15/20s -> 10-150/20s
T_Com_Trp_Acid                                                                  Acid Trap                             base 6.0->0.6 (/10) -> compensation; spell mag·dur x10; rounding: 2-4 has non-5 value
    Disintegrate Armor                      20-40/1s -> 20-40/10s
    Disintegrate Weapon                     20-40/1s -> 20-40/5s
    Poison                                  2-4/5s
T_Com_Des_FractureArmor                     100/2s -> 1000/2s                   Fracture Armor                        base 6.0->0.6 (/10) -> compensation; spell mag·dur x10
T_Com_Trp_AcidMaster                                                            Master Acid Trap                      base 6.0->0.6 (/10) -> compensation; spell mag·dur x10
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
disintegrate weapon                         6-25/1s -> 30-125/1s                Disintegrate Weapon                   base 6.0->1.2 (/5) -> compensation; spell mag·dur x5
weapon eater                                6-25/1s -> 100-300/1s               Weapon Eater                          base 6.0->1.2 (/5) -> compensation; spell mag·dur x12.9032
```

*Tamriel Data*
```
T_Rea_Des_IronEater                         1-25/2s -> 5-125/2s                 Iron Eater                            base 6.0->1.2 (/5) -> compensation; spell mag·dur x5
T_Rea_Des_SteelEater                        5-30/3s -> 25-150/3s                Steel Eater                           base 6.0->1.2 (/5) -> compensation; spell mag·dur x5
```

------------------------------------------------------------

### Drain Attribute

```
blood despair                               7-14/60s -> 5-15/60s                Blood Despair                         rebalanced magnitude/duration
```

------------------------------------------------------------

### Drain Fatigue

```
Base Cost                                   2.0 -> 0.2
```

```
weariness                                   1-10/1s -> 10-100/20s               Weariness                             base 2.0->0.2 (/10) -> compensation; spell mag·dur x200
sleep                                       5-15/30s -> 25-75/60s               Sleep                                 base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
wild exhaustion                             5-15/60s -> 25-75/120s              Wild Exhaustion                       base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
exhausting touch                            5-20/60s -> 25-100/120s             Exhausting Touch                      base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
exhaustion                                  5-20/90s -> 25-100/180s             Exhaustion                            base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
ordeal of st. olms                          5-20/60s -> 50-200/60s              Ordeal of St. Olms                    base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
wearying touch                              5-20/30s -> 25-100/60s              Wearying Touch                        base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
dagoth's bosom                              20/30s -> 200/30s                   Dagoth's Bosom                        base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
```

*Tamriel Data*
```
T_Com_Des_Duck                              200/2s -> 2000/2s                   Duck                                  base 2.0->0.2 (/10) -> compensation; spell mag·dur x10
```

------------------------------------------------------------

### Drain Health

```
ash feast                                   3/30s -> 30/3s                      Ash Feast                             rebalanced magnitude/duration
```

------------------------------------------------------------

### Drain Magicka

```
Base Cost                                   4.0 -> 0.4
```

```
magicka leech                               6-15/60s -> 5-15/60s                Magicka Leech                         base 4.0->0.4 (/10) -> compensation; spell mag·dur /1.05
```

*Tamriel Data*
```
T_Rea_Mys_SoulWither                                                            Dhamcka's Soul-Withering              base 4.0->0.4 (/10) -> compensation; spell mag·dur x10
    Drain Magicka                           1/30s -> 10/30s
    Soul Trap                               1/30s
T_Com_Des_RageOfMagnus                      60/10s -> 300/20s                   Rage of Magnus                        base 4.0->0.4 (/10) -> compensation; spell mag·dur x10
```

------------------------------------------------------------

### Fire Damage

```
Base Cost                                   5.0 -> 8.0
```

```
cruel firebloom                             10-16/1s -> 10-15/1s                Cruel Firebloom                       no-scale: magnitude kept vanilla; base 5.0->8.0 affects cost only
god's fire                                  11-60/10s -> 10-60/10s              God's Fire                            no-scale: magnitude kept vanilla; base 5.0->8.0 affects cost only
```

------------------------------------------------------------

### Frost Damage

```
Base Cost                                   5.0 -> 8.0
```

```
brittlewind                                                                     Brittlewind                           no-scale: magnitude kept vanilla; base 5.0->8.0 affects cost only
    Frost Damage                            10/10s
    Disintegrate Armor                      20/10s -> 200/10s
god's frost                                 11-60/10s -> 10-60/10s              God's Frost                           no-scale: magnitude kept vanilla; base 5.0->8.0 affects cost only
```

------------------------------------------------------------

### Poison

```
Base Cost                                   9.0 -> 8.0
```

```
poison_powerful                             2-15/10s -> 1-15/10s                Toxic Cloud                           no-scale: magnitude kept vanilla; base 9.0->8.0 affects cost only
poison                                      2-20/1s -> 1-20/1s                  Poison                                no-scale: magnitude kept vanilla; base 9.0->8.0 affects cost only
```

------------------------------------------------------------

### Shock Damage

```
Base Cost                                   7.0 -> 8.0
```

```
lightning storm                             2-10/10s -> 1-10/10s                Lightning Storm                       no-scale: magnitude kept vanilla; base 7.0->8.0 affects cost only
spark                                       2-20/1s -> 1-20/1s                  Spark                                 no-scale: magnitude kept vanilla; base 7.0->8.0 affects cost only
shockball_large                             2-40/1s -> 1-40/1s                  Greater Shockball                     no-scale: magnitude kept vanilla; base 7.0->8.0 affects cost only
shockball                                   2-40/1s -> 1-20/1s                  Shockball                             no-scale: magnitude kept vanilla; base 7.0->8.0 affects cost only
```

------------------------------------------------------------

### Weakness to Fire

```
dire weakness to fire                       2-60/10s -> 1-60/10s                Dire Weakness to Fire                 rebalanced magnitude/duration
```

------------------------------------------------------------

### Weakness to Frost

```
dire weakness to frost                      2-60/10s -> 1-60/10s                Dire Weakness to Frost                rebalanced magnitude/duration
```

------------------------------------------------------------

### Weakness to Magicka

```
dire weakness to magicka                    2-60/10s -> 1-60/10s                Dire Weakness to Magicka              rebalanced magnitude/duration
```

------------------------------------------------------------

### Weakness to Poison

```
dire weakness to poison                     2-60/10s -> 1-60/10s                Dire Weakness to Poison               rebalanced magnitude/duration
```

------------------------------------------------------------

### Weakness to Shock

```
dire weakness to shock                      2-60/10s -> 1-60/10s                Dire Weakness to Shock                rebalanced magnitude/duration
```

------------------------------------------------------------

## Illusion

------------------------------------------------------------

### Blind

```
crying eye                                  1-10/5s -> 1-10/20s                 Crying Eye                            rebalanced magnitude/duration
erelvam's wild sty                          1-40/10s -> 1-40/20s                Erelvam's Wild Sty                    rebalanced magnitude/duration
heavy_eyes_unique                                                               Harthoon's Heavy Eyes                 changed
    Blind                                   100/10s
    Burden                                  100/10s -> 1000/10s
```

------------------------------------------------------------

### Chameleon

```
shadow form                                 6-15/30s -> 12-30/30s               Shadow Form                           rebalanced magnitude/duration; rounding: 12-30 has non-5 value
```

------------------------------------------------------------

### Charm

```
Base Cost                                   5.0 -> 2.5
```

*Tamriel Data*
```
T_Com_Ilu_AlluringSpeech                    15-20/20s [80 -> 40]                Alluring Speech                       base 5.0->2.5 (/2) -> compensation; spell mag·dur x1
```

------------------------------------------------------------

### Invisibility

```
invisibility                                30s -> 60s                          Invisibility                          rebalanced magnitude/duration
```

------------------------------------------------------------

### Paralyze

```
Base Cost                                   40.0 -> 80.0
```

```
scrib_paralysis                             6s -> 12s [auto -> 6]               Paralysis                             base 40.0->80.0 (x2) -> compensation; spell mag·dur x2
BM_paralyze_hirc                            [46 -> 50]                          Hunter's Venom                        base 40.0->80.0 (x2) -> compensation; spell mag·dur x1
    Paralyze                                10s
    Burden                                  50/10s -> 500/10s
```

*Tamriel Data*
```
T_Com_Ilu_Paralysis                         3s [6 -> 12]                        Paralysis                             base 40.0->80.0 (x2) -> compensation; spell mag·dur x1
T_Com_Ilu_LivingStatue                      20s [30 -> 60]                      Living Statue                         base 40.0->80.0 (x2) -> compensation; spell mag·dur x1
```

------------------------------------------------------------

### Sanctuary

```
sotha's grace                               1-20/5s -> 1-20/10s                 Sotha's Grace                         rebalanced magnitude/duration
father's hand                               1-40/5s -> 1-40/10s                 Father's Hand                         rebalanced magnitude/duration
```

------------------------------------------------------------

### Sound

```
Base Cost                                   3.0 -> 1.0
```

```
wild earwig                                 1-30/5s -> 1-90/5s                  Wild Earwig                           base 3.0->1.0 (/3) -> compensation; spell mag·dur x2.93548
dire noise                                  2-60/5s -> 1-60/15s                 Dire Noise                            base 3.0->1.0 (/3) -> compensation; spell mag·dur x2.95161
earwig                                      3-8/5s -> 10-25/5s                  Earwig                                base 3.0->1.0 (/3) -> compensation; spell mag·dur x3.18182
noise                                       3-8/5s -> 1-10/15s                  Noise                                 base 3.0->1.0 (/3) -> compensation; spell mag·dur x3
cruel earwig                                5-11/5s -> 15-35/5s                 Cruel Earwig                          base 3.0->1.0 (/3) -> compensation; spell mag·dur x3.125
dire earwig                                 8-15/5s -> 25-45/5s                 Dire Earwig                           base 3.0->1.0 (/3) -> compensation; spell mag·dur x3.04348
cruel noise                                 10-22/5s -> 10-20/15s               Cruel Noise                           base 3.0->1.0 (/3) -> compensation; spell mag·dur x2.8125
```

*Tamriel Data*
```
T_Com_Ilu_Voices                            50/20s -> 50/60s [100 -> 50]        Voices                                base 3.0->1.0 (/3) -> compensation; spell mag·dur x3
```

------------------------------------------------------------

## Mysticism

------------------------------------------------------------

### Absorb Attribute

```
absorb intelligence [ranged]                5-51/30s -> 5-50/30s                Absorb Intelligence [Ranged]          rebalanced magnitude/duration
```

------------------------------------------------------------

### Absorb Fatigue

```
Base Cost                                   4.0 -> 6.0
```

```
absorb fatigue                              5-20/30s -> 5-20/3s                 Absorb Fatigue                        base 4.0->6.0 (x1.5) -> compensation; spell mag·dur /10
absorb fatigue [ranged]                     5-20/30s -> 5-20/3s                 Absorb Fatigue [Ranged]               base 4.0->6.0 (x1.5) -> compensation; spell mag·dur /10
energy leech                                5-20/30s -> 5-20/6s                 Energy Leech                          base 4.0->6.0 (x1.5) -> compensation; spell mag·dur /5
Tap Energy                                  20/30s -> 20/3s                     Tap Energy                            base 4.0->6.0 (x1.5) -> compensation; spell mag·dur /10
```

------------------------------------------------------------

### Absorb Health

```
Base Cost                                   8.0 -> 16.0
```

```
absorb health                               5-52/1s -> 5-50/1s                  Absorb Health                         base 8.0->16.0 (x2) -> compensation; spell mag·dur /1.03636
```

*Tamriel Data*
```
T_Com_Mys_Lifesteal                         40/1s [24 -> 48]                    Lifesteal                             base 8.0->16.0 (x2) -> compensation; spell mag·dur x1
```

------------------------------------------------------------

### Detect Animal

```
Base Cost                                   0.75 -> 0.15
```

*Tamriel Data*
```
T_Com_Mys_DetectHumanoid                    100-300/5s [38 -> 8]                Greater Detect Creature               base 0.75->0.15 (/5) -> compensation; spell mag·dur x1
```

------------------------------------------------------------

### Detect Enchantment

```
Base Cost                                   1.0 -> 0.2
```

```
detect enchantment                          10/10s -> 50/10s                    Detect Enchantment                    base 1.0->0.2 (/5) -> compensation; spell mag·dur x5
```

*Tamriel Data*
```
T_Com_Mys_Insight                           150/10s -> 50/10s [75 -> auto]      Greater Detect Enchantment -> Detect Enchantment VIOLATION: TD spell on AUTO_CALCULATE; base 1.0->0.2 (/5) -> compensation; spell mag·dur /3; renamed
```

------------------------------------------------------------

### Detect Key

```
Base Cost                                   1.0 -> 0.2
```

```
tevral's hawkshaw                           10/10s -> 50/10s                    Tevral's Hawkshaw                     base 1.0->0.2 (/5) -> compensation; spell mag·dur x5
detect_key                                  50/5s -> 250/5s                     Detect Key                            base 1.0->0.2 (/5) -> compensation; spell mag·dur x5
```

------------------------------------------------------------

### Reflect

```
Base Cost                                   10.0 -> 2.5
```

```
wild reflect                                1-40/10s -> 1-40/40s                Wild Reflect                          base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
sotha's mirror                              10/5s -> 10/20s                     Sotha's Mirror                        base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
reflect                                     10-20/5s -> 10-20/20s               Reflect                               base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
shalidor's mirror                           10-30/10s -> 10-30/40s              Shalidor's Mirror                     base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
llivam's reversal                           20-30/10s -> 20-30/40s              Llivam's Reversal                     base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
strong reflect                              20-30/5s -> 20-30/20s               Strong Reflect                        base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
```

*Tamriel Data*
```
T_Com_Mys_ReflectDamage                     1-5/50s -> 15/30s [76 -> 56]        Minor Reflect -> Reflect Damage       base 10.0->2.5 (/4) -> compensation; spell mag·dur x3; renamed
T_Imp_Res_SothasMirror                      10/5s -> 40/5s                      St. Naharine's Shield                 base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
T_Com_Mys_DistortedReflect                  20/15s -> 40/30s                    Distorted Reflection                  base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

### Spell Absorption

```
Base Cost                                   10.0 -> 2.5
```

```
wild spelldrinker                           1-40/5s -> 1-40/20s                 Wild Spelldrinker                     base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
spell absorption                            10/5s -> 10/20s                     Spell Absorption                      base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
vivec's feast                               10/5s -> 10/40s                     Vivec's Feast                         base 10.0->2.5 (/4) -> compensation; spell mag·dur x8
weak spelldrinker                           10-20/5s -> 10-20/20s               Weak Spelldrinker                     base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
strong spelldrinker                         20-30/5s -> 20-30/20s               Strong Spelldrinker                   base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
tranasa's spelltrap                         20-30/10s -> 20-30/40s              Tranasa's Spelltrap                   base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
```

*Tamriel Data*
```
T_Imp_Mys_VivecsFeast                       10/5s -> 40/5s                      St. Horuscia's Alms                   base 10.0->2.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

## Restoration

------------------------------------------------------------

### Fortify Fatigue

```
Base Cost                                   0.5 -> 0.25
```

```
vigor                                       5-20/30s -> 10-40/30s               Vigor                                 base 0.5->0.25 (/2) -> compensation; spell mag·dur x2
```

------------------------------------------------------------

### Fortify Skill

```
Base Cost                                   1.0 -> 4.0
```

```
masterful balanced armor                    15/60s -> 15/15s                    Masterful Balanced Armor              base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful deep biting                       15/60s -> 15/15s                    Masterful Deep Biting                 base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful denial                            15/60s -> 15/15s                    Masterful Denial                      base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful enterprise                        15/60s -> 15/15s                    Masterful Enterprise                  base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful fleetness                         15/60s -> 15/15s                    Masterful Fleetness                   base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful fluid evasion                     15/60s -> 15/15s                    Masterful Fluid Evasion               base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful glib speech                       15/60s -> 15/15s                    Masterful Glib Speech                 base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful golden wisdom                     15/60s -> 15/15s                    Masterful Golden Wisdom               base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful green wisdom                      15/60s -> 15/15s                    Masterful Green Wisdom                base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful hewing                            15/60s -> 15/15s                    Masterful Hewing                      base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful horny fist                        15/60s -> 15/15s                    Masterful Horny Fist                  base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful impaling thrust                   15/60s -> 15/15s                    Masterful Impaling Thrust             base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful leaping                           15/60s -> 15/15s                    Masterful Leaping                     base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful martial craft                     15/60s -> 15/15s                    Masterful Martial Craft               base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful nimble armor                      15/60s -> 15/15s                    Masterful Nimble Armor                base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masteful red wisdom                         15/60s -> 15/15s                    Masterful Red Wisdom                  base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful red wisdom                        15/60s -> 15/15s                    Masterful Red Wisdom                  base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful safekeeping                       15/60s -> 15/15s                    Masterful Safekeeping                 base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful silver wisdom                     15/60s -> 15/15s                    Masterful Silver Wisdom               base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful smiting                           15/60s -> 15/15s                    Masterful Smiting                     base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful stalking                          15/60s -> 15/15s                    Masterful Stalking                    base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masteful stolid armor                       15/60s -> 15/15s                    Masterful Stolid Armor                base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful stolid armor                      15/60s -> 15/15s                    Masterful Stolid Armor                base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful sublime wisdom                    15/60s -> 15/15s                    Masterful Sublime Wisdom              base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful sureflight                        15/60s -> 15/15s                    Masterful Sureflight                  base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful swiftblade                        15/60s -> 15/15s                    Masterful Swiftblade                  base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful transcendant wisdom               15/60s -> 15/15s                    Masterful Transcendant Wisdom -> Masterful Transcendent Wisdom base 1.0->4.0 (x4) -> compensation; spell mag·dur /4; renamed
masterful transfiguring wisdom              15/60s -> 15/15s                    Masterful Transfiguring Wisdom        base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
masterful unseen wisdom                     15/60s -> 15/15s                    Masterful Unseen Wisdom               base 1.0->4.0 (x4) -> compensation; spell mag·dur /4
```

*Tamriel Data*
```
T_Nor_Res_EagleEye                          10-15/40s [25 -> 100]               Eagle Eye                             base 1.0->4.0 (x4) -> compensation; spell mag·dur x1
T_Nor_Res_TreefellersRage                   10-15/40s [25 -> 100]               Treefellers Rage                      base 1.0->4.0 (x4) -> compensation; spell mag·dur x1
T_Com_Res_DeftSecurity                      15/30s [23 -> 92]                   Deft Security                         base 1.0->4.0 (x4) -> compensation; spell mag·dur x1
```

------------------------------------------------------------

### Resist Blight Disease

```
Base Cost                                   5.0 -> 0.25
```

```
poet's whim                                 1-30/10s -> 1-30/200s [auto -> 39]  Poet's Whim                           base 5.0->0.25 (/20) -> compensation; spell mag·dur x20
vivec's mercy                               20/10s -> 50/80s [auto -> 50]       Vivec's Mercy                         base 5.0->0.25 (/20) -> compensation; spell mag·dur x20
shield of the armiger                       30/10s -> 100/60s [auto -> 75]      Shield of the Armiger                 base 5.0->0.25 (/20) -> compensation; spell mag·dur x20
```

------------------------------------------------------------

### Resist Common Disease

```
Base Cost                                   2.0 -> 0.1
```

```
variable resist common disease              1-30/10s -> 1-30/200s [auto -> 16]  Variable Resist Common Disease        base 2.0->0.1 (/20) -> compensation; spell mag·dur x20
resist common disease                       10/5s -> 50/20s [auto -> 5]         Resist Common Disease                 base 2.0->0.1 (/20) -> compensation; spell mag·dur x20
seryn's blessing                            20/10s -> 50/80s [auto -> 20]       Seryn's Blessing                      base 2.0->0.1 (/20) -> compensation; spell mag·dur x20
great resist common disease                 30/10s -> 100/60s [auto -> 30]      Great Resist Common Disease           base 2.0->0.1 (/20) -> compensation; spell mag·dur x20
```

*Tamriel Data*
```
T_Imp_Res_SerynsBlessing                    20/10s -> 100/40s                   Pilgrimage of St. Rosunius            base 2.0->0.1 (/20) -> compensation; spell mag·dur x20
```

------------------------------------------------------------

### Resist Fire

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist fire                        1-30/10s -> 1-30/40s                Variable Resist Fire                  base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
resist fire                                 10/5s -> 10/20s                     Resist Fire                           base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
strong resist fire                          20/10s -> 20/40s                    Strong Resist Fire                    base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
flameguard                                  20-40/30s -> 20-40/120s             Flameguard                            base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
great resist fire                           30/10s -> 30/40s                    Great Resist Fire                     base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

### Resist Frost

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist frost                       1-30/10s -> 1-30/40s                Variable Resist Frost                 base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
resist frost                                10/5s -> 10/20s                     Resist Frost                          base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
strong resist frost                         20/10s -> 20/40s                    Strong Resist Frost                   base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
frostguard                                  20-40/30s -> 20-40/120s             Frostguard                            base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
great resist frost                          30/10s -> 30/40s                    Great Resist Frost                    base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

*Tamriel Data*
```
T_Nor_Res_WinteryMantle                     20/60s -> 80/60s                    Wintery Mantle                        base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

### Resist Magicka

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist magicka                     1-30/10s -> 1-30/40s                Variable Resist Magicka               base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
resist magicka                              10/5s -> 20/20s                     Resist Magicka                        base 2.0->0.5 (/4) -> compensation; spell mag·dur x8
strong resist magicka                       20/10s -> 20/40s                    Strong Resist Magicka                 base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
magickguard                                 20-40/10s -> 20-40/120s             Magickguard                           base 2.0->0.5 (/4) -> compensation; spell mag·dur x12
great resist magicka                        30/10s -> 30/40s                    Great Resist Magicka                  base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

### Resist Paralysis

```
resist paralysis                            50/30s [300 -> auto]                Resist Paralysis                      cost recomputed
```

------------------------------------------------------------

### Resist Poison

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist poison                      1-30/10s -> 1-30/40s                Variable Resist Poison                base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
resist poison                               20/5s -> 20/20s                     Resist Poison                         base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
strong resist poison                        20/10s -> 20/40s                    Strong Resist Poison                  base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
poisonguard                                 20-40/30s -> 20-40/120s             Poisonguard                           base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
greater resist poison                       30/10s -> 30/40s                    Greater Resist Poison                 base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

### Resist Shock

```
Base Cost                                   2.0 -> 0.5
```

```
variable resist shock                       1-30/10s -> 1-30/40s                Variable Resist Shock                 base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
resist shock                                20/5s -> 20/20s                     Resist Shock                          base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
strong resist shock                         20/10s -> 20/40s                    Strong Resist Shock                   base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
shockguard                                  20-40/30s -> 20-40/120s             Shockguard                            base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
great resist shock                          30/10s -> 30/40s                    Great Resist Shock                    base 2.0->0.5 (/4) -> compensation; spell mag·dur x4
```

------------------------------------------------------------

### Restore Attribute

```
Base Cost                                   1.0 -> 8.0
```

```
restore agility                             5-20/30s -> 5-20/1s                 Restore Agility                       base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore endurance                           5-20/30s -> 5-20/1s                 Restore Endurance                     base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore intelligence                        5-20/30s -> 5-20/1s                 Restore Intelligence                  base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore luck                                5-20/30s -> 5-20/1s                 Restore Luck                          base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore personality                         5-20/30s -> 5-20/1s                 Restore Personality                   base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore speed                               5-20/30s -> 5-20/1s                 Restore Speed                         base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore strength                            5-20/30s -> 5-20/1s                 Restore Strength                      base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
restore willpower                           5-20/30s -> 5-20/1s                 Restore Willpower                     base 1.0->8.0 (x8) -> compensation; spell mag·dur /30
```

------------------------------------------------------------

### Restore Fatigue

```
Base Cost                                   1.0 -> 2.5
```

```
rest of st. merris                          1-10/20s -> 1-10/8s                 Rest of St. Merris -> Rest of St. Meris base 1.0->2.5 (x2.5) -> compensation; spell mag·dur /2.5; renamed
stamina                                     10-30/30s -> 10-30/12s              Stamina                               base 1.0->2.5 (x2.5) -> compensation; spell mag·dur /2.5
```

*Tamriel Data*
```
T_Com_Res_WeaponResartus                    42-78/30s -> 30-60/12s [90 -> 68]   Greater Stamina                       base 1.0->2.5 (x2.5) -> compensation; spell mag·dur /3.33333
```

------------------------------------------------------------

### Restore Health

```
balyna's soothing balm                      3-12/1s -> 5-10/1s                  Balyna's Soothing Balm                rebalanced magnitude/duration
balyna's efficacious balm                   3-22/1s -> 5-20/1s                  Balyna's Efficacious Balm             rebalanced magnitude/duration
balyna's perfect balm                       3-30/1s -> 5-30/1s                  Balyna's Perfect Balm                 rebalanced magnitude/duration
heal companion                              6-15/1s -> 5-15/1s                  Heal Companion                        rebalanced magnitude/duration
```
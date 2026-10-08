# Remastered Rebalance Redux - Spells (Explained)

Generated companion to `R3 - Spells.md`. Same layout, with an extra
explanation column noting which rule produced each change. Only spells
that differ from vanilla are listed. Rows tagged `[NEW]` are
player-buyable Tamriel Rebuilt / Tamriel Data spells that are NOT yet
in the mod and that need rebalancing before import (a scalable effect's
base cost changed, or a no-scale effect needs a cost/rounding fix);
spells needing no change are omitted. Each is shown with a `PROPOSE:`
note giving the values and cost it would get if added, computed per
`docs/Spell-Rules-Reference.md`.
Non-`[NEW]` rows are unchanged mod spells. Rules: see
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
burden                                      20/10s -> 50/40s                    Burden                                                                mag x2.5, dur x4 = x10 compensated ✓
burden touch                                20/10s -> 50/40s                    Burden Touch                                                          mag x2.5, dur x4 = x10 compensated ✓
weary                                       30-60/10s -> 60-120/50s             Weary                                                                 mag x2, dur x5 = x10 compensated ✓
great burden of sin                         40/10s -> 80-120/100s               Great Burden of Sin                                                   mag x2.5, dur x10 = x25 ✗ (expected x10)
heavy burden                                40/10s -> 100/40s                   Heavy Burden                                                          mag x2.5, dur x4 = x10 compensated ✓
heavy burden touch                          40/10s -> 100/40s                   Heavy Burden Touch                                                    mag x2.5, dur x4 = x10 compensated ✓
burden of sin                               40-60/20s -> 80/50s                 Burden of Sin                                                         mag x1.5, dur x2.5 = x4 ✗ (expected x10)
cruel weary                                 50-70/10s -> 100-140/50s            Cruel Weary                                                           mag x2, dur x5 = x10 compensated ✓
crushing burden                             60/10s -> 150/40s                   Crushing Burden                                                       mag x2.5, dur x4 = x10 compensated ✓
crushing burden touch                       60/10s -> 150/40s                   Crushing Burden Touch                                                 mag x2.5, dur x4 = x10 compensated ✓
crushing burden of sin                      60-80/30s -> 120-160/150s           Crushing Burden of Sin                                                mag x2, dur x5 = x10 compensated ✓
dire weary                                  60-90/10s -> 120-180/50s            Dire Weary                                                            mag x2, dur x5 = x10 compensated ✓
```

*Tamriel Data*
```
T_Com_Alt_WeightOfGuilt                     500/3s -> 5000/3s                   Weight of Guilt                                                       mag x10, dur x1 = x10 compensated ✓
```

------------------------------------------------------------

### Feather

```
Base Cost                                   1.0 -> 0.1
```

```
feather                                     20/10s -> 40/50s                    Feather                                                               mag x2, dur x5 = x10 compensated ✓
strong feather                              50/10s -> 100/50s                   Strong Feather                                                        mag x2, dur x5 = x10 compensated ✓
ulms juicedaw's feather                     50/10s -> 250/20s                   Ulms's Juicedaw's Feather -> Ulms' Juicedaw Feather                   mag x5, dur x2 = x10 compensated ✓; renamed
great feather                               100/10s -> 200/50s                  Great Feather                                                         mag x2, dur x5 = x10 compensated ✓
```

*Tamriel Data*
```
T_Nor_Alt_UlmsJuicedawsFeather              50/10s                              Thelen Kaarn's Feather [NEW]                                          PROPOSE: dur x10 (base /10 compensation) -> 50/100s, cost 25 [recalc]
T_Imp_Alt_UlmsJuicedawsFeather              50/10s -> 500/10s                   Zenithar's Arms                                                       mag x10, dur x1 = x10 compensated ✓
T_Com_Alt_Fling                             500/3s -> 5000/3s                   Fling                                                                 mag x10, dur x1 = x10 compensated ✓
```

------------------------------------------------------------

### Fire Shield

```
fire_fathasa_unique                         1-10/10s                            Fire Barrier -> Fathasa's Fire Barrier                                renamed
fierce fire shield                          5-11/10s -> 5-10/10s                Fierce Fire Shield                                                    rounded
strong fire shield                          12/30s -> 15/30s                    Strong Fire Shield                                                    rescaled mag x1
```

*Tamriel Data*
```
T_Com_Alt_DaedraFireEye                                                         Fire Eye                                                              rounded
    Fire Shield                             10-23/20s -> 10-25/20s
    Night Eye                               20/20s
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

```
lock                                        5                                   Lock [NEW]                                                            PROPOSE: mag /12 (base x12 compensation) -> 1, cost 1.2 [recalc]
fenrick's doorjam                           10                                  Fenrick's Doorjam [NEW]                                               PROPOSE: mag /12 (base x12 compensation) -> 1, cost 1.2 [recalc]
```

*Tamriel Data*
```
T_Com_Alt_WizardLock                        20 [2 -> 24]                        Wizard Lock                                                           mag/dur held; cost x12 compensated via cost ✓
T_Com_Alt_DalgorsEntwining                  100 [8 -> 96]                       Dalgor's Entwining                                                    mag/dur held; cost x12 compensated via cost ✓
```

------------------------------------------------------------

### Open

```
Base Cost                                   6.0 -> 12.0
```

```
wild open                                   1-100                               Wild Open [NEW]                                                       PROPOSE: mag /2 (base x2 compensation) -> 1-50, cost 15.3 [recalc]
open                                        20                                  Open [NEW]                                                            PROPOSE: mag /2 (base x2 compensation) -> 10, cost 6 [recalc]
great open                                  50                                  Great Open [NEW]                                                      PROPOSE: mag /2 (base x2 compensation) -> 25, cost 15 [recalc]
ondusi's open door                          50                                  Ondusi's Open Door [NEW]                                              PROPOSE: mag /2 (base x2 compensation) -> 25, cost 15 [recalc]
strong open                                 50                                  Strong Open [NEW]                                                     PROPOSE: mag /2 (base x2 compensation) -> 25, cost 15 [recalc]
```

------------------------------------------------------------

### Shield

```
Base Cost                                   2.0 -> 1.0
```

```
second barrier                              20/30s                              Second Barrier [NEW]                                                  PROPOSE: dur x2 (base /2 compensation) -> 20/60s, cost 60 [recalc]
third barrier                               30/30s                              Third Barrier [NEW]                                                   PROPOSE: dur x2 (base /2 compensation) -> 30/60s, cost 90 [recalc]
fourth barrier                              40/30s                              Fourth Barrier [NEW]                                                  PROPOSE: dur x2 (base /2 compensation) -> 40/60s, cost 120 [recalc]
fifth barrier                               50/30s                              Fifth Barrier [NEW]                                                   PROPOSE: dur x2 (base /2 compensation) -> 50/60s, cost 150 [recalc]
sixth barrier                               60/30s                              Sixth Barrier [NEW]                                                   PROPOSE: dur x2 (base /2 compensation) -> 60/60s, cost 180 [recalc]
```

*Tamriel Data*
```
T_Com_Alt_Falling1stBarrier                                                     Falling First Barrier                                                 mag x2, dur x1 = x2 compensated ✓
    Shield                                  8/40s -> 16/40s
    Shield                                  5/20s -> 10/20s
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
TR_m7_AI_Savi_Swim                          40/15s                              Savi's Swift-Stroke [NEW]                                             PROPOSE: dur x4 (base /4 compensation) -> 40/60s, cost 60 [recalc]
```

*Tamriel Data*
```
T_Com_Alt_DreughsGrace                      30/20s -> 120/20s                   Dreugh's Grace                                                        mag x4, dur x1 = x4 compensated ✓
```

------------------------------------------------------------

## Destruction

------------------------------------------------------------

### Damage Attribute

```
Base Cost                                   8.0 -> 24.0
```

```
evil eye                                    1-10/1s                             Evil Eye [NEW]                                                        PROPOSE: dur /3 (base x3 compensation) -> 1-10/1s, cost 6.6 [recalc]
clench                                      1-20/1s                             Clench [NEW]                                                          PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
emasculate                                  1-20/1s                             Emasculate [NEW]                                                      PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
fuddle                                      1-20/1s                             Fuddle [NEW]                                                          PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
gripes                                      1-20/1s                             Gripes [NEW]                                                          PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
hex                                         1-20/1s                             Hex [NEW]                                                             PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
stumble                                     1-20/1s                             Stumble [NEW]                                                         PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
woe                                         1-20/1s                             Woe [NEW]                                                             PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 12.6 [recalc]
dread curse: strength                       5-12/1s                             Dread Curse: Strength [NEW]                                           PROPOSE: dur /3 (base x3 compensation) -> 5-12/1s, cost 10.2 [recalc]
```

*Tamriel Data*
```
T_De_Des_SphereWeakness                     1-20/1s                             Felms' Punishment [NEW]                                               PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 32.4 [recalc]
T_Com_Des_SphereWeakness                    1-20/1s                             Sphere of Weakness [NEW]                                              PROPOSE: dur /3 (base x3 compensation) -> 1-20/1s, cost 32.4 [recalc]
```

------------------------------------------------------------

### Damage Fatigue

```
Base Cost                                   4.0 -> 2.0
```

```
fleabite                                    1-10/1s -> 1-20/1s                  Fleabite                                                              mag x2, dur x1 = x2 compensated ✓
doze                                        1-20/1s -> 1-40/1s                  Doze                                                                  mag x2, dur x1 = x2 compensated ✓
knuckle luck                                3-120/1s                            Knuckle Luck [NEW]                                                    PROPOSE: dur x2 (base /2 compensation) -> 3-120/2s, cost 12.3 [recalc]
Aryon_rest                                                                      Aryon's Rest                                                          mag x1, dur x1 = x1 ✗ (expected x2)
    Damage Fatigue                          10/10s
    Burden                                  10/10s -> 100/10s
blood curse: fatigue                        10-20/5s                            Blood Curse: Fatigue [NEW]                                            PROPOSE: dur x2 (base /2 compensation) -> 10-20/10s, cost 22.5 [recalc]
hornhand                                    15-36/1s -> 30-70/1s                Hornhand                                                              mag x2, dur x1 = x2 compensated ✓
ironhand                                    21-42/1s                            Ironhand [NEW]                                                        PROPOSE: dur x2 (base /2 compensation) -> 21-42/2s, cost 6.3 [recalc]
hand of odros                                                                   Hand of Odros                                                         mag x1, dur x1 = x1 ✗ (expected x2); rounding ✗ (3-6)
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3-6/120s
    Burden                                  30-40/60s -> 300-400/60s
wrath of odros                                                                  Wrath of Odros                                                        mag x1, dur x1 = x1 ✗ (expected x2)
    Damage Fatigue                          60/1s
    Absorb Attribute: Agility               3/120s
    Burden                                  20-30/50s -> 200-300/50s
```

------------------------------------------------------------

### Damage Health

```
five fingers of pain                                                            Five Fingers of Pain [NEW]                                            PROPOSE: import as-is (no base-cost change), cost 6.6 +4 effects [cost-only]
    Damage Health                           3-5/1s
    Fire Damage                             3-5/1s
    Frost Damage                            3-5/1s
    Shock Damage                            3-5/1s
    Demoralize Humanoid                     3-5/1s
black hand                                                                      Black Hand                                                            rounded
    Damage Health                           5-12/1s -> 5-10/1s
    Poison                                  5-12/1s -> 5-10/1s
stormhand                                                                       Stormhand                                                             rounded
    Damage Health                           5-12/1s -> 5-10/1s
    Shock Damage                            5-12/1s -> 5-10/1s
vivec's_wrath                                                                   Vivec's Wrath [NEW]                                                   PROPOSE: import as-is (no base-cost change), cost 36 +3 effects [cost-only]
    Damage Health                           10-20/1s
    Fire Damage                             10-20/1s
    Frost Damage                            10-20/1s
    Shock Damage                            10-20/1s
firefist                                                                        Firefist [NEW]                                                        PROPOSE: import as-is (no base-cost change), cost 13.6 +1 effects [cost-only]
    Damage Health                           10-24/1s
    Fire Damage                             10-24/1s
frostfist                                                                       Frostfist [NEW]                                                       PROPOSE: import as-is (no base-cost change), cost 13.6 +1 effects [cost-only]
    Damage Health                           10-24/1s
    Frost Damage                            10-24/1s
```

*Tamriel Data*
```
T_Rea_Des_MeatRot                                                               Meat Rot [NEW]                                                        PROPOSE: import as-is (no base-cost change), cost 15.6 +1 effects [recalc]
    Damage Health                           1-20/2s
    Damage Attribute: Strength              1-5/2s
T_De_Des_IndGuardMothersIre                                                     Mother's Ire [NEW]                                                    PROPOSE: import as-is (no base-cost change), cost 50.25 +3 effects [recalc]
    Damage Health                           2/15s
    Fire Damage                             2/15s
    Damage Fatigue                          20/1s
    Drain Attribute: Strength               15/10s
```

------------------------------------------------------------

### Damage Magicka

```
Base Cost                                   8.0 -> 4.0
```

```
soulpinch                                   1-20/1s -> 1-40/1s                  Soulpinch                                                             mag x2, dur x1 = x2 compensated ✓
grave curse: spell points                   2-4/10s                             Grave Curse: Magicka [NEW]                                            PROPOSE: dur x2 (base /2 compensation) -> 2-4/20s, cost 18 [recalc]
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
bm_draugr_curse                             [200 -> auto]                       Eddard's Wrath                                                        mag x10, dur x1 = x10 compensated ✓
    Disintegrate Armor                      4-9/15s -> 40-90/15s
    Disintegrate Weapon                     4-9/15s -> 40-90/15s
disintegrate armor                          6-25/1s -> 60-250/1s                Disintegrate Armor                                                    mag x10, dur x1 = x10 compensated ✓
armor eater                                 10-30/1s -> 200-600/1s              Armor Eater                                                           mag x20, dur x1 = x20 ✗ (expected x10)
```

*Tamriel Data*
```
T_Rea_Des_ShadowRust                                                            Shadow Rust                                                           mag x10, dur x1 = x10 compensated ✓
    Disintegrate Armor                      1-5/20s -> 10-50/20s
    Burden                                  1-15/20s -> 10-150/20s
T_Com_Trp_Acid                                                                  Acid Trap                                                             mag x1, dur x10 = x10 compensated ✓; rounding ✗ (2-4)
    Disintegrate Armor                      20-40/1s -> 20-40/10s
    Disintegrate Weapon                     20-40/1s -> 20-40/5s
    Poison                                  2-4/5s
T_Com_Des_FractureArmor                     100/2s -> 1000/2s                   Fracture Armor                                                        mag x10, dur x1 = x10 compensated ✓
T_Com_Trp_AcidMaster                                                            Master Acid Trap                                                      mag x1, dur x10 = x10 compensated ✓
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
Ghost Curse                                                                     Ghost Curse [NEW]                                                     PROPOSE: import as-is (no base-cost change), cost 12.7 +2 effects [recalc]
    Drain Attribute: Endurance              5/30s
    Drain Fatigue                           10/30s
    Damage Health                           1-10/1s
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
drain blood                                                                     Drain Blood [NEW]                                                     PROPOSE: import as-is (no base-cost change), cost 33 +1 effects [recalc]
    Drain Health                            5/30s
    Drain Magicka                           5/30s
```

------------------------------------------------------------

### Drain Magicka

```
Base Cost                                   4.0 -> 0.4
```

```
gash spirit                                 5-20/30s                            Gash Spirit [NEW]                                                     PROPOSE: dur x10 (base /10 compensation) -> 5-20/300s, cost 75 [recalc]
gash spirit [ranged]                        5-20/30s                            Gash Spirit [Ranged] [NEW]                                            PROPOSE: dur x10 (base /10 compensation) -> 5-20/300s, cost 112.5 [recalc]
magicka leech                               6-15/60s -> 5-15/60s                Magicka Leech                                                         mag /1, dur x1 = /1 ✗ (expected x10)
wizard rend                                                                     Wizard Rend [NEW]                                                     PROPOSE: dur x10 (base /10 compensation) -> 10-35/40s, cost 51 +1 effects [recalc]
    Drain Magicka                           10-35/4s
    Paralyze                                4s
```

*Tamriel Data*
```
T_Rea_Mys_SoulWither                                                            Dhamcka's Soul-Withering                                              mag x10, dur x1 = x10 compensated ✓
    Drain Magicka                           1/30s -> 10/30s
    Soul Trap                               1/30s
T_Com_Des_RageOfMagnus                      60/10s -> 300/20s                   Rage of Magnus                                                        mag x5, dur x2 = x10 compensated ✓
```

------------------------------------------------------------

### Fire Damage

```
Base Cost                                   5.0 -> 8.0
```

```
fire storm                                  1-10/10s                            Fire Storm [NEW]                                                      PROPOSE: keep mag/dur, cost -> 36 (no-scale) [cost-only]
flame                                       1-15/1s                             Flame [NEW]                                                           PROPOSE: keep mag/dur, cost -> 3.2 (no-scale) [cost-only]
firebloom                                   1-25/5s                             Firebloom [NEW]                                                       PROPOSE: keep mag/dur, cost -> 42 (no-scale) [cost-only]
fireball                                    2-20/1s                             Fireball [NEW]                                                        PROPOSE: keep mag/dur, cost -> 8.1 (no-scale) round 1-20 [cost-only]
Fireball_large                              2-40/1s                             Greater Fireball [NEW]                                                PROPOSE: keep mag/dur, cost -> 15.6 (no-scale) round 1-40 [cost-only]
cruel firebloom                             10-16/1s -> 10-15/1s                Cruel Firebloom                                                       no-scale
flamebolt                                   10-50/2s                            Flamebolt [NEW]                                                       PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
god's fire                                  11-60/10s -> 10-60/10s              God's Fire                                                            no-scale
fire bite                                   15-30/1s                            Fire Bite [NEW]                                                       PROPOSE: keep mag/dur, cost -> 9 (no-scale) [cost-only]
TR_m3_RenesaFire                                                                Renesa's Hindering Flames [NEW]                                       PROPOSE: keep mag/dur, cost -> 108.431 (no-scale) round 20-40 +2 effects [recalc]
    Fire Damage                             21-39/3s
    Fire Damage                             5-9/10s
    Burden                                  150/3s
TR_m7_IndrasiFire                                                               Flameblast [NEW]                                                      PROPOSE: keep mag/dur, cost -> 43.8 (no-scale) round 55-135 +1 effects [cost-only]
    Fire Damage                             54-134/0s
    Fire Damage                             4-8/8s
```

*Tamriel Data*
```
T_Com_Des_IgniteFoe                         1-5/60s                             Ignite Foe [NEW]                                                      PROPOSE: keep mag/dur, cost -> 108.3 (no-scale) [cost-only]
T_Com_Des_Wildfire                          1-15/5s                             Wildfire [NEW]                                                        PROPOSE: keep mag/dur, cost -> 24 (no-scale) [cost-only]
T_De_Des_IndGuardJudgement                                                      Judgement Ordained [NEW]                                              PROPOSE: keep mag/dur, cost -> 58.5 (no-scale) +3 effects [cost-only]
    Fire Damage                             2/15s
    Shock Damage                            2/15s
    Drain Attribute: Agility                15/10s
    Drain Attribute: Speed                  15/10s
```

------------------------------------------------------------

### Frost Damage

```
Base Cost                                   5.0 -> 8.0
```

```
frost storm                                 1-10/10s                            Frost Storm [NEW]                                                     PROPOSE: keep mag/dur, cost -> 36 (no-scale) [cost-only]
frostbloom                                  1-25/5s                             Frostbloom [NEW]                                                      PROPOSE: keep mag/dur, cost -> 42 (no-scale) [cost-only]
frostball                                   2-20/1s                             Frostball [NEW]                                                       PROPOSE: keep mag/dur, cost -> 8.1 (no-scale) round 1-20 [cost-only]
Frostball_large                             2-40/1s                             Greater Frostball [NEW]                                               PROPOSE: keep mag/dur, cost -> 15.6 (no-scale) round 1-40 [cost-only]
brittlewind                                                                     Brittlewind                                                           no-scale
    Frost Damage                            10/10s
    Disintegrate Armor                      20/10s -> 200/10s
frost bolt                                  10-50/2s                            Frost Bolt [NEW]                                                      PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
god's frost                                 11-60/10s -> 10-60/10s              God's Frost                                                           no-scale
freezing touch                              15-30/1s                            Freezing Touch [NEW]                                                  PROPOSE: keep mag/dur, cost -> 9 (no-scale) [cost-only]
frostbite                                   15-30/1s                            Frostbite [NEW]                                                       PROPOSE: keep mag/dur, cost -> 9 (no-scale) [cost-only]
TR_m7_IndrasiFrost                          18-46/4s                            Freezing Gale [NEW]                                                   PROPOSE: keep mag/dur, cost -> 84.3 (no-scale) round 20-45 [cost-only]
```

*Tamriel Data*
```
T_Com_Des_IceStorm                          1-30/5s                             Ice Storm [NEW]                                                       PROPOSE: keep mag/dur, cost -> 52.5 (no-scale) [cost-only]
T_Com_Des_IceBolt                           1-35/5s                             Ice Bolt [NEW]                                                        PROPOSE: keep mag/dur, cost -> 54 (no-scale) [cost-only]
T_Nor_Des_MountainWind                                                          Mountain Wind [NEW]                                                   PROPOSE: keep mag/dur, cost -> 69 (no-scale) +1 effects [recalc]
    Frost Damage                            5-10/5s
    Paralyze                                5s
T_Com_Des_MaidRime                          30-75/2s                            Maid of Rime [NEW]                                                    PROPOSE: keep mag/dur, cost -> 42 (no-scale) [cost-only]
```

------------------------------------------------------------

### Poison

```
Base Cost                                   9.0 -> 8.0
```

```
deadly poison                               1-20/10s                            Deadly Poison [NEW]                                                   PROPOSE: keep mag/dur, cost -> 42 (no-scale) [cost-only]
deadly poison [ranged]                      1-20/10s                            Deadly Poison [Ranged] [NEW]                                          PROPOSE: keep mag/dur, cost -> 63 (no-scale) [cost-only]
poisonbloom                                 1-20/5s                             Poisonbloom [NEW]                                                     PROPOSE: keep mag/dur, cost -> 34.5 (no-scale) [cost-only]
viperbite                                   1-30/1s                             Viperbite [NEW]                                                       PROPOSE: keep mag/dur, cost -> 6.2 (no-scale) [cost-only]
viper                                       2-8/1s                              Viper [NEW]                                                           PROPOSE: keep mag/dur, cost -> 2 (no-scale) round 1-10 [cost-only]
poison_powerful                             2-15/10s -> 1-15/10s                Toxic Cloud                                                           no-scale
poison                                      2-20/1s -> 1-20/1s                  Poison                                                                no-scale
viperbolt                                   10-50/2s                            Viperbolt [NEW]                                                       PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
poisonous touch                             15-40/1s                            Poisonous Touch [NEW]                                                 PROPOSE: keep mag/dur, cost -> 11 (no-scale) [cost-only]
potent poison                               20-40/5s                            Potent Poison [NEW]                                                   PROPOSE: keep mag/dur, cost -> 60 (no-scale) [cost-only]
potent poison [ranged]                      20-40/5s                            Potent Poison [Ranged] [NEW]                                          PROPOSE: keep mag/dur, cost -> 90 (no-scale) [cost-only]
```

*Tamriel Data*
```
T_Cr_Des_SkyrenderPoison                                                        Poison Sting [NEW]                                                    PROPOSE: keep mag/dur, cost -> 17.6 (no-scale) +1 effects [recalc]
    Poison                                  6/4s
    Paralyze                                2s
```

------------------------------------------------------------

### Shock Damage

```
Base Cost                                   7.0 -> 8.0
```

```
shock                                       1-15/1s                             Shock [NEW]                                                           PROPOSE: keep mag/dur, cost -> 3.2 (no-scale) [cost-only]
shockbloom                                  1-25/5s                             Shockbloom [NEW]                                                      PROPOSE: keep mag/dur, cost -> 42 (no-scale) [cost-only]
lightning storm                             2-10/10s -> 1-10/10s                Lightning Storm                                                       no-scale
spark                                       2-20/1s -> 1-20/1s                  Spark                                                                 no-scale
shockball_large                             2-40/1s -> 1-40/1s                  Greater Shockball                                                     no-scale
shockball                                   2-40/1s -> 1-20/1s                  Shockball                                                             no-scale
wild shockbloom                             2-40/1s                             Wild Shockbloom [NEW]                                                 PROPOSE: keep mag/dur, cost -> 15.6 (no-scale) round 1-40 [cost-only]
shocking touch                              3-30/1s                             Shocking Touch [NEW]                                                  PROPOSE: keep mag/dur, cost -> 6.6 (no-scale) round 5-30 [cost-only]
god's spark                                 5-50/10s                            God's Spark [NEW]                                                     PROPOSE: keep mag/dur, cost -> 168 (no-scale) [cost-only]
lightning bolt                              10-50/2s                            Lightning Bolt [NEW]                                                  PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
shockbite                                   35-45/2s                            Shockbite [NEW]                                                       PROPOSE: keep mag/dur, cost -> 32 (no-scale) [cost-only]
TR_m3_ReveaTelamSpell                                                           Thunderclap [NEW]                                                     PROPOSE: keep mag/dur, cost -> 49.25 (no-scale) +1 effects [recalc]
    Shock Damage                            35-45/2s
    Sound                                   60/5s
dire shockball                              40-50/0s                            Dire Shockball [NEW]                                                  PROPOSE: keep mag/dur, cost -> 0 (no-scale) [cost-only]
TR_m7_IndrasiShock                                                              Conduction [NEW]                                                      PROPOSE: keep mag/dur, cost -> 12 (no-scale) round 45-100 +2 effects [cost-only]
    Shock Damage                            47-102/0s
    Shock Damage                            23-48/0s
    Shock Damage                            12-25/0s
TR_m7_SigillahShock                                                             Sigillah's Mind Blast [NEW]                                           PROPOSE: keep mag/dur, cost -> 32.625 (no-scale) round 70-125 +2 effects [recalc]
    Shock Damage                            68-124/0s
    Absorb Health                           10-27/0s
    Absorb Attribute: Intelligence          40/3s
```

*Tamriel Data*
```
T_Com_Des_Lightning                         1-25/5s                             Lightning [NEW]                                                       PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
T_Com_Des_WindsStorm                        30-75/2s                            Winds of Storm [NEW]                                                  PROPOSE: keep mag/dur, cost -> 63 (no-scale) [cost-only]
```

------------------------------------------------------------

### Weakness to Common Disease

*Tamriel Data*
```
T_Com_Des_CauseDisease                                                          Cause Disease [NEW]                                                   PROPOSE: import as-is (no base-cost change), cost 88.8 +4 effects [recalc]
    Weakness to Common Disease              10-30/20s
    Damage Attribute: Strength              2-6/1s
    Damage Attribute: Agility               2-6/1s
    Damage Attribute: Speed                 2-6/1s
    Damage Attribute: Endurance             2-6/1s
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
heavy_eyes_unique                                                               Harthoon's Heavy Eyes                                                 changed
    Blind                                   100/10s
    Burden                                  100/10s -> 1000/10s
```

------------------------------------------------------------

### Chameleon

```
shadow form                                 6-15/30s -> 12-30/30s               Shadow Form                                                           rescaled mag x2; rounding ✗ (12-30)
```

------------------------------------------------------------

### Charm

```
Base Cost                                   5.0 -> 2.5
```

```
charming touch                              30/30s                              Charming Touch [NEW]                                                  PROPOSE: dur x2 (base /2 compensation) -> 30/60s, cost 225 [recalc]
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
TR_m3_RenasoGalsLight                                                           Dazzling Flourish [NEW]                                               PROPOSE: dur /2 (base x2 compensation) -> 2s, cost 66.5625 +2 effects [recalc]
    Paralyze                                5s
    Light                                   35-65/10s
    Sound                                   35-50/5s
scrib_paralysis                             6s -> 12s [auto -> 6]               Paralysis                                                             mag x1, dur x2 = x2 ✗ (expected /2)
BM_paralyze_hirc                            [46 -> 50]                          Hunter's Venom                                                        mag x1, dur x1 = x1 ✗ (expected /2)
    Paralyze                                10s
    Burden                                  50/10s -> 500/10s
TR_m3_DravaynParalyze                       15s                                 Halt [NEW]                                                            PROPOSE: dur /2 (base x2 compensation) -> 8s, cost 93 [recalc]
medusa's gaze                               15s                                 Medusa's Gaze [NEW]                                                   PROPOSE: dur /2 (base x2 compensation) -> 8s, cost 48 [recalc]
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
TR_m3_ArvsWeaken                                                                Arvs' Confounding [NEW]                                               PROPOSE: dur x3 (base /3 compensation) -> 30-40/30s, cost 70 +2 effects [recalc]
    Sound                                   30-40/10s
    Blind                                   30-40/10s
    Damage Attribute: Agility               10/0s
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

*Tamriel Data*
```
T_Com_Mys_Tag                               40-50/8s                            Tag [NEW]                                                             PROPOSE: dur /1.5 (base x1.5 compensation) -> 40-50/5s, cost 67.5 [recalc]
```

------------------------------------------------------------

### Absorb Health

```
Base Cost                                   8.0 -> 16.0
```

```
absorb health [ranged]                      5-20/1s                             Absorb Health [Ranged] [NEW]                                          PROPOSE: dur /2 (base x2 compensation) -> 5-20/1s, cost 15 [recalc]
absorb health                               5-52/1s -> 5-50/1s                  Absorb Health                                                         mag /1, dur x1 = /1 ✗ (expected /2)
righteousness                               10/1s                               Righteousness [NEW]                                                   PROPOSE: dur /2 (base x2 compensation) -> 10/1s, cost 8 [recalc]
TR_m7_AmataryaAbsorb                                                            Amatarya's Repurposing [NEW]                                          PROPOSE: dur /2 (base x2 compensation) -> 15-20/2s, cost 106.5 +1 effects [recalc]
    Absorb Health                           15-20/5s
    Absorb Fatigue                          20-30/5s
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
T_Com_Mys_DetectEnemy                       57/20s                              Greater Detect Enchantment [NEW]                                      PROPOSE: dur x5 (base /5 compensation) -> 57/100s, cost 57 [recalc]
T_Com_Mys_DetectValuables                   60/20s                              Greater Detect Enchantment [NEW]                                      PROPOSE: dur x5 (base /5 compensation) -> 60/100s, cost 60 [recalc]
T_Com_Mys_Insight                           150/10s -> 50/10s [75 -> auto]      Greater Detect Enchantment -> Detect Enchantment                      TD-AUTOCALC ✗; mag /3, dur x1 = /3 ✗ (expected x5); renamed
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

*Tamriel Data*
```
T_Com_Mys_DetectInvisibility                100/15s                             Greater Detect Key [NEW]                                              PROPOSE: dur x5 (base /5 compensation) -> 100/75s, cost 75 [recalc]
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
T_Com_Mys_ReflectDamage                     1-5/50s -> 15/30s [76 -> 56]        Minor Reflect -> Reflect Damage                                       mag x5, dur /1.5 = x3 ✗ (expected x4); renamed
T_Nor_Mys_SothasMirror                      10/5s                               Jhunal's Intercession [NEW]                                           PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
T_Com_Mys_SpellReflection                   10/5s                               Spell Reflection [NEW]                                                PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
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
T_Nor_Mys_VivecsFeast                       10/5s                               Alduin's Maw [NEW]                                                    PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
T_Com_Mys_SpellAbsorption                   10/5s                               Spell Absorption [NEW]                                                PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
T_Imp_Mys_VivecsFeast                       10/5s -> 40/5s                      St. Horuscia's Alms                                                   mag x4, dur x1 = x4 compensated ✓
```

------------------------------------------------------------

## Restoration

------------------------------------------------------------

### Fortify Attribute

```
TR_m7_Prestidigitation                                                          Prestidigitation [NEW]                                                PROPOSE: import as-is (no base-cost change), cost 112.5 +3 effects [recalc]
    Fortify Attribute: Speed                10-20/15s
    Fortify Attribute: Agility              10-20/15s
    Fortify Skill: Sneak                    10-20/15s
    Fortify Skill: Security                 10-20/15s
```

------------------------------------------------------------

### Fortify Fatigue

```
Base Cost                                   0.5 -> 0.25
```

```
enrichment                                  5-20/30s                            Enrichment [NEW]                                                      PROPOSE: dur x2 (base /2 compensation) -> 5-20/60s, cost 9.375 [recalc]
vigor                                       5-20/30s -> 10-40/30s               Vigor                                                                 mag x2, dur x1 = x2 compensated ✓
```

------------------------------------------------------------

### Fortify Skill

```
Base Cost                                   1.0 -> 4.0
```

```
fortify restoration skill                   10/60s                              Fortify Restoration Skill [NEW]                                       PROPOSE: dur /4 (base x4 compensation) -> 10/15s, cost 30 [recalc]
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
blightguard                                 10/5s                               Blightguard [NEW]                                                     PROPOSE: dur x20 (base /20 compensation) -> 10/100s, cost 12.5 [recalc]
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
T_Nor_Res_SerynsBlessing                    20/10s                              Dibella's Whisper [NEW]                                               PROPOSE: dur x20 (base /20 compensation) -> 20/200s, cost 20 [recalc]
T_Rga_Res_SerynsBlessing                    20/10s                              Four Hands of Morwha [NEW]                                            PROPOSE: dur x20 (base /20 compensation) -> 20/200s, cost 20 [recalc]
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
resist magicka                              10/5s -> 20/20s                     Resist Magicka                                                        mag x2, dur x4 = x8 ✗ (expected x4)
strong resist magicka                       20/10s -> 20/40s                    Strong Resist Magicka                                                 mag x1, dur x4 = x4 compensated ✓
magickguard                                 20-40/10s -> 20-40/120s             Magickguard                                                           mag x1, dur x12 = x12 ✗ (expected x4)
great resist magicka                        30/10s -> 30/40s                    Great Resist Magicka                                                  mag x1, dur x4 = x4 compensated ✓
TR_m7_Intercession                          100/10s                             Intercession [NEW]                                                    PROPOSE: dur x4 (base /4 compensation) -> 100/40s, cost 100 [recalc]
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
restore agility                             5-20/30s -> 5-20/1s                 Restore Agility                                                       mag x1, dur /30 = /30 ✗ (expected /8)
restore endurance                           5-20/30s -> 5-20/1s                 Restore Endurance                                                     mag x1, dur /30 = /30 ✗ (expected /8)
restore intelligence                        5-20/30s -> 5-20/1s                 Restore Intelligence                                                  mag x1, dur /30 = /30 ✗ (expected /8)
restore luck                                5-20/30s -> 5-20/1s                 Restore Luck                                                          mag x1, dur /30 = /30 ✗ (expected /8)
restore personality                         5-20/30s -> 5-20/1s                 Restore Personality                                                   mag x1, dur /30 = /30 ✗ (expected /8)
restore speed                               5-20/30s -> 5-20/1s                 Restore Speed                                                         mag x1, dur /30 = /30 ✗ (expected /8)
restore strength                            5-20/30s -> 5-20/1s                 Restore Strength                                                      mag x1, dur /30 = /30 ✗ (expected /8)
restore willpower                           5-20/30s -> 5-20/1s                 Restore Willpower                                                     mag x1, dur /30 = /30 ✗ (expected /8)
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
T_Imp_Res_RestStMerris                      1-10/20s                            Breath of Morihaus [NEW]                                              PROPOSE: dur /2.5 (base x2.5 compensation) -> 1-10/8s, cost 5.5 [recalc]
T_Com_Res_WeaponResartus                    42-78/30s -> 30-60/12s [90 -> 68]   Greater Stamina                                                       mag /1.5, dur /2.5 = /3 ✗ (expected /2.5)
```

------------------------------------------------------------

### Restore Health

```
balyna's soothing balm                      3-12/1s -> 5-10/1s                  Balyna's Soothing Balm                                                rounded
balyna's efficacious balm                   3-22/1s -> 5-20/1s                  Balyna's Efficacious Balm                                             rounded
balyna's perfect balm                       3-30/1s -> 5-30/1s                  Balyna's Perfect Balm                                                 rounded
heal companion                              6-15/1s -> 5-15/1s                  Heal Companion                                                        rounded
```
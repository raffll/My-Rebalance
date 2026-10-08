# Remastered Rebalance Redux - TR Buyable Spells (Propositions)

Player-buyable Tamriel Rebuilt / Tamriel Data spells that are NOT yet in
`R3 - Spells.json` and that need rebalancing before import (`Recalc = Yes`
= a scalable effect's base cost changed, or `Cost only` = a no-scale
effect needs a cost/rounding fix). Import-as-is spells (`Recalc = -`) are
omitted. Each row shows the TR spell's current values and a `PROPOSE:`
note giving the values and cost it should take if imported, computed per
`docs/Spell-Rules-Reference.md`. Same layout as `docs/Spells-Explained.md`.
Source list: `docs/TR-Buyable-Spells.md`. Do not hand-edit; regenerate
with `python scripts/gen_tr_propositions.py`.

------------------------------------------------------------

## Alteration

------------------------------------------------------------

### Feather

```
Base Cost                                   1.0 -> 0.1
```

*Tamriel Data*
```
T_Dae_Alt_UNI_WabbajackTrans                1/15s                               Wabbajack [NEW]                                                       PROPOSE: dur x10 (base /10 compensation) -> 1/150s, cost 1.125 [recalc]
T_Nor_Alt_UlmsJuicedawsFeather              50/10s                              Thelen Kaarn's Feather [NEW]                                          PROPOSE: dur x10 (base /10 compensation) -> 50/100s, cost 25 [recalc]
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

------------------------------------------------------------

### Swift Swim

```
Base Cost                                   2.0 -> 0.5
```

```
TR_m7_AI_Savi_Swim                          40/15s                              Savi's Swift-Stroke [NEW]                                             PROPOSE: dur x4 (base /4 compensation) -> 40/60s, cost 60 [recalc]
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
knuckle luck                                3-120/1s                            Knuckle Luck [NEW]                                                    PROPOSE: dur x2 (base /2 compensation) -> 3-120/2s, cost 12.3 [recalc]
blood curse: fatigue                        10-20/5s                            Blood Curse: Fatigue [NEW]                                            PROPOSE: dur x2 (base /2 compensation) -> 10-20/10s, cost 22.5 [recalc]
ironhand                                    21-42/1s                            Ironhand [NEW]                                                        PROPOSE: dur x2 (base /2 compensation) -> 21-42/2s, cost 6.3 [recalc]
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
grave curse: spell points                   2-4/10s                             Grave Curse: Magicka [NEW]                                            PROPOSE: dur x2 (base /2 compensation) -> 2-4/20s, cost 18 [recalc]
```

------------------------------------------------------------

### Drain Attribute

```
Ghost Curse                                                                     Ghost Curse [NEW]                                                     PROPOSE: import as-is (no base-cost change), cost 12.7 +2 effects [recalc]
    Drain Attribute: Endurance              5/30s
    Drain Fatigue                           10/30s
    Damage Health                           1-10/1s
```

------------------------------------------------------------

### Drain Health

```
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
wild flay spirit                            1-20/3s                             Wild Flay Spirit [NEW]                                                PROPOSE: dur x10 (base /10 compensation) -> 1-20/30s, cost 9.45 [recalc]
flay spirit                                 5-20/60s                            Flay Spirit [NEW]                                                     PROPOSE: dur x10 (base /10 compensation) -> 5-20/600s, cost 150 [recalc]
gash spirit                                 5-20/30s                            Gash Spirit [NEW]                                                     PROPOSE: dur x10 (base /10 compensation) -> 5-20/300s, cost 75 [recalc]
gash spirit [ranged]                        5-20/30s                            Gash Spirit [Ranged] [NEW]                                            PROPOSE: dur x10 (base /10 compensation) -> 5-20/300s, cost 112.5 [recalc]
wizard rend                                                                     Wizard Rend [NEW]                                                     PROPOSE: dur x10 (base /10 compensation) -> 10-35/40s, cost 51 +1 effects [recalc]
    Drain Magicka                           10-35/4s
    Paralyze                                4s
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
flamebolt                                   10-50/2s                            Flamebolt [NEW]                                                       PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
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
frost bolt                                  10-50/2s                            Frost Bolt [NEW]                                                      PROPOSE: keep mag/dur, cost -> 39 (no-scale) [cost-only]
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

## Illusion

------------------------------------------------------------

### Charm

```
Base Cost                                   5.0 -> 2.5
```

```
charm mortal                                10-30/30s                           Charm Mortal [NEW]                                                    PROPOSE: dur x2 (base /2 compensation) -> 10-30/60s, cost 225 [recalc]
charming touch                              30/30s                              Charming Touch [NEW]                                                  PROPOSE: dur x2 (base /2 compensation) -> 30/60s, cost 225 [recalc]
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
TR_m3_DravaynParalyze                       15s                                 Halt [NEW]                                                            PROPOSE: dur /2 (base x2 compensation) -> 8s, cost 93 [recalc]
medusa's gaze                               15s                                 Medusa's Gaze [NEW]                                                   PROPOSE: dur /2 (base x2 compensation) -> 8s, cost 48 [recalc]
```

------------------------------------------------------------

### Sound

```
Base Cost                                   3.0 -> 1.0
```

```
TR_m3_ArvsWeaken                                                                Arvs' Confounding [NEW]                                               PROPOSE: dur x3 (base /3 compensation) -> 30-40/30s, cost 70 +2 effects [recalc]
    Sound                                   30-40/10s
    Blind                                   30-40/10s
    Damage Attribute: Agility               10/0s
```

------------------------------------------------------------

## Mysticism

------------------------------------------------------------

### Absorb Fatigue

```
Base Cost                                   4.0 -> 6.0
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
righteousness                               10/1s                               Righteousness [NEW]                                                   PROPOSE: dur /2 (base x2 compensation) -> 10/1s, cost 8 [recalc]
TR_m7_AmataryaAbsorb                                                            Amatarya's Repurposing [NEW]                                          PROPOSE: dur /2 (base x2 compensation) -> 15-20/2s, cost 106.5 +1 effects [recalc]
    Absorb Health                           15-20/5s
    Absorb Fatigue                          20-30/5s
```

------------------------------------------------------------

### Detect Enchantment

```
Base Cost                                   1.0 -> 0.2
```

*Tamriel Data*
```
T_Com_Mys_DetectEnemy                       57/20s                              Greater Detect Enchantment [NEW]                                      PROPOSE: dur x5 (base /5 compensation) -> 57/100s, cost 57 [recalc]
T_Com_Mys_DetectValuables                   60/20s                              Greater Detect Enchantment [NEW]                                      PROPOSE: dur x5 (base /5 compensation) -> 60/100s, cost 60 [recalc]
T_Com_Mys_UNI_Passwall                      480/4s                              Passwall [NEW]                                                        PROPOSE: dur x5 (base /5 compensation) -> 480/20s, cost 96 [recalc]
```

------------------------------------------------------------

### Detect Key

```
Base Cost                                   1.0 -> 0.2
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

*Tamriel Data*
```
T_Nor_Mys_SothasMirror                      10/5s                               Jhunal's Intercession [NEW]                                           PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
T_Com_Mys_SpellReflection                   10/5s                               Spell Reflection [NEW]                                                PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
```

------------------------------------------------------------

### Spell Absorption

```
Base Cost                                   10.0 -> 2.5
```

*Tamriel Data*
```
T_Nor_Mys_VivecsFeast                       10/5s                               Alduin's Maw [NEW]                                                    PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
T_Com_Mys_SpellAbsorption                   10/5s                               Spell Absorption [NEW]                                                PROPOSE: dur x4 (base /4 compensation) -> 10/20s, cost 25 [recalc]
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
daedric fatigue                             50/90s                              Daedric Fatigue [NEW]                                                 PROPOSE: dur x2 (base /2 compensation) -> 50/180s, cost 112.5 [recalc]
```

------------------------------------------------------------

### Fortify Skill

```
Base Cost                                   1.0 -> 4.0
```

```
fortify restoration skill                   10/60s                              Fortify Restoration Skill [NEW]                                       PROPOSE: dur /4 (base x4 compensation) -> 10/15s, cost 30 [recalc]
```

------------------------------------------------------------

### Resist Blight Disease

```
Base Cost                                   5.0 -> 0.25
```

```
blightguard                                 10/5s                               Blightguard [NEW]                                                     PROPOSE: dur x20 (base /20 compensation) -> 10/100s, cost 12.5 [recalc]
```

------------------------------------------------------------

### Resist Common Disease

```
Base Cost                                   2.0 -> 0.1
```

*Tamriel Data*
```
T_Nor_Res_SerynsBlessing                    20/10s                              Dibella's Whisper [NEW]                                               PROPOSE: dur x20 (base /20 compensation) -> 20/200s, cost 20 [recalc]
T_Rga_Res_SerynsBlessing                    20/10s                              Four Hands of Morwha [NEW]                                            PROPOSE: dur x20 (base /20 compensation) -> 20/200s, cost 20 [recalc]
```

------------------------------------------------------------

### Resist Magicka

```
Base Cost                                   2.0 -> 0.5
```

```
TR_m7_Intercession                          100/10s                             Intercession [NEW]                                                    PROPOSE: dur x4 (base /4 compensation) -> 100/40s, cost 100 [recalc]
```

------------------------------------------------------------

### Restore Fatigue

```
Base Cost                                   1.0 -> 2.5
```

*Tamriel Data*
```
T_Imp_Res_RestStMerris                      1-10/20s                            Breath of Morihaus [NEW]                                              PROPOSE: dur /2.5 (base x2.5 compensation) -> 1-10/8s, cost 5.5 [recalc]
```
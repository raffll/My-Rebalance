# Player-Buyable Spells — Tamriel Rebuilt / Tamriel Data

Every spell sold by at least one spell merchant (merchants placed in the TR province plugins (TR_Mainland, Cyr_Main, Sky_Main)). A spell is listed when an NPC with the `OFFERS_SPELLS` service knows it and its record is of type `Spell` (abilities, powers, curses and diseases are excluded).

**Total unique buyable spells: 534**

- Already in `R3 - Spells.json`: **175**
- Need recalc (scalable effect base cost changed): **194**
- Cost-only fix (no-scale effect base cost changed): **57**

## Legend

- **Mag**: per-effect magnitude; `30-50` is a min-max range, multiple effects joined by ` / `.
- **Dur**: effect duration in seconds.
- **Cost**: spell magicka cost from the record.
- **In R3**: `Y` if this exact spell ID already exists in `R3 - Spells.json`.
- **Recalc**: `Yes` = a scalable effect's base cost changed in R3, so mag/dur/cost need recomputation. `Cost only` = only a no-scale effect (Fire/Frost/Shock/Poison) changed, so just cost/rounding. `-` = no base-cost change.

## Alteration (68)

| Spell                        |   Mag |     Dur | Cost | In R3 | Recalc | ID                               |
| ---------------------------- | ----: | ------: | ---: | ----- | ------ | -------------------------------- |
| Buoyancy                     |     1 |      20 |    2 | Y     | Yes    | `buoyancy`                       |
| Burden                       |    20 |      10 |   15 | Y     | Yes    | `burden`                         |
| Burden of Sin                | 40-60 |      20 |   50 | Y     | Yes    | `burden of sin`                  |
| Burden Touch                 |    20 |      10 |   10 | Y     | Yes    | `burden touch`                   |
| Cruel Weary                  | 50-70 |      10 |   45 | Y     | Yes    | `cruel weary`                    |
| Crushing Burden              |    60 |      10 |   45 | Y     | Yes    | `crushing burden`                |
| Crushing Burden of Sin       | 60-80 |      30 |  158 | Y     | Yes    | `crushing burden of sin`         |
| Crushing Burden Touch        |    60 |      10 |   30 | Y     | Yes    | `crushing burden touch`          |
| Dire Weary                   | 60-90 |      10 |   56 | Y     | Yes    | `dire weary`                     |
| Falling First Barrier        | 8 / 5 | 40 / 20 |   42 | Y     | Yes    | `T_Com_Alt_Falling1stBarrier`    |
| Feather                      |    20 |      10 |   10 | Y     | Yes    | `feather`                        |
| Fenrick's Doorjam            |    10 |       1 |    1 | -     | Yes    | `fenrick's doorjam`              |
| Fierce Fire Shield           |  5-11 |      10 |   12 | Y     | -      | `fierce fire shield`             |
| Fierce Frost Shield          |  5-11 |      10 |   12 | Y     | -      | `fierce frost shield`            |
| Fierce Shock Shield          |  5-11 |      10 |   12 | Y     | -      | `fierce shock shield`            |
| Fifth Barrier                |    50 |      30 |  150 | -     | Yes    | `fifth barrier`                  |
| Fire Barrier                 |  1-10 |      10 |    8 | Y     | -      | `fire barrier`                   |
| Fire Shield                  |    10 |      30 |   45 | Y     | -      | `fire shield`                    |
| First Barrier                |    10 |      30 |   30 | Y     | Yes    | `first barrier`                  |
| Fling                        |   500 |       3 |  100 | Y     | Yes    | `T_Com_Alt_Fling`                |
| Force Wall                   |    50 |       5 |   25 | Y     | Yes    | `T_Com_Alt_ForceWall`            |
| Fourth Barrier               |    40 |      30 |  120 | -     | Yes    | `fourth barrier`                 |
| Frost Barrier                |     3 |      10 |    5 | Y     | -      | `frost barrier`                  |
| Frost Shield                 |    10 |      30 |   45 | Y     | -      | `frost shield`                   |
| Frost Shield                 |     6 |      30 |   27 | Y     | -      | `frost_shield`                   |
| Fuchon Cire's Gentle Descent |    10 |      20 |   20 | -     | -      | `T_Com_Alt_FuchonGentleDescent`  |
| Great Burden of Sin          |    40 |      10 |   30 | Y     | Yes    | `great burden of sin`            |
| Great Feather                |   100 |      10 |   50 | Y     | Yes    | `great feather`                  |
| Great Levitate               |    30 |      10 |   45 | -     | -      | `great levitate`                 |
| Great Open                   |    50 |       1 |   15 | -     | Yes    | `great open`                     |
| Heavy Burden                 |    40 |      10 |   30 | Y     | Yes    | `heavy burden`                   |
| Heavy Burden Touch           |    40 |      10 |   20 | Y     | Yes    | `heavy burden touch`             |
| Jump                         |     5 |      10 |    8 | -     | -      | `jump`                           |
| Levitate                     |    10 |      30 |   45 | -     | -      | `levitate`                       |
| Lightning Shield             |    10 |      30 |   45 | Y     | -      | `lightning shield`               |
| Lock                         |     5 |       1 |    1 | -     | Yes    | `lock`                           |
| Ondusi's Open Door           |    50 |       1 |   15 | -     | Yes    | `ondusi's open door`             |
| Open                         |    20 |       1 |    6 | -     | Yes    | `open`                           |
| Savi's Swift-Stroke          |    40 |      15 |   50 | -     | Yes    | `TR_m7_AI_Savi_Swim`             |
| Second Barrier               |    20 |      30 |   60 | -     | Yes    | `second barrier`                 |
| Shield                       |     5 |      30 |   15 | Y     | Yes    | `shield`                         |
| Shock Barrier                |  1-10 |      10 |    8 | Y     | -      | `shock barrier`                  |
| Shock Shield                 |     3 |      20 |    9 | Y     | -      | `shock shield`                   |
| Sixth Barrier                |    60 |      30 |  180 | -     | Yes    | `sixth barrier`                  |
| Slowfall                     |    30 |      10 |   45 | -     | -      | `slowfall`                       |
| Slowfalling                  | 10-30 |       3 |    9 | -     | -      | `T_Com_Alt_Slowfalling`          |
| St. Cirrha's Song            |     1 |     100 |   15 | -     | -      | `T_Imp_Alt_VivecsKiss`           |
| Strong Feather               |    50 |      10 |   25 | Y     | Yes    | `strong feather`                 |
| Strong Fire Shield           |    12 |      30 |   54 | Y     | -      | `strong fire shield`             |
| Strong Frost Shield          |    12 |      30 |   54 | Y     | -      | `strong frost shield`            |
| Strong Levitate              |    20 |      10 |   30 | -     | -      | `strong levitate`                |
| Strong Open                  |    50 |       1 |   15 | -     | Yes    | `strong open`                    |
| Strong Shock Shield          |    12 |      30 |   54 | Y     | -      | `strong shock shield`            |
| Swimmer's Blessing           |     5 |      30 |   15 | Y     | Yes    | `Swimmer's_Blessing`             |
| Thelen Kaarn's Feather       |    50 |      10 |   25 | -     | Yes    | `T_Nor_Alt_UlmsJuicedawsFeather` |
| Third Barrier                |    30 |      30 |   90 | -     | Yes    | `third barrier`                  |
| Tinur's Hoptoad              |    20 |      10 |   30 | -     | -      | `tinur's hoptoad`                |
| Ulms's Juicedaw's Feather    |    50 |      10 |   25 | Y     | Yes    | `ulms juicedaw's feather`        |
| Vivec's Kiss                 |     1 |     100 |   15 | -     | -      | `vivec's kiss`                   |
| Waft of Lightness            | 10-30 |       3 |    5 | -     | -      | `T_Com_Alt_Lightness`            |
| Water Breathing              |     1 |      30 |    5 | -     | -      | `water breathing`                |
| Water Walking                |     1 |      60 |    9 | -     | -      | `water walking`                  |
| Weary                        | 30-60 |      10 |   34 | Y     | Yes    | `weary`                          |
| Weight of Guilt              |   500 |       3 |  100 | Y     | Yes    | `T_Com_Alt_WeightOfGuilt`        |
| Wild Levitate                |  1-50 |      30 |  115 | -     | -      | `wild levitate`                  |
| Wild Open                    | 1-100 |       1 |   15 | -     | Yes    | `wild open`                      |
| Wizard Lock                  |    20 |       1 |    2 | Y     | Yes    | `T_Com_Alt_WizardLock`           |
| Zenithar's Arms              |    50 |      10 |   25 | Y     | Yes    | `T_Imp_Alt_UlmsJuicedawsFeather` |

## Conjuration (65)

| Spell                          |       Mag |     Dur | Cost | In R3 | Recalc | ID                                |
| ------------------------------ | --------: | ------: | ---: | ----- | ------ | --------------------------------- |
| Assistance                     |        15 |      10 |  100 | -     | -      | `T_Com_Cnj_Assistance`            |
| Blood Spirit                   |         1 |     120 |   42 | -     | -      | `T_Com_Cnj_BloodSpirit`           |
| Bound Battle Axe               |         1 |      60 |    6 | -     | -      | `T_Com_Cnj_BoundWarAxe`           |
| Bound Battle-Axe               |         1 |      60 |    6 | -     | -      | `bound battle-axe`                |
| Bound Boots                    |         1 |      60 |    6 | -     | -      | `T_Com_Cnj_BoundGreaves`          |
| Bound Boots                    |         1 |      60 |    6 | -     | -      | `bound boots`                     |
| Bound Cuirass                  |         1 |      60 |    6 | -     | -      | `bound cuirass`                   |
| Bound Dagger                   |         1 |      60 |    6 | -     | -      | `bound dagger`                    |
| Bound Gauntlets                |         1 |      60 |    6 | -     | -      | `bound gauntlets`                 |
| Bound Gauntlets                |         1 |      60 |    6 | -     | -      | `T_Com_Cnj_BoundPauldron`         |
| Bound Helm                     |         1 |      60 |    6 | -     | -      | `bound helm`                      |
| Bound Longbow                  |         1 |      60 |    6 | -     | -      | `bound longbow`                   |
| Bound Longsword                |         1 |      60 |    6 | -     | -      | `bound longsword`                 |
| Bound Longsword                |         1 |      60 |    6 | -     | -      | `T_Com_Cnj_BoundGreatsword`       |
| Bound Mace                     |         1 |      60 |    6 | -     | -      | `bound mace`                      |
| Bound Mace                     |         1 |      60 |    6 | -     | -      | `T_Com_Cnj_BoundWarhammer`        |
| Bound Shield                   |         1 |      60 |    6 | -     | -      | `bound shield`                    |
| Bound Spear                    |         1 |      60 |    6 | -     | -      | `bound spear`                     |
| Call of the Beasts             |        10 |      10 |   65 | -     | -      | `T_Com_Cnj_CallOfTheBeasts`       |
| Command Creature               |         5 |      30 |  169 | -     | -      | `command creature`                |
| Command Humanoid               |         5 |      30 |  169 | -     | -      | `command humanoid`                |
| Commanding Touch               |         5 |      10 |   38 | -     | -      | `commanding touch`                |
| Daedric Weapon                 |         1 |     120 |   12 | -     | -      | `T_Com_Cnj_DaedricWeapon`         |
| Death Howl                     | 10 / 2-10 | 20 / 10 |   39 | -     | -      | `T_Com_Cnj_DeathHowl`             |
| Greater Summon Ancestral Ghost |         1 |     430 |  147 | -     | -      | `T_Cyr_Cnj_SummonWraith`          |
| Greater Summon Bonelord        |         1 |     130 |  160 | -     | -      | `T_De_Cnj_SummonGreaterBonelord`  |
| Greater Summon Clannfear       |         1 |      90 |   99 | -     | -      | `T_Com_Cnj_SummonOgrim`           |
| Greater Summon Daedroth        |         1 |      80 |  126 | -     | -      | `T_Com_Cnj_SummonSpiderDaedra`    |
| Greater Summon Scamp           |         1 |     145 |   88 | -     | -      | `T_Com_Cnj_SummonVermai`          |
| Greater Summon Scamp           |         1 |      90 |   54 | -     | -      | `T_Com_Cnj_SummonHerne`           |
| Greater Summon Skeleton        |         1 |     150 |   96 | -     | -      | `T_Com_Cnj_SummonSkeletonChamp`   |
| Greater Summon Storm Atronach  |         1 |      95 |  180 | -     | -      | `T_Com_Cnj_SummonStormMonarch`    |
| Holy Touch                     |        10 |      60 |    6 | -     | -      | `holy touch`                      |
| Holy Word                      |         5 |      60 |    5 | -     | -      | `holy word`                       |
| Lesser Bound Dagger            |         1 |      30 |    3 | -     | -      | `T_Com_Cnj_BoundThrowingKnives`   |
| Lesser Summon Bonewalker       |         1 |      30 |   20 | -     | -      | `T_Com_Cnj_SummonHellHound`       |
| Lesser Summon Clannfear        |         1 |      50 |   57 | -     | -      | `T_Com_Cnj_SummonLesserClannfear` |
| Lesser Summon Daedroth         |         1 |      40 |   63 | -     | -      | `T_Com_Cnj_SummonMorphoid`        |
| Lesser Summon Skeleton         |         1 |      50 |   33 | -     | -      | `T_Cyr_Cnj_SummonBarrowguard`     |
| Saintly Touch                  |        25 |      60 |   15 | -     | -      | `saintly touch`                   |
| Saintly Word                   |        25 |      60 |   23 | -     | -      | `saintly word`                    |
| Scatter the Dead               |        70 |      20 |   21 | -     | -      | `TR_m7_RirayneaTurn`              |
| Summon Ancestral Ghost         |         1 |      60 |   21 | -     | -      | `summon ancestral ghost`          |
| Summon Ancestral Ghost         |         1 |      60 |   21 | -     | -      | `T_Cyr_Cnj_SummonGhost`           |
| Summon Bonelord                |         1 |      60 |   75 | -     | -      | `summon bonelord`                 |
| Summon Clannfear               |         1 |      60 |   66 | -     | -      | `summon clanfear`                 |
| Summon Daedroth                |         1 |      60 |   96 | -     | -      | `summon daedroth`                 |
| Summon Dremora                 |         1 |      60 |   84 | -     | -      | `summon dremora`                  |
| Summon Dremora                 |         1 |      65 |   93 | -     | -      | `T_Com_Cnj_SummonDremoraCaster`   |
| Summon Dremora                 |         1 |      70 |   98 | -     | -      | `T_Com_Cnj_SummonDremoraArcher`   |
| Summon Flame Atronach          |         1 |      60 |   69 | -     | -      | `summon flame atronach`           |
| Summon Frost Atronach          |         1 |      60 |   81 | -     | -      | `summon frost atronach`           |
| Summon Golden Saint            |         1 |      65 |  177 | -     | -      | `T_Com_Cnj_SummonNocturnal`       |
| Summon Golden Saint            |         1 |      75 |  207 | -     | -      | `T_Com_Cnj_SummonGuardian`        |
| Summon Golden Saint            |         1 |      60 |  165 | -     | -      | `summon golden saint`             |
| Summon Greater Bonewalker      |         1 |      60 |   45 | -     | -      | `summon greater bonewalker`       |
| Summon Hunger                  |         1 |      60 |   87 | -     | -      | `summon hunger`                   |
| Summon Least Bonewalker        |         1 |      60 |   39 | -     | -      | `summon least bonewalker`         |
| Summon Scamp                   |         1 |      60 |   36 | -     | -      | `summon scamp`                    |
| Summon Skeletal Minion         |         1 |      60 |   39 | -     | -      | `summon skeletal minion`          |
| Summon Storm Atronach          |         1 |      60 |  114 | -     | -      | `summon storm atronach`           |
| Summon Winged Twilight         |         1 |      60 |  156 | -     | -      | `summon winged twilight`          |
| Summon Winged Twilight         |         1 |      85 |  225 | -     | -      | `T_Com_Cnj_SummonSeducerDark`     |
| Summon Winged Twilight         |         1 |      60 |  156 | -     | -      | `T_Com_Cnj_SummonSeducer`         |
| Turn Undead                    |        50 |      10 |    5 | -     | -      | `turn undead`                     |

## Destruction (167)

| Spell                       |                           Mag |         Dur | Cost | In R3 | Recalc    | ID                            |
| --------------------------- | ----------------------------: | ----------: | ---: | ----- | --------- | ----------------------------- |
| Absorb Agility              |                          5-20 |          30 |   38 | -     | -         | `absorb agility`              |
| Absorb Agility [Ranged]     |                          5-20 |          30 |   56 | -     | -         | `absorb agility [ranged]`     |
| Absorb Endurance            |                          5-20 |          30 |   38 | -     | -         | `absorb endurance`            |
| Absorb Endurance [Ranged]   |                          5-20 |          30 |   56 | -     | -         | `absorb endurance [ranged]`   |
| Absorb Fatigue              |                          5-20 |          30 |   75 | Y     | Yes       | `absorb fatigue`              |
| Absorb Fatigue [Ranged]     |                          5-20 |          30 |  113 | Y     | Yes       | `absorb fatigue [ranged]`     |
| Absorb Health               |                          5-52 |           1 |   11 | Y     | Yes       | `absorb health`               |
| Absorb Health [Ranged]      |                          5-20 |           1 |    8 | -     | Yes       | `absorb health [ranged]`      |
| Absorb Intelligence         |                          5-20 |          30 |   38 | -     | -         | `absorb intelligence`         |
| Absorb Luck                 |                          5-20 |          30 |   38 | -     | -         | `absorb luck`                 |
| Absorb Luck [Ranged]        |                          5-20 |          30 |   56 | -     | -         | `absorb luck [ranged]`        |
| Absorb Personality          |                          5-20 |          30 |   38 | -     | -         | `absorb personality`          |
| Absorb Personality [Ranged] |                          5-20 |          30 |   56 | -     | -         | `absorb personality [ranged]` |
| Absorb Speed                |                          5-20 |          30 |   38 | -     | -         | `absorb speed`                |
| Absorb Speed [Ranged]       |                          5-20 |          30 |   56 | -     | -         | `absorb speed [ranged]`       |
| Absorb Strength             |                          5-20 |          30 |   38 | -     | -         | `absorb strength`             |
| Absorb Strength [Ranged]    |                          5-20 |          30 |   56 | -     | -         | `absorb strength [ranged]`    |
| Absorb Willpower            |                          5-20 |          30 |   38 | -     | -         | `absorb willpower`            |
| Absorb Willpower [Ranged]   |                          5-20 |          30 |   56 | -     | -         | `absorb willpower [ranged]`   |
| Amatarya's Repurposing      |                 15-20 / 20-30 |           5 |   66 | -     | Yes       | `TR_m7_AmataryaAbsorb`        |
| Armor Eater                 |                         10-30 |           1 |    6 | Y     | Yes       | `armor eater`                 |
| Ash Feast                   |                             3 |          30 |   18 | Y     | -         | `ash feast`                   |
| Black Hand                  |                   5-12 / 5-12 |           1 |    7 | Y     | Cost only | `black hand`                  |
| Blood Curse: Fatigue        |                         10-20 |           5 |   23 | -     | Yes       | `blood curse: fatigue`        |
| Blood Despair               |                          7-14 |          60 |   47 | Y     | -         | `blood despair`               |
| Cause Disease               | 10-30 / 2-6 / 2-6 / 2-6 / 2-6 |      20 / 1 |   70 | -     | Yes       | `T_Com_Des_CauseDisease`      |
| Clench                      |                          1-20 |           1 |    4 | -     | Yes       | `clench`                      |
| Conduction                  |        47-102 / 23-48 / 12-25 |           0 |   48 | -     | Cost only | `TR_m7_IndrasiShock`          |
| Crimson Despair             |                          5-20 |          60 |  113 | -     | -         | `crimson despair`             |
| Cruel Firebloom             |                         10-16 |           1 |    7 | Y     | Cost only | `cruel firebloom`             |
| Daedric Bite                |                            50 |           1 |   30 | -     | -         | `daedric bite`                |
| Deadly Poison               |                          1-20 |          10 |   47 | -     | Cost only | `deadly poison`               |
| Deadly Poison [Ranged]      |                          1-20 |          10 |   71 | -     | Cost only | `deadly poison [ranged]`      |
| Din of Revelations          |                       20 / 20 |     30 / 10 |  145 | -     | -         | `T_Com_Des_Revelations`       |
| Dire Shockball              |                         40-50 |           0 |   24 | -     | Cost only | `dire shockball`              |
| Dire Weakness to Fire       |                          2-60 |          10 |   47 | Y     | -         | `dire weakness to fire`       |
| Dire Weakness to Frost      |                          2-60 |          10 |   47 | Y     | -         | `dire weakness to frost`      |
| Dire Weakness to Magicka    |                          2-60 |          10 |   47 | Y     | -         | `dire weakness to magicka`    |
| Dire Weakness to Poison     |                          2-60 |          10 |   47 | Y     | -         | `dire weakness to poison`     |
| Dire Weakness to Shock      |                          2-60 |          10 |   47 | Y     | -         | `dire weakness to shock`      |
| Disintegrate Armor          |                          6-25 |           1 |    7 | Y     | Yes       | `disintegrate armor`          |
| Disintegrate Weapon         |                          6-25 |           1 |    7 | Y     | Yes       | `disintegrate weapon`         |
| Distracting Touch           |                          5-20 |          60 |   38 | -     | -         | `distracting touch`           |
| Distraction                 |                          5-20 |          30 |   28 | -     | -         | `distraction`                 |
| Doze                        |                          1-20 |           1 |    2 | Y     | Yes       | `doze`                        |
| Drain Alchemy               |                          5-20 |          60 |   56 | -     | -         | `drain alchemy`               |
| Drain Alteration            |                          5-20 |          60 |   56 | -     | -         | `drain alteration`            |
| Drain Blood                 |                         5 / 5 |          30 |   60 | -     | Yes       | `drain blood`                 |
| Drain Conjuration           |                          5-20 |          60 |   56 | -     | -         | `drain conjuration`           |
| Drain Destruction           |                          5-20 |          60 |   56 | -     | -         | `drain destruction`           |
| Drain Enchant               |                          5-20 |          60 |   56 | -     | -         | `drain enchant`               |
| Drain Illusion              |                          5-20 |          60 |   56 | -     | -         | `drain illusion`              |
| Drain Long Blade            |                          5-20 |          60 |   56 | -     | -         | `drain long blade`            |
| Drain Mysticism             |                          5-20 |          60 |   56 | -     | -         | `drain mysticism`             |
| Drain Restoration           |                          5-20 |          60 |   56 | -     | -         | `drain restoration`           |
| Drain Spear                 |                          5-20 |          60 |   56 | -     | -         | `drain spear`                 |
| Dread Curse: Strength       |                          5-12 |           1 |    3 | -     | Yes       | `dread curse: strength`       |
| Emasculate                  |                          1-20 |           1 |    4 | -     | Yes       | `emasculate`                  |
| Energy Leech                |                          5-20 |          30 |   75 | Y     | Yes       | `energy leech`                |
| Enervate                    |                          5-20 |          30 |   28 | -     | -         | `enervate`                    |
| Evil Eye                    |                          1-10 |           1 |    2 | -     | Yes       | `evil eye`                    |
| Exhausting Touch            |                          5-20 |          60 |   75 | Y     | Yes       | `exhausting touch`            |
| Felms' Punishment           |                          1-20 |           1 |    9 | -     | Yes       | `T_De_Des_SphereWeakness`     |
| Fire Bite                   |                         15-30 |           1 |    6 | -     | Cost only | `fire bite`                   |
| Fire Storm                  |                          1-10 |          10 |   23 | -     | Cost only | `fire storm`                  |
| Fireball                    |                          2-20 |           1 |    5 | -     | Cost only | `fireball`                    |
| Firebloom                   |                          1-25 |           5 |   26 | -     | Cost only | `firebloom`                   |
| Firefist                    |                 10-24 / 10-24 |           1 |   11 | -     | Cost only | `firefist`                    |
| Five Fingers of Pain        |   3-5 / 3-5 / 3-5 / 3-5 / 3-5 |           1 |    5 | -     | Cost only | `five fingers of pain`        |
| Flame                       |                          1-15 |           1 |    2 | -     | Cost only | `flame`                       |
| Flameblast                  |                  54-134 / 4-8 |       0 / 8 |   56 | -     | Cost only | `TR_m7_IndrasiFire`           |
| Flamebolt                   |                         10-50 |           2 |   24 | -     | Cost only | `flamebolt`                   |
| Fleabite                    |                          1-10 |           1 |    1 | Y     | Yes       | `fleabite`                    |
| Freezing Gale               |                         18-46 |           4 |   46 | -     | Cost only | `TR_m7_IndrasiFrost`          |
| Freezing Touch              |                         15-30 |           1 |    6 | -     | Cost only | `freezing touch`              |
| Frost Bolt                  |                         10-50 |           2 |   24 | -     | Cost only | `frost bolt`                  |
| Frost Storm                 |                          1-10 |          10 |   23 | -     | Cost only | `frost storm`                 |
| Frostball                   |                          2-20 |           1 |    5 | -     | Cost only | `frostball`                   |
| Frostbite                   |                         15-30 |           1 |    6 | -     | Cost only | `frostbite`                   |
| Frostbloom                  |                          1-25 |           5 |   26 | -     | Cost only | `frostbloom`                  |
| Frostfist                   |                 10-24 / 10-24 |           1 |   11 | -     | Cost only | `frostfist`                   |
| Fuddle                      |                          1-20 |           1 |    4 | -     | Yes       | `fuddle`                      |
| Gash Spirit                 |                          5-20 |          30 |   75 | -     | Yes       | `gash spirit`                 |
| Gash Spirit [Ranged]        |                          5-20 |          30 |  113 | -     | Yes       | `gash spirit [ranged]`        |
| Ghost Curse                 |                 5 / 10 / 1-10 |      30 / 1 |   40 | -     | Yes       | `Ghost Curse`                 |
| God's Fire                  |                         11-60 |          10 |  135 | Y     | Cost only | `god's fire`                  |
| God's Frost                 |                         11-60 |          10 |  135 | Y     | Cost only | `god's frost`                 |
| God's Spark                 |                          5-50 |          10 |  147 | -     | Cost only | `god's spark`                 |
| Grave Curse: Health         |                           1-4 |          10 |   15 | -     | -         | `grave curse: health`         |
| Grave Curse: Magicka        |                           2-4 |          10 |   18 | -     | Yes       | `grave curse: spell points`   |
| Grave Curse: Strength       |                           2-4 |          60 |   14 | -     | -         | `grave curse: strength`       |
| Greater Fireball            |                          2-40 |           1 |   10 | -     | Cost only | `Fireball_large`              |
| Greater Frostball           |                          2-40 |           1 |   10 | -     | Cost only | `Frostball_large`             |
| Greater Shockball           |                          2-40 |           1 |   14 | Y     | Cost only | `shockball_large`             |
| Gripes                      |                          1-20 |           1 |    4 | -     | Yes       | `gripes`                      |
| Heartbite                   |                         10-50 |           1 |   12 | -     | -         | `heartbite`                   |
| Hex                         |                          1-20 |           1 |    4 | -     | Yes       | `hex`                         |
| Ice Bolt                    |                          1-35 |           5 |   34 | -     | Cost only | `T_Com_Des_IceBolt`           |
| Ice Storm                   |                          1-30 |           5 |   33 | -     | Cost only | `T_Com_Des_IceStorm`          |
| Ignite Foe                  |                           1-5 |          60 |   68 | -     | Cost only | `T_Com_Des_IgniteFoe`         |
| Iron Eater                  |                          1-25 |           2 |   12 | Y     | Yes       | `T_Rea_Des_IronEater`         |
| Ironhand                    |                         21-42 |           1 |    6 | -     | Yes       | `ironhand`                    |
| Judgement Ordained          |               2 / 2 / 15 / 15 |     15 / 10 |   45 | -     | Cost only | `T_De_Des_IndGuardJudgement`  |
| Knuckle Luck                |                         3-120 |           1 |   12 | -     | Yes       | `knuckle luck`                |
| Lifesteal                   |                            40 |           1 |   24 | Y     | Yes       | `T_Com_Mys_Lifesteal`         |
| Lightning                   |                          1-25 |           5 |   34 | -     | Cost only | `T_Com_Des_Lightning`         |
| Lightning Bolt              |                         10-50 |           2 |   34 | -     | Cost only | `lightning bolt`              |
| Lightning Storm             |                          2-10 |          10 |   34 | Y     | Cost only | `lightning storm`             |
| Maid of Rime                |                         30-75 |           2 |   13 | -     | Cost only | `T_Com_Des_MaidRime`          |
| Meat Rot                    |                    1-20 / 1-5 |           2 |   11 | -     | Yes       | `T_Rea_Des_MeatRot`           |
| Mother's Ire                |               2 / 2 / 20 / 15 | 15 / 1 / 10 |   45 | -     | Yes       | `T_De_Des_IndGuardMothersIre` |
| Mountain Wind               |                      5-10 / 1 |           5 |   38 | -     | Yes       | `T_Nor_Des_MountainWind`      |
| Ordeal of St. Olms          |                          5-20 |          60 |   75 | Y     | Yes       | `ordeal of st. olms`          |
| Poison                      |                          2-20 |           1 |    9 | Y     | Cost only | `poison`                      |
| Poison Sting                |                         6 / 1 |       4 / 2 |   15 | -     | Yes       | `T_Cr_Des_SkyrenderPoison`    |
| Poisonbloom                 |                          1-20 |           5 |   39 | -     | Cost only | `poisonbloom`                 |
| Poisonous Touch             |                         15-40 |           1 |   12 | -     | Cost only | `poisonous touch`             |
| Potent Poison               |                         20-40 |           5 |   68 | -     | Cost only | `potent poison`               |
| Potent Poison [Ranged]      |                         20-40 |           5 |  101 | -     | Cost only | `potent poison [ranged]`      |
| Renesa's Hindering Flames   |             21-39 / 5-9 / 150 |      3 / 10 |   73 | -     | Yes       | `TR_m3_RenesaFire`            |
| Righteousness               |                            10 |           1 |    4 | -     | Yes       | `righteousness`               |
| Scourge Blade               |                   5-20 / 5-20 |          30 |   56 | -     | -         | `scourge blade`               |
| Shadow Rust                 |                    1-5 / 1-15 |          20 |   30 | Y     | Yes       | `T_Rea_Des_ShadowRust`        |
| Shock                       |                          1-15 |           1 |    3 | -     | Cost only | `shock`                       |
| Shockball                   |                          2-40 |           1 |   14 | Y     | Cost only | `shockball`                   |
| Shockbite                   |                         35-45 |           2 |   28 | -     | Cost only | `shockbite`                   |
| Shockbloom                  |                          1-25 |           5 |   37 | -     | Cost only | `shockbloom`                  |
| Shocking Touch              |                          3-30 |           1 |    6 | -     | Cost only | `shocking touch`              |
| Sigillah's Mind Blast       |           68-124 / 10-27 / 40 |       0 / 3 |   70 | -     | Yes       | `TR_m7_SigillahShock`         |
| Sleep                       |                          5-15 |          30 |   45 | Y     | Yes       | `sleep`                       |
| Soulpinch                   |                          1-20 |           1 |    4 | Y     | Yes       | `soulpinch`                   |
| Spark                       |                          2-20 |           1 |    7 | Y     | Cost only | `spark`                       |
| Sphere of Negation          |                         15-26 |           1 |    8 | -     | -         | `sphere of negation`          |
| Sphere of Weakness          |                          1-20 |           1 |    9 | -     | Yes       | `T_Com_Des_SphereWeakness`    |
| Stormhand                   |                   5-12 / 5-12 |           1 |    6 | Y     | Cost only | `stormhand`                   |
| Strength Leech              |                            20 |          30 |   30 | -     | -         | `strength leech`              |
| Stumble                     |                          1-20 |           1 |    4 | -     | Yes       | `stumble`                     |
| Tag                         |                         40-50 |           8 |   65 | -     | Yes       | `T_Com_Mys_Tag`               |
| Temptation                  |                          5-20 |          30 |   28 | -     | -         | `temptation`                  |
| Thimble of Magefire         |                         10-30 |           1 |    6 | Y     | Yes       | `T_Com_Des_Magefire`          |
| Thunderclap                 |                    35-45 / 60 |       2 / 5 |   63 | -     | Yes       | `TR_m3_ReveaTelamSpell`       |
| Torpor                      |                          5-20 |          30 |   28 | -     | -         | `torpor`                      |
| Toxic Cloud                 |                          2-15 |          10 |   61 | Y     | Cost only | `poison_powerful`             |
| Viper                       |                           2-8 |           1 |    2 | -     | Cost only | `viper`                       |
| Viperbite                   |                          1-30 |           1 |    7 | -     | Cost only | `viperbite`                   |
| Viperbolt                   |                         10-50 |           2 |   44 | -     | Cost only | `viperbolt`                   |
| Vivec's Wrath               | 10-20 / 10-20 / 10-20 / 10-20 |           1 |   28 | -     | Cost only | `vivec's_wrath`               |
| Weakness                    |                          5-20 |          30 |   28 | -     | -         | `weakness`                    |
| Weakness to Common Disease  |                          1-20 |          10 |   16 | -     | -         | `weakness to common disease`  |
| Weakness to Fire            |                            10 |           5 |    8 | -     | -         | `weakness to fire`            |
| Weakness to Frost           |                            10 |           5 |    8 | -     | -         | `weakness to frost`           |
| Weakness to Magicka         |                            10 |           5 |    8 | -     | -         | `weakness to magicka`         |
| Weakness to Poison          |                            10 |           5 |    8 | -     | -         | `weakness to poison`          |
| Weakness to Shock           |                            10 |           5 |    8 | -     | -         | `weakness to shock`           |
| Weapon Eater                |                          6-25 |           1 |    5 | Y     | Yes       | `weapon eater`                |
| Wearying Touch              |                          5-20 |          30 |   38 | Y     | Yes       | `wearying touch`              |
| Wild Clumsiness             |                          5-20 |          60 |   56 | -     | -         | `wild clumsiness`             |
| Wild Distraction            |                          5-20 |          60 |   56 | -     | -         | `wild distraction`            |
| Wild Exhaustion             |                          5-15 |          60 |   90 | Y     | Yes       | `wild exhaustion`             |
| Wild Shockbloom             |                          2-40 |           1 |   14 | -     | Cost only | `wild shockbloom`             |
| Wild Strain                 |                          1-20 |           3 |    2 | -     | -         | `wild strain`                 |
| Wild Torpor                 |                          5-20 |          30 |   28 | -     | -         | `wild torpor`                 |
| Wildfire                    |                          1-15 |           5 |   15 | -     | Cost only | `T_Com_Des_Wildfire`          |
| Winds of Storm              |                         30-75 |           2 |   28 | -     | Cost only | `T_Com_Des_WindsStorm`        |
| Wizard Rend                 |                     10-35 / 1 |           4 |   39 | -     | Yes       | `wizard rend`                 |
| Woe                         |                          1-20 |           1 |    4 | -     | Yes       | `woe`                         |
| Wounding Touch              |                          1-10 |           3 |    3 | -     | -         | `wounding touch`              |

## Illusion (64)

| Spell                     |                                     Mag |    Dur | Cost | In R3 | Recalc | ID                           |
| ------------------------- | --------------------------------------: | -----: | ---: | ----- | ------ | ---------------------------- |
| Alad's Caliginy           |                                   10-30 |     30 |   30 | -     | -      | `alad's caliginy`            |
| Alluring Speech           |                                   15-20 |     20 |   80 | Y     | Yes    | `T_Com_Ilu_AlluringSpeech`   |
| Arvs' Confounding         |                      30-40 / 30-40 / 10 | 10 / 0 |   60 | -     | Yes    | `TR_m3_ArvsWeaken`           |
| Azura's Light             |                                      20 |    120 |   10 | -     | -      | `T_Com_Ilu_AzurasLight`      |
| Blind                     |                                      20 |     10 |   10 | -     | -      | `blind`                      |
| Blindfold                 |                                     100 |     15 |   60 | -     | -      | `T_Com_Ilu_Blindfold`        |
| Brevusa's Averted Eyes    |                                       1 |     10 |   10 | -     | -      | `brevusa's averted eyes`     |
| Calm Creature             |                                      30 |     10 |   23 | -     | -      | `calm creature`              |
| Calm Humanoid             |                                      30 |     10 |   23 | -     | -      | `calm humanoid`              |
| Calming Touch             |                                      30 |     10 |   15 | -     | -      | `calming touch`              |
| Chameleon                 |                                      10 |     30 |   15 | -     | -      | `chameleon`                  |
| Chameleon                 |                                   12-17 |     30 |   22 | -     | -      | `T_Com_Ilu_DistractHumanoid` |
| Charming Touch            |                                      30 |     30 |  225 | -     | Yes    | `charming touch`             |
| Concealment               |                                       1 |     90 |   90 | -     | -      | `concealment`                |
| Confusion                 | 1-10 / 1-10 / 1-10 / 1-10 / 1-10 / 1-10 |     20 |   24 | -     | -      | `T_Com_Ilu_Confusion`        |
| Crying Eye                |                                    1-10 |      5 |    2 | Y     | -      | `crying eye`                 |
| Dazzling Flourish         |                       1 / 35-65 / 35-50 | 5 / 10 |   62 | -     | Yes    | `TR_m3_RenasoGalsLight`      |
| Demoralize Beast          |                                       5 |     10 |    4 | -     | -      | `demoralize beast`           |
| Demoralize Creature       |                                       5 |     10 |    4 | -     | -      | `demoralize creature`        |
| Demoralize Humanoid       |                                       5 |     10 |    4 | -     | -      | `demoralize humanoid`        |
| Demoralizing Touch        |                                       5 |     10 |    3 | -     | -      | `demoralizing touch`         |
| Dire Noise                |                                    2-60 |      5 |   35 | Y     | Yes    | `dire noise`                 |
| Dravayn's Obscured Visage |                                     100 |     20 |   80 | -     | -      | `TR_m3_DravaynChameleon`     |
| Earwig                    |                                     3-8 |      5 |    6 | Y     | Yes    | `earwig`                     |
| Erelvam's Wild Sty        |                                    1-40 |     10 |   10 | Y     | -      | `erelvam's wild sty`         |
| Etherealness              |                                     100 |     10 |   50 | -     | -      | `T_Com_Ilu_Etherealness`     |
| Far Silence               |                                       1 |     10 |   30 | Y     | -      | `far silence`                |
| Father's Hand             |                                    1-40 |      5 |    5 | Y     | -      | `father's hand`              |
| Fear                      |                                      12 |     30 |   18 | -     | -      | `T_Com_Ilu_Fear`             |
| Frenzy Creature           |                                       5 |     10 |    4 | -     | -      | `frenzy creature`            |
| Frenzy Humanoid           |                                       5 |     10 |    4 | -     | -      | `frenzy humanoid`            |
| Frenzying Touch           |                                       5 |     10 |    3 | -     | -      | `frenzying touch`            |
| Golanar's Eye-Maze        |                                   10-40 |     10 |   13 | -     | -      | `golanar's eye-maze`         |
| Halt                      |                                       1 |     15 |   60 | -     | Yes    | `TR_m3_DravaynParalyze`      |
| Hide                      |                                       1 |     30 |   30 | -     | -      | `hide`                       |
| Hunter's Eye              |                                 15 / 15 |     60 |   20 | -     | -      | `T_Com_Ilu_DaedraHuntersEye` |
| Invisibility              |                                       1 |     30 |   30 | Y     | -      | `invisibility`               |
| Lesser Chameleon          |                                       7 |     30 |   11 | -     | -      | `T_Com_Ilu_DistractCreature` |
| Lesser Invisibility       |                                       1 |     15 |   15 | -     | -      | `T_Com_Ilu_Ethereal`         |
| Light                     |                                      20 |     30 |    9 | -     | -      | `light`                      |
| Living Statue             |                                       1 |     20 |   30 | Y     | Yes    | `T_Com_Ilu_LivingStatue`     |
| Medusa's Gaze             |                                       1 |     15 |   45 | -     | Yes    | `medusa's gaze`              |
| Monstrous Vision          |                                      30 |     15 |   20 | -     | -      | `T_Com_Ilu_MonstrousVision`  |
| Night-Eye                 |                                      20 |     30 |    6 | -     | -      | `night-eye`                  |
| Noise                     |                                     3-8 |      5 |    4 | Y     | Yes    | `noise`                      |
| On the Move               |                                   40-60 |     10 |   20 | -     | -      | `T_Com_Ilu_OnTheMove`        |
| Orc's Eye                 |                                      30 |     30 |    8 | -     | -      | `T_Com_Ilu_OrcsEye`          |
| Paralysis                 |                                       1 |      5 |   10 | Y     | Yes    | `paralysis`                  |
| Paralysis                 |                                       1 |      3 |    6 | Y     | Yes    | `T_Com_Ilu_Paralysis`        |
| Rally Beast               |                                       5 |     30 |    2 | -     | -      | `rally beast`                |
| Rally Creature            |                                       5 |     30 |    2 | -     | -      | `rally creature`             |
| Rally Humanoid            |                                       5 |     30 |    2 | -     | -      | `rally humanoid`             |
| Rallying Touch            |                                       5 |     30 |    2 | -     | -      | `rallying touch`             |
| Sanctuary                 |                                      10 |     30 |   15 | -     | -      | `sanctuary`                  |
| Serene Nature             |                                      10 |     30 |   10 | -     | -      | `T_Com_Ilu_SereneNature`     |
| Shadow Form               |                                    6-15 |     30 |   16 | Y     | -      | `shadow form`                |
| Shadow Weave              |                                 20 / 20 |     10 |   20 | -     | -      | `shadow weave`               |
| Shadowmask                |                                   40-70 |     30 |   83 | -     | -      | `shadowmask`                 |
| Silence                   |                                       1 |      5 |   15 | Y     | -      | `silence`                    |
| Skein of Convulsion       |                                 50 / 50 |     30 |   75 | -     | -      | `T_Com_Ilu_Skein`            |
| Soothe the Savage Beast   |                                      30 |     10 |   15 | -     | -      | `soothe the savage beast`    |
| Sotha's Grace             |                                    1-20 |      5 |    3 | Y     | -      | `sotha's grace`              |
| Steadfast                 |                                      30 |     30 |    8 | -     | -      | `T_Com_Ilu_Steadfast`        |
| Wild Earwig               |                                    1-30 |      5 |   17 | Y     | Yes    | `wild earwig`                |

## Mysticism (44)

| Spell                      |     Mag | Dur | Cost | In R3 | Recalc | ID                             |
| -------------------------- | ------: | --: | ---: | ----- | ------ | ------------------------------ |
| Alduin's Maw               |      10 |   5 |   25 | -     | Yes    | `T_Nor_Mys_VivecsFeast`        |
| Almalexia's Grace          |      20 |   1 |    5 | -     | -      | `almalexia's grace`            |
| Almsivi Intervention       |       1 |   1 |    8 | -     | -      | `almsivi intervention`         |
| Detect Creature            |  50-150 |   5 |   19 | Y     | Yes    | `detect_creature`              |
| Detect Enchantment         |      10 |  10 |    5 | Y     | Yes    | `detect enchantment`           |
| Detect Key                 |      50 |   5 |   13 | Y     | Yes    | `detect_key`                   |
| Dispel                     |     100 |   1 |   25 | -     | -      | `dispel`                       |
| Dispel Magic               |   20-60 |   1 |   13 | -     | -      | `T_Com_Mys_DispelMagic`        |
| Dispel Other               |   30-40 |   1 |   13 | -     | -      | `TR_m1_q_MG4Dispel`            |
| Divine Intervention        |       1 |   1 |    8 | -     | -      | `divine intervention`          |
| Greater Detect Creature    | 100-300 |   5 |   38 | Y     | Yes    | `T_Com_Mys_DetectHumanoid`     |
| Greater Detect Enchantment |     150 |  10 |   75 | Y     | Yes    | `T_Com_Mys_Insight`            |
| Greater Detect Enchantment |      57 |  20 |   57 | -     | Yes    | `T_Com_Mys_DetectEnemy`        |
| Greater Detect Enchantment |      60 |  20 |   60 | -     | Yes    | `T_Com_Mys_DetectValuables`    |
| Greater Detect Key         |     100 |  15 |   76 | -     | Yes    | `T_Com_Mys_DetectInvisibility` |
| Greater Dispel Magic       |     100 |   1 |   64 | -     | -      | `T_Com_Mys_BanishDaedra`       |
| Greater Telekinesis        |      50 |  10 |   25 | -     | -      | `T_Com_Mys_Blink`              |
| Greater Telekinesis        |      50 |   5 |   13 | -     | -      | `T_Com_Mys_BloodMagic`         |
| Jhunal's Intercession      |      10 |   5 |   25 | -     | Yes    | `T_Nor_Mys_SothasMirror`       |
| Jogvir's Extended Arm      |      20 |  20 |   20 | -     | -      | `T_Nor_Mys_ExtendedArm`        |
| Llivam's Reversal          |   20-30 |  10 |  125 | Y     | Yes    | `llivam's reversal`            |
| Mark                       |       1 |   1 |   18 | -     | -      | `mark`                         |
| Minor Reflect              |     1-5 |  50 |   76 | Y     | Yes    | `T_Com_Mys_ReflectDamage`      |
| Recall                     |       1 |   1 |   18 | -     | -      | `recall`                       |
| Reflect                    |   10-20 |   5 |   38 | Y     | Yes    | `reflect`                      |
| Remove Enchantment         |     100 |   1 |   25 | -     | -      | `T_Com_Mys_RemoveEnchantment`  |
| Shalidor's Mirror          |   10-30 |  10 |  100 | Y     | Yes    | `shalidor's mirror`            |
| Sotha's Mirror             |      10 |   5 |   25 | Y     | Yes    | `sotha's mirror`               |
| Soul Trap                  |       1 |  60 |    6 | -     | -      | `soul trap`                    |
| Spell Absorption           |      10 |   5 |   25 | Y     | Yes    | `spell absorption`             |
| Spell Absorption           |      10 |   5 |   25 | -     | Yes    | `T_Com_Mys_SpellAbsorption`    |
| Spell Reflection           |      10 |   5 |   25 | -     | Yes    | `T_Com_Mys_SpellReflection`    |
| St. Horuscia's Alms        |      10 |   5 |   25 | Y     | Yes    | `T_Imp_Mys_VivecsFeast`        |
| St. Naharine's Shield      |      10 |   5 |   25 | Y     | Yes    | `T_Imp_Res_SothasMirror`       |
| Strong Reflect             |   20-30 |   5 |   63 | Y     | Yes    | `strong reflect`               |
| Strong Spelldrinker        |   20-30 |   5 |   63 | Y     | Yes    | `strong spelldrinker`          |
| Telekinesis                |      25 |   5 |    6 | -     | -      | `telekinesis`                  |
| Tevral's Hawkshaw          |      10 |  10 |    5 | Y     | Yes    | `tevral's hawkshaw`            |
| Touch Dispel               |       5 |   1 |    1 | -     | -      | `touch dispel`                 |
| Tranasa's Spelltrap        |   20-30 |  10 |  125 | Y     | Yes    | `tranasa's spelltrap`          |
| Vivec's Feast              |      10 |   5 |   25 | Y     | Yes    | `vivec's feast`                |
| Weak Spelldrinker          |   10-20 |   5 |   38 | Y     | Yes    | `weak spelldrinker`            |
| Wild Reflect               |    1-40 |  10 |  103 | Y     | Yes    | `wild reflect`                 |
| Wild Spelldrinker          |    1-40 |   5 |   51 | Y     | Yes    | `wild spelldrinker`            |

## Restoration (126)

| Spell                          |                           Mag |    Dur | Cost | In R3 | Recalc | ID                               |
| ------------------------------ | ----------------------------: | -----: | ---: | ----- | ------ | -------------------------------- |
| Azra's Sustenance              |                           1-2 |     60 |   23 | -     | -      | `T_Com_Res_AzraSustenance`       |
| Balyna's Antidote              |                             1 |      1 |    5 | -     | -      | `balyna's antidote`              |
| Balyna's Efficacious Balm      |                          3-22 |      1 |    3 | Y     | -      | `balyna's efficacious balm`      |
| Balyna's Perfect Balm          |                          3-30 |      1 |    4 | Y     | -      | `balyna's perfect balm`          |
| Balyna's Soothing Balm         |                          3-12 |      1 |    2 | Y     | -      | `balyna's soothing balm`         |
| Blightguard                    |                            10 |      5 |   13 | -     | Yes    | `blightguard`                    |
| Blood Beat                     |                            30 |     20 |   20 | -     | -      | `T_Com_Res_BloodBeat`            |
| Blood Gift                     |                         10-40 |     30 |   38 | -     | -      | `blood gift`                     |
| Breath of Morihaus             |                          1-10 |     20 |    6 | -     | Yes    | `T_Imp_Res_RestStMerris`         |
| Charisma                       |                            10 |     60 |   30 | -     | -      | `charisma`                       |
| Cure Blight Disease            |                             1 |      1 |  100 | -     | -      | `Cure Blight_Self`               |
| Cure Common Disease            |                             1 |      1 |   15 | -     | -      | `cure common disease`            |
| Cure Common Disease on Other   |                             1 |      1 |   15 | -     | -      | `cure common disease other`      |
| Cure Common Disease Victim     |                             1 |      1 |   23 | -     | -      | `cure common disease victim`     |
| Cure Poison                    |                             1 |      1 |    5 | -     | -      | `cure poison`                    |
| Cure Poison on Touch           |                             1 |      1 |    5 | -     | -      | `cure poison touch`              |
| Daedric Health                 |                            25 |     60 |   75 | -     | -      | `daedric health`                 |
| Daedric Luck                   |                            20 |     90 |   90 | -     | -      | `daedric luck`                   |
| Daedric Speed                  |                            20 |     90 |   90 | -     | -      | `daedric speed`                  |
| Daedric Strength               |                            20 |     90 |   90 | -     | -      | `daedric strength`               |
| Daedric Willpower              |                            20 |     90 |   90 | -     | -      | `daedric willpower`              |
| Dibella's Eye                  |                            10 |      1 |    3 | -     | -      | `T_Imp_Res_VelothsGift`          |
| Dibella's Whisper              |                            20 |     10 |   20 | -     | Yes    | `T_Nor_Res_SerynsBlessing`       |
| Divine Aid                     |                       10 / 10 |     60 |   60 | -     | -      | `divine aid`                     |
| Enrichment                     |                          5-20 |     30 |    9 | -     | Yes    | `enrichment`                     |
| Feet of Notorgo                |                            10 |     90 |   45 | Y     | -      | `feet of notorgo`                |
| Flameguard                     |                         20-40 |     30 |   90 | Y     | Yes    | `flameguard`                     |
| Fortify Restoration Skill      |                            10 |     60 |   30 | -     | Yes    | `fortify restoration skill`      |
| Fortitude                      |                            10 |     60 |   30 | -     | -      | `fortitude`                      |
| Four Hands of Morwha           |                            20 |     10 |   20 | -     | Yes    | `T_Rga_Res_SerynsBlessing`       |
| Free Action                    |                             1 |      1 |    5 | -     | -      | `free action`                    |
| Freedom of Movement            |                           100 |     20 |   20 | -     | -      | `TR_m7_FreedomMovement`          |
| Frostguard                     |                         20-40 |     30 |   90 | Y     | Yes    | `frostguard`                     |
| Great Heal Companion           |                          4-45 |      1 |    6 | -     | -      | `great heal companion`           |
| Great Resist Common Disease    |                            30 |     10 |   30 | Y     | Yes    | `great resist common disease`    |
| Great Resist Fire              |                            30 |     10 |   30 | Y     | Yes    | `great resist fire`              |
| Great Resist Frost             |                            30 |     10 |   30 | Y     | Yes    | `great resist frost`             |
| Great Resist Magicka           |                            30 |     10 |   30 | Y     | Yes    | `great resist magicka`           |
| Great Resist Shock             |                            30 |     10 |   30 | Y     | Yes    | `great resist shock`             |
| Greater Heal                   |                         25-47 |     10 |   90 | -     | -      | `T_Com_Res_ArmorResartus`        |
| Greater Resist Poison          |                            30 |     10 |   30 | Y     | Yes    | `greater resist poison`          |
| Greater Stamina                |                         42-78 |     30 |   90 | Y     | Yes    | `T_Com_Res_WeaponResartus`       |
| Haste                          |                         10-30 |     20 |   30 | -     | -      | `T_Com_Res_Haste`                |
| Heal Companion                 |                          6-15 |      1 |    3 | Y     | -      | `heal companion`                 |
| Heal True                      |                         25-50 |      5 |   47 | -     | -      | `T_Com_Res_HealTrue`             |
| Heal Wound                     |                            12 |      1 |    3 | -     | -      | `T_Com_Res_HealWound`            |
| Hearth Heal                    |                         20-80 |      1 |   13 | -     | -      | `hearth heal`                    |
| Intercession                   |                           100 |     10 |  100 | -     | Yes    | `TR_m7_Intercession`             |
| Iron Will                      |                            10 |     60 |   30 | -     | -      | `iron will`                      |
| Jack of Trades                 |                            10 |     60 |   30 | -     | -      | `jack of trades`                 |
| Jucilian's Rejuvenator         |                     10-70 / 1 |      1 |   25 | -     | -      | `T_Com_Res_Rejuvenator`          |
| Magickguard                    |                         20-40 |     10 |   30 | Y     | Yes    | `magickguard`                    |
| Mara's Hand                    |                             1 |      1 |   15 | -     | -      | `T_Imp_Res_RilmsCure`            |
| Masterful Golden Wisdom        |                            15 |     60 |   45 | Y     | Yes    | `masterful golden wisdom`        |
| Masterful Green Wisdom         |                            15 |     60 |   45 | Y     | Yes    | `masterful green wisdom`         |
| Masterful Red Wisdom           |                            15 |     60 |   45 | Y     | Yes    | `masteful red wisdom`            |
| Masterful Red Wisdom           |                            15 |     60 |   45 | Y     | Yes    | `masterful red wisdom`           |
| Masterful Silver Wisdom        |                            15 |     60 |   45 | Y     | Yes    | `masterful silver wisdom`        |
| Masterful Sublime Wisdom       |                            15 |     60 |   45 | Y     | Yes    | `masterful sublime wisdom`       |
| Masterful Transcendant Wisdom  |                            15 |     60 |   45 | Y     | Yes    | `masterful transcendant wisdom`  |
| Masterful Unseen Wisdom        |                            15 |     60 |   45 | Y     | Yes    | `masterful unseen wisdom`        |
| Mother's Kiss                  |                         10-20 |      1 |    4 | -     | -      | `mother's kiss`                  |
| Nimbleness                     |                            10 |     60 |   30 | -     | -      | `nimbleness`                     |
| Orc Strength                   |                          5-20 |     60 |   38 | -     | -      | `orc's strength`                 |
| Panacea                        |                     1 / 1 / 1 |      1 |  120 | -     | -      | `panacea`                        |
| Pilgrimage of St. Rosunius     |                            20 |     10 |   20 | Y     | Yes    | `T_Imp_Res_SerynsBlessing`       |
| Poet's Whim                    |                          1-30 |     10 |   39 | Y     | Yes    | `poet's whim`                    |
| Poisonguard                    |                         20-40 |     30 |   90 | Y     | Yes    | `poisonguard`                    |
| Powerwell                      |                          5-20 |     60 |   38 | -     | -      | `powerwell`                      |
| Prestidigitation               | 10-20 / 10-20 / 10-20 / 10-20 |     15 |   45 | -     | Yes    | `TR_m7_Prestidigitation`         |
| Purify                         |               100 / 1 / 10-30 | 1 / 20 |   50 | -     | -      | `T_Com_Res_Purify`               |
| Quicksilver                    |                            10 |     60 |   30 | -     | -      | `Quicksilver`                    |
| Rapid Regenerate               |                          5-10 |     20 |   38 | -     | -      | `rapid regenerate`               |
| Regenerate                     |                           1-5 |     20 |   15 | -     | -      | `regenerate`                     |
| Resist Common Disease          |                            10 |      5 |    5 | Y     | Yes    | `resist common disease`          |
| Resist Fire                    |                            10 |      5 |    5 | Y     | Yes    | `resist fire`                    |
| Resist Frost                   |                            10 |      5 |    5 | Y     | Yes    | `resist frost`                   |
| Resist Magicka                 |                            10 |      5 |    5 | Y     | Yes    | `resist magicka`                 |
| Resist Paralysis               |                            50 |     30 |  300 | Y     | -      | `resist paralysis`               |
| Resist Poison                  |                            20 |      5 |   10 | Y     | Yes    | `resist poison`                  |
| Resist Shock                   |                            20 |      5 |   10 | Y     | Yes    | `resist shock`                   |
| Rest of St. Merris             |                          1-10 |     20 |    6 | Y     | Yes    | `rest of st. merris`             |
| Restore Agility                |                          5-20 |     30 |   19 | Y     | Yes    | `restore agility`                |
| Restore Constitution           |                 5 / 5 / 5 / 5 |      5 |    5 | -     | -      | `T_De_Res_RestoreConstitution`   |
| Restore Endurance              |                          5-20 |     30 |   19 | Y     | Yes    | `restore endurance`              |
| Restore Finesse                | 5 / 5 / 5 / 5 / 5 / 5 / 5 / 5 |      5 |   10 | -     | -      | `T_De_Res_RestoreFinesse`        |
| Restore Fortitude              | 5 / 5 / 5 / 5 / 5 / 5 / 5 / 5 |      5 |   10 | -     | -      | `T_De_Res_RestoreFortitude`      |
| Restore Intelligence           |                          5-20 |     30 |   19 | Y     | Yes    | `restore intelligence`           |
| Restore Luck                   |                          5-20 |     30 |   19 | Y     | Yes    | `restore luck`                   |
| Restore Personality            |                          5-20 |     30 |   19 | Y     | Yes    | `restore personality`            |
| Restore Sorcery                | 5 / 5 / 5 / 5 / 5 / 5 / 5 / 5 |      5 |   10 | -     | -      | `T_De_Res_RestoreSorcery`        |
| Restore Speed                  |                          5-20 |     30 |   19 | Y     | Yes    | `restore speed`                  |
| Restore Strength               |                          5-20 |     30 |   19 | Y     | Yes    | `restore strength`               |
| Restore Willpower              |                          5-20 |     30 |   19 | Y     | Yes    | `restore willpower`              |
| Rilm's Cure                    |                             1 |      1 |   15 | -     | -      | `rilm's cure`                    |
| Rilm's Gift                    |                         1 / 1 |      1 |   30 | -     | -      | `rilm's gift`                    |
| Rilm's Grace                   |                             5 |   2880 |  720 | -     | -      | `rilm's grace`                   |
| Seryn's Blessing               |                            20 |     10 |   20 | Y     | Yes    | `seryn's blessing`               |
| Seryn's Gift                   |                             1 |      1 |    5 | -     | -      | `seryn's gift`                   |
| Shield of the Armiger          |                            30 |     10 |   75 | Y     | Yes    | `shield of the armiger`          |
| Shockguard                     |                         20-40 |     30 |   90 | Y     | Yes    | `shockguard`                     |
| Skylamp's Shadow               |                          5-20 |     30 |   19 | Y     | -      | `skylamp's shadow`               |
| Stamina                        |                         10-30 |     30 |   30 | Y     | Yes    | `stamina`                        |
| Strong Heal Companion          |                          6-25 |      1 |    4 | -     | -      | `strong heal companion`          |
| Strong Resist Fire             |                            20 |     10 |   20 | Y     | Yes    | `strong resist fire`             |
| Strong Resist Frost            |                            20 |     10 |   20 | Y     | Yes    | `strong resist frost`            |
| Strong Resist Magicka          |                            20 |     10 |   20 | Y     | Yes    | `strong resist magicka`          |
| Strong Resist Poison           |                            20 |     10 |   20 | Y     | Yes    | `strong resist poison`           |
| Strong Resist Shock            |                            20 |     10 |   20 | Y     | Yes    | `strong resist shock`            |
| Troll Strength                 |                            10 |     60 |   30 | -     | -      | `Troll Strength`                 |
| Turn of the Wheel              |                          5-20 |     30 |   19 | -     | -      | `turn of the wheel`              |
| Variable Resist Common Disease |                          1-30 |     10 |   16 | Y     | Yes    | `variable resist common disease` |
| Variable Resist Fire           |                          1-30 |     10 |   16 | Y     | Yes    | `variable resist fire`           |
| Variable Resist Frost          |                          1-30 |     10 |   16 | Y     | Yes    | `variable resist frost`          |
| Variable Resist Magicka        |                          1-30 |     10 |   16 | Y     | Yes    | `variable resist magicka`        |
| Variable Resist Poison         |                          1-30 |     10 |   16 | Y     | Yes    | `variable resist poison`         |
| Variable Resist Shock          |                          1-30 |     10 |   16 | Y     | Yes    | `variable resist shock`          |
| Veloth's Benison               |                            10 |      1 |    3 | -     | -      | `veloth's benison`               |
| Veloth's Gift                  |                            10 |      1 |    3 | -     | -      | `veloth's gift`                  |
| Veloth's Grace                 |                            10 |      2 |    5 | -     | -      | `veloth's grace`                 |
| Vigor                          |                          5-20 |     30 |    9 | Y     | Yes    | `vigor`                          |
| Vitality                       |                          5-20 |     30 |   19 | -     | -      | `vitality`                       |
| Vivec's Mercy                  |                            20 |     10 |   50 | Y     | Yes    | `vivec's mercy`                  |
| Vivec's Tears                  |                             1 |      1 |  100 | -     | -      | `vivec's tears`                  |
| Wisdom                         |                            10 |     60 |   30 | -     | -      | `wisdom`                         |
| Zenithar's Gospel              |                            10 |     90 |   45 | -     | -      | `Zenithar_gospel`                |

## Missing Spells to Consider

Buyable spells **not** yet in `R3 - Spells.json` whose effects use a magic effect we rebalanced. These are the candidates to review for import/adjustment; spells with no changed base cost are omitted since they need no attention.

**Total to consider: 112** (of 359 spells missing from R3).

| Spell                      | School      |                           Mag |         Dur | Cost | Recalc    | ID                               |
| -------------------------- | ----------- | ----------------------------: | ----------: | ---: | --------- | -------------------------------- |
| Fenrick's Doorjam          | Alteration  |                            10 |           1 |    1 | Yes       | `fenrick's doorjam`              |
| Fifth Barrier              | Alteration  |                            50 |          30 |  150 | Yes       | `fifth barrier`                  |
| Fourth Barrier             | Alteration  |                            40 |          30 |  120 | Yes       | `fourth barrier`                 |
| Great Open                 | Alteration  |                            50 |           1 |   15 | Yes       | `great open`                     |
| Lock                       | Alteration  |                             5 |           1 |    1 | Yes       | `lock`                           |
| Ondusi's Open Door         | Alteration  |                            50 |           1 |   15 | Yes       | `ondusi's open door`             |
| Open                       | Alteration  |                            20 |           1 |    6 | Yes       | `open`                           |
| Savi's Swift-Stroke        | Alteration  |                            40 |          15 |   50 | Yes       | `TR_m7_AI_Savi_Swim`             |
| Second Barrier             | Alteration  |                            20 |          30 |   60 | Yes       | `second barrier`                 |
| Sixth Barrier              | Alteration  |                            60 |          30 |  180 | Yes       | `sixth barrier`                  |
| Strong Open                | Alteration  |                            50 |           1 |   15 | Yes       | `strong open`                    |
| Thelen Kaarn's Feather     | Alteration  |                            50 |          10 |   25 | Yes       | `T_Nor_Alt_UlmsJuicedawsFeather` |
| Third Barrier              | Alteration  |                            30 |          30 |   90 | Yes       | `third barrier`                  |
| Wild Open                  | Alteration  |                         1-100 |           1 |   15 | Yes       | `wild open`                      |
| Absorb Health [Ranged]     | Destruction |                          5-20 |           1 |    8 | Yes       | `absorb health [ranged]`         |
| Amatarya's Repurposing     | Destruction |                 15-20 / 20-30 |           5 |   66 | Yes       | `TR_m7_AmataryaAbsorb`           |
| Blood Curse: Fatigue       | Destruction |                         10-20 |           5 |   23 | Yes       | `blood curse: fatigue`           |
| Cause Disease              | Destruction | 10-30 / 2-6 / 2-6 / 2-6 / 2-6 |      20 / 1 |   70 | Yes       | `T_Com_Des_CauseDisease`         |
| Clench                     | Destruction |                          1-20 |           1 |    4 | Yes       | `clench`                         |
| Conduction                 | Destruction |        47-102 / 23-48 / 12-25 |           0 |   48 | Cost only | `TR_m7_IndrasiShock`             |
| Deadly Poison              | Destruction |                          1-20 |          10 |   47 | Cost only | `deadly poison`                  |
| Deadly Poison [Ranged]     | Destruction |                          1-20 |          10 |   71 | Cost only | `deadly poison [ranged]`         |
| Dire Shockball             | Destruction |                         40-50 |           0 |   24 | Cost only | `dire shockball`                 |
| Drain Blood                | Destruction |                         5 / 5 |          30 |   60 | Yes       | `drain blood`                    |
| Dread Curse: Strength      | Destruction |                          5-12 |           1 |    3 | Yes       | `dread curse: strength`          |
| Emasculate                 | Destruction |                          1-20 |           1 |    4 | Yes       | `emasculate`                     |
| Evil Eye                   | Destruction |                          1-10 |           1 |    2 | Yes       | `evil eye`                       |
| Felms' Punishment          | Destruction |                          1-20 |           1 |    9 | Yes       | `T_De_Des_SphereWeakness`        |
| Fire Bite                  | Destruction |                         15-30 |           1 |    6 | Cost only | `fire bite`                      |
| Fire Storm                 | Destruction |                          1-10 |          10 |   23 | Cost only | `fire storm`                     |
| Fireball                   | Destruction |                          2-20 |           1 |    5 | Cost only | `fireball`                       |
| Firebloom                  | Destruction |                          1-25 |           5 |   26 | Cost only | `firebloom`                      |
| Firefist                   | Destruction |                 10-24 / 10-24 |           1 |   11 | Cost only | `firefist`                       |
| Five Fingers of Pain       | Destruction |   3-5 / 3-5 / 3-5 / 3-5 / 3-5 |           1 |    5 | Cost only | `five fingers of pain`           |
| Flame                      | Destruction |                          1-15 |           1 |    2 | Cost only | `flame`                          |
| Flameblast                 | Destruction |                  54-134 / 4-8 |       0 / 8 |   56 | Cost only | `TR_m7_IndrasiFire`              |
| Flamebolt                  | Destruction |                         10-50 |           2 |   24 | Cost only | `flamebolt`                      |
| Freezing Gale              | Destruction |                         18-46 |           4 |   46 | Cost only | `TR_m7_IndrasiFrost`             |
| Freezing Touch             | Destruction |                         15-30 |           1 |    6 | Cost only | `freezing touch`                 |
| Frost Bolt                 | Destruction |                         10-50 |           2 |   24 | Cost only | `frost bolt`                     |
| Frost Storm                | Destruction |                          1-10 |          10 |   23 | Cost only | `frost storm`                    |
| Frostball                  | Destruction |                          2-20 |           1 |    5 | Cost only | `frostball`                      |
| Frostbite                  | Destruction |                         15-30 |           1 |    6 | Cost only | `frostbite`                      |
| Frostbloom                 | Destruction |                          1-25 |           5 |   26 | Cost only | `frostbloom`                     |
| Frostfist                  | Destruction |                 10-24 / 10-24 |           1 |   11 | Cost only | `frostfist`                      |
| Fuddle                     | Destruction |                          1-20 |           1 |    4 | Yes       | `fuddle`                         |
| Gash Spirit                | Destruction |                          5-20 |          30 |   75 | Yes       | `gash spirit`                    |
| Gash Spirit [Ranged]       | Destruction |                          5-20 |          30 |  113 | Yes       | `gash spirit [ranged]`           |
| Ghost Curse                | Destruction |                 5 / 10 / 1-10 |      30 / 1 |   40 | Yes       | `Ghost Curse`                    |
| God's Spark                | Destruction |                          5-50 |          10 |  147 | Cost only | `god's spark`                    |
| Grave Curse: Magicka       | Destruction |                           2-4 |          10 |   18 | Yes       | `grave curse: spell points`      |
| Greater Fireball           | Destruction |                          2-40 |           1 |   10 | Cost only | `Fireball_large`                 |
| Greater Frostball          | Destruction |                          2-40 |           1 |   10 | Cost only | `Frostball_large`                |
| Gripes                     | Destruction |                          1-20 |           1 |    4 | Yes       | `gripes`                         |
| Hex                        | Destruction |                          1-20 |           1 |    4 | Yes       | `hex`                            |
| Ice Bolt                   | Destruction |                          1-35 |           5 |   34 | Cost only | `T_Com_Des_IceBolt`              |
| Ice Storm                  | Destruction |                          1-30 |           5 |   33 | Cost only | `T_Com_Des_IceStorm`             |
| Ignite Foe                 | Destruction |                           1-5 |          60 |   68 | Cost only | `T_Com_Des_IgniteFoe`            |
| Ironhand                   | Destruction |                         21-42 |           1 |    6 | Yes       | `ironhand`                       |
| Judgement Ordained         | Destruction |               2 / 2 / 15 / 15 |     15 / 10 |   45 | Cost only | `T_De_Des_IndGuardJudgement`     |
| Knuckle Luck               | Destruction |                         3-120 |           1 |   12 | Yes       | `knuckle luck`                   |
| Lightning                  | Destruction |                          1-25 |           5 |   34 | Cost only | `T_Com_Des_Lightning`            |
| Lightning Bolt             | Destruction |                         10-50 |           2 |   34 | Cost only | `lightning bolt`                 |
| Maid of Rime               | Destruction |                         30-75 |           2 |   13 | Cost only | `T_Com_Des_MaidRime`             |
| Meat Rot                   | Destruction |                    1-20 / 1-5 |           2 |   11 | Yes       | `T_Rea_Des_MeatRot`              |
| Mother's Ire               | Destruction |               2 / 2 / 20 / 15 | 15 / 1 / 10 |   45 | Yes       | `T_De_Des_IndGuardMothersIre`    |
| Mountain Wind              | Destruction |                      5-10 / 1 |           5 |   38 | Yes       | `T_Nor_Des_MountainWind`         |
| Poison Sting               | Destruction |                         6 / 1 |       4 / 2 |   15 | Yes       | `T_Cr_Des_SkyrenderPoison`       |
| Poisonbloom                | Destruction |                          1-20 |           5 |   39 | Cost only | `poisonbloom`                    |
| Poisonous Touch            | Destruction |                         15-40 |           1 |   12 | Cost only | `poisonous touch`                |
| Potent Poison              | Destruction |                         20-40 |           5 |   68 | Cost only | `potent poison`                  |
| Potent Poison [Ranged]     | Destruction |                         20-40 |           5 |  101 | Cost only | `potent poison [ranged]`         |
| Renesa's Hindering Flames  | Destruction |             21-39 / 5-9 / 150 |      3 / 10 |   73 | Yes       | `TR_m3_RenesaFire`               |
| Righteousness              | Destruction |                            10 |           1 |    4 | Yes       | `righteousness`                  |
| Shock                      | Destruction |                          1-15 |           1 |    3 | Cost only | `shock`                          |
| Shockbite                  | Destruction |                         35-45 |           2 |   28 | Cost only | `shockbite`                      |
| Shockbloom                 | Destruction |                          1-25 |           5 |   37 | Cost only | `shockbloom`                     |
| Shocking Touch             | Destruction |                          3-30 |           1 |    6 | Cost only | `shocking touch`                 |
| Sigillah's Mind Blast      | Destruction |           68-124 / 10-27 / 40 |       0 / 3 |   70 | Yes       | `TR_m7_SigillahShock`            |
| Sphere of Weakness         | Destruction |                          1-20 |           1 |    9 | Yes       | `T_Com_Des_SphereWeakness`       |
| Stumble                    | Destruction |                          1-20 |           1 |    4 | Yes       | `stumble`                        |
| Tag                        | Destruction |                         40-50 |           8 |   65 | Yes       | `T_Com_Mys_Tag`                  |
| Thunderclap                | Destruction |                    35-45 / 60 |       2 / 5 |   63 | Yes       | `TR_m3_ReveaTelamSpell`          |
| Viper                      | Destruction |                           2-8 |           1 |    2 | Cost only | `viper`                          |
| Viperbite                  | Destruction |                          1-30 |           1 |    7 | Cost only | `viperbite`                      |
| Viperbolt                  | Destruction |                         10-50 |           2 |   44 | Cost only | `viperbolt`                      |
| Vivec's Wrath              | Destruction | 10-20 / 10-20 / 10-20 / 10-20 |           1 |   28 | Cost only | `vivec's_wrath`                  |
| Wild Shockbloom            | Destruction |                          2-40 |           1 |   14 | Cost only | `wild shockbloom`                |
| Wildfire                   | Destruction |                          1-15 |           5 |   15 | Cost only | `T_Com_Des_Wildfire`             |
| Winds of Storm             | Destruction |                         30-75 |           2 |   28 | Cost only | `T_Com_Des_WindsStorm`           |
| Wizard Rend                | Destruction |                     10-35 / 1 |           4 |   39 | Yes       | `wizard rend`                    |
| Woe                        | Destruction |                          1-20 |           1 |    4 | Yes       | `woe`                            |
| Arvs' Confounding          | Illusion    |            30-40 / 30-40 / 10 |      10 / 0 |   60 | Yes       | `TR_m3_ArvsWeaken`               |
| Charming Touch             | Illusion    |                            30 |          30 |  225 | Yes       | `charming touch`                 |
| Dazzling Flourish          | Illusion    |             1 / 35-65 / 35-50 |      5 / 10 |   62 | Yes       | `TR_m3_RenasoGalsLight`          |
| Halt                       | Illusion    |                             1 |          15 |   60 | Yes       | `TR_m3_DravaynParalyze`          |
| Medusa's Gaze              | Illusion    |                             1 |          15 |   45 | Yes       | `medusa's gaze`                  |
| Alduin's Maw               | Mysticism   |                            10 |           5 |   25 | Yes       | `T_Nor_Mys_VivecsFeast`          |
| Greater Detect Enchantment | Mysticism   |                            57 |          20 |   57 | Yes       | `T_Com_Mys_DetectEnemy`          |
| Greater Detect Enchantment | Mysticism   |                            60 |          20 |   60 | Yes       | `T_Com_Mys_DetectValuables`      |
| Greater Detect Key         | Mysticism   |                           100 |          15 |   76 | Yes       | `T_Com_Mys_DetectInvisibility`   |
| Jhunal's Intercession      | Mysticism   |                            10 |           5 |   25 | Yes       | `T_Nor_Mys_SothasMirror`         |
| Spell Absorption           | Mysticism   |                            10 |           5 |   25 | Yes       | `T_Com_Mys_SpellAbsorption`      |
| Spell Reflection           | Mysticism   |                            10 |           5 |   25 | Yes       | `T_Com_Mys_SpellReflection`      |
| Blightguard                | Restoration |                            10 |           5 |   13 | Yes       | `blightguard`                    |
| Breath of Morihaus         | Restoration |                          1-10 |          20 |    6 | Yes       | `T_Imp_Res_RestStMerris`         |
| Dibella's Whisper          | Restoration |                            20 |          10 |   20 | Yes       | `T_Nor_Res_SerynsBlessing`       |
| Enrichment                 | Restoration |                          5-20 |          30 |    9 | Yes       | `enrichment`                     |
| Fortify Restoration Skill  | Restoration |                            10 |          60 |   30 | Yes       | `fortify restoration skill`      |
| Four Hands of Morwha       | Restoration |                            20 |          10 |   20 | Yes       | `T_Rga_Res_SerynsBlessing`       |
| Intercession               | Restoration |                           100 |          10 |  100 | Yes       | `TR_m7_Intercession`             |
| Prestidigitation           | Restoration | 10-20 / 10-20 / 10-20 / 10-20 |          15 |   45 | Yes       | `TR_m7_Prestidigitation`         |

## Appendix — Changed Base Costs (R3 vs vanilla/TD)

| Effect              | Base (vanilla/TD) | Base (R3) | No-Scale |
| ------------------- | ----------------: | --------: | -------- |
| AbsorbFatigue       |               4.0 |       6.0 | -        |
| AbsorbHealth        |               8.0 |      16.0 | -        |
| Burden              |               1.0 |       0.1 | -        |
| Charm               |               5.0 |       2.5 | -        |
| DamageAttribute     |               8.0 |      24.0 | -        |
| DamageFatigue       |               4.0 |       2.0 | -        |
| DamageMagicka       |               8.0 |       4.0 | -        |
| DetectAnimal        |              0.75 |      0.15 | -        |
| DetectEnchantment   |               1.0 |       0.2 | -        |
| DetectKey           |               1.0 |       0.2 | -        |
| DisintegrateArmor   |               6.0 |       0.6 | -        |
| DisintegrateWeapon  |               6.0 |       1.2 | -        |
| DrainFatigue        |               2.0 |       0.2 | -        |
| DrainMagicka        |               4.0 |       0.4 | -        |
| Feather             |               1.0 |       0.1 | -        |
| FireDamage          |               5.0 |       8.0 | yes      |
| FortifyFatigue      |               0.5 |      0.25 | -        |
| FortifySkill        |               1.0 |       4.0 | -        |
| FrostDamage         |               5.0 |       8.0 | yes      |
| Lock                |               2.0 |      24.0 | -        |
| Open                |               6.0 |      12.0 | -        |
| Paralyze            |              40.0 |      80.0 | -        |
| Poison              |               9.0 |       8.0 | yes      |
| Reflect             |              10.0 |       2.5 | -        |
| ResistBlightDisease |               5.0 |      0.25 | -        |
| ResistCommonDisease |               2.0 |       0.1 | -        |
| ResistFire          |               2.0 |       0.5 | -        |
| ResistFrost         |               2.0 |       0.5 | -        |
| ResistMagicka       |               2.0 |       0.5 | -        |
| ResistPoison        |               2.0 |       0.5 | -        |
| ResistShock         |               2.0 |       0.5 | -        |
| RestoreAttribute    |               1.0 |       8.0 | -        |
| RestoreFatigue      |               1.0 |       2.5 | -        |
| Shield              |               2.0 |       1.0 | -        |
| ShockDamage         |               7.0 |       8.0 | yes      |
| Sound               |               3.0 |       1.0 | -        |
| SpellAbsorption     |              10.0 |       2.5 | -        |
| SwiftSwim           |               2.0 |       0.5 | -        |


# Tamriel Data — All Schools Spell Cost Analysis

## R3 Base Cost Changes

| School       | Effect              | Vanilla |    R3 | Factor |
|--------------|---------------------|--------:|------:|-------:|
| Alteration   | Burden              |       1 |   0.1 |  ÷10.0 |
| Alteration   | Feather             |       1 |   0.1 |  ÷10.0 |
| Alteration   | Swift Swim          |       2 |   0.5 |   ÷4.0 |
| Alteration   | Shield              |       2 |     1 |   ÷2.0 |
| Alteration   | Lock                |       2 |    24 |  ×12.0 |
| Destruction  | Damage Attribute    |       8 |    24 |   ×3.0 |
| Destruction  | Damage Fatigue      |       4 |     2 |   ÷2.0 |
| Destruction  | Damage Magicka      |       8 |     4 |   ÷2.0 |
| Destruction  | Disintegrate Armor  |       6 |   0.6 |  ÷10.0 |
| Destruction  | Disintegrate Weapon |       6 |   1.2 |   ÷5.0 |
| Destruction  | Drain Fatigue       |       2 |   0.2 |  ÷10.0 |
| Destruction  | Drain Magicka       |       4 |   0.4 |  ÷10.0 |
| Destruction  | Fire Damage         |       5 |     8 |   ×1.6 |
| Destruction  | Frost Damage        |       5 |     8 |   ×1.6 |
| Destruction  | Poison              |       9 |     8 |  ×0.89 |
| Destruction  | Shock Damage        |       7 |     8 |  ×1.14 |
| Destruction  | Paralyze            |      40 |    80 |   ×2.0 |
| Illusion     | Light               |       1 |   0.2 |   ÷5.0 |
| Illusion     | Night Eye           |       1 |   0.2 |   ÷5.0 |
| Illusion     | Sound               |       3 |     1 |   ÷3.0 |
| Illusion     | Charm               |       5 |   2.5 |   ÷2.0 |
| Mysticism    | Absorb Health       |       8 |    16 |   ×2.0 |
| Mysticism    | Absorb Fatigue      |       4 |     6 |   ×1.5 |
| Mysticism    | Reflect             |      10 |   2.5 |   ÷4.0 |
| Mysticism    | Spell Absorption    |      10 |   2.5 |   ÷4.0 |
| Mysticism    | Detect Animal       |    0.75 |  0.15 |   ÷5.0 |
| Mysticism    | Detect Enchantment  |       1 |   0.2 |   ÷5.0 |
| Mysticism    | Detect Key          |       1 |   0.2 |   ÷5.0 |
| Restoration  | Restore Fatigue     |       1 |   2.5 |   ×2.5 |
| Restoration  | Restore Attribute   |       1 |     8 |   ×8.0 |
| Restoration  | Fortify Fatigue     |     0.5 |  0.25 |   ÷2.0 |
| Restoration  | Fortify Skill       |       1 |     4 |   ×4.0 |
| Restoration  | Resist Common Dis.  |       2 |   0.1 |  ÷20.0 |
| Restoration  | Resist Blight Dis.  |       5 |  0.25 |  ÷20.0 |
| Restoration  | Resist Fire         |       2 |   0.5 |   ÷4.0 |
| Restoration  | Resist Frost        |       2 |   0.5 |   ÷4.0 |
| Restoration  | Resist Shock        |       2 |   0.5 |   ÷4.0 |
| Restoration  | Resist Poison       |       2 |   0.5 |   ÷4.0 |
| Restoration  | Resist Magicka      |       2 |   0.5 |   ÷4.0 |

TD spells have **hand-set costs** (not AUTO_CALCULATE). When added to R3, costs must be set explicitly.

**Adjusted cost** = `floor( Formula@R3 × (TD_cost / Formula@vanilla) )` — preserves the TD author's intended discount/premium relative to formula.

### Spell Cost Formula

```
cost_per_effect = (min + max) × duration × (base_cost / 40) + area × (base_cost / 40)
OnTarget: multiply by 1.5
Multi-effect: sum each effect
```

---

## Destruction

### Damage Attribute (8 → 24)

| Spell                    | Effects                                        | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Kirhnarva's Leg-Breaker  | DA Str 1-8/2s + DA Agi 1-8/2s Touch           |          7 |       7 | 1.000 |          21 |   **21** |
| Meat Rot                 | DA Str 1-5/2s + DH 1-20/2s Touch              |         10 |      11 | 1.100 |          15 |   **16** |
| Mind Rot                 | DA Int 1-5/2s/2ft + DM 1-15/2s/2ft Target     |         14 |      14 | 1.000 |          17 |   **17** |

---

### Damage Fatigue (4 → 2)

| Spell                    | Effects                                                  | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|----------------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Hairdoch's Extinguisher  | DF 2/10s/1ft + Paralyze/10s/1ft + DH 2/10s/1ft Target   |         49 |      40 | 0.816 |          78 |   **63** |

*Paralyze doubles in R3 (40→80), driving the formula cost up sharply.*

---

### Damage Health (8 → 8, unchanged)

| Spell                    | Effects                                                            | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------------------------------|----------:|--------:|------:|------------:|---------:|
| Din of Revelations       | DH 20/30s Self + Restore Health 20/10s Self                        |       290 |     145 | 0.500 |         290 |  **145** |
| Jogvir's Soul Theft      | DH 1/30s/3ft + Soultrap 30s/3ft Target                             |        30 |      24 | 0.800 |          30 |   **24** |
| Meridians Burning Light  | DH 5/5s/4ft + Turn Undead 20-30/30s/4ft + Light 5/30s/4ft Target  |       196 |      15 | 0.077 |         187 |   **14** |
| Pinprick                 | DH 2/1s Target                                                     |         1 |       1 | 1.000 |           1 |    **1** |
| Sload Spell              | DH 1-20/3s/3ft Target                                              |        19 |      20 | 1.053 |          19 |   **20** |

---

### Damage Magicka (8 → 4)

| Spell                    | Effects                                        | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Thimble of Magefire      | DM 10-30/1s Target                             |         12 |       6 | 0.500 |           6 |    **3** |
| Mind Rot                 | (see Damage Attribute)                         |          — |      — |    — |           — |       — |

---

### Disintegrate Armor (6 → 0.6)

| Spell                    | Effects                                        | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Fracture Armor           | DisA 100/2s Touch                              |         60 |      40 | 0.667 |           6 |    **4** |
| Shadow Rust              | DisA 1-5/20s/2ft + Burden 1-15/20s/2ft Target |         39 |      30 | 0.769 |           3 |    **2** |

---

### Disintegrate Weapon (6 → 1.2)

| Spell                    | Effects                          | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|----------------------------------|-----------:|--------:|------:|------------:|---------:|
| Iron Eater               | DisW 1-25/2s/2ft Target          |         12 |      12 | 1.000 |           2 |    **2** |
| Steel Eater              | DisW 5-30/3s/4ft Target          |         24 |      25 | 1.042 |           4 |    **4** |

---

### Drain Fatigue (2 → 0.2)

| Spell                    | Effects                | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------|-----------:|--------:|------:|------------:|---------:|
| Duck                     | DrF 200/2s Target      |         60 |      40 | 0.667 |           6 |    **4** |

---

### Drain Health (4 → 4, unchanged)

| Spell                    | Effects             | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|---------------------|-----------:|--------:|------:|------------:|---------:|
| Vampire's Touch          | DrH 10/5s Touch     |         10 |      10 | 1.000 |          10 |   **10** |

---

### Drain Magicka (4 → 0.4)

| Spell                    | Effects                                        | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Dhamcka's Soul-Withering | DrM 1/30s/1ft + Soultrap 30s/1ft Target        |         20 |      14 | 0.700 |          12 |    **8** |
| Rage of Magnus           | DrM 60/10s/10ft Target                         |        181 |     160 | 0.884 |          18 |   **15** |

---

### Fire Damage (5 → 8)

| Spell                    | Effects                                          | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Apocalyptic Bloodstorm   | Fire 5/5s/10ft + Absorb Health 2/5s/10ft Target  |         20 |      10 | 0.500 |          36 |   **18** |
| Cey Molag                | Fire 20-40/3s/10ft Target                        |         35 |      13 | 0.371 |          57 |   **21** |
| Fiery Consolation        | Fire 30-50/1s/5ft + Fire 1-2/15s/10ft Target     |         26 |      25 | 0.962 |          42 |   **40** |
| Wildfire                 | Fire 1-15/5s Target                              |         15 |      15 | 1.000 |          24 |   **24** |

---

### Frost Damage (5 → 8)

| Spell                    | Effects                                                  | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|----------------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Celestial Frost          | Frost 15-50/0s/25ft + Absorb Fat 15-50/0s/25ft Target   |          8 |      30 | 3.750 |          13 |   **48** |
| Cey Mafre                | Frost 20-40/3s/10ft Target                               |         35 |      13 | 0.371 |          57 |   **21** |
| Ice Bolt                 | Frost 1-35/5s Target                                     |         33 |      34 | 1.030 |          54 |   **55** |
| Ice Storm                | Frost 1-30/5s/20ft Target                                |         32 |      34 | 1.062 |          52 |   **55** |
| Maid of Rime             | Frost 30-75/2s Touch                                     |         26 |      13 | 0.500 |          42 |   **21** |
| Mountain Wind            | Frost 5-10/5s/5ft + Paralyze/5s/5ft Target               |         37 |      38 | 1.027 |          69 |   **70** |
| Sliver of Skinchill      | Frost 10-30/3s Target                                    |         22 |      12 | 0.545 |          36 |   **19** |

*Celestial Frost has 0s duration — only area contributes. TD set it at 3.75× formula.*
*Mountain Wind: Paralyze doubles in R3, pushing formula from 37 to 69.*

---

### Poison (9 → 8)

| Spell                    | Effects                                    | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------|----------:|--------:|------:|------------:|---------:|
| Cuhlecain's Curse        | Poison 3/10s + Blind 50-100%/10s Touch     |        51 |      35 | 0.686 |          49 |   **33** |

---

### Shock Damage (7 → 8)

| Spell                    | Effects                                    | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------|----------:|--------:|------:|------------:|---------:|
| Cey Belle                | Shock 20-40/3s/10ft Target                 |        49 |      18 | 0.367 |          57 |   **20** |
| Lightning                | Shock 1-25/5s Target                       |        34 |      34 | 1.000 |          39 |   **39** |
| Light that Burns         | Shock 1-10/10s + Light 20/10s Touch        |        29 |      21 | 0.724 |          24 |   **17** |
| Shock                    | Shock 0/3s/5ft Touch                       |         0 |       1 |   n/a |           1 |    **1** |
| Winds of Storm           | Shock 30-75/2s Target                      |        55 |      28 | 0.509 |          63 |   **32** |

---

### Paralyze (40 → 80)

Effects handled in multi-effect spells above (Hairdoch's Extinguisher, Mountain Wind).

---

### Weakness effects (unchanged)

| Spell                    | Effects                       | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|-------------------------------|-----------:|--------:|------:|------------:|---------:|
| Fovila's Love            | Weakness Corprus 100%/20s Self |       400 |      50 | 0.125 |         400 |   **50** |
| Fear of the Flame        | Weakness Fire 100%/5s Touch   |        50 |      35 | 0.700 |          50 |   **35** |
| Terror of Baluok-Mir     | Weakness Frost 50%/15s Target |       112 |     200 | 1.786 |         112 |  **200** |

---

## Illusion

### Light (1 → 0.2)

| Spell                    | Effects                                    | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------|----------:|--------:|------:|------------:|---------:|
| Azura's Light            | Light 20/120s Self                         |       120 |      10 | 0.083 |          24 |    **2** |

*TD set it at 0.08× formula — massive discount. At R3 base the formula collapses to 24, adjusted = 2.*

---

### Night Eye (1 → 0.2)

| Spell                    | Effects                                    | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------|----------:|--------:|------:|------------:|---------:|
| Greater Raven Eye        | Night Eye 30/90s Self                      |       135 |      27 | 0.200 |          27 |    **5** |
| Hunter's Eye             | Chameleon 15%/60s + NE 15/60s Self         |        90 |      20 | 0.222 |          54 |   **12** |
| Orc's Eye                | Night Eye 30/30s Self                      |        45 |       8 | 0.178 |           9 |    **1** |
| Raven Eye                | Night Eye 15/60s Self                      |        45 |       9 | 0.200 |           9 |    **1** |

*Night Eye spells collapse heavily at ÷5 base. All were already discounted in TD.*

---

### Unchanged effects

No cost change needed for: Blindfold, Serene Nature, Smoke and Mirrors, Monstrous Vision, Skein of Convulsion, On the Move, Shameful Cowardice, Wind of Kyne, Etherealness, Falen's Justice, Steadfast.

Already in mod: Voices (Sound ÷3), Alluring Speech (Charm ÷2), Living Statue (Paralyze ×2), Paralysis TD (Paralyze ×2).

---

## Mysticism

### Absorb Health (8 → 16)

| Spell                    | Effects                                              | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Bloodlust of Molag Bal   | Absorb Str 5-15/15s/1ft + AbsH 3-4/3s/1ft Target    |         96 |      20 | 0.208 |         103 |   **21** |
| Dread Curse of the Lich  | AbsFat+AbsH+AbsMag 5-12/1s + AbsAttr×5 5-12/10s Touch |      178 |      51 | 0.287 |         182 |   **52** |
| Necromancer's Soul Trap  | AbsH 1-3/45s/3ft + Soultrap×3 45s/3ft Target         |       107 |      65 | 0.607 |         162 |   **98** |

Already in mod: Lifesteal.

---

### Absorb Fatigue (4 → 6)

| Spell                    | Effects                                              | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------------|-----------:|--------:|------:|------------:|---------:|
| Tag                      | Absorb Fatigue 40-50/8s Touch                        |         72 |      65 | 0.903 |         108 |   **97** |

*Celestial Frost also uses Absorb Fatigue — handled under Frost Damage.*

---

### Detect Key (1 → 0.2)

| Spell                    | Effects                                    | Formula @V | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|--------------------------------------------|----------:|--------:|------:|------------:|---------:|
| Fuchon Cire's Keyfinder  | Detect Key 1-15ft/60s Self                 |        24 |      25 | 1.042 |           4 |    **4** |

---

### Unchanged effects

No cost change needed for: Jogvir's Extended Arm (Telekinesis), Nahgacra's Soul Thef (Soultrap), Temple Song (Almsivi Intervention), Mara's Touch (Dispel), Remove Enchantment (Dispel), Reunrefine (Dispel).

Already in mod: St. Naharine's Shield (Reflect ÷4), Distorted Reflection (Reflect ÷4), Reflect Damage (Reflect ÷4), St. Horuscia's Alms (Spell Abs ÷4), Jogvir's Sword Hand, Greater Detect Creature (Detect Animal ÷5), Detect Enchantment TD (Detect Ench ÷5).

---

## Restoration

All TD Restoration spells with changed base costs are already in the mod: Eagle Eye, Treefellers Rage, Deft Security (Fortify Skill ×4), Pilgrimage of St. Rosunius (Resist Common ÷20), Wintery Mantle (Resist Frost ÷4), Impossible Effort (Fortify Fatigue ÷2), Greater Stamina (Restore Fatigue ×2.5).

No remaining TD Restoration spells need cost adjustment.

---

## Conjuration

No base cost changes affect Conjuration effects. All TD Conjuration spells keep their TD costs unchanged.

---

## Alteration

All TD Alteration spells with changed base costs are already in the mod: Shadow Rust, Weight of Guilt (Burden ÷10), Fling, Zenithar's Arms (Feather ÷10), Dreugh's Grace (Swift Swim ÷4), Falling First Barrier, Force Wall, Tsun's Ward (Shield ÷2), Dalgor's Entwining, Wizard Lock (Lock ×12), Fire Eye (NE ÷5 minor).

No remaining TD Alteration spells need cost adjustment.

---

## Complete Summary

### All spells requiring cost adjustment (proposed ≠ TD cost)

| Spell                    | School      | TD Cost | Proposed | Delta | Primary driver                    |
|--------------------------|-------------|--------:|---------:|------:|-----------------------------------|
| Kirhnarva's Leg-Breaker  | Destruction |       7 |       21 |   +14 | DA ×3                             |
| Meat Rot                 | Destruction |      11 |       16 |    +5 | DA ×3                             |
| Mind Rot                 | Destruction |      14 |       17 |    +3 | DA ×3 + DM ÷2 (net up)           |
| Hairdoch's Extinguisher  | Destruction |      40 |       63 |   +23 | Paralyze ×2 + DF ÷2              |
| Meridians Burning Light  | Destruction |      15 |       14 |    −1 | Light ÷5 (minor)                 |
| Thimble of Magefire      | Destruction |       6 |        3 |    −3 | DM ÷2                            |
| Fracture Armor           | Destruction |      40 |        4 |   −36 | DisA ÷10                          |
| Shadow Rust              | Destruction |      30 |        2 |   −28 | DisA ÷10 + Burden ÷10            |
| Iron Eater               | Destruction |      12 |        2 |   −10 | DisW ÷5                           |
| Steel Eater              | Destruction |      25 |        4 |   −21 | DisW ÷5                           |
| Duck                     | Destruction |      40 |        4 |   −36 | DrF ÷10                           |
| Dhamcka's Soul-Withering | Destruction |      14 |        8 |    −6 | DrM ÷10                           |
| Rage of Magnus           | Destruction |     160 |       15 |  −145 | DrM ÷10                           |
| Apocalyptic Bloodstorm   | Destruction |      10 |       18 |    +8 | Fire ×1.6 + AbsH ×2              |
| Cey Molag                | Destruction |      13 |       21 |    +8 | Fire ×1.6                         |
| Fiery Consolation        | Destruction |      25 |       40 |   +15 | Fire ×1.6                         |
| Wildfire                 | Destruction |      15 |       24 |    +9 | Fire ×1.6                         |
| Celestial Frost          | Destruction |      30 |       48 |   +18 | Frost ×1.6 + AbsFat ×1.5         |
| Cey Mafre                | Destruction |      13 |       21 |    +8 | Frost ×1.6                        |
| Ice Bolt                 | Destruction |      34 |       55 |   +21 | Frost ×1.6                        |
| Ice Storm                | Destruction |      34 |       55 |   +21 | Frost ×1.6                        |
| Maid of Rime             | Destruction |      13 |       21 |    +8 | Frost ×1.6                        |
| Mountain Wind            | Destruction |      38 |       70 |   +32 | Frost ×1.6 + Paralyze ×2         |
| Sliver of Skinchill      | Destruction |      12 |       19 |    +7 | Frost ×1.6                        |
| Cuhlecain's Curse        | Destruction |      35 |       33 |    −2 | Poison ×0.89                      |
| Cey Belle                | Destruction |      18 |       20 |    +2 | Shock ×1.14                       |
| Lightning                | Destruction |      34 |       39 |    +5 | Shock ×1.14                       |
| Light that Burns         | Destruction |      21 |       17 |    −4 | Shock ×1.14 + Light ÷5           |
| Winds of Storm           | Destruction |      28 |       32 |    +4 | Shock ×1.14                       |
| Azura's Light            | Illusion    |      10 |        2 |    −8 | Light ÷5                          |
| Greater Raven Eye        | Illusion    |      27 |        5 |   −22 | NE ÷5                            |
| Hunter's Eye             | Illusion    |      20 |       12 |    −8 | NE ÷5 (Chameleon unchanged)      |
| Orc's Eye                | Illusion    |       8 |        1 |    −7 | NE ÷5                            |
| Raven Eye                | Illusion    |       9 |        1 |    −8 | NE ÷5                            |
| Bloodlust of Molag Bal   | Mysticism   |      20 |       21 |    +1 | AbsH ×2                          |
| Dread Curse of the Lich  | Mysticism   |      51 |       52 |    +1 | AbsH ×2 + AbsFat ×1.5            |
| Necromancer's Soul Trap  | Mysticism   |      65 |       98 |   +33 | AbsH ×2                          |
| Tag                      | Mysticism   |      65 |       97 |   +32 | AbsFat ×1.5                       |
| Fuchon Cire's Keyfinder  | Mysticism   |      25 |        4 |   −21 | Detect Key ÷5                    |


### Spells with no cost change needed (proposed = TD cost)

| Spell                    | School      | TD Cost | Reason                                |
|--------------------------|-------------|--------:|---------------------------------------|
| Din of Revelations       | Destruction |     145 | DH + Restore Health both unchanged    |
| Jogvir's Soul Theft      | Destruction |      24 | DH + Soultrap unchanged               |
| Pinprick                 | Destruction |       1 | trivial                               |
| Sload Spell              | Destruction |      20 | DH unchanged                          |
| Vampire's Touch          | Destruction |      10 | DrH unchanged                         |
| Shock                    | Destruction |       1 | trivial                               |
| Fovila's Love            | Destruction |      50 | Weakness unchanged                    |
| Fear of the Flame        | Destruction |      35 | Weakness unchanged                    |
| Terror of Baluok-Mir     | Destruction |     200 | Weakness unchanged                    |
| Blindfold                | Illusion    |      60 | Blind unchanged                       |
| Serene Nature            | Illusion    |      10 | Calm Creature unchanged               |
| Smoke and Mirrors        | Illusion    |      60 | Chameleon unchanged                   |
| Monstrous Vision         | Illusion    |      20 | Demoralize unchanged                  |
| Skein of Convulsion      | Illusion    |      75 | Demoralize unchanged                  |
| On the Move              | Illusion    |      20 | Demoralize unchanged                  |
| Shameful Cowardice       | Illusion    |       5 | Invisibility unchanged                |
| Wind of Kyne             | Illusion    |      55 | Invis + Levitate unchanged            |
| Etherealness             | Illusion    |      50 | Sanctuary unchanged                   |
| Falen's Justice          | Illusion    |      45 | Sanctuary unchanged                   |
| Steadfast                | Illusion    |       8 | Rally Humanoid unchanged              |
| Jogvir's Extended Arm    | Mysticism   |      20 | Telekinesis unchanged                 |
| Nahgacra's Soul Thef     | Mysticism   |      12 | Soultrap unchanged                    |
| Temple Song              | Mysticism   |       8 | Almsivi Intervention unchanged        |
| Mara's Touch             | Mysticism   |      11 | Dispel + Restore Health unchanged     |
| Remove Enchantment       | Mysticism   |      25 | Dispel unchanged                      |
| Reunrefine               | Mysticism   |      40 | Dispel unchanged                      |
| To the ja-Kha'jay        | Alteration  |     130 | Jump unchanged                        |
| Fuchon Cire's Descent    | Alteration  |      20 | Slowfall unchanged                    |
| Slowfalling              | Alteration  |       9 | Slowfall unchanged                    |
| Harkin's Gills           | Alteration  |       5 | Water Breathing unchanged             |
| Suicide Dive             | Alteration  |       2 | Water Breathing unchanged             |
| Light that Protects      | Alteration  |      90 | Radiant Shield unchanged              |
| All Conjuration (19)     | Conjuration |     — | No base cost changes                  |
| All Restoration (17)     | Restoration |     — | Effects unchanged or already in mod   |

---

## Key Concerns

- **Paralyze ×2** makes Mountain Wind (70) and Hairdoch's Extinguisher (63) very expensive.
- **Disintegrate / Drain Magicka / Drain Fatigue** collapse to trivially small costs (2–8). May need flat minimums.
- **Night Eye ÷5** collapses Orc's Eye and Raven Eye to 1. May need flat minimums.
- **Absorb Health ×2** pushes Necromancer's Soul Trap from 65 to 98 and Tag from 65 to 97.
- **Cey trio** (Molag/Mafre/Belle) land at 21/21/20 — consistent.
- **Ice Bolt / Ice Storm** both at 55 — intentionally pricey in TD, stays pricey.
- **Celestial Frost** at 48 — TD set it at 3.75× formula due to 0s duration. Premium preserved.
- **Detect Key ÷5** collapses Fuchon Cire's Keyfinder from 25 to 4.

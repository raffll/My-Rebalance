# Tamriel Data — Destruction Spells Cost Analysis

## Context

R3 changes the base costs of several Destruction effects:

| Effect              | Vanilla |   R3 | Factor |
|---------------------|--------:|-----:|-------:|
| Damage Attribute    |       8 |   24 |   ×3.0 |
| Damage Fatigue      |       4 |    2 |   ÷2.0 |
| Damage Health       |       8 |    8 |    —   |
| Damage Magicka      |       8 |    4 |   ÷2.0 |
| Disintegrate Armor  |       6 |  0.6 |  ÷10.0 |
| Disintegrate Weapon |       6 |  1.2 |   ÷5.0 |
| Drain Fatigue       |       2 |  0.2 |  ÷10.0 |
| Drain Health        |       4 |    4 |    —   |
| Drain Magicka       |       4 |  0.4 |  ÷10.0 |
| Fire Damage         |       5 |    8 |   ×1.6 |
| Frost Damage        |       5 |    8 |   ×1.6 |
| Poison              |       9 |    8 |  ×0.89 |
| Shock Damage        |       7 |    8 |  ×1.14 |
| Paralyze            |      40 |   80 |   ×2.0 |
| Absorb Health       |       8 |   16 |   ×2.0 |
| Absorb Fatigue      |       4 |    6 |   ×1.5 |
| Burden              |       1 |  0.1 |  ÷10.0 |
| Blind               |       1 |    1 |    —   |
| Weakness to *       |       2 |    2 |    —   |

TD spells have **hand-set costs** (not AUTO_CALCULATE). When added to R3, costs must be set explicitly.

**Adjusted cost** = `floor( Formula@R3 × (TD_cost / Formula@vanilla) )` — preserves the TD author's intended discount/premium relative to formula.

### Spell Cost Formula

- **OnTarget:**     `floor( base_cost × ((min + max) × duration + area) / 40 )`
- **OnTouch/Self:** `floor( base_cost × ((min + max) × (duration + 1) + area) / 40 )`

---

## Damage Attribute (8 → 24)

| Spell                  | Effects                                              | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|------------------------|------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Kirhnarva's Leg-Breaker | DA Str 1-8/2s Touch + DA Agi 1-8/2s Touch          |               10 |       7 | 0.700 |          32 |   **22** |
| Meat Rot               | DA Str 1-5/2s Touch + DH 1-20/2s Touch              |               15 |      11 | 0.733 |          22 |   **16** |
| Mind Rot               | DA Int 1-5/2s/2ft Target + DM 1-15/2s/2ft Target    |                7 |      14 | 2.000 |          11 |   **22** |

*Mind Rot was set at 2× formula — intentionally expensive. Adjusted carries that premium forward.*

---

## Damage Fatigue (4 → 2)

| Spell                   | Effects                                                              | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|-------------------------|----------------------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Hairdoch's Extinguisher | DF 2/10s/1ft + Paralyze/10s/1ft + DH 2/10s/1ft (Target)            |               33 |      40 | 1.212 |          52 |   **63** |

*Paralyze doubles in R3 (40→80), driving the formula cost up sharply. Adjusted cost reflects both the base cost changes and the TD premium.*

---

## Damage Health (8 → 8, unchanged)

| Spell                   | Effects                                                              | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|-------------------------|----------------------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Din of Revelations      | DH 20/30s Self + Restore Health 20/10s Self                         |              303 |     145 | 0.478 |         303 |  **144** |
| Hairdoch's Extinguisher | (see Damage Fatigue)                                                 |               — |      40 |    — |           — |       — |
| Jogvir's Soul Theft     | DH 1/30s/3ft Target + Soultrap 30s/3ft Target                       |               16 |      24 | 1.500 |          16 |   **24** |
| Meat Rot                | DH 1-20/2s Touch + DA Str 1-5/2s Touch                              |               15 |      11 | 0.733 |          22 |   **16** |
| Meridians Burning Light | DH 5/5s/4ft Target + Turn Undead 20-30/30s/4ft + Light 5/30s/4ft   |               86 |      15 | 0.174 |          86 |   **14** |
| Pinprick                | DH 2/1s Target                                                       |                0 |       1 |   n/a |           0 |    **1** |
| Sload Spell             | DH 1-20/3s/3ft Target                                                |               13 |      20 | 1.538 |          13 |   **20** |

*Meridians Burning Light has a huge formula cost (86) due to Turn Undead, but TD set it at 15 — heavily discounted. Adjusted preserves that.*
*Din of Revelations adjusted (144) nearly matches TD (145) — the ratio approach works well here.*

---

## Damage Magicka (8 → 4)

| Spell              | Effects                                           | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------|---------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Mind Rot           | (see Damage Attribute)                            |                — |      14 |    — |           — |       — |
| Thimble of Magefire | DM 10-30/1s Target                              |                8 |       6 | 0.750 |           4 |    **3** |

---

## Disintegrate Armor (6 → 0.6)

| Spell          | Effects                                                    | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|----------------|------------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Fracture Armor | DisA 100/2s Touch                                          |               90 |      40 | 0.444 |           9 |    **4** |
| Shadow Rust    | DisA 1-5/20s/2ft Target + Burden 1-15/20s/2ft Target       |               26 |      30 | 1.154 |           1 |    **1** |

*Both spells collapse to near-zero formula cost at 0.6 base. Adjusted costs are minimal — worth reviewing whether these should just use a flat low cost.*

---

## Disintegrate Weapon (6 → 1.2)

| Spell       | Effects                          | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|-------------|----------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Iron Eater  | DisW 1-25/2s/2ft Target          |                8 |      12 | 1.500 |           1 |    **2** |
| Steel Eater | DisW 5-30/3s/4ft Target          |               15 |      25 | 1.667 |           3 |    **5** |

*Same situation as Disintegrate Armor — formula cost collapses at 1.2 base.*

---

## Drain Fatigue (2 → 0.2)

| Spell | Effects                  | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|-------|--------------------------|----------------:|--------:|------:|------------:|---------:|
| Duck  | DrF 200/2s Target        |              40 |      40 | 1.000 |           4 |    **4** |

*Formula cost collapses ÷10. Adjusted cost is 4 — very cheap for a 200pt drain.*

---

## Drain Health (4 → 4, unchanged)

| Spell           | Effects               | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|-----------------|-----------------------|-----------------:|--------:|------:|------------:|---------:|
| Vampire's Touch | DrH 10/5s Touch       |               12 |      10 | 0.833 |          12 |   **10** |

---

## Drain Magicka (4 → 0.4)

| Spell                    | Effects                                              | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------------|------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Dhamcka's Soul-Withering | DrM 1/30s/1ft Target + Soultrap 30s/1ft Target       |               10 |      14 | 1.400 |           4 |    **6** |
| Rage of Magnus           | DrM 60/10s/10ft Target                               |              120 |     160 | 1.333 |          12 |   **16** |

*Rage of Magnus collapses from 120→12 formula cost. Adjusted (16) is still very cheap for a 60pt/10s/10ft drain.*

---

## Fire Damage (5 → 8)

| Spell                  | Effects                                                      | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|------------------------|--------------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Apocalyptic Bloodstorm | Fire 5/5s/10ft + Absorb Health 2/5s/10ft (Target)           |               13 |      10 | 0.769 |          24 |   **18** |
| Cey Molag              | Fire 20-40/3s/10ft (Target)                                  |               23 |      13 | 0.565 |          38 |   **21** |
| Fiery Consolation      | Fire 30-50/1s/5ft + Fire 1-2/15s/10ft (Target)              |               17 |      25 | 1.471 |          28 |   **41** |
| Wildfire               | Fire 1-15/5s (Target)                                        |               10 |      15 | 1.500 |          16 |   **24** |

### Scaled values (÷1.6 for Fire, ÷2 for Absorb Health)

| Spell                  | Scaled effects                              | Recalc cost | Adjusted cost |
|------------------------|---------------------------------------------|------------:|--------------:|
| Apocalyptic Bloodstorm | Fire 3/5s/10ft + Absorb 1/5s/10ft          |          16 |        **18** |
| Cey Molag              | Fire 12-25/3s/10ft                          |          24 |        **21** |
| Fiery Consolation      | Fire 20-30/1s/5ft + Fire 1-2/9s/10ft       |          18 |        **41** |
| Wildfire               | Fire 1-9/5s (or 1-15/3s)                   |      10 (or 9) |      **24** |

*Fiery Consolation adjusted cost (41) is high because it was hand-set above formula at vanilla. Worth reviewing.*

---

## Frost Damage (5 → 8)

| Spell               | Effects                                                    | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|---------------------|------------------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Celestial Frost     | Frost 15-50/0s/25ft + Absorb Fatigue 15-50/0s/25ft (Target) |              5 |      30 | 6.000 |           8 |   **48** |
| Cey Mafre           | Frost 20-40/3s/10ft (Target)                               |               23 |      13 | 0.565 |          38 |   **21** |
| Ice Bolt            | Frost 1-35/5s (Target)                                     |               22 |      34 | 1.545 |          35 |   **54** |
| Ice Storm           | Frost 1-30/5s/20ft (Target)                                |               20 |      34 | 1.700 |          32 |   **54** |
| Maid of Rime        | Frost 30-75/2s (Touch)                                     |               16 |      13 | 0.813 |          25 |   **20** |
| Mountain Wind       | Frost 5-10/5s/5ft + Paralyze/5s/5ft (Target)               |               25 |      38 | 1.520 |          46 |   **69** |
| Sliver of Skinchill | Frost 10-30/3s (Target)                                    |                9 |      12 | 1.333 |          15 |   **20** |

*Celestial Frost has 0s duration — only area contributes to formula cost, making it very cheap by formula (5). TD set it at 30 (6× formula). Adjusted (48) reflects that premium at new base costs.*
*Mountain Wind: Paralyze doubles in R3, pushing formula from 25 to 46. Adjusted (69) is very expensive.*

---

## Poison (9 → 8)

| Spell              | Effects                                        | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------|------------------------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Cuhlecain's Curse  | Poison 3/10s Touch + Blind 50-100%/10s Touch   |               55 |      35 | 0.636 |          54 |   **34** |

---

## Shock Damage (7 → 8)

| Spell           | Effects                           | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|-----------------|-----------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Cey Belle       | Shock 20-40/3s/10ft (Target)      |               32 |      18 | 0.563 |          38 |   **21** |
| Lightning       | Shock 1-25/5s (Target)            |               28 |      34 | 1.214 |          32 |   **38** |
| Shock           | Shock 0/3s/5ft (Touch)            |                0 |       1 |   n/a |           0 |    **1** |
| Winds of Storm  | Shock 30-75/2s (Target)           |               26 |      28 | 1.077 |          30 |   **32** |

---

## Weakness to Corprus Disease (4 → 4, unchanged)

| Spell          | Effects                    | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|----------------|----------------------------|-----------------:|--------:|------:|------------:|---------:|
| Fovila's Love  | Weakness 100%/20s Self     |              420 |      50 | 0.119 |         420 |   **50** |

---

## Weakness to Fire (2 → 2, unchanged)

| Spell              | Effects                      | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|--------------------|------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Fear of the Flame  | Weakness 100%/5s Touch       |               60 |      35 | 0.583 |          60 |   **35** |

---

## Weakness to Frost (2 → 2, unchanged)

| Spell                | Effects                       | Formula @vanilla | TD cost | Ratio | Formula @R3 | Adjusted |
|----------------------|-------------------------------|-----------------:|--------:|------:|------------:|---------:|
| Terror of Baluok-Mir | Weakness 50%/15s Target       |               75 |     200 | 2.667 |          75 |  **200** |

---

## Priority Summary

| Spell                   | Formula @vanilla | TD cost | Formula @R3 | Adjusted | Note |
|-------------------------|----------------:|--------:|------------:|---------:|------|
| Cey Molag               |              23 |      13 |          38 |   **21** | Cey trio — accessible AoE, adjusted stays reasonable |
| Cey Mafre               |              23 |      13 |          38 |   **21** | same |
| Cey Belle               |              32 |      18 |          38 |   **21** | same |
| Apocalyptic Bloodstorm  |              13 |      10 |          24 |   **18** | two-effect AoE |
| Maid of Rime            |              16 |      13 |          25 |   **20** | fine |
| Mountain Wind           |              25 |      38 |          46 |   **69** | Paralyze ×2 drives cost up sharply — review |
| Hairdoch's Extinguisher |              33 |      40 |          52 |   **63** | same — Paralyze component |
| Celestial Frost         |               5 |      30 |           8 |   **48** | 0s duration — TD premium was 6× formula |
| Ice Bolt                |              22 |      34 |          35 |   **54** | intentionally pricey |
| Ice Storm               |              20 |      34 |          32 |   **54** | same |
| Fiery Consolation       |              17 |      25 |          28 |   **41** | was above formula — review premium |
| Wildfire                |              10 |      15 |          16 |   **24** | was above formula |
| Duck ✓                  |              40 |      40 |           4 |    **4** | collapses ÷10 — very cheap |
| Rage of Magnus ✓        |             120 |     160 |          12 |   **16** | collapses ÷10 — very cheap |
| Fracture Armor ✓        |              90 |      40 |           9 |    **4** | collapses ÷10 |
| Shadow Rust ✓           |              26 |      30 |           1 |    **1** | collapses ÷10 |
| Iron Eater ✓            |               8 |      12 |           1 |    **2** | collapses ÷5 |
| Steel Eater ✓           |              15 |      25 |           3 |    **5** | collapses ÷5 |
| Thimble of Magefire ✓   |               8 |       6 |           4 |    **3** | minor |
| Dhamcka's Soul-Withering ✓ |           10 |      14 |           4 |    **6** | minor |
| Sliver of Skinchill     |               9 |      12 |          15 |   **20** | minor |
| Kirhnarva's Leg-Breaker |              10 |       7 |          32 |   **22** | DA ×3 — cost triples |
| Mind Rot                |               7 |      14 |          11 |   **22** | DA ×3 — was 2× formula |
| Meat Rot                |              15 |      11 |          22 |   **16** | DA ×3 |

✓ = already documented in README - Magic.md

**Key concerns:**
- **Paralyze ×2** makes Mountain Wind and Hairdoch's Extinguisher very expensive (69, 63).
- **Disintegrate / Drain Magicka / Drain Fatigue** base costs collapse so far that adjusted costs become trivially small (1–5). These may need a flat minimum cost instead.
- **Damage Attribute ×3** triples the formula cost for Kirhnarva, Meat Rot, Mind Rot.
- **Cey trio** all land at 21 with adjusted method — consistent and reasonable.

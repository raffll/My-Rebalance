# Spell Rules — Reference

How spell values are computed and checked. Companion to
`.kiro/steering/spell-value-rules.md` (the governing spec) and
`docs/Potion-Tier-Rules-By-Effect.md` (potions use a different system — tiers,
not this cost formula).

Scope: the `R3 - Spells.json` plugin (MagicEffect + Spell + GameSetting). Potions
are a separate plugin and follow the potion-tier rules instead.

---

## 1. Cost formula

Per effect:

```
effect_cost = (min + max) × duration × (base_cost / 40) + area × (base_cost / 40)
OnTarget:  effect_cost × 1.5
```

| Term        | Meaning                                                        |
|-------------|----------------------------------------------------------------|
| min, max    | effect magnitude range (equal for a fixed magnitude)           |
| duration    | effect duration in seconds (stored value; see special cases)   |
| base_cost   | the effect's **current** base cost (right side of `Base Cost`) |
| area        | area of effect in feet (0 for most)                            |
| OnTarget    | ×1.5 multiplier; OnSelf and OnTouch do **not** get it          |

- **Multi-effect spells:** compute each effect separately and **sum**.
- The README cost bracket `[van -> cur]` just prints the stored `data.cost`; the
  generator does not recompute it. A stale stored cost prints verbatim.

### Worked examples (verified against stored cost)

| Spell                  | Effect / values              | Calc                              | Cost |
|------------------------|------------------------------|-----------------------------------|-----:|
| T_Com_Ilu_Paralysis    | Paralyze 3s, base 80         | (1+1)×3×(80/40)                   |   12 |
| T_Com_Alt_WizardLock   | Lock 20, base 24, dur 1      | (20+20)×1×(24/40)                 |   24 |
| T_Com_Mys_DistortedReflect | Reflect 40/30s, base 2.5 | (40+40)×30×(2.5/40)               |  150 |

---

## 2. Special cases in the formula

| Case                     | Rule                                                     |
|--------------------------|----------------------------------------------------------|
| Duration-only (Paralyze, Silence, …) | magnitude fixed at 1, so `(min+max)=2`. Formula uses that 2. |
| Lock / Open              | magnitude-only in game, but the JSON stores `duration=1`, so the standard formula applies with that 1. |
| Neither-axis (Mark, Recall, Interventions, Cure*) | instant; cost is not derived from mag/dur. |
| No-scale (Fire/Frost/Shock Damage, Poison) | mag/dur stay vanilla; base-cost change flows into cost only (no compensation). |

---

## 3. Magnitude rounding rule

| Condition                 | Rule                                               |
|---------------------------|----------------------------------------------------|
| Ranged magnitude (min≠max)| both ends must be **1** or a **multiple of 5**     |
| Fixed magnitude (min=max) | **exempt** — kept as-is                            |
| Duration                  | **exempt** — any integer                           |
| Duration-only effects     | stored magnitude is 1 (legal, never rounded)       |

---

## 4. No-scale effects (no compensation)

These four keep vanilla magnitude/duration (rounding fixes only). A base-cost
change raises/lowers **cost**, never the magnitude.

| Effect      | Base (van -> cur) |
|-------------|-------------------|
| FireDamage  | 5 -> 8            |
| FrostDamage | 5 -> 8            |
| ShockDamage | 7 -> 8            |
| Poison      | 9 -> 8            |

---

## 5. Base-cost spell compensation

When an effect's base cost is multiplied by **X**, spells of that effect move
`magnitude × duration` by about **1/X** (the opposite direction) so the
effective in-game cost stays similar. The split between magnitude and duration
is **chosen per spell** — this rule is discretionary, applied by judgment, not
mechanically. No-scale effects (section 4) are exempt.

| Base change | Example effect(s)              | Spell mag×dur moves |
|-------------|--------------------------------|---------------------|
| ÷10         | Burden, Feather (1.0 -> 0.1)   | ×10 (up)            |
| ÷4          | Reflect, SpellAbsorption (10 -> 2.5); Resists (2.0 -> 0.5) | ×4 (up) |
| ÷2          | Charm (5 -> 2.5)               | ×2 (up)             |
| ×4          | FortifySkill (1.0 -> 4.0)      | ÷4 (down)           |
| ×8          | RestoreAttribute (1.0 -> 8.0)  | ÷8 (down)           |

---

## 6. AUTO_CALCULATE policy

| Spell origin           | AUTO_CALCULATE allowed? | Requirement                        |
|------------------------|:-----------------------:|------------------------------------|
| Vanilla (non-`T_` id)  | yes                     | may show `auto`                    |
| Tamriel Data (`T_` id) | **no**                  | `flags=""`, explicit numeric cost  |

Any `T_` spell shown as `auto` (or `[auto -> …]`) is a rule violation
(`td-spells.md`).

---

## 7. Axis per effect (so nothing is misjudged)

From `scripts/effect_axis_flags.json` / `docs/Effect-Magnitude-Duration-Flags.md`.

| Axis class      | Effects                                                       | In output |
|-----------------|---------------------------------------------------------------|-----------|
| Duration-only   | Paralyze, Silence, Invisibility, WaterBreathing, WaterWalking, all Summon\*, all Bound\* | bare duration (e.g. `5s`) |
| Magnitude-only  | Lock, Open, Dispel                                            | bare magnitude (no `/Ns`) |
| Neither (instant)| Mark, Recall, Divine/Almsivi Intervention, all Cure\*        | `-`       |
| Both (normal)   | everything else (Damage/Drain/Restore/Absorb, Fortify/Resist/Weakness, Shields, Reflect, SpellAbsorption, Sound, Blind, Chameleon, Sanctuary, …) | `mag/durs` |

Never flag a duration-only spell for a "wrong magnitude" or a magnitude-only
spell for a "wrong duration".

---

## 8. What the checker enforces vs what needs judgment

| Rule                              | Automatable? |
|-----------------------------------|:------------:|
| Cost = formula(current base cost) | yes          |
| Magnitude rounding (ranged)       | yes          |
| No-scale magnitude == vanilla     | yes          |
| TD spells not AUTO_CALCULATE      | yes          |
| Compensation direction/factor     | review only (discretionary) |

---

# Part 2 — Findings to review (audit of current data)

Read-only audit results against the rules above. Nothing is applied yet; this is
for review. Confidence: **CONFIRMED** = clear rule break; **REVIEW** =
discretionary / needs a decision.

## (e) AUTO_CALCULATE on a Tamriel Data spell — CONFIRMED

| Spell id            | Effect / values                              | README    | Fix                                  |
|---------------------|----------------------------------------------|-----------|--------------------------------------|
| T_Com_Mys_Insight   | Detect Enchantment 50/10s OnSelf, AUTO_CALC  | [75 -> auto] | flags="" , cost=5 (`(50+50)×10×(0.2/40)`) |

Only TD auto violation in the file. All other `auto` rows are vanilla (allowed).

## (b) Magnitude rounding violations (ranged, not 1 / multiple of 5) — CONFIRMED

| Spell id         | Effect          | Current  | Offending  | Suggested            |
|------------------|-----------------|----------|------------|----------------------|
| shadow form      | Chameleon       | 12-30/30s| min 12     | 10-30 (or 15-30)     |
| hand of odros    | Absorb Agility  | 3-6/120s | min 3, max 6| legal range or fixed 5 |
| T_Com_Trp_Acid   | Poison          | 2-4/5s   | min 2, max 4| no-scale: confirm vanilla first; rule wants 1-5 |

Note: Poison is no-scale, so confirm the vanilla value before touching
`T_Com_Trp_Acid`.

## (a) Cost mismatch vs formula — CONFIRMED

Computed with each effect's current base cost. `stored` = `data.cost` (printed).

### Large gaps (fix first)

| Spell id                   | Current values                                        | Stored | Computed |
|----------------------------|-------------------------------------------------------|-------:|---------:|
| T_Com_Ilu_Voices           | Sound 50/60s OnSelf (base 1.0)                        |     50 |      150 |
| T_Com_Trp_AcidMaster       | DisArmor 150-300/10s + DisWeapon 150-300/5s + Poison 10-20/5s, OnTouch area 1 | 25 | ~165 |
| T_Nor_Res_WinteryMantle    | Resist Frost 80/60s OnSelf (base 0.5)                 |     30 |      120 |
| T_Com_Alt_DalgorsEntwining | Lock 100 OnTouch (base 24, dur 1)                     |     96 |      120 |
| T_Com_Ilu_LivingStatue     | Paralyze 20s OnTouch (base 80)                        |     60 |       80 |

### Moderate gaps (recompute cost)

| Spell id                     | Current values                          | Stored | Computed |  Δ |
|------------------------------|-----------------------------------------|-------:|---------:|---:|
| T_Com_Alt_DreughsGrace       | Swift Swim 120/20s OnTouch (0.5)        |     50 |       60 | +10|
| T_Com_Alt_Fling              | Feather 500/3s OnTarget (0.1)           |    100 |      113 | +13|
| T_Com_Alt_WeightOfGuilt      | Burden 500/3s OnTarget (0.1)            |    100 |      112 | +12|
| T_Com_Des_Duck               | Drain Fatigue 200/2s OnTarget (0.2)     |     40 |       60 | +20|
| T_Com_Des_FractureArmor      | Dis Armor 100/2s OnTouch (0.6)          |     40 |       60 | +20|
| T_Com_Des_Magefire           | Damage Magicka 10-30/2s OnTarget (4.0)  |      6 |       12 |  +6|
| T_Com_Des_RageOfMagnus       | Drain Magicka 60/20s OnTarget (0.4)     |    160 |      180 | +20|
| T_Com_Ilu_AlluringSpeech     | Charm 15-20/20s OnTouch (2.5)           |     40 |       44 |  +4|
| T_Com_Mys_DistortedReflect   | Reflect 40/30s OnSelf (2.5)             |    125 |      150 | +25|
| T_Com_Res_DeftSecurity       | Fortify Security 15/30s OnSelf (4.0)    |     92 |       90 |  -2|
| T_Rea_Des_ShadowRust         | Dis Armor 10-50/20s + Burden 10-150/20s OnTarget | 30 |  39 |  +9|

`T_Com_Res_DeftSecurity` (-2) is within rounding tolerance — low priority.

### Vanilla spells — context-dependent (needs a decision, not mechanical)

| Spell id         | Current values                                | Stored | Computed | Note |
|------------------|-----------------------------------------------|-------:|---------:|------|
| scrib_paralysis  | Paralyze 12s OnTouch (base 80), flags=""      |      6 |       48 | README prints `[auto -> 6]` but flags empty + cost 6. Auto label vs explicit cost disagree. Decide: auto, or cost 48. |
| BM_paralyze_hirc | Paralyze 10s + Burden 500/10s OnTouch         |     50 |       67 | Burden 50→500 raised cost; stored not refreshed. |
| Aryon_rest       | Damage Fatigue 10/10s + Burden 100/10s OnTarget |   38 |     ~22 | Stored higher than formula (Burden base dropped 1.0→0.1); looks stale. |

## (c) No-scale magnitude scaled — NONE FOUND

Fire/Frost/Shock/Poison show only rounding nudges (e.g. god's fire 11-60→10-60,
lightning storm 2-10→1-10). Correct. (shockball max 40→20 is a deliberate nerf,
20 is legal.)

## (d) Compensation direction / factor — REVIEW only (discretionary)

All moved the correct (opposite) direction. Two have a larger-than-implied
factor but read as intentional:

| Effect (base change)        | Observation                                           | Verdict |
|-----------------------------|-------------------------------------------------------|---------|
| Burden/Feather (÷10)        | mag×dur up ~×10 (feather 20/10s→40/50s, buoyancy ×20) | OK      |
| Reflect/SpellAbsorption (÷4)| durations ×4, magnitude held                          | OK      |
| Resists (÷4)                | durations ×4                                          | OK      |
| FortifySkill (×4)           | durations ÷4 (60s→15s)                                | OK      |
| RestoreAttribute (×8)       | durations 30s→1s (÷30, > ×8)                           | review  |
| AbsorbFatigue (×1.5)        | durations 30s→3s/6s (large cut)                       | review  |

## (f) Other / informational

| Item                        | Note                                                   |
|-----------------------------|--------------------------------------------------------|
| masteful* duplicate records | `masteful red wisdom` / `masteful stolid armor` (typo) vs correctly-spelled twins; identical 15/15s. IDs immutable — informational. |
| T_Com_Mys_Insight rename    | renamed to "Detect Enchantment", clashing with vanilla spell name, plus the AUTO_CALC issue in (e). |
| scrib_paralysis auto/cost   | see (a) vanilla table — needs a design decision.       |

## Suggested fix order (confirm each before applying)

1. T_Com_Mys_Insight — remove AUTO_CALCULATE, flags="", cost=5. (hard rule)
2. Rounding: shadow form 12→10/15; hand of odros 3-6 → legal; confirm
   T_Com_Trp_Acid vanilla (no-scale) before touching.
3. Recompute TD costs: Voices→150, AcidMaster→~165, WinteryMantle→120,
   LivingStatue→80, DalgorsEntwining→120, and the moderate list.
4. Decide scrib_paralysis (auto vs cost 48); review BM_paralyze_hirc, Aryon_rest.
5. Review (optional): RestoreAttribute, AbsorbFatigue duration cuts.

# TODO

## Summon Base Costs — Rebalance

| Creature            | Current | Proposed | Rationale                                          |
|---------------------|--------:|---------:|----------------------------------------------------|
| Ancestral Ghost     |       7 |        7 | —                                                  |
| Scamp               |      12 |       12 | —                                                  |
| Bonewalker          |      13 |       13 | —                                                  |
| Skeletal Minion     |      13 |       13 | —                                                  |
| Greater Bonewalker  |      15 |       20 | Permanent stat damage too strong for 15            |
| Clannfear           |      22 |       18 | No spells, no resists — pure melee                 |
| Flame Atronach      |      23 |       23 | —                                                  |
| Bonelord            |      25 |       25 | —                                                  |
| Frost Atronach      |      27 |       27 | —                                                  |
| Dremora             |      28 |       30 | High HP + weapon + shield + loot                   |
| Hunger              |      29 |       35 | Gear destruction + paralyze + quad immunity        |
| Daedroth            |      32 |       35 | Dual AoE + Shield 30 + Regen + 180 HP             |
| Storm Atronach      |      38 |       38 | —                                                  |
| Winged Twilight     |      52 |       42 | No abilities — overpriced vs Storm Atronach        |
| Golden Saint        |      55 |       50 | Slight reduction — still premium for soul farming  |

## README Audit Follow-ups

From `docs/README-Consistency-Audit.md`. Ordered by severity.

### Data rule violations (do first)

Both are magnitude-rounding violations (min ≠ max, value not 1 and not a multiple
of 5). Fix the magnitude range in `R3 - Spells.json`, then regenerate. Proposed
values need approval before applying.

| ID | Record            | Effect                   | Current | Proposed | Action                                       |
|----|-------------------|--------------------------|:-------:|:--------:|----------------------------------------------|
| V1 | `hand of odros`   | Absorb Attribute: Agility |  3-6   |   TBD    | Round to 1 / multiples of 5, regenerate      |
| V2 | `T_Com_Trp_Acid`  | Poison                   |  2-4    |   TBD    | Round to 1 / multiples of 5, regenerate      |

### Layout inconsistency

| ID | Location                                       | Issue                                                       | Action                                              |
|----|------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------|
| D1 | `gen_spells_explained.py` → `Spells-Explained.md` | Intro-prose paragraph violates the no-intro-prose rule   | Delete the six prose `out.append` lines; keep title + first divider |

### Cosmetic / low priority

| ID | Location                              | Issue                                                            | Action                                             |
|----|---------------------------------------|------------------------------------------------------------------|----------------------------------------------------|
| D2 | `gen_core.py` Crime block → `Core.md` | Lone interior blank line inside the Crime fence (no other block has one) | Drop the `out.append("")` separator for uniformity |
| A1 | `gen_spells_explained.py` `explain()` | Compensation judged on first effect only → false `✗` notes on multi-effect spells | Attribute the base-cost change to the matching effect, not `effs[0]` |

### Opportunity

| ID | Location          | Issue                                                     | Action                                                        |
|----|-------------------|-----------------------------------------------------------|---------------------------------------------------------------|
| R1 | `gen_common.py`   | Rounding-violation check is the one universally reusable algorithm | Extract a shared `rounding_violations(effects)` helper for all generators/checkers |

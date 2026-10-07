# Spell Value Rules

The README files (`R3 - *.md`) are **generated from the ESP JSON** by the
scripts in `scripts/` (`gen_readme.py`, `gen_core.py`, ...). Do not hand-edit
them. Edit the JSON, then regenerate.

These rules govern how values are **computed** when editing the JSON. They are
not about README formatting (that is handled by the generators).

## Spell Cost Formula

`((min + max) × duration × (base_cost / 40) + area × (base_cost / 40)) × 1.5 if OnTarget`

- OnSelf/OnTouch: `(min + max) × duration × (base_cost / 40) + area × (base_cost / 40)`
- OnTarget: multiply the above by 1.5

For multi-effect spells, sum the cost of each effect individually.

## Value Rounding Rule

All spell **magnitudes** must be either:
- **1** (minimum floor value), or
- A **multiple of 5** (5, 10, 15, 20, 25, 30, ...)

**Durations are exempt from rounding** — they may be any integer value produced
by scaling.

When scaling produces non-round magnitudes, first apply the scale, then round to
the nearest multiple of 5. If the result is less than 5, use 1 or 5 (never 2, 3,
4, 6, 7, etc. unless it is exactly 1).

**Exception — no range**: When an effect has no magnitude range (min == max), do
**not** round it. Rounding only applies to effects that use a min-max range
(min ≠ max). Fixed-magnitude effects keep their value unchanged.

## No-Scale Effects

The following effects do **not** get spell compensation scaling when their base
cost changes. Only rounding fixes apply:
- **Fire Damage**
- **Frost Damage**
- **Shock Damage**
- **Poison**

For these effects, spells keep their vanilla magnitudes/durations (rounded if
needed). The base cost change affects spell cost directly without compensating
adjustments.

## Scaling

- `new_magnitude = vanilla_magnitude × scale_mag`
- `new_duration = vanilla_duration × scale_dur`
- Apply a scale to the **vanilla default values**, not to a previously scaled value.
- Scale `x1/x1` means revert to vanilla.

## Base Cost and Spell Compensation

When a magic effect's base cost is changed, spells of that school are adjusted in
the **opposite direction** to keep their effective cost roughly the same:
- If base cost is multiplied by X, then spell mag×dur is divided by X (and vice versa).
- Example: base cost ÷2 → spell mag×dur ×2 (double magnitude, or double duration,
  or split between both).
- The split between magnitude and duration is chosen per spell as appropriate.
- Do not apply spell compensation automatically. When a base cost changes, list
  each affected spell with its vanilla values and propose new values for approval.
  Only apply after confirmation.

## Potions

Potion mag/dur values come from the tier table in `potion-tiers.md` — never
scaled from base cost like spells.

## Notes

- Never modify files inside `tes3conv/` — those are read-only vanilla references.
- Never change the `id` of any record in the ESP JSON. IDs are immutable; only
  `name` and other data fields may be edited.
- Never add new records that do not exist in vanilla or TD. Only modify existing records.

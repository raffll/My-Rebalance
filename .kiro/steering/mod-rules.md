# Remastered Rebalance Redux — Mod Rules

Project-specific rules for editing the R3 Morrowind ESP data and regenerating
its documentation.

## 1. Files & Data Sources

Where data comes from and where edits go.

### Read-Only Vanilla References

The JSON files inside the `tes3conv/` folder are **default/vanilla reference
files** and must **never be modified**:

- `tes3conv/Morrowind.json`
- `tes3conv/Tribunal.json`
- `tes3conv/Bloodmoon.json`
- `tes3conv/Tamriel_Data.json`
- `tes3conv/Patch for Purists.json`

They are the source of truth for original game data.

### Edit Targets

All edits must be made to the ESP-derived JSON files in the workspace root or the
`optional/` folder — never to the `tes3conv/` reference files.

### Generated READMEs

The README files (`R3 - *.md`) are **generated from the ESP JSON** by the scripts
in `scripts/` (`gen_spells.py`, `gen_core.py`, ...). Do not hand-edit them. Edit
the JSON, then regenerate.

Generated READMEs do **not** need intro prose. Do not add explanatory
paragraphs, descriptions, or section preambles to a generated README (or to the
generator templates that produce one). The data tables and labelled blocks speak
for themselves; keep the output to headers, labels, and the data.

#### Effect Value Token Format

An effect's value token is rendered in this fixed order:

```
mag/dur/ft/range [cost]
```

- `mag` — magnitude (a single value, or `min-max` range). Always shown when the
  effect uses magnitude.
- `dur` — duration, as `/<n>s`. Always shown when the effect uses duration.
- `ft` — area, as `/<n>ft`.
- `range` — `/Touch`, `/Target`, or `/Self`.
- `[cost]` — spell cost bracket (`[auto]` or a number), appended at the end.

#### Show-Only-If-Changed, But On Both Sides

Whenever a value token is rendered as a pair `A -> B` (vanilla -> current for the
same record, or removed -> added for two paired records), the **range**, **area
(ft)**, and **cost** axes follow this rule:

- Compare the axis between the two sides being paired.
- If the axis is **equal** on both sides, show it on **neither** side.
- If the axis **differs**, show it on **both** sides — including the default or
  zero value (e.g. show `/Self` or `/0ft` on the side that has it, so the pair
  never reads lopsided like `5/30s -> 10/20s/Target`).

Magnitude and duration are always shown on both sides. This keeps paired cells
symmetric: both sides carry the same set of axes.

### Looking Up Vanilla Data

When looking up vanilla spell data, check the `docs/References/` files **first**
before searching the large JSON files:

- `docs/References/Vanilla-Alteration-Spells.md`
- `docs/References/Vanilla-Conjuration-Spells.md`
- `docs/References/Vanilla-Destruction-Spells.md`
- `docs/References/Vanilla-Illusion-Spells.md`
- `docs/References/Vanilla-Mysticism-Spells.md`
- `docs/References/Vanilla-Restoration-Spells.md`
- `docs/References/Vanilla-Potions-Reference.md`
- `docs/References/Vanilla-Scrolls-Reference.md`
- `docs/References/Vanilla-Summon-Reference.md`
- `docs/References/TD-Spells-Analysis.md`
- `docs/References/TD-Potions-Reference.md`

Only fall back to the `tes3conv/` JSON files when the docs don't cover the needed
data.

## 2. Shell & Build

How to produce the ESPs.

Use whatever shell or language is most reliable for the task. There is no
requirement to use a specific shell.

### tes3conv ESP Build

Use the positional form recommended by `tes3conv --help`
(`tes3conv <input> <output>`), with `--overwrite` to skip numbered backups:

```
tes3conv.exe "input.json" "output.esp" --overwrite
```

To build every ESP at once, run `python scripts/build_esps.py`.

### JSON File Encoding

tes3conv requires JSON files without a UTF-8 BOM. Some editors and the `fsWrite`
tool may write a BOM. Ensure any JSON file passed to tes3conv is saved as UTF-8
without a BOM. Tools that write JSON should emit BOM-free UTF-8 directly
(Python's default `open(..., encoding="utf-8")` does this).

## 3. Record Integrity

Rules that apply to every record edit, regardless of type.

- **Never change the `id`** of any record in the ESP JSON. IDs are immutable;
  only `name` and other data fields may be edited.
- **Never add new records** that do not exist in vanilla or TD. Only modify
  existing records.
- **Tamriel Data spells must not use `AUTO_CALCULATE`.** In the `data` block, set
  `"flags": ""` (empty string) instead of `"flags": "AUTO_CALCULATE"`, and set the
  spell cost explicitly as a numeric value in `"cost"`.

## 4. Computing Spell Values

The math for spells. These rules govern how values are **computed** when editing
the JSON (README formatting is handled by the generators).

### Spell Cost Formula

`((min + max) × duration × (base_cost / 40) + area × (base_cost / 40)) × 1.5 if OnTarget`

- OnSelf/OnTouch: `(min + max) × duration × (base_cost / 40) + area × (base_cost / 40)`
- OnTarget: multiply the above by 1.5

For multi-effect spells, sum the cost of each effect individually.

### Scaling

- `new_magnitude = vanilla_magnitude × scale_mag`
- `new_duration = vanilla_duration × scale_dur`
- Apply a scale to the **vanilla default values**, not to a previously scaled value.
- Scale `x1/x1` means revert to vanilla.

### Value Rounding Rule

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

### Base Cost and Spell Compensation

When a magic effect's base cost is changed, spells of that school are adjusted in
the **opposite direction** to keep their effective cost roughly the same:
- If base cost is multiplied by X, then spell mag×dur is divided by X (and vice versa).
- Example: base cost ÷2 → spell mag×dur ×2 (double magnitude, or double duration,
  or split between both).
- The split between magnitude and duration is chosen per spell as appropriate.
- Do not apply spell compensation automatically. When a base cost changes, list
  each affected spell with its vanilla values and propose new values for approval.
  Only apply after confirmation.

#### Magnitude Cap (100)

After compensation, a spell's **magnitude must never exceed 100**. The cap
applies to the compensated magnitude (both `min` and `max`).

- When compensation would push a magnitude above 100, cap it at **100** and push
  the leftover compensation factor into **duration** instead, so the overall
  `mag × dur` target is preserved.
- Example: base cost ÷4 needs `mag × dur ×4`. A vanilla 40-magnitude effect
  scaled ×4 would be 160 (over the cap). Instead cap magnitude at 100 and move
  the remaining factor to duration. Prefer keeping magnitude at a round value
  (per the Value Rounding Rule) and absorbing the remainder in duration.
- For a min-max range, cap each end at 100 independently; if `max` hits the cap,
  put the overflow for both ends into the shared duration.
- The cap is a ceiling only — it never raises a magnitude. Magnitudes already at
  or below 100 after compensation are unchanged.
- Durations have no cap, so they can always absorb the overflow.

### No-Scale Effects

The following effects do **not** get spell compensation scaling when their base
cost changes. Only rounding fixes apply:
- **Fire Damage**
- **Frost Damage**
- **Shock Damage**
- **Poison**

For these effects, spells keep their vanilla magnitudes/durations (rounded if
needed). The base cost change affects spell cost directly without compensating
adjustments.

## 5. Computing Potion Values

Potions use a tier table, **not** the spell math. Potion mag/dur values come from
the tier table below — never scaled from base cost like spells.

Tier name = R3 base spell cost of the effect. Columns are tiers. Vanilla potion
values (5/8s, 8/15s, 10/30s, 15/45s, 20/60s) = tier 1. If R3 base cost is 1,
potions stay vanilla. If R3 base cost differs, potions must be adjusted to the
matching tier. Base cost > 8 uses tier 8.

### Column Selection by Base-Cost Range

Column headers (8, 5, 2, 1, 0.5, 0.2, 0.1) are reference points, **not** the only
allowed base costs. A base cost that falls between two headers snaps to the
nearest column using the **geometric midpoint** of adjacent headers as the
boundary (the scale is multiplicative, so midpoints are geometric, not
arithmetic). Each column owns a half-open range `[low, high)`:

| Column | Base-cost range            | Example effects at this tier        |
|-------:|----------------------------|-------------------------------------|
|      8 | `>= 6.32`                  | (base cost > 8 also uses col 8)     |
|      5 | `3.16 .. < 6.32`           | —                                   |
|      2 | `1.41 .. < 3.16`           | 3.0 Shields/Levitate, 2.5 Reflect   |
|      1 | `0.71 .. < 1.41`           | 1.0 vanilla-tier effects            |
|    0.5 | `0.32 .. < 0.71`           | 0.5 Resists, Swift Swim             |
|    0.2 | `0.14 .. < 0.32`           | 0.25 Fortify Fatigue, 0.2 Light,    |
|        |                            | 0.15 Detect Animal                  |
|    0.1 | `< 0.14`                   | 0.1 Burden/Feather                  |

Boundaries are `sqrt(a*b)` of the two neighbouring header values:
`sqrt(8*5)=6.32`, `sqrt(5*2)=3.16`, `sqrt(2*1)=1.41`, `sqrt(1*0.5)=0.71`,
`sqrt(0.5*0.2)=0.32`, `sqrt(0.2*0.1)=0.14`. A base cost exactly on a header uses
that header's column. Base cost `> 8` always uses col 8.

### Duration-Only Effects

**Duration-only effects** (Paralyze, Silence): These have magnitude 1, so the
effective tier is `base_cost × 1 = base_cost`. For duration-only effects, base
cost 40 is equivalent to base cost 1 in normal spells (tier 1). Use the
**duration column only** from the matching tier. The range boundaries above are
expressed in normal-spell base-cost terms; for a duration-only effect divide its
base cost by 40 first, then apply the ranges.

### Mag/Dur Tier Table

| Mag | Dur |  8  |  5  |  2  |  1  | 0.5 | 0.2 | 0.1 |
|----:|----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|   1 |   3 |  ●  |     |     |     |     |     |     |
|   2 |   6 |  ●  |  ●  |     |     |     |     |     |
|   3 |   9 |  ●  |  ●  |  ●  |     |     |     |     |
|   4 |  12 |  ●  |  ●  |  ●  |     |     |     |     |
|   6 |  18 |  ●  |  ●  |  ●  |  ●  |     |     |     |
|   8 |  24 |     |  ●  |  ●  |  ●  |     |     |     |
|  10 |  30 |     |     |  ●  |  ●  |  ●  |     |     |
|  15 |  45 |     |     |     |  ●  |  ●  |     |     |
|  20 |  60 |     |     |     |  ●  |  ●  |  ●  |     |
|  30 |  90 |     |     |     |     |  ●  |  ●  |     |
|  40 | 120 |     |     |     |     |  ●  |  ●  |     |
|  60 | 180 |     |     |     |     |     |  ●  |  ●  |
|  80 | 240 |     |     |     |     |     |  ●  |  ●  |
| 100 | 300 |     |     |     |     |     |     |  ●  |
| 150 | 450 |     |     |     |     |     |     |  ●  |
| 200 | 600 |     |     |     |     |     |     |  ●  |

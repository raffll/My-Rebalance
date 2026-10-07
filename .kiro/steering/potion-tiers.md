# Potion Tiers — Magnitude/Duration Scale

Tier name = R3 base spell cost of the effect. Columns are tiers.
Vanilla potion values (5/8s, 8/15s, 10/30s, 15/45s, 20/60s) = tier 1. If R3 base cost is 1, potions stay vanilla. If R3 base cost differs, potions must be adjusted to the matching tier.
Base cost > 8 uses tier 8.

## Column selection by base-cost range

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

**Duration-only effects** (Paralyze, Silence): These have magnitude 1, so the effective tier is `base_cost × 1 = base_cost`. For duration-only effects, base cost 40 is equivalent to base cost 1 in normal spells (tier 1). Use the **duration column only** from the matching tier. The range boundaries above are expressed in normal-spell base-cost terms; for a duration-only effect divide its base cost by 40 first, then apply the ranges.

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

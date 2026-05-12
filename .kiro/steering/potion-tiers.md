# Potion Tiers — Magnitude/Duration Scale

Tier name = R3 base spell cost of the effect. Columns are tiers.
Vanilla potion values (5/8s, 8/15s, 10/30s, 15/45s, 20/60s) = tier 1. If R3 base cost is 1, potions stay vanilla. If R3 base cost differs, potions must be adjusted to the matching tier.
Base cost > 8 uses tier 8.

**Duration-only effects** (Paralyze, Silence): These have magnitude 1, so the effective tier is `base_cost × 1 = base_cost`. For tier lookup, treat them the same as a regular effect with that base cost. E.g. Silence at base cost 20 behaves like a regular effect at base cost 20 with magnitude 1 — equivalent to base cost 1 with magnitude 20. Use the **duration column only** from the matching tier.

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

# Scroll Price vs Spell Cost Analysis

> Compares each affected scroll's gold price against the effective spell cost of its enchantment using R3 base costs.
> Formula: OnSelf/OnTouch = `(min + max) × duration × (base_cost / 40) + area × (base_cost / 40)`
> OnTarget = above × 1.5

## R3 Base Costs (Affected Effects)

| Effect | Vanilla Base Cost | R3 Base Cost | Factor |
|--------|------------------:|-------------:|-------:|
| Feather | 1 | 0.1 | ×10 |
| Burden | 1 | 0.1 | ×10 |
| Drain Magicka | 4 | 0.4 | ×10 |
| Drain Fatigue | 2 | 0.2 | ×10 |
| Disintegrate Armor | 6 | 0.6 | ×10 |
| Disintegrate Weapon | 6 | 1.2 | ×5 |
| Detect Animal | 0.75 | 0.15 | ×5 |
| Detect Enchantment | 1 | 0.2 | ×5 |
| Detect Key | 1 | 0.2 | ×5 |

## Other Base Costs (for multi-effect scrolls)

| Effect | R3 Base Cost |
|--------|-------------:|
| Blind | 1 |
| Demoralize Humanoid | 3 |

---

## Single-Effect Scrolls

### Scroll of Ulm Juiceda's Feather

| Field | Value |
|-------|-------|
| ID | sc_ulmjuicedasfeather |
| Gold Price | 114 |
| Vanilla Effect | Feather 50/240s Self |
| Compensated Effect | Feather 500/240s Self |
| Spell Cost (R3, vanilla) | (50+50) × 240 × (0.1/40) = **60** |
| Spell Cost (R3, compensated) | (500+500) × 240 × (0.1/40) = **600** |
| Price / Vanilla Cost | 114 / 60 = **1.9×** |
| Price / Compensated Cost | 114 / 600 = **0.19×** |
| Flag (>50% deviation) | **YES** — price is 81% below spell cost |

### Scroll of Fader's Leaden Flesh

| Field | Value |
|-------|-------|
| ID | sc_fadersleadenflesh |
| Gold Price | 129 |
| Vanilla Effect | Burden 0-50/30s Target |
| Compensated Effect | Burden 0-250/60s Target |
| Spell Cost (R3, vanilla) | (0+50) × 30 × (0.1/40) × 1.5 = **5.63** |
| Spell Cost (R3, compensated) | (0+250) × 60 × (0.1/40) × 1.5 = **56.25** |
| Price / Vanilla Cost | 129 / 5.63 = **22.9×** |
| Price / Compensated Cost | 129 / 56.25 = **2.29×** |
| Flag (>50% deviation) | **YES** — price is 129% above spell cost |

### Scroll of Reynos' Beast Finder

| Field | Value |
|-------|-------|
| ID | sc_reynosbeastfinder |
| Gold Price | 112 |
| Vanilla Effect | Detect Animal 40-80/10s Self |
| Compensated Effect | Detect Animal 100-200/20s Self |
| Spell Cost (R3, vanilla) | (40+80) × 10 × (0.15/40) = **4.5** |
| Spell Cost (R3, compensated) | (100+200) × 20 × (0.15/40) = **22.5** |
| Price / Vanilla Cost | 112 / 4.5 = **24.9×** |
| Price / Compensated Cost | 112 / 22.5 = **4.98×** |
| Flag (>50% deviation) | **YES** — price is 398% above spell cost |

### Scroll of The Mage's Eye

| Field | Value |
|-------|-------|
| ID | sc_mageseye |
| Gold Price | 112 |
| Vanilla Effect | Detect Enchantment 40-80/10s Self |
| Compensated Effect | Detect Enchantment 200-400/10s Self |
| Spell Cost (R3, vanilla) | (40+80) × 10 × (0.2/40) = **6** |
| Spell Cost (R3, compensated) | (200+400) × 10 × (0.2/40) = **30** |
| Price / Vanilla Cost | 112 / 6 = **18.7×** |
| Price / Compensated Cost | 112 / 30 = **3.73×** |
| Flag (>50% deviation) | **YES** — price is 273% above spell cost |

### Scroll of Tevral's Hawkshaw

| Field | Value |
|-------|-------|
| ID | sc_tevralshawkshaw |
| Gold Price | 112 |
| Vanilla Effect | Detect Key 40-80/30s Self |
| Compensated Effect | Detect Key 100-200/60s Self |
| Spell Cost (R3, vanilla) | (40+80) × 30 × (0.2/40) = **18** |
| Spell Cost (R3, compensated) | (100+200) × 60 × (0.2/40) = **90** |
| Price / Vanilla Cost | 112 / 18 = **6.2×** |
| Price / Compensated Cost | 112 / 90 = **1.24×** |
| Flag (>50% deviation) | **NO** — within 24% |

---

## Multi-Effect Scroll

### Scroll of Baleful Suffering

| Field | Value |
|-------|-------|
| ID | sc_balefulsuffering |
| Gold Price | 223 |
| Vanilla Effects | Blind 0-25/30s + Burden 0-25/30s + Demoralize 0-50/30s + DisArmor 5/5s + DisWeapon 5/5s/10ft — all Target |
| Compensated Effects | Blind 0-25/30s + Burden 0-250/30s + Demoralize 0-50/30s + DisArmor 50/5s + DisWeapon 25/5s/10ft — all Target |

**Per-effect spell cost breakdown (R3 base costs, vanilla magnitudes):**

| Effect | Calculation | Cost |
|--------|-------------|-----:|
| Blind 0-25/30s Target | (0+25) × 30 × (1/40) × 1.5 | 28.13 |
| Burden 0-25/30s Target | (0+25) × 30 × (0.1/40) × 1.5 | 2.81 |
| Demoralize 0-50/30s Target | (0+50) × 30 × (3/40) × 1.5 | 168.75 |
| DisArmor 5/5s Target | (5+5) × 5 × (0.6/40) × 1.5 | 1.13 |
| DisWeapon 5/5s/10ft Target | ((5+5) × 5 × (1.2/40) + 10 × (1.2/40)) × 1.5 | 2.70 |
| **Total (vanilla)** | | **203.51** |

**Per-effect spell cost breakdown (R3 base costs, compensated magnitudes):**

| Effect | Scale | Calculation | Cost |
|--------|-------|-------------|-----:|
| Blind 0-25/30s Target | unchanged | (0+25) × 30 × (1/40) × 1.5 | 28.13 |
| Burden 0-250/30s Target | ×10 | (0+250) × 30 × (0.1/40) × 1.5 | 28.13 |
| Demoralize 0-50/30s Target | unchanged | (0+50) × 30 × (3/40) × 1.5 | 168.75 |
| DisArmor 50/5s Target | ×10 | (50+50) × 5 × (0.6/40) × 1.5 | 11.25 |
| DisWeapon 25/5s/10ft Target | ×5 | ((25+25) × 5 × (1.2/40) + 10 × (1.2/40)) × 1.5 | 11.70 |
| **Total (compensated)** | | | **247.95** |

| Metric | Vanilla | Compensated |
|--------|---------|-------------|
| Total Spell Cost | 203.51 | 247.95 |
| Price / Cost | 223 / 203.51 = **1.10×** | 223 / 247.95 = **0.90×** |
| Flag (>50% deviation) | **NO** — within 10% | **NO** — within 10% |

**Note:** The Demoralize effect dominates the cost (68% of compensated total). The scaled effects (Burden, DisArmor, DisWeapon) increased from 3.3% to 20.6% of total cost after compensation, but Demoralize still keeps the overall ratio well within bounds.

---

## Summary Table

| Scroll | Price | Vanilla Cost | Vanilla Ratio | Compensated Cost | Comp. Ratio | Flagged |
|--------|------:|-------------:|--------------:|-----------------:|------------:|---------|
| Ulm Juiceda's Feather | 114 | 60.00 | 1.9× | 600.00 | 0.19× | YES |
| Fader's Leaden Flesh | 129 | 5.63 | 22.9× | 56.25 | 2.29× | YES |
| Reynos' Beast Finder | 112 | 4.50 | 24.9× | 22.50 | 4.98× | YES |
| The Mage's Eye | 112 | 6.00 | 18.7× | 30.00 | 3.73× | YES |
| Tevral's Hawkshaw | 112 | 18.00 | 6.2× | 90.00 | 1.24× | NO |
| Baleful Suffering | 223 | 203.51 | 1.10× | 247.95 | 0.90× | NO |

### Observations

1. **Compensation scaling dramatically improved ratios** for all single-effect scrolls. Vanilla ratios of 6×–25× dropped to 0.19×–5× after scaling.
2. **Tevral's Hawkshaw is now within range** — the ×5 compensation on Detect Key brought the ratio from 6.2× down to 1.24×, clearing the 50% deviation flag.
3. **Ulm Juiceda's Feather flipped direction** — the ×10 compensation made the spell cost (600) far exceed the gold price (114). The scroll is now "underpriced" relative to its enchantment power.
4. **Fader's Leaden Flesh, Reynos' Beast Finder, and The Mage's Eye remain flagged** — compensation helped significantly but prices still exceed spell cost by >50%.
5. **Baleful Suffering remains fine** — the Demoralize effect (unchanged base cost 3) still dominates the enchantment cost. After compensation, the total cost actually exceeds the price slightly (ratio 0.90×), but well within the 50% threshold.
6. **Price changes are out of scope** per Requirement 7.5 — the system does not modify gold values directly. This analysis is informational for the mod author.

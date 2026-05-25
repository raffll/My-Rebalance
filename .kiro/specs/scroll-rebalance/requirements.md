# Requirements Document

## Introduction

Scrolls in Morrowind use the same magic effects as spells but are one-use items with fixed enchantment values. The Remastered Rebalance Redux mod has already adjusted base costs and spell magnitudes/durations for many effects, but scrolls have not been systematically updated to match. This feature covers the analysis and readjustment of scrolls that use effects with a ×10 base cost reduction — the most dramatically changed effects — to align with the new spell balance. It also includes a price-vs-cost comparison to evaluate whether scroll gold values are appropriate relative to the enchantment's effective spell cost.

## Glossary

- **Scroll**: A one-use enchanted item in Morrowind that casts a fixed spell effect when used. Scrolls use "Cast Once" enchantment type.
- **Enchantment_Record**: The underlying enchantment data record attached to a scroll, containing effect type, magnitude, duration, area, and range.
- **Base_Cost**: The per-point cost of a magic effect, used in the spell cost formula. Changes to base cost affect how expensive an effect is to cast.
- **Compensation_Scale**: The magnitude/duration multiplier applied to spells when a base cost changes, to keep effective spell cost roughly constant (inverse of base cost change).
- **No_Scale_Effect**: An effect (Fire Damage, Frost Damage, Shock Damage, Poison) that does not receive compensation scaling when its base cost changes — only rounding fixes apply.
- **Rounding_Rule**: All spell magnitudes must be either 1 (minimum floor) or a multiple of 5. Value 2 rounds to 1; values 3-4 round to 5; values above 5 round to nearest multiple of 5.
- **Scroll_Rebalance_System**: The process and tooling for identifying and adjusting scroll enchantment values to match the mod's new spell balance.
- **Spell_Cost**: The magicka cost to cast an equivalent spell, calculated using the spell cost formula: `((min + max) × duration × (base_cost / 40) + area × (base_cost / 40)) × 1.5 if OnTarget`.
- **Scroll_Price**: The gold value assigned to a scroll's item record in the game data.
- **High_Scale_Effect**: A magic effect whose base cost was reduced by a factor of 5 or more, requiring ×5 or ×10 compensation scaling on magnitudes/durations. These are split into two tiers:
  - **×10 effects**: Burden (1→0.1), Feather (1→0.1), Drain Magicka (4→0.4), Drain Fatigue (2→0.2), Disintegrate Armor (6→0.6)
  - **×5 effects**: Disintegrate Weapon (6→1.2), Detect Animal (0.75→0.15), Detect Enchantment (1→0.2), Detect Key (1→0.2)

## Requirements

### Requirement 1: Identify Scrolls Using High_Scale_Effects

**User Story:** As a mod author, I want to identify which scrolls use effects whose base costs were reduced by ×5 or ×10, so that I can focus rebalancing on the most dramatically changed effects.

#### Acceptance Criteria

1. THE Scroll_Rebalance_System SHALL identify all scrolls from Morrowind.esm, Tribunal.esm, and Bloodmoon.esm that use at least one High_Scale_Effect, where High_Scale_Effects and their compensation factors are: Burden (×10), Feather (×10), Drain Magicka (×10), Drain Fatigue (×10), Disintegrate Armor (×10), Disintegrate Weapon (×5), Detect Animal (×5), Detect Enchantment (×5), Detect Key (×5).
2. THE Scroll_Rebalance_System SHALL list each affected scroll showing: scroll name, scroll ID, and for each High_Scale_Effect on that scroll the effect name, vanilla magnitude range, vanilla duration, and the compensation factor (×5 or ×10).
3. WHEN a scroll uses multiple effects and only some are High_Scale_Effects, THE Scroll_Rebalance_System SHALL mark only the High_Scale_Effect entries for compensation scaling and leave non-High_Scale_Effect entries unmodified in the output.
4. THE Scroll_Rebalance_System SHALL exclude scrolls that do not use any High_Scale_Effect from the compensation scope.
5. WHEN a single scroll uses more than one High_Scale_Effect with different compensation factors, THE Scroll_Rebalance_System SHALL list each High_Scale_Effect separately with its own compensation factor.

### Requirement 2: Identify Non-Round Magnitudes on Affected Scrolls

**User Story:** As a mod author, I want to identify which of the affected scrolls have magnitudes that violate the rounding rule, so that rounding can be applied alongside compensation.

#### Acceptance Criteria

1. WHEN an affected scroll's enchantment effect has a min_magnitude or max_magnitude that is not 1 and not a multiple of 5, THE Scroll_Rebalance_System SHALL flag that magnitude value as requiring rounding correction.
2. WHEN a scroll has multiple enchantment effects, THE Scroll_Rebalance_System SHALL evaluate each effect's min_magnitude and max_magnitude independently against the rounding rule.
3. THE Scroll_Rebalance_System SHALL report, for each flagged magnitude value, the scroll name, effect name, whether the value is min or max magnitude, the current non-round value, and the proposed rounded value.
4. WHEN a magnitude value is 2, THE Scroll_Rebalance_System SHALL propose rounding to 1 (nearest valid value). WHEN a magnitude value is 3 or 4, THE Scroll_Rebalance_System SHALL propose rounding to 5.
5. WHEN a magnitude value is above 5 and not a multiple of 5, THE Scroll_Rebalance_System SHALL propose rounding to the nearest multiple of 5, using standard rounding (values ending in 3, 4, 8, 9 round up; values ending in 1, 2, 6, 7 round down).

### Requirement 3: Compare Scroll Price vs Spell Cost

**User Story:** As a mod author, I want to compare each affected scroll's gold price against the effective spell cost of its enchantment (using the new base costs), so that I can evaluate whether scroll prices are appropriate.

#### Acceptance Criteria

1. THE Scroll_Rebalance_System SHALL identify affected scrolls as those whose enchantment contains at least one magic effect with a changed R3 base cost.
2. THE Scroll_Rebalance_System SHALL calculate the effective spell cost of each affected scroll's enchantment by applying the spell cost formula to each effect individually (using the R3 base costs, the effect's magnitude, duration, area, and a 1.5× multiplier for Target range type) and summing the results.
3. THE Scroll_Rebalance_System SHALL calculate the effective spell cost using both the vanilla magnitudes/durations and the proposed new magnitudes/durations (after compensation).
4. THE Scroll_Rebalance_System SHALL present, for each affected scroll, the scroll name, its current gold price, the effective spell cost under vanilla magnitudes, and the effective spell cost under proposed magnitudes.
5. WHEN a scroll's gold price differs from its effective spell cost (under proposed magnitudes) by more than 50%, THE Scroll_Rebalance_System SHALL flag that scroll for price review.

### Requirement 4: Apply Compensation Scaling (×5 or ×10)

**User Story:** As a mod author, I want scroll magnitudes and durations for High_Scale_Effects multiplied by their respective factor (×5 or ×10), so that scrolls remain balanced relative to the new spell costs.

#### Acceptance Criteria

1. WHEN a scroll uses a ×10 effect (Burden, Feather, Drain Magicka, Drain Fatigue, Disintegrate Armor), THE Scroll_Rebalance_System SHALL multiply the effect's magnitude×duration product by 10, applying the factor independently to both min_magnitude and max_magnitude when the effect uses a range.
2. WHEN a scroll uses a ×5 effect (Disintegrate Weapon, Detect Animal, Detect Enchantment, Detect Key), THE Scroll_Rebalance_System SHALL multiply the effect's magnitude×duration product by 5, applying the factor independently to both min_magnitude and max_magnitude when the effect uses a range.
3. THE Scroll_Rebalance_System SHALL apply the Rounding_Rule to all resulting magnitudes after scaling, where the Rounding_Rule requires each magnitude to be either 1 or a multiple of 5.
4. WHEN a scroll has non-High_Scale_Effects alongside High_Scale_Effects, THE Scroll_Rebalance_System SHALL leave the non-High_Scale_Effects unchanged unless they independently require rounding to satisfy the Rounding_Rule.
5. THE Scroll_Rebalance_System SHALL propose a magnitude/duration split for each scaled effect such that magnitude×duration equals the scaled product, magnitude satisfies the Rounding_Rule, and both magnitude and duration are positive integers, and present it for user approval before applying.
6. WHEN the user rejects a proposed split, THE Scroll_Rebalance_System SHALL accept an alternative magnitude/duration split provided by the user, provided the alternative preserves the scaled product (magnitude×duration equals the required value) and the magnitude satisfies the Rounding_Rule.
7. IF the user provides an alternative split where magnitude×duration does not equal the scaled product or magnitude violates the Rounding_Rule, THEN THE Scroll_Rebalance_System SHALL reject the split and display an error message indicating which constraint was violated.

### Requirement 5: Update README and JSON Records

**User Story:** As a mod author, I want the approved scroll changes written to both the README documentation and the ESP JSON file, so that the mod files stay synchronized.

#### Acceptance Criteria

1. WHEN scroll changes are approved, THE Scroll_Rebalance_System SHALL add entries to the matching magic-effect section in README - Enchantments.md using the column-aligned format: scroll name at column 0, magnitude/duration values at column 44, and the `id:` comment at column 76.
2. WHEN scroll changes are approved, THE Scroll_Rebalance_System SHALL update or create the corresponding enchantment record in R3 - Enchantments.json with the new `min_magnitude`, `max_magnitude`, `duration`, and `area` values for each effect in the scroll's enchantment.
3. THE Scroll_Rebalance_System SHALL include the scroll's enchantment ID (the `_en` suffixed record ID) in the README entry using the `id:` prefix in the comment column.
4. IF a scroll's enchantment record does not yet exist in R3 - Enchantments.json, THEN THE Scroll_Rebalance_System SHALL copy the full record from the appropriate vanilla reference JSON (Morrowind.json, Tribunal.json, or Bloodmoon.json) in the tes3conv folder before applying changes.
5. THE Scroll_Rebalance_System SHALL not modify any scroll's item record ID or enchantment record ID.
6. IF a scroll's enchantment contains multiple effects, THEN THE Scroll_Rebalance_System SHALL update all effects within the single enchantment record and list the primary changed effect's values in the README entry.

### Requirement 6: Handle Multi-Effect Scrolls Coherently

**User Story:** As a mod author, I want multi-effect scrolls handled as a coherent unit, so that the scroll's overall power level and theme remain consistent after rebalancing.

#### Acceptance Criteria

1. WHEN a scroll has 2 or more effects, THE Scroll_Rebalance_System SHALL present all effects in a single grouped README entry block showing each effect's vanilla and rebalanced magnitude/duration on consecutive lines under the same scroll name.
2. WHEN a scroll combines effects whose base cost change produces ×5 or ×10 magnitude/duration scaling with effects that remain at ×1 or ×2 scaling, THE Scroll_Rebalance_System SHALL annotate each effect line with its applied scale factor (e.g. "×10" or "unchanged") so that the reviewer can identify which effects were scaled and by how much.
3. THE Scroll_Rebalance_System SHALL display the total enchantment cost for the full multi-effect scroll, calculated as the sum of each effect's individual cost using the spell cost formula, showing both the vanilla total and the rebalanced total side by side.
4. IF a multi-effect scroll contains effects governed by different scale factors, THEN THE Scroll_Rebalance_System SHALL preserve each effect's independent scale without averaging or normalizing across effects, and shall flag the scroll for manual review when the ratio between the highest and lowest applied scale factors exceeds 5.

### Requirement 7: Preserve Scroll Identity and Availability

**User Story:** As a mod author, I want scrolls to keep their original names, IDs, and placement in the game world, so that only their power levels change.

#### Acceptance Criteria

1. THE Scroll_Rebalance_System SHALL not rename any scroll or change its item ID.
2. THE Scroll_Rebalance_System SHALL not change any scroll's enchantment ID.
3. THE Scroll_Rebalance_System SHALL not modify scroll weight, cell placement, leveled list membership, or merchant inventory.
4. THE Scroll_Rebalance_System SHALL only modify the enchantment effect magnitudes and durations attached to scrolls, preserving the original effect list composition, area, and range type of each enchantment.
5. THE Scroll_Rebalance_System SHALL not modify the scroll's gold value field directly; any value change that results from the engine recalculating enchantment cost is acceptable.

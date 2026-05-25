# Implementation Plan: Scroll Rebalance

## Overview

This plan implements the scroll rebalance workflow for scrolls using High_Scale_Effects (×5 and ×10 compensation factors). The workflow processes each unprocessed scroll by calculating the scaled magnitude×duration product, proposing a magnitude/duration split for user approval, applying rounding rules, computing spell costs for price comparison, and writing approved changes to `README - Enchantments.md` and `R3 - Enchantments.json`. Finally, the ESP is rebuilt with tes3conv.

Already processed: Scroll of Fader's Leaden Flesh (Burden ×10: 0-50/30s → 0-250/60s).

Remaining scrolls:
- Scroll of Ulm Juiceda's Feather (Feather ×10)
- Scroll of Reynos' Beast Finder (Detect Animal ×5)
- Scroll of The Mage's Eye (Detect Enchantment ×5)
- Scroll of Tevral's Hawkshaw (Detect Key ×5)
- Scroll of Baleful Suffering — DisArmor (×10) and DisWeapon (×5) effects still at vanilla values

## Tasks

- [x] 1. Process Scroll of Ulm Juiceda's Feather (Feather ×10)
  - [x] 1.1 Calculate compensation scaling for Feather effect
    - Vanilla: Feather 50/240s Self, factor ×10
    - Compute target product: 50 × 240 × 10 = 120,000
    - Propose magnitude/duration split where mag×dur = 120,000, mag is multiple of 5
    - Calculate spell cost using formula: `(min + max) × duration × (base_cost / 40)` with new base cost 0.1
    - Present proposal to user with vanilla vs proposed spell cost comparison
    - Scroll gold price: 114 — flag if >50% deviation from proposed spell cost
    - _Requirements: 1.1, 1.2, 2.1, 3.2, 3.4, 3.5, 4.1, 4.3, 4.5_

  - [x] 1.2 Write approved Feather scroll changes to README and JSON
    - Add/update entry in `## Feather` section of `README - Enchantments.md` with column-aligned format (name col 0, values col 44, id col 76)
    - Copy enchantment record from `tes3conv/Morrowind.json` if not already in `R3 - Enchantments.json`, then update `min_magnitude`, `max_magnitude`, `duration`
    - Enchantment ID: `sc_ulmjuicedasfeather_en` (verify against vanilla JSON)
    - Strip BOM from JSON after write
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 7.1, 7.2, 7.4_

- [x] 2. Process Detect-family scrolls (×5 compensation)
  - [x] 2.1 Calculate compensation scaling for Scroll of Reynos' Beast Finder
    - Vanilla: Detect Animal 40-80/10s, factor ×5
    - Compute target products: min = 40 × 10 × 5 = 2,000; max = 80 × 10 × 5 = 4,000
    - Propose magnitude/duration split for both min and max, magnitudes must be multiples of 5
    - Calculate spell cost with new base cost 0.15
    - Present proposal to user; scroll gold price: 112
    - _Requirements: 1.1, 1.2, 2.1, 3.2, 3.4, 3.5, 4.2, 4.3, 4.5_

  - [x] 2.2 Calculate compensation scaling for Scroll of The Mage's Eye
    - Vanilla: Detect Enchantment 40-80/10s, factor ×5
    - Compute target products: min = 40 × 10 × 5 = 2,000; max = 80 × 10 × 5 = 4,000
    - Propose magnitude/duration split, magnitudes must be multiples of 5
    - Calculate spell cost with new base cost 0.2
    - Present proposal to user; scroll gold price: 112
    - _Requirements: 1.1, 1.2, 2.1, 3.2, 3.4, 3.5, 4.2, 4.3, 4.5_

  - [x] 2.3 Calculate compensation scaling for Scroll of Tevral's Hawkshaw
    - Vanilla: Detect Key 40-80/30s, factor ×5
    - Compute target products: min = 40 × 30 × 5 = 6,000; max = 80 × 30 × 5 = 12,000
    - Propose magnitude/duration split, magnitudes must be multiples of 5
    - Calculate spell cost with new base cost 0.2
    - Present proposal to user; scroll gold price: 112
    - _Requirements: 1.1, 1.2, 2.1, 3.2, 3.4, 3.5, 4.2, 4.3, 4.5_

  - [x] 2.4 Write approved Detect-family scroll changes to README and JSON
    - Add entries to appropriate sections in `README - Enchantments.md` (create `## Detect Animal`, `## Detect Enchantment`, `## Detect Key` sections if they don't exist)
    - Copy enchantment records from `tes3conv/Morrowind.json` if not in `R3 - Enchantments.json`
    - Update `min_magnitude`, `max_magnitude`, `duration` for each scroll's enchantment
    - Enchantment IDs to verify: `sc_reynosbeastfinder_en`, `sc_mageseye_en`, `sc_tevralshawkshaw_en`
    - Strip BOM from JSON after write
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 7.1, 7.2, 7.4_

- [x] 3. Process Scroll of Baleful Suffering (multi-effect: ×10 + ×5)
  - [x] 3.1 Calculate compensation scaling for DisArmor and DisWeapon effects
    - Scroll has 6 effects total; only DisArmor and DisWeapon need scaling (Blind, Burden, Demoralize unchanged)
    - DisArmor: vanilla 5/5s, factor ×10 → target product = 5 × 5 × 10 = 250
    - DisWeapon: vanilla 5/5s, factor ×5 → target product = 5 × 5 × 5 = 125
    - Propose magnitude/duration splits for both, magnitudes must be 1 or multiple of 5
    - Note: Burden effect (0-25/30s) already has an entry in README but is listed at vanilla values — confirm whether it needs scaling too
    - Calculate total enchantment cost (sum of all 6 effects) for vanilla vs proposed, using respective new base costs
    - Present grouped proposal showing all effects with their scale factors (×10, ×10, ×5, unchanged, unchanged, unchanged)
    - Flag for manual review: ratio between highest (×10) and lowest (×5) applied factors = 2, which is ≤5 so no flag needed
    - Scroll gold price: 223
    - _Requirements: 1.1, 1.2, 1.5, 2.1, 3.2, 3.4, 3.5, 4.1, 4.2, 4.3, 4.5, 6.1, 6.2, 6.3, 6.4_

  - [x] 3.2 Write approved Baleful Suffering changes to README and JSON
    - Update existing entry in `## Burden` section or add multi-effect block per Requirement 6.1
    - Add entries to `## Disintegrate Armor` and create `## Disintegrate Weapon` section if needed
    - Update the existing enchantment record in `R3 - Enchantments.json` (record already exists for Burden effect)
    - Update `min_magnitude`, `max_magnitude`, `duration` for DisArmor and DisWeapon effects within the same enchantment record
    - Preserve all 6 effects in order; only modify the scaled effects
    - Strip BOM from JSON after write
    - _Requirements: 5.1, 5.2, 5.5, 5.6, 6.1, 6.2, 7.1, 7.2, 7.4_

- [x] 4. Price vs Spell Cost comparison
  - Reference document created at `docs/Scroll-Price-vs-Cost.md`
  - All single-effect High_Scale scrolls are flagged (price >> spell cost at R3 base costs)
  - Baleful Suffering is NOT flagged (Demoralize dominates cost, ratio 1.1×)
  - After compensation scaling is applied, recompute spell costs with new mag/dur values and update the reference document
  - Price changes are out of scope (Req 7.5) — this is informational only
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 5. Checkpoint — Verify all scroll changes
  - Ensure all README entries use correct column alignment (name col 0, values col 44, id col 76)
  - Ensure all JSON records have correct `min_magnitude`, `max_magnitude`, `duration` values matching approved proposals
  - Ensure enchantment record IDs are unchanged
  - Ensure effect lists preserve original order, area, range, skill, and attribute fields
  - Ensure all entries have `id:` tags in README
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Build ESP and final validation
  - [x] 6.1 Build R3 - Enchantments.esp with tes3conv
    - Run: `./tes3conv/tes3conv.exe "R3 - Enchantments.json" -o "R3 - Enchantments.esp"`
    - Verify tes3conv exits without errors
    - _Requirements: 5.2, 7.1_

- [x] 7. Final checkpoint — Confirm ESP build and documentation sync
  - Verify ESP file was created/updated successfully
  - Confirm README entries and JSON records contain matching values for all processed scrolls
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks follow the spell-edit-workflow steering rules: README and JSON are always updated together
- JSON files require BOM stripping after write (PowerShell: `[System.IO.File]::WriteAllText` with `UTF8Encoding $false`)
- tes3conv reference files in `tes3conv/` are read-only — never modify them
- Scroll of Fader's Leaden Flesh is already processed (0-250/60s) and will not be re-proposed
- The Baleful Suffering scroll's Burden effect (0-25/30s) appears in README at vanilla values — task 3.1 must confirm whether it needs ×10 scaling (target: 0-250/30s or alternative split) or was intentionally left unchanged
- Column alignment: name at col 0, values at col 44, comments/id at col 76
- Rounding rule: magnitudes must be 1 or multiple of 5; durations are exempt from rounding
- Each proposal requires user approval before writing to files (per Requirement 4.5)
- Multi-effect scrolls are presented as grouped blocks showing all effects (per Requirement 6.1)

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1", "2.1", "2.2", "2.3", "3.1"] },
    { "id": 1, "tasks": ["1.2", "2.4", "3.2", "4"] },
    { "id": 2, "tasks": ["6.1"] }
  ]
}
```

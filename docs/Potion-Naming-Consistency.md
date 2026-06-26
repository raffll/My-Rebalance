# Potion Naming Consistency Analysis

31-character limit. Grouped by effect, showing all vanilla + TD potions.

## Naming Patterns Found

Vanilla uses **three** different patterns inconsistently:

| Pattern | Example | Used By |
|---------|---------|---------|
| `[Tier] Potion of [Effect]` | Bargain Potion of Burden | Burden, Feather, Fire Shield, Frost Shield, Jump, Swift Swim, Light, Night-Eye, Paralyze, Silence, Shadow, Invisibility, Reflection |
| `[Tier] [Effect]` | Bargain Lightning Shield | Lightning Shield, Spell Absorption, Disease/Fire/Frost/Shock/Poison/Magicka Resistance |
| `[Tier] [Verb] [Stat]` | Bargain Restore Health | Restore Health/Magicka/Fatigue/Attribute, Fortify Fatigue/Attribute |
| Mixed | Bargain Fortify Health Potion / Cheap Potion of Fortify Health | Fortify Health (inconsistent within same set!) |

TD adds:
- `Potion of Evasion` (Sanctuary)
- `Potion of Protection` (Shield)
- `Potion of Cacophony` (Sound)
- `Potion of Blindness` (Blind)
- `Fortify Casting` (Fortify Magicka — different name!)
- `Potion of Fortify Luck` (Insight ID but standard name)
- `Rising Force Potion` / `Potion of Levitation` (TD Cheap uses different name than vanilla!)

## Inconsistencies by Effect

### Levitate
```
Bargain Rising Force Potion          (27) ✓
Cheap Rising Force Potion            (25) ✓
Standard Rising Force Potion         (28) ✓
Quality Rising Force Potion          (27) ✓
Exclusive Rising Force Potion        (29) ✓
Cheap Potion of Levitation           (24) TD — DIFFERENT PATTERN
```
**Issue**: TD uses "Potion of Levitation" while vanilla uses "Rising Force Potion".

### Lightning Shield
```
Bargain Lightning Shield             (24) 
Cheap Lightning Shield               (22) 
Standard Lightning Shield            (25) 
Quality Lightning Shield             (22) 
Exclusive Lightning Shield           (24) 
```
**Issue**: Missing "Potion of" — inconsistent with Fire Shield and Frost Shield which use "Potion of Fire Shield" etc.

### Frost Shield
```
Bargain Potion of Frost Shield       (30) 
Cheap Potion of Frost Shield         (28) 
Standard Potion of Frost Shield      (31) 
Quality Frost Shield                 (20) ← MISSING "Potion of"
Exclusive Frost Shield               (22) ← MISSING "Potion of"
```
**Issue**: Quality and Exclusive drop "Potion of" — inconsistent with Bargain/Cheap/Standard of same set.

### Spell Absorption
```
Bargain Spell Absorption             (24) 
Cheap Spell Absorption               (22) 
Standard Spell Absorption            (25) 
Quality Spell Absorption             (22) 
Exclusive Spell Absorption           (24) 
```
**Issue**: No "Potion of" — inconsistent with Reflection which uses "Potion of Reflection".

### Fortify Health
```
Bargain Fortify Health Potion        (29) ← "Potion" at END
Cheap Potion of Fortify Health       (28) ← "Potion of" at START
Standard Fortify Health Potion       (30) ← "Potion" at END
Quality Fortify Health               (22) ← NO "Potion" at all
Exclusive Fortify Health             (22) ← NO "Potion" at all
Cheap Potion of Fortify Health       (28) TD — matches vanilla Cheap
```
**Issue**: Three different patterns within the same effect!

### Fortify Magicka
```
Bargain Fortify Magicka              (23) ← no Potion
Cheap Potion of Fortify Magicka      (29) ← "Potion of"
Standard Fortify Magicka Potion      (31) ← "Potion" at END
Quality Fortify Magicka              (21) ← no Potion
Exclusive Fortify Magicka            (23) ← no Potion
Cheap Potion of Fortify Magicka      (29) TD — matches vanilla Cheap
Bargain Fortify Casting              (23) TD — DIFFERENT EFFECT NAME
Cheap Fortify Casting                (21) TD — DIFFERENT EFFECT NAME
```
**Issue**: Three patterns + TD uses "Casting" instead of "Magicka".

### Fortify Fatigue
```
Bargain Fortify Fatigue              (23) ✓
Cheap Fortify Fatigue                (21) ✓
Standard Fortify Fatigue Potion      (31) ← adds "Potion"
Quality Fortify Fatigue              (21) ✓
Exclusive Fortify Fatigue            (23) ✓
Cheap Fortify Fatigue                (21) TD ✓
```
**Issue**: Standard adds "Potion" — inconsistent with rest of set.

### Fortify Attribute
```
Bargain Fortify [Attribute]          (varies)
Cheap Fortify [Attribute]            (varies)
```
Consistent within set, but inconsistent with Fortify Health/Magicka which sometimes add "Potion of".

### Fortify Luck (TD)
```
Bargain Potion of Fortify Luck       (28) TD — "Potion of"
Cheap Potion of Fortify Luck         (26) TD — "Potion of"
```
**Issue**: Uses "Potion of" while other TD Fortify Attributes use bare "[Tier] Fortify [Attr]".

### Restore Health
```
Bargain Restore Health               (22) ✓
Cheap Restore Health                 (20) ✓
Standard Restore Health Potion       (30) ← adds "Potion"
Quality Restore Health               (22) ✓
Exclusive Restore Health             (22) ✓
```
**Issue**: Standard adds "Potion" — inconsistent with rest of set.

### Restore Magicka
```
Bargain Restore Magicka              (23) ✓
Cheap Restore Magicka                (21) ✓
Standard Restore Magicka Potion      (31) ← adds "Potion"
Quality Restore Magicka              (23) ✓
Exclusive Restore Magicka            (23) ✓
```
**Issue**: Standard adds "Potion" — inconsistent with rest of set.

### Resistance Potions
```
Bargain Disease Resistance           (26) 
Bargain Fire Resistance              (23) 
Bargain Frost Resistance             (24) 
Bargain Shock Resistance             (24) 
Bargain Poison Resistance            (25) 
Bargain Magicka Resistance           (26) 
Bargain Blight Resistance            (25) TD
```
All use "[Tier] [Element] Resistance" — consistent within group.

### Resist Paralysis (TD)
```
Bargain Paralysis Resistance         (28) 
Cheap Paralysis Resistance           (26) 
```
Matches other resistance potions. Consistent.

### Detect Potions
```
Potion of Detect Creatures           (26) 
Potion of Detect Enchantments        (29) 
Potion of Detect Key                 (20) 
```
**Issue**: "Enchantments" is plural but "Key" is singular. No tier prefix (Standard-only).

### Slowfall
```
Potion of Slowfalling                (21) 
```
**Issue**: "Slowfalling" vs game effect name "Slowfall". No tier prefix (Standard-only).

### Sound (TD)
```
Bargain Potion of Cacophony          (27) 
Cheap Potion of Cacophony            (25) 
Standard Potion of Cacophony         (28) 
Quality Potion of Cacophony          (27) 
Exclusive Potion of Cacophony        (29) 
```
Consistent within set.

### Blind (TD)
```
Bargain Potion of Blindness          (27) 
Cheap Potion of Blindness            (25) 
```
Consistent.

### Sanctuary (TD)
```
Bargain Potion of Evasion            (25) 
Cheap Potion of Evasion              (23) 
Standard Potion of Evasion           (26) 
Quality Potion of Evasion            (25) 
Exclusive Potion of Evasion          (27) 
```
Consistent within set.

### Shield (TD)
```
Bargain Potion of Protection         (28) 
Cheap Potion of Protection           (26) 
Standard Potion of Protection        (29) 
Quality Potion of Protection         (28) 
Exclusive Potion of Protection       (30) 
```
Consistent within set.

### Invisibility
```
Bargain Potion of Invisibility       (30) 
Cheap Potion of Invisibility         (28) 
Standard Potion of Invisibility      (31) 
Quality Potion of Invisibility       (30) 
Exclusive Invisibility               (22) ← MISSING "Potion of"
Cheap Potion of Invisibility         (28) TD
```
**Issue**: Exclusive drops "Potion of". "Exclusive Potion of Invisibility" = 32, exceeds limit.

---

## Proposed Naming Rules

1. Use `[Tier] Potion of [Effect]` when the longest tier (Standard/Exclusive) fits ≤ 31 chars.
2. Use `[Tier] [Effect]` when "Potion of" would exceed 31 chars.
3. All potions of the same effect must use the same pattern — no mixing within a set.
4. TD potions must match vanilla naming for the same effect.

### Character budget check

`Exclusive Potion of X` = 21 + len(X). Fits if effect name ≤ 10 chars.
`Standard Potion of X` = 20 + len(X). Fits if effect name ≤ 11 chars.

Longest tier word is "Exclusive" (9) or "Standard" (8). The binding constraint is always "Standard Potion of" (18+1 space) or "Exclusive Potion of" (19+1 space)... actually let's just count:
- `Exclusive Potion of ` = 20 chars prefix → effect name ≤ 11 chars
- `Standard Potion of ` = 19 chars prefix → effect name ≤ 12 chars

Effects that fit `Exclusive Potion of X` (≤11 chars):
- Burden (6) ✓
- Feather (7) ✓
- Fire Shield (11) ✓ → "Exclusive Potion of Fire Shield" = 31 ✓
- Jump (4) ✓
- Swift Swim (10) ✓ → "Exclusive Potion of Swift Swim" = 30 ✓
- Light (5) ✓
- Night-Eye (9) ✓
- Paralyze (8) ✓
- Silence (7) ✓
- Shadow (6) ✓
- Reflection (10) ✓ → "Exclusive Potion of Reflection" = 30 ✓
- Evasion (7) ✓
- Protection (10) ✓ → "Exclusive Potion of Protection" = 30 ✓
- Cacophony (9) ✓ → "Exclusive Potion of Cacophony" = 29 ✓
- Blindness (9) ✓

Effects that do NOT fit:
- Frost Shield (12) → "Exclusive Potion of Frost Shield" = 32 ✗
- Lightning Shield (16) → way over ✗
- Invisibility (13) → "Exclusive Potion of Invisibility" = 32 ✗ (but "Standard Potion of Invisibility" = 31 ✓)
- Spell Absorption (16) → way over ✗
- Fortify Health (14) → over ✗
- Fortify Magicka (15) → over ✗
- Fortify Fatigue (15) → over ✗
- Fortify [Attribute] (up to 20) → over ✗
- Restore [Stat] (up to 20) → over ✗
- [Element] Resistance (up to 18) → over ✗

---

## Final Rename List

### Fire Shield — drop "Potion of" to match Lightning Shield
All three elemental shields use `[Tier] Fire/Frost/Lightning Shield`.

| Current Name | New Name | Chars |
|---|---|---:|
| Bargain Potion of Fire Shield | Bargain Fire Shield | 19 |
| Cheap Potion of Fire Shield | Cheap Fire Shield | 17 |
| Standard Potion of Fire Shield | Standard Fire Shield | 20 |
| Quality Potion of Fire Shield | Quality Fire Shield | 19 |
| Exclusive Potion of Fire Shield | Exclusive Fire Shield | 21 |
| Cheap Potion of Fire Shield (TD) | Cheap Fire Shield | 17 |
| Quality Potion of Fire Shield (TD) | Quality Fire Shield | 19 |

### Frost Shield — drop "Potion of" from B/C/S to match Q/E
| Current Name | New Name | Chars |
|---|---|---:|
| Bargain Potion of Frost Shield | Bargain Frost Shield | 20 |
| Cheap Potion of Frost Shield | Cheap Frost Shield | 18 |
| Standard Potion of Frost Shield | Standard Frost Shield | 21 |
| Quality Frost Shield | Quality Frost Shield | 20 |
| Exclusive Frost Shield | Exclusive Frost Shield | 22 |
| Cheap Potion of Frost Shield (TD) | Cheap Frost Shield | 18 |
| Quality Frost Shield (TD) | Quality Frost Shield | 20 |

### Invisibility — drop "Potion of" (Exclusive = 32, exceeds limit)
| Current Name | New Name | Chars |
|---|---|---:|
| Bargain Potion of Invisibility | Bargain Invisibility | 20 |
| Cheap Potion of Invisibility | Cheap Invisibility | 18 |
| Standard Potion of Invisibility | Standard Invisibility | 21 |
| Quality Potion of Invisibility | Quality Invisibility | 20 |
| Exclusive Invisibility | Exclusive Invisibility | 22 |
| Cheap Potion of Invisibility (TD) | Cheap Invisibility | 18 |

### Fortify Health — standardize to `[Tier] Fortify Health`
| Current Name | New Name | Chars |
|---|---|---:|
| Bargain Fortify Health Potion | Bargain Fortify Health | 22 |
| Cheap Potion of Fortify Health | Cheap Fortify Health | 20 |
| Standard Fortify Health Potion | Standard Fortify Health | 23 |
| Quality Fortify Health | Quality Fortify Health | 22 |
| Exclusive Fortify Health | Exclusive Fortify Health | 24 |
| Cheap Potion of Fortify Health (TD) | Cheap Fortify Health | 20 |

### Fortify Magicka — standardize to `[Tier] Fortify Magicka`
| Current Name | New Name | Chars |
|---|---|---:|
| Bargain Fortify Magicka | Bargain Fortify Magicka | 23 |
| Cheap Potion of Fortify Magicka | Cheap Fortify Magicka | 21 |
| Standard Fortify Magicka Potion | Standard Fortify Magicka | 24 |
| Quality Fortify Magicka | Quality Fortify Magicka | 22 |
| Exclusive Fortify Magicka | Exclusive Fortify Magicka | 25 |
| Cheap Potion of Fortify Magicka (TD) | Cheap Fortify Magicka | 21 |
| Bargain Fortify Casting (TD) | Bargain Fortify Magicka | 23 |
| Cheap Fortify Casting (TD) | Cheap Fortify Magicka | 21 |

### Fortify Fatigue — drop "Potion" from Standard
| Current Name | New Name | Chars |
|---|---|---:|
| Standard Fortify Fatigue Potion | Standard Fortify Fatigue | 24 |

### Fortify Luck (TD) — drop "Potion of" to match other Fortify Attrs
| Current Name | New Name | Chars |
|---|---|---:|
| Bargain Potion of Fortify Luck | Bargain Fortify Luck | 20 |
| Cheap Potion of Fortify Luck | Cheap Fortify Luck | 18 |

### Restore Health — drop "Potion" from Standard
| Current Name | New Name | Chars |
|---|---|---:|
| Standard Restore Health Potion | Standard Restore Health | 23 |

### Restore Magicka — drop "Potion" from Standard
| Current Name | New Name | Chars |
|---|---|---:|
| Standard Restore Magicka Potion | Standard Restore Magicka | 24 |

### Levitation (TD) — rename to match vanilla
| Current Name | New Name | Chars |
|---|---|---:|
| Cheap Potion of Levitation | Cheap Rising Force Potion | 25 |

### Detect Enchantments — match spell name (singular)
| Current Name | New Name | Chars |
|---|---|---:|
| Potion of Detect Enchantments | Potion of Detect Enchantment | 28 |
| Potion of Detect Enchantments (TD) | Potion of Detect Enchantment | 28 |

### Slowfall — match effect name
| Current Name | New Name | Chars |
|---|---|---:|
| Potion of Slowfalling | Potion of Slowfall | 18 |

---

## Summary

| Group | Renames |
|-------|--------:|
| Fire Shield (drop "Potion of") | 7 |
| Frost Shield (drop "Potion of" from B/C/S) | 5 |
| Invisibility (drop "Potion of") | 6 |
| Fortify Health (standardize) | 4 |
| Fortify Magicka (standardize + TD Casting) | 5 |
| Fortify Fatigue (Standard outlier) | 1 |
| Fortify Luck TD (drop "Potion of") | 2 |
| Restore Health (Standard outlier) | 1 |
| Restore Magicka (Standard outlier) | 1 |
| Levitation TD (match vanilla) | 1 |
| Detect Enchantment (singular) | 2 |
| Slowfall (match effect name) | 1 |
| **Total** | **36** |

All proposed names verified ≤ 31 characters.

## Potions NOT renamed (already consistent)

- Burden: `[Tier] Potion of Burden` — all fit ✓
- Feather: `[Tier] Potion of Feather` — all fit ✓
- Jump: `[Tier] Potion of Jump` — all fit ✓
- Swift Swim: `[Tier] Potion of Swift Swim` — all fit ✓
- Levitate (vanilla): `[Tier] Rising Force Potion` — all fit ✓
- Light: `[Tier] Potion of Light` — all fit ✓
- Night-Eye: `[Tier] Potion of Night-Eye` — all fit ✓
- Paralyze: `[Tier] Potion of Paralyze` — all fit ✓
- Silence: `[Tier] Potion of Silence` — all fit ✓
- Shadow: `[Tier] Potion of Shadow` — all fit ✓
- Reflection: `[Tier] Potion of Reflection` — all fit ✓
- Evasion (TD): `[Tier] Potion of Evasion` — all fit ✓
- Protection (TD): `[Tier] Potion of Protection` — all fit ✓
- Cacophony (TD): `[Tier] Potion of Cacophony` — all fit ✓
- Blindness (TD): `[Tier] Potion of Blindness` — all fit ✓
- Lightning Shield: `[Tier] Lightning Shield` — all fit ✓
- Spell Absorption: `[Tier] Spell Absorption` — all fit ✓
- All Resistances: `[Tier] [Element] Resistance` — all fit ✓
- All Restore Attribute: `[Tier] Restore [Attr]` — all fit ✓
- All Fortify Attribute: `[Tier] Fortify [Attr]` — all fit ✓
- Restore Fatigue: `[Tier] Restore Fatigue` — all fit ✓
- Detect Creatures / Detect Key: already correct ✓
- Water Breathing / Water Walking / Dispel: unique, no tier set ✓

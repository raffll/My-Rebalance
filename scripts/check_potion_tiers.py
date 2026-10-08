#!/usr/bin/env python3
"""Verify potion mag/dur against the potion-tier rules.

Read-only. Checks every single-effect Alchemy (potion) record in the Potions
ESP JSON against the rules defined in docs/Potion-Tier-Rules-By-Effect.md and
.kiro/steering/potion-tiers.md. Prints only MISMATCHES.

Rule categories (see the docs for the authoritative list):
  - Multi-effect potions           -> SKIPPED (not tier-checked).
  - No-scale (Fire/Frost/Shock
    Damage, Poison)                -> SKIPPED.
  - Magnitude-only (Lock/Open/
    Dispel) and neither-axis
    (Mark/Recall/Interventions,
    all Cure*)                     -> SKIPPED.
  - Damage (DamageAttribute/Health/
    Magicka/Fatigue/Skill)         -> magnitude vs COLUMN 1; duration NOT checked.
  - Duration-only (Silence,
    Paralyze, Invisibility, Water
    Breathing/Walking, Summon*,
    Bound*)                        -> duration vs column for base_cost/40.
  - Standard (everything else)     -> magnitude AND duration vs base-cost column.

Base costs come from the Spells ESP's MagicEffect records (they moved there in
the Spells/Potions split), with vanilla masters as fallback.
"""
from __future__ import annotations
import json, math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ESP = os.path.join(ROOT, "R3 - Potions.json")
SPELLS_ESP = os.path.join(ROOT, "R3 - Spells.json")
MASTER_DIR = gc.DEFAULT_MASTER_DIR

# Tier table: column -> [(mag, dur) for B, C, S, Q, E].
TIERS = {
    8:   [(1, 3),  (2, 6),  (3, 9),  (4, 12), (6, 18)],
    5:   [(2, 6),  (3, 9),  (4, 12), (6, 18), (8, 24)],
    2:   [(3, 9),  (4, 12), (6, 18), (8, 24), (10, 30)],
    1:   [(6, 18), (8, 24), (10, 30),(15, 45),(20, 60)],
    0.5: [(10,30), (15,45), (20,60), (30,90), (40,120)],
    0.2: [(20,60), (30,90), (40,120),(60,180),(80,240)],
    0.1: [(60,180),(80,240),(100,300),(150,450),(200,600)],
}
GRADE_IX = {"b": 0, "c": 1, "s": 2, "q": 3, "e": 4}

# Damage family: magnitude only, always column 1.
DAMAGE = {"DamageAttribute", "DamageHealth", "DamageMagicka", "DamageFatigue",
          "DamageSkill"}
# No-scale: keep vanilla, never tiered.
NO_SCALE = {"FireDamage", "FrostDamage", "ShockDamage", "Poison"}


def base_to_col(base: float) -> float:
    """Map a base cost to a tier column via geometric-midpoint ranges."""
    if base >= math.sqrt(8 * 5):      # 6.32
        return 8
    if base >= math.sqrt(5 * 2):      # 3.16
        return 5
    if base >= math.sqrt(2 * 1):      # 1.41
        return 2
    if base >= math.sqrt(1 * 0.5):    # 0.71
        return 1
    if base >= math.sqrt(0.5 * 0.2):  # 0.32
        return 0.5
    if base >= math.sqrt(0.2 * 0.1):  # 0.14
        return 0.2
    return 0.1


def grade_of(rid: str) -> str | None:
    r = rid.lower()
    for g in ("_b", "_c", "_s", "_q", "_e"):
        if r.endswith(g):
            return g[1]
    return None


def load_base_costs(potions) -> dict[str, float]:
    base_cost: dict[str, float] = {}
    if os.path.exists(SPELLS_ESP):
        with open(SPELLS_ESP, "r", encoding="utf-8") as f:
            for o in json.load(f):
                if o.get("type") == "MagicEffect" and o.get("effect_id"):
                    bc = (o.get("data") or {}).get("base_cost")
                    if bc is not None:
                        base_cost[o["effect_id"]] = float(bc)
    missing = {(p["effects"][0] or {}).get("magic_effect") for p in potions}
    missing = {fx for fx in missing if fx and fx not in base_cost}
    if missing:
        for name in gc.MASTER_FILES:
            path = os.path.join(MASTER_DIR, name)
            if not os.path.exists(path):
                continue
            for o in gc.read_records(path):
                if isinstance(o, dict) and o.get("type") == "MagicEffect" \
                        and o.get("effect_id") in missing:
                    bc = (o.get("data") or {}).get("base_cost")
                    if bc is not None and o["effect_id"] not in base_cost:
                        base_cost[o["effect_id"]] = float(bc)
            if not (missing - set(base_cost)):
                break
    return base_cost


def main() -> int:
    with open(ESP, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_alchemy = [o for o in data if o.get("type") == "Alchemy" and o.get("effects")]
    single = [p for p in all_alchemy if len(p["effects"]) == 1]
    multi = [p for p in all_alchemy if len(p["effects"]) > 1]
    base_cost = load_base_costs(single)

    mismatches = 0
    checked = 0
    skipped_multi = len(multi)
    skipped_rule = 0

    for p in single:
        eff = p["effects"][0] or {}
        fx = eff.get("magic_effect") or ""
        rid = p.get("id") or ""
        grade = grade_of(rid)
        if grade is None:
            continue
        gi = GRADE_IX[grade]
        cur_mag = int(eff.get("max_magnitude", 0))
        cur_dur = int(eff.get("duration", 0))

        # Skipped categories: no-scale, magnitude-only, neither-axis.
        if fx in NO_SCALE:
            skipped_rule += 1
            continue
        if fx not in DAMAGE and not gc.effect_uses_duration(fx):
            # magnitude-only (Lock/Open/Dispel) or neither (also !uses_magnitude)
            skipped_rule += 1
            continue

        if fx in DAMAGE:
            # Magnitude vs column 1; duration not checked.
            exp_mag = TIERS[1][gi][0]
            checked += 1
            if cur_mag != exp_mag:
                mismatches += 1
                print(f"  MISMATCH {rid:<34} {fx:<22} DAMAGE col=1 "
                      f"grade={grade.upper()}  mag is {cur_mag} expected {exp_mag}")
            continue

        bc = base_cost.get(fx)
        if bc is None:
            print(f"  ? no base cost for {fx} ({rid})")
            continue

        if not gc.effect_uses_magnitude(fx):
            # Duration-only: duration vs column for base/40.
            col = base_to_col(bc / 40.0)
            exp_dur = TIERS[col][gi][1]
            checked += 1
            if cur_dur != exp_dur:
                mismatches += 1
                print(f"  MISMATCH {rid:<34} {fx:<22} DUR-ONLY col={col:<4} "
                      f"grade={grade.upper()}  dur is {cur_dur}s expected {exp_dur}s")
            continue

        # Standard: magnitude AND duration vs base-cost column.
        col = base_to_col(bc)
        exp_mag, exp_dur = TIERS[col][gi]
        checked += 1
        if cur_mag != exp_mag or cur_dur != exp_dur:
            mismatches += 1
            print(f"  MISMATCH {rid:<34} {fx:<22} STD col={col:<4} "
                  f"grade={grade.upper()}  is {cur_mag}/{cur_dur}s "
                  f"expected {exp_mag}/{exp_dur}s")

    print(f"\n{mismatches} mismatch(es).")
    print(f"  checked        : {checked} single-effect potions")
    print(f"  skipped (multi): {skipped_multi}")
    print(f"  skipped (rule) : {skipped_rule} (no-scale / magnitude-only / neither)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

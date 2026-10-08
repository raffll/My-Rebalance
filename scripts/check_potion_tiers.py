#!/usr/bin/env python3
"""Verify potion mag/dur against the potion-tiers ranges.

Read-only. For every Alchemy (potion) record in the Potions ESP JSON,
determine its effect's CURRENT base cost (from the MagicEffect records in the
Spells ESP JSON, falling back to the vanilla masters), map that base cost to a tier
column using the geometric-midpoint ranges from .kiro/steering/potion-tiers.md,
and compare the potion's actual mag/dur to the expected tier cell for its grade
(B/C/S/Q/E). Prints only MISMATCHES.

Duration-only effects (no magnitude) use effective base = base/40 and the
duration column only. Magnitude-only / neither-axis effects are skipped (no
tier scaling applies).
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

# Tier table: column -> {grade: (mag, dur)}. Grades keyed by vanilla duration.
# Columns are the dotted grid from potion-tiers.md.
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

# Range boundaries (geometric midpoints), high end exclusive.
# base >= 6.32 -> col 8 ; etc.
def base_to_col(base: float) -> float:
    if base >= math.sqrt(8*5):      # 6.32
        return 8
    if base >= math.sqrt(5*2):      # 3.16
        return 5
    if base >= math.sqrt(2*1):      # 1.41
        return 2
    if base >= math.sqrt(1*0.5):    # 0.71
        return 1
    if base >= math.sqrt(0.5*0.2):  # 0.32
        return 0.5
    if base >= math.sqrt(0.2*0.1):  # 0.14
        return 0.2
    return 0.1


def grade_of(rid: str) -> str | None:
    r = rid.lower()
    for g in ("_b", "_c", "_s", "_q", "_e"):
        if r.endswith(g):
            return g[1]
    return None


def main() -> int:
    with open(ESP, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Current base costs from the Spells ESP's MagicEffect records (MagicEffects
    # moved there in the Spells/Potions split; the Potions JSON has none).
    base_cost: dict[str, float] = {}
    if os.path.exists(SPELLS_ESP):
        with open(SPELLS_ESP, "r", encoding="utf-8") as f:
            spells_data = json.load(f)
        for o in spells_data:
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                bc = (o.get("data") or {}).get("base_cost")
                if bc is not None:
                    base_cost[o["effect_id"]] = float(bc)

    # Fill missing base costs from vanilla masters.
    missing = set()
    potions = [o for o in data if o.get("type") == "Alchemy" and (o.get("effects"))]
    for p in potions:
        fx = (p["effects"][0] or {}).get("magic_effect")
        if fx and fx not in base_cost:
            missing.add(fx)
    if missing:
        for name in gc.MASTER_FILES:
            path = os.path.join(MASTER_DIR, name)
            if not os.path.exists(path):
                continue
            for o in gc.read_records(path):
                if not isinstance(o, dict):
                    continue
                if o.get("type") == "MagicEffect" and o.get("effect_id") in missing:
                    bc = (o.get("data") or {}).get("base_cost")
                    if bc is not None and o["effect_id"] not in base_cost:
                        base_cost[o["effect_id"]] = float(bc)
            if not (missing - set(base_cost)):
                break

    mismatches = 0
    for p in potions:
        eff = p["effects"][0] or {}
        fx = eff.get("magic_effect") or ""
        rid = p.get("id") or ""
        grade = grade_of(rid)
        if grade is None:
            continue
        if not gc.effect_uses_magnitude(fx) and not gc.effect_uses_duration(fx):
            continue  # neither axis: no tier
        bc = base_cost.get(fx)
        if bc is None:
            print(f"  ? no base cost for {fx} ({rid})")
            continue
        dur_only = not gc.effect_uses_magnitude(fx)
        eff_base = (bc / 40.0) if dur_only else bc
        col = base_to_col(eff_base)
        exp_mag, exp_dur = TIERS[col][GRADE_IX[grade]]
        cur_mag = int(eff.get("max_magnitude", 0))
        cur_dur = int(eff.get("duration", 0))
        if dur_only:
            ok = (cur_dur == exp_dur)
            exp_s, cur_s = f"{exp_dur}s", f"{cur_dur}s"
        else:
            ok = (cur_mag == exp_mag and cur_dur == exp_dur)
            exp_s, cur_s = f"{exp_mag}/{exp_dur}s", f"{cur_mag}/{cur_dur}s"
        if not ok:
            mismatches += 1
            print(f"  MISMATCH {rid:<34} {fx:<20} base={bc:<5} col={col:<4} "
                  f"grade={grade.upper()}  is {cur_s:<10} expected {exp_s}")

    print(f"\n{mismatches} mismatch(es) across {len(potions)} potion records.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

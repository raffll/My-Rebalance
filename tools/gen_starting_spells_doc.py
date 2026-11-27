#!/usr/bin/env python3
"""Proposition doc: starting spells brought into the 5-30 cost range.

Lists every spell flagged PC_START_SPELL in the full TR load order (later files
win) and its engine cost with vanilla base costs and with R3 base costs (after
the R3 - Spells duration conversion, rules in
.kiro/steering/spell-conversion-rules.md). Spells outside 5-30 get two
propositions: change duration, or change magnitude. Writes
docs/Starting-Spells-Proposition.md.

Usage:
  python tools/gen_starting_spells_doc.py
"""
from __future__ import annotations
import math
import os
import re
import sys

MOD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc  # noqa: E402

MASTERS = ["Morrowind.json", "Tribunal.json", "Bloodmoon.json", "Patch for Purists.json",
           "Tamriel_Data.json", "TR_Mainland.json", "TR_Factions.json", "Cyr_Main.json",
           "Sky_Main.json"]
COSTS_LUA = os.path.join(MOD_DIR, "scripts", "R3SpellsLua", "costs.lua")
SPELLS_LUA = os.path.join(MOD_DIR, "scripts", "R3SpellsLua", "spells.lua")
OUT = os.path.join(MOD_DIR, "docs", "Starting-Spells-Proposition.md")
LOW, HIGH = 5, 30

# Substitute candidates for the out-of-range starting spells, kept with their
# own values (no edits): Morrowind.esm spells of the same role that cost 5-30
# with vanilla and with R3 base costs.
SUBSTITUTES = {
    "exhausting touch": ["knuckle luck", "ironhand", "hornhand", "grave curse: fatigue"],
    "feet of notorgo": ["skylamp's shadow", "quicksilver"],
    "tap energy": ["absorb health", "absorb health [ranged]", "vampire touch", "red despair"],
}


def lua_round(x: float) -> int:
    return math.floor(x + 0.5)


def is_whole(f: float) -> bool:
    r = f if f >= 1 else 1 / f
    return abs(r - lua_round(r)) < 1e-4


def round5(m: int) -> int:
    if m <= 1:
        return m
    if m < 5:
        return 1 if m <= 2 else 5
    return lua_round(m / 5) * 5


def main() -> int:
    text = open(COSTS_LUA, encoding="utf-8").read()
    r3 = {k: float(v) for k, _, v in
          re.findall(r'\["(\w+)"\] = \{ ([\d.]+), ([\d.]+) \}', text)}

    base: dict[str, float] = {}
    names: dict[str, str] = {}
    spells: dict[str, dict] = {}
    cost_mult = 0.5
    for m in MASTERS:
        path = os.path.join(gc.DEFAULT_MASTER_DIR, m)
        if not os.path.exists(path):
            continue
        for o in gc.read_records(path):
            if not isinstance(o, dict):
                continue
            t = o.get("type")
            if t == "MagicEffect":
                base[o["effect_id"].lower()] = float(o["data"]["base_cost"])
            elif t == "GameSetting":
                gid = o.get("id", "")
                v = (o.get("value") or {}).get("data")
                if gid.startswith("sEffect") and isinstance(v, str) and v:
                    names[gid[len("sEffect"):].lower()] = v
                elif gid == "fEffectCostMult" and isinstance(v, (int, float)):
                    cost_mult = float(v)
            elif t == "Spell":
                spells[o["id"].lower()] = o
    start = sorted((s for s in spells.values() if "PC_START_SPELL" in s["data"]["flags"]),
                   key=lambda s: (s.get("name") or s["id"]).lower())

    def effect_cost(e: dict, b: float) -> float:
        fx = e["magic_effect"]
        if gc.effect_uses_magnitude(fx):
            mn, mx = max(1, e["min_magnitude"]), max(1, e["max_magnitude"])
        else:
            mn = mx = 1
        d = max(1, e["duration"]) if gc.effect_uses_duration(fx) else 1
        x = 0.5 * (mn + mx) * 0.1 * b * d + 0.05 * e["area"] * b
        return x * 1.5 if e["range"] == "OnTarget" else x

    def cost(effects: list, costs: dict) -> int:
        return lua_round(sum(effect_cost(e, costs[e["magic_effect"].lower()]) for e in effects)
                         * cost_mult)

    def r3_convert(effects: list) -> list:
        out = []
        for e in effects:
            n = dict(e)
            fx = e["magic_effect"]
            k = fx.lower()
            b0, b1 = base.get(k, 0), r3.get(k, base.get(k, 0))
            if b0 > 0 and abs(b0 - b1) > 1e-4 and gc.effect_uses_duration(fx):
                f = b0 / b1
                d = e["duration"] * f
                if is_whole(f) and d >= 1 and abs(d - lua_round(d)) < 1e-4:
                    n["duration"] = lua_round(d)
            out.append(n)
        return out

    def target_of(c: int) -> int | None:
        if c < LOW:
            return LOW
        if c > HIGH:
            return HIGH
        return None

    def by_duration(effects: list, costs: dict):
        if not any(gc.effect_uses_duration(e["magic_effect"]) for e in effects):
            return None
        c = cost(effects, costs)
        t = target_of(c)
        new = [dict(e) for e in effects]
        for e in new:
            if gc.effect_uses_duration(e["magic_effect"]):
                e["duration"] = max(1, lua_round(e["duration"] * t / c))
        step = 1 if cost(new, costs) < LOW else -1
        for _ in range(10000):
            nc = cost(new, costs)
            if LOW <= nc <= HIGH:
                return new, nc
            for e in new:
                if gc.effect_uses_duration(e["magic_effect"]):
                    e["duration"] = max(1, e["duration"] + step)
            if all(e["duration"] == 1 for e in new if gc.effect_uses_duration(e["magic_effect"])) \
                    and step < 0 and cost(new, costs) > HIGH:
                return new, cost(new, costs)
        return None

    def by_magnitude(effects: list, costs: dict):
        if not any(gc.effect_uses_magnitude(e["magic_effect"]) for e in effects):
            return None
        c = cost(effects, costs)
        r = target_of(c) / c
        best = None
        for _ in range(500):
            new = [dict(e) for e in effects]
            for e in new:
                if gc.effect_uses_magnitude(e["magic_effect"]):
                    a = max(1, lua_round(e["min_magnitude"] * r))
                    b = max(1, lua_round(e["max_magnitude"] * r))
                    if a != b:
                        a, b = round5(a), round5(b)
                    e["min_magnitude"], e["max_magnitude"] = a, b
            nc = cost(new, costs)
            best = (new, nc)
            if LOW <= nc <= HIGH:
                return best
            r *= 0.98 if nc > HIGH else 1.02
        return best

    def label(e: dict) -> str:
        n = names.get(e["magic_effect"].lower(), gc.split_camel(e["magic_effect"]))
        a = e.get("attribute")
        if a and a != "None":
            n = f"{n}: {gc.split_camel(a)}"
        rng = {"OnTouch": " Touch", "OnTarget": " Target"}.get(e["range"], "")
        return f"{n} {gc.format_effect_values(e)}{rng}"

    def vals(effects: list) -> str:
        return " + ".join(gc.format_effect_values(e) for e in effects)

    head = ["Spell", "ID", "Effect", "Cost", "In range", "By duration", "Cost",
            "By magnitude", "Cost"]
    right = {3, 6, 8}

    def table(rows):
        w = [max(len(head[i]), *(len(r[i]) for r in rows)) for i in range(len(head))]

        def line(cells):
            return "| " + " | ".join(c.rjust(w[i]) if i in right else c.ljust(w[i])
                                     for i, c in enumerate(cells)) + " |"

        sep = "|" + "|".join(("-" * (w[i] + 1) + ":") if i in right else ("-" * (w[i] + 2))
                             for i in range(len(head))) + "|"
        return [line(head), sep] + [line(r) for r in rows]

    def section(costs: dict, convert: bool):
        rows, out_of_range = [], 0
        for s in start:
            effects = r3_convert(s["effects"]) if convert else s["effects"]
            c = cost(effects, costs)
            ok = LOW <= c <= HIGH
            d = m = None
            if not ok:
                out_of_range += 1
                d = by_duration(effects, costs)
                m = by_magnitude(effects, costs)
            rows.append([
                s.get("name") or s["id"],
                f"`{s['id']}`",
                " + ".join(label(e) for e in effects),
                str(c),
                "yes" if ok else ("below" if c < LOW else "above"),
                vals(d[0]) if d else ("-" if ok else "n/a"),
                str(d[1]) if d else "",
                vals(m[0]) if m else ("-" if ok else "n/a"),
                str(m[1]) if m else "",
            ])
        return rows, out_of_range

    van_rows, van_out = section(base, False)
    r3_costs = {k: r3.get(k, v) for k, v in base.items()}
    r3_rows, r3_out = section(r3_costs, True)

    out = [
        "# R3 - Starting Spells: Proposition",
        "",
        f"Rule: every starting spell costs between {LOW} and {HIGH} magicka.",
        "",
        "Starting spells are the spells flagged `PC_START_SPELL` in the full TR load",
        "order (later files win). Costs are the engine autocalc cost",
        f"(`calcEffectCost`, x1.5 on target, fEffectCostMult {cost_mult:g}). Generated by",
        "`tools/gen_starting_spells_doc.py`.",
        "",
        "## Legend",
        "",
        "- **Effect / Cost**: values and cost as loaded for that table.",
        f"- **In range**: `yes`, `below` {LOW} or `above` {HIGH}.",
        "- **By duration**: proposition that changes only duration (whole seconds,",
        "  at least 1s) to reach the nearest bound; magnitude kept.",
        "- **By magnitude**: proposition that changes only magnitude to reach the",
        "  nearest bound; ranges rounded to 1 or multiples of 5 (R3 - Rounding rule);",
        "  duration kept.",
        "- `n/a`: the effect has no duration (or no magnitude) to change.",
        "",
        f"## Vanilla base costs ({van_out} out of range)",
        "",
    ] + table(van_rows) + [
        "",
        f"## R3 base costs ({r3_out} out of range)",
        "",
        "With R3 - Spells: R3 base costs and its duration conversion applied first.",
        "",
    ] + table(r3_rows)

    # Substitutes (old R3 proposition).
    sub_head = ["Replaces", "Substitute", "ID", "Effect", "Vanilla", "R3"]
    sub_right = {4, 5}
    sub_rows = []
    for old_id, candidates in SUBSTITUTES.items():
        for i, new_id in enumerate(candidates):
            s = spells.get(new_id)
            if not s:
                continue
            effects = s["effects"]
            cv = cost(effects, base)
            r_eff = r3_convert(effects)
            cr = cost(r_eff, r3_costs)

            def mark(c):
                return f"{c}" if LOW <= c <= HIGH else f"{c} (out)"

            sub_rows.append([
                (spells[old_id].get("name") or old_id) if i == 0 else "",
                s.get("name") or new_id,
                f"`{s['id']}`",
                " + ".join(label(e) for e in effects),
                mark(cv),
                mark(cr) + (f" ({vals(r_eff)})" if r_eff != effects else ""),
            ])
    w = [max(len(sub_head[i]), *(len(r[i]) for r in sub_rows)) for i in range(len(sub_head))]

    def sub_line(cells):
        return "| " + " | ".join(c.rjust(w[i]) if i in sub_right else c.ljust(w[i])
                                 for i, c in enumerate(cells)) + " |"

    out += [
        "",
        "## Substitutes",
        "",
        "Existing Morrowind.esm spells, unchanged, that cost 5-30 with vanilla and with",
        "R3 base costs. First row of each group = old R3 choice where it fits",
        "(Skylamp's Shadow); old R3's Weariness costs 1 unedited and Tap Energy has no",
        "Absorb Fatigue substitute in range, so those groups list the closest roles.",
        "R3 column: after the R3 - Spells conversion (new values in brackets).",
        "",
        sub_line(sub_head),
        "|" + "|".join(("-" * (w[i] + 1) + ":") if i in sub_right else ("-" * (w[i] + 2))
                       for i in range(len(sub_head))) + "|",
    ] + [sub_line(r) for r in sub_rows]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print(f"{OUT}: {len(start)} starting spells, vanilla {van_out} / R3 {r3_out} out of range")
    return 0


if __name__ == "__main__":
    sys.exit(main())

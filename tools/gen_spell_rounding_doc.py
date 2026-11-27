#!/usr/bin/env python3
"""List buyable spells whose duration conversion does not come out exact.

Simulates scripts/R3SpellsLua/load.lua (rules in
.kiro/steering/spell-conversion-rules.md) over the spells in
scripts/R3SpellsLua/costs.lua and spells.lua, assuming the masters' (vanilla) base costs are
the loaded ones. Writes docs/Spell-Duration-Conversion.md.

Usage:
  python tools/gen_spell_rounding_doc.py
"""
from __future__ import annotations
import math
import os
import re
import sys

MOD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc  # noqa: E402

# Load order, lowest first; later files override (as in game).
MASTERS = ["Morrowind.json", "Tribunal.json", "Bloodmoon.json", "Patch for Purists.json",
           "Tamriel_Data.json", "TR_Mainland.json", "TR_Factions.json", "Cyr_Main.json",
           "Sky_Main.json"]
COSTS_LUA = os.path.join(MOD_DIR, "scripts", "R3SpellsLua", "costs.lua")
SPELLS_LUA = os.path.join(MOD_DIR, "scripts", "R3SpellsLua", "spells.lua")
OUT = os.path.join(MOD_DIR, "docs", "Spell-Duration-Conversion.md")
F_EFFECT_COST_MULT = 0.5


def lua_round(x: float) -> int:
    return math.floor(x + 0.5)


def is_whole(f: float) -> bool:
    r = f if f >= 1 else 1 / f
    return abs(r - lua_round(r)) < 1e-4


def fmt(x: float) -> str:
    return f"{x:.2f}".rstrip("0").rstrip(".")


def effect_cost(e: dict, fx: str, base: float, dur: int) -> float:
    if gc.effect_uses_magnitude(fx):
        mn, mx = max(1, e["min_magnitude"]), max(1, e["max_magnitude"])
    else:
        mn = mx = 1
    d = max(1, dur) if gc.effect_uses_duration(fx) else 1
    x = 0.5 * (mn + mx) * 0.1 * base * d + 0.05 * e["area"] * base
    return x * 1.5 if e["range"] == "OnTarget" else x


def main() -> int:
    text = open(COSTS_LUA, encoding="utf-8").read()
    r3 = {k: float(v) for k, _, v in
          re.findall(r'\["(\w+)"\] = \{ ([\d.]+), ([\d.]+) \}', text)}
    ids = set(re.findall(r'^    "(.+)",$', open(SPELLS_LUA, encoding="utf-8").read(), re.M))

    base: dict[str, float] = {}
    spells: dict[str, dict] = {}
    for m in MASTERS:
        for o in gc.read_records(os.path.join(gc.DEFAULT_MASTER_DIR, m)):
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect":
                base[o["effect_id"].lower()] = float(o["data"]["base_cost"])
            elif o.get("type") == "Spell" and o["id"].lower() in ids:
                spells[o["id"].lower()] = o

    groups = {(c, m, a): [] for c in (False, True) for m in (False, True) for a in (True, False)}
    for sid in sorted(spells, key=lambda s: (spells[s].get("name") or s).lower()):
        s = spells[sid]
        autocalc = "AUTO_CALCULATE" in str(s["data"].get("flags", ""))
        effects = s.get("effects") or []
        info, old, new, unclean, whole = [], 0.0, 0.0, False, False
        for e in effects:
            fx = e["magic_effect"]
            k = fx.lower()
            b0 = base.get(k, 0.0)
            b1 = r3.get(k, b0)
            dur = e["duration"]
            new_dur, f, would, issue = dur, None, "", ""
            if k in r3 and b0 > 0 and abs(b0 - b1) > 1e-4:
                f = b0 / b1
                if is_whole(f):
                    whole = True
                if not gc.effect_uses_duration(fx):
                    issue, unclean = "no duration", True
                elif not is_whole(f):
                    issue, unclean = "fractional change", True
                else:
                    exact = dur * f
                    would = f"{fmt(exact)}s"
                    if dur == 0:
                        issue, unclean = "0s duration", True
                    elif exact < 1:
                        issue, unclean = "below 1s", True
                    elif abs(exact - lua_round(exact)) > 1e-4:
                        issue, unclean = "not whole seconds", True
                    else:
                        new_dur = lua_round(exact)
                        issue = f"scaled to {new_dur}s"
            else:
                issue = "base cost unchanged"
            info.append((fx, f, dur, would, issue))
            old += effect_cost(e, fx, b0, dur)
            new += effect_cost(e, fx, b1, new_dur)
        if not whole:
            continue
        if autocalc:
            c0, c1 = lua_round(old * F_EFFECT_COST_MULT), lua_round(new * F_EFFECT_COST_MULT)
        else:
            c0 = s["data"]["cost"]
            c1 = max(1, lua_round(c0 * new / old)) if old > 0 and c0 > 0 else c0
        target = groups[(not unclean, len(effects) > 1, autocalc)]
        for i, (fx, f, dur, would, issue) in enumerate(info):
            first = i == 0
            target.append([
                (s.get("name") or sid) if first else "",
                f"`{s['id']}`" if first else "",
                gc.split_camel(fx),
                "" if f is None else (f"1/{lua_round(1 / f)}" if f < 1 and is_whole(f) else f"{f:.3f}".rstrip("0").rstrip(".")),
                f"{dur}s",
                would,
                issue,
                str(c0) if first else "",
                str(c1) if first else "",
            ])

    head = ["Spell", "ID", "Effect", "Factor", "Dur", "Would be",
            "Issue", "Cost before", "Cost after"]
    right = {3, 4, 5, 7, 8}

    def table(rows):
        w = [max(len(head[i]), *(len(r[i]) for r in rows)) for i in range(len(head))]

        def line(cells):
            return "| " + " | ".join(c.rjust(w[i]) if i in right else c.ljust(w[i])
                                     for i, c in enumerate(cells)) + " |"

        sep = "|" + "|".join(("-" * (w[i] + 1) + ":") if i in right else ("-" * (w[i] + 2))
                             for i in range(len(head))) + "|"
        return [line(head), sep] + [line(r) for r in rows]

    def count(rows):
        return len([r for r in rows if r[1]])

    def n(clean, multi=None):
        return sum(count(groups[(clean, m, au)]) for m in (False, True) for au in (True, False)
                   if multi is None or m == multi)

    out = [
        "# R3 - Spells Lua: Duration Conversion",
        "",
        "Buyable spells with a whole base cost change, by how the duration multiplier",
        "applies (`.kiro/steering/spell-conversion-rules.md`). Generated by",
        "`tools/gen_spell_rounding_doc.py`; assumes the loaded base costs are the",
        "masters' values (full TR load order, later files win).",
        "",
        f"- **Clean**: {n(True)} spells. Every effect with a changed base cost is",
        "  scaled to whole seconds, so the cost stays the same.",
        f"- **Unclean**: {n(False)} spells. At least one changed effect cannot be",
        "  scaled cleanly (fractional change, no duration, or the multiplier does not",
        "  give whole seconds). That effect is kept as is and the cost moves.",
        "",
        "Only spells with at least one whole base cost change are listed. Spells whose",
        "changes are all fractional keep magnitude and duration; only the cost moves.",
        "",
        "## Legend",
        "",
        "- **Factor**: loaded base cost / R3 base cost (empty = base cost unchanged).",
        "- **Would be**: duration x factor, for whole base cost changes.",
        "- **Issue**: `scaled to Ns` = clean multiplier applied; `not whole seconds` =",
        "  Would be has a fraction; `below 1s` = Would be is under 1s; `0s duration` =",
        "  stored duration is 0; `fractional change`, `no duration`,",
        "  `base cost unchanged` = effect kept as is.",
        "- **Autocalc** tables: the engine computes the cost from the base costs.",
        "- **Not autocalc** tables: the spell has a stored cost, which the cost",
        "  algorithm adjusts.",
        "- **Cost before**: magicka cost with the loaded base costs.",
        "- **Cost after**: magicka cost after conversion with the R3 base costs.",
        "",
    ]
    for clean, top in ((False, "Unclean"), (True, "Clean")):
        out += [f"## {top} ({n(clean)})", ""]
        for multi, title in ((False, "Single-effect"), (True, "Multi-effect")):
            out += [f"### {top}: {title} ({n(clean, multi)})", ""]
            for auto, sub in ((True, "Autocalc"), (False, "Not autocalc")):
                rows = groups[(clean, multi, auto)]
                out += [f"#### {top}: {title}, {sub} ({count(rows)})", ""]
                out += (table(rows) if rows else ["None."]) + [""]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out).rstrip("\n") + "\n")
    print(f"{OUT}: {n(True)} clean, {n(False)} unclean")
    return 0


if __name__ == "__main__":
    sys.exit(main())

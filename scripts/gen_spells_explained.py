#!/usr/bin/env python3
"""Generate docs/Spells-Explained.md — the spells README layout plus a plain-
English explanation column saying which rule produced each spell's change.

Same structure/format as R3 - Spells.md (school -> effect -> rows), but each row
gets a 4th column: a short note on the rule applied (base-cost compensation,
no-scale, rounding, cost recompute, rename, AUTO_CALCULATE violation, ...).
This is a SEPARATE document; it does not touch R3 - Spells.md or gen_spells.py.

Read-only on the data. Rules per docs/Spell-Rules-Reference.md.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

COL_VALUES = 44
COL_ID = 80
COL_NOTE = 150          # explanation column
EFFECT_INDENT = "    "
DIVIDER = "-" * 60

MASTER_FILES = gc.MASTER_FILES
NO_SCALE = {"FireDamage", "FrostDamage", "ShockDamage", "Poison"}


def is_td(obj: dict) -> bool:
    return (obj.get("id") or "").startswith("T_")


def cost_label(obj: dict | None):
    if not obj:
        return None
    d = obj.get("data") or {}
    if "AUTO_CALCULATE" in (d.get("flags") or ""):
        return "auto"
    return d.get("cost")


def eff_sig(e: dict) -> tuple:
    return (e.get("magic_effect"), e.get("skill"), e.get("attribute"),
            e.get("range"), int(e.get("area", 0)), int(e.get("duration", 0)),
            int(e.get("min_magnitude", 0)), int(e.get("max_magnitude", 0)))


def changed(cur: dict, van: dict | None) -> bool:
    if van is None:
        return True
    ce, ve = cur.get("effects") or [], van.get("effects") or []
    if len(ce) != len(ve) or any(eff_sig(a) != eff_sig(b) for a, b in zip(ce, ve)):
        return True
    if cost_label(cur) != cost_label(van):
        return True
    if (cur.get("name") or "") != (van.get("name") or ""):
        return True
    return False


def ratio_word(factor: float) -> str:
    """Render a multiplicative factor as 'x3' or '/3' approximately."""
    if factor >= 1:
        return f"x{factor:g}"
    return f"/{(1/factor):g}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate the explained Spells doc.")
    ap.add_argument("--json", default="R3 - Spells.json")
    ap.add_argument("--out", default="docs/Spells-Explained.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    spells = [o for o in data if o.get("type") == "Spell"]

    # Current base costs + schools from this ESP's MagicEffect records.
    fx_cur_base: dict[str, float] = {}
    fx_school: dict[str, str] = {}
    for o in data:
        if o.get("type") == "MagicEffect" and o.get("effect_id"):
            d = o.get("data") or {}
            fx_cur_base[o["effect_id"]] = d.get("base_cost")
            fx_school[o["effect_id"]] = d.get("school")

    needed = {o["id"].lower().strip() for o in spells if o.get("id")}

    van_by_id: dict[str, dict] = {}
    fx_van_base: dict[str, float] = {}
    effect_names: dict[str, str] = {}
    for name in MASTER_FILES:
        path = os.path.join(args.master_dir, name)
        if not os.path.exists(path):
            continue
        for o in gc.read_records(path):
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                fx_van_base.setdefault(o["effect_id"], (o.get("data") or {}).get("base_cost"))
                if o["effect_id"] not in fx_school or fx_school[o["effect_id"]] is None:
                    fx_school[o["effect_id"]] = (o.get("data") or {}).get("school")
                continue
            rid = o.get("id")
            if not rid:
                continue
            if o.get("type") == "GameSetting" and rid.startswith("sEffect"):
                key = rid[len("sEffect"):]
                if key not in effect_names:
                    v = (o.get("value") or {}).get("data")
                    if isinstance(v, str) and v:
                        effect_names[key] = v
            k = rid.lower().strip()
            if k in needed and k not in van_by_id:
                van_by_id[k] = o

    def ename(fx: str) -> str:
        return effect_names.get(fx, gc.split_camel(fx))

    def effect_display_name(eff: dict) -> str:
        base = ename(eff.get("magic_effect", "") or "")
        skill, attr = eff.get("skill"), eff.get("attribute")
        if skill and skill != "None":
            return f"{base}: {gc.split_camel(skill)}"
        if attr and attr != "None":
            return f"{base}: {gc.split_camel(attr)}"
        return base

    def value_pair(cur_e: dict, van_e: dict | None) -> str:
        cur = gc.format_effect_values(cur_e)
        van = gc.format_effect_values(van_e) if van_e else None
        return f"{van} -> {cur}" if (van is not None and van != cur) else cur

    def nice(f: float) -> str:
        """Round a factor to a clean 'xN' / '/N' label. Not precise by design."""
        if f <= 0:
            return "x0"
        g = f if f >= 1 else 1 / f
        # snap to a tidy value
        for t in (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50):
            if abs(g - t) / t <= 0.15:
                g = t
                break
        else:
            g = round(g)
        s = f"{g:g}"
        return f"x{s}" if f >= 1 else f"/{s}"

    def prod(mf: float, df: float) -> float:
        return mf * df

    def explain(obj: dict, van: dict | None) -> str:
        """Terse realized-intent note, read from the values. Compensation shown
        as mag/dur = product vs the factor the base change needs."""
        notes: list[str] = []
        if is_td(obj) and cost_label(obj) == "auto":
            notes.append("TD-AUTOCALC ✗")

        effs = obj.get("effects") or []
        veffs = (van or {}).get("effects") or []
        e0 = effs[0] if effs else {}
        v0 = veffs[0] if veffs else None
        fx = e0.get("magic_effect", "")
        vb, cb = fx_van_base.get(fx), fx_cur_base.get(fx)
        base_changed = vb is not None and cb is not None and vb != cb

        def md_split(cur_e, van_e):
            if not van_e:
                return 1.0, 1.0
            vmn = int(van_e.get("min_magnitude", 0)) + int(van_e.get("max_magnitude", 0))
            cmn = int(cur_e.get("min_magnitude", 0)) + int(cur_e.get("max_magnitude", 0))
            vd = int(van_e.get("duration", 0))
            cd = int(cur_e.get("duration", 0))
            mf = (cmn / vmn) if vmn else 1.0
            df = (cd / vd) if vd else 1.0
            return mf, df

        md_changed = v0 is not None and eff_sig(e0) != eff_sig(v0)

        if fx in NO_SCALE:
            notes.append("no-scale")
        elif base_changed and v0 is not None:
            needed = vb / cb              # mag*dur must move by this to compensate
            base_factor = cb / vb         # cost should move by this if compensating via cost
            mf, df = md_split(e0, v0)
            got = prod(mf, df)
            scale = f"mag {nice(mf)}, dur {nice(df)}"
            md_ok = needed and 0.85 <= (got / needed) <= 1.18
            md_held = abs(mf - 1) <= 0.2 and abs(df - 1) <= 0.2
            # Cost-based compensation: stored cost moved by the base factor while
            # mag/dur were held (fixed-cost spells repriced instead of rescaled).
            cv, cc = cost_label(van), cost_label(obj)
            cost_num = isinstance(cv, (int, float)) and isinstance(cc, (int, float)) and cv
            cost_ratio = (cc / cv) if cost_num else None
            cost_ok = cost_ratio is not None and 0.85 <= (cost_ratio / base_factor) <= 1.18

            if needed == 0:
                notes.append(scale)
            elif md_ok:
                notes.append(f"{scale} = {nice(got)} compensated ✓")
            elif md_held and cost_ok:
                notes.append(f"mag/dur held; cost {nice(cost_ratio)} compensated via cost ✓")
            else:
                notes.append(f"{scale} = {nice(got)} ✗ (expected {nice(needed)})")
        elif base_changed:
            notes.append(f"base {nice(cb / vb)}")
        elif md_changed:
            mf, df = md_split(e0, v0)
            # A factor within ~20% of 1 is just a rounding nudge, not a rescale.
            mag_real = abs(mf - 1) > 0.2
            dur_real = abs(df - 1) > 0.2
            bits = [b for b in ((f"mag {nice(mf)}" if mag_real else ""),
                                (f"dur {nice(df)}" if dur_real else "")) if b]
            if bits:
                notes.append("rescaled " + " ".join(bits))
            else:
                notes.append("rounded")

        # Rounding flag.
        for e in effs:
            mn, mx = int(e.get("min_magnitude", 0)), int(e.get("max_magnitude", 0))
            if mn != mx and any(v != 1 and v % 5 != 0 for v in (mn, mx)):
                notes.append(f"rounding ✗ ({mn}-{mx})")
                break

        vn = (van or {}).get("name") if van else None
        if vn and vn != (obj.get("name") or ""):
            notes.append("renamed")

        if not notes:
            notes.append("cost" if cost_label(obj) != cost_label(van) else "changed")
        return "; ".join(notes)

    def emit_record(obj: dict, van: dict | None) -> list[str]:
        effs = obj.get("effects") or []
        veffs = (van or {}).get("effects") or []
        rows = [value_pair(effs[i], veffs[i] if i < len(veffs) else None)
                for i in range(len(effs))]
        cur_name = obj.get("name") or "(unnamed)"
        vn = van.get("name") if van else None
        name_seg = f"{vn} -> {cur_name}" if (vn and vn != cur_name) else cur_name
        cv, vv = cost_label(obj), cost_label(van)
        cost = ""
        if cv is not None and vv is not None and cv != vv:
            cost = f"[{vv} -> {cv}]"
        note = explain(obj, van)
        id_col = obj.get("id") or ""

        if len(rows) <= 1:
            vals = rows[0] if rows else ""
            if cost:
                vals = f"{vals} {cost}".strip()
            line = gc.add_at_column(id_col, COL_VALUES, vals)
            line = gc.add_at_column(line, COL_ID, name_seg)
            line = gc.add_at_column(line, COL_NOTE, note)
            return [line]

        first = gc.add_at_column(id_col, COL_VALUES, cost)
        first = gc.add_at_column(first, COL_ID, name_seg)
        first = gc.add_at_column(first, COL_NOTE, note)
        lines = [first]
        for i, r in enumerate(rows):
            label = f"{EFFECT_INDENT}{effect_display_name(effs[i])}"
            lines.append(gc.add_at_column(label, COL_VALUES, r))
        return lines

    def sort_key(obj: dict):
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        ve = (van or {}).get("effects") or []
        if not ve:
            return (1, 0, 0, obj.get("name", ""))
        e0 = ve[0]
        fx = e0.get("magic_effect", "") or ""
        mn, mx = int(e0.get("min_magnitude", 0)), int(e0.get("max_magnitude", 0))
        dur = int(e0.get("duration", 0))
        if gc.effect_uses_magnitude(fx):
            return (0, mn, mx, obj.get("name", ""))
        return (0, dur, dur, obj.get("name", ""))

    # Bucket CHANGED spells only. Single-effect spells go under school -> effect;
    # multi-effect spells collect into a dedicated end section (like potions).
    groups: dict[str, dict[str, list]] = {}
    multi: list = []
    changed_count = 0
    for o in spells:
        van = van_by_id.get((o.get("id") or "").lower().strip())
        if not changed(o, van):
            continue
        changed_count += 1
        effs = o.get("effects") or []
        if not effs:
            continue
        if len(effs) > 1:
            multi.append((o, van))
            continue
        fx = effs[0].get("magic_effect")
        school = fx_school.get(fx) or "Misc"
        groups.setdefault(school, {}).setdefault(fx, []).append((o, van))

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Spells (Explained)")
    out.append("")
    out.append("Generated companion to `R3 - Spells.md`. Same layout, with an extra")
    out.append("explanation column noting which rule produced each change. Only spells")
    out.append("that differ from vanilla are listed. Rules: see")
    out.append("`docs/Spell-Rules-Reference.md`. Do not hand-edit; regenerate with")
    out.append("`python scripts/gen_spells_explained.py`.")
    out.append("")

    def header(text: str) -> None:
        out.append(DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    for school in sorted(groups):
        header(f"## {school}")
        for fx in sorted(groups[school], key=ename):
            recs = groups[school][fx]
            header(f"### {ename(fx)}")
            vb, cb = fx_van_base.get(fx), fx_cur_base.get(fx)
            if vb is not None and cb is not None and vb != cb:
                out.append("```")
                out.append(gc.add_at_column("Base Cost", COL_VALUES, f"{vb} -> {cb}"))
                out.append("```")

            def block(title, items):
                if not items:
                    return
                if out[-1] != "":
                    out.append("")
                if title:
                    out.append(f"*{title}*")
                out.append("```")
                for o, van in sorted(items, key=lambda t: sort_key(t[0])):
                    out.extend(emit_record(o, van))
                out.append("```")

            block(None, [t for t in recs if not is_td(t[0])])
            block("Tamriel Data", [t for t in recs if is_td(t[0])])
            out.append("")

    if multi:
        header("## Multi-Effect Spells")

        def multi_block(title, items):
            if not items:
                return
            if title:
                out.append(f"*{title}*")
            out.append("```")
            for o, van in sorted(items, key=lambda t: sort_key(t[0])):
                out.extend(emit_record(o, van))
            out.append("```")
            out.append("")

        multi_block(None, [t for t in multi if not is_td(t[0])])
        multi_block("Tamriel Data", [t for t in multi if is_td(t[0])])

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  changed spells: {changed_count} of {len(spells)}")
    print(f"  schools: {len(groups)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

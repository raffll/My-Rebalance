#!/usr/bin/env python3
"""Generate docs/Spells-Explained.md — the spells README layout plus a plain-
English explanation column saying which rule produced each spell's change.

Same structure/format as R3 - Spells.md (school -> effect -> rows), but each row
gets a 4th column: a short note on the rule applied (base-cost compensation,
no-scale, rounding, cost recompute, rename, AUTO_CALCULATE violation, ...).
This is a SEPARATE document; it does not touch R3 - Spells.md or gen_readme.py.

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
COL_NOTE = 118          # explanation column
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

    def explain(obj: dict, van: dict | None) -> str:
        """Describe the realized intent of this spell's change, read from the
        values. Where a known rule explains it, mark the rule; otherwise state
        the plain decision (cost raised/reduced, rescaled, renamed)."""
        notes: list[str] = []
        if is_td(obj) and cost_label(obj) == "auto":
            notes.append("VIOLATION: TD spell must not be AUTO_CALCULATE")

        effs = obj.get("effects") or []
        veffs = (van or {}).get("effects") or []
        e0 = effs[0] if effs else {}
        v0 = veffs[0] if veffs else None
        fx = e0.get("magic_effect", "")
        vb, cb = fx_van_base.get(fx), fx_cur_base.get(fx)
        base_changed = vb is not None and cb is not None and vb != cb
        auto = cost_label(obj) == "auto"

        def magdur(e):
            mn = int(e.get("min_magnitude", 0)); mx = int(e.get("max_magnitude", 0))
            return (mn + mx) * max(int(e.get("duration", 0)), 1)

        def md_split(cur_e, van_e):
            """Return (mag_factor, dur_factor) strings or None if no vanilla."""
            if not van_e:
                return None
            vmn = int(van_e.get("min_magnitude", 0)) + int(van_e.get("max_magnitude", 0))
            cmn = int(cur_e.get("min_magnitude", 0)) + int(cur_e.get("max_magnitude", 0))
            vd = max(int(van_e.get("duration", 0)), 0)
            cd = int(cur_e.get("duration", 0))
            mf = (cmn / vmn) if vmn else 1.0
            df = (cd / vd) if vd else 1.0
            return mf, df

        md_changed = v0 is not None and eff_sig(e0) != eff_sig(v0)

        if fx in NO_SCALE:
            # No-scale: magnitude kept vanilla; base change rides on cost.
            tag = "[NO-SCALE]"
            if base_changed:
                notes.append(f"{tag} magnitude kept vanilla; base {vb}->{cb}, cost absorbs it")
            else:
                notes.append(f"{tag} magnitude kept vanilla (rounding only)")
        elif base_changed:
            bf = cb / vb
            # Did effective cost (mag*dur*base) stay, drop, or rise?
            if v0 is not None:
                vmd, cmd = magdur(v0), magdur(e0)
                eff_v = vmd * vb
                eff_c = cmd * cb
                sp = md_split(e0, v0)
                split = ""
                if sp:
                    mf, df = sp
                    bits = []
                    if abs(mf - 1) > 0.01:
                        bits.append(f"mag {ratio_word(mf)}")
                    if abs(df - 1) > 0.01:
                        bits.append(f"dur {ratio_word(df)}")
                    split = (" via " + " & ".join(bits)) if bits else " (mag/dur unchanged)"
                if eff_v == 0:
                    notes.append(f"base {ratio_word(bf)}{split}")
                else:
                    r = eff_c / eff_v
                    if 0.85 <= r <= 1.18:
                        notes.append(f"[COMPENSATED] base {ratio_word(bf)}{split}; effective cost kept ~same")
                    elif r < 0.85:
                        notes.append(f"[COST REDUCED] base {ratio_word(bf)}{split}; effective cost {ratio_word(r)} (intended cheaper)")
                    else:
                        notes.append(f"[COST RAISED] base {ratio_word(bf)}{split}; effective cost {ratio_word(r)} (intended pricier)")
            else:
                notes.append(f"base {ratio_word(bf)} changed")
        elif md_changed:
            # No base-cost change — pure rebalance of mag/dur.
            sp = md_split(e0, v0)
            bits = []
            if sp:
                mf, df = sp
                if abs(mf - 1) > 0.01:
                    bits.append(f"mag {ratio_word(mf)}")
                if abs(df - 1) > 0.01:
                    bits.append(f"dur {ratio_word(df)}")
            notes.append("[RESCALED] " + (", ".join(bits) if bits else "magnitude/duration") +
                         " (no base-cost change)")

        if auto and not any(n.startswith("[NO-SCALE]") for n in notes):
            notes.append("auto-calc cost")

        # Rounding note (first offending ranged magnitude).
        for e in effs:
            mn, mx = int(e.get("min_magnitude", 0)), int(e.get("max_magnitude", 0))
            if mn != mx and any(v != 1 and v % 5 != 0 for v in (mn, mx)):
                notes.append(f"[ROUNDING] {mn}-{mx} has a non-1/5 value")
                break

        # Rename note.
        vn = (van or {}).get("name") if van else None
        if vn and vn != (obj.get("name") or ""):
            notes.append("renamed")

        # Cost-only change.
        if not notes:
            if cost_label(obj) != cost_label(van):
                notes.append("cost recomputed")
            else:
                notes.append("changed")
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

    # Bucket CHANGED spells only, by school -> effect.
    groups: dict[str, dict[str, list]] = {}
    changed_count = 0
    for o in spells:
        van = van_by_id.get((o.get("id") or "").lower().strip())
        if not changed(o, van):
            continue
        changed_count += 1
        effs = o.get("effects") or []
        if not effs:
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

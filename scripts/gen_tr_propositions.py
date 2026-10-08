#!/usr/bin/env python3
"""Generate docs/TR-Spells-Propositions.md — the player-buyable Tamriel Rebuilt
/ Tamriel Data spells that are NOT yet in R3 - Spells.json and that need
rebalancing before import (Recalc = Yes or Cost only in
docs/TR-Buyable-Spells.md).

Same layout/format as docs/Spells-Explained.md (school -> effect -> rows), but
every row shows the TR spell's CURRENT values plus a `PROPOSE:` note giving the
values and cost it should take if imported, computed per
docs/Spell-Rules-Reference.md. Import-as-is spells (Recalc = -) are omitted.

This is a SEPARATE document; it does not touch R3 - Spells.md, Spells-Explained.md
or any generator wiring (not in gen_all.py). Read-only on the data.
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
COL_NOTE = 150          # PROPOSE column
EFFECT_INDENT = "    "
DIVIDER = "-" * 60

MASTER_FILES = gc.MASTER_FILES
NO_SCALE = {"FireDamage", "FrostDamage", "ShockDamage", "Poison"}

TR_BUYABLE_DOC = "docs/TR-Buyable-Spells.md"
# Recalc flag -> consideration tag shown on the proposition note.
RECALC_TAG = {"Yes": "recalc", "Cost only": "cost-only", "-": "as-is"}


def is_td(obj: dict) -> bool:
    return (obj.get("id") or "").startswith("T_")


def cost_label(obj: dict | None):
    if not obj:
        return None
    d = obj.get("data") or {}
    if "AUTO_CALCULATE" in (d.get("flags") or ""):
        return "auto"
    return d.get("cost")


def parse_new_tr_ids(path: str) -> dict[str, str]:
    """Parse docs/TR-Buyable-Spells.md and return {id_lower: recalc_flag} for the
    NEW buyable spells that NEED rebalancing, i.e. the rows whose `In R3` cell is
    '-' AND whose `Recalc` flag is `Yes` (compensation) or `Cost only`.

    The "import as-is" category (`Recalc = -`, no base-cost change) is omitted
    entirely: those spells have nothing to propose and would just be clutter.

    The main school tables have the column shape
    `| Spell | Mag | Dur | Cost | In R3 | Recalc | ID |`, which splits (with the
    leading/trailing pipe empties) into >= 9 cells where cells[5] is `In R3`,
    cells[6] is `Recalc`, cells[7] is the backticked id. We only capture rows
    whose cells[5] == '-'. The "Missing Spells to Consider" table has a cost
    number (not '-') in cells[5], and the Appendix rows carry no backtick, so
    both are naturally excluded.
    """
    bt = chr(96)  # backtick
    out: dict[str, str] = {}
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            s = ln.strip()
            if not s.startswith("|") or bt not in s:
                continue
            cells = [c.strip() for c in s.split("|")]
            if len(cells) < 9:
                continue
            if cells[5] != "-":
                continue
            recalc = cells[6]
            if recalc not in ("Yes", "Cost only"):   # drop import-as-is spells
                continue
            rid = cells[7].strip(bt).lower().strip()
            if rid:
                out[rid] = recalc
    return out


def round_mag(v: float) -> int:
    """Round a ranged magnitude end to the legal set: 1 or a multiple of 5.
    Never returns 2/3/4/6/7..."""
    r = int(round(v / 5.0)) * 5
    if r < 5:
        return 1 if v < 2.5 else 5
    return r


def effect_cost(eff: dict, base: float) -> float:
    """Per-effect cost: (min+max)*dur*(base/40) + area*(base/40), *1.5 OnTarget."""
    if base is None:
        base = 0
    mn = int(eff.get("min_magnitude", 0))
    mx = int(eff.get("max_magnitude", 0))
    dur = int(eff.get("duration", 0))
    area = int(eff.get("area", 0))
    c = (mn + mx) * dur * (base / 40.0) + area * (base / 40.0)
    if eff.get("range") == "OnTarget":
        c *= 1.5
    return c


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


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate the TR propositions doc.")
    ap.add_argument("--json", default="R3 - Spells.json")
    ap.add_argument("--out", default="docs/TR-Spells-Propositions.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    ap.add_argument("--tr-doc", default=TR_BUYABLE_DOC)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    r3_spells = [o for o in data if o.get("type") == "Spell"]
    r3_ids = {o["id"].lower().strip() for o in r3_spells if o.get("id")}

    # Current base costs + schools from this ESP's MagicEffect records.
    fx_cur_base: dict[str, float] = {}
    fx_school: dict[str, str] = {}
    for o in data:
        if o.get("type") == "MagicEffect" and o.get("effect_id"):
            d = o.get("data") or {}
            fx_cur_base[o["effect_id"]] = d.get("base_cost")
            fx_school[o["effect_id"]] = d.get("school")

    # NEW buyable TR spells that need rebalancing: ids with `In R3 = -` and a
    # Recalc flag of Yes / Cost only. Never duplicate an In R3 = Y spell.
    new_flags = parse_new_tr_ids(args.tr_doc) if os.path.exists(args.tr_doc) else {}
    new_needed = set(new_flags) - r3_ids
    new_by_id: dict[str, dict] = {}

    # Resolve the NEW spell records + vanilla base costs + effect names from the
    # masters (first master wins), streaming the big landmass files.
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
                continue
            k = rid.lower().strip()
            if o.get("type") == "Spell" and k in new_needed and k not in new_by_id:
                new_by_id[k] = o

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

    def spell_cost(obj: dict) -> float:
        """Sum effect_cost over all effects using current base (fallback vanilla)."""
        total = 0.0
        for e in obj.get("effects") or []:
            fx = e.get("magic_effect", "") or ""
            cb = fx_cur_base.get(fx)
            vb = fx_van_base.get(fx)
            base = cb if cb is not None else (vb if vb is not None else 0)
            total += effect_cost(e, base)
        return total

    def propose_note(obj: dict, recalc_flag: str) -> str:
        """Build the 'PROPOSE: ...' note for a NEW buyable spell, per
        docs/Spell-Rules-Reference.md. Operates on the first (dominant) effect for
        the mag/dur proposition; cost always sums all effects."""
        effs = obj.get("effects") or []
        e0 = effs[0] if effs else {}
        fx = e0.get("magic_effect", "") or ""
        vb = fx_van_base.get(fx)
        cb = fx_cur_base.get(fx)
        if cb is None:                      # effect untouched by the mod
            cb = vb
        base_changed = (vb is not None and cb is not None and vb != cb)

        # A local copy of the first effect that may be rescaled for the proposal,
        # then rendered through the shared value formatter.
        prop = dict(e0)

        def render_vals(d: dict) -> str:
            return gc.format_effect_values(d)

        extra = f" +{len(effs) - 1} effects" if len(effs) > 1 else ""
        tag = f" [{RECALC_TAG.get(recalc_flag, 'as-is')}]"

        if fx in NO_SCALE:
            # Keep vanilla mag/dur; base change rides on cost only.
            cost = spell_cost(obj)
            note = f"PROPOSE: keep mag/dur, cost -> {cost:g} (no-scale)"
            mn, mx = int(e0.get("min_magnitude", 0)), int(e0.get("max_magnitude", 0))
            if mn != mx and any(v != 1 and v % 5 != 0 for v in (mn, mx)):
                note += f" round {round_mag(mn)}-{round_mag(mx)}"
            return note + extra + tag

        if base_changed:
            X = vb / cb                     # mag*dur must move by this factor
            mn, mx = int(e0.get("min_magnitude", 0)), int(e0.get("max_magnitude", 0))
            dur = int(e0.get("duration", 0))
            uses_dur = gc.effect_uses_duration(fx)
            if uses_dur and dur > 0:
                # Default split: put the whole factor on duration (exempt from
                # rounding), magnitude held. Keeps magnitudes legal by construction.
                prop["duration"] = max(1, int(round(dur * X)))
                split_desc = f"dur {nice(X)}"
            else:
                # Magnitude-only (or dur==0): scale the ranged magnitude, round.
                prop["min_magnitude"] = round_mag(mn * X)
                prop["max_magnitude"] = round_mag(mx * X)
                split_desc = f"mag {nice(X)}"
            prop_obj = dict(obj)
            prop_obj["effects"] = [prop] + list(effs[1:])
            cost = spell_cost(prop_obj)
            note = (f"PROPOSE: {split_desc} (base {nice(cb / vb)} compensation) "
                    f"-> {render_vals(prop)}, cost {cost:g}")
            return note + extra + tag

        # No base-cost change: import as-is. Confirm cost.
        cost = spell_cost(obj)
        stored = cost_label(obj)
        if isinstance(stored, (int, float)) and abs(stored - cost) < 0.5:
            note = f"PROPOSE: import as-is (no base-cost change), cost ok"
        else:
            note = f"PROPOSE: import as-is (no base-cost change), cost {cost:g}"
        return note + extra + tag

    def emit_record(obj: dict, recalc_flag: str) -> list[str]:
        effs = obj.get("effects") or []
        rows = [gc.format_effect_values(effs[i]) for i in range(len(effs))]
        cur_name = obj.get("name") or "(unnamed)"
        name_seg = f"{cur_name} [NEW]"
        note = propose_note(obj, recalc_flag)
        id_col = obj.get("id") or ""

        if len(rows) <= 1:
            vals = rows[0] if rows else ""
            line = gc.add_at_column(id_col, COL_VALUES, vals)
            line = gc.add_at_column(line, COL_ID, name_seg)
            line = gc.add_at_column(line, COL_NOTE, note)
            return [line]

        first = gc.add_at_column(id_col, COL_VALUES, "")
        first = gc.add_at_column(first, COL_ID, name_seg)
        first = gc.add_at_column(first, COL_NOTE, note)
        lines = [first]
        for i, r in enumerate(rows):
            label = f"{EFFECT_INDENT}{effect_display_name(effs[i])}"
            lines.append(gc.add_at_column(label, COL_VALUES, r))
        return lines

    def sort_key(obj: dict):
        ve = obj.get("effects") or []
        if not ve:
            return (1, 0, 0, obj.get("name", ""))
        e0 = ve[0]
        fx = e0.get("magic_effect", "") or ""
        mn, mx = int(e0.get("min_magnitude", 0)), int(e0.get("max_magnitude", 0))
        dur = int(e0.get("duration", 0))
        if gc.effect_uses_magnitude(fx):
            return (0, mn, mx, obj.get("name", ""))
        return (0, dur, dur, obj.get("name", ""))

    # Bucket NEW spells by school -> effect.
    # Entries are 2-tuples (obj, recalc_flag).
    groups: dict[str, dict[str, list]] = {}
    new_count = 0
    recalc_count = 0
    costonly_count = 0
    for k, o in new_by_id.items():
        if k in r3_ids:                      # defensive: never duplicate In R3 = Y
            continue
        effs = o.get("effects") or []
        if not effs:
            continue
        fx = effs[0].get("magic_effect")
        school = fx_school.get(fx) or "Misc"
        flag = new_flags.get(k, "-")
        groups.setdefault(school, {}).setdefault(fx, []).append((o, flag))
        new_count += 1
        if flag == "Yes":
            recalc_count += 1
        elif flag == "Cost only":
            costonly_count += 1

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - TR Buyable Spells (Propositions)")
    out.append("")
    out.append("Player-buyable Tamriel Rebuilt / Tamriel Data spells that are NOT yet in")
    out.append("`R3 - Spells.json` and that need rebalancing before import (`Recalc = Yes`")
    out.append("= a scalable effect's base cost changed, or `Cost only` = a no-scale")
    out.append("effect needs a cost/rounding fix). Import-as-is spells (`Recalc = -`) are")
    out.append("omitted. Each row shows the TR spell's current values and a `PROPOSE:`")
    out.append("note giving the values and cost it should take if imported, computed per")
    out.append("`docs/Spell-Rules-Reference.md`. Same layout as `docs/Spells-Explained.md`.")
    out.append("Source list: `docs/TR-Buyable-Spells.md`. Do not hand-edit; regenerate")
    out.append("with `python scripts/gen_tr_propositions.py`.")
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
                for o, flag in sorted(items, key=lambda t: sort_key(t[0])):
                    out.extend(emit_record(o, flag))
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

    unresolved = sorted(new_needed - set(new_by_id))
    print(f"Wrote {args.out}")
    print(f"  NEW TR spells: {new_count}")
    print(f"    recalc (Yes):   {recalc_count}")
    print(f"    cost-only:      {costonly_count}")
    print(f"  NEW ids unresolved: {len(unresolved)}")
    if unresolved:
        for u in unresolved:
            print(f"    - {u}")
    print(f"  schools: {len(groups)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

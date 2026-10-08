#!/usr/bin/env python3
"""Generate the "Potions" README purely from JSON.

The layout spec is baked into this script; it does NOT read the existing README.

Sources
-------
- ESP JSON (R3 - Potions.json)   : current Alchemy values, IDs, records changed.
- Spells JSON (R3 - Spells.json) : MagicEffect metadata (school + base_cost).
  MagicEffect records live in the Spells plugin after the Spells/Potions split,
  so the per-effect "Base Cost" line and the "## <School>" bucket are sourced
  from there (NOT from the Potions file, which has no MagicEffect records).
- Master JSONs (tes3conv folder) : vanilla values (matched by id), vanilla
  MagicEffect base costs, and sEffect* GMSTs for effect display names.

Master lookup order (first hit wins):
    Morrowind -> Tribunal -> Bloodmoon -> Patch for Purists
    -> Tamriel_Data -> TR_Mainland -> Sky_Main -> Cyr_Main

Output structure
----------------
    # Title
    ## <School>                         one per magic-effect school
      ### <Effect>                      one per effect used by single-effect records
        Base Cost                       vanilla base_cost -> current (overridden effects only)
        *Potions*                       single-effect Alchemy, non-TD
        *Potions - Tamriel Data*        single-effect Alchemy, id starts T_
    ## Multi-Effect Potions             every potion with 2+ effects

Effects with no MagicEffect override in R3 - Spells.json have no fx_meta entry,
so (as in the combined README) they bucket under school "Misc" and emit no
"Base Cost" line.

Line format matches gen_readme.py (name col, values col 44, id col 80).
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
EFFECT_INDENT = "    "  # indent before "effect N" rows on multi-effect records
DIVIDER = "-" * 60

MASTER_FILES = [
    "Morrowind.json",
    "Tribunal.json",
    "Bloodmoon.json",
    "Patch for Purists.json",
    "Tamriel_Data.json",
    "TR_Mainland.json",
    "Sky_Main.json",
    "Cyr_Main.json",
]

# Files at/above this size are read with the streaming decoder.
STREAM_THRESHOLD = 50 * 1024 * 1024  # 50 MB


# ---------------------------------------------------------------------------
# Formatting helpers (mirrors gen_readme.py)
# ---------------------------------------------------------------------------
def fmt_num(v) -> str:
    return str(v)


def add_at_column(base: str, col: int, segment: str) -> str:
    if not segment:
        return base
    if len(base) < col:
        base += " " * (col - len(base))
    else:
        base += " "
    return base + segment


RANGE_LABEL = {"OnTouch": "Touch", "OnTarget": "Target", "OnSelf": "Self"}


def format_effect(eff: dict, show_area: bool = True, show_range: bool = True) -> str:
    area = int(eff.get("area", 0))
    v = gc.format_effect_values(eff)
    if show_area and area > 0:
        v = f"{v}/{area}ft"
    if show_range:
        label = RANGE_LABEL.get(eff.get("range", ""), eff.get("range", ""))
        if label:
            v = f"{v}/{label}"
    return v


def format_effect_pair(eff: dict, van_eff: dict | None) -> str:
    cur_area = int(eff.get("area", 0))
    van_area = int(van_eff.get("area", 0)) if van_eff is not None else None
    area_changed = van_area is not None and van_area != cur_area
    show_area = area_changed if van_eff is not None else cur_area > 0

    cur_range = eff.get("range", "")
    van_range = van_eff.get("range", "") if van_eff is not None else None
    range_changed = van_range is not None and van_range != cur_range
    show_range = range_changed if van_eff is not None else False

    cur = format_effect(eff, show_area=show_area, show_range=show_range)
    van = (format_effect(van_eff, show_area=show_area, show_range=show_range)
           if van_eff is not None else None)
    if van is not None and van != cur:
        return f"{van} -> {cur}"
    return cur


def format_value_rows(obj: dict, vanilla: dict | None) -> list[str]:
    effects = obj.get("effects") or []
    van_effects = (vanilla or {}).get("effects") or []
    rows = []
    for i, eff in enumerate(effects):
        van_eff = van_effects[i] if i < len(van_effects) else None
        rows.append(format_effect_pair(eff, van_eff))
    return rows


def is_td(obj: dict) -> bool:
    rid = obj.get("id") or ""
    return rid.startswith("T_")


# ---------------------------------------------------------------------------
# Streaming reader for large master files.
# ---------------------------------------------------------------------------
def iter_json_array(path: str):
    decoder = json.JSONDecoder()
    with open(path, "r", encoding="utf-8") as f:
        buf = f.read()
    i = 0
    n = len(buf)
    while i < n and buf[i] in " \t\r\n":
        i += 1
    if i < n and buf[i] == "[":
        i += 1
    while i < n:
        while i < n and buf[i] in " \t\r\n,":
            i += 1
        if i >= n or buf[i] == "]":
            break
        obj, end = decoder.raw_decode(buf, i)
        yield obj
        i = end


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="Generate Potions README from JSON.")
    ap.add_argument("--json", default="R3 - Potions.json",
                    help="Potions ESP JSON path.")
    ap.add_argument("--out", default="R3 - Potions.md",
                    help="Output README path.")
    ap.add_argument("--spells-json", default="R3 - Spells.json",
                    help="Spells ESP JSON holding MagicEffect metadata "
                         "(school + base_cost).")
    ap.add_argument("--master-dir", default="C:/OMEN/Morrowind/tes3conv",
                    help="Directory holding the master JSONs.")
    args = ap.parse_args()

    if not os.path.exists(args.json):
        print(f"ESP JSON not found: {args.json}", file=sys.stderr)
        return 1

    print(f"Loading ESP JSON: {args.json}")
    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # MagicEffect metadata from the Spells ESP: effect_id -> {school, base_cost}.
    # MagicEffect records moved to R3 - Spells.json in the split, so the potions
    # README's "## <School>" headers and per-effect "Base Cost" lines are
    # sourced from there. Effects with no override have no entry here (as in the
    # combined README) and fall back to school "Misc" with no Base Cost line.
    fx_meta: dict[str, dict] = {}
    if os.path.exists(args.spells_json):
        print(f"Loading MagicEffect metadata: {args.spells_json}")
        with open(args.spells_json, "r", encoding="utf-8") as f:
            spells_data = json.load(f)
        for o in spells_data:
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                fx_meta[o["effect_id"]] = {
                    "school": (o.get("data") or {}).get("school") or "Misc",
                    "base_cost": (o.get("data") or {}).get("base_cost"),
                }
    else:
        print(f"  (warning) spells JSON not found: {args.spells_json}",
              file=sys.stderr)

    # Collect the ids we need vanilla data for: Alchemy ids.
    needed_ids: set[str] = set()
    for o in data:
        if o.get("type") == "Alchemy" and o.get("id"):
            needed_ids.add(o["id"].lower().strip())

    # Load vanilla records from masters (in order, first hit wins). We also read
    # vanilla MagicEffect base costs (for the "vanilla -> current" Base Cost
    # line) and sEffect* GMSTs (for effect display names).
    print(f"Loading masters from: {args.master_dir}")
    van_by_id: dict[str, dict] = {}
    fx_van_cost: dict[str, float] = {}
    effect_names: dict[str, str] = {}
    for name in MASTER_FILES:
        path = os.path.join(args.master_dir, name)
        if not os.path.exists(path):
            print(f"  (skip, not found) {name}")
            continue
        print(f"  reading {name}")
        size = os.path.getsize(path)
        records = iter_json_array(path) if size >= STREAM_THRESHOLD else json.load(open(path, "r", encoding="utf-8"))
        for o in records:
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                if o["effect_id"] not in fx_van_cost:
                    fx_van_cost[o["effect_id"]] = (o.get("data") or {}).get("base_cost")
                continue
            rid = o.get("id")
            if not rid:
                continue
            if o.get("type") == "GameSetting" and rid.startswith("sEffect"):
                key = rid[len("sEffect"):]
                if key not in effect_names:
                    val = (o.get("value") or {}).get("data")
                    if isinstance(val, str) and val:
                        effect_names[key] = val
            k = rid.lower().strip()
            if k in needed_ids and k not in van_by_id:
                van_by_id[k] = o

    def split_camel(s: str) -> str:
        out_chars = []
        for i, ch in enumerate(s):
            if i > 0 and ch.isupper() and not s[i - 1].isupper():
                out_chars.append(" ")
            out_chars.append(ch)
        return "".join(out_chars)

    def effect_display_name(eff: dict) -> str:
        fx = eff.get("magic_effect", "") or ""
        base = effect_names.get(fx, split_camel(fx))
        skill = eff.get("skill")
        attr = eff.get("attribute")
        target = None
        if skill and skill != "None":
            target = split_camel(skill)
        elif attr and attr != "None":
            target = split_camel(attr)
        return f"{base}: {target}" if target else base

    def emit_record(obj: dict) -> list[str]:
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        rows = format_value_rows(obj, van)

        cur_name = obj.get("name") or "(unnamed)"
        van_name = van.get("name") if van else None
        renamed = bool(van_name) and van_name != cur_name

        id_col = obj.get("id") or ""
        name_seg = f"{van_name} -> {cur_name}" if renamed else cur_name

        # Single-effect (or no effects): one line.
        if len(rows) <= 1:
            vals = rows[0] if rows else ""
            line = add_at_column(id_col, COL_VALUES, vals)
            line = add_at_column(line, COL_ID, name_seg)
            return [line]

        # Multi-effect: first row carries id and name; each effect its own row.
        lines = []
        first = add_at_column(id_col, COL_VALUES, "")
        first = add_at_column(first, COL_ID, name_seg)
        lines.append(first)
        effects = obj.get("effects") or []
        for i, r in enumerate(rows):
            fx_name = effect_display_name(effects[i]) if i < len(effects) else ""
            label = f"{EFFECT_INDENT}{fx_name}"
            lines.append(add_at_column(label, COL_VALUES, r))
        return lines

    def sort_key(obj: dict):
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        veffs = (van or {}).get("effects") or []
        if not veffs:
            return (1, 0, 0, 0, obj.get("name", ""))
        e0 = veffs[0]
        fx = e0.get("magic_effect", "") or ""
        mn = int(e0.get("min_magnitude", 0))
        mx = int(e0.get("max_magnitude", 0))
        dur = int(e0.get("duration", 0))
        if gc.effect_uses_magnitude(fx):
            return (0, mn, mx, dur, obj.get("name", ""))
        return (0, dur, dur, 0, obj.get("name", ""))

    # Bucket records (Alchemy only).
    groups: dict[str, dict[str, list]] = {}
    multi: list = []
    for o in data:
        if o.get("type") != "Alchemy":
            continue
        effects = o.get("effects") or []
        if not effects:
            continue
        if len(effects) > 1:
            multi.append(o)
            continue
        fx = effects[0].get("magic_effect")
        school = fx_meta.get(fx, {}).get("school", "Misc")
        groups.setdefault(school, {}).setdefault(fx, []).append(o)

    # Build output.
    out: list[str] = []

    def header(text: str) -> None:
        out.append(DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    out.append("# Remastered Rebalance Redux - Potions")
    out.append("")

    def effect_base_name(fx: str) -> str:
        return effect_names.get(fx, split_camel(fx))

    for school in sorted(groups):
        header(f"## {school}")
        for fx in sorted(groups[school], key=effect_base_name):
            recs = groups[school][fx]
            header(f"### {effect_base_name(fx)}")

            # Base Cost line only for effects that have a MagicEffect override
            # in R3 - Spells.json (matching the combined README's behavior: the
            # 20 effects with no override emit no Base Cost line).
            meta = fx_meta.get(fx)
            if meta:
                cur_cost = fmt_num(meta["base_cost"])
                van_cost = fx_van_cost.get(fx)
                van_cost = fmt_num(van_cost) if van_cost is not None else None
                cb = (f"{van_cost} -> {cur_cost}"
                      if van_cost is not None and van_cost != cur_cost
                      else cur_cost)
                out.append("```")
                out.append(add_at_column("Base Cost", COL_VALUES, cb))
                out.append("```")

            def block(title: str, items: list) -> None:
                if not items:
                    return
                out.append("")
                out.append(f"*{title}*")
                out.append("```")
                for r in sorted(items, key=sort_key):
                    out.extend(emit_record(r))
                out.append("```")

            block("Potions",
                  [r for r in recs if r.get("type") == "Alchemy" and not is_td(r)])
            block("Potions - Tamriel Data",
                  [r for r in recs if r.get("type") == "Alchemy" and is_td(r)])

            out.append("")

    if multi:
        header("## Multi-Effect Potions")

        def multi_block(title: str, items: list) -> None:
            if not items:
                return
            out.append(f"*{title}*")
            out.append("```")
            for r in sorted(items, key=sort_key):
                out.extend(emit_record(r))
            out.append("```")
            out.append("")

        multi_block("Potions",
                    [r for r in multi if r.get("type") == "Alchemy" and not is_td(r)])
        multi_block("Potions - Tamriel Data",
                    [r for r in multi if r.get("type") == "Alchemy" and is_td(r)])

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print()
    print(f"Wrote README to: {args.out}")
    print(f"  Schools        : {len(groups)}")
    print(f"  Multi-effect   : {len(multi)}")
    print(f"  Effects w/ cost: {sum(1 for s in groups for fx in groups[s] if fx_meta.get(fx))}")
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed_ids)} needed ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Generate the "Potions" README purely from JSON.

The layout spec is baked into this script; it does NOT read the existing README.

Sources
-------
- ESP JSON (R3 - Potions.json)   : current Alchemy values, IDs, records changed.
- Master JSONs (tes3conv folder) : vanilla values (matched by id), MagicEffect
  SCHOOL (for the "## <School>" header), and sEffect* GMSTs for effect display
  names.

The Potions README shows NO "Base Cost" line (R3 - Potions.json contains no
MagicEffect records; base-cost changes live in R3 - Spells.md). It does show an
always-present per-effect "Tier" line derived from the effect's R3 base cost,
read from R3 - Spells.json (--spells-json). Each effect's school and display name
come from the vanilla masters (read-only).

Master lookup order (first hit wins):
    Morrowind -> Tribunal -> Bloodmoon -> Patch for Purists
    -> Tamriel_Data -> TR_Mainland -> Sky_Main -> Cyr_Main

Output structure
----------------
    # Title
    ## <School>                         one per magic-effect school
      ### <Effect>                      one per effect used by single-effect records
        Tier                            always-present tier column from base cost
        *Vanilla*                       single-effect Alchemy, non-TD
        *Tamriel Data*                  single-effect Alchemy, id starts T_
    ## Multi-Effect Potions             every potion with 2+ effects

Line format matches gen_spells.py (name col, values col 44, id col 80).
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


# ---------------------------------------------------------------------------
# Potion Tier column from an effect's R3 base cost.
# Geometric-midpoint half-open ranges (see context.json tier_boundaries).
# Duration-only effects divide the base cost by 40 first.
# ---------------------------------------------------------------------------
def tier_column(base_cost: float, uses_magnitude: bool) -> str:
    v = base_cost if uses_magnitude else base_cost / 40.0
    if v >= 6.32:
        col = 8
    elif v >= 3.16:
        col = 5
    elif v >= 1.41:
        col = 2
    elif v >= 0.71:
        col = 1
    elif v >= 0.32:
        col = 0.5
    elif v >= 0.14:
        col = 0.2
    else:
        col = 0.1
    return {8: "8", 5: "5", 2: "2", 1: "1", 0.5: "0.5", 0.2: "0.2", 0.1: "0.1"}[col]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="Generate Potions README from JSON.")
    ap.add_argument("--json", default="R3 - Potions.json",
                    help="Potions ESP JSON path.")
    ap.add_argument("--out", default="R3 - Potions.md",
                    help="Output README path.")
    ap.add_argument("--master-dir", default="C:/OMEN/Morrowind/tes3conv",
                    help="Directory holding the master JSONs.")
    ap.add_argument("--spells-json", default="R3 - Spells.json",
                    help="Spells ESP JSON path (source of MagicEffect base costs "
                         "used for the per-effect Tier line).")
    args = ap.parse_args()

    if not os.path.exists(args.json):
        print(f"ESP JSON not found: {args.json}", file=sys.stderr)
        return 1

    print(f"Loading ESP JSON: {args.json}")
    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # R3 base cost per effect, from the Spells ESP JSON (MagicEffect records).
    # Used for the always-present Tier line on each "### <Effect>" subsection.
    fx_base_cost: dict[str, float] = {}
    if os.path.exists(args.spells_json):
        print(f"Loading spells JSON: {args.spells_json}")
        for o in gc.read_records(args.spells_json):
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                cost = (o.get("data") or {}).get("base_cost")
                if cost is not None and o["effect_id"] not in fx_base_cost:
                    fx_base_cost[o["effect_id"]] = cost
    else:
        print(f"  (skip, not found) {args.spells_json}", file=sys.stderr)

    # Collect the ids we need vanilla data for: Alchemy ids.
    needed_ids: set[str] = set()
    for o in data:
        if o.get("type") == "Alchemy" and o.get("id"):
            needed_ids.add(o["id"].lower().strip())

    # Load vanilla records from masters (in order, first hit wins). We read:
    #  - vanilla Alchemy records (for the "vanilla -> current" value diffs),
    #  - MagicEffect SCHOOL (effect_id -> school) for the "## <School>" header,
    #  - sEffect* GMSTs (effect_id -> display name) for the "### <Effect>" header.
    # No base cost is read: the Potions README has no Base Cost line (MagicEffect
    # records live in R3 - Spells.json, not here).
    print(f"Loading masters from: {args.master_dir}")
    van_by_id: dict[str, dict] = {}
    fx_school: dict[str, str] = {}
    fx_van_cost: dict[str, float] = {}  # vanilla base cost, Tier fallback
    effect_names: dict[str, str] = {}
    for name in MASTER_FILES:
        path = os.path.join(args.master_dir, name)
        if not os.path.exists(path):
            print(f"  (skip, not found) {name}")
            continue
        print(f"  reading {name}")
        for o in gc.read_records(path):
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                if o["effect_id"] not in fx_school:
                    sch = (o.get("data") or {}).get("school")
                    if sch:
                        fx_school[o["effect_id"]] = sch
                if o["effect_id"] not in fx_van_cost:
                    cost = (o.get("data") or {}).get("base_cost")
                    if cost is not None:
                        fx_van_cost[o["effect_id"]] = cost
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

    def school_of(fx: str) -> str:
        """School for an effect: vanilla master MagicEffect school first, else
        'Misc' as a last resort (mirrors gen_spells.py; potions carry no ESP
        MagicEffect metadata so there is no fx_meta layer)."""
        return fx_school.get(fx) or "Misc"

    def tier_label(fx: str) -> str | None:
        """Tier column string for an effect from its R3 base cost (fallback to
        the vanilla master base cost). Duration-only effects divide by 40 first.
        Returns None when no base cost is available anywhere."""
        cost = fx_base_cost.get(fx)
        if cost is None:
            cost = fx_van_cost.get(fx)
        if cost is None:
            return None
        return tier_column(cost, gc.effect_uses_magnitude(fx))

    def emit_record(obj: dict) -> list[str]:
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        rows = gc.format_value_rows(obj, van)

        cur_name = obj.get("name") or "(unnamed)"
        van_name = van.get("name") if van else None
        renamed = bool(van_name) and van_name != cur_name

        id_col = obj.get("id") or ""
        name_seg = f"{van_name} -> {cur_name}" if renamed else cur_name

        # Single-effect (or no effects): one line.
        if len(rows) <= 1:
            vals = rows[0] if rows else ""
            line = gc.add_at_column(id_col, COL_VALUES, vals)
            line = gc.add_at_column(line, COL_ID, name_seg)
            return [line]

        # Multi-effect: first row carries id and name; each effect its own row.
        lines = []
        first = gc.add_at_column(id_col, COL_VALUES, "")
        first = gc.add_at_column(first, COL_ID, name_seg)
        lines.append(first)
        effects = obj.get("effects") or []
        for i, r in enumerate(rows):
            fx_name = effect_display_name(effects[i]) if i < len(effects) else ""
            label = f"{EFFECT_INDENT}{fx_name}"
            lines.append(gc.add_at_column(label, COL_VALUES, r))
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
        school = school_of(fx)
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

            # Always-present Tier line (same position spells uses for Base Cost).
            tier = tier_label(fx)
            if tier is not None:
                out.append("```")
                out.append(gc.add_at_column("Tier", COL_VALUES, tier))
                out.append("```")

            def block(title: str | None, items: list) -> None:
                if not items:
                    return
                # Exactly one blank line before each block.
                if out and out[-1] != "":
                    out.append("")
                if title:
                    out.append(f"*{title}*")
                out.append("```")
                for r in sorted(items, key=sort_key):
                    out.extend(emit_record(r))
                out.append("```")

            # Vanilla records: "Vanilla" label. TD records: "Tamriel Data" label.
            block("Vanilla",
                  [r for r in recs if r.get("type") == "Alchemy" and not gc.is_td(r)])
            block("Tamriel Data",
                  [r for r in recs if r.get("type") == "Alchemy" and gc.is_td(r)])

            out.append("")

    if multi:
        header("## Multi-Effect Potions")

        def multi_block(title: str | None, items: list) -> None:
            if not items:
                return
            if title:
                out.append(f"*{title}*")
            out.append("```")
            for r in sorted(items, key=sort_key):
                out.extend(emit_record(r))
            out.append("```")
            out.append("")

        multi_block("Vanilla",
                    [r for r in multi if r.get("type") == "Alchemy" and not gc.is_td(r)])
        multi_block("Tamriel Data",
                    [r for r in multi if r.get("type") == "Alchemy" and gc.is_td(r)])

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
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed_ids)} needed ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())

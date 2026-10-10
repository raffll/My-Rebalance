#!/usr/bin/env python3
"""Enchantments README generator.

Enchanting records have no name field, so display names are mapped from the id:
first from the item/scroll names that carry the enchant (item_names), falling
back to a baked-in table (NAME_MAP).

Layout mirrors Spells & Potions:
    ## <School>                         one per magic-effect school
      ### <Effect>                      one per effect used by single-effect records
        *Vanilla*                       single-effect Enchanting, non-TD
        *Tamriel Data*                  single-effect Enchanting, id starts T_
    ## Multi-Effect Enchantments        every enchant with 2+ effects, once

There is NO Base Cost / Tier line. Line: id (col 0) - vanilla -> current
(col 44) - name (col 80). Output: R3 - Enchantments.md
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

# Enchanting id -> display name (names are not stored on Enchanting records).
NAME_MAP = {
    "black_jinx_en_unique": "Black Jinx",
    "bm_hunterspear": "Spear of the Hunter",
    "Crescent Moon": "Daedric Crescent",
    "feather_en": "Feather Belt",
    "saint's shield_en": "Saint's Shield",
    "sc_balefulsuffering_en": "Scroll of Baleful Suffering",
    "sc_blackstorm_en": "Scroll of The Black Storm",
    "sc_didalasknack_en": "Scroll of Didala's Knack",
    "sc_fadersleadenflesh_en": "Scroll of Fader's Leaden Flesh",
    "sc_FiercelyRoastThyEnemy_en": "Scroll of Fiercely Roasting",
    "sc_hellfire_en": "Scroll of Hellfire",
    "sc_mageseye_en": "Scroll of The Mage's Eye",
    "sc_reynosbeastfinder_en": "Scroll of Reynos' Beast Finder",
    "sc_tevralshawkshaw_en": "Scroll of Tevral's Hawkshaw",
    "sc_ulmjuicedasfeather_en": "Scroll of Ulm Juiceda's Feather",
    "sc_vaerminaspromise_en": "Scroll of Vaermina's Promise",
    "T_Once_BurdenTouch30-35": "Scroll of Makkun's Heavy Hand",
    "T_Once_FallingBarrier": "Scroll of The Falling Barrier",
    "ulms juicedaw's feather_en": "Juicedaw Feather Ring",
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Enchantments README generator.")
    ap.add_argument("--json", default="R3 - Enchantments.json")
    ap.add_argument("--out", default="R3 - Enchantments.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    ench = [o for o in data if o.get("type") == "Enchanting"]
    needed = {o["id"].lower().strip() for o in ench if o.get("id")}

    # Load vanilla records, MagicEffect SCHOOL (effect_id -> school) for the
    # "## <School>" header, and sEffect* GMSTs (effect display names). We scan
    # the masters once here (gc.load_vanilla does not return schools).
    print(f"Loading masters from: {args.master_dir}")
    van_by_id: dict[str, dict] = {}
    fx_school: dict[str, str] = {}
    effect_names: dict[str, str] = {}
    # enchant_id (lower) -> ordered unique list of item names that carry it.
    item_names: dict[str, list] = {}
    for mname in gc.MASTER_FILES:
        mpath = os.path.join(args.master_dir, mname)
        if not os.path.exists(mpath):
            print(f"  (skip, not found) {mname}")
            continue
        print(f"  reading {mname}")
        for o in gc.read_records(mpath):
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                if o["effect_id"] not in fx_school:
                    sch = (o.get("data") or {}).get("school")
                    if sch:
                        fx_school[o["effect_id"]] = sch
                continue
            rid = o.get("id")
            # sEffect<Name> GMSTs hold the in-game display name of each effect.
            if o.get("type") == "GameSetting" and isinstance(rid, str) \
                    and rid.startswith("sEffect"):
                key = rid[len("sEffect"):]
                if key not in effect_names:
                    val = (o.get("value") or {}).get("data")
                    if isinstance(val, str) and val:
                        effect_names[key] = val
            # Items/scrolls carrying one of our enchants supply its display name.
            en = o.get("enchanting")
            if en:
                k = en.lower().strip()
                if k in needed:
                    name = (o.get("name") or "").strip()
                    if name:
                        lst = item_names.setdefault(k, [])
                        if name not in lst:
                            lst.append(name)
            if not rid:
                continue
            k = rid.lower().strip()
            if k in needed and k not in van_by_id:
                van_by_id[k] = o

    def effect_display(fx):
        return effect_names.get(fx, gc.split_camel(fx))

    def display_name(idv):
        names = item_names.get((idv or "").lower().strip())
        if names:
            return ", ".join(names)
        return NAME_MAP.get(idv) or NAME_MAP.get((idv or "").lower()) or idv

    def school_of(fx: str) -> str:
        """School for an effect: vanilla master MagicEffect school first, else
        'Misc' as a last resort (enchants carry no ESP MagicEffect metadata)."""
        return fx_school.get(fx) or "Misc"

    def emit_record(obj: dict) -> list[str]:
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        rows = gc.format_value_rows(obj, van)

        id_col = obj.get("id") or ""
        name_seg = display_name(id_col)

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
            fx_name = effect_display(effects[i].get("magic_effect", "")) if i < len(effects) else ""
            label = f"{EFFECT_INDENT}{fx_name}"
            lines.append(gc.add_at_column(label, COL_VALUES, r))
        return lines

    def sort_key(obj: dict):
        """Sort by the vanilla first-effect's min then max magnitude, duration
        as tiebreaker. Records with no vanilla counterpart sort last; name is
        the final tiebreaker."""
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        veffs = (van or {}).get("effects") or []
        if not veffs:
            return (1, 0, 0, 0, display_name(obj.get("id", "")))
        e0 = veffs[0]
        fx = e0.get("magic_effect", "") or ""
        mn = int(e0.get("min_magnitude", 0))
        mx = int(e0.get("max_magnitude", 0))
        dur = int(e0.get("duration", 0))
        if gc.effect_uses_magnitude(fx):
            return (0, mn, mx, dur, display_name(obj.get("id", "")))
        return (0, dur, dur, 0, display_name(obj.get("id", "")))

    # Bucket records: single-effect into groups[school][fx], 2+ effects into
    # a single `multi` list (listed once, not per effect).
    groups: dict[str, dict[str, list]] = {}
    multi: list = []
    for o in ench:
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

    out.append("# Remastered Rebalance Redux - Enchantments")
    out.append("")

    for school in sorted(groups):
        header(f"## {school}")
        for fx in sorted(groups[school], key=effect_display):
            recs = groups[school][fx]
            header(f"### {effect_display(fx)}")

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

            # Non-TD records: "Vanilla" label. TD records: "Tamriel Data" label.
            block("Vanilla", [r for r in recs if not gc.is_td(r)])
            block("Tamriel Data", [r for r in recs if gc.is_td(r)])

            out.append("")

    if multi:
        header("## Multi-Effect Enchantments")

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

        multi_block("Vanilla", [r for r in multi if not gc.is_td(r)])
        multi_block("Tamriel Data", [r for r in multi if gc.is_td(r)])

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  Enchantments: {len(ench)}  schools: {len(groups)}  multi-effect: {len(multi)}")
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

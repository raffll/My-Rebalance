#!/usr/bin/env python3
"""Enchantments README generator.

Enchanting records have no name field, so display names are mapped from id via
a baked-in table (NAME_MAP). Records are grouped by effect: a multi-effect
enchantment appears once under each of its effects' sections, showing that
effect's value.

Layout matches Spells & Potions:
    ## <Effect>
      <non-TD enchantments>
      *Tamriel Data*  (id starts with T_)
Line: id (col 0) - vanilla -> current (col 44) - name (col 80)
Output: R3 - Enchantments.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

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


def is_td(idv: str) -> bool:
    return (idv or "").startswith("T_")


def _one(eff, show_area) -> str:
    area = int(eff.get("area", 0))
    # Shared axis-aware renderer so axis-only effects (Water Breathing, Silence,
    # Paralyze, Lock, Open...) render identically to spells/potions/core.
    v = gc.format_effect_values(eff)
    if show_area and area > 0:
        v = f"{v}/{area}ft"
    return v


def value_pair(eff, veff) -> str:
    """"vanilla -> current" for one effect; area shown only when it changed."""
    cur_area = int(eff.get("area", 0))
    van_area = int(veff.get("area", 0)) if veff is not None else None
    area_changed = van_area is not None and van_area != cur_area
    show_area = area_changed if veff is not None else cur_area > 0

    cur = _one(eff, show_area)
    van = _one(veff, show_area) if veff is not None else None
    return f"{van} -> {cur}" if van is not None and van != cur else cur


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
    van_by_id, effect_names = gc.load_vanilla(args.master_dir, needed, want_effect_names=True)

    # Build enchant_id (lower) -> ordered unique list of item names that carry
    # it, scanning masters in order (first occurrence wins the ordering).
    item_names: dict[str, list] = {}
    for mname in gc.MASTER_FILES:
        mpath = os.path.join(args.master_dir, mname)
        if not os.path.exists(mpath):
            continue
        for o in gc.read_records(mpath):
            if not isinstance(o, dict):
                continue
            en = o.get("enchanting")
            if not en:
                continue
            k = en.lower().strip()
            if k not in needed:
                continue
            name = (o.get("name") or "").strip()
            if not name:
                continue
            lst = item_names.setdefault(k, [])
            if name not in lst:
                lst.append(name)

    def effect_display(fx):
        return effect_names.get(fx, gc.split_camel(fx))

    def display_name(idv):
        names = item_names.get((idv or "").lower().strip())
        if names:
            return ", ".join(names)
        return NAME_MAP.get(idv) or NAME_MAP.get((idv or "").lower()) or idv

    # Build: effect_display_name -> list of (enchant, effect_index).
    sections: dict[str, list] = {}
    for o in ench:
        van = van_by_id.get((o.get("id") or "").lower().strip())
        veffs = (van or {}).get("effects") or []
        for i, eff in enumerate(o.get("effects") or []):
            fx = eff.get("magic_effect", "")
            name = effect_display(fx)
            sections.setdefault(name, []).append((o, i, veffs[i] if i < len(veffs) else None))

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Enchantments")
    out.append("")

    def header(text):
        out.append(gc.DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    def line_for(o, i, veff):
        eff = (o.get("effects") or [])[i]
        vb = value_pair(eff, veff)
        idv = o.get("id", "")
        line = gc.add_at_column(idv, gc.COL_VALUES, vb)
        return gc.add_at_column(line, gc.COL_ID, display_name(idv))

    def sort_key(t):
        """Sort by vanilla min magnitude, then max (ascending). Entries with no
        vanilla effect sort last; name is the final tiebreaker."""
        o, i, veff = t
        if veff is not None:
            return (0, int(veff.get("min_magnitude", 0)),
                    int(veff.get("max_magnitude", 0)), display_name(o.get("id", "")))
        return (1, 0, 0, display_name(o.get("id", "")))

    def block(items):
        if not items:
            return
        out.append("```")
        for (o, i, veff) in sorted(items, key=sort_key):
            out.append(line_for(o, i, veff))
        out.append("```")

    for effect_name in sorted(sections):
        items = sections[effect_name]
        header(f"## {effect_name}")
        non_td = [t for t in items if not is_td(t[0].get("id", ""))]
        td = [t for t in items if is_td(t[0].get("id", ""))]
        block(non_td)
        if td:
            if non_td:
                out.append("")
            out.append("*Tamriel Data*")
            block(td)
        out.append("")

    while out and out[-1] == "":
        out.pop()
    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  Enchantments: {len(ench)}  effect sections: {len(sections)}")
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

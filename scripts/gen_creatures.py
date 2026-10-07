#!/usr/bin/env python3
"""Creatures README generator.

The changed value for creatures is **magicka** (data.magicka). Creatures are
grouped by display name; each group is a section. Vanilla magicka comes from
the masters (matched by id).

Line: id (col 0) - vanilla -> current magicka (col 44) - name (col 80)
Output: R3 - Creatures.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc


def norm_name(name: str) -> str:
    """Collapse repeated whitespace (e.g. 'Frost  Atronach' -> 'Frost Atronach')."""
    return re.sub(r"\s+", " ", (name or "").strip())


def main() -> int:
    ap = argparse.ArgumentParser(description="Creatures README generator.")
    ap.add_argument("--json", default="R3 - Creatures.json")
    ap.add_argument("--out", default="R3 - Creatures.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    creatures = [o for o in data if o.get("type") == "Creature"]
    needed = {o["id"].lower().strip() for o in creatures if o.get("id")}
    van_by_id, _ = gc.load_vanilla(args.master_dir, needed)

    def van_magicka(idl):
        v = van_by_id.get(idl)
        return (v.get("data") or {}).get("magicka") if v else None

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Creatures")
    out.append("")
    out.append(gc.DIVIDER)
    out.append("")
    out.append("## Magicka")
    out.append("")
    out.append("```")
    for o in sorted(creatures, key=lambda x: x.get("id", "")):
        idl = (o.get("id") or "").lower().strip()
        cur = (o.get("data") or {}).get("magicka")
        vb = gc.arrow(van_magicka(idl), cur)
        line = gc.add_at_column(o.get("id", ""), gc.COL_VALUES, vb)
        line = gc.add_at_column(line, gc.COL_ID, norm_name(o.get("name")))
        out.append(line)
    out.append("```")
    out.append("")

    while out and out[-1] == "":
        out.pop()
    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  Creatures: {len(creatures)}")
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

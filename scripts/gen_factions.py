#!/usr/bin/env python3
"""Factions README generator.

The changed value per faction rank is the attribute requirement
(data.requirements[i].attributes[0]). Vanilla comes from the masters (matched
by faction id). One section per faction, ranks listed in order.

Layout (matches the hand-authored README): rank name in col 0, value in col 44.
    ## Attributes
    ### <Faction name>
      <rank name>    vanilla -> current
Output: R3 - Factions.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

# Faction display order, matching the hand-authored README.
FACTION_ORDER = [
    ("Mages Guild", "Mages Guild"),
    ("Fighters Guild", "Fighters Guild"),
    ("Hlaalu", "Great House Hlaalu"),
    ("Redoran", "Great House Redoran"),
    ("Telvanni", "Great House Telvanni"),
    ("Imperial Cult", "Imperial Cult"),
    ("Imperial Legion", "Imperial Legion"),
    ("Temple", "Temple"),
    ("Thieves Guild", "Thieves Guild"),
    ("Morag Tong", "Morag Tong"),
    ("East Empire Company", "East Empire Company"),
]


def rank_attr(req):
    """Attribute requirement for a rank = attributes[0] (both are equal)."""
    attrs = (req or {}).get("attributes") or []
    return attrs[0] if attrs else None


def main() -> int:
    ap = argparse.ArgumentParser(description="Factions README generator.")
    ap.add_argument("--json", default="R3 - Factions.json")
    ap.add_argument("--out", default="R3 - Factions.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    by_id = {o["id"].lower().strip(): o for o in data
             if o.get("type") == "Faction" and o.get("id")}
    needed = set(by_id.keys())
    # Faction ids collide with same-named Dialogue topics, so match on
    # (type, id) rather than id alone.
    van_typed, _ = gc.load_vanilla_typed(args.master_dir, {"Faction"}, set())
    van_by_id = {k: v for (t, k), v in van_typed.items() if t == "Faction"}

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Factions")
    out.append("")
    out.append(gc.DIVIDER)
    out.append("")
    out.append("## Attributes")
    out.append("")

    def header3(text):
        out.append(gc.DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    # Any factions present in the JSON but not in FACTION_ORDER get appended.
    ordered_ids = [fid for fid, _ in FACTION_ORDER]
    extras = [o["id"] for o in data if o.get("type") == "Faction"
              and o.get("id") and o["id"] not in ordered_ids]
    order = FACTION_ORDER + [(e, e) for e in extras]

    for fid, title in order:
        o = by_id.get(fid.lower())
        if not o:
            continue
        van = van_by_id.get(fid.lower())
        ranks = o.get("rank_names") or []
        reqs = (o.get("data") or {}).get("requirements") or []
        vreqs = ((van or {}).get("data") or {}).get("requirements") or []

        header3(f"### {title}")
        out.append("```")
        for i, rank in enumerate(ranks):
            if not rank or rank == "None":
                continue
            cur = rank_attr(reqs[i]) if i < len(reqs) else None
            vanv = rank_attr(vreqs[i]) if i < len(vreqs) else None
            out.append(gc.add_at_column(rank, gc.COL_VALUES, gc.arrow(vanv, cur)))
        out.append("```")
        out.append("")

    while out and out[-1] == "":
        out.pop()
    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  Factions: {len(by_id)}")
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

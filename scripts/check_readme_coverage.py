#!/usr/bin/env python3
"""Audit: is every ESP JSON record represented in its README?

For each R3 plugin, list every record in the JSON and check whether its
identifying token (id / effect_id for MagicEffect) appears anywhere in the
matching README. Records whose token is absent are reported as coverage gaps,
grouped by record type so systematic omissions (an entire type the generator
skips) are obvious.

Read-only. Prints a report; writes nothing.
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# plugin JSON  ->  README
PAIRS = [
    ("R3 - Core.json", "R3 - Core.md"),
    ("R3 - Spells.json", "R3 - Spells.md"),
    ("R3 - Potions.json", "R3 - Potions.md"),
    ("R3 - Creatures.json", "R3 - Creatures.md"),
    ("R3 - Enchantments.json", "R3 - Enchantments.md"),
    ("R3 - Factions.json", "R3 - Factions.md"),
    ("R3 - Races & Birthsigns.json", "R3 - Races & Birthsigns.md"),
    (os.path.join("optional", "R3 - Optional - Morag Tong Polished.json"),
     os.path.join("optional", "R3 - Optional.md")),
    (os.path.join("optional", "R3 - Optional - No Magic Insufficient Charge Messagebox.json"),
     os.path.join("optional", "R3 - Optional.md")),
    (os.path.join("optional", "R3 - Optional - One Hour Barter Gold Reset Delay.json"),
     os.path.join("optional", "R3 - Optional.md")),
]

# Record types we expect NOT to appear by id in a README (structural/header
# records tes3conv emits that carry no balance data). Reported separately.
SKIP_TYPES = {"Header", "TES3"}


def token(o: dict):
    """The string that should appear in the README for this record."""
    t = o.get("type")
    if t == "MagicEffect":
        return o.get("effect_id")
    return o.get("id")


def main() -> int:
    grand = {}
    for jrel, mdrel in PAIRS:
        jpath = os.path.join(ROOT, jrel)
        mdpath = os.path.join(ROOT, mdrel)
        if not os.path.exists(jpath):
            print(f"!! JSON missing: {jrel}")
            continue
        if not os.path.exists(mdpath):
            print(f"!! README missing: {mdrel}")
            continue
        with open(jpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        md = open(mdpath, "r", encoding="utf-8").read()

        by_type_total = {}
        by_type_missing = {}
        missing_examples = {}
        for o in data:
            if not isinstance(o, dict):
                continue
            t = o.get("type") or "?"
            if t in SKIP_TYPES:
                continue
            tok = token(o)
            if not tok:
                continue
            by_type_total[t] = by_type_total.get(t, 0) + 1
            # Case-insensitive substring test: README quotes ids verbatim.
            if tok.lower() not in md.lower():
                by_type_missing[t] = by_type_missing.get(t, 0) + 1
                missing_examples.setdefault(t, []).append((tok, o.get("name")))

        print("=" * 70)
        print(f"{jrel}  ->  {mdrel}")
        for t in sorted(by_type_total):
            miss = by_type_missing.get(t, 0)
            tot = by_type_total[t]
            flag = "  <-- GAP" if miss else ""
            print(f"  {t:14} {tot-miss:4}/{tot:<4} covered{flag}")
            for tok, nm in missing_examples.get(t, [])[:12]:
                print(f"        MISSING: {tok!r}  (name={nm!r})")
            extra = by_type_missing.get(t, 0) - 12
            if extra > 0:
                print(f"        ... and {extra} more")
        grand[jrel] = sum(by_type_missing.values())
    print("=" * 70)
    print("SUMMARY (missing tokens per plugin):")
    for k, v in grand.items():
        print(f"  {v:4}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

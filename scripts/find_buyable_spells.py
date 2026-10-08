#!/usr/bin/env python3
"""Find all player-buyable spells in Tamriel Rebuilt / Tamriel Data.

A spell is "buyable" when a spell merchant (an NPC whose AI services include
OFFERS_SPELLS) knows it in their personal `spells` list AND the spell record
is of spell_type "Spell". Abilities, Powers, Curses, Diseases and Blight are
never sold at a merchant's spell-buy menu, so they are excluded.

Spell IDs on an NPC may be defined in any loaded master, so this script loads
the full TR load order (vanilla + Tamriel Data + the TR province plugins) and
resolves spell IDs case-insensitively across all of them.

Outputs two things:
  1. The list of spell-merchant NPCs (id, name, how many spells they sell).
  2. The de-duplicated list of player-buyable spells (id, name, cost, which
     merchants sell them).

Usage:
    python find_buyable_spells.py                 # prints report to stdout
    python find_buyable_spells.py --out report.md # also writes a markdown file
    python find_buyable_spells.py --csv spells.csv # also writes a CSV of spells
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict

# tes3conv JSON reference folder (read-only vanilla/TD/TR data).
TES3CONV_DIR = r"c:\OMEN\Morrowind\tes3conv"

# Load order, lowest master first. Later files override earlier ones for a
# given record id (matching how the game resolves records).
LOAD_ORDER = [
    "Morrowind.json",
    "Tribunal.json",
    "Bloodmoon.json",
    "Tamriel_Data.json",
    "TR_Mainland.json",
    "Cyr_Main.json",
    "Sky_Main.json",
]

# The AI service flag that marks an NPC as a spell merchant.
SPELL_SERVICE = "OFFERS_SPELLS"

# Only this spell_type is purchasable at a merchant.
BUYABLE_SPELL_TYPE = "Spell"

# TR province plugins whose merchants we care about (player-reachable content).
# Merchants defined in vanilla/TD masters are also included because TR reuses
# and places them, but you can restrict reporting with --tr-only.
TR_PROVINCE_FILES = {"TR_Mainland.json", "Cyr_Main.json", "Sky_Main.json"}


def load_json(path: str) -> list:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def build_data(files: list[str]):
    """Load the load order and build:
    - spells_by_id: lowercase spell id -> spell record (last definition wins)
    - npcs: list of (source_file, npc_record)
    """
    spells_by_id: dict[str, dict] = {}
    npcs: list[tuple[str, dict]] = []

    for fname in files:
        path = os.path.join(TES3CONV_DIR, fname)
        if not os.path.exists(path):
            print(f"WARNING: missing {path}, skipping", file=sys.stderr)
            continue
        data = load_json(path)
        for rec in data:
            rtype = rec.get("type")
            if rtype == "Spell":
                spells_by_id[rec["id"].lower()] = rec
            elif rtype == "Npc":
                npcs.append((fname, rec))

    return spells_by_id, npcs


def is_spell_merchant(npc: dict) -> bool:
    services = (npc.get("ai_data") or {}).get("services") or ""
    return SPELL_SERVICE in services


def collect(spells_by_id, npcs, tr_only: bool):
    """Return (merchants, buyable_spells).

    merchants: list of dicts {file, id, name, sold_spell_ids}
    buyable_spells: dict spell_id(lower) -> {record, sold_by:set(npc ids)}
    """
    merchants = []
    buyable: dict[str, dict] = {}

    for fname, npc in npcs:
        if not is_spell_merchant(npc):
            continue
        if tr_only and fname not in TR_PROVINCE_FILES:
            continue

        sold = []
        for sid in npc.get("spells", []):
            rec = spells_by_id.get(sid.lower())
            if rec is None:
                # Spell id the NPC references but no record found in load order.
                continue
            if rec["data"].get("spell_type") != BUYABLE_SPELL_TYPE:
                continue
            sold.append(rec["id"])
            entry = buyable.setdefault(
                rec["id"].lower(), {"record": rec, "sold_by": set()}
            )
            entry["sold_by"].add(npc["id"])

        merchants.append(
            {
                "file": fname,
                "id": npc["id"],
                "name": npc.get("name", ""),
                "sold_spell_ids": sold,
            }
        )

    return merchants, buyable


def spell_schools(rec: dict) -> str:
    """Best-effort school label from the first effect's magic effect name."""
    effects = rec.get("effects") or []
    if not effects:
        return ""
    return effects[0].get("magic_effect", "")


def print_report(merchants, buyable):
    print("=" * 70)
    print(f"SPELL MERCHANTS: {len(merchants)}")
    print("=" * 70)
    for m in sorted(merchants, key=lambda x: (x["file"], x["id"])):
        print(f"  [{m['file']:<16}] {m['id']:<35} {m['name']:<28} "
              f"sells {len(m['sold_spell_ids'])}")

    print()
    print("=" * 70)
    print(f"PLAYER-BUYABLE SPELLS (unique): {len(buyable)}")
    print("=" * 70)
    for sid in sorted(buyable):
        rec = buyable[sid]["record"]
        n_merch = len(buyable[sid]["sold_by"])
        print(f"  {rec['id']:<40} cost={rec['data'].get('cost', '?'):<5} "
              f"name={rec.get('name', '')!r:<30} merchants={n_merch}")


def write_markdown(path, merchants, buyable):
    lines = []
    lines.append("# Player-Buyable Spells (Tamriel Rebuilt / Tamriel Data)\n")
    lines.append(f"Spell merchants found: **{len(merchants)}**  ")
    lines.append(f"Unique buyable spells: **{len(buyable)}**\n")

    lines.append("## Buyable Spells\n")
    lines.append("| Spell ID | Name | Cost | # Merchants |")
    lines.append("|----------|------|-----:|------------:|")
    for sid in sorted(buyable):
        rec = buyable[sid]["record"]
        name = rec.get("name", "").replace("|", "\\|")
        rid = rec["id"].replace("|", "\\|")
        cost = rec["data"].get("cost", "?")
        nm = len(buyable[sid]["sold_by"])
        lines.append(f"| {rid} | {name} | {cost} | {nm} |")

    lines.append("\n## Spell Merchants\n")
    lines.append("| File | NPC ID | Name | # Spells Sold |")
    lines.append("|------|--------|------|--------------:|")
    for m in sorted(merchants, key=lambda x: (x["file"], x["id"])):
        name = m["name"].replace("|", "\\|")
        mid = m["id"].replace("|", "\\|")
        lines.append(f"| {m['file']} | {mid} | {name} | {len(m['sold_spell_ids'])} |")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"\nWrote markdown report: {path}")


def write_csv(path, buyable):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["spell_id", "name", "cost", "first_effect", "num_merchants",
                    "sold_by"])
        for sid in sorted(buyable):
            rec = buyable[sid]["record"]
            sold_by = ";".join(sorted(buyable[sid]["sold_by"]))
            w.writerow([
                rec["id"],
                rec.get("name", ""),
                rec["data"].get("cost", ""),
                spell_schools(rec),
                len(buyable[sid]["sold_by"]),
                sold_by,
            ])
    print(f"Wrote CSV: {path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", help="write a markdown report to this path")
    ap.add_argument("--csv", help="write a CSV of buyable spells to this path")
    ap.add_argument("--tr-only", action="store_true",
                    help="only report merchants defined in TR province plugins "
                         "(TR_Mainland, Cyr_Main, Sky_Main)")
    args = ap.parse_args()

    spells_by_id, npcs = build_data(LOAD_ORDER)
    merchants, buyable = collect(spells_by_id, npcs, args.tr_only)

    print_report(merchants, buyable)

    if args.out:
        write_markdown(args.out, merchants, buyable)
    if args.csv:
        write_csv(args.csv, buyable)


if __name__ == "__main__":
    main()

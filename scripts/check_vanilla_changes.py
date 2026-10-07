#!/usr/bin/env python3
"""Check whether any record your ESP modifies had its VANILLA definition change
between the old (backup) and new (current) master JSONs.

For every record id in the given ESP JSON, the script looks that id up in both
the old backup masters and the new masters (non-base masters only, since the
base game was not refreshed), and reports any id whose full record differs.

This flags upstream changes to records you rebalanced, so you can review whether
your tuning still makes sense against the new baseline.

Usage:
  python scripts/check_vanilla_changes.py                       # Spells & Potions
  python scripts/check_vanilla_changes.py --esp "R3 - Core.json"
  python scripts/check_vanilla_changes.py --backup <dir>        # pick a backup
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

# Masters that were refreshed (base game Morrowind/Tribunal/Bloodmoon excluded).
CHECK_MASTERS = [
    "Patch for Purists.json",
    "Tamriel_Data.json",
    "TR_Mainland.json",
    "TR_Factions.json",
    "Sky_Main.json",
    "Cyr_Main.json",
]


def load_by_id(dir_path: str, masters: list[str], needed: set[str]) -> dict:
    """id_lower -> record, first master wins, limited to needed ids."""
    out: dict[str, dict] = {}
    for name in masters:
        p = os.path.join(dir_path, name)
        if not os.path.exists(p):
            continue
        for o in gc.read_records(p):
            if not isinstance(o, dict):
                continue
            rid = o.get("id")
            if not rid:
                continue
            k = rid.lower().strip()
            if k in needed and k not in out:
                out[k] = o
    return out


def canon(obj):
    """Stable JSON string for deep comparison."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=False)


def latest_backup(tes3_dir: str) -> str | None:
    base = os.path.join(tes3_dir, "_backup_json")
    if not os.path.isdir(base):
        return None
    subs = sorted(d for d in glob.glob(os.path.join(base, "*")) if os.path.isdir(d))
    return subs[-1] if subs else None


def brief(o: dict) -> str:
    """A short human summary of a record's key values."""
    if not o:
        return "(absent)"
    parts = []
    effs = o.get("effects")
    if effs:
        for e in effs:
            mn, mx = e.get("min_magnitude"), e.get("max_magnitude")
            mag = f"{mn}" if mn == mx else f"{mn}-{mx}"
            seg = f"{e.get('magic_effect')} {mag}/{e.get('duration')}s"
            if e.get("area"):
                seg += f"/{e.get('area')}ft"
            parts.append(seg)
    data = o.get("data") or {}
    for key in ("cost", "value", "magicka"):
        if key in data:
            parts.append(f"{key}={data[key]}")
    if o.get("name"):
        parts.append(f'name="{o["name"]}"')
    return "; ".join(parts) if parts else canon(o)[:120]


def main() -> int:
    ap = argparse.ArgumentParser(description="Report upstream vanilla changes to records your ESP modifies.")
    ap.add_argument("--esp", default="R3 - Spells & Potions.json")
    ap.add_argument("--tes3", default=gc.DEFAULT_MASTER_DIR)
    ap.add_argument("--backup", default=None,
                    help="Backup JSON dir (defaults to the newest under tes3conv/_backup_json).")
    args = ap.parse_args()

    with open(args.esp, "r", encoding="utf-8") as f:
        esp = json.load(f)

    esp_by_id = {o["id"].lower().strip(): o for o in esp if o.get("id")}
    needed = set(esp_by_id.keys())

    backup = args.backup or latest_backup(args.tes3)
    if not backup:
        print("No backup directory found under tes3conv/_backup_json.", file=sys.stderr)
        return 1

    print(f"ESP     : {args.esp}  ({len(needed)} records)")
    print(f"Old     : {backup}")
    print(f"New     : {args.tes3}")
    print(f"Masters : {', '.join(CHECK_MASTERS)}\n")

    old = load_by_id(backup, CHECK_MASTERS, needed)
    new = load_by_id(args.tes3, CHECK_MASTERS, needed)

    changed = []
    for k in sorted(set(old) | set(new)):
        o_old = old.get(k)
        o_new = new.get(k)
        if canon(o_old) != canon(o_new):
            changed.append((k, o_old, o_new))

    if not changed:
        print("No vanilla changes affect the records this ESP modifies.")
        return 0

    print(f"{len(changed)} record(s) changed upstream:\n")
    for k, o_old, o_new in changed:
        esp_rec = esp_by_id.get(k)
        name = (o_new or o_old or {}).get("name") or (esp_rec or {}).get("name") or k
        print(f"- {name}  (id: {k})")
        print(f"    old vanilla : {brief(o_old)}")
        print(f"    new vanilla : {brief(o_new)}")
        print(f"    your ESP    : {brief(esp_rec)}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())

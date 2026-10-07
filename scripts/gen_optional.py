#!/usr/bin/env python3
"""Optional plugins README generator.

Each `optional/R3 - Optional - *.json` is a tiny single-record plugin. One
section per plugin, showing its changed value as `vanilla -> current` (vanilla
from the masters). Fully derived from the JSON so it always reflects the
current state.

Supported records:
  - GameSetting : value (strings shown quoted; empty string as "")
  - Script      : the `set murdercost to N` value (Morag Tong feature)

Output: optional/R3 - Optional.md
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc


def quote(v):
    """Strings shown in quotes (empty string -> \"\"); numbers as-is."""
    if isinstance(v, str):
        return f'"{v}"'
    return gc.fmt_num(v)


def murdercost(rec):
    txt = (rec or {}).get("text") or (rec or {}).get("script_text") or ""
    m = re.search(r"set murdercost to (-?\d+)", txt)
    return int(m.group(1)) if m else None


def plugin_title(filename: str) -> str:
    """'R3 - Optional - One Hour Barter Gold Reset Delay.json'
       -> 'One Hour Barter Gold Reset Delay'."""
    base = os.path.splitext(os.path.basename(filename))[0]
    marker = "Optional - "
    i = base.find(marker)
    return base[i + len(marker):] if i >= 0 else base


def main() -> int:
    ap = argparse.ArgumentParser(description="Optional plugins README generator.")
    ap.add_argument("--dir", default="optional")
    ap.add_argument("--out", default="optional/R3 - Optional.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(args.dir, "R3 - Optional - *.json")))

    # Collect needed ids for vanilla lookup (GameSettings + the MT script).
    needed = set()
    for p in files:
        for o in json.load(open(p, encoding="utf-8")):
            if o.get("id"):
                needed.add(o["id"].lower().strip())
    van_by_id, _ = gc.load_vanilla(args.master_dir, needed, masters=gc.BASE_MASTERS)

    # Scripts aren't captured by load_vanilla's value logic; grab them directly.
    van_scripts: dict[str, dict] = {}
    for m in gc.BASE_MASTERS:
        mp = os.path.join(args.master_dir, m)
        if not os.path.exists(mp):
            continue
        for o in gc.read_records(mp):
            if isinstance(o, dict) and o.get("type") == "Script" and o.get("id"):
                k = o["id"].lower().strip()
                if k not in van_scripts:
                    van_scripts[k] = o

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Optional")
    out.append("")

    def header(text):
        out.append(gc.DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    for p in files:
        recs = [o for o in json.load(open(p, encoding="utf-8"))
                if o.get("type") != "Header"]
        header(f"## {plugin_title(p)}")
        out.append("```")
        for o in recs:
            idl = (o.get("id") or "").lower().strip()
            if o.get("type") == "GameSetting":
                cur = (o.get("value") or {}).get("data")
                vrec = van_by_id.get(idl)
                van = (vrec.get("value") or {}).get("data") if vrec else None
                # A blanked string setting is stored as Float 0.0; if vanilla is
                # a string, render the current as an empty string "".
                if isinstance(van, str) and not isinstance(cur, str):
                    cur = ""
                vb = (f"{quote(van)} -> {quote(cur)}"
                      if van is not None and van != cur else quote(cur))
                out.append(gc.add_at_column(o.get("id", ""), gc.COL_VALUES, vb))
            elif o.get("type") == "Script":
                cur = murdercost(o)
                van = murdercost(van_scripts.get(idl))
                if cur is not None:
                    vb = (gc.arrow(van, cur) if van is not None
                          else gc.fmt_num(cur))
                    out.append(gc.add_at_column(o.get("id", ""), gc.COL_VALUES, vb))
        out.append("```")
        out.append("")

    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  Plugins: {len(files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

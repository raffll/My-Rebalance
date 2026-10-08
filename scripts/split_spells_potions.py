#!/usr/bin/env python3
"""One-shot structural split of "R3 - Spells & Potions.json" into two files.

Produces:
  - "R3 - Potions.json"  : Header + all Alchemy records (in source order).
  - "R3 - Spells.json"   : Header + all non-Alchemy, non-Header records
                           (MagicEffect + Spell + GameSetting, in source order).

Purely mechanical: no data value is changed, records are only redistributed.
Hard count assertions abort (non-zero exit, no files written) on any mismatch.

Both outputs are written UTF-8 without BOM, CRLF line endings.
Does NOT delete the old source file.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SOURCE = os.path.join(ROOT, "R3 - Spells & Potions.json")
POTIONS = os.path.join(ROOT, "R3 - Potions.json")
SPELLS = os.path.join(ROOT, "R3 - Spells.json")


def write_json_crlf(path: str, records: list) -> None:
    """Write a JSON array UTF-8 (no BOM) with CRLF line endings."""
    # json.dump with newline="" writes LF-only; normalize to CRLF in binary.
    with open(path, "w", encoding="utf-8", newline="") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    with open(path, "rb") as f:
        data = f.read()
    if data[:3] == b"\xef\xbb\xbf":
        data = data[3:]
    # Normalize any lone \n to \r\n (collapse existing \r\n first to avoid \r\r\n).
    data = data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    with open(path, "wb") as f:
        f.write(data)


def main() -> int:
    if not os.path.exists(SOURCE):
        print(f"Source not found: {SOURCE}", file=sys.stderr)
        return 1

    with open(SOURCE, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    if not data or data[0].get("type") != "Header":
        print("First record is not a Header; aborting.", file=sys.stderr)
        return 1
    header = data[0]
    body = data[1:]

    alchemy = [o for o in body if o.get("type") == "Alchemy"]
    non_alchemy = [o for o in body if o.get("type") not in ("Alchemy", "Header")]

    # Count sanity on the non-Alchemy side.
    counts = {}
    for o in non_alchemy:
        counts[o.get("type")] = counts.get(o.get("type"), 0) + 1

    assert len(alchemy) == 296, f"expected 296 Alchemy, got {len(alchemy)}"
    assert counts.get("MagicEffect") == 48, f"expected 48 MagicEffect, got {counts.get('MagicEffect')}"
    assert counts.get("Spell") == 234, f"expected 234 Spell, got {counts.get('Spell')}"
    assert counts.get("GameSetting") == 2, f"expected 2 GameSetting, got {counts.get('GameSetting')}"
    assert len(non_alchemy) == 48 + 234 + 2, f"non-Alchemy total mismatch: {len(non_alchemy)}"
    # No stray Header leaked into either body.
    assert all(o.get("type") != "Header" for o in alchemy)
    assert all(o.get("type") != "Header" for o in non_alchemy)

    potions = [header] + alchemy
    spells = [header] + non_alchemy

    assert len(potions) == 1 + 296, f"potions total {len(potions)}"
    assert len(spells) == 1 + 284, f"spells total {len(spells)}"

    write_json_crlf(POTIONS, potions)
    write_json_crlf(SPELLS, spells)

    print(f"Wrote {POTIONS}")
    print(f"  Header 1 + Alchemy {len(alchemy)} = {len(potions)} records")
    print(f"Wrote {SPELLS}")
    print(f"  Header 1 + MagicEffect {counts.get('MagicEffect')} + "
          f"Spell {counts.get('Spell')} + GameSetting {counts.get('GameSetting')} "
          f"= {len(spells)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())

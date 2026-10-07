#!/usr/bin/env python3
"""Build all ESPs from their JSON sources, on demand.

Converts every `R3 - *.json` in the workspace root (and optionally the
`optional/` folder) to a matching `.esp` using tes3conv.

tes3conv syntax: `tes3conv <input> <output> --overwrite`
(`--overwrite` writes without making numbered backups).

Usage:
  python scripts/build_esps.py
  python scripts/build_esps.py --optional          # also build optional/ ESPs
  python scripts/build_esps.py --tes3conv <path>   # override exe path
"""
from __future__ import annotations

import argparse
import glob
import os
import subprocess
import sys

DEFAULT_TES3CONV = "C:/OMEN/Morrowind/tes3conv/tes3conv.exe"


def strip_bom(path: str) -> None:
    """tes3conv rejects a UTF-8 BOM; remove it in place if present."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:3] == b"\xef\xbb\xbf":
        with open(path, "wb") as f:
            f.write(data[3:])


def convert(exe: str, json_path: str) -> bool:
    esp_path = os.path.splitext(json_path)[0] + ".esp"
    strip_bom(json_path)
    print(f"  {os.path.basename(json_path)} -> {os.path.basename(esp_path)}")
    result = subprocess.run(
        [exe, json_path, esp_path, "--overwrite"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip() or result.stdout.strip()}",
              file=sys.stderr)
        return False
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Build all R3 ESPs from JSON.")
    ap.add_argument("--tes3conv", default=DEFAULT_TES3CONV,
                    help="Path to tes3conv.exe")
    ap.add_argument("--optional", action="store_true",
                    help="Also build the ESPs in the optional/ folder")
    args = ap.parse_args()

    exe = args.tes3conv
    if not os.path.exists(exe):
        print(f"tes3conv not found: {exe}", file=sys.stderr)
        return 1

    targets = sorted(glob.glob("R3 - *.json"))
    if args.optional:
        targets += sorted(glob.glob(os.path.join("optional", "R3 - *.json")))

    if not targets:
        print("No R3 - *.json files found.", file=sys.stderr)
        return 1

    print(f"Building {len(targets)} ESP(s) with {exe}")
    ok = 0
    for jp in targets:
        if convert(exe, jp):
            ok += 1

    print(f"\nDone: {ok}/{len(targets)} built.")
    return 0 if ok == len(targets) else 1


if __name__ == "__main__":
    sys.exit(main())

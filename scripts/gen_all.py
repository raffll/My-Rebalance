#!/usr/bin/env python3
"""Regenerate every README from JSON (and optionally build all ESPs).

Runs all README generators in sequence. With --build, also runs build_esps.py
afterward so JSON -> README -> ESP are all refreshed in one command.

Usage:
  python scripts/gen_all.py                 # regenerate all READMEs
  python scripts/gen_all.py --build         # ... then build main ESPs
  python scripts/gen_all.py --build --optional   # ... including optional ESPs
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# README generators, in order.
GENERATORS = [
    "gen_core.py",
    "gen_readme.py",
    "gen_creatures.py",
    "gen_enchantments.py",
    "gen_factions.py",
    "gen_races.py",
    "gen_optional.py",
]


def run(script: str, extra_args=None) -> bool:
    path = os.path.join(HERE, script)
    print(f"\n>>> {script}")
    result = subprocess.run([sys.executable, path, *(extra_args or [])])
    return result.returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Regenerate all READMEs (and optionally ESPs).")
    ap.add_argument("--build", action="store_true",
                    help="Also build ESPs after regenerating READMEs.")
    ap.add_argument("--optional", action="store_true",
                    help="With --build, also build the optional/ ESPs.")
    args = ap.parse_args()

    ok = 0
    for g in GENERATORS:
        if run(g):
            ok += 1
        else:
            print(f"    (generator failed: {g})", file=sys.stderr)

    print(f"\nREADMEs: {ok}/{len(GENERATORS)} generated.")

    if args.build:
        build_args = ["--optional"] if args.optional else []
        if not run("build_esps.py", build_args):
            print("ESP build failed.", file=sys.stderr)
            return 1

    return 0 if ok == len(GENERATORS) else 1


if __name__ == "__main__":
    sys.exit(main())

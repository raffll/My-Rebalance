#!/usr/bin/env python3
"""Shared helpers for the README generators (Spells & Potions, Core, ...).

Provides: column formatting, number formatting, the streaming JSON-array reader
for very large master files, and master loading with a fixed lookup order.
"""
from __future__ import annotations

import json
import os

# Column grid (0-indexed).
COL_VALUES = 44
COL_ID = 80
EFFECT_INDENT = "    "
DIVIDER = "-" * 60

# Master lookup order: first hit wins.
MASTER_FILES = [
    "Morrowind.json",
    "Tribunal.json",
    "Bloodmoon.json",
    "Patch for Purists.json",
    "Tamriel_Data.json",
    "TR_Mainland.json",
    "Sky_Main.json",
    "Cyr_Main.json",
]

DEFAULT_MASTER_DIR = "C:/OMEN/Morrowind/tes3conv"

# Masters that actually contain base-game records (races, birthsigns, their
# ability spells, GMSTs). Excludes the huge TR_Mainland / Sky / Cyr landmass
# files, which hold no vanilla race/birthsign/base-spell data.
BASE_MASTERS = [
    "Morrowind.json",
    "Tribunal.json",
    "Bloodmoon.json",
    "Patch for Purists.json",
    "Tamriel_Data.json",
]

# Files at/above this size are read with the streaming decoder.
STREAM_THRESHOLD = 50 * 1024 * 1024  # 50 MB


def fmt_num(v) -> str:
    """Render a number as-is from JSON (floats stay floats)."""
    return str(v)


def add_at_column(base: str, col: int, segment: str) -> str:
    if not segment:
        return base
    if len(base) < col:
        base += " " * (col - len(base))
    else:
        base += " "
    return base + segment


def split_camel(s: str) -> str:
    """LongBlade -> "Long Blade"; leaves already-spaced text alone."""
    out = []
    for i, ch in enumerate(s):
        if i > 0 and ch.isupper() and not s[i - 1].isupper():
            out.append(" ")
        out.append(ch)
    return "".join(out)


def iter_json_array(path: str):
    """Yield objects from a JSON array file one at a time (stdlib only)."""
    decoder = json.JSONDecoder()
    with open(path, "r", encoding="utf-8") as f:
        buf = f.read()
    i, n = 0, len(buf)
    while i < n and buf[i] in " \t\r\n":
        i += 1
    if i < n and buf[i] == "[":
        i += 1
    while i < n:
        while i < n and buf[i] in " \t\r\n,":
            i += 1
        if i >= n or buf[i] == "]":
            break
        obj, end = decoder.raw_decode(buf, i)
        yield obj
        i = end


def read_records(path: str):
    """Read a master file, streaming if large."""
    size = os.path.getsize(path)
    if size >= STREAM_THRESHOLD:
        return iter_json_array(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_vanilla(master_dir: str, needed_ids: set[str], want_effect_names: bool = False,
                 masters: list[str] | None = None):
    """Load vanilla records (by id, first master wins) for the given ids.

    Returns (van_by_id, effect_names) where effect_names maps effect_id ->
    display name from the sEffect<Name> GMSTs (empty when not requested).
    """
    van_by_id: dict[str, dict] = {}
    effect_names: dict[str, str] = {}
    for name in (masters or MASTER_FILES):
        path = os.path.join(master_dir, name)
        if not os.path.exists(path):
            continue
        for o in read_records(path):
            if not isinstance(o, dict):
                continue
            rid = o.get("id")
            if want_effect_names and o.get("type") == "GameSetting" \
                    and isinstance(rid, str) and rid.startswith("sEffect"):
                key = rid[len("sEffect"):]
                if key not in effect_names:
                    val = (o.get("value") or {}).get("data")
                    if isinstance(val, str) and val:
                        effect_names[key] = val
            if not rid:
                continue
            k = rid.lower().strip()
            if k in needed_ids and k not in van_by_id:
                van_by_id[k] = o
    return van_by_id, effect_names


def load_vanilla_typed(master_dir: str, want_types: set[str], want_spell_ids: set[str],
                       want_spell_names: set[str] | None = None,
                       masters: list[str] | None = None):
    """Load vanilla records keyed by (type, id_lower), plus spell lookups by id
    and (optionally) by name for effect resolution.

    - want_types: record types to capture into the (type, id) map.
    - want_spell_ids: spell ids to capture into the by-id spell map.
    - want_spell_names: spell names (lowercased) to capture into a by-name map.

    First master wins for each key. Returns (typed, spells_by_id, spells_by_name).
    """
    want_spell_names = want_spell_names or set()
    typed: dict[tuple, dict] = {}
    spells: dict[str, dict] = {}
    spells_by_name: dict[str, dict] = {}
    for name in (masters or MASTER_FILES):
        path = os.path.join(master_dir, name)
        if not os.path.exists(path):
            continue
        for o in read_records(path):
            if not isinstance(o, dict):
                continue
            t = o.get("type")
            rid = o.get("id")
            if not rid:
                continue
            k = rid.lower().strip()
            if t in want_types:
                key = (t, k)
                if key not in typed:
                    typed[key] = o
            if t == "Spell":
                if k in want_spell_ids and k not in spells:
                    spells[k] = o
                nm = (o.get("name") or "").strip().lower()
                if nm and nm in want_spell_names and nm not in spells_by_name:
                    spells_by_name[nm] = o
    return typed, spells, spells_by_name


def arrow(van, cur) -> str:
    """"vanilla -> current" when they differ, else just current (as strings)."""
    cur_s = fmt_num(cur)
    van_s = fmt_num(van) if van is not None else None
    if van_s is not None and van_s != cur_s:
        return f"{van_s} -> {cur_s}"
    return cur_s

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


# ---------------------------------------------------------------------------
# Per-effect axis flags (No Magnitude / No Duration).
# Loaded from scripts/effect_axis_flags.json so all generators share one source
# of truth. tes3conv does not expose the engine MGEF flags, so they live in that
# data file. See docs/Effect-Magnitude-Duration-Flags.md.
# ---------------------------------------------------------------------------
_AXIS_FLAGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "effect_axis_flags.json")
_axis_cache = None


def _load_axis_flags() -> dict:
    global _axis_cache
    if _axis_cache is None:
        try:
            with open(_AXIS_FLAGS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            no_mag = set(data.get("no_magnitude") or [])
            no_dur = set(data.get("no_duration") or [])
            both = set(data.get("no_magnitude_no_duration") or [])
            # Effects in the "neither" group lack both axes.
            no_mag |= both
            no_dur |= both
            _axis_cache = {"no_magnitude": no_mag, "no_duration": no_dur}
        except (OSError, ValueError):
            # Missing/corrupt file: fail open (every effect uses both axes).
            _axis_cache = {"no_magnitude": set(), "no_duration": set()}
    return _axis_cache


def effect_uses_magnitude(fx: str) -> bool:
    """False for effects with no magnitude (Silence, Paralyze, Summon*, Cure*,
    teleports...). Magnitude is omitted from output for these."""
    return fx not in _load_axis_flags()["no_magnitude"]


def effect_uses_duration(fx: str) -> bool:
    """False for effects with no duration (Lock, Open, Dispel, Cure*,
    teleports...). Duration is omitted from output for these.
    NOTE: Damage/Drain/Restore/Absorb DO use duration (they act per second), so
    they are not in this set even when a given record has duration 0."""
    return fx not in _load_axis_flags()["no_duration"]


def format_effect_values(eff: dict) -> str:
    """Render an effect's magnitude/duration, omitting whichever axis the effect
    does not use. Silence -> "18s" (not "1/18s"); Lock -> "5" (not "5/0s"); a
    teleport/cure (neither axis) -> "-". Does not append area/range; callers that
    need those add them."""
    fx = eff.get("magic_effect", "") or ""
    mn = int(eff.get("min_magnitude", 0))
    mx = int(eff.get("max_magnitude", 0))
    dur = int(eff.get("duration", 0))
    mag = f"{mn}" if mn == mx else f"{mn}-{mx}"
    use_mag = effect_uses_magnitude(fx)
    use_dur = effect_uses_duration(fx)
    if use_mag and use_dur:
        return f"{mag}/{dur}s"
    if use_dur:            # duration-only (Silence, Paralyze, Summon*...)
        return f"{dur}s"
    if use_mag:            # magnitude-only (Lock, Open, Dispel)
        return f"{mag}"
    return "-"             # neither axis (Mark/Recall/Intervention, Cure*)


# Range value -> short label used in the README (Self is the default and is
# never shown; only Touch/Target appear when the range changed).
RANGE_LABEL = {"OnTouch": "Touch", "OnTarget": "Target", "OnSelf": "Self"}


def format_effect(eff: dict, show_area: bool = True, show_range: bool = True) -> str:
    """Render an effect's values. Magnitude/duration come from the shared
    axis-aware renderer, so an effect with no magnitude shows duration only
    (Silence -> "18s") and an effect with no duration shows magnitude only
    (Damage Health -> "5"). Area and range are only appended when the caller
    asks (i.e. when they changed)."""
    area = int(eff.get("area", 0))
    # Base magnitude/duration, with the unused axis omitted per effect flags.
    v = format_effect_values(eff)
    if show_area:
        v = f"{v}/{area}ft"
    if show_range:
        label = RANGE_LABEL.get(eff.get("range", ""), eff.get("range", ""))
        if label:
            v = f"{v}/{label}"
    return v


def format_effect_pair(eff: dict, van_eff: dict | None) -> str:
    """Render one effect as "vanilla -> current", showing area and range only
    when they changed. Magnitude/duration always shown."""
    cur_area = int(eff.get("area", 0))
    van_area = int(van_eff.get("area", 0)) if van_eff is not None else None
    area_changed = van_area is not None and van_area != cur_area
    show_area = area_changed if van_eff is not None else cur_area > 0

    cur_range = eff.get("range", "")
    van_range = van_eff.get("range", "") if van_eff is not None else None
    range_changed = van_range is not None and van_range != cur_range
    show_range = range_changed if van_eff is not None else False

    cur = format_effect(eff, show_area=show_area, show_range=show_range)
    van = (format_effect(van_eff, show_area=show_area, show_range=show_range)
           if van_eff is not None else None)
    if van is not None and van != cur:
        return f"{van} -> {cur}"
    return cur


def format_value_rows(obj: dict, vanilla: dict | None) -> list[str]:
    """One "vanilla -> current" string per effect, matched positionally."""
    effects = obj.get("effects") or []
    van_effects = (vanilla or {}).get("effects") or []
    rows = []
    for i, eff in enumerate(effects):
        van_eff = van_effects[i] if i < len(van_effects) else None
        rows.append(format_effect_pair(eff, van_eff))
    return rows


def is_td(obj_or_id) -> bool:
    """True for Tamriel Data records (id starts with "T_"). Accepts either a
    record dict or a bare id string."""
    rid = obj_or_id.get("id", "") if isinstance(obj_or_id, dict) else (obj_or_id or "")
    return rid.startswith("T_")


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

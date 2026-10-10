#!/usr/bin/env python3
"""Generate the "Spells" README purely from JSON.

The layout spec is baked into this script; it does NOT read the existing README.

Sources
-------
- ESP JSON (R3 - Spells.json)            : current values, IDs, records changed.
- Master JSONs (tes3conv folder)         : vanilla values, matched by id.

Master lookup order (first hit wins):
    Morrowind -> Tribunal -> Bloodmoon -> Patch for Purists
    -> Tamriel_Data -> TR_Mainland -> Sky_Main -> Cyr_Main

Output structure
----------------
    # Title
    ## Settings                         GameSettings: vanilla -> current
    ## <School>                         one per magic-effect school
      ### <Effect>                      one per effect used by single-effect records
        Base Cost                       vanilla base_cost -> current
        *Spells*                        single-effect Spell, non-TD
        *Spells - Tamriel Data*         single-effect Spell, id starts T_
    ## Multi-Effect Spells              every spell record with 2+ effects

Line format: name(col 0)  values(col 44)  id:(col 76)
    values = "<vanilla> -> <current>" per effect (joined with " + " for multi),
             or "<current>" when no vanilla counterpart exists.
Comments and the "*" deviation marker are intentionally DROPPED.

Large masters (e.g. TR_Mainland.json ~658MB) are read with a streaming decoder
that keeps only the records whose id is needed, so peak memory stays flat.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

COL_VALUES = 44
COL_ID = 80
EFFECT_INDENT = "    "  # indent before "effect N" rows on multi-effect records
DIVIDER = "-" * 60

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

# Files at/above this size are read with the streaming decoder.
STREAM_THRESHOLD = 50 * 1024 * 1024  # 50 MB


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------
def fmt_num(v) -> str:
    """Render a number as-is from JSON. Floats stay floats (1.0 stays "1.0")."""
    return str(v)


def add_at_column(base: str, col: int, segment: str) -> str:
    if not segment:
        return base
    if len(base) < col:
        base += " " * (col - len(base))
    else:
        base += " "
    return base + segment


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
    v = gc.format_effect_values(eff)
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


def cost_label(obj: dict | None) -> str | None:
    """Spell cost as a string: "auto" when AUTO_CALCULATE, else the numeric
    cost. Returns None when the record has no spell cost (e.g. potions)."""
    if not obj:
        return None
    data = obj.get("data") or {}
    if obj.get("type") != "Spell":
        return None
    flags = data.get("flags") or ""
    if "AUTO_CALCULATE" in flags:
        return "auto"
    cost = data.get("cost")
    return fmt_num(cost) if cost is not None else None


def format_cost_bracket(obj: dict, vanilla: dict | None) -> str:
    """"[vanilla -> current]" for spell cost, shown only when it changed.
    Empty string when unchanged or not applicable."""
    cur = cost_label(obj)
    van = cost_label(vanilla)
    if cur is None:
        return ""
    if van is not None and van != cur:
        return f"[{van} -> {cur}]"
    return ""


def is_td(obj: dict) -> bool:
    rid = obj.get("id") or ""
    return rid.startswith("T_")


# ---------------------------------------------------------------------------
# Streaming reader for large master files.
# Reads a pretty-printed JSON array of objects, yielding one object at a time
# via raw_decode, without loading the whole file into a Python structure.
# ---------------------------------------------------------------------------
def iter_json_array(path: str):
    decoder = json.JSONDecoder()
    with open(path, "r", encoding="utf-8") as f:
        buf = f.read()
    # Skip whitespace and the opening bracket.
    i = 0
    n = len(buf)
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


def load_master(path: str, needed_ids: set[str], out: dict) -> None:
    """Populate `out` (id_lower -> record) with records from `path` whose id is
    in `needed_ids` and not already present (first file wins)."""
    size = os.path.getsize(path)
    if size >= STREAM_THRESHOLD:
        records = iter_json_array(path)
    else:
        with open(path, "r", encoding="utf-8") as f:
            records = json.load(f)
    for o in records:
        if not isinstance(o, dict):
            continue
        rid = o.get("id")
        if not rid:
            continue
        k = rid.lower().strip()
        # MagicEffect records key on effect_id, handled separately; keep by id
        # only when needed for value lookup.
        if k in needed_ids and k not in out:
            out[k] = o


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="Generate Spells README from JSON.")
    ap.add_argument("--json", default="R3 - Spells.json",
                    help="ESP JSON path.")
    ap.add_argument("--out", default="R3 - Spells.md",
                    help="Output README path.")
    ap.add_argument("--master-dir", default="C:/OMEN/Morrowind/tes3conv",
                    help="Directory holding the master JSONs.")
    args = ap.parse_args()

    if not os.path.exists(args.json):
        print(f"ESP JSON not found: {args.json}", file=sys.stderr)
        return 1

    print(f"Loading ESP JSON: {args.json}")
    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # MagicEffect metadata from the ESP: effect_id -> {school, base_cost}.
    fx_meta: dict[str, dict] = {}
    for o in data:
        if o.get("type") == "MagicEffect" and o.get("effect_id"):
            fx_meta[o["effect_id"]] = {
                "school": (o.get("data") or {}).get("school") or "Misc",
                "base_cost": (o.get("data") or {}).get("base_cost"),
            }

    # Collect the ids we need vanilla data for: Spell/Alchemy/GameSetting ids.
    needed_ids: set[str] = set()
    for o in data:
        if o.get("type") in ("Spell", "Alchemy", "GameSetting") and o.get("id"):
            needed_ids.add(o["id"].lower().strip())

    # Load vanilla records from masters (in order, first hit wins).
    print(f"Loading masters from: {args.master_dir}")
    van_by_id: dict[str, dict] = {}
    fx_van_cost: dict[str, float] = {}
    fx_van_school: dict[str, str] = {}  # effect_id -> vanilla school
    # effect_id -> display name, from the sEffect<effect_id> GMSTs in masters.
    effect_names: dict[str, str] = {}
    # Every vanilla Spell carrying PC_START_SPELL, keyed by lower-case id
    # (first master wins). Used to build the Starting Spells section, which
    # must include start spells the ESP never overrides.
    van_start_by_id: dict[str, dict] = {}
    for name in MASTER_FILES:
        path = os.path.join(args.master_dir, name)
        if not os.path.exists(path):
            print(f"  (skip, not found) {name}")
            continue
        print(f"  reading {name}")
        # For vanilla base costs we also want MagicEffect records; scan once.
        size = os.path.getsize(path)
        records = iter_json_array(path) if size >= STREAM_THRESHOLD else json.load(open(path, "r", encoding="utf-8"))
        for o in records:
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                if o["effect_id"] not in fx_van_cost:
                    fx_van_cost[o["effect_id"]] = (o.get("data") or {}).get("base_cost")
                if o["effect_id"] not in fx_van_school:
                    fx_van_school[o["effect_id"]] = (o.get("data") or {}).get("school")
                continue
            rid = o.get("id")
            if not rid:
                continue
            # Collect every vanilla PC-start spell (first master wins).
            if o.get("type") == "Spell":
                flags = (o.get("data") or {}).get("flags") or ""
                if "PC_START_SPELL" in flags:
                    ks = rid.lower().strip()
                    if ks not in van_start_by_id:
                        van_start_by_id[ks] = o
            # sEffect<Name> GMSTs hold the in-game display name of each effect.
            if o.get("type") == "GameSetting" and rid.startswith("sEffect"):
                key = rid[len("sEffect"):]
                if key not in effect_names:
                    val = (o.get("value") or {}).get("data")
                    if isinstance(val, str) and val:
                        effect_names[key] = val
                # fall through: this GMST may also be a needed record.
            k = rid.lower().strip()
            if k in needed_ids and k not in van_by_id:
                van_by_id[k] = o

    def split_camel(s: str) -> str:
        """LongBlade -> "Long Blade"; leaves already-spaced text alone."""
        out_chars = []
        for i, ch in enumerate(s):
            if i > 0 and ch.isupper() and not s[i - 1].isupper():
                out_chars.append(" ")
            out_chars.append(ch)
        return "".join(out_chars)

    def effect_display_name(eff: dict) -> str:
        """Resolve an effect to its in-game name, with a skill/attribute
        suffix when the effect targets one (e.g. "Fortify Skill: Long Blade")."""
        fx = eff.get("magic_effect", "") or ""
        base = effect_names.get(fx, split_camel(fx))
        skill = eff.get("skill")
        attr = eff.get("attribute")
        target = None
        if skill and skill != "None":
            target = split_camel(skill)
        elif attr and attr != "None":
            target = split_camel(attr)
        return f"{base}: {target}" if target else base

    def emit_record(obj: dict) -> list[str]:
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        rows = format_value_rows(obj, van)

        cur_name = obj.get("name") or "(unnamed)"
        van_name = van.get("name") if van else None
        renamed = bool(van_name) and van_name != cur_name

        id_col = obj.get("id") or ""
        name_seg = f"{van_name} -> {cur_name}" if renamed else cur_name
        cost = format_cost_bracket(obj, van)

        # Single-effect (or no effects): one line.
        #   id (col 0) · "values [cost]" (col 44) · name (col 76)
        if len(rows) <= 1:
            vals = rows[0] if rows else ""
            if cost:
                vals = f"{vals} {cost}".strip()
            line = add_at_column(id_col, COL_VALUES, vals)
            line = add_at_column(line, COL_ID, name_seg)
            return [line]

        # Multi-effect: first row carries id, cost bracket, and name; each
        # effect gets its own indented "effect N" row.
        #   id (col 0) · "[cost]" (col 44) · name (col 76)
        #       effect N (col 0, indented) · values (col 44)
        lines = []
        first = add_at_column(id_col, COL_VALUES, cost)
        first = add_at_column(first, COL_ID, name_seg)
        lines.append(first)
        effects = obj.get("effects") or []
        for i, r in enumerate(rows):
            fx_name = effect_display_name(effects[i]) if i < len(effects) else ""
            label = f"{EFFECT_INDENT}{fx_name}"
            lines.append(add_at_column(label, COL_VALUES, r))
        return lines

    def sort_key(obj: dict):
        """Sort ascending by the vanilla first-effect's *potency*, keyed on the
        axis the effect actually uses so each grade ladder reads low -> high:
          - duration-only effects (Silence, Paralyze): sort by duration (their
            magnitude is a fixed 1, so sorting on it is meaningless);
          - everything else: sort by magnitude (min then max), with duration as
            a tiebreaker so equal-magnitude grades still order by duration.
        Records with no vanilla counterpart sort last; name is the final
        tiebreaker for stable, readable output."""
        van = van_by_id.get((obj.get("id") or "").lower().strip())
        veffs = (van or {}).get("effects") or []
        if not veffs:
            return (1, 0, 0, 0, obj.get("name", ""))
        e0 = veffs[0]
        fx = e0.get("magic_effect", "") or ""
        mn = int(e0.get("min_magnitude", 0))
        mx = int(e0.get("max_magnitude", 0))
        dur = int(e0.get("duration", 0))
        if gc.effect_uses_magnitude(fx):
            # Magnitude is the meaningful axis; duration breaks ties.
            return (0, mn, mx, dur, obj.get("name", ""))
        # Duration-only effect: sort by duration (magnitude is a fixed 1).
        return (0, dur, dur, 0, obj.get("name", ""))

    def school_of(fx: str) -> str:
        """School for an effect: ESP metadata first, else the vanilla master
        MagicEffect (effects the ESP doesn't override aren't in fx_meta)."""
        s = fx_meta.get(fx, {}).get("school")
        if not s:
            s = fx_van_school.get(fx)
        return s or "Misc"

    # Bucket records.
    groups: dict[str, dict[str, list]] = {}
    multi: list = []
    settings: list = []
    for o in data:
        if o.get("type") == "GameSetting":
            settings.append(o)
            continue
        if o.get("type") not in ("Spell", "Alchemy"):
            continue
        effects = o.get("effects") or []
        if not effects:
            continue
        if len(effects) > 1:
            multi.append(o)
            continue
        fx = effects[0].get("magic_effect")
        school = school_of(fx)
        groups.setdefault(school, {}).setdefault(fx, []).append(o)

    # Build output.
    out: list[str] = []

    def header(text: str) -> None:
        """Every header is preceded by a divider and a blank line."""
        out.append(DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    out.append("# Remastered Rebalance Redux - Spells")
    out.append("")

    if settings:
        header("## Settings")
        out.append("```")
        for s in sorted(settings, key=lambda x: x.get("id", "")):
            cur = (s.get("value") or {}).get("data")
            van_rec = van_by_id.get((s.get("id") or "").lower().strip())
            van = (van_rec.get("value") or {}).get("data") if van_rec else None
            cur_s = fmt_num(cur)
            van_s = fmt_num(van) if van is not None else None
            vb = f"{van_s} -> {cur_s}" if van_s is not None and van_s != cur_s else cur_s
            out.append(add_at_column(s.get("id", ""), COL_VALUES, vb))
        out.append("```")
        out.append("")

    def effect_base_name(fx: str) -> str:
        return effect_names.get(fx, split_camel(fx))

    # -- Starting Spells -------------------------------------------------
    # A single flat fenced block of paired one-line entries. Each line pairs a
    # REMOVED vanilla start spell with an ADDED R3 start spell across three
    # columns:
    #   <removed id> -> <added id>   <removed vals> -> <added vals>   <removed name> -> <added name>
    #   * REMOVED = a vanilla start spell (in van_start_by_id) that the ESP
    #               overrides (in esp_by_id) with the start flag dropped.
    #   * ADDED   = an esp_start_ids spell with no vanilla counterpart.
    # Removed and added lists are each sorted alphabetically by display name,
    # then zipped positionally. Uneven counts leave the missing side blank.
    def has_start_flag(obj: dict) -> bool:
        return "PC_START_SPELL" in ((obj.get("data") or {}).get("flags") or "")

    esp_by_id = {
        (o.get("id") or "").lower().strip(): o
        for o in data if o.get("type") == "Spell" and o.get("id")
    }
    esp_start_ids = {k for k, o in esp_by_id.items() if has_start_flag(o)}

    # REMOVED: vanilla start spells whose flag the ESP override drops
    # (vanilla records, from van_start_by_id).
    removed = [
        van_start_by_id[k] for k in van_start_by_id
        if k in esp_by_id and not has_start_flag(esp_by_id[k])
    ]
    # ADDED: ESP start spells with no vanilla counterpart (ESP records).
    added = [esp_by_id[k] for k in esp_start_ids if k not in van_start_by_id]

    def start_display_name(rec: dict) -> str:
        return (rec.get("name") or rec.get("id") or "")

    def start_pair_values(rem: dict | None, add: dict | None) -> str:
        """Render the paired "removed -> added" value token for the first effect
        of each side, symmetric per the steering rule: magnitude/duration always
        on both sides; range, area (ft), and cost each shown on BOTH sides when
        they differ between the two sides and on NEITHER side when equal. Token
        order per side: mag/dur/ft/range [cost]."""
        rem_eff = (rem.get("effects") or [None])[0] if rem else None
        add_eff = (add.get("effects") or [None])[0] if add else None

        # Compare axes between the two sides; show on both or neither.
        if rem_eff is not None and add_eff is not None:
            show_range = rem_eff.get("range", "") != add_eff.get("range", "")
            show_area = int(rem_eff.get("area", 0)) != int(add_eff.get("area", 0))
        else:
            show_range = False
            show_area = False

        rem_tok = (format_effect(rem_eff, show_area=show_area, show_range=show_range)
                   if rem_eff is not None else "")
        add_tok = (format_effect(add_eff, show_area=show_area, show_range=show_range)
                   if add_eff is not None else "")

        # Cost axis: compute each side's spell cost; show the bracket on both
        # sides when they differ, on neither when equal (or either missing).
        rem_cost = cost_label(rem)
        add_cost = cost_label(add)
        if rem_cost is not None and add_cost is not None and rem_cost != add_cost:
            if rem_tok:
                rem_tok = f"{rem_tok} [{rem_cost}]"
            if add_tok:
                add_tok = f"{add_tok} [{add_cost}]"

        return f"{rem_tok} -> {add_tok}"

    if removed or added:
        header("## Starting Spells")
        removed_sorted = sorted(removed, key=lambda r: start_display_name(r).lower())
        added_sorted = sorted(added, key=lambda r: start_display_name(r).lower())
        out.append("```")
        for i in range(max(len(removed_sorted), len(added_sorted))):
            rem = removed_sorted[i] if i < len(removed_sorted) else None
            add = added_sorted[i] if i < len(added_sorted) else None
            rem_id = rem.get("id") if rem else ""
            add_id = add.get("id") if add else ""
            rem_name = start_display_name(rem) if rem else ""
            add_name = start_display_name(add) if add else ""
            id_seg = f"{rem_id} -> {add_id}"
            values_seg = start_pair_values(rem, add)
            name_seg = f"{rem_name} -> {add_name}"
            line = add_at_column(id_seg, COL_VALUES, values_seg)
            line = add_at_column(line, COL_ID, name_seg)
            out.append(line)
        out.append("```")
        out.append("")

    for school in sorted(groups):
        header(f"## {school}")
        # Sort effects by their display name so the section reads naturally.
        for fx in sorted(groups[school], key=effect_base_name):
            recs = groups[school][fx]
            header(f"### {effect_base_name(fx)}")

            meta = fx_meta.get(fx)
            cur_cost = fmt_num(meta["base_cost"]) if meta else None
            van_cost = fx_van_cost.get(fx)
            van_cost = fmt_num(van_cost) if van_cost is not None else None
            if cur_cost is not None and van_cost is not None and van_cost != cur_cost:
                cb = f"{van_cost} -> {cur_cost}"
            else:
                cb = cur_cost if cur_cost is not None else van_cost
            if cb is not None:
                out.append("```")
                out.append(add_at_column("Base Cost", COL_VALUES, cb))
                out.append("```")

            def block(title: str | None, items: list) -> None:
                if not items:
                    return
                # Exactly one blank line before each block.
                if out and out[-1] != "":
                    out.append("")
                if title:
                    out.append(f"*{title}*")
                out.append("```")
                for r in sorted(items, key=sort_key):
                    out.extend(emit_record(r))
                out.append("```")

            # Vanilla records: "Vanilla" label. TD records: "Tamriel Data" label.
            block("Vanilla",
                  [r for r in recs if r.get("type") == "Spell" and not is_td(r)])
            block("Tamriel Data",
                  [r for r in recs if r.get("type") == "Spell" and is_td(r)])

            out.append("")

    if multi:
        header("## Multi-Effect Spells")

        def multi_block(title: str | None, items: list) -> None:
            if not items:
                return
            if title:
                out.append(f"*{title}*")
            out.append("```")
            for r in sorted(items, key=sort_key):
                out.extend(emit_record(r))
            out.append("```")
            out.append("")

        multi_block("Vanilla",
                    [r for r in multi if r.get("type") == "Spell" and not is_td(r)])
        multi_block("Tamriel Data",
                    [r for r in multi if r.get("type") == "Spell" and is_td(r)])

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    # Strip trailing blank lines, then write without a trailing newline.
    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    print()
    print(f"Wrote README to: {args.out}")
    print(f"  Schools        : {len(groups)}")
    print(f"  Multi-effect   : {len(multi)}")
    print(f"  Settings       : {len(settings)}")
    print(f"  Vanilla matched: {len(van_by_id)} of {len(needed_ids)} needed ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())

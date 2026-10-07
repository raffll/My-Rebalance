#!/usr/bin/env python3
"""Races & Birthsigns README generator.

Per Race and per Birthsign, two blocks show the full state of each version so
added/removed abilities are visible by their presence/absence (no annotations):
    ### <name>
    *Vanilla*   skill bonuses + Abilities/Powers/Spells (from the master record)
    *Current*   skill bonuses + Abilities/Powers/Spells (from the ESP record)

Spell category = the granted spell's data.spell_type (Ability/Power/Spell).
Ability effects show magnitude only (always-on, duration is meaningless).

Line grid: col 0 label - col 44 values - (effect rows indented).
Output: R3 - Races & Birthsigns.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

SPELL_TYPE_GROUP = {"Ability": "Abilities", "Power": "Powers", "Spell": "Spells"}
GROUP_ORDER = ["Abilities", "Powers", "Spells"]


def eff_value(eff: dict, is_ability: bool = False) -> str:
    mn = int(eff.get("min_magnitude", 0))
    mx = int(eff.get("max_magnitude", 0))
    dur = int(eff.get("duration", 0))
    area = int(eff.get("area", 0))
    mag = f"{mn}" if mn == mx else f"{mn}-{mx}"
    # Abilities are always-on: duration is meaningless, show magnitude only.
    if is_ability:
        v = mag
    else:
        v = f"{mag}/{dur}s" if dur > 0 else mag
    if area > 0:
        v = f"{v}/{area}ft"
    return v


SKILL_IDS = ["Strength", "Intelligence", "Willpower", "Agility",
             "Speed", "Endurance", "Personality", "Luck"]


def main() -> int:
    ap = argparse.ArgumentParser(description="Races & Birthsigns README generator.")
    ap.add_argument("--json", default="R3 - Races & Birthsigns.json")
    ap.add_argument("--out", default="R3 - Races & Birthsigns.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # ESP lookups.
    esp_spells: dict[str, dict] = {}
    races: list = []
    signs: list = []
    for o in data:
        t = o.get("type")
        if t == "Spell" and o.get("id"):
            esp_spells[o["id"].lower().strip()] = o
        elif t == "Race":
            races.append(o)
        elif t == "Birthsign":
            signs.append(o)

    # Which spell ids do we need vanilla data for? Every spell referenced by a
    # race/birthsign. Many custom race spells have new ids but share a vanilla
    # spell's display name, so collect names too for a name-based fallback.
    referenced: set[str] = set()
    referenced_names: set[str] = set()
    for o in races + signs:
        for sid in (o.get("spells") or []):
            k = sid.lower().strip()
            referenced.add(k)
            sp = esp_spells.get(k)
            if sp and sp.get("name"):
                referenced_names.add(sp["name"].strip().lower())

    want_types = {"Race", "Birthsign"}
    # First pass: load vanilla race/birthsign records so we can also gather the
    # spell ids *they* reference (the vanilla ability/power/spell ids differ
    # from the ESP's custom ids).
    van_typed, _, _ = gc.load_vanilla_typed(
        args.master_dir, want_types, set(), set(), masters=gc.BASE_MASTERS)
    for (t, k), rec in van_typed.items():
        for sid in (rec.get("spells") or []):
            referenced.add(sid.lower().strip())

    # Second pass: load every referenced spell (ESP + vanilla ids) by id, plus
    # by name for the current-vs-vanilla name fallback.
    _, van_spells, van_spells_by_name = gc.load_vanilla_typed(
        args.master_dir, set(), referenced, referenced_names, masters=gc.BASE_MASTERS)
    # Effect display names.
    _, effect_names = gc.load_vanilla(args.master_dir, set(), want_effect_names=True,
                                      masters=gc.BASE_MASTERS)

    def resolve_spell(sid: str):
        k = sid.lower().strip()
        return esp_spells.get(k) or van_spells.get(k)

    def van_spell(sid: str):
        """Vanilla spell for diffing: match by id, else by the ESP spell's
        display name (custom race spells reuse vanilla names under new ids)."""
        k = sid.lower().strip()
        if k in van_spells:
            return van_spells[k]
        sp = esp_spells.get(k)
        if sp and sp.get("name"):
            return van_spells_by_name.get(sp["name"].strip().lower())
        return None

    def effect_label(eff: dict) -> str:
        fx = eff.get("magic_effect", "") or ""
        base = effect_names.get(fx, gc.split_camel(fx))
        skill = eff.get("skill")
        attr = eff.get("attribute")
        if skill and skill != "None":
            base += f": {gc.split_camel(skill)}"
        elif attr and attr != "None":
            base += f": {gc.split_camel(attr)}"
        return base

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Races & Birthsigns")
    out.append("")

    def header(text):
        out.append(gc.DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    def spell_by_id_any(sid: str, vanilla: bool):
        """Resolve a spell id. For the Current block prefer ESP; for the
        Vanilla block use masters only."""
        k = sid.lower().strip()
        if vanilla:
            return van_spells.get(k)
        return esp_spells.get(k) or van_spells.get(k)

    def skill_map(record):
        """skill name -> bonus, preserving order, skipping None."""
        sb = (record.get("data") or {}).get("skill_bonuses") or {}
        m = {}
        for i in range(7):
            s = sb.get(f"skill_{i}")
            if s and s != "None":
                m[s] = sb.get(f"bonus_{i}")
        return m

    def skill_lines(current, vanilla):
        """One line per skill: vanilla -> current (shown once, not per block)."""
        cur_m = skill_map(current)
        van_m = skill_map(vanilla) if vanilla else {}
        lines = []
        for s, cur in cur_m.items():
            lines.append(gc.add_at_column(gc.split_camel(s), gc.COL_VALUES,
                                          gc.arrow(van_m.get(s), cur)))
        return lines

    def spell_block_lines(record, vanilla: bool):
        """Lines for the Abilities/Powers/Spells of one race/birthsign version."""
        groups: dict[str, list] = {"Abilities": [], "Powers": [], "Spells": []}
        for sid in (record.get("spells") or []):
            sp = spell_by_id_any(sid, vanilla)
            st = ((sp or {}).get("data") or {}).get("spell_type") if sp else None
            grp = SPELL_TYPE_GROUP.get(st, "Spells")
            groups[grp].append((sid, sp))

        lines = []
        for grp in GROUP_ORDER:
            if not groups[grp]:
                continue
            lines.append(grp)
            for sid, sp in groups[grp]:
                if not sp:
                    lines.append(f"    {sid}  (spell not found)")
                    continue
                lines.append(f"    {sp.get('name') or sid}")
                is_ability = ((sp.get("data") or {}).get("spell_type") == "Ability")
                for eff in sp.get("effects") or []:
                    label = gc.EFFECT_INDENT * 2 + effect_label(eff)
                    lines.append(gc.add_at_column(label, gc.COL_VALUES,
                                                  eff_value(eff, is_ability)))
            lines.append("")
        while lines and lines[-1] == "":
            lines.pop()
        return lines

    def labeled_block(title, lines):
        out.append(f"*{title}*")
        out.append("```")
        out.extend(lines)
        out.append("```")
        out.append("")

    def plain_block(lines):
        out.append("```")
        out.extend(lines)
        out.append("```")
        out.append("")

    def emit_entity(o, kind: str):
        name = o.get("name") or o.get("id")
        header(f"### {name}")
        vo = van_typed.get((kind, (o.get("id") or "").lower().strip()))

        # Skill bonuses once, with vanilla -> current (races only).
        if kind == "Race":
            sl = skill_lines(o, vo)
            if sl:
                plain_block(sl)

        van_spells_lines = spell_block_lines(vo, vanilla=True) if vo else []
        cur_spells_lines = spell_block_lines(o, vanilla=False)

        # If the ability/power/spell content is identical (nothing changed),
        # show a single unlabeled block; otherwise show both versions.
        if van_spells_lines == cur_spells_lines:
            if cur_spells_lines:
                plain_block(cur_spells_lines)
        else:
            if van_spells_lines:
                labeled_block("Vanilla", van_spells_lines)
            if cur_spells_lines:
                labeled_block("Current", cur_spells_lines)

    header("## Races")
    for o in sorted(races, key=lambda x: (x.get("name") or x.get("id") or "")):
        emit_entity(o, "Race")

    header("## Birthsigns")
    for o in sorted(signs, key=lambda x: (x.get("name") or x.get("id") or "")):
        emit_entity(o, "Birthsign")

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))

    print(f"Wrote {args.out}")
    print(f"  Races: {len(races)}  Birthsigns: {len(signs)}  ESP spells: {len(esp_spells)}")
    print(f"  Vanilla races/signs matched: {len(van_typed)}  vanilla spells: {len(van_spells)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

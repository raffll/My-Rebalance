#!/usr/bin/env python3
"""Core README generator.

The editorial layout of README - Core.md is baked in, extended so that NOTHING
is omitted: every record lands in a section, and any record not explicitly
placed is dumped into "## Other Records" at the end (expected to be empty).

Values and vanilla (-> ) sides come from JSON + masters.

Line: id (col 0) - vanilla -> current (col 44) - name (col 80)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common as gc

ATTRIBUTES = ["Strength", "Intelligence", "Willpower", "Agility",
              "Speed", "Endurance", "Personality", "Luck"]

# Baked-in GameSetting section map (mirrors README - Core.md).
GMST_SECTIONS = [
    ("Skills", ["fLevelUpHealthEndMult"]),
    ("Movement", ["fMinWalkSpeed", "fMaxWalkSpeed",
                  "fMinWalkSpeedCreature", "fMaxWalkSpeedCreature"]),
    ("Barter", ["fBarterGoldResetDelay", "fMagesGuildTravel"]),
    ("Crime", ["iCrimeKilling", "iCrimeAttack", "iCrimePickPocket",
               "iCrimeTresspass", "iDaysinPrisonMod"]),
    ("Pickpocket", ["iPickMaxChance", "fPickPocketMod"]),
    ("Lockpicking", ["fPickLockMult"]),
    ("Traps", ["fTrapCostMult"]),
    ("Alchemy", ["fPotionStrengthMult"]),
    ("Enchant", ["fMagicItemRechargePerSecond", "fEnchantmentChanceMult"]),
]

MERCHANT_CREATURES = ["scamp_creeper", "mudcrab_unique"]
APPARATUS_IDS = ["apparatus_sm_mortar_01", "apparatus_sm_alembic_01",
                 "apparatus_sm_calcinator_01", "apparatus_sm_retort_01"]
LOCK_SPELL_IDS = ["ondusi's open door", "strong open", "great open"]
# Scrolls documented under Lockpicking (Book = price, Enchanting = magnitude).
SCROLL_BOOK_IDS = ["sc_ondusisunhinging"]
SCROLL_ENCH_IDS = ["sc_ekashslocksplitter_en"]
# Trap spells: cost is what changed; order matches README.
TRAP_IDS = [
    "trap_fire00", "trap_frost00", "trap_shock00", "trap_health00",
    "trap_poison00", "trap_paralyze00", "trap_silence00",
    "trap_fire_killer", "trap_frost_killer", "trap_shock_killer",
    "trap_poison_killer",
]


def gv(o):
    return (o.get("value") or {}).get("data")


def main() -> int:
    ap = argparse.ArgumentParser(description="Core README generator.")
    ap.add_argument("--json", default="R3 - Core.json")
    ap.add_argument("--out", default="R3 - Core.md")
    ap.add_argument("--master-dir", default=gc.DEFAULT_MASTER_DIR)
    args = ap.parse_args()

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    by_id = {o["id"].lower().strip(): o for o in data if o.get("id")}
    needed = set(by_id.keys())
    van_by_id, _ = gc.load_vanilla(args.master_dir, needed)

    # Vanilla MagicEffect base costs (keyed by effect_id) and Skill records
    # (keyed by skill_id) - these record types have no `id`, so they are not
    # captured by the id-based vanilla loader.
    van_effect_cost: dict[str, float] = {}
    van_skill: dict[str, dict] = {}
    for mname in gc.MASTER_FILES:
        mpath = os.path.join(args.master_dir, mname)
        if not os.path.exists(mpath):
            continue
        for o in gc.read_records(mpath):
            if not isinstance(o, dict):
                continue
            if o.get("type") == "MagicEffect" and o.get("effect_id"):
                eid = o["effect_id"]
                if eid not in van_effect_cost:
                    van_effect_cost[eid] = (o.get("data") or {}).get("base_cost")
            elif o.get("type") == "Skill" and o.get("skill_id"):
                sid = o["skill_id"].lower()
                if sid not in van_skill:
                    van_skill[sid] = o

    placed: set[str] = set()

    def van(idl):
        return van_by_id.get(idl)

    def mark(idl):
        placed.add(idl)

    out: list[str] = []
    out.append("# Remastered Rebalance Redux - Core")
    out.append("")

    def header(text):
        out.append(gc.DIVIDER)
        out.append("")
        out.append(text)
        out.append("")

    def open_fence():
        out.append("```")

    def close_fence():
        out.append("```")

    def gmst_line(idl):
        o = by_id.get(idl)
        if not o:
            return None
        mark(idl)
        v = van(idl)
        return gc.add_at_column(o.get("id", idl), gc.COL_VALUES,
                                gc.arrow(gv(v) if v else None, gv(o)))

    def eff_mag(o):
        """min[-max] of the first effect (magnitude only)."""
        effs = o.get("effects") or []
        if not effs:
            return None
        e = effs[0]
        mn, mx = int(e.get("min_magnitude", 0)), int(e.get("max_magnitude", 0))
        return f"{mn}" if mn == mx else f"{mn}-{mx}"

    # Record names that are missing from the JSON (e.g. Enchanting records have
    # no name field) but documented in the README.
    NAME_OVERRIDE = {
        "sc_ekashslocksplitter_en": "Scroll of Ekash's Lock Splitter",
    }

    def display_name(o):
        idl = (o.get("id") or "").lower()
        return o.get("name") or NAME_OVERRIDE.get(idl) or o.get("id") or ""

    def rec_line(rec, value):
        """id (col 0) - value (col 44) - name (col 80)."""
        line = gc.add_at_column(rec.get("id", ""), gc.COL_VALUES, value)
        return gc.add_at_column(line, gc.COL_ID, display_name(rec))

    for title, ids in GMST_SECTIONS:
        lines = [gmst_line(i.lower()) for i in ids]
        lines = [ln for ln in lines if ln]

        # Some sections still render even if the GMST list is empty, because
        # they carry sub-blocks. Skills always has the Armorer skill.
        has_sub = title in ("Skills", "Barter", "Lockpicking", "Traps", "Alchemy")
        if not lines and not has_sub:
            continue

        header(f"## {title}")
        if lines:
            open_fence()
            out.extend(lines)
            close_fence()
            out.append("")

        if title == "Skills":
            sk = next((o for o in data if o.get("type") == "Skill"
                       and (o.get("skill_id") or "").lower() == "armorer"), None)
            if sk:
                vsk = van_skill.get("armorer")
                sdata = sk.get("data") or {}
                vdata = (vsk or {}).get("data") or {}

                def attr_name(x):
                    return ATTRIBUTES[x] if isinstance(x, int) and 0 <= x < 8 else str(x)

                out.append("*Armorer*")
                open_fence()
                # Row label in col 0, value in col 44 (no col-80 name).
                cur_ga = attr_name(sdata.get("governing_attribute"))
                van_ga = attr_name(vdata.get("governing_attribute")) if vsk else None
                out.append(gc.add_at_column("Governing Attribute", gc.COL_VALUES,
                                            gc.arrow(van_ga, cur_ga)))
                # Successful Repair = actions[0]: 0.4 -> 1.
                cur_act = (sdata.get("actions") or [None])[0]
                van_act = (vdata.get("actions") or [None])[0] if vsk else None
                if cur_act is not None:
                    out.append(gc.add_at_column("Successful Repair", gc.COL_VALUES,
                                                gc.arrow(van_act, cur_act)))
                close_fence()
                out.append("")

        if title == "Crime":
            # Death Warrant feature = Script + Dialogue + DialogueInfo plumbing.
            # Emit two lines, each: real id (col 0) - value - description:
            #   DialogueInfo INAM id : PcCrimeLevel threshold (Death Warrant)
            #   Script id            : murdercost value       (Murder Cost)
            dw_ids = [o.get("id", "").lower() for o in data
                      if o.get("type") in ("Script", "Dialogue", "DialogueInfo")]
            for i in dw_ids:
                if i:
                    mark(i)

            def pccrime_threshold(rec):
                for f in ((rec or {}).get("filters") or []):
                    if f.get("function") == "PcCrimeLevel":
                        return (f.get("value") or {}).get("data")
                return None

            def murdercost(rec):
                txt = (rec or {}).get("text") or (rec or {}).get("script_text") or ""
                m = re.search(r"set murdercost to (-?\d+)", txt)
                return int(m.group(1)) if m else None

            crime_lines = []

            info = next((o for o in data if o.get("type") == "DialogueInfo"), None)
            if info:
                cur_dw = pccrime_threshold(info)
                van_dw = pccrime_threshold(van((info.get("id") or "").lower()))
                if cur_dw is not None:
                    crime_lines.append(gc.add_at_column(info.get("id", ""),
                                                        gc.COL_VALUES, gc.arrow(van_dw, cur_dw)))

            sc = next((o for o in data if o.get("type") == "Script"), None)
            if sc:
                cur_mc = murdercost(sc)
                van_mc = murdercost(van((sc.get("id") or "").lower()))
                if cur_mc is not None:
                    crime_lines.append(gc.add_at_column(sc.get("id", ""),
                                                        gc.COL_VALUES, gc.arrow(van_mc, cur_mc)))

            if crime_lines:
                if out and out[-1] == "":
                    out.pop()
                if out and out[-1] == "```":
                    out.pop()  # reopen the Crime fence to append the lines
                    out.append("")
                    out.extend(crime_lines)
                    out.append("```")
                    out.append("")

        if title == "Barter":
            recs = [by_id.get(c) for c in MERCHANT_CREATURES]
            recs = [c for c in recs if c]
            if recs:
                out.append("*Merchants Gold*")
                open_fence()
                for c in recs:
                    idl = c["id"].lower()
                    mark(idl)
                    v = van(idl)
                    vanv = (v.get("data") or {}).get("gold") if v else None
                    cur = (c.get("data") or {}).get("gold")
                    out.append(rec_line(c, gc.arrow(vanv, cur)))
                close_fence()
                out.append("")

        if title == "Lockpicking":
            # Spell Effects: the Open MagicEffect base cost (6 -> 12).
            me = next((o for o in data if o.get("type") == "MagicEffect"
                       and o.get("effect_id") == "Open"), None)
            if me:
                cur = (me.get("data") or {}).get("base_cost")
                vanb = van_effect_cost.get("Open")
                out.append("*Spell Effects*")
                open_fence()
                out.append(gc.add_at_column("Open", gc.COL_VALUES, gc.arrow(vanb, cur)))
                close_fence()
                out.append("")

            spells = [by_id.get(s) for s in LOCK_SPELL_IDS]
            spells = [s for s in spells if s]
            if spells:
                out.append("*Spell Magnitudes*")
                open_fence()
                for s in spells:
                    idl = s["id"].lower()
                    mark(idl)
                    v = van(idl)
                    cur = eff_mag(s)
                    vanv = eff_mag(v) if v else None
                    out.append(rec_line(s, gc.arrow(vanv, cur)))
                close_fence()
                out.append("")

            books = [by_id.get(b) for b in SCROLL_BOOK_IDS]
            books = [b for b in books if b]
            enchs = [by_id.get(e) for e in SCROLL_ENCH_IDS]
            enchs = [e for e in enchs if e]
            if books:
                out.append("*Scroll Prices*")
                open_fence()
                for b in books:
                    idl = b["id"].lower()
                    mark(idl)
                    v = van(idl)
                    vanv = (v.get("data") or {}).get("value") if v else None
                    cur = (b.get("data") or {}).get("value")
                    out.append(rec_line(b, gc.arrow(vanv, cur)))
                close_fence()
                out.append("")
            if enchs:
                out.append("*Scroll Magnitudes*")
                open_fence()
                for e in enchs:
                    idl = e["id"].lower()
                    mark(idl)
                    v = van(idl)
                    cur = eff_mag(e)
                    vanv = eff_mag(v) if v else None
                    out.append(rec_line(e, gc.arrow(vanv, cur)))
                close_fence()
                out.append("")

        if title == "Traps":
            traps = [by_id.get(t) for t in TRAP_IDS]
            traps = [t for t in traps if t]
            if traps:
                out.append("*Common Trap Costs*")
                open_fence()
                for t in traps:
                    idl = t["id"].lower()
                    mark(idl)
                    v = van(idl)
                    vanv = (v.get("data") or {}).get("cost") if v else None
                    cur = (t.get("data") or {}).get("cost")
                    out.append(rec_line(t, gc.arrow(vanv, cur)))
                close_fence()
                out.append("")

        if title == "Alchemy":
            apps = [by_id.get(a) for a in APPARATUS_IDS]
            apps = [a for a in apps if a]
            if apps:
                out.append("*Apparatus Prices*")
                open_fence()
                for a in apps:
                    idl = a["id"].lower()
                    mark(idl)
                    v = van(idl)
                    vanv = (v.get("data") or {}).get("value") if v else None
                    cur = (a.get("data") or {}).get("value")
                    out.append(rec_line(a, gc.arrow(vanv, cur)))
                close_fence()
                out.append("")

    # Completeness guarantee: any record with an id not placed above, plus any
    # record without an id (Skill/MagicEffect/Script/Dialogue), goes here.
    leftovers = []
    for o in data:
        if o.get("type") == "Header":
            continue
        idl = (o.get("id") or "").lower().strip()
        if idl and idl in placed:
            continue
        if o.get("type") == "Skill" and (o.get("skill_id") or "").lower() == "armorer":
            continue  # shown under Skills
        if o.get("type") == "MagicEffect" and o.get("effect_id") == "Open":
            continue  # shown under Lockpicking -> Spell Effects
        leftovers.append(o)

    if leftovers:
        header("## Other Records")
        open_fence()
        for o in leftovers:
            ident = o.get("id") or o.get("skill_id") or o.get("effect_id") or "(no id)"
            out.append(gc.add_at_column(str(o.get("type")), gc.COL_VALUES, str(ident)))
        close_fence()
        out.append("")

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    # Strip any trailing blank lines, then write without a trailing newline.
    while out and out[-1] == "":
        out.pop()
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out))

    total = sum(1 for o in data if o.get("type") != "Header")
    print(f"Wrote {args.out}")
    print(f"  Vanilla matched : {len(van_by_id)} of {len(needed)}")
    print(f"  Records placed  : {len(placed)}")
    print(f"  In Other Records: {len(leftovers)}")
    print(f"  Total records   : {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

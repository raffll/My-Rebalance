#!/usr/bin/env python3
"""Generate a markdown doc listing all player-buyable spells in
Tamriel Rebuilt / Tamriel Data, grouped by magic school.

"Buyable" = known by at least one spell merchant (an NPC whose AI services
include OFFERS_SPELLS) AND spell_type == "Spell" (abilities, powers, curses,
diseases are not sold). Spell IDs are resolved case-insensitively across the
full TR load order.

Columns per spell:
  - Spell        : display name
  - Mag          : magnitude range across effects (e.g. "30-50", "10", "-")
  - Dur          : duration (seconds) across effects
  - Cost         : spell cost (magicka) from the spell record
  - In R3?       : whether this spell ID already exists in R3 - Spells.json
  - Recalc?      : whether any of the spell's effects uses a magic effect
                   whose base cost was changed in R3 (so the spell cost /
                   mag / dur would need recomputation if we imported it).
                   Marks no-scale effects (Fire/Frost/Shock/Poison) separately
                   since those only need a cost/rounding fix, not scaling.

Usage:
    python gen_buyable_spells_doc.py [--out PATH] [--tr-only]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

TES3CONV_DIR = r"c:\OMEN\Morrowind\tes3conv"
MOD_DIR = r"c:\OMEN\Morrowind\MO2\mods\Remastered Rebalance Redux"
R3_SPELLS_JSON = os.path.join(MOD_DIR, "R3 - Spells.json")

LOAD_ORDER = [
    "Morrowind.json",
    "Tribunal.json",
    "Bloodmoon.json",
    "Tamriel_Data.json",
    "TR_Mainland.json",
    "Cyr_Main.json",
    "Sky_Main.json",
]

# Masters that establish the vanilla/TD baseline base cost for each effect.
BASELINE_FILES = ["Morrowind.json", "Tribunal.json", "Bloodmoon.json",
                  "Tamriel_Data.json"]

TR_PROVINCE_FILES = {"TR_Mainland.json", "Cyr_Main.json", "Sky_Main.json"}
SPELL_SERVICE = "OFFERS_SPELLS"
BUYABLE_SPELL_TYPE = "Spell"

DEFAULT_OUT = os.path.join(MOD_DIR, "docs", "TR-Buyable-Spells.md")

# Effects that do NOT get spell-compensation scaling on a base-cost change
# (per spell-value-rules "No-Scale Effects"). A base-cost change here only
# affects spell cost + rounding, not magnitude/duration scaling.
NO_SCALE_EFFECTS = {"FireDamage", "FrostDamage", "ShockDamage", "Poison"}

# Canonical Morrowind magic-effect -> school map (tes3conv CamelCase names).
EFFECT_SCHOOL = {
    # Alteration
    "Burden": "Alteration", "Feather": "Alteration",
    "FireShield": "Alteration", "FrostShield": "Alteration",
    "LightningShield": "Alteration", "Jump": "Alteration",
    "Levitate": "Alteration", "Lock": "Alteration", "Open": "Alteration",
    "SlowFall": "Alteration", "SwiftSwim": "Alteration",
    "WaterBreathing": "Alteration", "WaterWalking": "Alteration",
    "Shield": "Alteration",
    # Conjuration
    "BoundBattleAxe": "Conjuration", "BoundBoots": "Conjuration",
    "BoundCuirass": "Conjuration", "BoundDagger": "Conjuration",
    "BoundGloves": "Conjuration", "BoundHelm": "Conjuration",
    "BoundLongbow": "Conjuration", "BoundLongsword": "Conjuration",
    "BoundMace": "Conjuration", "BoundShield": "Conjuration",
    "BoundSpear": "Conjuration", "SummonBear": "Conjuration",
    "SummonBoneWolf": "Conjuration", "SummonBonelord": "Conjuration",
    "SummonCenturionSphere": "Conjuration", "SummonClannfear": "Conjuration",
    "SummonDaedroth": "Conjuration", "SummonDremora": "Conjuration",
    "SummonFlameAtronach": "Conjuration", "SummonFrostAtronach": "Conjuration",
    "SummonGhost": "Conjuration", "SummonGoldenSaint": "Conjuration",
    "SummonGreaterBonewalker": "Conjuration", "SummonHunger": "Conjuration",
    "SummonLeastBonewalker": "Conjuration", "SummonScamp": "Conjuration",
    "SummonSkeleton": "Conjuration", "SummonStormAtronach": "Conjuration",
    "SummonTwilight": "Conjuration", "SummonWolf": "Conjuration",
    "SummonFabricant": "Conjuration",
    "TurnUndead": "Conjuration", "CommandCreature": "Conjuration",
    "CommandHumanoid": "Conjuration",
    # Destruction
    "AbsorbAttribute": "Destruction", "AbsorbFatigue": "Destruction",
    "AbsorbHealth": "Destruction", "AbsorbMagicka": "Destruction",
    "AbsorbSkill": "Destruction", "DamageAttribute": "Destruction",
    "DamageFatigue": "Destruction", "DamageHealth": "Destruction",
    "DamageMagicka": "Destruction", "DamageSkill": "Destruction",
    "DisintegrateArmor": "Destruction", "DisintegrateWeapon": "Destruction",
    "DrainAttribute": "Destruction", "DrainFatigue": "Destruction",
    "DrainHealth": "Destruction", "DrainMagicka": "Destruction",
    "DrainSkill": "Destruction", "FireDamage": "Destruction",
    "FrostDamage": "Destruction", "ShockDamage": "Destruction",
    "Poison": "Destruction", "SunDamage": "Destruction",
    "WeaknessToBlightDisease": "Destruction",
    "WeaknessToCommonDisease": "Destruction",
    "WeaknessToCorprus": "Destruction", "WeaknessToFire": "Destruction",
    "WeaknessToFrost": "Destruction", "WeaknessToMagicka": "Destruction",
    "WeaknessToNormalWeapons": "Destruction",
    "WeaknessToPoison": "Destruction", "WeaknessToShock": "Destruction",
    # Illusion
    "CalmCreature": "Illusion", "CalmHumanoid": "Illusion",
    "Chameleon": "Illusion", "DemoralizeCreature": "Illusion",
    "DemoralizeHumanoid": "Illusion", "FrenzyCreature": "Illusion",
    "FrenzyHumanoid": "Illusion", "Invisibility": "Illusion",
    "Light": "Illusion", "NightEye": "Illusion", "Paralyze": "Illusion",
    "RallyCreature": "Illusion", "RallyHumanoid": "Illusion",
    "Silence": "Illusion", "Sanctuary": "Illusion", "Blind": "Illusion",
    "Sound": "Illusion", "Charm": "Illusion",
    # Mysticism
    "AlmsiviIntervention": "Mysticism", "DetectAnimal": "Mysticism",
    "DetectEnchantment": "Mysticism", "DetectKey": "Mysticism",
    "DivineIntervention": "Mysticism", "Mark": "Mysticism",
    "Recall": "Mysticism", "Reflect": "Mysticism",
    "SoulTrap": "Mysticism", "SpellAbsorption": "Mysticism",
    "StuntedMagicka": "Mysticism", "Telekinesis": "Mysticism",
    "Dispel": "Mysticism",
    # Restoration
    "CureBlightDisease": "Restoration", "CureCommonDisease": "Restoration",
    "CureCorprus": "Restoration", "CureParalyzation": "Restoration",
    "CurePoison": "Restoration", "FortifyAttackBonus": "Restoration",
    "FortifyAttribute": "Restoration", "FortifyFatigue": "Restoration",
    "FortifyHealth": "Restoration", "FortifyMagicka": "Restoration",
    "FortifyMagickaMultiplier": "Restoration", "FortifySkill": "Restoration",
    "RestoreAttribute": "Restoration", "RestoreFatigue": "Restoration",
    "RestoreHealth": "Restoration", "RestoreMagicka": "Restoration",
    "RestoreSkill": "Restoration", "ResistBlightDisease": "Restoration",
    "ResistCommonDisease": "Restoration", "ResistCorprus": "Restoration",
    "ResistFire": "Restoration", "ResistFrost": "Restoration",
    "ResistMagicka": "Restoration", "ResistNormalWeapons": "Restoration",
    "ResistParalysis": "Restoration", "ResistPoison": "Restoration",
    "ResistShock": "Restoration", "RemoveCurse": "Restoration",
    # Misc / special
    "Corprus": "Other", "Vampirism": "Other",
}

SCHOOL_ORDER = ["Alteration", "Conjuration", "Destruction", "Illusion",
                "Mysticism", "Restoration", "Other"]


def load(path):
    if not os.path.exists(path):
        print(f"WARNING: missing {path}", file=sys.stderr)
        return []
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def mag_range(effects):
    """Collapse all effect magnitudes into one display string.

    Shows per-effect min-max joined by ' / ' when a spell has multiple
    effects. Effects whose min==max show a single number.
    """
    parts = []
    for e in effects:
        lo = e.get("min_magnitude", 0)
        hi = e.get("max_magnitude", 0)
        if lo == hi:
            parts.append(str(lo))
        else:
            parts.append(f"{lo}-{hi}")
    return " / ".join(parts) if parts else "-"


def dur_range(effects):
    durs = [e.get("duration", 0) for e in effects]
    if not durs:
        return "-"
    uniq = []
    for d in durs:
        if d not in uniq:
            uniq.append(d)
    return " / ".join(str(d) for d in uniq)


def recalc_flag(effects, changed_effects):
    """Return a short label describing whether this spell needs a recalc.

    - "Yes"        : at least one scalable effect's base cost changed
    - "Cost only"  : only no-scale effects (Fire/Frost/Shock/Poison) changed
    - "-"          : no effect's base cost changed
    """
    hit_scale = False
    hit_noscale = False
    for e in effects:
        eid = e.get("magic_effect")
        if eid in changed_effects:
            if eid in NO_SCALE_EFFECTS:
                hit_noscale = True
            else:
                hit_scale = True
    if hit_scale:
        return "Yes"
    if hit_noscale:
        return "Cost only"
    return "-"


def build_table(rows, headers, aligns):
    """Build a space-padded markdown table. aligns: 'l' or 'r' per column."""
    cols = len(headers)
    widths = [len(h) for h in headers]
    for r in rows:
        for i in range(cols):
            widths[i] = max(widths[i], len(r[i]))

    def fmt_row(cells):
        out = []
        for i, c in enumerate(cells):
            if aligns[i] == "r":
                out.append(c.rjust(widths[i]))
            else:
                out.append(c.ljust(widths[i]))
        return "| " + " | ".join(out) + " |"

    sep = []
    for i in range(cols):
        if aligns[i] == "r":
            sep.append("-" * (widths[i] - 1) + ":")
        else:
            sep.append("-" * widths[i])
    lines = [fmt_row(headers), "| " + " | ".join(sep) + " |"]
    lines += [fmt_row(r) for r in rows]
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--tr-only", action="store_true",
                    help="only merchants defined in TR province plugins")
    args = ap.parse_args()

    # Load spells + NPCs across the whole load order.
    spells_by_id = {}
    npcs = []
    for fname in LOAD_ORDER:
        for rec in load(os.path.join(TES3CONV_DIR, fname)):
            if rec["type"] == "Spell":
                spells_by_id[rec["id"].lower()] = rec
            elif rec["type"] == "Npc":
                npcs.append((fname, rec))

    # Baseline base costs (vanilla + TD).
    baseline = {}
    for fname in BASELINE_FILES:
        for rec in load(os.path.join(TES3CONV_DIR, fname)):
            if rec["type"] == "MagicEffect":
                baseline[rec["effect_id"]] = rec["data"]["base_cost"]

    # R3 spell ids + R3 magic-effect base costs.
    r3_data = load(R3_SPELLS_JSON)
    r3_spell_ids = {r["id"].lower() for r in r3_data if r["type"] == "Spell"}
    r3_effect_cost = {r["effect_id"]: r["data"]["base_cost"]
                      for r in r3_data if r["type"] == "MagicEffect"}

    # Which effects changed base cost in R3 vs baseline.
    changed_effects = {}
    for eid, cost in r3_effect_cost.items():
        base = baseline.get(eid)
        if base is None or abs(base - cost) > 1e-9:
            changed_effects[eid] = (base, cost)

    # Collect buyable spells.
    buyable = {}
    for fname, npc in npcs:
        if SPELL_SERVICE not in ((npc.get("ai_data") or {}).get("services") or ""):
            continue
        if args.tr_only and fname not in TR_PROVINCE_FILES:
            continue
        for sid in npc.get("spells", []):
            rec = spells_by_id.get(sid.lower())
            if rec and rec["data"].get("spell_type") == BUYABLE_SPELL_TYPE:
                buyable[rec["id"].lower()] = rec

    # Group by school (first effect).
    by_school = {s: [] for s in SCHOOL_ORDER}
    unknown = set()
    for rec in buyable.values():
        effects = rec.get("effects") or []
        first = effects[0]["magic_effect"] if effects else ""
        school = EFFECT_SCHOOL.get(first, "Other")
        if first and first not in EFFECT_SCHOOL:
            unknown.add(first)
        by_school[school].append(rec)
    if unknown:
        print("Unmapped first-effects (under Other):",
              ", ".join(sorted(unknown)), file=sys.stderr)

    # Build the document.
    lines = []
    lines.append("# Player-Buyable Spells — Tamriel Rebuilt / Tamriel Data\n")
    scope = ("merchants placed in the TR province plugins "
             "(TR_Mainland, Cyr_Main, Sky_Main)" if args.tr_only
             else "all spell merchants in the TR load order")
    lines.append(
        "Every spell sold by at least one spell merchant "
        f"({scope}). A spell is listed when an NPC with the `OFFERS_SPELLS` "
        "service knows it and its record is of type `Spell` (abilities, "
        "powers, curses and diseases are excluded).\n"
    )
    lines.append(f"**Total unique buyable spells: {len(buyable)}**\n")

    # Count recalc flags for the summary.
    total_in_r3 = total_recalc = total_costonly = 0
    for rec in buyable.values():
        if rec["id"].lower() in r3_spell_ids:
            total_in_r3 += 1
        flag = recalc_flag(rec.get("effects") or [], changed_effects)
        if flag == "Yes":
            total_recalc += 1
        elif flag == "Cost only":
            total_costonly += 1
    lines.append(
        f"- Already in `R3 - Spells.json`: **{total_in_r3}**\n"
        f"- Need recalc (scalable effect base cost changed): **{total_recalc}**\n"
        f"- Cost-only fix (no-scale effect base cost changed): "
        f"**{total_costonly}**\n"
    )

    lines.append("## Legend\n")
    lines.append("- **Mag**: per-effect magnitude; `30-50` is a min-max range, "
                 "multiple effects joined by ` / `.")
    lines.append("- **Dur**: effect duration in seconds.")
    lines.append("- **Cost**: spell magicka cost from the record.")
    lines.append("- **In R3**: `Y` if this exact spell ID already exists in "
                 "`R3 - Spells.json`.")
    lines.append("- **Recalc**: `Yes` = a scalable effect's base cost changed "
                 "in R3, so mag/dur/cost need recomputation. `Cost only` = "
                 "only a no-scale effect (Fire/Frost/Shock/Poison) changed, so "
                 "just cost/rounding. `-` = no base-cost change.\n")

    headers = ["Spell", "Mag", "Dur", "Cost", "In R3", "Recalc", "ID"]
    aligns = ["l", "r", "r", "r", "l", "l", "l"]

    for school in SCHOOL_ORDER:
        recs = by_school[school]
        if not recs:
            continue
        recs.sort(key=lambda r: (r.get("name", "") or "").lower())
        lines.append(f"## {school} ({len(recs)})\n")
        rows = []
        for rec in recs:
            effects = rec.get("effects") or []
            name = (rec.get("name", "") or "").replace("|", "\\|")
            rid = rec["id"].replace("|", "\\|")
            cost = rec["data"].get("cost", "?")
            in_r3 = "Y" if rec["id"].lower() in r3_spell_ids else "-"
            flag = recalc_flag(effects, changed_effects)
            rows.append([
                name,
                mag_range(effects),
                dur_range(effects),
                str(cost),
                in_r3,
                flag,
                f"`{rid}`",
            ])
        lines += build_table(rows, headers, aligns)
        lines.append("")

    # Missing-spells worklist: buyable spells NOT already in R3 whose effects
    # use a changed base cost, so they are worth considering for R3.
    missing = []
    for rec in buyable.values():
        if rec["id"].lower() in r3_spell_ids:
            continue
        effects = rec.get("effects") or []
        flag = recalc_flag(effects, changed_effects)
        if flag == "-":
            continue  # no changed base cost -> nothing to reconsider
        first = effects[0]["magic_effect"] if effects else ""
        school = EFFECT_SCHOOL.get(first, "Other")
        missing.append((school, rec, flag))

    lines.append("## Missing Spells to Consider\n")
    lines.append(
        "Buyable spells **not** yet in `R3 - Spells.json` whose effects use a "
        "magic effect we rebalanced. These are the candidates to review for "
        "import/adjustment; spells with no changed base cost are omitted since "
        "they need no attention.\n"
    )
    lines.append(f"**Total to consider: {len(missing)}** "
                 f"(of {len(buyable) - total_in_r3} spells missing from R3).\n")

    miss_headers = ["Spell", "School", "Mag", "Dur", "Cost", "Recalc", "ID"]
    miss_aligns = ["l", "l", "r", "r", "r", "l", "l"]
    miss_rows = []
    for school, rec, flag in sorted(
            missing,
            key=lambda x: (SCHOOL_ORDER.index(x[0]),
                           (x[1].get("name", "") or "").lower())):
        effects = rec.get("effects") or []
        name = (rec.get("name", "") or "").replace("|", "\\|")
        rid = rec["id"].replace("|", "\\|")
        miss_rows.append([
            name,
            school,
            mag_range(effects),
            dur_range(effects),
            str(rec["data"].get("cost", "?")),
            flag,
            f"`{rid}`",
        ])
    lines += build_table(miss_rows, miss_headers, miss_aligns)
    lines.append("")

    # Appendix: which effects changed base cost (drives the Recalc column).
    lines.append("## Appendix — Changed Base Costs (R3 vs vanilla/TD)\n")
    ap_rows = []
    for eid in sorted(changed_effects):
        base, cost = changed_effects[eid]
        noscale = "yes" if eid in NO_SCALE_EFFECTS else "-"
        ap_rows.append([eid, "n/a" if base is None else str(base),
                        str(cost), noscale])
    lines += build_table(
        ap_rows,
        ["Effect", "Base (vanilla/TD)", "Base (R3)", "No-Scale"],
        ["l", "r", "r", "l"],
    )
    lines.append("")

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"Wrote {args.out} ({len(buyable)} spells, "
          f"{total_in_r3} in R3, {total_recalc} recalc, "
          f"{total_costonly} cost-only, "
          f"{len(missing)} to consider)")


if __name__ == "__main__":
    main()

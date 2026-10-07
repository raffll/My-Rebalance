# Magic Effect Magnitude / Duration Flags

Quick-reference for which magic effects have **no magnitude** or **no duration**,
so values are not scaled or tiered on an axis the effect does not use.

Classification taken from the UESP Morrowind spell-effect descriptions
(en.uesp.net/wiki/Morrowind:Magic_Effects). Content was rephrased for compliance
with licensing restrictions. The machine-readable source of truth is
`scripts/effect_axis_flags.json`; the generators read it via `gen_common.py`.

The UESP intro states directly: effects related to **curing, summoning,
teleportation, water breathing and water walking have no magnitude**. Individual
pages add the rest (Paralyze "no magnitude, only duration"; Invisibility
magnitude "is not variable"; Lock "has no duration"; teleports "instantaneous").

## Why this matters for editing

- **Duration-only** (no magnitude): magnitude is fixed at 1. Scale/tier the
  **duration** only. Never put a tier *magnitude* value on these. (This is the
  Silence / Paralyze case — tier table "duration column only".)
- **Magnitude-only** (no duration): duration is fixed at 0. Scale the
  **magnitude** only. Never put a scaled *duration* on these.
- **Neither** (instant toggle): no magnitude and no duration. Nothing to scale.

When editing a record, check this list first and only touch the axis the effect
actually uses.

---

## Duration-only — No Magnitude (magnitude is always 1)

| Effect           | School     | Notes                                       |
|------------------|------------|---------------------------------------------|
| Silence          | Illusion   | Blocks casting for the duration.            |
| Paralyze         | Illusion   | "No magnitude, only duration."              |
| Invisibility     | Illusion   | Magnitude not variable (always 100%).       |
| Water Breathing  | Alteration | Breathe underwater for the duration.        |
| Water Walking    | Alteration | Walk on water for the duration.             |
| **All Summon\*** | Conjuration| Summon creature for the duration.           |
| **All Bound\***  | Conjuration| Bound weapon/armor for the duration.        |

For these, use the **duration column only** of the potion tier table; for spells,
apply duration scaling only (never a magnitude range).

---

## Magnitude-only — No Duration (duration is always 0, effect is instant)

| Effect  | School     | Notes                                              |
|---------|------------|----------------------------------------------------|
| Lock    | Alteration | Magnitude = lock level applied. "Has no duration." |
| Open    | Alteration | Magnitude = highest lock level opened. Instant.    |
| Dispel  | Mysticism  | Magnitude = % chance to remove each effect. Instant.|

Scale the magnitude only. (Lock/Open magnitudes are lock levels, effectively
fixed per record.)

---

## Neither axis — instant toggle (No Magnitude AND No Duration)

| Effect               | School      | Notes                                 |
|----------------------|-------------|---------------------------------------|
| Mark                 | Mysticism   | Sets a recall anchor. Instantaneous.  |
| Recall               | Mysticism   | Teleport to Mark. Instantaneous.      |
| Divine Intervention  | Mysticism   | Teleport. Instantaneous.              |
| Almsivi Intervention | Mysticism   | Teleport. Instantaneous.              |
| Cure Common Disease  | Restoration | Instant cure.                         |
| Cure Blight Disease  | Restoration | Instant cure.                         |
| Cure Corprus Disease | Restoration | Instant cure.                         |
| Cure Poison          | Restoration | Instant cure.                         |
| Cure Paralyzation    | Restoration | Instant cure.                         |

Nothing to scale or tier on these.

---

## Uses BOTH axes — do NOT treat as single-axis

These are easy to mistake for instant/magnitude-only because a given record may
store duration 0, but the **effect itself uses duration** (UESP: the effect acts
"each second of the effect's duration"). They are deliberately absent from the
flag lists; a duration of 0 on one of these is a real value and is shown as such
(e.g. a Damage Health poison prints `6/0s`).

- **Damage** Health / Magicka / Fatigue / Attribute / Skill
- **Drain** Health / Magicka / Fatigue / Attribute / Skill
- **Restore** Health / Magicka / Fatigue / Attribute / Skill
- **Absorb** Health / Magicka / Fatigue / Attribute / Skill

Plus every other effect not listed in the three groups above (Fire/Frost/Shock
Damage, Poison, Fortify \*, Resist \*, Weakness \*, Shield, Fire/Frost/Lightning
Shield, Burden, Feather, Levitate, Jump, Slowfall, Swift Swim, Telekinesis,
Detect \*, Blind, Sound, Chameleon, Sanctuary, Light, Night Eye, Charm,
Calm/Frenzy/Demoralize/Rally/Turn Undead, Reflect, Spell Absorption, etc.) uses
both magnitude and duration and is scaled/tiered normally on both axes.

Note: the four **no-scale** damage effects (Fire Damage, Frost Damage, Shock
Damage, Poison) use both axes but are exempt from spell-compensation scaling —
see the spell-value rules.

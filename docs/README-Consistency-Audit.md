# R3 README Consistency & Rule-Compliance Audit — Findings

Read-only audit. No ESP JSON, generator, or README was modified. All data-level
findings were cross-checked against the ESP JSON in the workspace root and, where
needed, the vanilla masters in `d:\tes3conv`. The project's own authoritative
checker (`scripts/check_potion_tiers.py`) was run against `d:\tes3conv` to vet
potion tiers.

---

## Summary (answer first)

The generated READMEs are in good shape. The finalized Spells layout
(`## School` -> `### Effect` -> `*Vanilla*` / `*Tamriel Data*` fenced blocks ->
`## Multi-Effect` section, column grid 44/80, divider+blank before every header)
is shared cleanly by Potions and Enchantments, and the smaller READMEs (Core,
Creatures, Factions, Races, Optional) follow the same header/divider/fenced-block
skeleton. The specific defects the user originally reported — lopsided paired
tokens (`Touch` on one side only), asymmetric `ft`/cost, double blank lines, and
layout drift between Potions/Enchantments and Spells — are **not present in the
current output**. The symmetric "show-on-both-or-neither" rule for range/area/cost
is correctly implemented in `gen_common.format_effect_pair` and in
`gen_spells.start_pair_values`.

Two genuine **data** rule violations remain, both surfaced by the READMEs and both
independently flagged by `gen_spells_explained.py`:

1. `hand of odros` — Absorb Attribute effect `3-6` (min≠max, neither value is 1
   nor a multiple of 5). Rounding-rule violation.
2. `T_Com_Trp_Acid` (Acid Trap) — Poison effect `2-4` (min≠max, non-round).
   Rounding-rule violation (rounding still applies to no-scale effects).

No TD spell uses `AUTO_CALCULATE` (clean). All 289 single-effect potions pass the
tier table (0 mismatches). No markdown pipe tables exist in the generated output,
so the general-rules table-padding rule does not apply to them.

The one real cross-README **layout** inconsistency: `gen_spells_explained.py`
emits a 6-line intro-prose paragraph after its title, which violates the
"no intro prose in generated READMEs" rule. A minor cosmetic divergence: the Core
Crime fenced block contains a single interior blank line that no other Core block
has.

---

## Q1 — Cross-README layout consistency

### Reference layout (R3 - Spells.md)

Established conventions, confirmed in `scripts/gen_spells.py`:

- Title `# Remastered Rebalance Redux - <Topic>`, one blank line.
- `------` (60 dashes) divider + blank line before **every** `##`/`###` header
  (the `header()` helper).
- `## <School>` -> `### <Effect>` for single-effect records; a trailing
  `## Multi-Effect <Topic>` section for 2+ effect records.
- Per-effect `Base Cost` line (spells) rendered in its own fenced block at the
  values column (col 44).
- `*Vanilla*` and `*Tamriel Data*` labelled fenced blocks.
- Column grid: id/label col 0, values col 44 (`COL_VALUES`), name col 80
  (`COL_ID`).
- No `## Misc` catch-all is emitted in practice (every effect resolves a school).
- Trailing blank lines stripped; file written with CRLF, no BOM
  (`open(..., encoding="utf-8", newline="\r\n")`).

### Conformance by file

| README                        | School->Effect | Vanilla/TD labels | Multi-Effect | Col 44/80 | Divider+blank | Notes |
|-------------------------------|:--------------:|:-----------------:|:------------:|:---------:|:-------------:|-------|
| R3 - Spells.md                |      yes       |        yes        |     yes      |    yes    |      yes      | reference |
| R3 - Potions.md               |      yes       |        yes        |     yes      |    yes    |      yes      | `Tier` line replaces `Base Cost`; by design |
| R3 - Enchantments.md          |      yes       |        yes        |     yes      |    yes    |      yes      | no Base Cost/Tier line; by design |
| R3 - Core.md                  |   n/a (GMST)   |     n/a           |     n/a      |    yes    |      yes      | editorial section map; one interior blank (below) |
| R3 - Creatures.md             |   n/a          |     n/a           |     n/a      |    yes    |      yes      | single `## Magicka` block |
| R3 - Factions.md              |   n/a          |     n/a           |     n/a      |    yes    |      yes      | `## Attributes` -> `### Faction` |
| R3 - Races & Birthsigns.md    |   n/a          |  `*Vanilla*`/`*Current*` | n/a   |    yes    |      yes      | interior group blanks by design (below) |
| optional/R3 - Optional.md     |   n/a          |     n/a           |     n/a      |    yes    |      yes      | one `##` per plugin |
| docs/Spells-Explained.md      |      yes       |     yes (Vanilla implicit) | yes  | 44/80/150 | yes       | **intro prose present** (violation, below) |

The three "magic" generators (`gen_spells.py`, `gen_potions.py`,
`gen_enchantments.py`) are structurally near-identical: same `header()`,
`block()`, `emit_record()`, `sort_key()` shapes and the same bucketing into
`groups[school][fx]` + `multi`. Potions and Enchantments correctly reuse the
Spells layout; the only intentional differences are the per-effect line label
(`Base Cost` on Spells, `Tier` on Potions, none on Enchantments — this matches
the user's "1 no, 2 yes" decision: potions get a tier line, enchantments do not).

### Divergences found

- **D1 — intro prose in `docs/Spells-Explained.md`** (rule violation of
  "no intro prose"). `gen_spells_explained.py` `main()` appends six prose lines
  after the title:

  > `Generated companion to \`R3 - Spells.md\`. Same layout, with an extra`
  > `explanation column noting which rule produced each change. ...`

  (lines 3–8 of `docs/Spells-Explained.md`). Every other generated README jumps
  straight from the title to the first divider. Recommendation: drop these
  `out.append(...)` prose lines in `gen_spells_explained.py` (keep only the title
  and the first divider), matching `gen_spells.py`.

- **D2 — Core Crime block has an interior blank line.** `R3 - Core.md` line 53:
  the Crime fenced block renders the five `iCrime*` GMSTs, then a blank line,
  then `58028831233554797` (DialogueInfo Death-Warrant threshold) and
  `BILL_MT_calc_legit_kills` (Script murder cost). Source:
  `gen_core.py` Crime handling reopens the fence and inserts `out.append("")`
  before the crime_lines. No other Core block has an interior gap. This is inside
  a fence so it is not a markdown paragraph break, but it is a cosmetic
  inconsistency. Recommendation: drop the separator blank for visual uniformity
  (or keep intentionally — low priority).

- **D3 (not a defect) — Races interior group blanks.** `R3 - Races & Birthsigns.md`
  has blank lines inside its fenced blocks (e.g. lines 75, 119, 130, ...) that
  separate the `Abilities` / `Powers` / `Spells` groups. These come from
  `gen_races.py` `spell_block_lines()` and are a deliberate, internally
  consistent readability device within fences. Noted for completeness; no change
  recommended.

### Checks that passed (no divergence)

- **No document-level double blank lines** in any README (scan of every file).
- **No lopsided paired tokens**: a scan of all `A -> B` value cells in Spells,
  Potions, Enchantments, Core, and Races found 0 cells where a range label
  (`/Touch`,`/Target`,`/Self`) or `ft` appears on only one side. The two Starting
  Spells pairs that carry a range on both sides
  (`5-20/60s/Touch -> 10/30s/Self`, `5/30s/Self -> 10-100/20s/Target`) are
  correct — the range differs so it is shown on **both** sides per the rule.
- **No markdown pipe tables** in generated output; all data is in fixed-column
  fenced blocks, so the general-rules pipe-table padding rule is out of scope for
  these files.
- **Token order** `mag/dur/ft/range [cost]` is honored by `gen_common.format_effect`
  (area then range appended in that order) and the cost bracket is appended last
  by `format_cost_bracket` / `start_pair_values`.

---

## Q2 — Rule violations in the data (surfaced by the READMEs)

### Confirmed violations

**V1 — Rounding: `hand of odros`, Absorb Attribute `3-6`.**
Rendered in `R3 - Spells.md` Multi-Effect section:
`Absorb Attribute: Agility   3-6/120s`.
JSON (`R3 - Spells.json`, record `hand of odros`, effect index 1):
`AbsorbAttribute min=3 max=6 dur=120 area=0 range=OnTouch`. min≠max and both 3
and 6 violate the Value Rounding Rule (allowed: 1 or a multiple of 5).
Expected: a round range such as `5-5`→`5` or `1-5`/`5-10` (design choice).
Independently flagged by `gen_spells_explained.py`:
`rounding ✗ (3-6)` on Hand of Odros.

**V2 — Rounding: `T_Com_Trp_Acid` (Acid Trap), Poison `2-4`.**
Rendered in `R3 - Spells.md` Multi-Effect (Tamriel Data):
`Poison   2-4/5s`.
JSON effect index 2: `Poison min=2 max=4 dur=5 area=1 range=OnTouch`. min≠max,
both non-round. Poison is a **No-Scale** effect, but the rounding rule still
applies ("Only rounding fixes apply" to no-scale effects). Expected a round
range (e.g. `1-5`). Independently flagged by the explained doc:
`rounding ✗ (2-4)` on Acid Trap. (Its paired master `T_Com_Trp_AcidMaster` uses
`10-20`, which is already round.)

These are the **only** two min≠max rounding violations across Spells, Potions,
and Enchantments JSON.

### Checks that passed

- **AUTO_CALCULATE on TD spells: none.** Every `T_`-prefixed Spell in
  `R3 - Spells.json` has a non-auto `flags` and an explicit numeric `cost`. The
  `[auto -> N]` and `[N -> auto]` cost brackets visible in Spells.md
  (e.g. `poet's whim ... [auto -> 39]`, `resist paralysis ... [300 -> auto]`)
  are all on **vanilla-id** spells, which the AUTO_CALCULATE rule does not
  restrict. `gen_spells_explained.py`'s `TD-AUTOCALC ✗` note fires nowhere.

- **Potion tiers: 0 mismatches.** `scripts/check_potion_tiers.py` run against
  `d:\tes3conv` reports `0 mismatch(es)` over 289 single-effect potions
  (6 multi-effect skipped, 1 skipped by rule). The checker correctly applies the
  geometric-midpoint column boundaries, treats the Damage family as column-1
  magnitude-only, skips No-Scale (Poison), and skips magnitude-only (Dispel) and
  neither-axis effects. A naive first-pass check flagged 12 "mismatches"
  (poisons, Damage-family, Dispel) that are all legitimate exclusions — the
  project checker is authoritative and clean.

- **Spell cost formula: consistent on spot-checks.**
  `T_Com_Mys_Lifesteal` stored 48 = computed 48.0; `T_Nor_Res_EagleEye` stored
  100 = computed 100.0; `T_Com_Ilu_AlluringSpeech` stored 40 vs computed 43.75
  (Charm 15-20/20s at base 2.5 — within rounding tolerance, not a clear
  violation). The `(min+max)*dur*(base/40) + area*(base/40)`, ×1.5-if-OnTarget,
  summed-per-effect formula is being applied.

- **Magnitude cap (100):** no compensated single-value magnitude in the scanned
  data exceeds 100 in a way that reads as uncapped; large multi-effect Burden
  values (e.g. `1000/10s` on Harthoon's Heavy Eyes) are Burden at base cost 0.1,
  i.e. compensated ×10 from vanilla 100 — Burden is not range-rounded (min==max)
  and the cap note is a spell-design concern already visible, not a README error.

---

## Q3 — Reuse of `gen_spells_explained.py` algorithms

### What `explain(obj, van)` computes

For each changed spell it reads the realized values and emits a terse note:

1. **TD-AUTOCALC check** — `is_td(obj) and cost_label(obj) == "auto"` →
   `TD-AUTOCALC ✗`. Pure rule check on `id` prefix + `flags`.
2. **No-scale detection** — first effect's `magic_effect` in
   `{FireDamage, FrostDamage, ShockDamage, Poison}` → `no-scale`.
3. **Base-cost compensation direction/ratio** — compares vanilla vs current
   MagicEffect `base_cost` for the first effect. `needed = vb/cb` is the factor
   `mag×dur` must move to hold effective cost; `md_split()` derives the realized
   magnitude factor `mf = cur(min+max)/van(min+max)` and duration factor
   `df = cur_dur/van_dur`; `prod(mf,df)` is the realized combined factor. It then
   classifies: within ~15–18% of `needed` → `compensated ✓`; else if mag/dur held
   and the stored **cost** moved by the base factor → `compensated via cost ✓`;
   else `✗ (expected ...)`.
4. **Mag/dur split rendering** — `nice()` snaps a raw factor to a tidy
   `xN` / `/N` label (approximate by design).
5. **Rounding-violation flag** — for every effect, `min≠max and any(v!=1 and
   v%5!=0)` → `rounding ✗ (mn-mx)`. This is the exact Value Rounding Rule check
   and is the engine behind findings V1/V2.
6. **Rename note** — vanilla `name` ≠ current `name` → `renamed`.
7. **Fallback** — otherwise `cost` (if cost changed) or `changed`.

Known limitation: compensation is judged from the **first effect only**
(`e0 = effs[0]`). On multi-effect spells where the compensated effect is not
first (e.g. Aryon's Rest, Hand of Odros, Wrath of Odros — first effect is an
instant Damage Fatigue, the scaled effect is Burden), the note reads
`✗ (expected x2)` even though the intended effect was scaled correctly. Useful as
a flag, but not authoritative for multi-effect records.

### Transferability to other READMEs

| Algorithm                        | Potions | Enchantments | Core / others | Verdict |
|----------------------------------|:-------:|:------------:|:-------------:|---------|
| Rounding-violation flag          | direct  | direct       | direct (any min≠max record) | **Transfers directly.** Already a universal check; could live in `gen_common`. |
| Rename note (vanilla vs current name) | direct | n/a (no name field; enchants map id→item name) | partial (Core uses NAME_OVERRIDE) | Transfers where records carry a `name`. |
| TD-AUTOCALC check                | n/a (potions have no spell cost/flags) | n/a | n/a | Spell-only; does not apply. |
| No-scale detection               | **different meaning** — potions already handle no-scale by *skipping tiering* (`check_potion_tiers`), not by compensation | n/a | n/a | Concept exists for potions but is enforced by the tier checker, not compensation. |
| Base-cost compensation direction/ratio + mag/dur split | **does not apply** — potions are tier-table driven, not `mag×dur` compensated | **does not apply** — enchants have no base cost / tier axis | n/a | Spell-math only. |
| `nice()` factor labelling        | low value (no factors to show) | low value | low value | Tied to compensation; moves only if compensation moves. |

Concrete assessment:

- **Potions**: the analogous "explained" capability is *tier correctness*, which
  already exists and is better expressed by `check_potion_tiers.py` (column
  selection + expected mag/dur per grade). A potions-explained doc would annotate
  each row with its tier column and expected vs actual mag/dur — reusing
  `base_to_col()` and `TIERS` from the checker, **not** `explain()`'s
  compensation math. The compensation/no-scale/`nice()` logic does not transfer.
- **Enchantments**: have no base cost and no tier; the only transferable note is
  the rounding flag (and arguably a "scaled ×N vs vanilla" magnitude factor, which
  is informational, not a rule). An enchantments-explained doc is low value.
- **Core / Creatures / Factions / Races**: single scalar diffs
  (GMST / magicka / attribute requirement / skill bonus). The only transferable
  piece is the generic rounding check where a min–max magnitude is present
  (Races ability effects, Core scroll magnitudes). No compensation applies.

### Recommendation (describe only; implement nothing)

- Extract the **rounding-violation check** into `gen_common` as a small helper
  (e.g. `rounding_violations(effects) -> list[(fx, mn, mx)]`). It is already
  duplicated in spirit between `gen_spells_explained.py` and this audit, and is
  the one algorithm that is genuinely universal across every record type with a
  min–max magnitude.
- Keep **compensation / mag-dur-split / no-scale / TD-AUTOCALC** in the spells
  layer. They are spell-cost-model specific and have no meaning for tier-based
  potions or axis-less enchantments. Factoring them into `gen_common` would add a
  shared surface that only one caller can use.
- If a potions-explained doc is wanted, build it on the existing
  `check_potion_tiers` logic (`base_to_col`, `TIERS`, the Damage/duration-only/
  no-scale categories), surfaced as an annotation column — a parallel to, not a
  reuse of, `explain()`.
- Fix the first-effect-only limitation before trusting multi-effect compensation
  notes (iterate effects and attribute the base-change to the matching effect).

---

## Q4 — Prioritized summary

### Rule violation in data (highest)

| ID | Location | Issue | One-line fix (describe only) |
|----|----------|-------|------------------------------|
| V1 | `R3 - Spells.json` `hand of odros` eff1 (rendered Spells.md Multi-Effect) | Absorb Attribute `3-6` — min≠max, non-round | Round the range to 1/multiples of 5 (e.g. `5-5`→`5`, or `1-5`/`5-10`) in the JSON, then regenerate. |
| V2 | `R3 - Spells.json` `T_Com_Trp_Acid` eff2 (rendered Spells.md Multi-Effect, TD) | Poison `2-4` — min≠max, non-round (no-scale still rounds) | Round the Poison range (e.g. `1-5`), regenerate. |

### Cross-README layout inconsistency (medium)

| ID | Location | Issue | One-line fix |
|----|----------|-------|--------------|
| D1 | `scripts/gen_spells_explained.py` → `docs/Spells-Explained.md` lines 3–8 | Intro-prose paragraph violates "no intro prose in generated READMEs" | Delete the six prose `out.append` lines; keep title + first divider only. |

### Cosmetic (low)

| ID | Location | Issue | One-line fix |
|----|----------|-------|--------------|
| D2 | `scripts/gen_core.py` Crime block → `R3 - Core.md` line 53 | Lone interior blank line inside the Crime fence that no other Core block has | Drop the `out.append("")` separator in the Crime handler for uniform block spacing. |
| A1 | `gen_spells_explained.py` `explain()` | Compensation judged on first effect only → false `✗ (expected ...)` notes on multi-effect spells | Attribute the base-cost change to the matching effect, not `effs[0]`. |

### Opportunity (low)

| ID | Location | Issue | One-line fix |
|----|----------|-------|--------------|
| R1 | `gen_common.py` | Rounding-violation check is the one universally reusable algorithm | Add a shared `rounding_violations()` helper usable by every generator/checker. |

---

## Method notes

- Steering source of truth: `.kiro/steering/mod-rules.md`,
  `.kiro/steering/general-rules.md`.
- Potion tiers vetted with the project's own `scripts/check_potion_tiers.py`
  (master dir overridden to `d:\tes3conv`): 0 mismatches.
- Rounding and AUTO_CALCULATE checks run directly against `R3 - Spells.json`,
  `R3 - Potions.json`, `R3 - Enchantments.json`; the two rounding hits were
  confirmed by dumping the exact JSON effect records.
- Layout checks (double blanks, interior fence blanks, pipe tables, token
  symmetry) run over the rendered `.md` files.
- No files were modified; the temporary audit helper used during the scan was
  removed. Content from UESP effect-axis descriptions (via
  `scripts/effect_axis_flags.json`) was rephrased for compliance.

# Spell Edit Workflow

This workflow applies to all three file pairs:
- `README - Magic.md` ↔ `R3 - Magic.json` → `R3 - Magic.esp`
- `README - Races & Birthsigns.md` ↔ `R3 - Races & Birthsigns.json` → `R3 - Races & Birthsigns.esp`
- `README - Core.md` ↔ `R3 - Core.json` → `R3 - Core.esp`

When asked to modify a spell, race ability, birthsign, or game setting:

## 1. README update
Find the entry's section in the relevant `README - *.md` file and add or update its entry using this format:

```
Spell Name                                  [default mag/dur from vanilla] -> [new mag/dur]
```

Column positions (0-indexed):
- **col 0**: spell/entry name
- **col 44**: values (mag/dur)
- **col 76**: comments and IDs (notes, flags, scale, `id: <json_id>`)

Multiple comments separated by `;`. IDs use `id:` prefix and go last. Example:
```
Paralysis                                   6s [auto -> 12]                 used by Scribs; id: scrib_paralysis
Scroll of Baleful Suffering                 0−25/30s                        id: sc_balefulsuffering_en
```

- Values are `magnitude/duration` (e.g. `20/10s -> 50/40s`)
- Range spells use `min-max/duration` (e.g. `30-60/10s -> 60-120/50s`)
- If there is an area, append it after duration: `50/10s/10ft`
- If there is also a range type, append it after area: `50/10s/10ft/Target`
- If a cost override is also present, it comes last in brackets: `50/10s/10ft/Target [10]`
- For **abilities** (always-on), duration is irrelevant — show magnitude only: `200/1s -> 1`
- If there is a cost override, append it in brackets: `50/10s [25]`
- Anything after the values (notes, flags) goes in a comment at the end of the line, with multiple comments separated by `;`: `50/10s               used by Aryon; !`
- Add the scale as a comment on the first spell that uses it, e.g. `x2.5/x4`. Skip the comment on subsequent spells if the scale is the same.
- Always use `xMAG/xDUR` format (e.g. `x10/x1` for magnitude-only, `x1/x4` for duration-only). Never write `x10 dur` or `x4 mag`.
- Do not add scale comments to potions.
- If the scale follows directly from the base cost change (opposite direction, same factor — e.g. base cost ÷2 → spells ×2), omit the scale comment entirely since it is implied.
- Potions always use a value from the potion tier table — never scale potion mag/dur from base cost changes.
- If the user writes a scale like `! 5x/2x` as a trailing comment on a README entry, it means: apply that scale to all entries in that section (until an empty line or a new `!` trigger appears), compute and write the new target values in README and JSON, then remove the scale comment.
- If the user writes `! [Nx]` (a single value in brackets, e.g. `! [5x]`), it means: apply that scale to the **spell cost override** (the `[cost]` value in brackets on the spell line) for all entries in that section, then remove the scale comment.
- If a `! Nx` scale comment appears on a **Base Cost** line, apply that scale to the Base Cost value, then remove the scale comment.
- The `->` means: left side is the vanilla/default value, right side is the new target value
- If the right side value is identical to the left side value, omit the `->` and right side entirely — just leave the vanilla value alone

## The `!` marker
`!` is a general attention marker. When the user writes `!` anywhere — on a line, a section header, or as a standalone comment — it means: **look at this, analyze it, and report back**. Do not apply any changes unless the user explicitly asks after the analysis.

Specific `!` trigger forms that do cause changes (only when the hook processes them):
- `! Nx/Nx` trailing on a spell entry — scale trigger for mag/dur
- `! [Nx]` trailing on a spell entry — scale trigger for cost override
- `! Nx` on a Base Cost line — scale trigger for base cost

## 2. JSON update
Find the entry in the relevant ESP JSON (`R3 - Magic.json`, `R3 - Races & Birthsigns.json`, or `R3 - Core.json`).

- If the spell **already exists** in the ESP JSON: update `min_magnitude`, `max_magnitude`, `duration`, `area` as needed.
- If the spell **does not exist** in the ESP JSON: copy the full entry from the appropriate default reference JSON in `tes3conv/` (Morrowind.json, Tribunal.json, Bloodmoon.json, or Tamriel_Data.json), then apply the new values.

## README IDs
IDs go in the comment section of the line (col 76), prefixed with `id: `. Example:
```
Paralysis                                   6s [auto -> 12]                 used by Scribs; id: scrib_paralysis
Scroll of Baleful Suffering                 0−25/30s                        id: sc_balefulsuffering_en
```

Add IDs for:
- **All enchanted items** (scrolls, weapons, clothing with enchantments) — always include `id:`
- **Spells or potions that share a display name with another record** — both need `id:`, EXCEPT when one is from Tamriel Data (starts with `T_`) and the other is vanilla: in that case only the TD entry needs `id:`
- **All Tamriel Data records** — always include `id:` since TD IDs start with `T_` and are not obvious from the name

Do NOT add IDs for vanilla spells/potions with unique names, or for base cost entries.

The col 120 rule is retired — IDs are part of the comment column at col 76, using `id:` prefix to distinguish from other comments. Multiple comments are separated by `;`.

## JSON value scaling
The user will specify the scale to use each time. Wait for the user to provide the scale before writing JSON values.

The scale is applied to the **vanilla default values** (left of `->` in README) to produce the new values:
- `new_magnitude = vanilla_magnitude × scale_mag`
- `new_duration = vanilla_duration × scale_dur`

The JSON and README store the same new values — no conversion needed between them.

**Important**: When a scale is specified (either by the user or via `! Nx/Nx` trigger in README), always apply it to the vanilla default (left of `->`) and replace whatever target value was previously on the right side — even if a target already exists. The value on the right of `->` is always the output of the last scale and is meaningless as input.

**x1/x1 special case**: Scale x1/x1 means revert to vanilla. Set the target values to the vanilla defaults — keep the entry in both README and JSON, just update the values.

**-> TODO special case**: When an entry has `-> TODO` as a comment, the value already on the right side of `->` is the final target — apply it directly to the JSON without any scale calculation. When the user says "don't apply, just add rule" (or similar), only update the steering file — do not touch README or JSON files.

## Base Cost and spell compensation rule
When a magic effect's base cost is changed, spells of that school must be adjusted in the **opposite direction** to keep their effective cost roughly the same:
- If base cost is multiplied by X, then spell mag×dur must be divided by X (and vice versa)
- Example: base cost ÷2 → spell mag×dur ×2 (e.g. double magnitude, or double duration, or split between both)
- The split between magnitude and duration is chosen per spell as appropriate

## Notes
- Never modify files inside `tes3conv/` — those are read-only vanilla references.
- Never change the `id` field of any record in ESP JSON files. IDs are immutable — only `name` and other data fields may be edited.
- README and JSON must always be updated together. ESP conversion is handled separately and is not part of this workflow.
- Only rebuild the ESP for the JSON file that was actually changed.
- The top-level `## Potions` section in README - Magic.md defines default Bargain and Cheap values for all potions (e.g. `Bargain... 5/8s -> 6/18s`). If an individual potion entry has its own explicit values, those override the general rule.

## Modification Policy
Only hooks may trigger actual modifications to README, JSON, and ESP files. Direct user requests must not apply changes — they may only update steering rules or prepare instructions for hooks to execute.

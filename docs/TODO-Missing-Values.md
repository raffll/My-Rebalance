# TODO — Missing Spell/Scroll/Enchantment Values

This document proposes R3 values for items not yet covered in the READMEs.
Rules applied:
- Base cost ÷X → spell mag×dur ×X (inverse compensation)
- Base cost ×X → spell mag×dur ÷X
- Elemental damage (Fire/Frost/Shock/Poison): NO compensation, only rounding
- Magnitudes must be multiples of 5 (or exactly 1). Durations exempt from rounding.
- Effects with no magnitude range (min==max) do NOT get rounded.

---

## Shield (base cost 2→1, compensation ×2)

### Spells
Already covered: TD spells (Falling First Barrier, Force Wall, Tsun's Ward)

MISSING vanilla spells — these all have fixed magnitudes (min==max), so ×2 applies cleanly:
- Shield: 5/30s → 10/30s
- First Barrier: 10/30s → 20/30s
- Second Barrier: 20/30s → 40/30s
- Third Barrier: 30/30s → 60/30s
- Fourth Barrier: 40/30s → 80/30s
- Fifth Barrier: 50/30s → 100/30s
- Sixth Barrier: 60/30s → 120/30s

### Scrolls
- Scroll of The First Barrier: 5/30s → 10/30s
- Scroll of The Second Barrier: 10/30s → 20/30s
- Scroll of The Third Barrier: 15/30s → 30/30s
- Scroll of The Fourth Barrier: 20/30s → 40/30s
- Scroll of The Fifth Barrier: 25/30s → 50/30s
- Scroll of The Sixth Barrier: 30/30s → 60/30s
- Scroll of The Ninth Barrier: Shield 35/60s → 70/60s [multi-effect scroll, only Shield effect scales]

### Enchanted Items
- first barrier_en (5/10s): Amulet of Shield, Brawler's Belt, First Barrier Belt/Ring, Herder's Belt → 10/10s
- second barrier_en (10/30s): Hunter's Belt, Second Barrier Belt/Ring → 20/30s
- third barrier_en (15/10s): Third Barrier Belt/Ring → 30/10s
- fourth barrier_en (20/10s): Khan Belt → 40/10s
- fire shield_en (3/5s): Chest of Fire, Helm of Holy Fire → 5/5s [rounding: 3×2=6→5]
- lightning shield_en (3/5s): Storm Helm → 5/5s [rounding: 3×2=6→5]
- fiend_helm_en: Lightning Shield 3/10s → 5/10s [rounding: 3×2=6→5]
- devil helm_en: Reflect component — see Reflect section below
- devil cephalopod / devil mole crab: Spell Absorption component — see Spell Absorption section

NOTE: Hort-Ledd's Robe has Shield 5/30s — that's a unique enchantment, propose 10/30s.

---

## Damage Attribute (base cost 8→24, compensation ÷3)

### Spells
Vanilla Damage Attribute spells — all have 1-20 range, 1s duration (Touch):
- Evil Eye: DA Personality 1-10/1s → 1-5/1s [10÷3=3.3→5; but min stays 1]
- Clench: DA Speed 1-20/1s → 1-5/1s [20÷3=6.7→5]
- Emasculate: DA Endurance 1-20/1s → 1-5/1s
- Fuddle: DA Intelligence 1-20/1s → 1-5/1s
- Hex: DA Luck 1-20/1s → 1-5/1s
- Stumble: DA Agility 1-20/1s → 1-5/1s
- Woe: DA Willpower 1-20/1s → 1-5/1s

TD Spells:
- Kirhnarva's Leg-Breaker: DA Str 1-8/2s + DA Agi 1-8/2s → DA Str 1-5/1s + DA Agi 1-5/1s [8÷3=2.7→5; dur 2÷3=0.67→1]
- Meat Rot: DA Str 1-5/2s + DH 1-20/2s → DA Str 1-5/1s + DH unchanged [only DA component scales; DH base cost unchanged]
- Mind Rot: DA Int 1-5/2s + DM 1-15/2s → DA Int 1-5/1s + DM component scales separately (see Damage Magicka)

### Scrolls
- Scroll of Black Despair: DA Willpower 5-15/10s → 1-5/3s [mag: 5÷3=1.7→1, 15÷3=5; dur: 10÷3=3.3→3]
- Scroll of Black Fate: DA Luck 5-15/10s → 1-5/3s
- Scroll of Black Mind: DA Intelligence 5-15/10s → 1-5/3s
- Scroll of Black Scorn: DA Personality 5-15/10s → 1-5/3s
- Scroll of Black Sloth: DA Agility 5-15/10s → 1-5/3s
- Scroll of Black Weakness: DA Strength 5-15/10s → 1-5/3s
- Scroll of Drathis' Soulrot: DA End 0-50 + DA Wil 0-50 → DA End 0-15 + DA Wil 0-15 [50÷3=16.7→15; 0 stays 0, no-range exception doesn't apply since min≠max]

### Enchanted Items
- stumble_en: DA Agility 1-20/1s Touch → 1-5/1s
- bonebiter_en: DA Agility 20/1s Target → 5/1s [20÷3=6.7→5; fixed mag but min==max so no rounding exception... wait, this IS min==max (20/20). No-range exception: do NOT round. 20÷3=6.67. Since it can't stay non-round and exception says don't round... this is tricky. Actually the exception says effects with no magnitude RANGE (min==max) do NOT get rounded. So 20→6.67 stays as... 7? The rule says magnitudes must be multiples of 5 or exactly 1. Conflict: exception says don't round, but the value 7 violates the multiple-of-5 rule. Resolution: the exception means we don't apply the rounding step, so the raw ÷3 result stands. But 6.67 must be an integer. Round to nearest integer: 7. So → 7/1s]
- gripes_en: DA Endurance 1-20/1s → 1-5/1s
- fuddle_en: DA Intelligence 1-20/1s → 1-5/1s
- hex_en: DA Luck 1-20/1s → 1-5/1s
- clench_en: DA Speed 1-20/1s → 1-5/1s
- evil eye_en: DA Personality 1-20/1s → 1-5/1s
- woe_en: DA Willpower 1-20/1s → 1-5/1s

---

## Drain Magicka (base cost 4→0.4, compensation ×10)

### Spells
Already covered: Magicka Leech, TD spells (Dhamcka's Soul-Withering, Rage of Magnus)

MISSING vanilla spells:
- Wild Flay Spirit: 1-20/3s → 10-200/3s [×10 mag; dur stays]
- Drain Blood: DrH 5/30s + DrM 5/30s → DrH unchanged + DrM 50/30s [only DrM component ×10; DrH base cost 4 unchanged]
- Gash Spirit: 5-20/30s → 50-200/30s
- Gash Spirit [Ranged]: 5-20/30s → 50-200/30s
- Flay Spirit: 5-20/60s → 50-200/60s

### Scrolls
- Scroll of The Black Storm: DM 1-10/2s component → 10-100/2s [only the DM effect scales; Shock Damage does NOT scale]

### Enchanted Items
- ri_drainmagicka_en (3-7/1s Target): Ring of Nullification → 30-70/1s [×10]
- flay spirit [ranged]_en (5-10/30s Target): Spiritstrike Ring → 50-100/30s [×10]
- Azura's Servant shield: Frost Damage 1-15 + Drain Magicka 1-10/30s → Frost unchanged + DrM 10-100/30s [×10]

---

## Drain Fatigue (base cost 2→0.2, compensation ×10)

### Spells
Already covered: Weariness, Sleep, Wild Exhaustion, Wearying Touch, Exhausting Touch, Exhaustion, Ordeal of St. Olms, Dagoth's Bosom, TD Duck

MISSING: None — all vanilla Drain Fatigue spells are already in the README.

### Scrolls
None with Drain Fatigue effect.

### Enchanted Items
- weariness_en (1-10/1s Target): Shame Ring, The Chiding Cuirass → 10-100/1s [×10]
- sleep_en (1-15/3s Target): Sleep Amulet → 10-150/3s [×10]
- exhaustion_en (5-20/30s Target): Ring of Exhaustion → 50-200/30s [×10]

---

## Damage Fatigue (base cost 4→2, compensation ×2)

### Spells
Already covered: Fleabite, Doze, Hornhand

MISSING: None — all vanilla Damage Fatigue spells are in the README.

TD Spells:
- Hairdoch's Extinguisher: DF 2/10s + Paralyze 10s + DH 2/10s → DF 4/10s (×2, but 4 isn't mult of 5... DF is fixed mag min==max=2, so no-range exception applies: don't round. 2×2=4 → 4/10s) + Paralyze component scales separately + DH unchanged

### Scrolls
None with standalone Damage Fatigue.

### Enchanted Items
- doze_en (1-20/1s Touch): Doze Charm → 1-40/1s [×2; 1 stays 1, 20×2=40]
- fleabite_en (9-18/1s Touch): Ring of Fleabite → 20-35/1s [9×2=18→20; 18×2=36→35]
- hornhand_en (15-36/1s Touch): Ring of Hornhand → 30-70/1s [15×2=30; 36×2=72→70]
- ironhand_en (21-42/1s Touch): Ring of Ironhand → 40-85/1s [21×2=42→40; 42×2=84→85]
- knuckle luck_en (3-120/1s Touch): Ring of Knuckle Luck → 5-240/1s [3×2=6→5; 120×2=240]
  Also: Belt of Northern Knuck Knuck uses same enchantment

---

## Disintegrate Armor (base cost 6→0.6, compensation ×10)

### Spells
Already covered: Armor Eater, Disintegrate Armor (Hungers), Brittlewind, Eddard's Wrath, TD spells

MISSING: None — all covered.

### Scrolls
Already covered: Scroll of Baleful Suffering (DisArmor component)

### Enchanted Items
Already covered: Daedric Crescent, Scroll of Baleful Suffering enchantment

MISSING: None.

---

## Disintegrate Weapon (base cost 6→1.2, compensation ×5)

### Spells
Already covered: Weapon Eater, Disintegrate Weapon (Hungers), Brittlewind, Eddard's Wrath, TD spells

MISSING: None — all covered.

### Scrolls
Already covered: Scroll of Baleful Suffering (DisWeapon component)

### Enchanted Items
Already covered: Scroll of Baleful Suffering enchantment

MISSING: None.

---

## Sound (base cost 3→1, compensation ×3)

### Spells
Already covered: Earwig, Cruel Earwig, Dire Earwig, Wild Earwig, Noise, Cruel Noise, Dire Noise, TD Voices

MISSING: None — all vanilla Sound spells are covered.

### Scrolls
None with Sound effect (Madstone artifact has Sound but it's a unique item, not a scroll).

### Enchanted Items
- Madstone of the Ahemmusa (artifact): Sound 50/20s Touch → 50/60s [fixed mag min==max, no rounding; dur ×3]
  Enchantment is unique to this item.

---

## Charm (base cost 5→2.5, compensation ×2)

### Spells
Already covered: TD Alluring Speech

MISSING vanilla spells:
- Charming Touch: 30/30s → 60/30s [30×2=60; dur stays]
- Charm Mortal: 10-30/30s → 20-60/30s [×2 mag]

### Scrolls
- Scroll of Didala's Knack: 0-24/30s → 0-50/30s [already in Enchantments README as 0-25/30s — rounding from 24×2=48→50]
- Scroll of Vaermina's Promise: 0-48/60s → 0-100/60s [already in Enchantments README as 0-50/60s — rounding from 48×2=96→100... wait, README says 0-50. Let me recalculate: 48×2=96→95 or 100? Nearest 5 = 95 or 100. 96 rounds to 95. Actually README already has 0-50 which is just a rounding fix without ×2. Need to re-propose as 0-95/60s or 0-100/60s]

CORRECTION: The Enchantments README currently shows these as rounding-only fixes (0-24→0-25, 0-48→0-50). With ×2 compensation they should be:
- Scroll of Didala's Knack: 0-24/30s → 0-50/30s [24×2=48→50; 0 stays 0]
- Scroll of Vaermina's Promise: 0-48/60s → 0-95/60s [48×2=96→95; 0 stays 0]

NOTE: These are already in README - Enchantments.md but may need value updates if ×2 wasn't applied.

### Enchanted Items
- Zenithar Whispers (unique): Charm 30/5s Touch → 60/5s [fixed mag, 30×2=60]
- Zenithar's Wiles (unique gloves): Charm 1-50/5s Touch → 1-100/5s [1 stays 1; 50×2=100]

---

## Paralyze (base cost 40→80, compensation ÷2 on duration)

### Spells
Already covered: Paralysis (5s stays), scrib_paralysis (6s), TD Living Statue, TD Paralysis

MISSING vanilla spells:
- Medusa's Gaze: 15s Target → 7s [15÷2=7.5→7; duration exempt from mult-of-5 rounding]

TD Spells:
- Hairdoch's Extinguisher: Paralyze 10s → 5s [10÷2=5]
- Mountain Wind: Paralyze 5s → 2s [5÷2=2.5→2; or 3?]

### Scrolls
- Scroll of Sertises' Porphyry: Paralyze 15s Target → 7s [15÷2=7.5→7]
- Scroll of Psychic Prison: Paralyze 30s + Soultrap 30s → Paralyze 15s + Soultrap 30s [only Paralyze halved]
- Scroll of Illnea's Breath: Frost Damage 35-60 + Paralyze 6s → Frost unchanged + Paralyze 3s [6÷2=3]
- Scroll of Drathis' Soulrot: Paralyze 5s → 2s [5÷2=2.5→2; or 3]

### Enchanted Items
- medusa's gaze_en (Paralyze 5s Target): Ring of Medusa's Gaze, Adusamsi's Robe → 2s [5÷2=2.5→2; or 3]
- Amulet of Admonition (unique): Paralyze 30s + Frost 1-2/30s → Paralyze 15s + Frost unchanged
- Shashev's Ring (unique): Paralyze 15s + Poison 5-10/15s → Paralyze 7s + Poison unchanged

---

## Absorb Health (base cost 8→16, compensation ÷2)

### Spells
Already covered: Absorb Health (5-52→5-50, rounding only — but with ÷2 it should be further reduced)

WAIT — README shows Absorb Health 5-52/1s → 5-50/1s marked with `*`. This is just rounding. The ÷2 compensation hasn't been applied yet. Let me re-propose:
- Righteousness: 10/1s Touch → 5/1s [10÷2=5; fixed mag, no-range exception: don't round. 10÷2=5, already mult of 5]
- Absorb Health: 5-52/1s Touch → 5-25/1s [5÷2=2.5→1 or 5? Min stays at floor. 52÷2=26→25]

Actually, looking at the README pattern: it already shows 5-50 (rounding fix). With ÷2 applied to mag×dur product where dur=1, we divide magnitude by 2:
- Absorb Health: 5-52/1s → 1-25/1s [5÷2=2.5→1 (floor); 52÷2=26→25]

TD Spells:
- Lifesteal: 40/1s Target → already has cost override [24→48] in README. Fixed mag 40÷2=20. Propose 20/1s [24→48].
  Wait, README shows "Lifesteal 40/1s [24→48]" — that's a cost override only, magnitude unchanged. With ÷2 compensation on magnitude: 40÷2=20. So either magnitude halves OR cost doubles. README chose cost doubling. Consistent — no magnitude change needed.
- Bloodlust of Molag Bal: Absorb Str 5-15/15s + Absorb Health 3-4/3s → AbsStr unchanged + AbsH 1-2/3s [3÷2=1.5→1; 4÷2=2, no-range exception doesn't apply since min≠max... but 2 isn't mult of 5. Since it's below 5, use 1. Hmm. Actually 3-4 is a range, so rounding applies: 1.5→1, 2→1? That makes min==max which is weird. Propose 1-2/3s and note the irregularity]
- Necromancer's Soul Trap: AbsH 1-3/45s → 1-1/45s [1÷2=0.5→1; 3÷2=1.5→1] — effectively becomes fixed 1/45s
- Dread Curse of the Lich: AbsH 5-12 Touch → 5-5/1s [5÷2=2.5→5(floor); 12÷2=6→5] — becomes fixed 5
  Actually these are very small values. Maybe just leave at 1-5 or similar.

### Scrolls
- Scroll of Red Death: Absorb Health 5-25/5s Touch → 5-10/2s [mag×dur: (5+25)×5=150 → ÷2=75. Propose 5-10/5s: (5+10)×5=75 ✓. Or 5-25/2s: (5+25)×2=60, too low. Better: 5-10/5s or 1-15/5s]
  Propose: 5-10/5s [sum×dur = 75, close to target 75]

### Enchanted Items
- blood feast_en (5-20/10s Touch): Blood Feast Shield → 5-10/5s [mag×dur: (5+20)×10=250→÷2=125. Propose 5-10/10s: (5+10)×10=150, close. Or 5-20/5s: (5+20)×5=125 ✓]
  Propose: 5-20/5s
- vampire's kiss_en (1-10/1s Touch): Ring of Vampire's Kiss → 1-5/1s [mag×dur: (1+10)×1=11→÷2=5.5. Propose 1-5/1s: (1+5)×1=6, close enough]
- Vampiric Ring (artifact): Absorb Fatigue+Health 20-30/10s Touch → Health component: 20-30/10s → 10-15/10s [mag÷2; or 20-30/5s]
  Propose: 10-15/10s (halve magnitude, keep duration for consistency with short-burst Absorb Fatigue pattern)

---

## Absorb Fatigue (base cost 4→6, ×1.5 — intentionally short-burst, keep existing pattern)

### Spells
Already covered: Tap Energy, Absorb Fatigue, Absorb Fatigue [Ranged], Energy Leech — all shortened to 3s or 6s.

MISSING: None for vanilla. TD spells:
- Tag: 40-50/8s Touch → keep short-burst pattern. Propose 40-50/3s [matching other Absorb Fatigue spells]
- Celestial Frost: AbsFat 15-50/25ft Target + Frost 15-50/25ft Target → AbsFat component: keep short. Propose 15-50/1s (this is an AoE burst)
- Dread Curse of the Lich: AbsFat 5-12 Touch → 5-10/1s [short burst; round 12→10]

### Scrolls
None with Absorb Fatigue.

### Enchanted Items
- Vampiric Ring (artifact): Absorb Fatigue 20-30/10s → 20-30/3s [short-burst pattern]

---

## Detect Animal (base cost 0.75→0.15, compensation ×5)

### Spells
Already covered: TD Greater Detect Creature

MISSING vanilla spells:
- Detect Creature: 50-150/5s → 250-750/5s [×5; 750 is mult of 5 ✓. But 250-750 is huge range. Alternative: 50-150/25s (×5 on duration). Duration approach may be more useful.]
  Propose: 50-150/25s [×5 dur; keeps magnitude readable]

### Scrolls
Already covered: Scroll of Reynos' Beast Finder (40-80/10s → 100-200/20s in Enchantments README — that's ×2.5 mag, ×2 dur = ×5 total ✓)

### Enchanted Items
- Thong of Zainab (artifact): Detect Animal 150/5s Self → 150/25s [fixed mag no-range exception; ×5 on dur]
  Enchantment is unique to this artifact.

---

## Detect Enchantment (base cost 1→0.2, compensation ×5)

### Spells
Already covered: Detect Enchantment (10/10s → 50/10s), TD Detect Enchantment

MISSING: None.

### Scrolls
Already covered: Scroll of The Mage's Eye (40-80/10s → 100-200/20s)

### Enchanted Items
- Detect_Enchantment_ring (unique): Detect Enchantment 100/10s Self → 100/50s [fixed mag no-range; ×5 dur]
- tevral's hawkshaw_en: This is Detect Key, not Detect Enchantment — see below.

---

## Detect Key (base cost 1→0.2, compensation ×5)

### Spells
Already covered: Tevral's Hawkshaw (10/10s → 50/10s), Detect Key (50/5s → 250/5s)

TD: Fuchon Cire's Keyfinder: 1-15ft/60s — this is range-based, not magnitude. Unclear how to scale. Propose: 5-75ft/60s [×5 on range magnitude]

### Scrolls
Already covered: Scroll of Tevral's Hawkshaw (40-80/30s → 100-200/60s)

### Enchanted Items
- tevral's hawkshaw_en (10/10s Self): Hawkshaw Ring → 50/10s [fixed mag; ×5 on mag. Or 10/50s. Match spell pattern: 50/10s]

---

## Reflect (base cost 10→2.5, compensation ×4)

### Spells
Already covered: Sotha's Mirror, Reflect, Strong Reflect, Shalidor's Mirror, Wild Reflect, Llivam's Reversal, TD spells

MISSING: None — all vanilla Reflect spells are covered.

### Scrolls
- Scroll of Tranasa's Spelltrap: Reflect 20-60/30s Self → 20-60/120s [×4 dur; mag already good multiples of 5]

### Enchanted Items
- flamemirror robe_en: Resist Fire 20-40/60s + Reflect 20-30/60s → Resist Fire component scales separately (Resist Fire ×4) + Reflect 20-30/240s [×4 dur]
  NOTE: Both effects scale ×4! Resist Fire (base 2→0.5, ×4) and Reflect (base 10→2.5, ×4). So both get ×4 duration.
  Propose: Resist Fire 20-40/240s + Reflect 20-30/240s
- frostmirror robe_en: Resist Frost 20-40/10s + Reflect 20-30/10s → 20-40/40s + 20-30/40s [×4 both]
- poisonmirror robe_en: Resist Poison 20-40/10s + Reflect 20-30/10s → 20-40/40s + 20-30/40s [×4 both]
- shockmirror robe_en: Resist Shock 20-40/10s + Reflect 20-30/10s → 20-40/40s + 20-30/40s [×4 both]
- devil helm_en: Bound Gloves 60s + Reflect 20-30/10s → Bound unchanged + Reflect 20-30/40s [×4]
- Warlock's Ring (artifact): Reflect 10-20/30s + Fortify Speed 10-20/30s → Reflect 10-20/120s + Fortify Speed unchanged
- Ring of Equity (unique): Spell Absorption 100/30s + Reflect 70/30s → SpAbs 100/120s + Reflect 70/120s [both ×4]
- Marara's Ring (CE): Reflect 20 — CE items don't scale (always-on)

---

## Spell Absorption (base cost 10→2.5, compensation ×4)

### Spells
Already covered: Spell Absorption, Weak/Wild/Strong Spelldrinker, Tranasa's Spelltrap, Vivec's Feast, TD St. Horuscia's Alms

MISSING: None.

### Scrolls
- Scroll of Tranasa's Spellmire: Spell Absorption 20-60/30s Self → 20-60/120s [×4 dur]

### Enchanted Items
- spell absorption_en (10/5s Self): Amulet of Spell Absorption → 10/20s [×4 dur; fixed mag]
- flameeater robe_en: Resist Fire 20-40/10s + Spell Absorption 20-30/10s → 20-40/40s + 20-30/40s [both ×4]
- frosteater robe_en: Resist Frost 20-40/10s + Spell Absorption 20-30/10s → 20-40/40s + 20-30/40s [both ×4]
- poisoneater robe_en: Resist Poison 20-40/10s + Spell Absorption 20-30/10s → 20-40/40s + 20-30/40s [both ×4]
- shockeater robe_en: Resist Shock 20-40/10s + Spell Absorption 20-30/10s → 20-40/40s + 20-30/40s [both ×4]
- devil cephalopod (Bound Cuirass 60s + SpAbs 20-30/10s): → Bound unchanged + SpAbs 20-30/40s [×4]
- devil mole crab (Bound Boots 60s + SpAbs 20-30/10s): → Bound unchanged + SpAbs 20-30/40s [×4]
- Ring of Equity (unique): SpAbs 100/30s + Reflect 70/30s → SpAbs 100/120s + Reflect 70/120s [both ×4; fixed mags, no-range exception]
- Amulet of Heartthrum (artifact): Fortify Magicka 40/30s + SpAbs 10-20/30s + Lightning Shield 20/30s → FortMag unchanged + SpAbs 10-20/120s + LightShield 20/60s [SpAbs ×4; LightShield: base cost 3 unchanged, no compensation]
  Wait — Lightning Shield base cost is 3 (unchanged). So only SpAbs scales here.
  Propose: Fortify Magicka 40/30s + SpAbs 10-20/120s + Lightning Shield 20/30s

---

## Lock (base cost 2→24, ×12 — use cost overrides, not magnitude changes)

### Spells
Already covered: TD Dalgor's Entwining [8→96], TD Wizard Lock [2→24]

MISSING vanilla spell:
- Fenrick's Doorjam: Lock 10 Touch, cost 1 → cost override [1→12]

### Scrolls
- Scroll of Galmes' Seal: Lock 20-80/1ft Target → cost override or leave as-is?
  Since scrolls don't have a "cost" in the same way (they're one-use), the base cost increase just makes the scroll's enchantment more expensive to create. For scrolls, the magnitude IS the lock level — reducing it makes the scroll weaker. Following the pattern of cost overrides for Lock: no magnitude change needed for scrolls. The scroll just becomes more expensive in terms of enchant points, which is already baked into the item.
  Propose: No change to scroll magnitude. Note that the scroll's effective enchantment cost increases naturally.

### Enchanted Items
- lock_en (Lock 5 Touch): Amulet of Locking → No magnitude change (Lock level = gameplay utility). The increased base cost means the enchantment uses more charge per cast, which is the intended nerf.
  Propose: No value change — the base cost increase already nerfs charge efficiency.

---

## Burden (base cost 1→0.1, compensation ×10)

### Spells
Already covered: All vanilla and TD Burden spells are in the README.

### Scrolls
Already covered: Scroll of Baleful Suffering, Scroll of Fader's Leaden Flesh (in Enchantments README)

### Enchanted Items
Already covered: Black Jinx, Spear of the Hunter, TD Scroll of Makkun's Heavy Hand
- burden_en (20/10s Target): Robe of Burdens → 200/10s [fixed mag ×10; no-range exception applies since min==max=20, don't round. 20×10=200]
  NOTE: This item isn't in the Enchantments README yet.

---

## Feather (base cost 1→0.1, compensation ×10)

### Spells
Already covered: Feather, Strong Feather, Great Feather, Ulms' Juicedaw Feather, TD spells

### Scrolls
Already covered: Scroll of Ulm Juiceda's Feather (in Enchantments README)

### Enchanted Items
Already covered: feather_en, saint's shield_en, ulms juicedaw's feather_enu

MISSING:
- Feather Shield (feather_shield): uses feather_en enchantment — already covered (20/10s → 40/50s... wait, README shows 40/50s which is ×2 mag, ×5 dur = ×10 total ✓)
  All feather enchanted items are covered.

---

## Swift Swim (base cost 2→0.5, compensation ×4)

### Spells
Already covered: Buoyancy, Swimmer's Blessing, TD Dreugh's Grace

### Scrolls
- Scroll of Reynos' Fins: Swift Swim 50/180s + Water Breathing 180s → Swift Swim 200/180s + WB unchanged [50×4=200; fixed mag no-range exception, don't round. 200 is mult of 5 anyway]
  Or: 50/720s (×4 dur) — but 720s = 12 minutes, seems excessive for a scroll.
  Propose: 200/180s [×4 on magnitude, keep duration]

### Enchanted Items
None with Swift Swim enchantment in vanilla clothing/armor.

---

## Damage Magicka (base cost 8→4, compensation ×2)

### Spells
Already covered: Soulpinch (1-20→1-40), TD Thimble of Magefire (10-30/1s→10-30/2s)

MISSING: None — Soulpinch is the only vanilla purchasable DM spell.

TD Spells:
- Mind Rot: DM 1-15/2s component → 1-30/2s [×2 mag] or 1-15/4s [×2 dur]
  Propose: 1-30/2s [×2 mag, matching Soulpinch pattern]

### Scrolls
Already covered: Scroll of The Black Storm (DM component in Enchantments README as 0-10→0-10 rounding only)
  WAIT — The Enchantments README shows "Scroll of The Black Storm: 0-12/5s → 0-10/5s" for the Shock Damage component. The DM component (1-10/2s) needs ×2:
  DM 1-10/2s → 1-20/2s [×2 mag]
  This is NOT yet in the README.

### Enchanted Items
- soulpinch_en (1-20/1s Touch): Soulpinch Charm → 1-40/1s [×2; 1 stays 1, 20×2=40]

---

## Reflect & Spell Absorption in Resist Robes (combined note)

The "eater" robes (Flameeater, Frosteater, Poisoneater, Shockeater) combine:
- Resist Element (base cost 2→0.5, ×4) 
- Spell Absorption (base cost 10→2.5, ×4)

Both effects get ×4 duration. Current vanilla: 20-40/10s + 20-30/10s → proposed: 20-40/40s + 20-30/40s

The "mirror" robes combine:
- Resist Element (×4)
- Reflect (×4)

Both get ×4 duration. Flamemirror is special: vanilla already has 60s duration (not 10s like others).
- Flamemirror: Resist Fire 20-40/60s + Reflect 20-30/60s → 20-40/240s + 20-30/240s
- Others (Frost/Poison/Shock mirror): 20-40/10s + 20-30/10s → 20-40/40s + 20-30/40s

The "guard" robes (Flameguard, Frostguard, etc.) have only Resist Element:
- 20-40/10s → 20-40/40s [×4]
- Magickguard Robe: 20-40/10s → 20-40/40s [×4]
- Poisonguard Robe: 20-40/10s → 20-40/40s [×4]
- Shockguard Robe: 20-40/10s → 20-40/40s [×4]
- Frostguard Robe: 20-40/10s → 20-40/40s [×4]
- Flameguard Robe: 20-40/10s → 20-40/40s [×4]

Also: Heart Wall cuirass (Resist Magicka 30/10s) → 30/40s [fixed mag, ×4 dur]

---

## Summary of ALL Missing Enchanted Items (not yet in README - Enchantments.md)

### Shield ×2
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| first barrier_en | 5/10s | 10/10s | Amulet of Shield, Brawler's Belt, First Barrier Belt/Ring, Herder's Belt |
| second barrier_en | 10/30s | 20/30s | Hunter's Belt, Second Barrier Belt/Ring |
| third barrier_en | 15/10s | 30/10s | Third Barrier Belt/Ring |
| fourth barrier_en | 20/10s | 40/10s | Khan Belt |
| fire shield_en | 3/5s | 5/5s | Chest of Fire, Helm of Holy Fire |
| lightning shield_en | 3/5s | 5/5s | Storm Helm |
| fiend_helm_en | LShield 3/10s | LShield 5/10s | Fiend Helm |
| hort_ledd_robe (unique) | Shield 5/30s | Shield 10/30s | Hort-Ledd's Robe |

### Damage Attribute ÷3
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| stumble_en | DA Agi 1-20/1s | 1-5/1s | Stumble Charm |
| bonebiter_en | DA Agi 20/1s | 7/1s | Bonebiter Charm [no-range exception] |
| gripes_en | DA End 1-20/1s | 1-5/1s | Gripes Charm |
| fuddle_en | DA Int 1-20/1s | 1-5/1s | Fuddle Charm |
| hex_en | DA Luck 1-20/1s | 1-5/1s | Hex Charm |
| clench_en | DA Spd 1-20/1s | 1-5/1s | Clench Charm |
| evil eye_en | DA Per 1-20/1s | 1-5/1s | Evil Eye Charm |
| woe_en | DA Wil 1-20/1s | 1-5/1s | Woe Charm |

### Drain Magicka ×10
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| ri_drainmagicka_en | 3-7/1s | 30-70/1s | Ring of Nullification |
| flay spirit [ranged]_en | 5-10/30s | 50-100/30s | Spiritstrike Ring |
| azura's servant (shield) | DrM 1-10/30s | DrM 10-100/30s | Azura's Servant |

### Drain Fatigue ×10
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| weariness_en | 1-10/1s | 10-100/1s | Shame Ring, The Chiding Cuirass |
| sleep_en | 1-15/3s | 10-150/3s | Sleep Amulet |
| exhaustion_en | 5-20/30s | 50-200/30s | Ring of Exhaustion |

### Damage Fatigue ×2
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| doze_en | 1-20/1s | 1-40/1s | Doze Charm |
| fleabite_en | 9-18/1s | 20-35/1s | Ring of Fleabite |
| hornhand_en | 15-36/1s | 30-70/1s | Ring of Hornhand |
| ironhand_en | 21-42/1s | 40-85/1s | Ring of Ironhand |
| knuckle luck_en | 3-120/1s | 5-240/1s | Ring of Knuckle Luck, Belt of Northern Knuck Knuck |

### Damage Magicka ×2
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| soulpinch_en | DM 1-20/1s | 1-40/1s | Soulpinch Charm |

### Charm ×2
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| zenithar whispers (unique) | 30/5s | 60/5s | Zenithar Whispers |
| zenithar's wiles (unique) | 1-50/5s | 1-100/5s | Zenithar's Wiles |

### Paralyze ÷2 (duration)
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| medusa's gaze_en | 5s | 2s | Ring of Medusa's Gaze, Adusamsi's Robe |
| amulet of admonition (unique) | 30s | 15s | Amulet of Admonition |
| shashev's ring (unique) | 15s | 7s | Shashev's Ring |

### Absorb Health ÷2
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| blood feast_en | 5-20/10s | 5-20/5s | Blood Feast Shield |
| vampire's kiss_en | 1-10/1s | 1-5/1s | Ring of Vampire's Kiss |
| vampiric ring (artifact) | AbsH 20-30/10s | AbsH 10-15/10s | Vampiric Ring |

### Detect Animal ×5
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| thong (artifact) | 150/5s | 150/25s | Thong of Zainab [fixed mag, ×5 dur] |

### Detect Key ×5
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| tevral's hawkshaw_en | 10/10s | 50/10s | Hawkshaw Ring |

### Detect Enchantment ×5
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| Detect_Enchantment_ring (unique) | 100/10s | 100/50s | Detect Enchantment Ring [fixed mag, ×5 dur] |

### Reflect ×4
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| flamemirror robe_en | Reflect 20-30/60s | 20-30/240s | Flamemirror Robe |
| frostmirror robe_en | Reflect 20-30/10s | 20-30/40s | Frostmirror Robe |
| poisonmirror robe_en | Reflect 20-30/10s | 20-30/40s | Poisonmirror Robe |
| shockmirror robe_en | Reflect 20-30/10s | 20-30/40s | Shockmirror Robe |
| devil helm_en | Reflect 20-30/10s | 20-30/40s | Devil Helm |
| warlock's ring (artifact) | Reflect 10-20/30s | 10-20/120s | Warlock's Ring |
| ring_equity (unique) | Reflect 70/30s | 70/120s | Ring of Equity |

### Spell Absorption ×4
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| spell absorption_en | 10/5s | 10/20s | Amulet of Spell Absorption |
| flameeater robe_en | SpAbs 20-30/10s | 20-30/40s | Flameeater Robe |
| frosteater robe_en | SpAbs 20-30/10s | 20-30/40s | Frosteater Robe |
| poisoneater robe_en | SpAbs 20-30/10s | 20-30/40s | Poisoneater Robe |
| shockeater robe_en | SpAbs 20-30/10s | 20-30/40s | Shockeater Robe |
| devil cephalopod | SpAbs 20-30/10s | 20-30/40s | Devil Cephalopod Helm |
| devil mole crab | SpAbs 20-30/10s | 20-30/40s | Devil Mole Crab Helm |
| ring_equity (unique) | SpAbs 100/30s | 100/120s | Ring of Equity |
| heartthrum (artifact) | SpAbs 10-20/30s | 10-20/120s | Amulet of Heartthrum |

### Resist Element ×4 (Robes & Armor)
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| flameguard_en | ResFire 20-40/10s | 20-40/40s | Flameguard Robe |
| frostguard_en | ResFrost 20-40/10s | 20-40/40s | Frostguard Robe |
| poisonguard_en | ResPoison 20-40/10s | 20-40/40s | Poisonguard Robe |
| shockguard_en | ResShock 20-40/10s | 20-40/40s | Shockguard Robe |
| magickguard | ResMagicka 20-40/10s | 20-40/40s | Magickguard Robe |
| great resist magicka_en | ResMagicka 30/10s | 30/40s | Heart Wall [fixed mag] |
| flamemirror robe_en | ResFire 20-40/60s | 20-40/240s | Flamemirror Robe |
| frostmirror robe_en | ResFrost 20-40/10s | 20-40/40s | Frostmirror Robe |
| poisonmirror robe_en | ResPoison 20-40/10s | 20-40/40s | Poisonmirror Robe |
| shockmirror robe_en | ResShock 20-40/10s | 20-40/40s | Shockmirror Robe |
| flameeater robe_en | ResFire 20-40/10s | 20-40/40s | Flameeater Robe |
| frosteater robe_en | ResFrost 20-40/10s | 20-40/40s | Frosteater Robe |
| poisoneater robe_en | ResPoison 20-40/10s | 20-40/40s | Poisoneater Robe |
| shockeater robe_en | ResShock 20-40/10s | 20-40/40s | Shockeater Robe |

### Burden ×10
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| burden_en | 20/10s | 200/10s | Robe of Burdens [fixed mag, no-range] |

### Swift Swim ×4
| Enchantment ID | Vanilla | Proposed | Items |
|---|---|---|---|
| (Scroll of Reynos' Fins) | SwiftSwim 50/180s | 200/180s | Scroll [fixed mag, ×4] |

---

## Missing Scroll Proposals (not yet in any README)

| Scroll | Effect | Vanilla | Proposed | Rationale |
|---|---|---|---|---|
| Scroll of The First Barrier | Shield | 5/30s | 10/30s | ×2 |
| Scroll of The Second Barrier | Shield | 10/30s | 20/30s | ×2 |
| Scroll of The Third Barrier | Shield | 15/30s | 30/30s | ×2 |
| Scroll of The Fourth Barrier | Shield | 20/30s | 40/30s | ×2 |
| Scroll of The Fifth Barrier | Shield | 25/30s | 50/30s | ×2 |
| Scroll of The Sixth Barrier | Shield | 30/30s | 60/30s | ×2 |
| Scroll of The Ninth Barrier | Shield 35/60s | 35/60s | 70/60s | ×2 (Shield only) |
| Scroll of Sertises' Porphyry | Paralyze | 15s | 7s | ÷2 |
| Scroll of Psychic Prison | Paralyze+Soultrap | 30s+30s | 15s+30s | Paralyze ÷2 only |
| Scroll of Illnea's Breath | Frost+Paralyze | 35-60+6s | unchanged+3s | Paralyze ÷2; Frost no-scale |
| Scroll of Drathis' Soulrot | Para+Poison+DA×2 | 5s+15-45/5s+0-50+0-50 | 2s+unchanged+0-15+0-15 | Para÷2; Poison no-scale; DA÷3 |
| Scroll of Tranasa's Spelltrap | Reflect | 20-60/30s | 20-60/120s | ×4 dur |
| Scroll of Tranasa's Spellmire | SpAbs | 20-60/30s | 20-60/120s | ×4 dur |
| Scroll of Red Death | AbsHealth | 5-25/5s | 5-10/5s | ÷2 |
| Scroll of Manarape | AbsMagicka | 5-25/15s | unchanged | AbsMag base cost 8→8, no change |
| Scroll of Reynos' Fins | SwiftSwim | 50/180s | 200/180s | ×4 mag |
| Scroll of Black Despair | DA Wil | 5-15/10s | 1-5/3s | ÷3 |
| Scroll of Black Fate | DA Luck | 5-15/10s | 1-5/3s | ÷3 |
| Scroll of Black Mind | DA Int | 5-15/10s | 1-5/3s | ÷3 |
| Scroll of Black Scorn | DA Per | 5-15/10s | 1-5/3s | ÷3 |
| Scroll of Black Sloth | DA Agi | 5-15/10s | 1-5/3s | ÷3 |
| Scroll of Black Weakness | DA Str | 5-15/10s | 1-5/3s | ÷3 |
| Scroll of The Black Storm | DM component | 1-10/2s | 1-20/2s | DM ×2 |

---

## Missing Vanilla Spell Proposals (not yet in README - Spells & Potions.md)

### Shield ×2
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Shield | 5/30s Self | 10/30s | |
| First Barrier | 10/30s Self | 20/30s | |
| Second Barrier | 20/30s Self | 40/30s | |
| Third Barrier | 30/30s Self | 60/30s | |
| Fourth Barrier | 40/30s Self | 80/30s | |
| Fifth Barrier | 50/30s Self | 100/30s | |
| Sixth Barrier | 60/30s Self | 120/30s | |

### Damage Attribute ÷3
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Evil Eye | DA Per 1-10/1s Touch | 1-5/1s | 10÷3=3.3→5 |
| Clench | DA Spd 1-20/1s Touch | 1-5/1s | 20÷3=6.7→5 |
| Emasculate | DA End 1-20/1s Touch | 1-5/1s | |
| Fuddle | DA Int 1-20/1s Touch | 1-5/1s | |
| Hex | DA Luck 1-20/1s Touch | 1-5/1s | |
| Stumble | DA Agi 1-20/1s Touch | 1-5/1s | |
| Woe | DA Wil 1-20/1s Touch | 1-5/1s | |

### Charm ×2
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Charming Touch | 30/30s Touch | 60/30s | fixed mag ×2 |
| Charm Mortal | 10-30/30s Target | 20-60/30s | ×2 mag |

### Paralyze ÷2
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Medusa's Gaze | 15s Target | 7s | 15÷2=7.5→7 |

### Absorb Health ÷2
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Righteousness | 10/1s Touch | 5/1s | fixed mag ÷2 |
| Absorb Health | 5-52/1s Touch | 1-25/1s | 5÷2=2.5→1; 52÷2=26→25 |

### Drain Magicka ×10
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Wild Flay Spirit | 1-20/3s Target | 10-200/3s | ×10 mag |
| Gash Spirit | 5-20/30s Touch | 50-200/30s | ×10 mag |
| Gash Spirit [Ranged] | 5-20/30s Target | 50-200/30s | ×10 mag |
| Flay Spirit | 5-20/60s Touch | 50-200/60s | ×10 mag |
| Drain Blood | DrM 5/30s component | DrM 50/30s | ×10; DrH unchanged |

### Detect Animal ×5
| Spell | Vanilla | Proposed | Notes |
|---|---|---|---|
| Detect Creature | 50-150/5s Self | 50-150/25s | ×5 dur (more useful than ×5 mag) |

### Swift Swim ×4 (Scroll)
| Scroll | Vanilla | Proposed | Notes |
|---|---|---|---|
| Scroll of Reynos' Fins | SwiftSwim 50/180s | 200/180s | ×4 mag; fixed mag |

---

## Open Questions / Decisions Needed

1. **Paralyze rounding**: 15÷2=7.5 → 7 or 8? (Duration exempt from mult-of-5, so just round to nearest int: 7 or 8)
2. **Bonebiter Charm** (DA Agi 20/1s, fixed mag): 20÷3=6.67 → 7? The no-range exception says don't round to mult-of-5, but the value must still be an integer. Propose 7.
3. **Scroll of Drathis' Soulrot Paralyze**: 5÷2=2.5 → 2 or 3?
4. **Medusa's Gaze enchantment**: 5÷2=2.5 → 2 or 3? (2s Paralyze is very short for a ring)
5. **Flamemirror Robe**: 240s duration (4 minutes) — is this too long for a Cast When Used item? Consider capping at 120s (×2 instead of ×4)?
6. **Ring of Equity**: SpAbs 100/120s + Reflect 70/120s — 2 minutes of near-immunity seems very strong. Consider capping?
7. **Absorb Health spell**: Should min magnitude go to 1 (floor) or stay at 5? Going to 1-25 from 5-52 is a big range compression.
8. **Detect Creature**: ×5 on duration (5s→25s) vs ×5 on magnitude (50-150→250-750)? Duration seems more practical.
9. **Lock spells/scrolls/items**: Confirm cost-override-only approach (no magnitude changes)?
10. **TD Mind Rot**: DM component 1-15/2s → ×2 on mag (1-30/2s) or dur (1-15/4s)?

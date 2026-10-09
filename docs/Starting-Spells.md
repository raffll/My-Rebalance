# Starting Spells — Reference

A new character begins knowing the spells whose `data.flags` contain
`PC_START_SPELL`. Data taken straight from the records — no assumptions.

An ESP only changes records it contains. R3 overrides **8** spell records to do
**4 swaps**: it drops the start flag from 4 vanilla spells and adds it to 4 new
ones. The 7 other vanilla start spells are absent from `R3 - Spells.json`, so
they keep their vanilla flag and stay starting spells unchanged.

Costs are **recalculated** from the formula
`(min+max) × dur × (base/40) + area × (base/40)`, ×1.5 for OnTarget, using each
table's base costs (vanilla table = vanilla base; R3 table = R3 base).

Sources: `tes3conv/Morrowind.json` (vanilla), `R3 - Spells.json` (R3).
Tribunal, Bloodmoon, and Patch for Purists add no PC-start spells (verified).

---

## Vanilla starting spells (12)

| School       | Spell                   | Effect                            | Cost |
|--------------|-------------------------|-----------------------------------|-----:|
| Alteration   | Shield                  | Shield 5/30s OnSelf               |   15 |
| Alteration   | Water Walking           | Water Walking 60s OnSelf          |    9 |
| Conjuration  | Bound Dagger            | Bound Dagger 60s OnSelf           |    6 |
| Conjuration  | Summon Ancestral Ghost  | Summon Ghost 60s OnSelf           |   21 |
| Destruction  | Exhausting Touch        | Drain Fatigue 5-20/60s OnTouch    |   75 |
| Destruction  | Fire Bite               | Fire Damage 15-30/1s OnTouch      |    6 |
| Illusion     | Chameleon               | Chameleon 10/30s OnSelf           |   15 |
| Illusion     | Sanctuary               | Sanctuary 10/30s OnSelf           |   15 |
| Mysticism    | Detect Creature         | Detect Animal 50-150/5s OnSelf    |   19 |
| Mysticism    | Tap Energy              | Absorb Fatigue 20/30s OnTarget    |  180 |
| Restoration  | Feet of Notorgo         | Fortify Speed 10/90s OnSelf       |   45 |
| Restoration  | Hearth Heal             | Restore Health 20-80/1s OnSelf    |   13 |

---

## R3 starting spells (12)

| School       | Spell                   | Change  | Effect                            | Cost |
|--------------|-------------------------|---------|-----------------------------------|-----:|
| Alteration   | First Barrier           | added   | Shield 10/30s OnSelf              |   15 |
| Alteration   | Water Walking           | kept    | Water Walking 60s OnSelf          |    9 |
| Conjuration  | Bound Dagger            | kept    | Bound Dagger 60s OnSelf           |    6 |
| Conjuration  | Summon Ancestral Ghost  | kept    | Summon Ghost 60s OnSelf           |   21 |
| Destruction  | Weariness               | added   | Drain Fatigue 10-100/20s OnTarget |   17 |
| Destruction  | Fire Bite               | kept    | Fire Damage 15-30/1s OnTouch      |    6 |
| Illusion     | Chameleon               | kept    | Chameleon 10/30s OnSelf           |   15 |
| Illusion     | Sanctuary               | kept    | Sanctuary 10/30s OnSelf           |   15 |
| Mysticism    | Detect Enchantment      | added   | Detect Enchantment 50/10s OnSelf  |    5 |
| Mysticism    | Tap Energy              | kept    | Absorb Fatigue 20/3s OnTarget     |   27 |
| Restoration  | Skylamp's Shadow        | added   | Fortify Speed 5-20/30s OnSelf     |   19 |
| Restoration  | Hearth Heal             | kept    | Restore Health 20-80/1s OnSelf    |   13 |

Notes on recalculated R3 costs:
- **Weariness** 10-100/20s OnTarget at Drain Fatigue base 0.2 → `(10+100)×20×(0.2/40)×1.5 = 16.5` ≈ **17**.
- **Tap Energy** is `AUTO_CALCULATE`; at Absorb Fatigue base 6 with the
  shortened 3s duration it recalcs to **27** in-game. Its stored `cost=180` is a
  stale vanilla leftover (ignored by the engine for auto spells).
- The 7 "kept" vanilla spells not in the ESP (Water Walking, Bound Dagger,
  Summon Ancestral Ghost, Fire Bite, Chameleon, Sanctuary, Hearth Heal) use
  vanilla base costs because R3 never overrides them — their cost equals the
  vanilla table.

---

## The 4 swaps

| Removed (flag off)  | Added (flag on)    | Shared role       |
|---------------------|--------------------|-------------------|
| Shield              | First Barrier      | Alteration shield |
| Exhausting Touch    | Weariness          | Drain Fatigue     |
| Detect Creature     | Detect Enchantment | Detect utility    |
| Feet of Notorgo     | Skylamp's Shadow   | Fortify Speed     |

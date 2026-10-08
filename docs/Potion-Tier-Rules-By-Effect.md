# Potion Tier Rules — By Effect

Per-effect reference for the potion-tier checker
(`scripts/check_potion_tiers.py`) and for manual edits.

For each effect: the current (R3) base cost, which rule category applies, and
the tier column. Column mapping uses the geometric-midpoint ranges in
`potion-tiers.md`. Axis classification (duration-only / magnitude-only /
neither) comes from `scripts/effect_axis_flags.json`.

Effects that **currently have at least one potion** are listed first, by rule
category. Effects that **no potion uses yet** are collected at the end of the
file (their rule is still defined so a future potion is covered).

## Rule categories

- **Standard** — uses both magnitude and duration. Tier-checked on the
  effect's current base-cost column (both axes).
- **Damage** — DamageAttribute/Health/Magicka/Fatigue/Skill. Tier-checked on
  **magnitude** against **column 1** (6/8/10/15/20 for B/C/S/Q/E); duration is
  not tiered or checked. Does NOT use the base-cost column.
- **Duration-only** — magnitude is always 1. Tier-checked on **duration** only,
  using the column for `effective base = base_cost / 40`.
- **No-scale** — Fire/Frost/Shock Damage, Poison. Keep vanilla magnitude/
  duration (rounding only). NOT tier-checked.
- **Magnitude-only** — Lock, Open, Dispel. Magnitude is a level/chance, not a
  tier value. NOT tier-checked.
- **Neither** — Mark/Recall/Interventions, all Cure*. Instant toggles. NOT
  tier-checked.
- **Multi-effect** — any potion with 2+ effects is NOT tier-checked regardless
  of its effects.

===============================================================================
# PART 1 — Effects that have potions
===============================================================================

## Standard — tier-checked (both axes, base-cost column)

| Effect              | School      | Base | Column |
|---------------------|-------------|-----:|:------:|
| Burden              | Alteration  | 0.1  |  0.1   |
| Feather             | Alteration  | 0.1  |  0.1   |
| SwiftSwim           | Alteration  | 0.5  |  0.5   |
| Shield              | Alteration  | 1.0  |   1    |
| FireShield          | Alteration  | 3.0  |   2    |
| FrostShield         | Alteration  | 3.0  |   2    |
| LightningShield     | Alteration  | 3.0  |   2    |
| Jump                | Alteration  | 3.0  |   2    |
| Levitate            | Alteration  | 3.0  |   2    |
| SlowFall            | Alteration  | 3.0  |   2    |
| DrainAttribute      | Destruction | 1.0  |   1    |
| Blind               | Illusion    | 1.0  |   1    |
| Chameleon           | Illusion    | 1.0  |   1    |
| Sanctuary           | Illusion    | 1.0  |   1    |
| Sound               | Illusion    | 1.0  |   1    |
| Light               | Illusion    | 0.2  |  0.2   |
| NightEye            | Illusion    | 0.2  |  0.2   |
| DetectAnimal        | Mysticism   | 0.15 |  0.2   |
| DetectEnchantment   | Mysticism   | 0.2  |  0.2   |
| DetectKey           | Mysticism   | 0.2  |  0.2   |
| Reflect             | Mysticism   | 2.5  |   2    |
| SpellAbsorption     | Mysticism   | 2.5  |   2    |
| ResistCommonDisease | Restoration | 0.1  |  0.1   |
| FortifyFatigue      | Restoration | 0.25 |  0.2   |
| ResistBlightDisease | Restoration | 0.25 |  0.2   |
| ResistParalysis     | Restoration | 0.2  |  0.2   |
| ResistFire          | Restoration | 0.5  |  0.5   |
| ResistFrost         | Restoration | 0.5  |  0.5   |
| ResistShock         | Restoration | 0.5  |  0.5   |
| ResistMagicka       | Restoration | 0.5  |  0.5   |
| ResistPoison        | Restoration | 0.5  |  0.5   |
| FortifyAttribute    | Restoration | 1.0  |   1    |
| FortifyAttackBonus  | Restoration | 1.0  |   1    |
| FortifyHealth       | Restoration | 1.0  |   1    |
| FortifyMagicka      | Restoration | 1.0  |   1    |
| RestoreFatigue      | Restoration | 2.5  |   2    |
| RestoreHealth       | Restoration | 5.0  |   5    |
| RestoreMagicka      | Restoration | 5.0  |   5    |
| RestoreAttribute    | Restoration | 8.0  |   8    |

## Damage — magnitude only (column 1), duration skipped

Magnitude follows column 1 (6/8/10/15/20 for B/C/S/Q/E). Duration not tiered.

| Effect          | School      | Base |
|-----------------|-------------|-----:|
| DamageFatigue   | Destruction | 2.0  |
| DamageMagicka   | Destruction | 4.0  |
| DamageHealth    | Destruction | 8.0  |
| DamageAttribute | Destruction | 24.0 |

## Duration-only — magnitude always 1, tier-checked on duration

Column from `effective base = base_cost / 40`.

| Effect         | School     | Base | eff. base | Column | Durations (B/C/S/Q/E) |
|----------------|------------|-----:|-----------|:------:|-----------------------|
| Silence        | Illusion   | 40   | 1.0       |   1    | 18/24/30/45/60        |
| Paralyze       | Illusion   | 80   | 2.0       |   2    | 9/12/18/24/30         |
| Invisibility   | Illusion   | 20   | 0.5       |  0.5   | 30/45/60/90/120       |
| WaterBreathing | Alteration | 3    | 0.075     |  0.1   | 180/240/300/450/600   |
| WaterWalking   | Alteration | 3    | 0.075     |  0.1   | 180/240/300/450/600   |

## Magnitude-only — NOT tier-checked

| Effect | School    | Base | Note                               |
|--------|-----------|-----:|------------------------------------|
| Dispel | Mysticism | 5.0  | Fixed magnitude 100 (full dispel). |

## Multi-effect / special potions — NOT tier-checked

Any potion with 2+ effects is skipped (e.g. the 6-effect Fortify Casting
potions, the Spoiled Slowfall combos). The tier table applies only to
single-effect potions.

===============================================================================
# PART 2 — Effects with NO potion yet (rule defined for the future)
===============================================================================

## Standard — would tier on base-cost column

| Effect                  | School      | Base | Column |
|-------------------------|-------------|-----:|:------:|
| TurnUndead              | Conjuration | 0.2  |  0.2   |
| CommandCreature         | Conjuration | 15.0 |   8    |
| CommandHumanoid         | Conjuration | 15.0 |   8    |
| DrainFatigue            | Destruction | 0.2  |  0.2   |
| DrainMagicka            | Destruction | 0.4  |  0.5   |
| DisintegrateArmor       | Destruction | 0.6  |  0.5   |
| DrainSkill              | Destruction | 1.0  |   1    |
| DisintegrateWeapon      | Destruction | 1.2  |   1    |
| StuntedMagicka          | Destruction | 1.0  |   1    |
| SunDamage               | Destruction | 1.0  |   1    |
| DrainHealth             | Destruction | 4.0  |   5    |
| Vampirism               | Destruction | 5.0  |   5    |
| WeaknessToFire          | Destruction | 2.0  |   2    |
| WeaknessToFrost         | Destruction | 2.0  |   2    |
| WeaknessToShock         | Destruction | 2.0  |   2    |
| WeaknessToMagicka       | Destruction | 2.0  |   2    |
| WeaknessToPoison        | Destruction | 2.0  |   2    |
| WeaknessToNormalWeapons | Destruction | 2.0  |   2    |
| WeaknessToCommonDisease | Destruction | 2.0  |   2    |
| WeaknessToBlightDisease | Destruction | 4.0  |   5    |
| WeaknessToCorprus       | Destruction | 4.0  |   5    |
| Corprus                 | Destruction | 2500 |   8    |
| CalmCreature            | Illusion    | 1.0  |   1    |
| CalmHumanoid            | Illusion    | 1.0  |   1    |
| DemoralizeCreature      | Illusion    | 1.0  |   1    |
| DemoralizeHumanoid      | Mysticism   | 1.0  |   1    |
| FrenzyCreature          | Illusion    | 1.0  |   1    |
| FrenzyHumanoid          | Illusion    | 1.0  |   1    |
| RallyCreature           | Illusion    | 0.2  |  0.2   |
| RallyHumanoid           | Illusion    | 0.2  |  0.2   |
| Charm                   | Illusion    | 2.5  |   2    |
| Telekinesis             | Mysticism   | 1.0  |   1    |
| AbsorbAttribute         | Mysticism   | 2.0  |   2    |
| AbsorbSkill             | Mysticism   | 2.0  |   2    |
| SoulTrap                | Mysticism   | 2.0  |   2    |
| AbsorbFatigue           | Mysticism   | 6.0  |   5    |
| AbsorbMagicka           | Mysticism   | 8.0  |   8    |
| AbsorbHealth            | Mysticism   | 16.0 |   8    |
| RestoreSkill            | Restoration | 1.0  |   1    |
| FortifySkill            | Restoration | 4.0  |   5    |
| FortifyMagickaMultiplier| Restoration | 4.0  |   5    |
| ResistCorprus           | Restoration | 5.0  |   5    |
| ResistNormalWeapons     | Restoration | 5.0  |   5    |

(FortifySkill appears only on the multi-effect Fortify Casting potions, which
are skipped as multi-effect; no single-effect FortifySkill potion exists.)

## Damage — magnitude only (column 1), duration skipped

| Effect      | School      | Base |
|-------------|-------------|-----:|
| DamageSkill | Destruction | 8.0  |

## Duration-only — Summon / Bound (magnitude always 1)

Column from `effective base = base_cost / 40`. No graded potion is expected.

| Effect                 | Base | eff. base | Column |
|------------------------|-----:|-----------|:------:|
| SummonGhost            | 7    | 0.175     |  0.2   |
| SummonFabricant        | 10   | 0.25      |  0.2   |
| SummonScamp            | 12   | 0.30      |  0.2   |
| SummonLeastBonewalker  | 13   | 0.325     |  0.5   |
| SummonSkeleton         | 13   | 0.325     |  0.5   |
| SummonGreaterBonewalker| 15   | 0.375     |  0.5   |
| SummonClannfear        | 22   | 0.55      |  0.5   |
| SummonFlameAtronach    | 23   | 0.575     |  0.5   |
| SummonBonelord         | 25   | 0.625     |  0.5   |
| SummonCenturionSphere  | 25   | 0.625     |  0.5   |
| SummonFrostAtronach    | 27   | 0.675     |  0.5   |
| SummonDremora          | 28   | 0.70      |  0.5   |
| SummonHunger           | 29   | 0.725     |   1    |
| SummonBear             | 30   | 0.75      |   1    |
| SummonBoneWolf         | 30   | 0.75      |   1    |
| SummonWolf             | 30   | 0.75      |   1    |
| SummonDaedroth         | 32   | 0.80      |   1    |
| SummonStormAtronach    | 38   | 0.95      |   1    |
| SummonTwilight         | 52   | 1.30      |   1    |
| SummonGoldenSaint      | 55   | 1.375     |   1    |
| BoundDagger            | 2    | 0.05      |  0.1   |
| BoundLongsword         | 2    | 0.05      |  0.1   |
| BoundMace              | 2    | 0.05      |  0.1   |
| BoundBattleAxe         | 2    | 0.05      |  0.1   |
| BoundSpear             | 2    | 0.05      |  0.1   |
| BoundLongbow           | 2    | 0.05      |  0.1   |
| BoundCuirass           | 2    | 0.05      |  0.1   |
| BoundHelm              | 2    | 0.05      |  0.1   |
| BoundBoots             | 2    | 0.05      |  0.1   |
| BoundShield            | 2    | 0.05      |  0.1   |
| BoundGloves            | 2    | 0.05      |  0.1   |

## No-scale — NOT tier-checked (keep vanilla, rounding only)

| Effect      | School      | Base |
|-------------|-------------|-----:|
| FireDamage  | Destruction | 8.0  |
| FrostDamage | Destruction | 8.0  |
| ShockDamage | Destruction | 8.0  |
| Poison      | Destruction | 8.0  |

## Magnitude-only — NOT tier-checked

| Effect | School     | Base | Note                    |
|--------|------------|-----:|-------------------------|
| Lock   | Alteration | 24.0 | Magnitude = lock level. |
| Open   | Alteration | 12.0 | Magnitude = lock level. |

## Neither axis — NOT tier-checked (instant toggles)

| Effect              | School      | Base | Note             |
|---------------------|-------------|-----:|------------------|
| Mark                | Mysticism   | 350  | Teleport anchor. |
| Recall              | Mysticism   | 350  | Teleport.        |
| DivineIntervention  | Mysticism   | 150  | Teleport.        |
| AlmsiviIntervention | Mysticism   | 150  | Teleport.        |
| CureCommonDisease   | Restoration | 300  | Instant cure.    |
| CureBlightDisease   | Restoration | 2000 | Instant cure.    |
| CureCorprus         | Restoration | 2500 | Instant cure.    |
| CurePoison          | Restoration | 100  | Instant cure.    |
| CureParalyzation    | Restoration | 100  | Instant cure.    |
| RemoveCurse         | Restoration | 15   | Instant.         |

# Remastered Rebalance Redux - Potions

Sets graded potions (Bargain, Cheap, Standard, Quality, Exclusive) to fixed
magnitude/duration tiers at startup. The tier column comes from the effect base
cost loaded at that moment, so results follow whatever the load order provides.
When R3 - Spells loads before R3 - Potions, the R3 base costs are used.

------------------------------------------------------------

## Tiers

```
| Grade     |    10    |    5     |    2     |    1     |   0.5    |   0.2    |   0.1    |
|-----------|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| Bargain   |   1/3s   |   2/6s   |   3/9s   |  6/18s   |  10/30s  |  20/60s  | 60/180s  |
| Cheap     |   2/6s   |   3/9s   |  4/12s   |  8/24s   |  15/45s  |  30/90s  | 80/240s  |
| Standard  |   3/9s   |  4/12s   |  6/18s   |  10/30s  |  20/60s  | 40/120s  | 100/300s |
| Quality   |  4/12s   |  6/18s   |  8/24s   |  15/45s  |  30/90s  | 60/180s  | 150/450s |
| Exclusive |  6/18s   |  8/24s   |  10/30s  |  20/60s  | 40/120s  | 80/240s  | 200/600s |
```

------------------------------------------------------------

## Column

The base cost goes to the nearest column (geometric midpoint between columns).

```
10                                          7.07 and above
5                                           3.16 - 7.07
2                                           1.41 - 3.16
1                                           0.71 - 1.41
0.5                                         0.32 - 0.71
0.2                                         0.14 - 0.32
0.1                                         below 0.14
```

*Effects*
```
Standard                                    magnitude and duration from column
Duration only                               duration from column of base / 40
Damage                                      magnitude from column 1, duration kept
Fire/Frost/Shock Damage, Poison             never tiered
No duration                                 never tiered
```

Duration only: Paralyze, Silence, Invisibility, Water Breathing, Water Walking
and other effects without magnitude. Damage: Damage Attribute, Health, Magicka,
Fatigue, Skill.

------------------------------------------------------------

## Potions

Single-effect potions whose id ends in `_b`, `_c`, `_s`, `_q` or `_e` (Bargain to
Exclusive). The tier magnitude replaces both ends of a range (5-10 -> 6).
Multi-effect potions and potions without a grade suffix keep their values.
Potion value is not changed.

------------------------------------------------------------

## Names

Old R3 potion names for 46 potions (`scripts/R3PotionsLua/names.lua`), e.g.
`Bargain Potion of Fire Shield` -> `Bargain Fire Shield`,
`Standard Fortify Fatigue Potion` -> `Standard Fortify Fatigue`,
`Potion of Detect Enchantments` -> `Potion of Detect Enchantment`.

------------------------------------------------------------

## Usage

No settings: enable `R3 - Potions.omwscripts` in the content list to apply, disable it
to turn it off. Changes apply at startup.

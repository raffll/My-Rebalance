# Remastered Rebalance Redux - Spells

Sets the R3 effect base costs at startup and converts buyable spells so they
keep their value. Everything is computed from the base costs the load order
provides, so results follow whatever other plugins change.

------------------------------------------------------------

## Base Costs

```
Absorb Fatigue                              6
Absorb Health                               16
Burden                                      0.1
Charm                                       2.5
Damage Attribute                            24
Damage Fatigue                              2
Damage Magicka                              4
Detect Animal                               0.15
Detect Enchantment                          0.2
Detect Key                                  0.2
Disintegrate Armor                          0.6
Disintegrate Weapon                         1.2
Drain Fatigue                               0.2
Drain Magicka                               0.4
Feather                                     0.1
Fire Damage                                 8
Fortify Fatigue                             0.25
Fortify Skill                               4
Frost Damage                                8
Lock                                        24
Open                                        12
Paralyze                                    80
Poison                                      8
Reflect                                     2.5
Resist Blight Disease                       0.25
Resist Common Disease                       0.1
Resist Fire                                 0.5
Resist Frost                                0.5
Resist Magicka                              0.5
Resist Poison                               0.5
Resist Shock                                0.5
Restore Attribute                           8
Restore Fatigue                             2.5
Shield                                      1
Shock Damage                                8
Sound                                       1
Spell Absorption                            2.5
Swift Swim                                  0.5
```

------------------------------------------------------------

## Conversion

Per effect:

```
factor = loaded base cost / R3 base cost
```

*Duration*
```
Whole change                                duration x factor
Fractional change                           kept as is
No duration                                 kept as is
Not whole seconds                           kept as is
```

- **Whole change**: the base cost is multiplied or divided by a whole number.
  1 -> 0.1 (x10), 2 -> 0.5 (x4), 40 -> 80 (x1/2).
- **Fractional change**: anything else. 5 -> 8 (x0.625), 4 -> 6 (x2/3).
- **Not whole seconds**: duration x factor has a fraction or is under 1s.
  3s x1/2 = 1.5s, 1s x1/3 = 0.33s.

Magnitude, area and range never change.

*Cost*
```
Autocalc                                    engine prices it from base costs
Fixed cost                                  cost x new formula / old formula
Fixed cost 0                                stays 0
```

The formula is the engine's spell cost (`calcEffectCost`, x1.5 on target),
before and after conversion. A clean duration conversion keeps the cost; any
effect kept as is moves it.

Multi-effect spells: each effect follows its own rule; the cost is computed
once over all effects.

------------------------------------------------------------

## Spells

Buyable spells only: spells sold by a spell merchant in the Tamriel Rebuilt load
order (vanilla, Tamriel Data, Tamriel Rebuilt, Project Cyrodiil, Skyrim: Home of
the Nords) that use an effect listed above. Other spells keep their values;
autocalc ones are still priced from the new base costs by the engine.

------------------------------------------------------------

## Names

```
burden of sin                               Great Burden of Sin
great burden of sin                         Burden of Sin
fire_fathasa_unique                         Fathasa's Fire Barrier
frost_shield                                Weak Frost Shield
lightning shield                            Shock Shield
shock shield                                Lightning Shield
```

------------------------------------------------------------

## Usage

No settings: enable `R3 - Spells.omwscripts` in the content list to apply, disable it
to turn it off. Changes apply at startup.

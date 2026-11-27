# Remastered Rebalance Redux - Spells

Converts buyable spells at startup so they keep their value when the effect
base costs change. The base costs are set by R3 - Core (menu toggle, see its
README). This plugin reads them from the game and compares them with the
vanilla costs the spells were made for. With R3 - Core off or not enabled the
costs are vanilla, the factor is 1 and nothing changes. Enable
`R3 - Core.omwscripts` before this plugin; a warning is logged if not.

------------------------------------------------------------

## Conversion

Per effect:

```
factor = vanilla base cost / base cost in the game
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
autocalc ones are still priced from the base costs in the game by the engine.

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

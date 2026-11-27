# Remastered Rebalance Redux - Rounding

Rounds the magnitude ranges of buyable spells at startup, so every range end
is 1 or a multiple of 5. Works with or without R3 - Spells, in any load order.

------------------------------------------------------------

## Rule

```
Ranged magnitude                            each end to 1 or a multiple of 5
Fixed magnitude                             kept
No magnitude (Paralyze, Silence...)         kept
Duration                                    kept
```

*Range ends*
```
1                                           1
2                                           1
3 - 4                                       5
5 and above                                 nearest multiple of 5
```

*Examples*
```
5-11                                        5-10
2-20                                        1-20
3-12                                        5-10
10-24                                       10-25
```

------------------------------------------------------------

## Cost

```
Autocalc                                    engine prices it from magnitudes
Fixed cost                                  cost x new formula / old formula
Fixed cost 0                                stays 0
```

The formula is the engine's spell cost at the base costs loaded at that moment.
Fixed costs never go below 1.

------------------------------------------------------------

## Spells

Buyable spells only: spells sold by a spell merchant in the Tamriel Rebuilt load
order (vanilla, Tamriel Data, Tamriel Rebuilt, Project Cyrodiil, Skyrim: Home of
the Nords).

------------------------------------------------------------

## Usage

No settings: enable `R3 - Rounding.omwscripts` in the content list to apply, disable it
to turn it off. Changes apply at startup.

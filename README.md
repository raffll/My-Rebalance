# Rebalanced Rebalance Redux

#### Intentions
Regardless of the name, my intention here is not to balance the game. It's impossible. Neither make it harder nor easier. The reason behind this is to make more options useful for the fun of role-playing more specialized characters.

------------------------------------------------------------

#### Philosophy
- Simplicity
- Modularity
- Purist friendly

------------------------------------------------------------

#### Assumptions
- I highly recommend using my other mod: https://www.nexusmods.com/morrowind/mods/55507. Where the skill cap is set to 150 and the attribute cap is set to 300. It's not a requirement but a reasonable limit.
- OpenMW is used (vanilla may have different calculations, and MCP can fix some issues).
- Tamriel Rebuilt is used, but not required.
- Some kind of lua real time talking with NPC mod is used. This is mainly to prevent persuasion exploits.

------------------------------------------------------------

#### Inspirations
- BTB's Game Improvements
- Thief Experience Overhaul
- Spell Effects Rebalance: https://www.nexusmods.com/morrowind/mods/52858

------------------------------------------------------------

## Skills

Armorer skill is better suited in Endurance, as this attribute lacks any non-combat skill. Security is based on Agility anyway.
```
Armorer                         Strength -> Endurance
Security                        Intelligence -> Agility
```

------------------------------------------------------------

## Running

Just a 25% speed boost for PC, NPCs, and creatures.
```
fMinWalkSpeed                   100 -> 125
fMaxWalkSpeed                   200 -> 250
fMinWalkSpeedCreature             5 -> 6.25
fMaxWalkSpeedCreature           300 -> 375
```

------------------------------------------------------------

## Alchemy

This is the best skill in the game. It's impossible to compare it with buyable potions because they are using completely different formulas. Pre-made potions are made from templates, like in a factory. However, self-made potions all have the same magnitude and duration at the same spell effect base cost. Those mechanics are not quite suitable for some spell effects.

But the main problem is that you can successfully create excellent restore fatigue potions (200 pts) with Alchemy at 5, making other choices garbage on the same level (e.g., restore fatigue equivalent will cost you 15 mana with a 9% chance at Restoration level 5).

So after applying this patch, some potions will be much weaker (but others still not so much) than pre-made counterparts and spells. But overall, you can get good results with decent stats and equipment at average levels, and buyable potions will be useful much longer.
```
fPotionStrengthMult             0.5 -> 0.1          5x smaller magnitude, duration and price.
```

Secret Master's apparatus prices were lower than Grandmaster's in some cases. Now they are 5x more expensive.
```
apparatus_sm_alembic_01         1600 -> 8000
apparatus_sm_calcinator_01      3200 -> 16000
apparatus_sm_mortar_01          6000 -> 30000
apparatus_sm_retort_01          1000 -> 5000
```

------------------------------------------------------------

## Enchant

This is the worst skill in the game. Self-made enchantments are almost impossible to do. You don't need to recharge items because they are recharging by themselves. And at the end, the secret master will attack you on sight.

Those changes are trying to make self-enchanting as good as an enchanter service but forcing you to go and hunt for soulgems to keep your equipment useful. As a fighter or thief, you have to do better resource management or just buy the same item again.
```
sMagicInsufficientCharge                            Removed annoing message.
fMagicItemRechargePerSecond     0.05 -> 0           Disabled idle recharging.
fEnchantmentChanceMult          3 -> 0.6            5x easier self enchant.
```

#### How to enchant high-level spell - 100pts/24s spell (with a magic effect base cost of 1):
- Enchanter -- 17000gp with Mercantile 100 and Disposition 100. Mercantile, Intelligence, and Luck are taken into account but capped at 100.
- Self-Enchant -- 53% chance of making an item with Enchant 100 and average (50) attributes.

------------------------------------------------------------

## Barter

The economy is broken because there is an unlimited supply of money in the game, so making everything more expensive won't fix the problem. The real problem is a player mindset that wants to just replace all garbage with money as quickly as possible. You don't need to do that. Pick only valuable items and sell them when you really need cash. And the only scenario when you really need cash is to buy an enchanted item or to train with a trainer. There should already be enough money on the market to suit those needs for one month.

Additionally, it will force you to invest in Speechcraft and Mercantile to get better prices.
```
fBarterGoldResetDelay           24 -> 720           30 days to reset merchants gold.
```

------------------------------------------------------------

## Pickpocket

It's a stat game between you and NPC, but in vanilla your max chance was only 56% regardless of stats, because the cap was set to 75% and the check is done twice, on picking an item and on closing the pickpocket window.

Also, it's not even realistic to take item price into account, so I disabled that requirement.
```
iPickMaxChance                  75 -> 95            5% chance of being caught anyway.
fPickPocketMod                  0.3 -> 0            Any item available to steal.
```

------------------------------------------------------------

## Magic

Lots of spell effects weren't really useful because of better alternatives. Also, it's worth trying elemental shield now, for the fun of killing low-level creatures.
```
fElementalShieldMult            0.1 -> 1            1 point of damage for 1 point of magnitude.
sEffectSlowFall                 SlowFall -> Slowfall
```

------------------------------------------------------------

#### Alteration

Those weren't useful previously. Feather cost was the same as Fortify Strength, resulting in being 5x weaker in encumbrance gain. The same rule applies to Swift Swim.
```
Feather                         1 -> 0.1            2x encumbrance gain than Fortify Strength.
Burden                          1 -> 0.1            2x encumbrance lost than Drain Strength.
Swift Swim                      2 -> 0.5            2x faster swim than Fortify Speed.
```

------------------------------------------------------------

#### Destruction

Elemental damage doesn't make sense; there is no point in using spells other than fire or frost damage. However, I want to preserve some flavor here anyway. Damage Fatigue is almost useless or very powerful, depending on if you are using the "Uncapped Damage Fatigue" setting. So I leave it untouched.
```
Fire Damage                          5.0            Unchanged.
Frost Damage                    5 -> 5.25
Shock Damage                    7 -> 5.5
Damage Health                   8 -> 5.75
Poison                          9 -> 6.0
```

Disintegrate would be better as an offensive skill in other schools; in Destruction, there is no point in using it. It was only useful for stealing armor, and now it's easier.
```
Disintegrate Armor              6 -> 1
Disintegrate Weapon             6 -> 1
```

------------------------------------------------------------

#### Illusion

There was no point in using them instead of paralysis.
```
Silence                         40 -> 20            2x cheaper than Paralyze.
Sound                           3 -> 0.8            2x cheaper at 25% than Paralyze.
Demoralize Humanoid             Mysticism -> Illusion
```

------------------------------------------------------------

#### Mysticism

Absorb spells were overpowered at the same cost as damage spells. A single effect has an advantage over two effects combined, so the cost will be 50% higher.
```
Absorb Health                   8 -> 12             Damage Health (5.75) + Restore Health (5) = 10.75
Absorb Fatigue                  4 -> 6              Damage Fatigue (4) + Restore Fatigue (1) = 5
```

Detect spells were just too expensive.
```
Detect Animal                   0.75 -> 0.15
Detect Enchantment              1 -> 0.2
Detect Key                      1 -> 0.2
```

------------------------------------------------------------

#### Restoration

Fortify Magicka was doing less than Fortify Intelligence for the same price. Fortifying skill over 50 should be available only for the highest-level characters.
```
Fortify Magicka                 1 -> 0.75           25% cheaper than Fortify Intelligence.
Fortify Skill                   1 -> 4              4x more expensive.
```

------------------------------------------------------------

## Lockpicking

The main goal here is to make Security useful on higher skill levels and, additionally, to be better than Alteration. Previously there was no benefit from raising Security over 50.

The second goal is to make opening 100-point locks possible only for higher-level characters. Earlier, magic was a better option to unlock the door at any level with cheap spells and scrolls. Now it requires a mage skilled in Alteration to use existing open spells. Or even a well-trained mage to create one, because self-made spells are 2x more expensive than standalones. For warriors, scrolls still exist, but they are nerfed or have the price increased because they are widely available.
```
fPickLockMult                   -1 -> -1.25         Locks are harder to unlock.
```

#### Spell Effect
```
Open                            6 -> 12
```

#### Price
```
sc_ondusisunhinging             73 -> 273           Available in stores.
```

#### Magnitude
```
sc_ekashslocksplitter_en        100 -> 80

open                                   20           Unchanged, unavailable in vanilla.
ondusi's open door               50 -> 40
strong open                      50 -> 60
great open                       50 -> 80           Unavailable in vanilla.
wild open                              1-100        Unchanged.
```

#### How to open a 100-point lock:
- Thief -- Security starting from level 60 (6% with pick quality 1.4 and average (50) attributes).
- Mage -- Alteration starting from level 60 (spell costs 120 with an 8% chance on average (50) attributes).
- Warrior -- Enchanting service -- 27000gp with Mercantile 50 and Disposition 100.

------------------------------------------------------------

Trap mechanic is restored; formerly, anyone could untrap any trap easily. So, from now on, the trap spell cost will be taken into account on disarming, similar to the lock level. Common trap costs don't make any sense, so I readjusted them to give a better challenge (you can see average damage in the brackets).
```
fTrapCostMult                    0 -> -1            Trap spell cost is taken into account.
```

#### Cost
```
trap_fire00         (30)         3 -> 10
trap_frost00        (30)         3 -> 15
trap_shock00        (30)         5 -> 20
trap_health00       (30)         8 -> 25
trap_poison00       (150)       16 -> 50

trap_paralyze00     (10s)       13 -> 30
trap_silence00      (30s)       37 -> 35

trap_fire_killer    (200)        3 -> 60
trap_frost_killer   (200)        3 -> 65
trap_shock_killer   (200)        5 -> 70
trap_poison_killer  (375)       16 -> 100
```

#### How to untrap 100-point spell:
- Thief -- Security starting from level 90 (8% with probe quality 1.25 and average (50) attributes).
- Mage -- Telekinesis.
- Warrior -- Take it on the chin.

------------------------------------------------------------

## History
```
- 1.1
    - Elemental damage costs increased
    - Detect spells 5x cheaper
    - Secret Master's apparatus 5x more expensive
```
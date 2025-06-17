# Rebalanced Rebalance Redux

#### Intentions

Regardless of the name, my intention here is not to balance the game. It's impossible. Neither make it harder nor easier. The reason behind this is to make more options useful for the fun of role-playing more specialized characters. This mod includes changes to spell effects, lockpicking, traps, alchemy, enchanting, and many more!

**You will be overpowered anyway! But the path to achieve that will be more fun!**

------------------------------------------------------------

#### Philosophy

- Simplicity -- I prefer to change as little as possible to achieve the goal. It's easier to maintain and more compatible.
- Modularity -- Everything is divided into separate modules, so you can mix and match with other mods.
- Purist friendly -- Changes done here are carefully implemented as if they were in the game from the beginning.

------------------------------------------------------------

#### Assumptions

- Patch for Purists is applied.
- OpenMW is used (vanilla may have different calculations, and MCP can fix some issues).
- Tamriel Rebuilt is used, but not required.
- Some kind of real-time talking with NPC mod is recommended. This is mainly to prevent persuasion exploits.
- "Use Magic Item Animation" setting is on in OpenMW (or equivalent in MCP).

If you are using MCP, leave vanilla mechanics for creating spells.
- Max spell magnitude at 100 for 1440s. Creating spells with a magnitude over 100 is overpowered in most cases.
- Self-made spell with one additional second added while calculating cost. This is because a 100/1s spell is much more powerful than a 1/100s spell at the same cost. In vanilla, a 100/1s spell will cost 2x more.
- $${\color{orange}\*\*}$$ Only one spell effect per spell. This can be used as a workaround for the cap on magnitude.

$${\color{orange}\*\*}$$ Ideally we need a mod that allows a bigger magnitude cap for some effects like Feather. Some spells shouldn't be allowed to have 1s duration, like Charm. Summon spells should allow summoning a couple of skeletons in one spell. But until we have that, it's impossible to balance the spell system when those "cheats" are enabled.

I highly recommend using my other mod: https://www.nexusmods.com/morrowind/mods/55507.
- The skill cap is set to 150, and the attribute cap is set to 300.
- $${\color{orange}\*\*}$$ Potion consumption is limited to prevent stacking too many effects.
- $${\color{orange}\*\*}$$ Training limit is enabled. This just simply removes the leveling problem.

It's not a requirement but a reasonable limit.

------------------------------------------------------------

#### Inspirations

- BTB's Game Improvements
- Thief Experience Overhaul
- HotFusion's Economy Adjuster
- Spell Effects Rebalance: https://www.nexusmods.com/morrowind/mods/52858
- Gentleman's Level-Up and Progression Rebalance: https://www.nexusmods.com/morrowind/mods/54569

------------------------------------------------------------

#### Compatibility

- If you are using Morag Tong Polished, enable also "Corrupted Crime - Morag Tong Polished.esp" at the end.

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
fMinWalkSpeedCreature           5 -> 6.25
fMaxWalkSpeedCreature           300 -> 375
```

------------------------------------------------------------

## Alchemy

My main goal here is to adjust potion creation to be more in line with what we have in stores. It's a difficult task to compare it with buyable potions because they are using entirely different formulas. Pre-made potions are made from templates, like in a factory. And that's fine; in real life, most things are standardized. However, self-made potions depend heavily on spell effect base cost, which may differ from effect to effect, and also have this automatic magnitude-to-duration ratio. At the end we have useless pre-made potions and overpowered self-made ones, or vice versa.

Another problem is that you can successfully create excellent restore fatigue potions (200 pts) with Alchemy at 5, making other choices garbage on the same level (e.g., restore fatigue equivalent will cost you 15 mana with a 9% chance at Restoration level 5).

So after applying this patch, some potions will be much weaker (up to 4x, but it depends on the spell effect). But overall, you can get good results with decent stats and equipment, and buyable potions will be useful much longer.
```
fPotionStrengthMult             0.5 -> 0.25         2x smaller magnitude, duration and price.
```

Secret Master's apparatus prices were lower than Grandmaster's in some cases. Now they are 5x more expensive.
```
apparatus_sm_alembic_01         1600 -> 8000
apparatus_sm_calcinator_01      3200 -> 16000
apparatus_sm_mortar_01          6000 -> 30000
apparatus_sm_retort_01          1000 -> 5000
```

#### How to create an exclusive potion - 20pts/60s (with a magic effect base cost of 1)
- You need Alchemy, Intelligence, and Luck at 100 and mortar with a quality of 1. Previously this was possible with Alchemy at 40.

------------------------------------------------------------

## Enchant

This is the worst skill in the game. Self-made enchantments are almost impossible to do. You don't need to recharge items because they are recharging by themselves. And at the end, the secret master will attack you on sight.

Those changes are trying to make self-enchanting as good as an enchanter service but forcing you to go and hunt for soulgems to keep your equipment useful. As a fighter or thief, you have to do better resource management or just buy the same item again.
```
sMagicInsufficientCharge                            Removed annoing message.
fMagicItemRechargePerSecond     0.05 -> 0           Disabled idle recharging.
fEnchantmentChanceMult          3 -> 0.6            5x easier self enchant.
```

#### How to enchant a high-level spell - 100pts/24s (with a magic effect base cost of 1)
- Enchanter -- 17000gp with Mercantile at 100 and Disposition at 100. Mercantile, Intelligence, and Luck are taken into account but capped at 100.
- Self-enchant -- 53% chance of making an item with Enchant at 100 and average (50) attributes.

------------------------------------------------------------

## Magic

Lots of spell effects weren't really useful because of better alternatives. Also, it's worth trying elemental shield now, for the fun of killing low-level creatures.
```
fElementalShieldMult            0.1 -> 1            1 point of damage for 1 point of magnitude.
sEffectSlowFall                 SlowFall -> Slowfall
```

------------------------------------------------------------

#### Alteration

Those weren't useful previously. Feather cost was the same as Fortify Strength, resulting in being 5x weaker in encumbrance gain. $${\color{orange}\*\*}$$ However, reducing encumbrance is more speed efficient than adding extra strength, but I decided to keep them that low anyway because the custom spell magnitude cap is set to 100, and those effects never will be fully useful without further game changes. Except in alchemy, where potions with those effects will be much stronger.
```
Feather                         1 -> 0.1            2x encumbrance gain than Fortify Strength.
Burden                          1 -> 0.1            2x encumbrance lost than Drain Strength.
```

The same rule applies to Swift Swim. $${\color{orange}\*\*}$$ It's doing only one thing, so it should do it better than Fortify Speed.
```
Swift Swim                      2 -> 0.5            2x faster swim than Fortify Speed.
```

------------------------------------------------------------

#### Destruction

Elemental damage doesn't make sense; there was no point in using spells other than fire or frost damage. However, I want to preserve some flavor here anyway. $${\color{orange}\*\*}$$ Finally, I decided to switch Damage Health with Poison for more consistency.
```
Fire Damage                          5.00           Unchanged.
Frost Damage                    5 -> 5.25
Shock Damage                    7 -> 5.50
Poison                          9 -> 5.75
Damage Health                   8 -> 6.00
```

$${\color{orange}\*\*}$$ Damage Magicka has been lowered to be on par with Damage Health.
```
Damage Magicka                  8 -> 6
```

Damage Fatigue is almost useless or very powerful, depending on if you are using the "Uncapped Damage Fatigue" setting. So I leave it untouched.
```
Damage Fatigue                       4              Unchanged.
```

$${\color{orange}\*\*}$$ Damage Attribute was so powerful that it outperforms almost every other "utility" spell. For 40 magicka, you could drop the target's Strength or Intelligence to 0, leaving the opponent without the ability to walk, fight, or cast spells.
```
Damage Attribute                8 -> 24
```

Disintegrate would be better as an offensive skill in other schools; in Destruction, there is no point in using it, other than for stealing armor, and now it's easier. $${\color{orange}\*\*}$$ Low-tier armor or weapons have durability around 300-500. With those adjustments, they can be destroyed by a 25-cost spell.
```
Disintegrate Armor              6 -> 1
Disintegrate Weapon             6 -> 1
```

$${\color{orange}\*\*}$$ Drain spells have been lowered to be at the same cost as fortify spells. The reason behind this is, once again, the maximum magnitude of 100 for those spells, so they are mostly useless on higher levels. Also, Drain Magicka was 4x more expensive than Drain Intelligence. Now it's 25% cheaper. The side effect of this is that many potion ingredients have them as a negative effect, and now they will be stronger, which is a good thing. Drain Health is unchanged because it can be too strong on lower levels.
```
Drain Health                         4              Unchanged.
Drain Magicka                   4 -> 0.75
Drain Fatigue                   2 -> 0.5
```

$${\color{orange}\*\*}$$ Drain Skill is now more expensive because it can be overpowered, the same way as Fortify Skill. Compared to Drain Attribute, it has a lot bigger impact, and at a cost of 1, it was just as good in combat as Blind, but more versatile.
```
Drain Skill                     1 -> 2
```

------------------------------------------------------------

#### Illusion

There was no point in using them instead of paralysis.
```
Silence                         40 -> 20            2x cheaper than Paralyze.
Sound                           3 -> 0.8            2x cheaper at 25% than Paralyze.
```

This is only bugfix.
```
Demoralize Humanoid             Mysticism -> Illusion
```

$${\color{orange}\*\*}$$ Here I have a dilemma: in vanilla, a spell with 1s duration can be enough. So, to fix that, I recommend using some kind of real-time dialogue mod instead.
```
Charm                           5                   Unchanged.
```

------------------------------------------------------------

#### Mysticism

Absorb spells were overpowered at the same cost as damage spells. A single effect has an advantage over two effects combined, so the cost should be higher. $${\color{orange}\*\*}$$ Furthermore, you can cast them on an area with multiple opponents or your minions to get massive health restoration.
```
Absorb Health                   8 -> 12             Damage Health (6) + Restore Health (5) = 11
Absorb Fatigue                  4 -> 6              Damage Fatigue (4) + Restore Fatigue (1) = 5
```

$${\color{orange}\*\*}$$ I decided to also include those effects, despite they are not being used by any craftable spell in the vanilla game.
```
Absorb Magicka                  8 -> 12             Damage Magicka (6) + Restore Magicka (5) = 11
Absorb Skill                    2 -> 6              Drain Skill (2) + Fortify Skill (4)
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
Fortify Skill                   1 -> 4
```

This looks like a typo to me, compared to other resistances.
```
Resist Paralysis                0.2 -> 2
```

------------------------------------------------------------

#### How to stop a mage with 100 Intelligence using a 120-cost spell

Damage spells are most powerful but need time to kick in; otherwise, they will cost 2x more.
```
Damage Intelligence     24      2 * 50s             Permanent drop 100 Intelligence over 50s.
Damage Magicka          6       4 * 100s            Permanent drop 400 Magicka over 100s.
```

Drain Intelligence is good if you don't have time or you're not skilled in Illusion. Drain Magicka is the worst, even after adjustment.  
```
Drain Intelligence      1       100 / 24s           Drop 100 Intelligence for 24s.
Drain Magicka           0,75    100 / 32s           Drop 100 Magicka for 32s.
```

Silence is 5x more effective than Drain Intelligence and also better if the opponent mage has more than 100 Intelligence. Sound may be 4x less efficient, but the opponent can still cast, wasting time and magicka.
```
Silence                 20      120s                Can't cast spells for 120s.
Sound                   0,8     100% / 30s          100% to fail for 30s.
```

------------------------------------------------------------

## Barter

The economy is broken because there is an unlimited supply of money in the game, so making everything more expensive won't fix the problem. The real problem is a player mindset that wants to just replace all garbage with money as quickly as possible. You don't need to do that. Pick only valuable items and sell them when you really need cash. And the only scenario when you really need cash is to buy an enchanted item or to train with a trainer. There should already be enough money on the market to suit those needs for one month.

Additionally, it will force you to invest in Speechcraft and Mercantile to get better prices. Another side effect of this is you have more time to get back money you already spent on enchantments or training if this person also offers to buy things.
```
fBarterGoldResetDelay           24 -> 720           30 days to reset merchants gold.
```

The Mages Guild's teleportation price is increased. As an instant and modern style of transportation, it shouldn't be lower than other conventional travel options.
```
fMagesGuildTravel               10 -> 100           10x more expensive.
```

------------------------------------------------------------

## Crime

You probably prefer to load your previous save game instead of accepting the punishment. But, if you don't, you'll realize that bounties are ridiculously small and just unrealistic. That's why the penalties for crime have been increased.
```
iCrimeKilling                   1000 -> 10000
iCrimeAttack                      40 -> 1000
iCrimePickPocket                  25 -> 250
iCrimeTresspass                    5 -> 500         Trespassing is a more serious crime
                                                    than pickpocketing.

iDaysinPrisonMod                 100 -> 1000        Days in prison will be the same as in vanilla.
```
The crime threshold is not changed, which means that the guard will be chasing you after one attack.
```
iCrimeThreshold                         1000        Unchanged.
```
The death penalty will be set after one killing, one attack, and any other crime. That means you have to be perfectly clean while doing MT's Writs.
```
Death Warrant                   5000 -> 11001       You can kill only one person, instead of 4.
```

------------------------------------------------------------

## Pickpocket

It's a stat game between you and NPC, but in vanilla your max chance was only 56% regardless of stats, because the cap was set to 75% and the check is done twice, on picking an item and on closing the pickpocket window.
```
iPickMaxChance                  75 -> 95            5% chance of being caught anyway.
```
It's not even realistic to take item price into account, so I disabled that requirement.
```
fPickPocketMod                  0.3 -> 0            Any item available to steal.
```

------------------------------------------------------------

## Lockpicking

The main goal here is to make Security useful on higher skill levels and, additionally, to be better than Alteration. Previously there was no benefit from raising Security over 50.

The second goal is to make opening 100-point locks possible only for higher-level characters. Earlier, magic was a better option to unlock the door at any level with cheap spells and scrolls. Now it requires a mage skilled in Alteration to use existing open spells. Or even a well-trained mage to create one, because self-made spells are 2x more expensive than standalones. For warriors, scrolls still exist, but they are nerfed or have the price increased because they are widely available.
```
fPickLockMult                   -1 -> -1.25         Locks are harder to unlock.
```

Spell effect cost:
```
Open                            6 -> 12             Spells are harder to cast.
```

Scroll price:
```
sc_ondusisunhinging             73 -> 273           Available in stores.
```

Scrolls & spells magnitude:
```
sc_ekashslocksplitter_en        100 -> 80           Available in random loot later in the game.

open                                   20           Unchanged, unavailable in vanilla.
ondusi's open door               50 -> 40
strong open                      50 -> 60
great open                       50 -> 80           Unavailable in vanilla.
wild open                              1-100        Unchanged.
```

#### How to open a 100-point lock
- Thief -- Security starting from level 60; 6% with pick quality 1.4 and average (50) attributes.
- Mage -- Alteration starting from level 60; spell costs 120 with an 8% chance on average (50) attributes.
- Warrior -- Enchanting service; 27000gp with Mercantile 50 and Disposition 100.

------------------------------------------------------------

## Traps

Trap mechanic is restored; formerly, anyone could untrap any trap easily. So, from now on, the trap spell cost will be taken into account on disarming, similar to the lock level.
```
fTrapCostMult                    0 -> -1            Trap spell cost is taken into account.
```

Common trap costs don't make any sense, so I readjusted them to give a better challenge (you can see average damage in the brackets).
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

#### How to untrap a 100-point spell
- Thief -- Security starting from level 90; 8% with probe quality 1.25 and average (50) attributes.
- Mage -- Telekinesis.
- Warrior -- Take it on the chin.

------------------------------------------------------------

## History
```
- 1.1
    - Elemental damage costs increased
    - Detect spells 5x cheaper
    - Secret Master's apparatus 5x more expensive
- 1.2
    - Lockpicking and traps split into separate esps
    - Alchemy adjusted
    - Mages Guild's travel 10x more expensive
- 1.3
    - Resist Paralysis spell 10x more expensive
    - Crime module added
- 1.4
    - Magic module revisited
```

$${\color{orange}\*\*}$$ -- added in version 1.4
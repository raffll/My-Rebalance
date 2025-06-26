# Remastered Rebalance Redux

#### Intentions

Regardless of the name, my intention here is not to balance the game. It's impossible. Neither make it harder nor easier. The reason behind this is to make more options useful for the fun of role-playing more specialized characters. This mod includes changes to spell effects, lockpicking, traps, alchemy, enchanting, and many more!

**You will be overpowered anyway! But the path to achieve that will be more fun!**

------------------------------------------------------------

#### Philosophy

- Simplicity -- I prefer to change as little as possible to achieve the goal. It's easier to maintain and more compatible.
- Modularity -- Everything is divided into separate modules, so you can mix and match with other mods.
- Purist friendly -- I'm trying to not make many arbitrary decisions. Most of the changes are multipliers or additions to existing values.
- Math-driven -- Seriously, I'm doing serious calculations here.

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
- Only one spell effect per spell. This can be used as a workaround for the cap on magnitude.

Ideally we need a mod that allows a bigger magnitude cap for some effects like Feather. Some spells shouldn't be allowed to have 1s duration, like Charm. Summon spells should allow summoning a couple of skeletons in one spell. But until we have that, it's impossible to balance the spell system when those "cheats" are enabled.

I highly recommend using my other mod: https://www.nexusmods.com/morrowind/mods/55507.
- The skill cap is set to 150, and the attribute cap is set to 300.
- Potion consumption is limited to prevent stacking too many effects.
- Training limit is enabled. This just simply removes the leveling problem.

It's not a requirement but a reasonable limit.

------------------------------------------------------------

#### Inspirations

- BTB's Game Improvements
- Thief Experience Overhaul
- HotFusion's Economy Adjuster
- Spell Effects Rebalance: https://www.nexusmods.com/morrowind/mods/52858
- Magicka Awakening - Magicka Costs Adjustments: https://www.nexusmods.com/morrowind/mods/51723
- Gentleman's Level-Up and Progression Rebalance: https://www.nexusmods.com/morrowind/mods/54569

------------------------------------------------------------

#### Compatibility

- If you are using Morag Tong Polished, enable also "Corrupted Crime - Morag Tong Polished.esp" at the end.

------------------------------------------------------------

#### History
```
1.1
  - Elemental damage costs increased
  - Detect spells 5x cheaper
  - Secret Master's apparatus 5x more expensive
1.2
  - Lockpicking and traps split into separate esps
  - Alchemy adjusted
  - Mages Guild's travel 10x more expensive
1.3
  - Resist Paralysis spell 10x more expensive
  - Crime module added
1.4
  - Magic module revisited
1.5
  - Magic module remastered
1.6
  - Name reinvented
  - Trap costs readjusted
  - Potion module added
  - Spell module added
```

* $${\color{red}\*1.5\*}$$ -- added or changed in version 1.5
* $${\color{yellow}\*1.6\*}$$ -- added or changed in version 1.6

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

Another problem is that you can successfully create excellent Restore Fatigue potions (200 pts) with Alchemy at 5, making other choices garbage on the same level (e.g., Restore Fatigue equivalent will cost you 15 Magicka with a 9% chance at Restoration level 5).

So after applying this patch, some potions will be much weaker (up to 4x, but it depends on the spell effect). But overall, you can get good results with decent stats and equipment, and buyable potions will be useful much longer.
```
fPotionStrengthMult             0.5 -> 0.25         2x smaller magnitude, duration and price.
```

Secret Master's apparatus prices were lower than Grandmaster's in some cases. Now they are 5x more expensive.
```
apparatus_sm_alembic_01         1600gp -> 8000gp
apparatus_sm_calcinator_01      3200gp -> 16000gp
apparatus_sm_mortar_01          6000gp -> 30000gp
apparatus_sm_retort_01          1000gp -> 5000gp
```

#### _How to create an exclusive potion - 20pts/60s (with a magic effect base cost of 1)_
- _You need Alchemy, Intelligence, and Luck at 100 and mortar with a quality of 1._
- _Previously this was possible with Alchemy at 40._

------------------------------------------------------------

## Enchant

This is the worst skill in the game. Self-made enchantments are almost impossible to do. You don't need to recharge items because they are recharging by themselves. And at the end, the secret master will attack you on sight.

Those changes are trying to make self-enchanting as good as an enchanter service but forcing you to go and hunt for soulgems to keep your equipment useful. As a fighter or thief, you have to do better resource management or just buy the same item again.
```
sMagicInsufficientCharge                            Removed annoing message.
fMagicItemRechargePerSecond     0.05 -> 0           Disabled idle recharging.
fEnchantmentChanceMult          3 -> 0.6            5x easier self enchant.
```

#### _How to enchant a high-level spell - 100pts/24s (with a magic effect base cost of 1)_
- _Enchanter -- 17000gp with Mercantile at 100 and Disposition at 100. Mercantile, Intelligence, and Luck are taken into account but capped at 100._
- _Self-enchant -- 53% chance of making an item with Enchant at 100 and average (50) attributes._

------------------------------------------------------------

## Magic

Fixes.
```
sEffectSlowFall                 SlowFall -> Slowfall
Demoralize Humanoid             Mysticism -> Illusion
```

#### _How to stop a mage using a 120-cost spell_
```
Mage with 120 Intelligence * 1.5 Magicka Multiplier = 180 Magicka
```

_Damage spells are most powerful but need time to kick in; otherwise, they will cost 2x more._
```
Damage Intelligence             2pts/50s            Permanent drop 150 Magicka over 50s.
Damage Magicka                  4pts/100s           Permanent drop 400 Magicka over 100s.

or

Damage Intelligence             50pts/1s            Permanent drop 75 Magicka.
Damage Magicka                  100pts/3s           Permanent drop 300 Magicka over 3s.
```

_Drain Intelligence is good if you don't have time or you're not skilled in Illusion. Drain Magicka is the worst, even after adjustment._
```
Drain Intelligence              100pts/24s          Drop 150 Magicka for 24s.
Drain Magicka                   100pts/32s          Drop 100 Magicka for 32s.
```

_Silence is 5x longer than Drain Intelligence and also better if the opponent mage has more than 100 Intelligence. Sound may be 4x less efficient, but the opponent can still cast, wasting time and magicka._
```
Silence                         120s                Can't cast any spells for 120s.
Sound                           100%/30s            100% to fail cast for 30s.
```

------------------------------------------------------------

### Alteration

It's worth trying elemental shields now, for the fun of killing low-level creatures. Cost is not changed, as it does two things: resist the element and damage the opponent that hits you. But even now with 10x more damage, it's just a gimmick compared to real damage spells.
```
fElementalShieldMult            0.1 -> 1            1 point of damage for 1 point of magnitude.
```

Those weren't useful previously. Feather cost was the same as Fortify Strength, resulting in being 5x weaker in encumbrance gain. However, reducing encumbrance is more speed efficient than adding extra strength, but I decided to keep them that low anyway because the custom spell magnitude cap is set to 100, and those effects never will be fully useful without further game changes. Except in alchemy, where potions with those effects will be much stronger.
```
Feather                         1 -> 0.1            2x encumbrance gain than Fortify Strength.
Burden                          1 -> 0.1            2x encumbrance lost than Drain Strength.
```

The same rule applies to Swift Swim. It's doing only one thing, so it should do it better than Fortify Speed.
```
Swift Swim                      2 -> 0.5            2x faster swim than Fortify Speed.
```

$${\color{red}\*1.5\*}$$ Jump and Slowfall are generally worse than Levitate. But using them together, they can be a cheaper alternative.
```
Jump                            3 -> 1
Slowfall                        3 -> 1
```

$${\color{red}\*1.5\*}$$ Shield even with this adjustment is worse than Sanctuary.
```
Shield                          2 -> 1
```

------------------------------------------------------------

### Destruction

Elemental damage didn't make sense; there was no point in using spells other than Fire or Frost Damage. So I lowered them all to almost the same levels. However, I wanted to preserve some flavor here anyway. Finally, I decided to switch Damage Health with Poison for more consistency.
```
Fire Damage                          5.00           Unchanged.
Frost Damage                    5 -> 5.25
Shock Damage                    7 -> 5.50
Poison                          9 -> 5.75
Damage Health                   8 -> 6.00
```

Damage Magicka has been lowered to be on par with Damage Health.
```
Damage Magicka                  8 -> 6
```

Damage Fatigue is almost useless or very powerful, depending on if you are using the "Uncapped Damage Fatigue" setting. So I leave it untouched.
```
Damage Fatigue                       4              Unchanged.
```

Damage Attribute was so powerful that it outperforms almost every other "utility" spell. For 40 Magicka, you could drop the target's Strength or Intelligence to 0, leaving the opponent without the ability to walk, fight, or cast spells.
```
Damage Attribute                8 -> 24
```

Disintegrate would be better as an offensive skill in other schools; in Destruction, there is no point in using it, other than for stealing armor, and now it's easier. Low-tier armor or weapons have durability around 300-500. With those adjustments, they can be destroyed by a 25-cost spell. It's a equivalent of 100pts Fire Damage.
```
Disintegrate Armor              6 -> 1
Disintegrate Weapon             6 -> 1
```

Drain spells have been lowered to be at the same cost as fortify spells. The reason behind this is, once again, the maximum magnitude of 100 for those spells, so they are mostly useless on higher levels. Also, Drain Magicka was 4x more expensive than Drain Intelligence. Now it's 25% cheaper. The side effect of this is that many potion ingredients have them as a negative effect, and now they will be stronger, which is a good thing. Drain Health is unchanged because it can be too strong on lower levels.
```
Drain Health                         4.00           Unchanged.
Drain Magicka                   4 -> 0.75
Drain Fatigue                   2 -> 0.50
```

Drain Skill is now more expensive because it can be overpowered, the same way as Fortify Skill. Compared to Drain Attribute, it has a lot bigger impact, and at a cost of 1, it was just as good in combat as Blind, but more versatile.
```
Drain Skill                     1 -> 2
```

------------------------------------------------------------

### Illusion

There was no point in using them instead of paralysis.
```
Silence                         40 -> 20            2x cheaper than Paralyze.
Sound                           3 -> 0.8            2x cheaper at 25% than Paralyze.
```

Here I have a dilemma: in vanilla, a spell with 1s duration can be enough. So, to fix that, I recommend using some kind of real-time dialogue mod instead.
```
Charm                           5                   Unchanged.
```

------------------------------------------------------------

### Mysticism

Absorb spells were overpowered at the same cost as damage spells. A single effect has an advantage over two effects combined, so the cost should be higher. Furthermore, you can cast them on an area with multiple opponents or your minions to get massive health restoration.
```
Absorb Health                   8 -> 12             Damage Health (6) + Restore Health (5) = 11
Absorb Fatigue                  4 -> 6              Damage Fatigue (4) + Restore Fatigue (1) = 5
```

I decided to also include those effects, despite they are not being used by any craftable spell in the vanilla game.
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

$${\color{red}\*1.5\*}$$ Those are just more powerful variants of resist spells. Too expensive on lower levels and not very useful anymore on higher levels.
```
Reflect                         10 -> 4
Spell Absorption                10 -> 4
```

------------------------------------------------------------

### Restoration

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

## Magic - Potions

$${\color{yellow}\*1.6\*}$$ Using new spell effect costs those potions that were too different from their self-made counterparts are now 10x stronger.

```
p_burden_b                      5pts/8s -> 50pts/80s         Bargain Potion of Burden
p_burden_c                      8pts/15s -> 80pts/150s       Cheap Potion of Burden
p_burden_s                      10pts/30s -> 100pts/300s     Standard Potion of Burden
p_burden_q                      15pts/45s -> 150pts/450s     Quality Potion of Burden
p_burden_e                      20pts/60s -> 200pts/600s     Exclusive Potion of Burden

p_feather_b                     5pts/8s -> 50pts/80s         Bargain Potion of Feather
p_feather_c                     8pts/15s -> 80pts/150s       Cheap Potion of Feather
p_feather_q                     15pts/45s -> 150pts/450s     Quality Potion of Feather
p_feather_e                     20pts/60s -> 200pts/600s     Exclusive Potion of Feather

p_detect_creatures_s            10pts/15s -> 100pts/150s     Potion of Detect Creatures
p_detect_key_s                  10pts/15s -> 100pts/150s     Potion of Detect Key
p_detect_enchantment_s          10pts/15s -> 100pts/150s     Potion of Detect Enchantments
```

------------------------------------------------------------

## Magic - Spells & Scrolls

$${\color{yellow}\*1.6\*}$$ Spells are adjusted when they are too cheap or too expensive using new spell effect costs.

```
armor eater                     10-30pts -> 100-300pts
weapon eater                    6-25pts  -> 60-250pts
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

$${\color{yellow}\*1.6\*}$$ Crime bounties lowered from previous version. This time they are only 5x higher than vanilla.
```
iCrimeKilling                   1000 -> 5000
iCrimeAttack                    40 -> 200
iCrimePickPocket                25 -> 100
iCrimeTresspass                 5 -> 25

iDaysinPrisonMod                100 -> 500          Days in prison will be the same as in vanilla.
```

The crime threshold lowered, which means that the guard will be chasing you after one attack.
```
iCrimeThreshold                 1000 -> 200
```

The death penalty will be set after one killing, one attack, and any other crime. That means you have to be perfectly clean while doing MT's Writs.
```
Death Warrant                   5000 -> 5201        You can kill only one person, instead of 4.
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

#### Cost
```
Open                            6 -> 12             Spells are harder to cast.
```

#### Price
```
sc_ondusisunhinging             73gp -> 273gp       Available in stores.
```

#### Magnitude
```
sc_ekashslocksplitter_en        100pts -> 80pts     Available in random loot later in the game.

open                                     20pts      Unchanged, unavailable in vanilla.
ondusi's open door              50pts -> 40pts
strong open                     50pts -> 60pts
great open                      50pts -> 80pts      Unavailable in vanilla.
wild open                                1-100pts   Unchanged.
```

#### _How to open a 100-point lock_

- _Thief -- Security starting from level 60; 6% with pick quality 1.4 and average (50) attributes._
- _Mage -- Alteration starting from level 60; spell costs 120 with an 8% chance on average (50) attributes._
- _Warrior -- Enchanting service; 27000gp with Mercantile 50 and Disposition 100._

------------------------------------------------------------

## Traps

Trap mechanic is restored; formerly, anyone could untrap any trap easily. So, from now on, the trap spell cost will be taken into account on disarming, similar to the lock level.
```
fTrapCostMult                   0 -> -1             Trap spell cost is taken into account.
```

Common trap costs didn't make any sense, so I readjusted them to give a better challenge.

$${\color{yellow}\*1.6\*}$$ They are now auto-calculated from the new magic effect costs.
```
trap_fire00                     3 -> 8              2-20pts/3s
trap_frost00                    3 -> 9              2-20pts/3s
trap_shock00                    5 -> 9              2-20pts/3s
trap_health00                   8 -> 10             2-20pts/3s
trap_poison00                   16 -> 52            1-5pts/60s

trap_paralyze00                 13 -> 21            10s
trap_silence00                  37 -> 31            30s

trap_fire_killer                3 -> 63             20-30pts/10s
trap_frost_killer               3 -> 66             20-30pts/10s
trap_shock_killer               5 -> 69             20-30pts/10s
trap_poison_killer              16 -> 108           5-10pts/50s
```

#### _How to untrap a 100-point spell_
- _Thief -- Security starting from level 90; 8% with probe quality 1.25 and average (50) attributes._
- _Mage -- Telekinesis._
- _Warrior -- Take it on the chin._
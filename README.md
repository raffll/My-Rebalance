# Remastered Rebalance Redux

#### Intentions

Despite the name, my intention here is not to balance the game. That’s impossible. Nor is it to make it harder or easier. The idea is to make more options usable, especially for the fun of role-playing more specialized characters. This mod includes changes to spell effects, lockpicking, traps, alchemy, enchanting, and many more!

------------------------------------------------------------

#### Philosophy

- Simplicity - I prefer to change as little as possible to achieve the goal. It's easier to maintain and more compatible.
- Modularity - Everything is divided into separate modules, so you can mix and match with other mods.
- Purist friendly - I try to avoid arbitrary decisions. Most changes are multipliers or additions to existing values.
- Math-driven - Seriously, I'm doing real calculations here.

------------------------------------------------------------

#### Assumptions

- Patch for Purists is applied.
- OpenMW is preferred (vanilla may have different calculations, and MCP can fix some issues).
- Tamriel Rebuilt is used, but not required.
- "Use Magic Item Animation" setting is on in OpenMW (or equivalent in MCP).

If you are using MCP, leave vanilla mechanics for creating spells:
- Maximum spell magnitude is set to 100 for 1440 seconds. Creating spells with a magnitude over 100 is generally overpowered.
- Self-made spells have one additional second added when calculating cost. A 100/1s spell is much more powerful than a 1/100s spell at the same cost. In vanilla, a 100/1s spell costs twice as much.
- Only one spell effect per spell is allowed.

Ideally, a mod that allows a higher magnitude cap for certain effects like Feather is needed. Some spells shouldn’t be allowed to have a 1-second duration, such as Charm. Summon spells should allow summoning multiple skeletons in one spell. Until such mods exist, balancing the spell system is impossible when these "cheats" are enabled.

------------------------------------------------------------

#### Recommendations

- Using some form of real-time dialogue mod with NPCs is recommended, primarily to prevent persuasion exploits.
- I also recommend my other mod: https://www.nexusmods.com/morrowind/mods/55507, which sets the skill cap to 150 and the attribute cap to 300, limits potion consumption, and enables a training limit per level.

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

If you are using *Morag Tong Polished*, make sure to also enable "**Corrupted Crime - Morag Tong Polished.esp**" at the end of your load order.

------------------------------------------------------------

#### History

* $${\color{green}\*1.9\*}$$ -- added or changed in version 1.9
* $${\color{lime}\*1.8\*}$$ -- added or changed in version 1.8
* $${\color{orange}\*1.7\*}$$ -- added or changed in version 1.7
* $${\color{yellow}\*1.6\*}$$ -- added or changed in version 1.6
* $${\color{red}\*?\*}$$ -- will be added in the future

------------------------------------------------------------

## Skills

Armorer skill is better suited in Endurance, as this attribute lacks any non-combat skill. Meanwhile, Security is based on Agility anyway.
```
Armorer                             Strength -> Endurance
Security                            Intelligence -> Agility
```

------------------------------------------------------------

## Running

Applies a simple 25% speed boost to the player, NPCs, and creatures.
```
fMinWalkSpeed                       100 -> 125
fMaxWalkSpeed                       200 -> 250
fMinWalkSpeedCreature               5 -> 6.25
fMaxWalkSpeedCreature               300 -> 375
```

------------------------------------------------------------

## Alchemy

The main goal here is to fix the imbalance at low skill levels. For example, you can easily make highly effective Restore Fatigue potions (e.g., 200 points) with only 5 Alchemy, while a similar Restore Fatigue spell at Restoration level 5 would cost 15 Magicka and have just a 9% success rate. This makes some choices clearly superior to others with little effort.

After this patch, some potion effects—depending on the underlying spell effect—may be up to four times weaker. However, the system as a whole should feel more balanced. Crafted potions will still scale well with better stats and equipment, while store-bought potions will remain useful for much longer.
```
fPotionStrengthMult                 0.5 -> 0.25         2x smaller magnitude, duration and price
```

Some Secret Master's apparatuses were cheaper than Grandmaster versions. They all are now five times more expensive.
```
Secret Master's Alembic             1600gp -> 8000gp
Secret Master's Calcinator          3200gp -> 16000gp
Secret Master's Mortar & Pestle     6000gp -> 30000gp
Secret Master's Retort              1000gp -> 5000gp
```

------------------------------------------------------------

## Enchant

This was one of the weakest skills in the game. Creating your own enchantments was nearly impossible, and you didn’t even need to recharge enchanted items—they recharged automatically. To make things worse, the Secret Master would attack you on sight.

These changes aim to make self-enchanting a viable alternative to using an enchanter while requiring you to actively hunt for soul gems to keep your equipment charged. As a fighter or thief, you'll need to manage your resources more carefully—or just buy a replacement item when needed.
```
sMagicInsufficientCharge            "Item does not have enough charge." -> ""
fMagicItemRechargePerSecond         0.05 -> 0           Disabled idle recharging
fEnchantmentChanceMult              3 -> 0.6            5x easier self enchant
```

------------------------------------------------------------

## Magic

------------------------------------------------------------

### Alteration

Elemental shields are now worth experimenting with—especially for the fun of killing low-level creatures. Their cost hasn’t changed, since they serve a dual purpose: providing elemental resistance and dealing damage to attackers. Even with 10x more damage, though, they remain more of a gimmick than a true alternative to direct damage spells.
```
fElementalShieldMult                0.1 -> 1            1 point of damage for 1 point of magnitude
```

Previously, Feather wasn’t very useful because its cost matched Fortify Strength, so it provided five times less encumbrance increase per point.
```
Feather                             1 -> 0.1            2x encumbrance gain than Fortify Strength
Burden                              1 -> 0.1            2x encumbrance lost than Drain Strength
```

The same logic applies to Swift Swim, which affects only swimming speed and should therefore outperform Fortify Speed.
```
Swift Swim                          2 -> 0.5            2x faster swim than Fortify Speed
```

Jump and Slowfall are generally harder to use than Levitate, but used together, they should offer a more affordable alternative.
```
Jump                                3 -> 1
Slowfall                            3 -> 1

sEffectSlowFall                     SlowFall -> Slowfall
```

Even with this adjustment, Shield remains less effective than Sanctuary.
```
Shield                              2 -> 1
```

$${\color{lime}\*1.8\*}$$ The cost of these spell effects has been changed to be on par with Lockpicking.
```
Open                                6 -> 12
Lock                                2 -> 24
```

------------------------------------------------------------

### Conjuration

$${\color{red}\*?\*}$$ TODO

------------------------------------------------------------

### Destruction

Elemental damage felt unbalanced—there was little reason to use anything other than Fire or Frost. To address this, I adjusted all elemental damage types to the same level.
```
Fire Damage                         5 -> 6
Frost Damage                        5 -> 6
Shock Damage                        7 -> 6
Poison                              9 -> 6
Damage Health                       8 -> 6
```

Damage Magicka has been reduced to align with Damage Health.
```
Damage Magicka                      8 -> 6
```

Damage Fatigue remains unchanged, as it is either nearly useless or very powerful depending on the "Uncapped Damage Fatigue" setting.
```
Damage Fatigue                           4              Unchanged
```

Damage Attribute was so powerful it outperformed almost every other "utility" spell. For just 40 Magicka, you could reduce the target’s Strength or Intelligence to zero, leaving them unable to walk, fight, or cast spells.
```
Damage Attribute                    8 -> 24
```

Low-tier gear typically has a durability of around 300–500. With these changes, it can now be destroyed by a 25-cost spell—the equivalent of 100 points of Fire Damage.
```
Disintegrate Armor                  6 -> 1
Disintegrate Weapon                 6 -> 1
```

Drain spells have been lowered to match the cost of corresponding Fortify spells. This change reflects that the 100-magnitude cap makes them mostly ineffective at higher levels. Additionally, Drain Magicka was four times more expensive than Drain Intelligence; now it’s 20% cheaper. As a side effect, many potions with these negative effects will become stronger.
```
Drain Magicka                       4 -> 0.8
Drain Fatigue                       2 -> 0.5
```

Drain Skill is now more expensive due to its potential for being overpowered—similar to Fortify Skill. Compared to Drain Attribute, it has a much greater impact.
```
Drain Skill                         1 -> 2
```

* $${\color{lime}\*1.8\*}$$ Drain Magicka changed from 0.75 to 0.8. Now it's exactly 5x cheaper.
* $${\color{green}\*1.9\*}$$ All elemental damage costs changed to 6. **TODO**

------------------------------------------------------------

### Illusion

Previously, there was little reason to use these effects over Paralyze.
```
Silence                             40 -> 20            2x cheaper than Paralyze
Sound                               3 -> 1              2x cheaper at 20% than Paralyze
```

Additionally, a bugfix related to Illusion has been included.
```
Demoralize Humanoid                 Mysticism -> Illusion
```

* $${\color{lime}\*1.8\*}$$ Sound changed from 0.8 to 1. Now it's exactly 3x cheaper.

------------------------------------------------------------

### Mysticism

Absorb spells were previously overpowered, costing the same as their damage-based counterparts. Since each Absorb spell effectively combines two effects—damage and restore—it should come at a higher cost.
```
Absorb Health                       8 -> 12             Damage Health (6) + Restore Health (5)
Absorb Fatigue                      4 -> 6              Damage Fatigue (4) + Restore Fatigue (1)
```

The following effects, while not available in any vanilla craftable spells, have been adjusted for consistency.
```
Absorb Magicka                      8 -> 12             Damage Magicka (6) + Restore Magicka (5)
Absorb Skill                        2 -> 6              Drain Skill (2) + Fortify Skill (4)
```

Detect spells were just too expensive.
```
Detect Animal                       0.75 -> 0.15
Detect Enchantment                  1 -> 0.2
Detect Key                          1 -> 0.2
```

Reflect and Spell Absorption are essentially stronger versions of resist effects. They were just too costly to be useful.
```
Reflect                             10 -> 4
Spell Absorption                    10 -> 4
```

------------------------------------------------------------

### Restoration

Fortify Magicka was doing less than Fortify Intelligence for the same price.
```
Fortify Magicka                     1 -> 0.8            20% cheaper than Fortify Intelligence
```

Fortifying skill over 50 should be available only for the highest-level characters.
```
Fortify Skill                       1 -> 4
```

This looks like a typo compared to other resistances.
```
Resist Paralysis                    0.2 -> 2
```

$${\color{lime}\*1.8\*}$$ Fortify Magicka changed from 0.75 to 0.8. To be on par with Drain Magicka.

------------------------------------------------------------

## Barter

The economy is broken because there is an unlimited supply of money in the game, so simply making everything more expensive won’t fix the problem. The real issue is a player mindset focused on quickly replacing all items with gold. You don’t need to do that. Instead, pick only valuable items and sell them when you truly need cash. Typically, the only times you’ll really need cash are to purchase enchanted items or pay for training. There should already be enough money in the market to cover those needs for about a month.

Additionally, this encourages investing in Speechcraft and Mercantile to secure better prices. A beneficial side effect is having more time to recover money spent on enchantments or training, especially if the merchant also buys your items.
```
fBarterGoldResetDelay               24 -> 720           30 days to reset merchants' gold
```

The Mages Guild’s teleportation price has been increased. As a fast, modern form of travel, it shouldn’t be cheaper than traditional methods.
```
fMagesGuildTravel                   10 -> 100           10x more expensive
```

------------------------------------------------------------

## Crime

You might prefer loading a previous save rather than facing the consequences. But if you don’t, you’ll quickly see that bounties were previously unrealistically low. That’s why crime penalties have been increased significantly.
```
iCrimeKilling                       1000 -> 5000
iCrimeAttack                        40 -> 200
iCrimePickPocket                    25 -> 100
iCrimeTresspass                     5 -> 25

iDaysinPrisonMod                    100 -> 500          Days in prison same as in vanilla
```

The crime threshold is lowered, so guards will pursue you after just one attack.
```
iCrimeThreshold                     1000 -> 200
```

The death warrant will be triggered after a combination of one killing, one attack, and any other crime. This means you must be perfectly clean while doing MT’s Writs.
```
Death Warrant                       5000 -> 5201        You can kill only one person, instead of 4
```

$${\color{yellow}\*1.6\*}$$ Crime bounties have been reduced from the previous version; they are now only 5 times higher than vanilla values.

------------------------------------------------------------

## Pickpocket

Pickpocketing is essentially a stat-based contest between you and the NPC. However, in vanilla, your maximum success chance was capped at just 56%, no matter your stats, because the cap was set to 75% and the check happens twice—once when picking the item and again when closing the pickpocket window.
```
iPickMaxChance                      75 -> 95            5% chance of being caught anyway
```

It also didn’t make much sense to factor in the item’s value when determining success, so I removed that requirement.
```
fPickPocketMod                      0.3 -> 0            Any item available to steal
```

------------------------------------------------------------

## Lockpicking

The primary goal is to make the Security skill more valuable at higher levels and to ensure it’s more effective than Alteration for lock-related tasks. Previously, raising Security above 50 provided no real benefit.
```
fPickLockMult                       -1 -> -1.25         Locks harder to unlock
```

The second goal is to ensure that unlocking 100-point locks is only achievable by higher-level characters. Previously, cheap Alteration spells and scrolls made magic a better option for unlocking doors at any level.

```
Open                                6 -> 12             2x increased base cost
Lock                                2 -> 24
```

Now, using existing open spells requires a mage skilled in Alteration, or even a master mage to create new ones, since self-made spells cost twice as much as standalone spells.
```
Open                                         20pts      Unchanged, unavailable in vanilla
Ondusi's Open Door                  50pts -> 40pts
Strong Open                         50pts -> 60pts
Great Open                          50pts -> 80pts      Unavailable in vanilla
Wild Open                                    1-100pts   Unchanged
```

For warriors, scrolls remain available but have been nerfed or had their prices increased due to their widespread availability.
```
Scroll of Ondusi's Unhinging        73gp -> 273gp       Available in stores
Scroll of Ekash's Lock Splitter     100pts -> 80pts     Available in random loot later in the game
```

$${\color{lime}\*1.8\*}$$ The cost of the Lock spell effect has been changed from 60 to 24.

------------------------------------------------------------

## Traps

The trap mechanic has been restored; previously, anyone could disarm any trap with ease. Now, the trap spell cost will be factored into disarming difficulty, similar to how lock levels work.
```
fTrapCostMult                       0 -> -0.75          Trap spell cost taken into account
```

Common trap costs were previously too low, so they have been adjusted to present a greater challenge. These spells are roughly 50% of all traps in the game, and most of the others are under 20 points.
```
Fire Trap                           3 -> 30             2-20pts/3s
Frost Trap                          3 -> 35             2-20pts/3s
Shock Trap                          5 -> 40             2-20pts/3s
Lifeforce Trap                      8 -> 45             2-20pts/3s
Poison Trap                         16 -> 50            1-5pts/60s

Paralysis Trap                      13 -> 55            10s
Silence Trap                        37 -> 60            30s

Master Fire Trap                    3 -> 65             20-30pts/10s
Master Frost Trap                   3 -> 70             20-30pts/10s
Master Shock Trap                   5 -> 75             20-30pts/10s
Master Poison Trap                  16 -> 100           5-10pts/50s
```

$${\color{lime}\*1.8\*}$$ Changes:
* The fTrapCostMult setting has been changed from -1 to -0.75. Now it scales more like lockpicking.
* Trap costs have been revisited. It doesn't make sense to auto-calculate them; the values were too low anyway, and trap difficulty can be independent from spell power.

------------------------------------------------------------

## Magic - Potions

$${\color{orange}\*1.7\*}$$ With the new spell effect costs, potions that used to be very weak compared to their self-made versions have now been adjusted. I also want to keep this 1 to 3 magnitude-to-duration ratio, at least for the standard potions.

```
Bargain Potion of Burden            5pts/8s -> 50pts/80s                10x/10x (cost 0.1)
Cheap Potion of Burden              8pts/15s -> 80pts/150s
Standard Potion of Burden           10pts/30s -> 100pts/300s
Quality Potion of Burden            15pts/45s -> 150pts/450s
Exclusive Potion of Burden          20pts/60s -> 200pts/600s

Bargain Potion of Feather           5pts/8s -> 50pts/80s
Cheap Potion of Feather             8pts/15s -> 80pts/150s
Quality Potion of Feather           15pts/45s -> 150pts/450s
Exclusive Potion of Feather         20pts/60s -> 200pts/600s
```

```
Potion of Detect Creatures          10pts/15s -> 50pts/150s             5x/10x (cost 0.2)
Potion of Detect Key                10pts/15s -> 50pts/150s
Potion of Detect Enchantments       10pts/15s -> 50pts/150s
```

```
Bargain Potion of Light             5pts/8s -> 25/40s                   5x/5x (cost 0.2)
Cheap Potion of Light               8pts/15s -> 40pts/75s
Standard Potion of Light            10pts/30s -> 50pts/150s
Quality Potion of Light             15pts/45s -> 75pts/225s
Exclusive Potion of Light           20pts/60s -> 100pts/300s

Bargain Potion of Night-Eye         5pts/8s -> 25/40s
Cheap Potion of Night-Eye           8pts/15s -> 40pts/75s
Standard Potion of Night-Eye        10pts/30s -> 50pts/150s
Quality Potion of Night-Eye         15pts/45s -> 75pts/225s
Exclusive Potion of Night-Eye       20pts/60s -> 100pts/300s
```

Those potions are standard, so they should have a standard duration.
```
Potion of Slowfalling               10pts/15s -> 10pts/30s              1x/2x
Potion of Telekinesis               10pts/15s -> 10pts/30s
Potion of Water Breathing           15s -> 30s
Potion of Water Walking             15s -> 30s
```

Additionally, potion inconsistencies have been fixed.
```
Bargain Potion of Swift Swim        1pts/8s -> 5pts/8s
Spoiled Slowfall Potion             10pts/15s -> 1pts/15s
```

------------------------------------------------------------

## Magic - Potions - Tamriel Data

$${\color{lime}\*1.8\*}$$ Following potions from Tamriel Data has been updated.
```
Standard Potion of Feather          10pts/30s -> 100pts/300s            T_Com_Potion_Feather_S

Cheap Potion of Burden              8pts/15s -> 50pts/80s               T_Nor_Potion_Burden_C
Quality Potion of Burden            15pts/45s -> 150pts/450s            T_Nor_Potion_Burden_Q

Cheap Potion of Feather             8pts/15s -> 50pts/80s               T_Nor_Potion_Feather_C
Quality Potion of Feather           15pts/45s -> 150pts/450s            T_Nor_Potion_Feather_Q
```

```
Potion of Detect Key                10pts/15s -> 50pts/150s             T_Com_Potion_Detect_Invisib_S
Potion of Detect Creatures          10pts/15s -> 50pts/150s             T_Com_Potion_Detect_Humanoid_S
Potion of Detect Enchantments       10pts/15s -> 50pts/150s             T_Com_Potion_Detect_Enemy_S
```

```
Cheap Potion of Light               8pts/15s -> 40pts/75s               T_Nor_Potion_Light_C
Quality Potion of Light             15pts/45s -> 75pts/225s             T_Nor_Potion_Light_Q

Cheap Potion of Night-Eye           8pts/15s -> 40pts/75s               T_Nor_Potion_NightEye_C
Quality Potion of Night-Eye         15pts/45s -> 75pts/225s             T_Nor_Potion_NightEye_Q
```

```
Spoiled Slowfall Potion             10pts/15s -> 1pts/15s               T_Nor_Potion_DrainEndurance_Q
```

------------------------------------------------------------

## Magic - Spells

$${\color{orange}\*1.7\*}$$ Spells have been tweaked to stay useful following the changes to spell effect costs.

### Alteration

```
Burden Touch                        20/10s/Touch -> 100/20s             5x/2x
Burden                              20/10s/Target -> 100/20s

Heavy Burden Touch                  40/10s/Touch -> 200/20s
Heavy Burden                        40/10s/Target -> 200/20s

Crushing Burden Touch               60/10s/Touch -> 300/20s
Crushing Burden                     60/10s/Target -> 300/20s

Weary                               30-60/10s/Target -> 150-300/20s     5x/2x
Cruel Weary                         50-70/10s/Target -> 250-350/20s
Dire Weary                          60-90/10s/Target -> 300-450/20s

*Burden of Sin                      40/10s/Target -> 400/10s            10x/1x
*Great Burden of Sin                40-60/20s/Touch -> 400-600/20s
Crushing Burden of Sin              60-80/30s/Target -> 600-800/30s

* swapped names
```

```
Feather                             20/10s/Self -> 100/20s              5x/2x
Strong Feather                      50/10s/Self -> 250/20s              5x/2x
Great Feather                       100/10s/Self -> 500/20s             5x/2x

Ulms' Juicedaw Feather              50/10s/Self -> 500/10s              10x/1x
```

### Destruction

```
Armor Eater                         10-30/Touch -> 10-30/6s             1x/6x
Weapon Eater                        6-25/Touch -> 6-25/6s

*Disintegrate Armor                 6-25/Target -> 6-25/6s              1x/6x
*Disintegrate Weapon                6-25/Target -> 6-25/6s

* used by hungers, unavailable in vanilla
```

------------------------------------------------------------

## Magic - Spells - Tamriel Data

$${\color{green}\*1.9\*}$$ Following spells from Tamriel Data has been updated.

### Alteration

```
Shadow Rust
	Burden              			1-15/20s -> 10-150/20s              10x/1x
    Disintegrate Armor  			1-5/20s -> 6-30/20s                 6x/1x
Weight of Guilt                     500/3s -> 500/30s                   1x/10x
Fling                               500/3s -> 500/30s                   1x/10x
To the ja-Kha'jay                   50/20s -> 50/60s                    1x/3x
Fuchon Cire's Gentle Descent        10/20s -> 10/60s                    1x/3x
Dreugh's Grace                      30/20s -> 30/80s                    1x/4x

Dalgor's Entwining                  [8 -> 96]
Falling First Barrier               [42 -> 21]
Tsun's Ward                         [40 -> 20]
```

### Destruction

```
Fracture Armor                      100/2s -> 100/20s                   1x/10x
Iron Eater                          1-25/2s -> 1-25/12s                 1x/6x
Steel Eater                         5-30/3s -> 5-30/18s                 1x/6x

Duck                                [40 -> 10]
```

### Illusion

```
Voices                              50/20s -> 50/60s                    1x/3x
```

------------------------------------------------------------

## Magic - Enchantments

$${\color{green}\*1.9\*}$$ Following enchantments has been updated.

```
shadowstrike_en
	Chameleon						200-100 -> 100
slave_bracer_en                     Drain Magicka -> Damage Magicka
```

------------------------------------------------------------

## Appendix A

#### _How to create an exclusive potion - 20pts/60s (with a magic effect base cost of 1)_

- _You need Alchemy, Intelligence, and Luck at 100 and mortar with a quality of 1. Previously this was possible with Alchemy at 40._

#### _How to enchant a high-level spell - 100pts/24s (with a magic effect base cost of 1)_

- _Enchanter - 17000gp with Mercantile at 100 and Disposition at 100. Mercantile, Intelligence, and Luck are taken into account but capped at 100._
- _Self-enchant - 53% chance of making an item with Enchant at 100 and average (50) attributes._

#### _How to open a 100-point lock_

- _Thief - Security starting from level 60; 6% with pick quality 1.4 and average (50) attributes._
- _Mage - Alteration starting from level 60; spell costs 120 with an 8% chance on average (50) attributes._
- _Warrior - Enchanting service; 27000gp with Mercantile 50 and Disposition 100._

#### _How to untrap a 100-point spell_

- _Thief - Security starting from level 65; 8% with probe quality 1.25 and average (50) attributes._
- _Mage - Telekinesis._
- _Warrior - Take it on the chin._

# Remastered Rebalance Redux

#### Intentions

Despite the name, my intention here is not to balance the game. That's impossible. Nor is it to make it harder or easier. The idea is to make more options usable, especially for the fun of role-playing more specialized characters. This mod includes changes to spell effects, lockpicking, traps, alchemy, enchanting, and many more!

------------------------------------------------------------

#### Philosophy

- Simplicity - I prefer to change as little as possible to achieve the goal. It's easier to maintain and more compatible.
- Modularity - Everything is divided into separate modules, so you can mix and match with other mods.
- Purist friendly - I'm trying to avoid arbitrary decisions. Most changes are multipliers or additions to existing values.
- Math-driven - Seriously, I'm doing real calculations here.

------------------------------------------------------------

#### Assumptions

- Patch for Purists is applied.
- Tamriel Rebuilt is used, but not required.
- OpenMW is preferred (vanilla may have different calculations, and MCP can fix some issues).
- "Use Magic Item Animation" setting is on in OpenMW (or equivalent in MCP).

If you are using MCP, leave vanilla mechanics for creating spells:
- Maximum spell magnitude is set to 100 for 1440 seconds. Creating spells with a magnitude over 100 is generally overpowered.
- Self-made spells have one additional second added when calculating cost. A 100/1s spell is much more powerful than a 1/100s spell at the same cost. In vanilla, a 100/1s spell costs twice as much.
- Only one spell effect per spell is allowed.

Ideally, a mod that allows a higher magnitude cap for certain effects like Feather is needed. Some spells shouldn't be allowed to have a 1-second duration, such as Charm. Summon spells should allow summoning multiple skeletons in one spell. Until such mods exist, balancing the spell system is impossible when these "cheats" are enabled.

------------------------------------------------------------

#### Recommendations

- Using some form of real-time dialogue mod with NPCs is recommended, primarily to prevent persuasion exploits.
- I also recommend my other mod: https://www.nexusmods.com/morrowind/mods/55507, which sets the skills and attribute caps, limit potion consumption, and training sessions per level. All changes below are made with those limits in mind.

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

- If you are using **Morag Tong Polished**, make sure to also enable **Corrupted Crime - Morag Tong Polished.esp** at the end of your load order.

------------------------------------------------------------

#### History

- 1.10
  - Races: Module added
  - Birthsigns: Module added
  - Skills: Security reverted back to Intelligence
  - Alchemy TR: Module added
  - Magic:
    - Minor PfP fixes forwarded
    - Jump reverted from 1 to 3
    - Slowfall reverted from 1 to 3
    - Chameleon changed from 1 to 2
    - Sanctuary changed from 1 to 2
    - Charm changed from 5 to 2
    - Drain Magicka changed from 0.8 -> 0.5
    - Drain Fatigue changed from 0.5 -> 0.25
    - Absorb Health changed from 8 -> 10
    - Absorb Magicka changed from 8 -> 10
    - Restore Health changed from 5 -> 4
    - Restore Magicka changed from 5 -> 4
    - Restore Fatigue changed from 1 -> 2
    - Restore Attribute changed from 1 -> 8
    - Restore Skill changed from 1 -> 8
    - Fortify Magicka changed from 1 -> 0.5
    - Fortify Fatigue changed from 0.5 -> 0.25
    - Fortify Attack changed from 1 -> 4
  - Spells TD: Adjusted to changes in magic
- 1.9
  - Barter: Mages Guild's travel cost changed from 10x to 5x
  - Barter: Merchant creatures' gold decreased 10x
  - Magic: All elemental damage effects cost set to 6
  - Spells TD: Module added
  - Enchantments: Module added
- 1.8
  - Magic: Open and Lock spell effects added
  - Magic: Drain Magicka changed from 0.75 to 0.8 (now it's exactly 5x cheaper)
  - Magic: Sound changed from 0.8 to 1 (now it's exactly 3x cheaper)
  - Magic: Fortify Magicka changed from 0.75 to 0.8 (to be on par with Drain Magicka)
  - Lockpicking: Lock changed from 60 to 24
  - Traps: fTrapCostMult changed from -1 to -0.75 (now it scales more like lockpicking)
  - Traps: Trap costs have been revisited (it doesn't make sense to auto-calculate them; the values were too low anyway, and trap difficulty can be independent from spell power)
  - Potions TD: Module added
- 1.7
  - Potions and Spells: Modules in progress...
  - Lockpicking: Lock spell effect 30x more expensive
- 1.6
  - Traps: Costs readjusted
  - Crime: Bounties have been reduced from the previous version (they are now only 5 times higher than vanilla values)
  - Potions: Module added
  - Spells: Module added
- 1.5
  - Magic: Module remastered
- 1.4
  - Magic: Module revisited
- 1.3
  - Magic: Resist Paralysis spell effect 10x more expensive
  - Crime: Module added
- 1.2
  - Lockpicking and Traps: Split into separate esps
  - Alchemy: Adjusted
  - Barter: Mages Guild's travel 10x more expensive
- 1.1
  - Magic: Elemental damage effects costs increased
  - Magic: Detect spells effects 5x cheaper
  - Alchemy: Secret Master's apparatuses 5x more expensive

------------------------------------------------------------

## Skills

Armorer skill is better suited in Endurance, as this attribute lacks any non-combat skill.
```
Armorer                             Strength -> Endurance
```

And this is how skills table looks now.
```
Strength        5 -> 4              Acrobatics, Axe, Blunt, Long Blade
Intelligence    4                   Alchemy, Conjuration, Enchant, Security
Willpower       4                   Alteration, Destruction, Mysticism, Restoration
Agility         4                   Block, Light Armor, Marksman, Sneak
Speed           4                   Athletics, Hand-to-Hand, Short Blade, Unarmored
Endurance       3 -> 4              Heavy Armor, Medium Armor, Spear, ~~Armorer~~
Personality     3                   Illusion, Mercantile, Speechcraft
```

------------------------------------------------------------

## Skills - Races

Here is my attempt to improve racial abilities. I'm trying to stay as close as possible to the original concept but also balance and take into account changes I made in magical effects. The only exceptions are beast races that are improved significantly (they have 5 abilities now compared to 2-3 for other races).

### Argonian

When I think about Argonians, spears are my first choice, and also weapon skill is just more important early game than athletics.
```
Skill Bonuses
    Athletics                       +15 -> +5
    Alchemy                         +5
    Illusion                        +5
    Medium Armor                    +5
    Mysticism                       +5
    Spear                           +5 -> +15
    Unarmored                       +5
```

I added a new, very rare Resist Normal Weapons ability because Argonians can have some kind of natural armor made from scales. Water breathing and swimming are just their natural abilities now (there is one quest related to this, but it can be worked around). They also acquired a small bonus to Magicka, as we can read in the description: *"The female life-phase is highly intelligent, and gifted in the magical arts"*.
```
Abilities
    Immune to Poison
        Resist Poison               100%
    Resist Disease
        Resist Common Disease       75%
    [NEW] Scales
        Resist Normal Weapons       25%
    [NEW] Amphibious
        Water Breathing
        Swift Swim                  50
    [NEW] Magicka Bonus
        Magicka Bonus               0.2xINT

Spells
    [REMOVED] Water Breathing
        Water Breathing             120s/Self
```

### Breton

No changes here.
```
Abilities
    Resist Magicka
        Resist Magicka              50%
    Magicka Bonus
        Fortify Maximum Magicka     0.5×INT

Powers
    Dragon Skin
        Shield                      50/60s/Self
```

### Dark Elf -> Dunmer

No changes here.
```
Abilities
    Resist Fire
        Resist Fire                 75%

Powers
    Ancestor Guardian
        Sanctuary                   50/60s/Self
```

### High Elf -> Altmer

Weakness to Fire is slightly decreased, as there are too many weaknesses already.
```
Abilities
    Resist Disease
        Resist Common Disease       75%
    Weakness to Shock
        Weakness to Shock           25%
    Weakness to Frost
        Weakness to Frost           25%
    Weakness to Fire
        Weakness to Fire            50% -> 25%
    Weakness to Magicka
        Weakness to Magicka         50%
    Magicka Bonus
        Fortify Maximum Magicka     1.5×INT
```

### Imperial

Warning: Changes made here are done with the assumption that you are using the real-time dialogue mod when longer Charm effects are necessary.

Imperial is a real star here. I imagine he can charm everyone in a room for a good period of time. And also be tireless doing so. You're not losing fatigue while running at 0 Encumbrance and 75 Endurance (previously 125 Endurance).
```
Abilities
    [NEW] Star of the West
        Restore Fatigue             1
Powers
    [REMOVED] Star of the West
        Absorb Fatigue              200/Target
    Voice of the Emperor
        Charm                       25-50/15s/Target -> 25/120s/25ft/Target
```

### Khajiit

Description says: "_Many Khajiit disdain weapons in favor of their natural claws._" and acrobatics is already improved as a constant ability.
```
Skill Bonuses
    Acrobatics                      +15 -> +5
    Athletics                       +5
    Hand-to-hand                    +5 -> +15
    Light Armor                     +5
    Security                        +5
    Short Blade                     +5
    Sneak                           +5
```

Khajiits now acquired a small Resist Frost ability because they have fur. Eye of Night is permanent (it looks good on OpenMW). The new Feline Grace spell allows them to jump higher, and also they are immune to fall damage. The last ability is Fortify Luck as it just perfectly fits there.
```
Abilities
    [NEW] Resist Frost
        Resist Frost                25
    [NEW] Feline Grace
        Jump                        5
        Slowfall                    1
    [NEW] Eye of Night
        Night Eye                   25
    [NEW] Nine Lives
        Fortify Luck                10

Powers
    Eye of Fear
        Demoralize Humanoid         100/30s/Target

Spells
    [REMOVED] Eye of Night
        Night Eye                   50/30s/Self -> 50/120s/Self
```

### Nord

Warning: Changes made here are done with the assumption that you are using setting tweak to how elemental shield effects work.

Nords have the best resistances compared to other races, even after debuffs. Thunder Fist is almost useless, as this is just a low-level spell. Woad does the same as Breton power but worse. To fix that I decided to replace them with elemental shields that in combination with natural resistances give them the same levels as before, but with additional 50 pts of passive damage to all melee attackers. Nord can be paralyzed now and still do the damage.
```
Abilities
    Resist Shock
        Resist Shock                50% -> 25%
    Immune to Frost -> Resist Frost
        Resist Frost                100% -> 75%

Powers
    [REMOVED] Thunder Fist
        Frost Damage                25/Touch
    [REMOVED] Woad
        Shield                      30/60s/Self
    [NEW] Blizzard Barrier
        Lightning Shield            25/30s/Self
        Frost Shield                25/30s/Self
```

### Orc -> Orsimer

There is a lot to say about Berserk. Fortify Health is meaningless in the mid-game when characters have decent stats already. Boost to Fatigue can affect a lot of other things you can do in the game, like picking a lock, enchanting, persuasion, etc. Fortify Attack makes any combat trivial if you know how to workaround Drain Agility, because every hit will cause you to fall.

This power is simply too overpowered and allows you to beat any boss at level 1. I just nerfed it a little, but it's still doable.
```
Abilities
    Resist Magicka
        Resist Magicka              25%

Powers
    Berserk
        [REMOVED] Fortify Health    20/60s/Self
        Fortify Fatigue             200/60s/Self
        Fortify Attack              100/60s/Self -> 50/60s/Self
        Drain Agility               100/60s/Self -> 200/60s/Self
```

### Redguard

No changes here. Adrenaline Rush is fine effect that can be compared to being after several local drinks.
```
Abilities
    Resist Poison
        Resist Poison               75%
    Resist Disease
        Resist Common Disease       75%

Powers
    Adrenaline Rush
        Fortify Agility             50/60s/Self
        Fortify Strength            50/60s/Self
        Fortify Speed               50/60s/Self
        Fortify Endurance           50/60s/Self
        Fortify Health              25/60s/Self
```

### Wood Elf -> Bosmer

Previously with Beast Tongue at level 5 best creatures available to command were Scamp or Dreugh; At level 15 those will be Winged Twilight or Storm Atronach.
```
Abilities
    Resist Disease
        Resist Common Disease       75%

Powers
    Beast Tongue
        Command Creature            5/600s/Target -> 15/600s/Target
```

Bosmer females were just too tall.
```
Female Height                       1 -> 0.92
```

------------------------------------------------------------

## Skills - Birthsigns

### Warrior

No changes here. It's useful entire game.
```
Abilities
    Warwyrd
        Fortify Attack              10
```

### Mage

There was little reason to take this instead of Apprentice.
```
Abilities
    Fay
        Fortify Maximum Magicka     0.5xINT -> 1.0xINT
```

### Thief

No changes here. It's useful entire game.
```
Abilities
    Akaviri Danger-sense
        Sanctuary                   10
```

### Serpent

Serpent was originally just awful spell. Now it's very powerful, but you need to workaround its negative effect.
```
Spells -> Powers
    Star-Curse
        Poison                      3/30s/Touch -> 3/300s/Touch
        Damage Health               1/30s/Self -> 1/300s/Self
```

### Lady

No changes here. Best if you want to maximize Health.
```
Abilities
    Lady's Favor
        Fortify Personality         25
    Lady's Grace
        Fortify Endurance           25
```

### Steed

Attribute boost is only useful early game. With this addition it will be handy entire time.
```
Abilities
    Charioteer
        Fortify Speed               25
        [NEW] Feather               100
```

### Lord

No one would ever pick this before for other reasons than role playing.
```
Spells -> Powers
    Blood of the North
        Restore Health              2/30s/Self -> 1/600s/Self

Abilities
    Trollkin
        Weakness to Fire            100% -> 25%
```

### Apprentice

No changes here.
```
Abilities
    Elfborn
        Fortify Maximum Magicka     1.5xINT
        Weakness to Magicka         50%
```

### Atronach

This was overpowered late game when every caster only exist to regenerate your Magicka.
```
Abilities
    Wombburn
        Spell Absorption            50 -> 25
        Fortify Maximum Magicka     2.0xINT
        Stunted Magicka
```

### Ritual

Mara's Gift was just boring spell previously, now it can be useful as a last resort even until late game. Blessed Word also is greatly improved.
```
Spells
    Blessed Word
        Turn Undead                 100/30s/Target -> 100/60s/50ft/Target
    [REMOVED] Blessed Touch
        Turn Undead                 100/30s/Touch

Powers
    Mara's Gift
        Restore Health              100/Self -> 200/Self
```

### Lover

No changes here. Very powerful power.
```
Abilities
    Mooncalf
        Fortify Agility             25

Powers
    Lover's Kiss
        Paralyze                    60s/Target
        Damage Fatigue              200/Self
```

### Shadow

Very low level spell upgraded to be useful entire game.
```
Powers
    Moonshadow
        [REMOVED] Invisibility      60s/Self
        [NEW] Chameleon             20/120s/Self
```

### Tower

Detect spells are so cheap now that Beggar's Nose deserves constant effect. Tower Key is improved for being useful much longer.
```
Spells -> Abilities
    Beggar's Nose
        Detect Animal               200/60s/Self -> 200
        Detect Enchantment          200/60s/Self -> 200
        Detect Key                  200/60s/Self -> 200

Powers
    Tower Key
        Open                        50/Touch -> 80/Touch
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

Those tables show how self made potion strength scales now, depending on different levels of A-Alchemy, Q-Mortar Quality, and BC-Spell Effect Base Cost.

```
fPotionStrengthMult: 0.5

5/8s    :
8/15s   :
10/30s  : [A:40,Q:1,BC:2]
15/45s  :
20/60s  : [A:40,Q:1,BC:1] or [A:100,Q:1,BC:2] or [A:40,Q:2,BC:2]
        :
40/120s : [A:100,Q:1,BC:1] or [A:100,Q:2,BC:2]
```

```
fPotionStrengthMult: 0.25

5/8s    : [A:40,Q:1,BC:2] <- actually this will be 5/15s
8/15s   :
10/30s  : [A:40,Q:1,BC:1] or [A:100,Q:1,BC:2] or [A:40,Q:2,BC:2]
15/45s  :
20/60s  : [A:100,Q:1,BC:1] or [A:100,Q:2,BC:2]
```

Some Secret Master's apparatuses were cheaper than Grandmaster's versions. They all are now five times more expensive.
```
apparatus_sm_mortar_01          Secret Master's Mortar & Pestle     6000 -> 30000
apparatus_sm_alembic_01         Secret Master's Alembic             1600 -> 8000
apparatus_sm_calcinator_01      Secret Master's Calcinator          3200 -> 16000
apparatus_sm_retort_01          Secret Master's Retort              1000 -> 5000
```

------------------------------------------------------------

## Alchemy - Tamriel Rebuilt

Tamriel Rebuilt apparatuses prices doesn't make sense also.
```
TR_m7_apparatus_sm_mortar_02    Secret Master's Mortar & Pestle     6000 -> 30000
TR_m7_apparatus_sm_alembic_02   Secret Master's Alembic             6000 -> 8000
TR_m7_apparatus_sm_calcin_02    Secret Master's Calcinator          6000 -> 16000
TR_m7_apparatus_sm_retort_02    Secret Master's Retort              2400 -> 5000
```

------------------------------------------------------------

## Enchant

This was one of the weakest skills in the game. Creating your own enchantments was nearly impossible, and you didn't even need to recharge enchanted items—they recharged automatically. To make things worse, the Secret Master would attack you on sight.

These changes aim to make self-enchanting a viable alternative to using an enchanter while requiring you to actively hunt for soul gems to keep your equipment charged. As a fighter or thief, you'll need to manage your resources more carefully, or just buy a replacement item when needed.
```
fMagicItemRechargePerSecond     0.05 -> 0                                   No idle recharging
fEnchantmentChanceMult          3 -> 0.6                                    5x easier self enchant

sMagicInsufficientCharge        "Item does not have enough charge." -> ""   No annoing messages
```

------------------------------------------------------------

## Magic

The point of reference here is Fortify Attribute spell effect which stay untouched. Every other effect is balanced around it.

* All spell examples here are self made high level spells that can cost around 120-130 Magicka.
* I you want to know how powerful they will be in constant enchantment, just switch magnitude with duration (constant duration is always 100s).
* Potion examples are provided for Alchemy, Intelligence, and Luck at 100, mortar quality at 1 and fPotionStrengthMult at 0.25.

------------------------------------------------------------

### Alteration

Elemental shields are now worth experimenting with. Especially for the fun of killing low-level creatures. Their cost hasn't changed, since they serve a dual purpose: providing elemental resistance and dealing damage to attackers.
```
fElementalShieldMult                0.1 -> 1            1 point of damage for 1 point of magnitude

Fire, Frost, Lightning Shield       3 -> Unchanged      100/7s or 8/100s (potion: 7/20s)
```

Previously, Feather wasn't very useful because its cost matched Fortify Strength, so it provided five times less encumbrance increase per point. Now it is 2x more cost efficient.
```
Feather [8]                         1 -> 0.1            100/240s (potion: 200/600s)
Burden [7]                          1 -> 0.1
```

The same logic applies to Swift Swim, which affects only swimming speed and should therefore outperform Fortify Speed.
```
Swift Swim [1]                      2 -> 0.5            100/48s (potion: 40/120s)
```

No changes here. Jump and Slowfall are generally harder to use than Levitate, but used together, they offer a more affordable alternative to travel long distances. 1 point of jump is equivalent to 6.6 points of Acrobatics.
```
Levitate                            3 -> Unchanged      100/7s (potion: 7/20s)
Jump                                3 -> Unchanged      100/7s (potion: 7/20s)
Slowfall                            3 -> Unchanged      1/800s (potion: 7/20s)

sEffectSlowFall                     SlowFall -> Slowfall
```

With this adjustment, Shield can be used as an good addition to Unarmored skill.
```
Shield [3]                          2 -> 1              100/24s (potion: 20/60s)
```

The cost of these spell effects has been changed to be on par with Lockpicking module.
```
Open [13]                           6 -> 12
Lock [12]                           2 -> 24
```

------------------------------------------------------------

### Destruction

Elemental damage felt unbalanced—there was little reason to use anything other than Fire or Frost. To address this, I adjusted all elemental damage types to the same level.
```
Fire Damage [14]                    5 -> 6              100/3s or 4/100s
Frost Damage [16]                   5 -> 6
Shock Damage [15]                   7 -> 6
Damage Health [23]                  8 -> 6
Poison [27]                         9 -> 6
```

Damage Magicka has been reduced to align with Damage Health.
```
Damage Magicka [24]                 8 -> 6              100/3s
```

Damage Fatigue remains unchanged, as it is either nearly useless or very powerful depending on the "Uncapped Damage Fatigue" setting.
```
Damage Fatigue                      4 -> Unchanged      100/5s
```

Damage Attribute was so powerful it outperformed almost every other "utility" spell. For just 40 Magicka, you could reduce the target's Strength or Intelligence to zero, leaving them unable to walk, fight, or cast spells. Now it is 3x more expensive.
```
Damage Attribute [22]               8 -> 24             1/100s or 50/1s
Damage Skill [26]                   8 -> 24
```

Low-tier gear typically has a durability of around 300–500. With these changes, it can now be destroyed by a 25-cost spell.
```
Disintegrate Armor [38]             6 -> 1              100/24s
Disintegrate Weapon [37]            6 -> 1
```

Drain spells have been lowered to match the cost of corresponding Fortify spells. This change reflects that the 100-magnitude cap makes them mostly ineffective at higher levels. Additionally, Drain Magicka was four times more expensive than Drain Intelligence; now it's 2x cheaper. As a side effect, many potions with these negative effects will become stronger. Drain Health is unchanged, because it can still kill low level creature cheaper than Damage Health spell.
```
Drain Health                        4 -> Unchanged      100/5s (potion: 5/15s)
Drain Magicka [19]                  4 -> 0.5
Drain Fatigue [20]                  2 -> 0.25
```

No changes here.
```
Drain Attribute                     1                   100/24s
```

Drain Skill is now more expensive due to its potential for being overpowered—similar to Fortify Skill. Compared to Drain Attribute, it has a much greater impact.
```
Drain Skill [21]                    1 -> 2              100/11s (potion: 10/30s)
```

------------------------------------------------------------

### Illusion

Previously, there was little reason to use these effects over Paralyze.
```
Paralyze                            40 -> Unchanged     60s
Silence [46]                        40 -> 20            120s
Sound [48]                          3 -> 1              100/24s
```

Additionally, a bugfix related to Illusion has been included.
```
Demoralize Humanoid [53]            Mysticism -> Illusion
```

Chameleon is powerful tool that increase your sneak skill, evasion, and making you invisible to opponents. It was too cheap before.
```
Chameleon [40]                      1 -> 2              100/11s (potion: 10/30s)
```

Sanctuary compared to Blind can be cast in advance and also as an constant enchantment. Thus should be more expensive.
```
Sanctuary [42]                      1 -> 2              100/11s (potion: 10/30s)
```

Charm was broken in original game, so I assume you are using real-time time dialogue mod, where duration matters.
```
Charm [44]                          5 -> 2              100/11s
```

------------------------------------------------------------

### Mysticism

Absorb spells were previously overpowered, costing the same as their damage-based counterparts. Since each Absorb spell effectively combines two effects—damage and restore—and also can be cast on area and on your own allys, it should come at a higher cost. Absorb Magicka and Absorb Skill, while not available in any vanilla craftable spells, have been adjusted for consistency.

```
Absorb Health [86]                  8 -> 10             50/4s or 1/240s
Absorb Magicka [87]                 8 -> 10
Absorb Fatigue [88]                 4 -> 6

Absorb Attribute                    2 -> Unchanged
Absorb Skill [89]                   2 -> 6
```

Detect spells were just too expensive.
```
Detect Animal [64]                  0.75 -> 0.15        100/160s (potion: 133/400s)
Detect Enchantment [65]             1 -> 0.2            100/120s (potion: 100/300s)
Detect Key [66]                     1 -> 0.2
```

Reflect and Spell Absorption are essentially stronger versions of resist effects. They were just too costly to be useful.
```
Reflect [68]                        10 -> 4             100/5s (potion: 5/15s)
Spell Absorption [67]               10 -> 4
```

------------------------------------------------------------

### Restoration

Those changes are done mostly to balance self made potions.
```
Restore Health [75]                 5 -> 4
Restore Magicka [76]                5 -> 4
Restore Fatigue [77]                1 -> 2
```

Those were ridiculously cheap before.
```
Restore Attribute [74]              1 -> 8
Restore Skill [78]                  1 -> 8
```

No changes here.
```
Fortify Health                      1 -> Unchanged
```

Fortify Magicka was doing less than Fortify Intelligence for the same price. Now it's 2x cheaper than Fortify Intelligence.
```
Fortify Magicka [81]                1 -> 0.5            100/30s (potion: 25/75s)
```

This should be cheaper than Fortify Magicka.
```
Fortify Fatigue [82]                0.5 -> 0.25
```

No changes here.
```
Fortify Attribute                   1 -> Unchanged
```

Fortifying skill over 50 should be available only for the highest-level characters.
```
Fortify Skill [83]                  1 -> 4              100/5s (potion: 5/15s)
```

Fortify Attack is doing same as Fortify Skill but it's more versatile.
```
Fortify Attack [117]                1 -> 4
```

This looks like a typo compared to other resistances.
```
Resist Paralysis [99]               0.2 -> 2            100/11s
```

------------------------------------------------------------

## Barter

The economy is broken because there is an unlimited supply of money in the game, so simply making everything more expensive won't fix the problem. The real issue is a player mindset focused on quickly replacing all items with gold. You don't need to do that. Instead, pick only valuable items and sell them when you truly need cash. Typically, the only times you'll really need cash are to purchase enchanted items or pay for training. There should already be enough money in the market to cover those needs for about a month.

Additionally, this encourages investing in Speechcraft and Mercantile to secure better prices. A beneficial side effect is having more time to recover money spent on enchantments or training, especially if the merchant also buys your items.
```
fBarterGoldResetDelay               24 -> 720           30 days to reset merchants' gold
```

The Mages Guild's teleportation price has been increased. As a fast, modern form of travel, it shouldn't be cheaper than traditional methods.
```
fMagesGuildTravel                   10 -> 50            5x more expensive
```

Merchant creatures gold has been reduced.
```
Creeper                             5000gp -> 500gp
Mudcrab                             10000gp -> 1000gp
```

------------------------------------------------------------

## Crime

You might prefer loading a previous save rather than facing the consequences. But if you don't, you'll quickly see that bounties were previously unrealistically low. That's why crime penalties have been increased significantly.
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

The death warrant will be triggered after a combination of one killing, one attack, and any other crime. This means you must be perfectly clean while doing MT's Writs.
```
Death Warrant                       5000 -> 5201        You can kill only one person, instead of 4
```

------------------------------------------------------------

## Pickpocket

Pickpocketing is essentially a stat-based contest between you and the NPC. However, in vanilla, your maximum success chance was capped at just 56%, no matter your stats, because the cap was set to 75% and the check happens twice—once when picking the item and again when closing the pickpocket window.
```
iPickMaxChance                      75 -> 95            ~10% chance of being caught anyway
```

It also didn't make much sense to factor in the item's value when determining success, so I removed that requirement.
```
fPickPocketMod                      0.3 -> 0            Any item available to steal
```

------------------------------------------------------------

## Lockpicking

The primary goal is to make the Security skill more valuable at higher levels and to ensure it's more effective than Alteration for lock-related tasks. Previously, raising Security above 50 provided no real benefit.
```
fPickLockMult                       -1 -> -1.25         Locks harder to unlock
```

The second goal is to ensure that unlocking 100-point locks is only achievable by higher-level characters. Previously, cheap Alteration spells and scrolls made magic a better option for unlocking doors at any level.
```
Open                                6 -> 12             100pts spell will cost you 120 Magicka
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

------------------------------------------------------------

## Traps

The trap mechanic has been restored; previously, anyone could disarm any trap with ease. Now, the trap spell cost will be factored into disarming difficulty, similar to how lock levels work.
```
fTrapCostMult                       0 -> -0.75          Trap spell cost taken into account
```

Common trap costs were previously too low, so they have been adjusted to present a greater challenge. These spells are roughly 50% of all traps in the game, and most of the others are under 20 points.
```
Fire Trap                           3 -> 30             2-20/3s
Frost Trap                          3 -> 35             2-20/3s
Shock Trap                          5 -> 40             2-20/3s
Lifeforce Trap                      8 -> 45             2-20/3s
Poison Trap                         16 -> 50            1-5/60s

Paralysis Trap                      13 -> 55            10s
Silence Trap                        37 -> 60            30s

Master Fire Trap                    3 -> 65             20-30/10s
Master Frost Trap                   3 -> 70             20-30/10s
Master Shock Trap                   5 -> 75             20-30/10s
Master Poison Trap                  16 -> 100           5-10/50s
```

------------------------------------------------------------

## Magic - Potions

With the new spell effect costs, potions that used to be very weak compared to their self-made versions have now been adjusted. I also want to keep this 1 to 3 magnitude-to-duration ratio, at least for the standard potions.
```
Bargain Potion of Burden            5/8s -> 50/80s                      10x/10x
Cheap Potion of Burden              8/15s -> 80/150s
Standard Potion of Burden           10/30s -> 100/300s
Quality Potion of Burden            15/45s -> 150/450s
Exclusive Potion of Burden          20/60s -> 200/600s

Bargain Potion of Feather           5/8s -> 50/80s
Cheap Potion of Feather             8/15s -> 80/150s
Quality Potion of Feather           15/45s -> 150/450s
Exclusive Potion of Feather         20/60s -> 200/600s
```

```
Potion of Detect Creatures          10/15s -> 50/150s                   5x/10x
Potion of Detect Key                10/15s -> 50/150s
Potion of Detect Enchantments       10/15s -> 50/150s
```

```
Bargain Potion of Light             5/8s -> 25/40s                      5x/5x
Cheap Potion of Light               8/15s -> 40/75s
Standard Potion of Light            10/30s -> 50/150s
Quality Potion of Light             15/45s -> 75/225s
Exclusive Potion of Light           20/60s -> 100/300s

Bargain Potion of Night-Eye         5/8s -> 25/40s
Cheap Potion of Night-Eye           8/15s -> 40/75s
Standard Potion of Night-Eye        10/30s -> 50/150s
Quality Potion of Night-Eye         15/45s -> 75/225s
Exclusive Potion of Night-Eye       20/60s -> 100/300s
```

Those potions are standard, so they should have a standard duration.
```
Potion of Slowfalling               10/15s -> 10/30s                    1x/2x
Potion of Telekinesis               10/15s -> 10/30s
Potion of Water Breathing           15s -> 30s
Potion of Water Walking             15s -> 30s
```

Additionally, potion inconsistencies have been fixed.
```
Bargain Potion of Swift Swim        1/8s -> 5/8s
Spoiled Slowfall Potion             10/15s -> 1/15s
```

------------------------------------------------------------

## Magic - Potions - Tamriel Data

Following potions from Tamriel Data has been updated.
```
Standard Potion of Feather          10/30s -> 100/300s

Cheap Potion of Burden              8/15s -> 50/80s
Quality Potion of Burden            15/45s -> 150/450s

Cheap Potion of Feather             8/15s -> 50/80s
Quality Potion of Feather           15/45s -> 150/450s
```

```
Potion of Detect Key                10/15s -> 50/150s
Potion of Detect Creatures          10/15s -> 50/150s
Potion of Detect Enchantments       10/15s -> 50/150s
```

```
Cheap Potion of Light               8/15s -> 40/75s
Quality Potion of Light             15/45s -> 75/225s

Cheap Potion of Night-Eye           8/15s -> 40/75s
Quality Potion of Night-Eye         15/45s -> 75/225s
```

```
Spoiled Slowfall Potion             10/15s -> 1/15s
```

------------------------------------------------------------

## Magic - Spells (In Progress)

Spells have been tweaked to stay useful following the changes to spell effect costs.

### Alteration

#### Burden
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

#### Feather
```
Feather                             20/10s/Self -> 100/20s              5x/2x
Strong Feather                      50/10s/Self -> 250/20s              5x/2x
Great Feather                       100/10s/Self -> 500/20s             5x/2x

Ulms' Juicedaw Feather              50/10s/Self -> 500/10s              10x/1x
```

### Destruction

#### Disintegrate
```
Armor Eater                         10-30/Touch -> 10-30/6s             1x/6x
Weapon Eater                        6-25/Touch -> 6-25/6s

*Disintegrate Armor                 6-25/Target -> 6-25/6s              1x/6x
*Disintegrate Weapon                6-25/Target -> 6-25/6s

* used by hungers, unavailable in vanilla
```

------------------------------------------------------------

## Magic - Spells - Tamriel Data (In Progress)

Following spells from Tamriel Data has been updated.

### Alteration
```
Shadow Rust
    Burden                          1-15/20s -> 10-150/20s              10x/1x
    Disintegrate Armor              1-5/20s -> 6-30/20s                 6x/1x
Weight of Guilt
    Burden                          500/3s -> 500/30s                   1x/10x
Fling
    Feather                         500/3s -> 500/30s                   1x/10x
Dreugh's Grace                      
    Swift Swim						30/20s -> 30/80s                    1x/4x
Dalgor's Entwining
    Lock                            [8] -> [96]
Falling First Barrier
    Shield                          [42] -> [21]
Force Wall
    Shield                          50/5s -> 50/10s
Tsun's Ward
    Shield                          [40] -> [20]
```

### Destruction
```
Fracture Armor                      
    Disintegrate Armor				100/2s -> 100/12s                   1x/6x
Iron Eater                          
    Disintegrate Weapon				1-25/2s -> 1-25/12s                 1x/6x
Steel Eater                         
    Disintegrate Weapon				5-30/3s -> 5-30/18s                 1x/6x

Duck                                
    Drain Fatigue					[40] -> [10]
```

### Illusion
```
Voices                              
	Sound							50/20s -> 50/60s                    1x/3x
```

------------------------------------------------------------

## Magic - Enchantments (In Progress)

Following enchantments has been updated.
```
Shadowsting
    Chameleon                       200-100/20s/Target -> 100/20s/Target
    Poison                          5/20s/Target
Slave's Left/Right Bracer
    Drain Magicka -> Damage Magicka
```

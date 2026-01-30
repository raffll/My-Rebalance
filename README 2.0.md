# Remastered Rebalance Redux

#### Intentions

The idea is to make more options interesting to use, especially for the fun of role-playing more specialized characters. This mod includes changes to spell effects, lockpicking, traps, alchemy, enchanting, and many more!

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
- The "Use Magic Item Animation" setting is on in OpenMW (or equivalent in MCP).

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
- 1.11
  - Magic: Generally I wasn't happy with the changes that I made here. So it was completely refined.
  - Birthsigns: Shadow converted to Ability -> Chameleon 20
- 1.10
  - Races: Module added
  - Birthsigns: Module added
  - Skills: Security reverted back to Intelligence
  - Alchemy TR: Module added
  - Magic:
    - Minor PfP fixes forwarded
    - Jump reverted to 3
    - Slowfall reverted to 3
    - Chameleon changed to 2
    - Sanctuary changed to 2
    - Charm changed to 2
    - Drain Magicka changed to 0.5
    - Drain Fatigue changed to 0.25
    - Absorb Health changed to 10
    - Absorb Magicka changed to 10
    - Restore Health changed to 4
    - Restore Magicka changed to 4
    - Restore Fatigue changed to 2
    - Restore Attribute changed to 8
    - Restore Skill changed to 8
    - Fortify Magicka changed to 0.5
    - Fortify Fatigue changed to 0.25
    - Fortify Attack changed to 4
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

```
Armorer                             Strength -> Endurance
```

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

### Argonian

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

```
Abilities
    Resist Fire
        Resist Fire                 75%

Powers
    Ancestor Guardian
        Sanctuary                   50/60s/Self
```

### High Elf -> Altmer

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

```
Abilities
    Resist Disease
        Resist Common Disease       75%

Powers
    Beast Tongue
        Command Creature            5/600s/Target -> 15/600s/Target
```

```
Female Height                       1 -> 0.92
```

------------------------------------------------------------

## Skills - Birthsigns

### Warrior

```
Abilities
    Warwyrd
        Fortify Attack              10
```

### Mage

```
Abilities
    Fay
        Fortify Maximum Magicka     0.5xINT -> 1.0xINT
```

### Thief

```
Abilities
    Akaviri Danger-sense
        Sanctuary                   10
```

### Serpent

```
Spells -> Powers
    Star-Curse
        Poison                      3/30s/Touch -> 3/300s/Touch
        Damage Health               1/30s/Self -> 1/300s/Self
```

### Lady

```
Abilities
    Lady's Favor
        Fortify Personality         25
    Lady's Grace
        Fortify Endurance           25
```

### Steed

```
Abilities
    Charioteer
        Fortify Speed               25
        [NEW] Feather               100
```

### Lord

```
Spells -> Powers
    Blood of the North
        Restore Health              2/30s/Self -> 1/600s/Self

Abilities
    Trollkin
        Weakness to Fire            100% -> 25%
```

### Apprentice

```
Abilities
    Elfborn
        Fortify Maximum Magicka     1.5xINT
        Weakness to Magicka         50%
```

### Atronach

```
Abilities
    Wombburn
        Spell Absorption            50 -> 25
        Fortify Maximum Magicka     2.0xINT
        Stunted Magicka
```

### Ritual

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

```
Powers -> Abilities
    Moonshadow
        [REMOVED] Invisibility      60s/Self
        [NEW] Chameleon             20
```

### Tower

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

```
fMinWalkSpeed                       100 -> 125			25% speed boost to the player, NPCs, and creatures
fMaxWalkSpeed                       200 -> 250
fMinWalkSpeedCreature               5 -> 6.25
fMaxWalkSpeedCreature               300 -> 375
```

------------------------------------------------------------

## Barter

```
fBarterGoldResetDelay               24 -> 720           30 days to reset merchants' gold
```

```
fMagesGuildTravel                   10 -> 50            5x more expensive
```

```
Creeper                             5000gp -> 500gp
Mudcrab                             10000gp -> 1000gp
```

------------------------------------------------------------

## Crime

```
iCrimeKilling                       1000 -> 5000
iCrimeAttack                        40 -> 200
iCrimePickPocket                    25 -> 100
iCrimeTresspass                     5 -> 25

iDaysinPrisonMod                    100 -> 500          Days in prison same as in vanilla
```

```
iCrimeThreshold                     1000 -> 200
```

```
Death Warrant                       5000 -> 5201        You can kill only one person, instead of 4
```

------------------------------------------------------------

## Pickpocket

```
iPickMaxChance                      75 -> 95            ~10% chance of being caught anyway
```

```
fPickPocketMod                      0.3 -> 0            Any item available to steal
```

------------------------------------------------------------

## Lockpicking

```
fPickLockMult                       -1 -> -1.25         Locks harder to unlock
```

```
Open                                6 -> 12             100pts spell will cost you 120 Magicka
Lock                                2 -> 24
```

```
Open                                         20pts      Unchanged, unavailable in vanilla
Ondusi's Open Door                  50pts -> 40pts
Strong Open                         50pts -> 60pts
Great Open                          50pts -> 80pts      Unavailable in vanilla
Wild Open                                    1-100pts   Unchanged
```

```
Scroll of Ondusi's Unhinging        73gp -> 273gp       Available in stores
Scroll of Ekash's Lock Splitter     100pts -> 80pts     Available in random loot later in the game
```

------------------------------------------------------------

## Traps

```
fTrapCostMult                       0 -> -0.75          Trap spell cost taken into account
```

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

## Alchemy

```
fPotionStrengthMult                 0.5 -> 0.25         2x smaller magnitude, duration and price
```

```
apparatus_sm_mortar_01          Secret Master's Mortar & Pestle     6000 -> 30000
apparatus_sm_alembic_01         Secret Master's Alembic             1600 -> 8000
apparatus_sm_calcinator_01      Secret Master's Calcinator          3200 -> 16000
apparatus_sm_retort_01          Secret Master's Retort              1000 -> 5000
```

------------------------------------------------------------

## Alchemy - Tamriel Rebuilt

```
TR_m7_apparatus_sm_mortar_02    Secret Master's Mortar & Pestle     6000 -> 30000
TR_m7_apparatus_sm_alembic_02   Secret Master's Alembic             6000 -> 8000
TR_m7_apparatus_sm_calcin_02    Secret Master's Calcinator          6000 -> 16000
TR_m7_apparatus_sm_retort_02    Secret Master's Retort              2400 -> 5000
```

------------------------------------------------------------

## Enchant

```
fMagicItemRechargePerSecond     0.05 -> 0                                   No idle recharging
fEnchantmentChanceMult          3 -> 0.6                                    5x easier self enchant

sMagicInsufficientCharge        "Item does not have enough charge." -> ""   No annoing messages
```

------------------------------------------------------------

## Magic

```
sEffectSlowFall                     SlowFall -> Slowfall
Demoralize Humanoid                 Mysticism -> Illusion
```

------------------------------------------------------------

## Magic - Burden & Feather

------------------------------------------------------------

## Magic - Enchantments

```
Shadowsting
    Chameleon                       200-100/20s/Target -> 100/20s/Target
    Poison                          5/20s/Target
Slave's Left/Right Bracer
    Drain Magicka -> Damage Magicka
```

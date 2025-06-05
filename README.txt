## Inspirations

## Intentions
My intention here is not to balance the game. It's impossible. Neither make it harder or easier. Reason behind this is to make more options useful, for fun of role-playing more specialized characters.

## Assumptions
- Skill cap is set to 150 and attribute cap is set to 300 like in my other mod: https://www.nexusmods.com/morrowind/mods/55507. It's not requirement, but reasonable limit.
- OpenMW is used (Vanilla may have different calculations and MCP can fix some issues).
- Tamriel Rebuilt is used, but not required.

----------------------------------------------------------

## Skills

Armorer							Strength -> Endurance
Security						Intelligence -> Agility

----------------------------------------------------------

## Speed -- Just 25% speed boost for PC, NPCs and creatures.

fMinWalkSpeed					100 -> 125
fMaxWalkSpeed					200 -> 250
fMinWalkSpeedCreature			  5 -> 6.25
fMaxWalkSpeedCreature			300 -> 375

----------------------------------------------------------

## Alchemy -- This is the best skill in the game. It's impossible to compare it with buyable potions because they are using completely different formula. Pre-made potions are made from templates, like in factory. However self-made potions all have same magnitude and duration at same spell effect base cost. Those mechanics are not quite suitable for some spell effects. But the main problem is that you can succesfuly create excelent restore fatigue potions (200pts) with Alchemy at 5, making other choices garbage on the same level (e.g. restore fatigue equivalent will cost you 15 mana with 9% chance at Restoration level 5). So after applying this patch, some potions will be much weaker (but others still not so much) than pre-made counterparts and spells. But overall, you can get good results with decent stats and equipment on average levels and buyable potions will be useful much longer.

fPotionStrengthMult				0.5 -> 0.1			5x smaller magnitude, duration and price.

----------------------------------------------------------

## Enchant -- This is the worst skill in the game. Self made enchantments are almost impossible to do. You don't need to recharge items, because they are rechanging by themselves. And secret master will attack you on sight. Those changes are trying to make self-enchanting as good as an enchanter service, but forcing you to go and hunt for soulgems to keep your equipment useful. As a fighter you have to do better resource management or just buy same item again.

sMagicInsufficientCharge							Removed annoing message.
fMagicItemRechargePerSecond		0.05 -> 0			Disabled idle recharging. This change alone make Enchant skill useful.
fEnchantmentChanceMult			3 -> 0.6			5x easier self enchant.

# How to enchant 100pts/24s spell (with magic effect base cost of 1):
- Enchanter -- 17000gp with Mercatile 100 and Disposition 100. Mercantile, Intelligence and Luck are taken into account but capped at 100.
- Self-Enchant -- 53% chance of making item with Enchant 100 and average (50) attributes.

----------------------------------------------------------

## Economy -- Economy is broken because there is unlimited supply of money in the game,	so doing everything more expensive won't fix the problem. Real problem is a player mindset that want to just replace all garbage with money as quickly as possible. You don't need to do that. Pick only valuable items and sell them when you really need cash. And only scenarios when you need cash, is to buy enchanted item or to train with trainer. There is already enought money on the market too suit those needs for one month. Additionally, it will force you to invest in Speechcraft and Mercantile to get better prices.

fBarterGoldResetDelay			24 -> 720 			Less gold on the market should fix economy.

----------------------------------------------------------

## Pickpocket -- It's a stat game between you and NPC, but in vanilla your max chance was only 56% regardles of stats, because cap was set to 75% and check is done twice, on picking an item and on closing the window. It's not even realistic to take item price into account, so I disabled that requirement.

iPickMaxChance					75  -> 95			5% chance of being caught anyway.
fPickPocketMod					0.3 -> 0			This setting only changes max item price available for you to steal. 0 means infinite.

----------------------------------------------------------

## Magic -- Lots of spell effects wasn't really useful because of better alternatives. Also it's worth trying elemental shield now, for fun of killing low level creatures.

fElementalShieldMult			0.1 -> 1			1 point of damage for 1 point of magnitude.
sEffectSlowFall					SlowFall -> Slowfall

# Alteration -- Those weren't useful previously. Feather cost was the same as Fortify Strength, resulting being 5x weaker in encumbrance gain. Same rule apply to Swift Swim.

Feather							1 -> 0.1			2x encumbrance gain than Fortify Strength.
Burden							1 -> 0.1			2x encumbrance lost than Drain Strength.
Swift Swim						2 -> 0.5			2x faster swim than Fortify Speed.

# Destruction -- Elemental damage changes are just made for fun. Disintegrate would be better as offensive skill in other school, in Destruction there is no point of using it.

Poison							9 -> 4				
Fire Damage							 5				Unchanged.
Frost Damage					5 -> 6
Shock Damage						 7				Unchanged.
Damage Health						 8				Unchanged.
Disintegrate Armor				6 -> 1				It was only useful for stealing armor. Now it's easier.
Disintegrate Weapon				6 -> 1				Still it's better to kill opponent than using this.

# Illusion -- There was no point of using them instead of paralysis.

Silence							40 -> 20			2x cheaper than Paralyze.
Sound							3  -> 0.8			2x cheaper at 25% than Paralyze.
Demoralize Humanoid				Mysticism -> Illusion

# Mysticism -- Absorb spells were overpowered at the same cost as damage spells.

Absorb Health					8 -> 13				Damage Health (8) + Restore Health (5).
Absorb Fatigue					4 -> 5				Damage Fatigue (4) + Restore Fatigue (1).

# Restoration -- Fortify Magicka was doing less than Fortify Intelligence for the same price.

Fortify Magicka					1 -> 0.75			25% cheaper than Fortify Intelligence.
Fortify Skill					1 -> 4				4x more expensive, because it's overpowered.

----------------------------------------------------------

## Lockpicking -- Main goal here is to make Security skill useful on higher levels and be better than Alteration. Also opening 100 pts locks should be possible only for higher level characters. Previously magic was a better option to unlock the door at any level with cheap spells and scrolls. Now it requires mage skilled in Alteration to use existing or create useful open spells (Keep in mind that self made spells are 2x more expensive than standalones). For warriors there are still scrolls, but with price adjusted, because they are widely available. Also trap mechanics is restored, previously anyone could untrap any trap easly.

fPickLockMult					-1 -> -1.25			Locks are harder to unlock. To get any benefit from raising Security over 50.
fTrapCostMult					 0 -> -1			Trap spell cost is taken into account on disarming, similar to lock level.

# Spell Effect
Open							6  -> 12			2x more expensive.

# Cost
trap_poison00					16 -> 36			Only trap spell costs re-calculated from new spell effect values.
trap_fire00						3  -> 8
trap_health00					8  -> 13
trap_frost00					3  -> 10
trap_paralyze00					13 -> 21
trap_shock00					5  -> 12
trap_silence00					37 -> 31
trap_fire_killer				3  -> 63
trap_frost_killer				3  -> 75
trap_shock_killer				5  -> 88
trap_poison_killer				16 -> 75

# Price
sc_ondusisunhinging				73 -> 273			200gp more expensive.

# Magnitude
sc_ekashslocksplitter_en		100 -> 80
open							       20			Unchanged, unavailable in vanilla.
ondusi's open door				50  -> 40
strong open						50  -> 60
great open						50  -> 80			Unavailable in vanilla.
wild open						       1-100		Unchanged.

# How to open 100pts lock
- Thief	-- Security starting from level 60 (6% with pick quality 1,4 and average (50) attributes).
- Mage -- Alteration starting from level 60 (spell cost 120 with 8% chance on average (50) attributes).
- Warrior -- Enchanting Service -- 27000gp with Mercatile 50 and Disposition 100.

# How to untrap 100pts spell
- Thief	-- Security starting from level 90 (8% with probe quality 1,25 and average (50) attributes).
- Mage -- Telekinesis.
- Warrior -- Take it on the chin.

-----------------------------

TODO:
## Secret master apparatus prices
## Faction requirements

NOT TODO:
## Speechcraft -- It's not broken! It's a stat game between you and NPC. Boost your Speechcraft, Mercantile and reputation to get better results.
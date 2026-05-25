# Vanilla Spell Effects — Comprehensive Reference

Source: Individual UESP effect pages (en.uesp.net/wiki/Morrowind:*)
Content was rephrased for compliance with licensing restrictions.

---

## Alteration

### Burden
- **Base Cost:** 1.0
- **Mechanics:** Increases target's encumbrance by M points for D seconds. If encumbrance exceeds maximum, target becomes immobile.
- **Magnitude/Duration:** M = encumbrance points added; D = seconds.
- **Corner Cases:** Can be combined with Drain/Damage Strength for maximum effect (lowering max encumbrance while adding weight). Burden potions exist but are useless since potions are self-only.
- **Notes:** Resisted by Resist Magicka. Amplified by Weakness to Magicka. Alternative: Drain Strength or Damage Strength to lower max encumbrance.

### Feather
- **Base Cost:** 1.0
- **Mechanics:** Reduces target's encumbrance by M points for D seconds, allowing them to carry more. Also causes Fatigue to drain more slowly.
- **Magnitude/Duration:** M = encumbrance points removed; D = seconds. Can make encumbrance negative (displayed as 0).
- **Corner Cases:** Fortify Strength is generally superior — each point of Strength gives 5 encumbrance, making it 5x more effective per base cost. However, Feather is better when encumbrance is already low (speed/jump/fatigue are based on encumbrance ratio, not magnitude).
- **Bugs:** Loading a save can cause an active Feather effect to stop reducing encumbrance. When the effect expires, extra weight is still dumped on you, resulting in non-zero encumbrance with no items. Fix via console by adding/removing items.
- **Notes:** Useful if skilled in Alteration but not Restoration.

### Fire Shield
- **Base Cost:** 3.0
- **Mechanics:** Two effects: (1) Provides M% Resist Fire, reducing Fire Damage by M%. (2) Deals retaliatory elemental damage to melee attackers at ~1 point per 10 points of magnitude.
- **Magnitude/Duration:** M = percentage resistance AND shield strength; D = seconds.
- **Corner Cases:** Retaliatory damage formula is complex (per OpenMW code): factors in attacker's Destruction skill, Willpower, Luck, fatigue ratio, and elemental resistance. Damage is further modified by difficulty scaling. Total resistance is capped 0–100.
- **Notes:** Despite red icon suggesting Destruction, this is an Alteration effect. Does NOT increase armor rating (unlike Oblivion). fElementalShieldMult default = 0.01.

### Frost Shield
- **Base Cost:** 3.0
- **Mechanics:** Two effects: (1) Provides M% Resist Frost. (2) Deals retaliatory frost damage to melee attackers (~1 point per 10 magnitude).
- **Magnitude/Duration:** M = percentage resistance AND shield strength; D = seconds.
- **Corner Cases:** Same formula as Fire Shield but using frost resistance.
- **Notes:** Does NOT increase armor rating. Is an Alteration effect.

### Lightning Shield
- **Base Cost:** 3.0
- **Mechanics:** Two effects: (1) Provides M% Resist Shock. (2) Deals retaliatory shock damage to melee attackers (~1 point per 10 magnitude).
- **Magnitude/Duration:** M = percentage resistance AND shield strength; D = seconds.
- **Corner Cases:** Same formula as Fire Shield but using shock resistance.
- **Notes:** Unique naming — uses "Lightning" instead of "Shock" unlike all other shock-related effects. Does NOT increase armor rating.

### Jump
- **Base Cost:** 3.0
- **Mechanics:** Increases maximum jumping height of the subject by M points for D seconds.
- **Magnitude/Duration:** M modifies jump height; D = seconds. Exact formula unclear (additive vs multiplicative debated).
- **Corner Cases:** Does NOT increase safe fall height — you can take damage landing from your own jump. Combine with Slowfall (even 1 pt negates all fall damage) or short Levitate before landing. NPCs/creatures never jump, so casting on them is useless. Multiple Hoptoad Rings can be activated in succession for free high-powered Jump.
- **Notes:** Can be used for fast travel across the map when combined with Slowfall. Acrobatics trains faster from fall damage, so Jump without Slowfall can be used for training.

### Levitate
- **Base Cost:** 3.0
- **Mechanics:** Allows target to walk on air. Movement speed determined by M and character's Speed attribute. Encumbrance also affects speed.
- **Magnitude/Duration:** M = levitation speed factor; D = seconds. Athletics has NO effect on levitation speed.
- **Corner Cases:** Cannot rest on ground while levitating (can rest in beds). Head can get stuck in ceilings in cramped spaces. Spell persists through fast travel as if instantaneous. Low-magnitude Levitate (1 pt) can be used offensively to render enemies nearly immobile. Overrides swimming speed penalty — 1 pt Levitate dramatically speeds up water movement for high-Speed characters.
- **Bugs:** Levitating into lava does no damage. Entering a door while levitating can snag PC on floor (race-dependent — Altmer snag more than Bosmer). Cliff Racers hit by Levitate crash to ground and take fall damage. Enemy corpses affected by Levitate in interior cells fall through the floor (not guards).
- **Notes:** Cannot levitate in Mournhold or Mortrag Glacier. Levitate 1pt + Fortify Speed is more efficient than high-magnitude Levitate. Constant Effect Levitate on Daedric Tower Shield = 15 pts; Exquisite ring/amulet = 8 pts.

### Lock
- **Base Cost:** 2.0
- **Mechanics:** Locks a door or container at M points. Effect is permanent until opened by Open spell, lockpick, or key. Uses only magnitude (no duration).
- **Magnitude/Duration:** M = lock level applied. No duration component.
- **Corner Cases:** If cast on already-locked object: only replaces lock if spell magnitude > current lock level. Cannot weaken a lock. NPCs cannot pick locks or cast Open, so even 1-point Lock is effective against them. Can lock almost any container including sacks and barrels. Locked/unlocked containers permanently show "unlocked" notice after being Lock-spelled and opened.
- **Notes:** Can be used to trap pursuers or keep witnesses out. Useful for training Security (lock then pick repeatedly). Lockpicking an owned container is a crime even if you locked it. Can permanently trap yourself if you lock a door you cannot unlock. Fenrick's Doorjam (1 magicka) is the only Lock spell you ever need.

### Open
- **Base Cost:** 6.0
- **Mechanics:** Opens a locked door or chest. Magnitude equals the lock level that can be opened. Uses only magnitude (no duration). Does NOT disarm traps.
- **Magnitude/Duration:** M = maximum lock level that can be opened. No duration.
- **Corner Cases:** Casting Open as Touch or Target is a crime if witnessed. A 3-second 100% Chameleon spell covers you long enough to cast unseen. Crouching in third person causes the effect to trigger before the animation finishes.
- **Notes:** Use Telekinesis to trigger traps from safe distance, or a probe to disarm them.

### Shield
- **Base Cost:** 2.0
- **Mechanics:** Increases target's Armor Rating by M points for D seconds. Creates a magical shield around the entire body.
- **Magnitude/Duration:** M = armor rating points added; D = seconds.
- **Corner Cases:** For armor with base AR ≥ 15, Fortify Armor Skill is more cost-effective. For Netch Leather/Nordic Fur/Chitin (low AR), Shield is better. For unarmored characters, Shield is better if (base Unarmored + Shield magnitude) < 38; otherwise Fortify Unarmored is superior.
- **Notes:** Shield AR is NOT diminished by armor damage. Purely additive to existing AR.

### Slowfall
- **Base Cost:** 3.0
- **Mechanics:** Reduces falling damage by slowing descent rate. M determines how much descent is slowed.
- **Magnitude/Duration:** M = slowfall strength; D = seconds.
- **Corner Cases:** ANY value of Slowfall (even 0 pts as Constant Effect) makes you completely immune to fall damage. However, 1 pt Slowfall reduces horizontal jump distance by ~50%. High magnitude can serve as pseudo-Levitate in areas where levitation is disabled (Mournhold, Bloodmoon).
- **Bugs:** Using Slowfall on NPCs/creatures (especially followers entering new cells) causes the effect to work in REVERSE, increasing fall damage. Often fatal. Never use on anyone but yourself.
- **Notes:** Best combined with Jump or Fortify Acrobatics. Fortify Acrobatics to 125 also negates fall damage without affecting momentum.

### Swift Swim
- **Base Cost:** 2.0
- **Mechanics:** Increases target's swimming speed by M points for D seconds.
- **Magnitude/Duration:** M = swim speed bonus; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Generally inferior to Fortify Speed, which works on land too and has similar cost-effectiveness.

### Water Breathing
- **Base Cost:** 3.0
- **Mechanics:** Allows target to breathe underwater for D seconds. No magnitude — duration only.
- **Magnitude/Duration:** No magnitude. D = seconds of underwater breathing.
- **Corner Cases:** When effect expires, breath meter returns to FULL capacity regardless of state when cast. This means even a very short duration spell completely replenishes air. All creatures can breathe underwater by default — only NPCs can drown.
- **Notes:** Avoid permanent Water Breathing before completing "Pilgrimages of the Seven Graces" (requires drowning). Touch/Target versions useful for escort missions (escort AI is bad at swimming). Luminous Russula can be eaten raw for short Water Breathing.

### Water Walking
- **Base Cost:** 3.0
- **Mechanics:** Allows target to walk on water at normal speed for D seconds. No magnitude — duration only.
- **Magnitude/Duration:** No magnitude. D = seconds.
- **Corner Cases:** Cannot swim underwater while effect is active (problematic for underwater areas). In rare cases, sloping ceilings leading into water can force you under. Falling onto water with this effect active still causes fall damage. Activating the effect while deep underwater shows "You cannot cast this effect at the moment."
- **Notes:** Underwater creatures cannot reach you. Few flying creatures appear over water. Not ideal as permanent effect due to inability to dive.

---

## Destruction

### Fire Damage
- **Base Cost:** 5.0
- **Mechanics:** Deals M points of fire damage per second for D seconds. Total damage = M × D.
- **Magnitude/Duration:** M = damage per second; D = seconds.
- **Corner Cases:** Projectile speed scale of 1.25 — ranged Fire Damage-only spells travel faster than other spells. Multi-effect spells travel at normal speed.
- **Notes:** Dark Elves have natural Resist Fire (75%), making it less effective against the most common humanoid race on Vvardenfell. However, many undead are resistant/immune to all elements EXCEPT fire. Low base cost + high projectile speed make it viable despite Dunmer resistance.

### Frost Damage
- **Base Cost:** 5.0
- **Mechanics:** Deals M points of frost damage per second for D seconds. Total damage = M × D.
- **Magnitude/Duration:** M = damage per second; D = seconds.
- **Corner Cases:** Projectile speed scale of 0.80 — ranged Frost Damage-only spells travel SLOWER than other spells. Multi-effect spells travel at normal speed.
- **Notes:** Nords are immune to Frost. Most undead resist or are immune to frost. Especially problematic in Bloodmoon (most enemies are Nords or frost-resistant creatures).

### Shock Damage
- **Base Cost:** 7.0
- **Mechanics:** Deals M points of shock damage per second for D seconds. Total damage = M × D.
- **Magnitude/Duration:** M = damage per second; D = seconds.
- **Corner Cases:** No special projectile speed modifier documented.
- **Notes:** Most expensive elemental damage but fewest enemies resist it (only Nords and Storm Atronachs without resisting everything). Most universally useful for enchantments. Premade shock items are equally effective as fire/frost counterparts for no extra cost. For spellcasting, having separate Fire and Frost spells may be more efficient — few enemies resist both without also resisting Shock.

### Poison
- **Base Cost:** 9.0
- **Mechanics:** Deals M points of poison damage per second for D seconds. Total damage = M × D.
- **Magnitude/Duration:** M = damage per second; D = seconds.
- **Corner Cases:** Can be negated by Cure Poison spell (no equivalent exists for other elements).
- **Notes:** Least useful elemental damage: most expensive base cost, most creatures immune (all undead), and can be cured. Resisted by Resist Poison.

### Damage Health
- **Base Cost:** 8.0
- **Mechanics:** Permanently lowers current Health by M points (instant effect). Does NOT affect maximum health. Not elemental — bypasses elemental resistances.
- **Magnitude/Duration:** M = health points removed. No duration (instant).
- **Corner Cases:** Absorb Health has the same base cost but also heals the caster — strictly superior for both spells and enchantments.
- **Notes:** Useful against creatures resistant to elemental damage. More expensive than elemental options but universally effective. Only Resist Magicka reduces it.

### Damage Magicka
- **Base Cost:** 8.0
- **Mechanics:** Permanently lowers current Magicka by M points. Does not affect maximum magicka.
- **Magnitude/Duration:** M = magicka points removed. No duration (instant).
- **Corner Cases:** None documented.
- **Notes:** Useful for disabling enemy spellcasters.

### Damage Fatigue
- **Base Cost:** 4.0
- **Mechanics:** Permanently lowers current Fatigue by M points. Does not affect maximum fatigue.
- **Magnitude/Duration:** M = fatigue points removed. No duration (instant).
- **Corner Cases:** None documented.
- **Notes:** Low base cost. Reducing fatigue to 0 causes unconsciousness. Affects hit chance and spell success.

### Damage Attribute
- **Base Cost:** 5.0
- **Mechanics:** Permanently lowers a specific attribute by M points. Requires Restore Attribute to recover.
- **Magnitude/Duration:** M = attribute points removed. No duration (permanent until restored).
- **Corner Cases:** Can be reflected — very dangerous if your own Damage Strength/etc. bounces back.
- **Notes:** Extremely powerful debuff. Greater Bonewalkers use Damage Strength which can permanently cripple unprepared characters.

### Damage Skill
- **Base Cost:** 5.0
- **Mechanics:** Permanently lowers a specific skill by M points. Requires Restore Skill to recover.
- **Magnitude/Duration:** M = skill points removed. No duration (permanent until restored).
- **Corner Cases:** None documented.
- **Notes:** Rarely used by enemies. Can be devastating if reflected.

### Drain Health
- **Base Cost:** 4.0
- **Mechanics:** Temporarily lowers current Health by M points for D seconds. Health returns when effect expires (if target survives).
- **Magnitude/Duration:** M = health points drained; D = seconds.
- **Corner Cases:** WILL kill if health reaches 0 — despite being "temporary," death is permanent. Drain Health 100 pts for 1 sec is an efficient kill spell against enemies with <100 HP. Can be amplified by Weakness to Magicka 100% for 1 sec (doubles effect).
- **Notes:** Lowest base cost in Destruction school (tied with Damage Fatigue at 4). Not elemental — few creatures resist Magicka. Excellent for enchantments and efficient kill combos.

### Drain Magicka
- **Base Cost:** 5.0
- **Mechanics:** Temporarily lowers current Magicka by M points for D seconds. Magicka returns when effect expires.
- **Magnitude/Duration:** M = magicka points drained; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Useful for temporarily disabling spellcasters.

### Drain Fatigue
- **Base Cost:** 5.0
- **Mechanics:** Temporarily lowers current Fatigue by M points for D seconds. Fatigue returns when effect expires.
- **Magnitude/Duration:** M = fatigue points drained; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Can cause temporary unconsciousness if fatigue reaches 0.

### Drain Attribute
- **Base Cost:** 5.0
- **Mechanics:** Temporarily lowers a specific attribute by M points for D seconds. Attribute returns when effect expires.
- **Magnitude/Duration:** M = attribute points drained; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Drain Strength to 0 makes target immobile (encumbrance exceeds capacity). Temporary alternative to Damage Attribute.

### Drain Skill
- **Base Cost:** 5.0
- **Mechanics:** Temporarily lowers a specific skill by M points for D seconds. Skill returns when effect expires.
- **Magnitude/Duration:** M = skill points drained; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Rarely used offensively.

### Disintegrate Armor
- **Base Cost:** 6.0
- **Mechanics:** Damages one piece of equipped armor by M points per second for D seconds. Targets armor in order: Shield, Cuirass, Left Pauldron, Right Pauldron, Left Gauntlet, Right Gauntlet, Helm, Greaves, Boots.
- **Magnitude/Duration:** M = condition damage per second; D = seconds.
- **Corner Cases:** If armor breaks (condition reaches 0), it is immediately unequipped and target auto-equips next-most-valuable piece. "On Self" only works on already-damaged equipment. Resisted by Sanctuary (NOT Resist Magicka).
- **Notes:** Can be used to steal armor — break it, Calm the NPC, pickpocket the broken piece, repair it. Don't sell it back to the same person.

### Disintegrate Weapon
- **Base Cost:** 6.0
- **Mechanics:** Damages equipped and drawn weapon by M points per second for D seconds.
- **Magnitude/Duration:** M = condition damage per second; D = seconds.
- **Corner Cases:** Only works if weapon is equipped AND drawn. Non-hostile enemies won't have weapons drawn, but casting (hostile action) causes them to draw weapons — subsequent casts work. "On Self" only works on already-damaged equipment. Resisted by Sanctuary (NOT Resist Magicka).
- **Notes:** Casting on non-hostile target is a crime.

### Weakness to Fire
- **Base Cost:** 1.0
- **Mechanics:** Increases fire damage taken by M% for D seconds.
- **Magnitude/Duration:** M = percentage weakness; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Must be applied BEFORE fire damage for full effect (or use multi-effect spell where weakness is listed first).

### Weakness to Magicka
- **Base Cost:** 2.0
- **Mechanics:** Increases the magnitude of certain hostile magical effects by M% for D seconds.
- **Magnitude/Duration:** M = percentage increase; D = seconds.
- **Corner Cases:** Does NOT affect elemental damage (Fire/Frost/Shock/Poison). Does NOT increase duration of any effect. Does NOT affect Paralyze. DOES increase: Absorb Health, Damage Health, Drain Health, all other Absorb/Damage/Drain effects, Blind, Burden, Sound, Silence, Charm, Frenzy, and other Weakness effects.
- **Notes:** High Elves and The Apprentice birthsign have innate Weakness to Magicka. Not a serious handicap since enemies using Absorb/Damage Health are rare (Vampires being the notable exception).

---

## Illusion

### Blind
- **Base Cost:** 1.0
- **Mechanics:** Reduces target's chance to hit with physical attacks by M points for D seconds. Additive penalty to attacker's hit roll.
- **Magnitude/Duration:** M = hit chance reduction (points, not percent); D = seconds.
- **Corner Cases:** Works additively in the combat hit formula alongside Fortify Attack and Sanctuary.
- **Notes:** Casting Blind is a hostile action. Can be used with Chameleon/Sneak to further reduce detection.

### Paralyze
- **Base Cost:** 40.0
- **Mechanics:** Completely immobilizes target for D seconds. No magnitude — duration only. Target cannot move, attack, cast spells, or use enchanted items/scrolls. CAN still use potions, eat ingredients, and equip/unequip items.
- **Magnitude/Duration:** No magnitude. D = seconds of paralysis.
- **Corner Cases:** Paralyzed opponents take direct health damage from Hand-to-Hand attacks (normally H2H only damages fatigue until knockout). Resisted by high Willpower. NOT resisted by Resist Magicka. CAN be Absorbed or Reflected. Paralyzed Cliff Racers fall from sky without taking damage. Paralyzed dreugh/slaughterfish float to surface.
- **Notes:** Vampires are completely immune. Very high base cost (40) makes it expensive. Extremely powerful crowd control.

### Silence
- **Base Cost:** 5.0
- **Mechanics:** Prevents target from casting spells for D seconds. No magnitude — duration only.
- **Magnitude/Duration:** No magnitude. D = seconds.
- **Corner Cases:** Does not prevent use of enchanted items, scrolls, or potions.
- **Notes:** Effective against enemy spellcasters. Can be combined with Paralyze for total lockdown.

### Sound
- **Base Cost:** 0.5
- **Mechanics:** Reduces target's chance to successfully cast spells by M points for D seconds. Essentially a partial Silence.
- **Magnitude/Duration:** M = spell failure chance increase; D = seconds.
- **Corner Cases:** At 100 magnitude, functionally identical to Silence but much cheaper base cost.
- **Notes:** Extremely low base cost (0.5). Affected by Weakness to Magicka.

### Chameleon
- **Base Cost:** 1.0
- **Mechanics:** Makes target partially transparent, reducing detectability. M is listed as percentage but does not mechanically work as a true percentage.
- **Magnitude/Duration:** M = chameleon strength; D = seconds.
- **Corner Cases:** 75% appears sufficient to walk past hostile NPCs. Magnitude adds directly to Sneak chance. Increases evasion (capped at 500 Chameleon) at same rate as Agility but NOT subject to Fatigue modifier. Talking to NPCs while under Chameleon may fail — NPC loses 5 Disposition per failed attempt. Ghost NPCs use 50% Chameleon as their "Ghost Ability."
- **Notes:** Unlike Invisibility, does NOT break on interaction (attacking, opening doors, casting spells, etc.). Effectively disabled the conversation-failure mechanic in Bloodmoon via ESM change, but mods can accidentally reintroduce it.

### Invisibility
- **Base Cost:** 20.0
- **Mechanics:** Makes target completely invisible and undetectable for D seconds. No magnitude — duration only. Breaks immediately upon ANY interaction (attacking, picking up items, opening doors/containers, talking).
- **Magnitude/Duration:** No magnitude. D = seconds.
- **Corner Cases:** Sneak skill is irrelevant while invisible — you are completely undetectable. Constant Effect Invisibility still breaks on interaction (must re-equip item to reactivate). Can bump into NPCs/creatures without detection — can nudge stationary NPCs around.
- **Notes:** Attack from invisibility is not undetectable — can still incur bounty. Many players prefer Chameleon for sustained stealth since it doesn't break.

### Sanctuary
- **Base Cost:** 1.0
- **Mechanics:** Increases target's chance to dodge physical attacks by M points for D seconds. Additive bonus to defender's roll in combat formula.
- **Magnitude/Duration:** M = dodge bonus (points); D = seconds.
- **Corner Cases:** Capped at 100 — points above 100 do nothing. Effect is additive and NOT subject to Fatigue coefficient (unlike Agility/Luck contributions). If defender's total (Agility + Luck + Sanctuary) exceeds attacker's total (skill + Agility + Luck + Fortify Attack) by enough, hit chance is 0%. If attacker exceeds defender by 100+, they always hit.
- **Notes:** Also resists Disintegrate Armor/Weapon effects (unusual interaction). Most efficient avoidance: 100 Sanctuary + high Agility.

### Charm
- **Base Cost:** 3.0
- **Mechanics:** Temporarily increases target's Disposition toward caster by M points for D seconds.
- **Magnitude/Duration:** M = disposition points added; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Useful for passing disposition checks for services/information. Temporary — disposition reverts after duration.

### Calm Humanoid
- **Base Cost:** 1.0
- **Mechanics:** Causes hostile humanoid NPCs to stop attacking for D seconds. Magnitude determines the level of creature/NPC that can be affected.
- **Magnitude/Duration:** M = maximum level affected; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Useful for de-escalating combat or accessing services from hostile NPCs.

### Demoralize Humanoid
- **Base Cost:** 1.0
- **Mechanics:** Causes humanoid NPCs to flee in terror for D seconds. Magnitude determines the level affected.
- **Magnitude/Duration:** M = maximum level affected; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Fleeing enemies can be difficult to chase down.

### Frenzy Humanoid
- **Base Cost:** 1.0
- **Mechanics:** Causes humanoid NPCs to attack nearby targets (including allies) for D seconds. Magnitude determines level affected.
- **Magnitude/Duration:** M = maximum level affected; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Useful for causing infighting or provoking NPCs to attack first (avoiding bounty).

### Light
- **Base Cost:** 0.5
- **Mechanics:** Creates a light source of M brightness for D seconds.
- **Magnitude/Duration:** M = light radius/brightness; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Very cheap base cost. Useful in dark dungeons.

---

## Mysticism

### Absorb Health
- **Base Cost:** 8.0
- **Mechanics:** Transfers M health points per second from target to caster for D seconds. Damages target AND heals caster simultaneously.
- **Magnitude/Duration:** M = health transferred per second; D = seconds.
- **Corner Cases:** Same base cost as Damage Health but strictly superior (also heals caster). Better choice for enchantments.
- **Notes:** Not elemental — bypasses elemental resistances. Affected by Weakness to Magicka.

### Absorb Magicka
- **Base Cost:** 5.0
- **Mechanics:** Transfers M magicka points per second from target to caster for D seconds.
- **Magnitude/Duration:** M = magicka transferred per second; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Useful for magicka recovery, especially for Atronach birthsign characters.

### Absorb Fatigue
- **Base Cost:** 5.0
- **Mechanics:** Transfers M fatigue points per second from target to caster for D seconds.
- **Magnitude/Duration:** M = fatigue transferred per second; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Can knock out targets while restoring your own fatigue.

### Absorb Attribute
- **Base Cost:** 5.0
- **Mechanics:** Temporarily transfers M points of a specific attribute from target to caster for D seconds.
- **Magnitude/Duration:** M = attribute points transferred; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Attribute returns to target and leaves caster when effect expires.

### Reflect
- **Base Cost:** 10.0
- **Mechanics:** Gives M% chance that incoming hostile spells are reflected back at their caster. Unreflected spells do full damage.
- **Magnitude/Duration:** M = reflection chance (percentage); D = seconds.
- **Corner Cases:** Multiple Reflect sources are evaluated SEPARATELY (multiplicative failure chance). Two 50% Reflects = 75% total, not 100%. Spells can only be reflected ONCE. Reflected spells cannot be dodged (no projectile), bypass godmode, and hit instantly. If both caster and target have 100% Reflect, spell hits the caster. Traps cannot be reflected.
- **Notes:** Interacts with Spell Absorption — whichever was applied FIRST takes precedence. Reflected spells are still subject to the new target's resistances (not reduced by original target's resistances first). Many creatures have innate Reflect (Ash Ghouls, Atronachs, Dremora, Golden Saints, etc.).
- **Bugs:** Melee damage from weapons with "on Target" enchantments can be reflected if the weapon has enough charges.

### Spell Absorption
- **Base Cost:** 10.0
- **Mechanics:** Gives M% chance that incoming spells are absorbed, restoring their casting cost as Magicka instead of taking effect. Unabsorbed spells do full damage.
- **Magnitude/Duration:** M = absorption chance (percentage); D = seconds.
- **Corner Cases:** Multiple sources evaluated SEPARATELY (same multiplicative formula as Reflect). Two 50% absorptions = 75% total. Interacts with Reflect — whichever was applied first takes precedence. Beneficial spells (shrine blessings, cures) can also be absorbed. Spells with no magnitude (Silence, Paralyze) CAN be absorbed — their casting cost is what gets absorbed.
- **Notes:** Essential for Atronach birthsign (50% innate absorption). Can regenerate magicka by summoning an Ancestor Ghost, attacking it 3 times to turn it hostile, then absorbing its spells.

### Telekinesis
- **Base Cost:** 1.0
- **Mechanics:** Allows interaction with objects at a distance of M feet for D seconds.
- **Magnitude/Duration:** M = range in feet; D = seconds.
- **Corner Cases:** Can be used to trigger traps from safe distance. Can activate objects through walls in some cases.
- **Notes:** Useful with Open spell to avoid crime detection.

### Detect Animal
- **Base Cost:** 1.0
- **Mechanics:** Detects animals/creatures within M feet for D seconds, showing them on the local map/compass.
- **Magnitude/Duration:** M = detection range in feet; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Also Detect Enchantment (base cost 1.0) and Detect Key (base cost 1.0) exist as separate effects.

### Dispel
- **Base Cost:** 5.0
- **Mechanics:** Cancels all temporary magic effects on target. M determines the chance each effect is removed. Dispel 100% always removes all temporary effects.
- **Magnitude/Duration:** M = percentage chance to remove each effect. No duration (instant).
- **Corner Cases:** Only removes TEMPORARY spell effects. Does NOT affect: abilities, potions, enchanted item effects, scroll effects, or diseases. Removes both positive AND negative effects indiscriminately. Can remove enemy bound items and summoned creatures. Can dispel enchanted item effects only if the Dispel is cast from the SAME item.
- **Notes:** Disadvantage vs. targeted cures (like Cure Paralyzation) when used on self/allies since it removes buffs too. Advantage on enemies since it strips their defenses.

### Soultrap
- **Base Cost:** 3.0
- **Mechanics:** If target dies while under this effect and caster has an appropriately-sized empty soul gem, the target's soul is captured.
- **Magnitude/Duration:** No magnitude. D = seconds (window during which death must occur).
- **Corner Cases:** None documented.
- **Notes:** Essential for enchanting. Can be combined with damage spells in a single cast for efficiency.

---

## Restoration

### Restore Health
- **Base Cost:** 3.0
- **Mechanics:** Restores M health points per second for D seconds. Cannot exceed maximum health.
- **Magnitude/Duration:** M = health restored per second; D = seconds.
- **Corner Cases:** None documented.
- **Notes:** Standard healing effect. Also exists as Restore Magicka (base cost 3.0), Restore Fatigue (base cost 3.0), Restore Attribute (base cost 3.0), and Restore Skill (base cost 3.0).

### Fortify Attribute
- **Base Cost:** 1.0
- **Mechanics:** Temporarily increases a specific attribute by M points for D seconds. Attribute returns to normal when effect expires.
- **Magnitude/Duration:** M = attribute points added; D = seconds.
- **Corner Cases:** Fortify Strength gives 5 encumbrance per point (5x more effective than Feather). Fortify Speed affects levitation speed.
- **Notes:** Very low base cost (1.0) makes this extremely efficient. Fortify Intelligence before creating potions for alchemy exploits.

### Fortify Health
- **Base Cost:** 1.0
- **Mechanics:** Temporarily increases maximum AND current Health by M points for D seconds.
- **Magnitude/Duration:** M = health points added; D = seconds.
- **Corner Cases:** When effect expires, maximum health returns to normal. If current health exceeds new maximum, it is reduced to the new maximum.
- **Notes:** Very low base cost. Effectively a damage buffer.

### Fortify Skill
- **Base Cost:** 1.0
- **Mechanics:** Temporarily increases a specific skill by M points for D seconds.
- **Magnitude/Duration:** M = skill points added; D = seconds.
- **Corner Cases:** Fortify Acrobatics to 125 negates all fall damage without affecting momentum. Fortify armor skills can be more efficient than Shield for high-AR armor.
- **Notes:** Very low base cost. Useful for passing skill checks or improving combat effectiveness.

### Resist Fire
- **Base Cost:** 2.0
- **Mechanics:** Reduces fire damage taken by M% for D seconds.
- **Magnitude/Duration:** M = percentage resistance; D = seconds.
- **Corner Cases:** Stacks with racial resistances (Dunmer 75% innate).
- **Notes:** Also exists as Resist Frost (base cost 2.0) and Resist Shock (base cost 2.0).

### Resist Magicka
- **Base Cost:** 2.0
- **Mechanics:** Reduces the magnitude of non-elemental hostile magic effects by M% for D seconds.
- **Magnitude/Duration:** M = percentage resistance; D = seconds.
- **Corner Cases:** Does NOT resist Paralyze. Does NOT resist elemental damage (use Resist Fire/Frost/Shock for those). Does resist Burden, Drain effects, Damage effects, Absorb effects, etc.
- **Notes:** Breton racial ability provides 50% innate Resist Magicka.

### Resist Normal Weapons
- **Base Cost:** 3.0
- **Mechanics:** Reduces physical damage from non-enchanted weapons by M% for D seconds.
- **Magnitude/Duration:** M = percentage resistance; D = seconds.
- **Corner Cases:** Only affects "normal" (non-magical, non-silver, non-daedric) weapons. Enchanted weapons, silver weapons, and daedric weapons bypass this resistance entirely.
- **Notes:** Many creatures have innate Resist Normal Weapons (ghosts, daedra). At 100%, completely immune to normal weapon damage.

### Resist Paralysis
- **Base Cost:** 3.0
- **Mechanics:** Reduces chance of being paralyzed by M% for D seconds.
- **Magnitude/Duration:** M = percentage resistance; D = seconds.
- **Corner Cases:** This is one of the few ways to resist Paralyze (Resist Magicka does NOT work against it).
- **Notes:** Important defense against paralysis-using enemies (Scribs, Greater Bonewalkers, etc.).

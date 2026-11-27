-- R3 - Core values (absolute). Source: the old R3 - Core.esp before the move to Lua.
local M = {}


-- Movement speed (menu choice, menu.lua): vanilla GMST values and the multiplier
-- of each choice. "vanilla" leaves the GMSTs as the load order provides them.
M.WALK_SPEED = {
    fMinWalkSpeed = 100,
    fMaxWalkSpeed = 200,
    fMinWalkSpeedCreature = 5,
    fMaxWalkSpeedCreature = 300,
}
M.WALK_SPEED_MULT = { vanilla = 1, plus25 = 1.25, plus50 = 1.5 }
M.WALK_SPEED_DEFAULT = 'plus25'
-- Merchant gold reset (menu choice): fBarterGoldResetDelay, in hours.
M.BARTER_RESET = { hour = 1, day = 24, month = 720 }
M.BARTER_RESET_DEFAULT = 'month'
-- Message hidden by the menu option: GMST id, set to an empty string. The engine
-- shows "#{sMagicInsufficientCharge}"; a string GMST is replaced by its text, so
-- the box gets no text and a display time of 0 (length x time per character) and
-- is removed on the next frame. Any non-string value (number, or no value at all)
-- makes the engine print the tag name "sMagicInsufficientCharge" instead.
-- [mwgui/windowmanagerimp.cpp onRetrieveTag, mwgui/messagebox.cpp]
M.HIDDEN_MESSAGE = 'sMagicInsufficientCharge'

-- Magic effect id -> base cost (Rebalanced Spell Costs setting). Open 12 is also
-- in the lockpicking group, so it applies when either setting is on.
M.EFFECTS = {
    ["absorbfatigue"] = 6,
    ["absorbhealth"] = 16,
    ["burden"] = 0.1,
    ["charm"] = 2.5,
    ["damageattribute"] = 24,
    ["damagefatigue"] = 2,
    ["damagemagicka"] = 4,
    ["detectanimal"] = 0.15,
    ["detectenchantment"] = 0.2,
    ["detectkey"] = 0.2,
    ["disintegratearmor"] = 0.6,
    ["disintegrateweapon"] = 1.2,
    ["drainfatigue"] = 0.2,
    ["drainmagicka"] = 0.4,
    ["feather"] = 0.1,
    ["firedamage"] = 8,
    ["fortifyfatigue"] = 0.25,
    ["fortifyskill"] = 4,
    ["frostdamage"] = 8,
    ["lock"] = 24,
    ["open"] = 12,
    ["paralyze"] = 80,
    ["poison"] = 8,
    ["reflect"] = 2.5,
    ["resistblightdisease"] = 0.25,
    ["resistcommondisease"] = 0.1,
    ["resistfire"] = 0.5,
    ["resistfrost"] = 0.5,
    ["resistmagicka"] = 0.5,
    ["resistpoison"] = 0.5,
    ["resistshock"] = 0.5,
    ["restoreattribute"] = 8,
    ["restorefatigue"] = 2.5,
    ["shield"] = 1,
    ["shockdamage"] = 8,
    ["sound"] = 1,
    ["spellabsorption"] = 2.5,
    ["swiftswim"] = 0.5,
}




-- Value groups, README section in brackets. Groups listed in settings.TOGGLES
-- have a Yes/No menu setting (default Yes); off leaves the records as the load
-- order provides them. The other groups always apply.
-- Tables per group: gmsts (id -> value), skills (id -> { attribute, skillGain }),
-- effects (id -> base cost), spells / enchantments (id -> { cost, [charge],
-- effects per index }), books / apparatuses (id -> value).
M.GROUPS = {
    { -- [Health]
        key = "health",
        gmsts = {
            fLevelUpHealthEndMult = 0.05,
        },
    },
    { -- [Skills]
        key = "skills",
        skills = {
            armorer = { attribute = "endurance", skillGain = { 1, 1, 1, 1 } },
            enchant = { attribute = "intelligence", skillGain = { 2, 0.1, 5, 0 } },
        },
    },
    { -- [Travel]
        key = "travel",
        gmsts = {
            fMagesGuildTravel = 50,
        },
    },
    { -- [Crime]
        key = "crime",
        gmsts = {
            iCrimeAttack = 1000,
            iCrimeKilling = 5000,
            iCrimePickPocket = 250,
            iCrimeTresspass = 500,
            iDaysinPrisonMod = 500,
        },
    },
    { -- [Pickpocket]
        key = "pickpocket",
        gmsts = {
            fPickPocketMod = 0.001,
            iPickMaxChance = 100,
        },
    },
    { -- [Lockpicking]
        key = "lockpicking",
        gmsts = {
            fPickLockMult = -1.25,
        },
        effects = {
            ["open"] = 12,
        },
        spells = {
            ["great open"] = { cost = 48, effects = { { magnitudeMin = 80, magnitudeMax = 80, duration = 1, area = 0 } } },  -- Great Open
            ["ondusi's open door"] = { cost = 24, effects = { { magnitudeMin = 40, magnitudeMax = 40, duration = 1, area = 0 } } },  -- Ondusi's Open Door
            ["strong open"] = { cost = 36, effects = { { magnitudeMin = 60, magnitudeMax = 60, duration = 1, area = 0 } } },  -- Strong Open
        },
        enchantments = {
            ["sc_ekashslocksplitter_en"] = { cost = 72, charge = 72, effects = { { magnitudeMin = 80, magnitudeMax = 100, duration = 1, area = 0 } } },
        },
        books = {
            ["sc_ondusisunhinging"] = 173,  -- Scroll of Ondusi's Unhinging
        },
    },
    { -- [Traps]
        key = "traps",
        gmsts = {
            fTrapCostMult = -0.75,
        },
        spells = {
            ["trap_fire00"] = { cost = 8, effects = { { magnitudeMin = 2, magnitudeMax = 20, duration = 3, area = 1 } } },  -- Fire Trap
            ["trap_fire_killer"] = { cost = 63, effects = { { magnitudeMin = 20, magnitudeMax = 30, duration = 10, area = 1 } } },  -- Master Fire Trap
            ["trap_frost00"] = { cost = 8, effects = { { magnitudeMin = 2, magnitudeMax = 20, duration = 3, area = 1 } } },  -- Frost Trap
            ["trap_frost_killer"] = { cost = 63, effects = { { magnitudeMin = 20, magnitudeMax = 30, duration = 10, area = 1 } } },  -- Master Frost Trap
            ["trap_health00"] = { cost = 13, effects = { { magnitudeMin = 2, magnitudeMax = 20, duration = 3, area = 1 } } },  -- Lifeforce Trap
            ["trap_paralyze00"] = { cost = 21, effects = { { magnitudeMin = 1, magnitudeMax = 1, duration = 10, area = 1 } } },  -- Paralysis Trap
            ["trap_poison00"] = { cost = 81, effects = { { magnitudeMin = 1, magnitudeMax = 5, duration = 60, area = 1 } } },  -- Poison Trap
            ["trap_poison_killer"] = { cost = 169, effects = { { magnitudeMin = 5, magnitudeMax = 10, duration = 50, area = 1 } } },  -- Master Poison Trap
            ["trap_shock00"] = { cost = 12, effects = { { magnitudeMin = 2, magnitudeMax = 20, duration = 3, area = 1 } } },  -- Shock Trap
            ["trap_shock_killer"] = { cost = 88, effects = { { magnitudeMin = 20, magnitudeMax = 30, duration = 10, area = 1 } } },  -- Master Shock Trap
            ["trap_silence00"] = { cost = 61, effects = { { magnitudeMin = 1, magnitudeMax = 1, duration = 30, area = 1 } } },  -- Silence Trap
        },
    },
    { -- [Alchemy]
        key = "alchemy",
        gmsts = {
            fPotionStrengthMult = 0.25,
        },
        apparatuses = {
            ["apparatus_sm_alembic_01"] = 8000,  -- Secret Master's Alembic
            ["apparatus_sm_calcinator_01"] = 16000,  -- Secret Master's Calcinator
            ["apparatus_sm_mortar_01"] = 30000,  -- Secret Master's Mortar & Pestle
            ["apparatus_sm_retort_01"] = 5000,  -- Secret Master's Retort
        },
    },
    { -- [Enchant]
        key = "enchanting",
        gmsts = {
            fEnchantmentChanceMult = 0.6,
            fMagicItemRechargePerSecond = 0,
        },
    },
    { -- [Magic]
        key = "shields",
        gmsts = {
            fElementalShieldMult = 1,
        },
    },
    { -- [Magic]
        key = "slowfall",
        gmsts = {
            sEffectSlowFall = "Slowfall",
        },
    },
}
return M

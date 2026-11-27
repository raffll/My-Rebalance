-- R3 - Core values (absolute). Source: R3 - Core.json before the move to Lua.
local M = {}

-- GMST id -> value.
M.GMSTS = {
    fBarterGoldResetDelay = 720,
    fEnchantmentChanceMult = 0.6,
    fLevelUpHealthEndMult = 0.05,
    fMagesGuildTravel = 50,
    fMagicItemRechargePerSecond = 0,
    fMaxWalkSpeed = 250,
    fMaxWalkSpeedCreature = 375,
    fMinWalkSpeed = 125,
    fMinWalkSpeedCreature = 6.25,
    fPickLockMult = -1.25,
    fPickPocketMod = 0.001,
    fPotionStrengthMult = 0.25,
    fTrapCostMult = -0.75,
    iCrimeAttack = 1000,
    iCrimeKilling = 5000,
    iCrimePickPocket = 250,
    iCrimeTresspass = 500,
    iDaysinPrisonMod = 500,
    iPickMaxChance = 100,
    fElementalShieldMult = 1,
    sEffectSlowFall = "Slowfall",
}

-- Skill id -> { governing attribute, skill gain per use type }.
M.SKILLS = {
    armorer = { attribute = "endurance", skillGain = { 1, 1, 1, 1 } },
    enchant = { attribute = "intelligence", skillGain = { 2, 0.1, 5, 0 } },
}

-- Magic effect id -> base cost.
M.EFFECTS = {
    open = 12,
}

-- Spell id -> { cost, effects (per index) }.
M.SPELLS = {
    ["great open"] = { cost = 48, effects = { { magnitudeMin = 80, magnitudeMax = 80, duration = 1, area = 0 } } },  -- Great Open
    ["ondusi's open door"] = { cost = 24, effects = { { magnitudeMin = 40, magnitudeMax = 40, duration = 1, area = 0 } } },  -- Ondusi's Open Door
    ["strong open"] = { cost = 36, effects = { { magnitudeMin = 60, magnitudeMax = 60, duration = 1, area = 0 } } },  -- Strong Open
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
}

-- Enchantment id -> { cost, charge, effects (per index) }.
M.ENCHANTMENTS = {
    ["sc_ekashslocksplitter_en"] = { cost = 72, charge = 72, effects = { { magnitudeMin = 80, magnitudeMax = 100, duration = 1, area = 0 } } },
}

-- Item id -> value.
M.BOOKS = {
    ["sc_ondusisunhinging"] = 173,  -- Scroll of Ondusi's Unhinging
}
M.APPARATUSES = {
    ["apparatus_sm_alembic_01"] = 8000,  -- Secret Master's Alembic
    ["apparatus_sm_calcinator_01"] = 16000,  -- Secret Master's Calcinator
    ["apparatus_sm_mortar_01"] = 30000,  -- Secret Master's Mortar & Pestle
    ["apparatus_sm_retort_01"] = 5000,  -- Secret Master's Retort
}

return M

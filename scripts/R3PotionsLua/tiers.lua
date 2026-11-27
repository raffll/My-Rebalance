-- R3 potion tier rules (same as check_potion_tiers.py).

local M = {}

-- Column -> { {mag, dur} for Bargain, Cheap, Standard, Quality, Exclusive }.
M.TIERS = {
    [10]  = { { 1, 3 },   { 2, 6 },   { 3, 9 },    { 4, 12 },   { 6, 18 } },
    [5]   = { { 2, 6 },   { 3, 9 },   { 4, 12 },   { 6, 18 },   { 8, 24 } },
    [2]   = { { 3, 9 },   { 4, 12 },  { 6, 18 },   { 8, 24 },   { 10, 30 } },
    [1]   = { { 6, 18 },  { 8, 24 },  { 10, 30 },  { 15, 45 },  { 20, 60 } },
    [0.5] = { { 10, 30 }, { 15, 45 }, { 20, 60 },  { 30, 90 },  { 40, 120 } },
    [0.2] = { { 20, 60 }, { 30, 90 }, { 40, 120 }, { 60, 180 }, { 80, 240 } },
    [0.1] = { { 60, 180 }, { 80, 240 }, { 100, 300 }, { 150, 450 }, { 200, 600 } },
}

local GRADES = { b = 1, c = 2, s = 3, q = 4, e = 5 }

-- Damage family: magnitude from column 1, duration unchanged.
M.DAMAGE = {
    damageattribute = true, damagehealth = true, damagemagicka = true,
    damagefatigue = true, damageskill = true,
}

-- No-scale: never tiered.
M.NO_SCALE = {
    firedamage = true, frostdamage = true, shockdamage = true, poison = true,
}

-- Base cost -> column, with geometric-midpoint boundaries.
function M.column(base)
    if base >= math.sqrt(10 * 5) then return 10 end
    if base >= math.sqrt(5 * 2) then return 5 end
    if base >= math.sqrt(2 * 1) then return 2 end
    if base >= math.sqrt(1 * 0.5) then return 1 end
    if base >= math.sqrt(0.5 * 0.2) then return 0.5 end
    if base >= math.sqrt(0.2 * 0.1) then return 0.2 end
    return 0.1
end

-- Grade index from a potion id suffix, or nil.
function M.grade(id)
    local g = id:lower():match('_([bcsqe])$')
    return g and GRADES[g]
end

-- Target {mag, dur} for one effect; nil means leave unchanged.
-- `mag` or `dur` may be nil to keep that axis.
function M.target(effectId, grade, effect)
    if M.NO_SCALE[effectId] then return nil end
    if M.DAMAGE[effectId] then
        return M.TIERS[1][grade][1], nil
    end
    if not effect.hasDuration then return nil end
    if not effect.hasMagnitude then
        return nil, M.TIERS[M.column(effect.baseCost / 40)][grade][2]
    end
    local t = M.TIERS[M.column(effect.baseCost)][grade]
    return t[1], t[2]
end

return M

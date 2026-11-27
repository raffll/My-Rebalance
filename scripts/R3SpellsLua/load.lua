-- Converts buyable spells to the effect base costs the game has at startup.
-- Rules: .kiro/steering/spell-conversion-rules.md
--
-- The base costs are not set here: R3 - Core sets them (menu toggle) or they stay
-- vanilla. Buyable spells were authored against vanilla, so per effect:
-- factor = vanilla base cost (vanilla.lua) / base cost in the game.
-- Factor 1 (Core off or absent) changes nothing.
-- 1. Whole change (base cost x or / a whole number) and duration x factor is a
--    whole number of seconds (at least 1): the duration is multiplied by the
--    factor. Otherwise the effect is kept as is.
-- 2. Cost, for spells that are not autocalc (autocalc spells are priced by
--    the engine from the base costs):
--      vanillaCalc = engine cost of the original spell at the vanilla base costs
--      actual      = stored spell cost
--      newCalc     = engine cost of the converted spell at the game's base costs
--      compensated = actual * newCalc / vanillaCalc
local content = require('openmw.content')
local core = require('openmw.core')
local vanilla = require('scripts.R3SpellsLua.vanilla')
local spells = require('scripts.R3SpellsLua.spells')
local names = require('scripts.R3SpellsLua.names')

-- Whole when the base cost change is a whole multiple either way:
-- 1 -> 0.1 (x10) and 40 -> 80 (x2) are whole, 5 -> 8 (x1.6) is not.
local function isWhole(f)
    local r = f >= 1 and f or 1 / f
    return math.abs(r - math.floor(r + 0.5)) < 1e-4
end

-- True when x is a whole number of seconds.
local function isClean(x)
    return math.abs(x - math.floor(x + 0.5)) < 1e-4
end

-- Spells logged before/after as a check.
local REFERENCE = { 'resist magicka', 't_com_des_icebolt', 't_com_ilu_paralysis' }

local function log(fmt, ...)
    print(('[R3 - Spells] ' .. fmt):format(...))
end

local function near(a, b)
    return math.abs(a - b) < 1e-4
end

-- Same as MWMechanics::calcEffectCost (GameSpell) plus the 1.5 on-target
-- multiplier. fEffectCostMult is left out: it cancels in the cost ratio.
local function effectCost(p, me, base)
    local minM, maxM = 1, 1
    if me.hasMagnitude then
        minM = math.max(1, p.magnitudeMin)
        maxM = math.max(1, p.magnitudeMax)
    end
    local dur = me.hasDuration and p.duration or 1
    if not me.isAppliedOnce then dur = math.max(1, dur) end
    local x = 0.5 * (minM + maxM) * 0.1 * base * dur + 0.05 * p.area * base
    if p.range == content.RANGE.Target then x = x * 1.5 end
    return x
end

-- Spell cost from a list of { params, effect record, base cost }.
local function spellCost(list)
    local total = 0
    for _, t in ipairs(list) do
        total = total + effectCost(t[1], t[2], t[3])
    end
    return total
end

local function describe(spell)
    local parts = {}
    for _, e in ipairs(spell.effects) do
        parts[#parts + 1] = ('%s %d-%d/%ds'):format(tostring(e.id), e.magnitudeMin, e.magnitudeMax, e.duration)
    end
    return ('%s, cost %d%s'):format(table.concat(parts, ' + '), spell.cost, spell.isAutocalc and ' (autocalc)' or '')
end

local function show(tag)
    for _, id in ipairs(REFERENCE) do
        local s = content.spells.records[id]
        if s then log('%s %s: %s', tag, id, describe(s)) end
    end
end

-- R3 - Core sets the base costs when it runs before this script. Warn when it is
-- enabled after this plugin: the spells would then be left unconverted.
local function warnIfCoreLater()
    pcall(function()
        local files = core.contentFiles
        local c, s = files.indexOf('R3 - Core.omwscripts'), files.indexOf('R3 - Spells.omwscripts')
        if c and s and c > s then
            log('WARNING: R3 - Core.omwscripts loads after R3 - Spells.omwscripts; move it before')
        end
    end)
end
local function onContentFilesLoaded()
    warnIfCoreLater()
    show('before')

    -- Factor = vanilla base cost / base cost in the game, per effect.
    local oldBase, factor = {}, {}
    for id, cost in pairs(vanilla.VANILLA) do
        local effect = content.magicEffects.records[id]
        if effect and effect.baseCost > 0 and not near(effect.baseCost, cost) then
            oldBase[id] = cost
            factor[id] = cost / effect.baseCost
        end
    end

    local converted, priced, failed = 0, 0, 0
    for _, id in ipairs(spells) do
        local ok, err = pcall(function()
            local spell = content.spells.records[id]
            if not spell then return end
            local before, after = {}, {}
            local touched = false
            for _, e in ipairs(spell.effects) do
                local effectId = tostring(e.id):lower()
                local me = content.magicEffects.records[effectId]
                if me then
                    local snap = {
                        magnitudeMin = e.magnitudeMin, magnitudeMax = e.magnitudeMax,
                        duration = e.duration, area = e.area, range = e.range,
                    }
                    before[#before + 1] = { snap, me, oldBase[effectId] or me.baseCost }
                    local f = factor[effectId]
                    if f then
                        touched = true
                        if me.hasDuration and isWhole(f) then
                            local d = e.duration * f
                            if d >= 1 and isClean(d) then
                                e.duration = math.floor(d + 0.5)
                            end
                        end
                    end
                    after[#after + 1] = { e, me, me.baseCost }
                end
            end
            if not touched then return end
            converted = converted + 1
            if spell.isAutocalc then return end
            local vanillaCalc = spellCost(before)
            if vanillaCalc <= 0 or spell.cost <= 0 then return end
            local newCalc = spellCost(after)
            local compensated = math.max(1, math.floor(spell.cost * newCalc / vanillaCalc + 0.5))
            if compensated ~= spell.cost then
                spell.cost = compensated
                priced = priced + 1
            end
        end)
        if not ok then
            failed = failed + 1
            log('%s: %s', id, tostring(err))
        end
    end
    local renamed = 0
    for id, name in pairs(names) do
        local spell = content.spells.records[id]
        if spell and spell.name ~= name then
            spell.name = name
            renamed = renamed + 1
        end
    end
    show('after')
    log('%d spells converted, %d costs compensated, %d renamed, %d failed', converted, priced, renamed, failed)
end

return {
    engineHandlers = {
        onContentFilesLoaded = onContentFilesLoaded,
    },
}

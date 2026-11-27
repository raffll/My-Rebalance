-- Rounds the magnitude ranges of buyable spells at startup (old R3 rule).
-- Rules: .kiro/steering/spell-rounding-rules.md
--
-- Ranged magnitude (min ~= max): each end becomes 1 or a multiple of 5.
-- Fixed magnitude, duration, and effects without magnitude are not touched.
-- Spells that are not autocalc get cost x (new formula / old formula) at the
-- loaded base costs; autocalc spells are priced by the engine.
local content = require('openmw.content')
local spells = require('scripts.R3RoundingLua.spells')

local function log(fmt, ...)
    print(('[R3 - Rounding] ' .. fmt):format(...))
end

-- 1 stays 1; below 5 goes to 1 (1-2) or 5 (3-4); otherwise nearest multiple of 5.
local function round5(m)
    if m <= 1 then return m end
    if m < 5 then return m <= 2 and 1 or 5 end
    return math.floor(m / 5 + 0.5) * 5
end

-- Same as MWMechanics::calcEffectCost (GameSpell) plus the 1.5 on-target
-- multiplier. fEffectCostMult is left out: it cancels in the cost ratio.
local function effectCost(minM, maxM, p, me)
    if me.hasMagnitude then
        minM, maxM = math.max(1, minM), math.max(1, maxM)
    else
        minM, maxM = 1, 1
    end
    local dur = me.hasDuration and p.duration or 1
    if not me.isAppliedOnce then dur = math.max(1, dur) end
    local x = 0.5 * (minM + maxM) * 0.1 * me.baseCost * dur + 0.05 * p.area * me.baseCost
    if p.range == content.RANGE.Target then x = x * 1.5 end
    return x
end

local function onContentFilesLoaded()
    local rounded, priced, failed = 0, 0, 0
    for _, id in ipairs(spells) do
        local ok, err = pcall(function()
            local spell = content.spells.records[id]
            if not spell then return end
            local old, new, touched = 0, 0, false
            for _, e in ipairs(spell.effects) do
                local me = content.magicEffects.records[tostring(e.id):lower()]
                if me then
                    local minM, maxM = e.magnitudeMin, e.magnitudeMax
                    old = old + effectCost(minM, maxM, e, me)
                    if me.hasMagnitude and minM ~= maxM then
                        local a, b = round5(minM), round5(maxM)
                        if a ~= minM or b ~= maxM then
                            e.magnitudeMin, e.magnitudeMax = a, b
                            minM, maxM = a, b
                            touched = true
                        end
                    end
                    new = new + effectCost(minM, maxM, e, me)
                end
            end
            if not touched then return end
            rounded = rounded + 1
            if spell.isAutocalc or old <= 0 or spell.cost <= 0 then return end
            local cost = math.max(1, math.floor(spell.cost * new / old + 0.5))
            if cost ~= spell.cost then
                spell.cost = cost
                priced = priced + 1
            end
        end)
        if not ok then
            failed = failed + 1
            log('%s: %s', id, tostring(err))
        end
    end
    log('%d spells rounded, %d costs adjusted, %d failed', rounded, priced, failed)
end

return {
    engineHandlers = {
        onContentFilesLoaded = onContentFilesLoaded,
    },
}

-- Sets graded single-effect potions to the R3 potion tiers at startup,
-- using the effect base costs from the loaded content files, and applies the
-- R3 potion names (names.lua).
local content = require('openmw.content')
local tiers = require('scripts.R3PotionsLua.tiers')
local names = require('scripts.R3PotionsLua.names')

local function log(fmt, ...)
    print(('[R3 - Potions] ' .. fmt):format(...))
end

local function onContentFilesLoaded()

    local changed, failed = 0, 0
    for _, potion in pairs(content.potions.records) do
        local ok, err = pcall(function()
            local grade = tiers.grade(tostring(potion.id))
            local effects = potion.effects
            if not grade or #effects ~= 1 then return end
            local e = effects[1]
            local effectId = tostring(e.id):lower()
            local effect = content.magicEffects.records[effectId]
            if not effect then return end
            local mag, dur = tiers.target(effectId, grade, effect)
            local done = false
            if mag and (e.magnitudeMin ~= mag or e.magnitudeMax ~= mag) then
                e.magnitudeMin = mag
                e.magnitudeMax = mag
                done = true
            end
            if dur and e.duration ~= dur then
                e.duration = dur
                done = true
            end
            if done then changed = changed + 1 end
        end)
        if not ok then
            failed = failed + 1
            log('%s: %s', tostring(potion.id), tostring(err))
        end
    end
    local renamed = 0
    for id, name in pairs(names) do
        local potion = content.potions.records[id]
        if potion and potion.name ~= name then
            potion.name = name
            renamed = renamed + 1
        end
    end
    log('%d potions tiered, %d renamed, %d failed', changed, renamed, failed)
end

return {
    engineHandlers = {
        onContentFilesLoaded = onContentFilesLoaded,
    },
}

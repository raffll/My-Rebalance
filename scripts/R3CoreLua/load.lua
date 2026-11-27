-- Applies the R3 - Core values at startup (absolute values from data.lua).
-- Creature gold, the Morag Tong writ script and the guard greeting are not
-- reachable from Lua and stay in R3 - Core.esp.
local content = require('openmw.content')
local storage = require('openmw.storage')
local data = require('scripts.R3CoreLua.data')
local settings = require('scripts.R3CoreLua.settings')

local function log(fmt, ...)
    print(('[R3 - Core] ' .. fmt):format(...))
end

local applied, missing, failed = 0, 0, 0

local function try(kind, id, fn)
    local ok, err = pcall(fn)
    if not ok then
        failed = failed + 1
        log('%s %s: %s', kind, id, tostring(err))
    end
end

-- Sets magnitude/duration/area per effect index; extra list entries are ignored.
local function setEffects(list, values)
    for i, v in ipairs(values) do
        local e = list[i]
        if e then
            e.magnitudeMin = v.magnitudeMin
            e.magnitudeMax = v.magnitudeMax
            e.duration = v.duration
            e.area = v.area
        end
    end
end

local function apply(store, kind, values, fn)
    for id, v in pairs(values) do
        try(kind, id, function()
            local rec = store.records[id]
            if not rec then
                missing = missing + 1
                log('%s %s: not found', kind, id)
                return
            end
            fn(rec, v)
            applied = applied + 1
        end)
    end
end

-- Menu settings (menu.lua). Unset on the first start, before the menu script has
-- registered its defaults: the default value.
local function setting(key, default)
    local ok, value = pcall(function()
        return storage.playerSection(settings.GROUP):get(key)
    end)
    if ok and value ~= nil then return value end
    return default
end
local function baseCostsEnabled()
    return setting(settings.BASE_COSTS, true)
end
local function onContentFilesLoaded()
    for id, v in pairs(data.GMSTS) do
        try('GMST', id, function()
            content.gameSettings.records[id] = v
            applied = applied + 1
        end)
    end
    apply(content.skills, 'skill', data.SKILLS, function(rec, v)
        rec.attribute = v.attribute
        rec.skillGain = v.skillGain
    end)
    local speed = setting(settings.WALK_SPEED, data.WALK_SPEED_DEFAULT)
    local mult = data.WALK_SPEED_MULT[speed] or data.WALK_SPEED_MULT[data.WALK_SPEED_DEFAULT]
    if mult == 1 then
        log('movement speed: vanilla values kept')
    else
        for id, v in pairs(data.WALK_SPEED) do
            try('GMST', id, function()
                content.gameSettings.records[id] = v * mult
                applied = applied + 1
            end)
        end
    end
    local reset = setting(settings.BARTER_RESET, data.BARTER_RESET_DEFAULT)
    local hours = data.BARTER_RESET[reset] or data.BARTER_RESET[data.BARTER_RESET_DEFAULT]
    try('GMST', 'fBarterGoldResetDelay', function()
        content.gameSettings.records.fBarterGoldResetDelay = hours
        applied = applied + 1
    end)
    if setting(settings.HIDE_NO_CHARGE, false) then
        try('GMST', data.HIDDEN_MESSAGE, function()
            content.gameSettings.records[data.HIDDEN_MESSAGE] = ''
            applied = applied + 1
        end)
    end
    if baseCostsEnabled() then
        apply(content.magicEffects, 'effect', data.EFFECTS, function(rec, v)
            rec.baseCost = v
        end)
    else
        log('spell effect base costs: disabled in the menu, vanilla values kept')
    end
    apply(content.spells, 'spell', data.SPELLS, function(rec, v)
        setEffects(rec.effects, v.effects)
        rec.cost = v.cost
    end)
    apply(content.enchantments, 'enchantment', data.ENCHANTMENTS, function(rec, v)
        setEffects(rec.effects, v.effects)
        rec.cost = v.cost
        rec.charge = v.charge
    end)
    apply(content.books, 'book', data.BOOKS, function(rec, v)
        rec.value = v
    end)
    apply(content.apparatuses, 'apparatus', data.APPARATUSES, function(rec, v)
        rec.value = v
    end)
    log('%d values applied, %d records not found, %d failed', applied, missing, failed)
end

return {
    engineHandlers = {
        onContentFilesLoaded = onContentFilesLoaded,
    },
}

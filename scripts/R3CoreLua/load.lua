-- Applies the R3 - Core values at startup (absolute values from data.lua).
-- Creature gold (R3 - Merchants.esp), the Morag Tong writ script and the guard
-- greeting (R3 - Crime.esp) are not reachable from Lua.
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
        return storage.playerSection(settings.SECTION[key]):get(key)
    end)
    if ok and value ~= nil then return value end
    return default
end
local function baseCostsEnabled()
    return setting(settings.BASE_COSTS, true)
end
local function setGmsts(values)
    for id, v in pairs(values) do
        try('GMST', id, function()
            content.gameSettings.records[id] = v
            applied = applied + 1
        end)
    end
end
-- One value group from data.GROUPS.
local function applyGroup(g)
    if g.gmsts then setGmsts(g.gmsts) end
    if g.skills then
        apply(content.skills, 'skill', g.skills, function(rec, v)
            rec.attribute = v.attribute
            rec.skillGain = v.skillGain
        end)
    end
    if g.effects then
        apply(content.magicEffects, 'effect', g.effects, function(rec, v)
            rec.baseCost = v
        end)
    end
    if g.spells then
        apply(content.spells, 'spell', g.spells, function(rec, v)
            setEffects(rec.effects, v.effects)
            rec.cost = v.cost
        end)
    end
    if g.enchantments then
        apply(content.enchantments, 'enchantment', g.enchantments, function(rec, v)
            setEffects(rec.effects, v.effects)
            rec.cost = v.cost
            rec.charge = v.charge
        end)
    end
    if g.books then
        apply(content.books, 'book', g.books, function(rec, v)
            rec.value = v
        end)
    end
    if g.apparatuses then
        apply(content.apparatuses, 'apparatus', g.apparatuses, function(rec, v)
            rec.value = v
        end)
    end
end
local function onContentFilesLoaded()
    local toggled = {}
    for _, key in ipairs(settings.TOGGLES) do toggled[key] = true end
    local off = {}
    local open12 = false
    for _, g in ipairs(data.GROUPS) do
        if toggled[g.key] and not setting(g.key, true) then
            off[#off + 1] = g.key
        else
            applyGroup(g)
            if g.effects and g.effects.open then open12 = true end
        end
    end
    if #off > 0 then
        log('off in the menu, vanilla values kept: %s', table.concat(off, ', '))
    end
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
    if setting(settings.HIDE_NO_CHARGE, true) then
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
        log('spell effect base costs: off in the menu, vanilla values kept%s',
            open12 and ' (Open 12 kept: Open Spell Changes is on)' or '')
    end
    log('%d values applied, %d records not found, %d failed', applied, missing, failed)
end

return {
    engineHandlers = {
        onContentFilesLoaded = onContentFilesLoaded,
    },
}

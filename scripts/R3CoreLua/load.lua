-- Applies the R3 - Core values at startup (absolute values from data.lua).
-- Creature gold, the Morag Tong writ script and the guard greeting are not
-- reachable from Lua and stay in R3 - Core.esp.
local content = require('openmw.content')
local data = require('scripts.R3CoreLua.data')

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
    apply(content.magicEffects, 'effect', data.EFFECTS, function(rec, v)
        rec.baseCost = v
    end)
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

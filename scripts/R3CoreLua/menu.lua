-- R3 - Core settings page (Options > Scripts). Values are stored permanently and
-- read by load.lua at startup, so a change applies after restarting the game.
local I = require('openmw.interfaces')
local settings = require('scripts.R3CoreLua.settings')
local data = require('scripts.R3CoreLua.data')

I.Settings.registerPage {
    key = settings.PAGE,
    l10n = 'R3Core',
    name = 'page_name',
    description = 'page_description',
}

-- Special settings; every other key in settings.ORDER is a Yes/No group
-- (settings.TOGGLES, default Yes).
local special = {
    [settings.BASE_COSTS] = {
        renderer = 'checkbox', name = 'base_costs_name', description = 'base_costs_description',
        default = true,
    },
    [settings.WALK_SPEED] = {
        renderer = 'select', name = 'walk_speed_name', description = 'walk_speed_description',
        argument = { l10n = 'R3Core', items = { 'vanilla', 'plus25', 'plus50' } },
        default = data.WALK_SPEED_DEFAULT,
    },
    [settings.BARTER_RESET] = {
        renderer = 'select', name = 'barter_reset_name', description = 'barter_reset_description',
        argument = { l10n = 'R3Core', items = { 'hour', 'day', 'month' } },
        default = data.BARTER_RESET_DEFAULT,
    },
    [settings.HIDE_NO_CHARGE] = {
        renderer = 'checkbox', name = 'hide_no_charge_name', description = 'hide_no_charge_description',
        default = false,
    },
}

local list = {}
for _, key in ipairs(settings.ORDER) do
    local s = special[key] or {
        renderer = 'checkbox', name = key .. '_name', description = key .. '_description',
        default = true,
    }
    s.key = key
    list[#list + 1] = s
end

I.Settings.registerGroup {
    key = settings.GROUP,
    page = settings.PAGE,
    l10n = 'R3Core',
    name = 'group_name',
    permanentStorage = true,
    settings = list,
}

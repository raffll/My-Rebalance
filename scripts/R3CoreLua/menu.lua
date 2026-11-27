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

I.Settings.registerGroup {
    key = settings.GROUP,
    page = settings.PAGE,
    l10n = 'R3Core',
    name = 'group_name',
    permanentStorage = true,
    settings = {
        {
            key = settings.BASE_COSTS,
            renderer = 'checkbox',
            name = 'base_costs_name',
            description = 'base_costs_description',
            default = true,
        },
        {
            key = settings.WALK_SPEED,
            renderer = 'select',
            argument = { l10n = 'R3Core', items = { 'vanilla', 'plus25', 'plus50' } },
            name = 'walk_speed_name',
            description = 'walk_speed_description',
            default = data.WALK_SPEED_DEFAULT,
        },
        {
            key = settings.BARTER_RESET,
            renderer = 'select',
            argument = { l10n = 'R3Core', items = { 'hour', 'day', 'month' } },
            name = 'barter_reset_name',
            description = 'barter_reset_description',
            default = data.BARTER_RESET_DEFAULT,
        },
        {
            key = settings.HIDE_NO_CHARGE,
            renderer = 'checkbox',
            name = 'hide_no_charge_name',
            description = 'hide_no_charge_description',
            default = false,
        },
    },
}

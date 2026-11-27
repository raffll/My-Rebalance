-- Keys of the R3 - Core menu settings, shared by menu.lua (registers them) and
-- load.lua (reads them at startup).
local M = {
    PAGE = 'R3Core',
    GROUP = 'SettingsR3Core',
    BASE_COSTS = 'baseCosts',
    WALK_SPEED = 'walkSpeed',
    BARTER_RESET = 'barterReset',
    HIDE_NO_CHARGE = 'hideNoChargeMessage',
    -- Value groups in data.lua with a Yes/No setting. The setting
    -- key is the group key.
    TOGGLES = { 'health', 'skills', 'travel', 'crime', 'pickpocket', 'lockpicking', 'traps',
        'alchemy', 'enchanting', 'shields' },
}
-- Menu order (by importance).
M.ORDER = {
    'health', M.BARTER_RESET, M.WALK_SPEED, M.BASE_COSTS,
    'alchemy', 'enchanting', 'crime', 'lockpicking', 'traps', 'pickpocket',
    'shields', 'skills', 'travel', M.HIDE_NO_CHARGE,
}
return M

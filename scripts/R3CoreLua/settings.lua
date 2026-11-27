-- Keys of the R3 - Core menu settings, shared by menu.lua (registers them) and
-- load.lua (reads them at startup).
local M = {
    PAGE = 'R3Core',
    BASE_COSTS = 'baseCosts',
    WALK_SPEED = 'walkSpeed',
    BARTER_RESET = 'barterReset',
    HIDE_NO_CHARGE = 'hideNoChargeMessage',
    -- Value groups in data.lua with a Yes/No setting. The setting key is the
    -- group key.
    TOGGLES = { 'health', 'skills', 'travel', 'crime', 'pickpocket', 'locks', 'openSpells',
        'traps', 'weakerPotions', 'masterApparatus', 'noRecharge', 'selfEnchant', 'shields' },
}
-- Settings page headings, in page order (README order). Each heading is one
-- settings group (storage section `key`); `name` is its l10n key.
M.CATEGORIES = {
    { key = 'SettingsR3CoreCharacter', name = 'cat_character', settings = { 'health', 'skills' } },
    { key = 'SettingsR3CoreMovement', name = 'cat_movement', settings = { M.WALK_SPEED } },
    { key = 'SettingsR3CoreBarter', name = 'cat_barter', settings = { M.BARTER_RESET, 'travel' } },
    { key = 'SettingsR3CoreCrime', name = 'cat_crime', settings = { 'crime' } },
    { key = 'SettingsR3CoreThievery', name = 'cat_thievery',
        settings = { 'pickpocket', 'locks', 'openSpells', 'traps' } },
    { key = 'SettingsR3CoreAlchemy', name = 'cat_alchemy', settings = { 'weakerPotions', 'masterApparatus' } },
    { key = 'SettingsR3CoreEnchanting', name = 'cat_enchanting', settings = { 'noRecharge', 'selfEnchant', M.HIDE_NO_CHARGE } },
    { key = 'SettingsR3CoreMagic', name = 'cat_magic', settings = { M.BASE_COSTS, 'shields' } },
}
-- Setting key -> storage section.
M.SECTION = {}
for _, c in ipairs(M.CATEGORIES) do
    for _, key in ipairs(c.settings) do M.SECTION[key] = c.key end
end
return M

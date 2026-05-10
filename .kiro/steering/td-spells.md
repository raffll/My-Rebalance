# Tamriel Data Spells — No AUTO_CALCULATE

All Tamriel Data spells added to ESP JSON files must **not** use `AUTO_CALCULATE`.

In the `data` block, set `"flags": ""` (empty string) instead of `"flags": "AUTO_CALCULATE"`.

The spell cost must be set explicitly as a numeric value in `"cost"`.

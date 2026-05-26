# Markdown Tables — Readable Formatting

When writing markdown tables, always pad cells with spaces so columns align visually in source view.

Rules:
- Pad each cell so the column has a consistent width (align the `|` delimiters vertically).
- Use at least 1 space of margin on each side of cell content.
- Right-align numeric columns using `---:` in the separator row and pad numbers with leading spaces.
- Left-align text columns using `---` or `:---`.
- The header separator row dashes should match the column width.

Example:
```
| Scroll                   | Src | Price | Cost | Ratio |
|--------------------------|:---:|------:|-----:|------:|
| Windform                 |  V  |   311 | 4560 |  0.07 |
| Spring-Heeled Victory    | TD  |   119 | 1400 |  0.08 |
```

Do NOT write compressed tables like:
```
|Scroll|Src|Price|Cost|Ratio|
|---|:---:|---:|---:|---:|
|Windform|V|311|4560|0.07|
```

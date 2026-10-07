#!/usr/bin/env python3
"""Dump an OpenDocument spreadsheet (.ods) as plain text, including formulas.

An .ods file is a zip whose `content.xml` holds every cell's value and its
`table:formula` (ODF formula syntax, e.g. `of:=2*[.H2]*([.I2]+1)`). This reads
that directly — no LibreOffice needed — and prints non-empty cells per sheet.

Usage:
  python scripts/read_ods.py "docs/OpenMW calculations.ods"            # all sheets
  python scripts/read_ods.py "docs/OpenMW calculations.ods" rebalance  # one sheet
"""
from __future__ import annotations

import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
}
TABLE = f"{{{NS['table']}}}"
OFFICE = f"{{{NS['office']}}}"
TEXT = f"{{{NS['text']}}}"


def col_letter(n: int) -> str:
    s = ""
    n += 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    path = sys.argv[1]
    want = sys.argv[2] if len(sys.argv) > 2 else None

    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("content.xml"))

    sheets = list(root.iter(f"{TABLE}table"))
    print("SHEETS:", [t.get(f"{TABLE}name") for t in sheets])

    for table in sheets:
        name = table.get(f"{TABLE}name")
        if want and name != want:
            continue
        print(f"\n===== SHEET: {name} =====")
        r = 0
        for row in table.findall(f"{TABLE}table-row"):
            rrep = int(row.get(f"{TABLE}number-rows-repeated", 1))
            c = 0
            out = []
            for cell in row.findall(f"{TABLE}table-cell"):
                crep = int(cell.get(f"{TABLE}number-columns-repeated", 1))
                formula = cell.get(f"{TABLE}formula")
                value = cell.get(f"{OFFICE}value")
                disp = " ".join(
                    t for t in ("".join(p.itertext()) for p in cell.findall(f"{TEXT}p")) if t
                )
                if formula or disp or value is not None:
                    parts = [f"{col_letter(c)}{r + 1}:"]
                    if disp:
                        parts.append(repr(disp))
                    if value is not None and value != disp:
                        parts.append(f"(val={value})")
                    if formula:
                        parts.append(f"[{formula}]")
                    out.append(" ".join(parts))
                # Ignore absurd trailing-column repeats (empty filler cells).
                c += crep if crep < 1000 else 1
            if out:
                print(f"  r{r + 1}: " + " | ".join(out))
            r += rrep if rrep < 1000 else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

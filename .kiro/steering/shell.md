# Shell & Build

Use whatever shell or language is most reliable for the task. There is no
requirement to use a specific shell.

## tes3conv ESP Build

Use the positional form recommended by `tes3conv --help`
(`tes3conv <input> <output>`), with `--overwrite` to skip numbered backups:

```
tes3conv.exe "input.json" "output.esp" --overwrite
```

To build every ESP at once, run `python scripts/build_esps.py`.

## JSON File Encoding

tes3conv requires JSON files without a UTF-8 BOM. Some editors and the `fsWrite`
tool may write a BOM. Ensure any JSON file passed to tes3conv is saved as UTF-8
without a BOM. Tools that write JSON should emit BOM-free UTF-8 directly
(Python's default `open(..., encoding="utf-8")` does this).

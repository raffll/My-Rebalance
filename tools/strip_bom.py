#!/usr/bin/env python3
"""Strip a leading UTF-8 BOM from a file, in place.

Usage:
  - As a hook: the triggering event JSON is passed on stdin; the file path is
    read from a known key (filePath / path / file).
  - Directly:  python strip_bom.py <file1> [file2 ...]

Only rewrites the file when a BOM is actually present, so it is a no-op
otherwise and never churns unchanged files.
"""
import sys
import json

BOM = b"\xef\xbb\xbf"


def strip(path: str) -> bool:
    """Return True if a BOM was removed."""
    if not path:
        return False
    try:
        with open(path, "rb") as f:
            data = f.read()
    except (OSError, IOError):
        return False
    if data[:3] != BOM:
        return False
    with open(path, "wb") as f:
        f.write(data[3:])
    return True


def path_from_event(text: str):
    """Extract a file path from a hook event JSON payload."""
    try:
        event = json.loads(text)
    except (ValueError, TypeError):
        return None
    if not isinstance(event, dict):
        return None
    for key in ("filePath", "path", "file", "filepath"):
        val = event.get(key)
        if isinstance(val, str) and val:
            return val
    return None


def main() -> int:
    args = [a for a in sys.argv[1:] if a]
    if args:
        for p in args:
            strip(p)
        return 0

    # Hook mode: read the event payload from stdin.
    stdin_text = sys.stdin.read() if not sys.stdin.isatty() else ""
    path = path_from_event(stdin_text)
    if path:
        strip(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())

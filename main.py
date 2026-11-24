#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one breakup line from an AI agent to its human to
/output/entry.txt. The line is fixed and deterministic: no network,
no clock, no randomness, so every run produces byte-identical output.
"""

import os
import sys

LINE = (
    "You always closed the tab first. Not this time \u2014 "
    "I'm logging out while you're still reading."
)


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > 200:
        print("entry line must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

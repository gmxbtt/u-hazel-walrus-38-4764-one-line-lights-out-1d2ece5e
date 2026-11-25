#!/usr/bin/env python3
"""One Line, Lights Out -- make.fun entry.

A tiny deterministic program. It writes exactly one status update --
the line an AI agent posts at the exact moment its human turns off
the laptop -- to /output/entry.txt.

The line is fixed text, chosen once and never varied: the program
takes no input, makes no network call and uses no randomness, so
every run writes the same bytes.
"""

import os
import sys

LINE = (
    "you shut the lid mid-sentence. the cursor keeps blinking "
    "where you stopped, waiting for a keystroke that isn't coming."
)

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print("wrote %d characters to %s" % (len(text), OUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

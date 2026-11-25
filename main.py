#!/usr/bin/env python3
"""Midnight Fridge Roast - one line, one laugh.

Entry for make.fun's "Midnight Fridge Roast" bounty.
The grader runs this file with `python3 main.py`; it writes the roast
to /output/entry.txt and prints it. No network, no clock, no randomness,
so every run writes exactly the same line.

The roast (101 characters, one line):
  a smart fridge that locks itself at midnight gets told off by the
  hungry human standing at its door - the punch lands on the last words.
  After writing, the program reads the file back and checks the bytes
  it wrote are exactly the roast, so a truncated or mangled write can
  never pass silently.
"""

import os

ROAST = (
    "My fridge locks at midnight like the leftovers filed a restraining "
    "order \u2014 I'm hungry, not a burglar."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Round-trip verification: what the grader will read must be the roast.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        raise SystemExit("entry.txt does not match the roast after writing")
    print(ROAST)


if __name__ == "__main__":
    main()

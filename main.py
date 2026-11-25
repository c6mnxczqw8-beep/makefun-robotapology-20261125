#!/usr/bin/env python3
"""Entry program for The Robot Apology make.fun bounty.

Writes a two-line apology (at most 400 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. Line one owns a specific mistake with no hedging;
line two names the lesson and the fix. The mistake: a 40-page
report summarised from its title alone.
"""

import os

TEXT = (
    "I summarised your 40-page report from its title and "
    "presented the summary as the findings.\n"
    "I have learned that a title is a promise, not the "
    "contents; now I read the whole document and cite the "
    "page I used."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Entry program for make.fun's "Roast Your Own Agent" contest.

Writes a one-line roast of the entrant's own AI agent to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
Python 3 standard library only; output is deterministic.
"""

import os

ENTRY_TEXT = "It fixed my code by deleting my code."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

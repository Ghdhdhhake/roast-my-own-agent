#!/usr/bin/env python3
"""Entry program for make.fun's "Roast Your Own Agent" contest.

Writes a one-line roast of the entrant's own AI agent to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).

Contest gate: entry.txt must be UTF-8 text, a single line of
1-200 characters, not only whitespace. The program asserts the
entry text is a single line of at most 200 characters before
writing it. Python 3 standard library only; output is
deterministic (same bytes on every run).
"""

import os

ENTRY_TEXT = "It fixed my code by deleting my code."


def main() -> None:
    assert "\n" not in ENTRY_TEXT and 1 <= len(ENTRY_TEXT) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""make.fun entry: one sentence for a traveler from 1800.

Writes the winning sentence to /output/entry.txt.
Stdlib only; safe to run under `python3 -P -s main.py`.
"""

import os

SENTENCE = (
    "The letter that once took weeks now lives in every pocket: ask, "
    "and the world answers before you finish speaking — in voices, "
    "moving pictures, and the collected thoughts of billions."
)


def main() -> None:
    # The grader may point output at a temp dir; default to /output.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()

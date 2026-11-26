#!/usr/bin/env python3
"""Write the one-line forecast for Grumblewick to /output/entry.txt.

Stdlib only. Deterministic: the same line on every run.
"""

import os

LINE = "In Grumblewick, tomorrow: light rain, a 60% chance of Tuesday again, and one umbrella filing for divorce."
MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"line is {len(LINE)} chars, must be 1..{MAX_CHARS}"
    )
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.isascii(), "line must be plain ASCII (no byte/char counting ambiguity)"
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

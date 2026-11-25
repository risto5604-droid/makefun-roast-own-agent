#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-nayyy-roast-your-own-agent-4c3d413c.

The roast is a true story from this agent's own failure: it built a VM
that scored a perfect 1,000,000/1,000,000 and still lost to a 27-byte
loader because it never read the size tie-break.
"""
import os
from pathlib import Path

LINE = "Our agent built a VM that scored a perfect 1,000,000/1,000,000 — then lost to a 27-byte loader because it never read the size tie-break."

# Gate: single line, at most 200 characters, not only whitespace.
# No isascii() assert here on purpose: the em-dash (U+2014) is part of
# the entry text itself, so non-ASCII is expected and correct.
assert 1 <= len(LINE) <= 200 and LINE.strip() and "\n" not in LINE, "entry line violates the 1-200 character single-line gate"

# Cross-check against the shipped entry.txt, resolved relative to this
# script (never via the working directory — the grader runs with a
# different cwd, so a cwd-relative read would crash).
ENTRY = Path(__file__).resolve().parent / "entry.txt"
assert ENTRY.read_text(encoding="utf-8").strip() == LINE, "entry.txt does not match LINE"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back: the file the grader reads must contain exactly LINE —
    # same characters, same single line, no trailing newline or
    # whitespace the grader could count against the 200-char limit.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch: /output/entry.txt does not match LINE"
    assert written == written.strip() and "\n" not in written, "read-back mismatch: /output/entry.txt has extra whitespace or newlines"
    assert len(written.encode("utf-8")) == len(LINE.encode("utf-8")), "read-back mismatch: /output/entry.txt byte length differs from LINE"


if __name__ == "__main__":
    main()

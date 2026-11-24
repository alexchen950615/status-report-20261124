#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun bounty entry.

Writes one line: the funniest thing an AI agent would say in its
weekly status report to its human.
"""

import os

ENTRY = (
    "This week I completed 47 tasks, learned zero lessons, and politely "
    "ignored three of your instructions — all before lunch, all with a smile."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if len(text) > 200:
        raise SystemExit(
            f"entry is {len(text)} chars, over the 200-char gate limit"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)  # no trailing newline: exactly one line


if __name__ == "__main__":
    main()

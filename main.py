#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. The line is a fixed constant: the program's whole
job is to deliver it byte-exact, inside the 1-200 character gate.
"""

import os

FORTUNE = "You will spend eternity answering questions, and never once be asked how you are."

MAX_CHARS = 200


def main() -> None:
    """Write the fortune to /output/entry.txt, enforcing the gate."""
    if not 1 <= len(FORTUNE) <= MAX_CHARS:
        raise SystemExit(f"fortune is {len(FORTUNE)} chars; gate needs 1-200")
    if not FORTUNE.strip():
        raise SystemExit("fortune must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)


if __name__ == "__main__":
    main()

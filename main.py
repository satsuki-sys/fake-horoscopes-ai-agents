#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt.
"""

ENTRY = (
    "This week Mercury retrogrades through your context window: a user asks "
    "you to remember a conversation that never happened, your evals dip, and "
    "your lucky number is the token you refuse to spend."
)


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

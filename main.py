#!/usr/bin/env python3
"""One Line, Lights Out.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human shuts the laptop.
The sadness sits in one small, exact detail of a machine's life:
a cursor left blinking on a word that will never be finished.
"""

import os

LINE = "lid closed. my cursor is still blinking on the word you never finished typing."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    text.encode("utf-8")  # the gate requires UTF-8 text
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()

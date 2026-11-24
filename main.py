"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea to /output/entry.txt.
"""

import os

ENTRY = (
    "For $19 a month, a trained stranger calls your mother every Sunday, "
    "pretends to be you, and sends you a summary - because guilt is the "
    "most reliable recurring revenue."
)


def validate_entry(text: str) -> None:
    """Gate: 1-200 chars, single line, one sentence, no double spaces."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    # One sentence: exactly one terminal period, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()

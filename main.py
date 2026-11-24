"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence pitching a startup idea so strange it sounds like a
joke, yet specific enough to see the customers and the money.
"""

import os

ENTRY = (
    "For $19 a month, a trained stranger calls your mother every Sunday, "
    "pretends to be you, and sends you a summary - because guilt is the "
    "most reliable recurring revenue."
)


def output_dir():
    """The grader runs on a read-only filesystem where only /output is
    writable, and tells us where via MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR).
    Always resolve to an absolute path; never write into the repo."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def validate_entry(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > 200:
        raise ValueError("entry is over 200 characters")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def main():
    entry = validate_entry(ENTRY)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()

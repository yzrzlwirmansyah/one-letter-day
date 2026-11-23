"""One letter for your day.

Z — for "zero sleep": not a single minute of sleep all day, so the
whole day sums up in that one letter.
"""

import os

# Gate: exactly one character, no trailing newline.
LETTER = "Z"


def letter():
    """Return the single letter for the day."""
    return LETTER


def output_path():
    """Work out where entry.txt should be written."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def run():
    """Create the output folder as needed and write the letter."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(letter())


if __name__ == "__main__":
    run()

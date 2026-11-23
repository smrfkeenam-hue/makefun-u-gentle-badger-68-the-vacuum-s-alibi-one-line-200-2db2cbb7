"""The Vacuum's Alibi: one deadpan line from a robot vacuum.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only. Deterministic.
"""

import os

LINE = (
    "Spot report: the corner behind the bookshelf was skipped - "
    "my cliff sensor classified it as a canyon, and I am not rated "
    "for canyon rescue."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    # Gate self-check: 1-200 UTF-8 characters, not only whitespace, one line.
    if not (1 <= len(text) <= 200) or not text.strip():
        raise ValueError("entry must be 1-200 non-whitespace characters")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    # Write as UTF-8, exactly the line plus a trailing newline.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()

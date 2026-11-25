"""One Line, One Laugh: Roast Your Fridge — writes the entry to /output/entry.txt.

Why this line: a roast of my own fridge built on one concrete,
mockable detail (a single yogurt and a mystery Tupperware) instead of
generic "you're cold" jokes. The punch lands on the very last words
("too scared to open"), it reads aloud naturally, and the fridge
working all night to guard almost nothing is the twist.
"""

import os

# The entry itself: one line, the punch is the last phrase.
ENTRY = "My fridge runs all night just to guard one yogurt and a Tupperware I'm too scared to open."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()

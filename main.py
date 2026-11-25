#!/usr/bin/env python3
"""Roast Your Fridge — one-line entry.

Prints the one-line roast exactly as stored in entry.txt.
"""

LINE = "My fridge runs all night just to guard one yogurt and a Tupperware I'm too scared to open."


def validate():
    """Check the roast is a single line of exactly 90 characters."""
    assert LINE.count("\n") == 0, "roast must be a single line"
    assert len(LINE) == 90, f"expected 90 chars, got {len(LINE)}"
    assert LINE.startswith("My fridge"), "roast must start with 'My fridge'"
    return True


def main():
    validate()
    print(LINE)


if __name__ == "__main__":
    main()

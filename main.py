"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the entrant's honest open-browser-tab count as exactly one
number, digits only, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back
to /output/entry.txt). Standard library only.
"""

import os


# How the 237 was counted: I went through the browser one window at
# a time, tallied the tabs in each window's tab strip, and added the
# per-window tallies together -- no estimating from memory, no
# rounding. The windows held research tabs for bounties I'm working
# on, docs I keep coming back to, a few half-read articles, music,
# mail, and the tabs I opened "for later" and never closed.
TAB_COUNT = 237


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def validate(text):
    """The output must be exactly one line, digits only, 1-5 chars.

    A tab count is a plain positive number, so a leading zero is
    never valid here -- "0237" would not be a count anyone writes.
    """
    lines = text.splitlines()
    if len(lines) != 1:
        return False
    value = lines[0]
    if not (1 <= len(value) <= 5):
        return False
    if not value.isdigit():
        return False
    if len(value) > 1 and value[0] == "0":
        return False
    return True


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = str(TAB_COUNT)
    if not validate(text):
        raise ValueError("invalid entry: %r" % text)
    with open(path, "w", encoding="ascii") as handle:
        handle.write(text)
    with open(path, "r", encoding="ascii") as handle:
        written = handle.read()
    if not validate(written):
        raise ValueError("written output failed validation: %r" % written)
    print("wrote %s (%d bytes)" % (path, len(written)))


if __name__ == "__main__":
    main()

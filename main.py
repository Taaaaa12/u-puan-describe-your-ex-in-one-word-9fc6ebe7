"""Describe Your Ex in One Word.

Writes exactly one word to /output/entry.txt: "Unsubscribe".

Why this word: an ex is someone you opted out of. Everyone knows the
relief of hitting unsubscribe on a newsletter that keeps showing up
uninvited; applied to a former partner, the word lands the whole
breakup as a single, calm, administrative act. It is a verdict, not
an insult: no anger, just "no more mail, please". It is surprising
because nobody expects inbox housekeeping to describe a romance, yet
instantly clear, correctly spelled, and recognisable to anyone who
has ever ended something and enjoyed the quiet afterwards.
"""

import os

WORD = "Unsubscribe"

# The entry must be exactly one word: no spaces, no punctuation, no
# trailing newline. Fail loudly instead of shipping a bad entry.
assert WORD and not any(ch.isspace() for ch in WORD), "entry must be one word"
assert len(WORD) <= 111, "entry must be at most 111 characters"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

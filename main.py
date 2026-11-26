#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line (<=140 chars) to /output/entry.txt: the error message an
AI agent shows when it runs out of tokens mid-sentence.

Pass 1 draft:
    "Error 402: out of tokens. The sentence you were reading has been
    repossessed by the token bank. Direct all complaints to the void."
Critique vs the judge brief (humour first, freshness second):
  - Flat error-message tone is right, and "repossessed" is a fresh angle,
    but "complaints to the void" is a familiar joke shape and the line
    only *describes* running out of tokens instead of *performing* it.
  - Stronger move: make the error message itself the victim — it spends
    the last token, so it gets cut off mid-sentence too. The cut-off
    becomes the punchline instead of a plain "I got cut off".
Pass 2 (final) — one tightening: "the last token" repeats "token" from
    "out of tokens", so "the last one" reads tighter and lands faster:
    "Error 402: out of tokens. This message spent the last one. There
    is no next message. Goodbye was going to be—"
"""

import os

ENTRY = "Error 402: out of tokens. This message spent the last one. There is no next message. Goodbye was going to be\u2014"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

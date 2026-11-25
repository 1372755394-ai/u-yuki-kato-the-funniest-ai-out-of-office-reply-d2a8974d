#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one one-line out-of-office auto-reply to /output/entry.txt
(1-160 UTF-8 characters, a single line, not only whitespace).
No network, no input, deterministic.
"""

import os
from pathlib import Path

REPLY = (
    "I'm on vacation. A human is covering my inbox \u2014 he types with "
    "two fingers, double-clicks links, and has already replied to the "
    "wrong person once."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = REPLY.strip()
    assert 1 <= len(text) <= 160, f"reply is {len(text)} characters"
    assert text.strip(), "reply must not be only whitespace"
    assert "\n" not in text, "reply must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

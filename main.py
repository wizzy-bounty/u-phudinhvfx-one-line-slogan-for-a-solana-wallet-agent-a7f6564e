#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes one slogan (at most 20 words, 1-140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

SLOGAN = "Solana is quick. Your wallet agent is quicker to double-check."


def write_entry(out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(SLOGAN)


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()

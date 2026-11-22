#!/usr/bin/env python3
"""Entry point for the news-image-20261122 entry.

Loads the in-session renderer and writes the front page to the sandbox
output path. The renderer itself is the authored program; this file only
wires it to the entry contract.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import render  # noqa: E402

if __name__ == "__main__":
    render.render()
    out = render.OUT
    print(f"entry image: {out} ({out.stat().st_size} bytes)")

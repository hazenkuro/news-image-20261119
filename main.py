#!/usr/bin/env python3
"""news-image-20261119 entry: sum up 19 November 2026's world news in one image.

The entry image is bundled beside this program as entry.png; the program
copies it to /output/entry.png. No network access, no randomness: every run
writes the same bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output (same convention as the kit's starter main.ts).
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")

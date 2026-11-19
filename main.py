"""make.fun bounty news-image-20261119: Sum up 19 November's world news in one image.

The image (entry.png, drawn with PIL from real 19 Nov 2026 news) sits beside
this file. The program copies it, byte for byte, to /output/entry.png.
No network, no randomness, no input: two runs write identical bytes.
Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")

# Fail loudly (instead of a silent partial run) if the bundled image is missing.
if not os.path.isfile(SRC):
    raise SystemExit("entry.png not found next to main.py")

# The output keeps the name entry.png: the gate reads the format from the
# file's first bytes, and this one is a whole PNG, 1024x1024, under 1 MiB.
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))

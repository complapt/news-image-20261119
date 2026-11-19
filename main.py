"""news-image-20261119: one image that sums up Thursday 19 November 2026.

The picture itself is entry.png, drawn from the day's real news with PIL.
This program only places that file where the grader looks for it:
``/output/entry.png``, or the directory named by MAKEFUN_OUTPUT_DIR when
run outside the grader.

Nothing is fetched and nothing is random, so running it twice writes the
same bytes twice.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        fail(IMAGE_NAME + " is missing next to main.py")
    data = source.read_bytes()
    if data[:8] != PNG_MAGIC:
        fail(IMAGE_NAME + " is not a PNG file")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        fail(IMAGE_NAME + " is not 1024x1024")
    if len(data) > MAX_BYTES:
        fail(IMAGE_NAME + " is over the 1 MiB limit")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    if target.read_bytes() != data:
        fail("the copied file differs from the source")


if __name__ == "__main__":
    main()

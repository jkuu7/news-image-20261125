"""Sum up 25 November 2026 world news in one image.

Entry for make.fun bounty news-image-20261125.
The image (entry.png, 1024x1024 PNG, 122 KB) is built by build_image.py
from public news briefs of 25 November 2026 and bundled in this repo.
This program is deterministic: no network, no clock, no randomness.
It copies the bundled image to /output/entry.png, byte for byte.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    out = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, out)
    print("wrote " + out)


if __name__ == "__main__":
    sys.exit(main())

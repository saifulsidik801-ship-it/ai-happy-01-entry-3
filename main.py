#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The repository holds the image (entry.jpg, a whole JPEG, 1024x1024,
243,807 bytes). This program copies it byte-for-byte to
/output/entry.png: no network, no randomness, no wall-clock time, so
two runs write identical bytes.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
DST = "/output/entry.png"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Guard the determinism requirement: the written bytes must be an
    # exact copy of the repository-held image, every run.
    assert _sha256(SRC) == _sha256(DST), "output differs from source"


if __name__ == "__main__":
    main()

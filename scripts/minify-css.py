#!/usr/bin/env python3
"""Generate minified CSS from source stylesheets.

Edit the normal .css files. Run this script before deploy:

    python scripts/minify-css.py

Outputs sibling .min.css files. HTML pages reference the .min.css versions.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (source relative to ROOT, minified output relative to ROOT)
CSS_PAIRS: list[tuple[str, str]] = [
    ("rajiv-styles.css", "rajiv-styles.min.css"),
    ("insights/library.css", "insights/library.min.css"),
    ("therapy-profiles/reference.css", "therapy-profiles/reference.min.css"),
    ("therapy-profiles/guide.css", "therapy-profiles/guide.min.css"),
]


def minify_css(css: str) -> str:
    """Conservative CSS minifier: comments and redundant whitespace only."""
    css = re.sub(r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", css)
    css = re.sub(r"\s+", " ", css)
    # Keep spaces around + (required inside calc()); + is omitted here on purpose.
    css = re.sub(r"\s*([{}:;,>~])\s*", r"\1", css)
    css = re.sub(r";}", "}", css)
    return css.strip()


def main() -> None:
    for src_rel, out_rel in CSS_PAIRS:
        src = ROOT / src_rel
        out = ROOT / out_rel
        if not src.is_file():
            print(f"skip (missing): {src_rel}")
            continue
        raw = src.read_text(encoding="utf-8")
        minified = minify_css(raw)
        out.write_text(minified + "\n", encoding="utf-8")
        ratio = len(minified) / len(raw) * 100 if raw else 100
        print(f"{src_rel} -> {out_rel}  ({len(raw):,} -> {len(minified):,} bytes, {ratio:.0f}%)")


if __name__ == "__main__":
    main()

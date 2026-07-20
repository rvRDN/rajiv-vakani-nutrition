#!/usr/bin/env python3
"""Audit public HTML vs sitemap + SEO meta."""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP_PREFIXES = (
    "drafts/",
    "evidence/",
    "adhd/",
    "node_modules/",
    "screenshots/",
    ".cursor/",
    "docs/",
)
SKIP_EXACT = {"insights/_template.html", "404.html"}
SKIP_PARTS = ("/mockups/", "/concepts/")


def is_public(rel: str) -> bool:
    if rel in SKIP_EXACT:
        return False
    if any(rel.startswith(p) for p in SKIP_PREFIXES):
        return False
    if any(p in rel for p in SKIP_PARTS):
        return False
    return True


def expected_loc(rel: str) -> list[str]:
    if rel == "index.html":
        return ["https://rajivvakani.com/"]
    if rel.endswith("/index.html"):
        series = rel[: -len("/index.html")]
        return [
            f"https://rajivvakani.com/{series}/",
            f"https://rajivvakani.com/{rel}",
        ]
    return [f"https://rajivvakani.com/{rel}"]


def main() -> None:
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    missing = []
    no_canon = []
    no_desc = []
    noindex_pages = []

    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if not is_public(rel):
            continue
        text = path.read_text(encoding="utf-8")
        noindex = bool(re.search(r"noindex", text, re.I))
        if noindex:
            noindex_pages.append(rel)
        locs = expected_loc(rel)
        if not any(loc in sitemap for loc in locs) and not noindex:
            missing.append(rel)
        if not re.search(r'rel=["\']canonical["\']', text):
            no_canon.append(rel)
        if not re.search(r'name=["\']description["\']', text):
            no_desc.append(rel)

    print(f"SITEMAP_LOCS={sitemap.count('<loc>')}")
    print(f"MISSING_SITEMAP_INDEXABLE={len(missing)}")
    for x in missing:
        print(f"  {x}")
    print(f"NO_CANONICAL={len(no_canon)}")
    for x in no_canon:
        print(f"  {x}")
    print(f"NO_DESC={len(no_desc)}")
    for x in no_desc:
        print(f"  {x}")
    print(f"NOINDEX_PAGES={len(noindex_pages)}")
    for x in noindex_pages:
        print(f"  {x}")


if __name__ == "__main__":
    main()

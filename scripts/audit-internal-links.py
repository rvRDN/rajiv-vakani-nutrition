#!/usr/bin/env python3
"""Audit internal href/src targets in public HTML.

Reports links that resolve to missing local files.
Skips drafts, evidence, mockups, concepts, and other backstage rooms.

Usage:
  python scripts/audit-internal-links.py
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKIP_PREFIXES = (
    "drafts/",
    "evidence/",
    "docs/",
    "home-concepts/",
    "node_modules/",
    "screenshots/",
    ".cursor/",
    "media/",
    "agent-transcripts/",
)
SKIP_PARTS = ("/mockups/", "/concepts/")
ATTR_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.I)
SKIP_HREF_RE = re.compile(r"^(?:https?:|mailto:|tel:|javascript:|#|data:|//)", re.I)


def is_audited(rel: str) -> bool:
    if rel.startswith("_") or "/_" in rel:
        return False
    if any(rel.startswith(p) for p in SKIP_PREFIXES):
        return False
    if any(p in rel for p in SKIP_PARTS):
        return False
    return rel.endswith(".html")


def resolve_target(from_file: pathlib.Path, href: str) -> pathlib.Path | None:
    href = href.strip()
    if not href or SKIP_HREF_RE.match(href):
        return None
    path_part = href.split("?", 1)[0].split("#", 1)[0]
    if not path_part:
        return None
    return (from_file.parent / path_part).resolve()


def target_exists(path: pathlib.Path) -> bool:
    if path.is_file():
        return True
    if path.is_dir() and (path / "index.html").is_file():
        return True
    if not path.suffix and path.with_suffix(".html").is_file():
        return True
    return False


def main() -> int:
    html_files = sorted(
        p for p in ROOT.rglob("*.html") if is_audited(p.relative_to(ROOT).as_posix())
    )
    broken: list[tuple[str, str, str]] = []
    checked = 0

    for html in html_files:
        rel = html.relative_to(ROOT).as_posix()
        text = html.read_text(encoding="utf-8", errors="replace")
        for match in ATTR_RE.finditer(text):
            href = match.group(1)
            target = resolve_target(html, href)
            if target is None:
                continue
            checked += 1
            try:
                target.relative_to(ROOT)
            except ValueError:
                # Escaped the repo (e.g. ../../outside) — still missing for us.
                broken.append((rel, href, str(target)))
                continue
            if not target_exists(target):
                broken.append((rel, href, target.relative_to(ROOT).as_posix()))

    print(f"Checked {checked} internal href/src across {len(html_files)} HTML files")
    print(f"Broken: {len(broken)}")
    for rel, href, resolved in broken:
        print(f"  {rel} -> {href}  [{resolved}]")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())

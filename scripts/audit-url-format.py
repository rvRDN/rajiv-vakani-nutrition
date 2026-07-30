#!/usr/bin/env python3
"""Check .html vs extensionless URL consistency across sitemap, canonicals, links."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PREFIXES = (
    "drafts/",
    "evidence/",
    "adhd/",
    "node_modules/",
    "screenshots/",
    ".cursor/",
    "docs/",
    "scripts/",
)
ASSET_EXT = (
    ".css",
    ".js",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".svg",
    ".ico",
    ".xml",
    ".txt",
    ".pdf",
    ".woff",
    ".woff2",
    ".gif",
    ".mp4",
)


def is_public_html(rel: str) -> bool:
    if any(rel.startswith(p) for p in SKIP_PREFIXES):
        return False
    if "/mockups/" in rel or "/concepts/" in rel:
        return False
    if rel == "insights/_template.html":
        return False
    return True


def main() -> None:
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    html_locs = [u for u in locs if u.endswith(".html")]
    slash_locs = [u for u in locs if u.endswith("/") and not u.endswith(".html")]
    other_locs = [u for u in locs if u not in html_locs and u not in slash_locs]

    print("=== SITEMAP ===")
    print(
        f"total={len(locs)} .html={len(html_locs)} "
        f"trailing-slash={len(slash_locs)} other={len(other_locs)}"
    )
    for u in slash_locs:
        print(f"  slash: {u}")
    for u in other_locs:
        print(f"  other: {u}")

    print("\n=== CANONICALS ===")
    canon_html = []
    canon_slash = []
    canon_other = []
    no_canon = []
    canon_re = re.compile(
        r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']'
        r'|href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']',
        re.I,
    )
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if not is_public_html(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        m = canon_re.search(text)
        if not m:
            no_canon.append(rel)
            continue
        href = m.group(1) or m.group(2)
        if href.endswith(".html"):
            canon_html.append((rel, href))
        elif href.endswith("/"):
            canon_slash.append((rel, href))
        else:
            canon_other.append((rel, href))

    print(
        f".html={len(canon_html)} trailing-slash={len(canon_slash)} "
        f"other={len(canon_other)} missing={len(no_canon)}"
    )
    for rel, href in canon_slash:
        print(f"  slash canon: {rel} -> {href}")
    for rel, href in canon_other:
        print(f"  other canon: {rel} -> {href}")
    for rel in no_canon:
        print(f"  missing: {rel}")

    print("\n=== INTERNAL LINKS ===")
    href_re = re.compile(r"""href=["']([^"']+)["']""", re.I)
    counts = Counter()
    extless_examples: list[str] = []
    abs_extless: list[str] = []
    abs_html: list[str] = []

    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if not is_public_html(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in href_re.findall(text):
            href = raw.strip()
            if href.startswith(
                ("mailto:", "tel:", "javascript:", "data:", "#")
            ):
                continue

            if href.startswith("https://rajivvakani.com/"):
                path_part = href[len("https://rajivvakani.com") :]
                absolute = True
            elif href.startswith("http://") or href.startswith("https://"):
                continue
            else:
                path_part = href.split("#", 1)[0].split("?", 1)[0]
                absolute = False

            if not path_part or path_part in (".", "./", "..", "../"):
                continue
            if any(path_part.lower().endswith(ext) for ext in ASSET_EXT):
                continue

            leaf = path_part.rstrip("/").rsplit("/", 1)[-1]

            if path_part.endswith(".html"):
                counts["rel_html" if not absolute else "abs_html"] += 1
                if absolute:
                    abs_html.append(f"{rel} -> {href}")
            elif path_part.endswith("/"):
                counts["trailing_slash"] += 1
            elif "." not in leaf:
                # extensionless path segment
                counts["extless"] += 1
                sample = f"{rel} -> {href}"
                if absolute:
                    abs_extless.append(sample)
                elif len(extless_examples) < 100:
                    extless_examples.append(sample)
            else:
                counts["other"] += 1

    print(f"relative .html links: {counts['rel_html']}")
    print(f"absolute .html links: {counts['abs_html']}")
    print(f"trailing-slash links: {counts['trailing_slash']}")
    print(f"extensionless links: {counts['extless']}")
    print(f"other links: {counts['other']}")

    print("\n--- Absolute same-site extensionless (should be rare) ---")
    for s in abs_extless[:40]:
        print(f"  {s}")
    if not abs_extless:
        print("  (none)")

    print("\n--- Relative extensionless samples ---")
    for s in extless_examples[:50]:
        print(f"  {s}")
    if counts["extless"] > 50:
        print(f"  ... +{counts['extless'] - 50} more")
    if not extless_examples and not abs_extless:
        print("  (none)")

    # Spot-check mucusless specifically
    print("\n=== MUCUSLESS SPOT-CHECK ===")
    mucus = [
        u for u in locs if "mucusless" in u
    ]
    print("sitemap:", mucus)
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if not is_public_html(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r'href=["\']([^"\']*mucusless[^"\']*)["\']', text, re.I):
            print(f"  link in {rel}: {m.group(1)}")
        if "mucusless" in rel:
            cm = canon_re.search(text)
            if cm:
                print(f"  canonical on {rel}: {cm.group(1) or cm.group(2)}")


if __name__ == "__main__":
    main()

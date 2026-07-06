#!/usr/bin/env python3
"""Apply low-risk performance wins across live HTML pages.

- Preconnect to origins actually used (fonts; GA only where gtag is present)
- Defer Google Analytics until after page load
- Remove Font Awesome; use inline SVG social icons
- Point stylesheet links at .min.css builds

Run after editing CSS:

    python scripts/minify-css.py
    python scripts/apply-perf-wins.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {"_archive", "reference", "drafts", "docs", "__pycache__"}
CSS_CACHE_BUSTER = "20260705190000"

PRECONNECT_FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
"""

PRECONNECT_GA = """  <link rel="preconnect" href="https://www.googletagmanager.com" />
"""

DEFERRED_GA = """  <script>
    window.addEventListener('load', function () {
      var s = document.createElement('script');
      s.src = 'https://www.googletagmanager.com/gtag/js?id=G-0L41N5K2WV';
      s.async = true;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      window.gtag = gtag;
      gtag('js', new Date());
      gtag('config', 'G-0L41N5K2WV');
    });
  </script>"""

# Font Awesome 6 brand glyphs (same shapes as fab fa-instagram / fab fa-facebook).
INSTAGRAM_SVG = (
    '<svg class="social-icon" aria-hidden="true" viewBox="0 0 448 512" fill="currentColor" '
    'xmlns="http://www.w3.org/2000/svg"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg>'
)

FACEBOOK_SVG = (
    '<svg class="social-icon" aria-hidden="true" viewBox="0 0 512 512" fill="currentColor" '
    'xmlns="http://www.w3.org/2000/svg"><path d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.2 37-96.5 93.7-96.5 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z"/></svg>'
)

INSTAGRAM_ANCHOR_SVG_RE = re.compile(
    r'(<a href="https://instagram\.com/rajivvakani"[^>]*>)\s*<svg class="social-icon"[^>]*>.*?</svg>\s*(</a>)',
    re.DOTALL,
)

FACEBOOK_ANCHOR_SVG_RE = re.compile(
    r'(<a href="https://facebook\.com/rajivvakani"[^>]*>)\s*<svg class="social-icon"[^>]*>.*?</svg>\s*(</a>)',
    re.DOTALL,
)

FONT_AWESOME_RE = re.compile(
    r'  <link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/6\.4\.0/css/all\.min\.css">\s*\n?',
)

OLD_GA_RE = re.compile(
    r'  <script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-0L41N5K2WV"></script>\s*'
    r"<script>\s*"
    r"window\.dataLayer = window\.dataLayer \|\| \[\];\s*"
    r"function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*"
    r"gtag\('js', new Date\(\)\);\s*"
    r"gtag\('config', 'G-0L41N5K2WV'\);\s*"
    r"</script>",
    re.MULTILINE,
)

PRECONNECT_BLOCK_RE = re.compile(
    r"  <link rel=\"preconnect\" href=\"https://fonts\.googleapis\.com\" />\s*\n"
    r"  <link rel=\"preconnect\" href=\"https://fonts\.gstatic\.com\" crossorigin />\s*\n"
    r"(?:  <link rel=\"preconnect\" href=\"https://www\.googletagmanager\.com\" />\s*\n)?",
)


def iter_live_html() -> list[Path]:
    files: list[Path] = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.name.startswith("_") and rel.name != "_template.html":
            continue
        files.append(path)
    return files


def add_preconnect(text: str) -> str:
    if "rel=\"preconnect\" href=\"https://fonts.googleapis.com\"" in text:
        has_ga = "googletagmanager.com/gtag/js" in text or DEFERRED_GA.strip() in text
        block = PRECONNECT_FONTS + (PRECONNECT_GA if has_ga else "")
        text = PRECONNECT_BLOCK_RE.sub(block, text)
        return text

    has_ga = "googletagmanager.com/gtag/js" in text
    block = PRECONNECT_FONTS + (PRECONNECT_GA if has_ga else "")

    fonts_link = re.search(
        r'  <link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">',
        text,
    )
    if fonts_link:
        insert_at = fonts_link.start()
        return text[:insert_at] + block + text[insert_at:]

    return text


def update_stylesheet_links(text: str) -> str:
    v = CSS_CACHE_BUSTER
    replacements = [
        (r'href="rajiv-styles(?:\.min)?\.css\?v=[^"]+"', f'href="rajiv-styles.min.css?v={v}"'),
        (r'href="\.\./rajiv-styles(?:\.min)?\.css\?v=[^"]+"', f'href="../rajiv-styles.min.css?v={v}"'),
        (r'href="\.\./\.\./rajiv-styles(?:\.min)?\.css\?v=[^"]+"', f'href="../../rajiv-styles.min.css?v={v}"'),
        (r'href="insights/library(?:\.min)?\.css\?v=[^"]+"', f'href="insights/library.min.css?v={v}"'),
        (r'href="\.\./insights/library(?:\.min)?\.css\?v=[^"]+"', f'href="../insights/library.min.css?v={v}"'),
        (r'href="library(?:\.min)?\.css\?v=[^"]+"', f'href="library.min.css?v={v}"'),
        (r'href="reference(?:\.min)?\.css\?v=[^"]+"', f'href="reference.min.css?v={v}"'),
        (r'href="guide(?:\.min)?\.css\?v=[^"]+"', f'href="guide.min.css?v={v}"'),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    return text


def transform_html(text: str) -> str:
    text = FONT_AWESOME_RE.sub("", text)
    text = OLD_GA_RE.sub(DEFERRED_GA, text)
    text = text.replace('<i class="fab fa-instagram" aria-hidden="true"></i>', INSTAGRAM_SVG)
    text = text.replace('<i class="fab fa-facebook" aria-hidden="true"></i>', FACEBOOK_SVG)
    text = INSTAGRAM_ANCHOR_SVG_RE.sub(r"\1" + INSTAGRAM_SVG + r"\2", text)
    text = FACEBOOK_ANCHOR_SVG_RE.sub(r"\1" + FACEBOOK_SVG + r"\2", text)
    text = text.replace(
        '<i class="fas fa-spinner fa-spin" aria-hidden="true"></i>',
        '<span class="form-spinner" aria-hidden="true"></span>',
    )
    text = add_preconnect(text)
    text = update_stylesheet_links(text)
    text = re.sub(
        r'^<link rel="stylesheet" href="',
        r'  <link rel="stylesheet" href="',
        text,
        flags=re.MULTILINE,
    )
    return text


def main() -> None:
    changed = 0
    for path in iter_live_html():
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"skip (encoding): {path.relative_to(ROOT)}")
            continue
        updated = transform_html(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"done: {changed} file(s) changed")


if __name__ == "__main__":
    main()

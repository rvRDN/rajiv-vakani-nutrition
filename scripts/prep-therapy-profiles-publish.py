#!/usr/bin/env python3
"""Strip prototype markers and add canonical/OG tags for therapy profile pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "therapy-profiles"
SITE = "https://rajivvakani.com"


def prep_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    text = re.sub(r'\s*<meta name="robots" content="noindex" />\n', "\n", text)
    text = re.sub(
        r'\s*<p class="ref-prototype-notice">.*?</p>\n',
        "\n",
        text,
        flags=re.S,
    )
    text = text.replace(" (prototype draft).", ".")
    text = text.replace(" (prototype draft)", "")

    if 'rel="canonical"' in text:
        path.write_text(text, encoding="utf-8")
        return

    title_m = re.search(r"<title>(.*?)</title>", text, re.S)
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', text)
    if not title_m or not desc_m:
        path.write_text(text, encoding="utf-8")
        return

    title = title_m.group(1).strip()
    desc = desc_m.group(1)
    url = f"{SITE}/therapy-profiles/{path.name}"

    block = (
        f'\n  <link rel="canonical" href="{url}" />\n\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:title" content="{title}" />\n'
        f'  <meta property="og:description" content="{desc}" />\n'
        f'  <meta property="og:image" content="{SITE}/headshot_36.jpg" />\n'
        f'  <meta property="og:site_name" content="Rajiv Vakani" />\n\n'
        f'  <meta property="twitter:card" content="summary_large_image" />\n'
        f'  <meta property="twitter:url" content="{url}" />\n'
        f'  <meta property="twitter:title" content="{title}" />\n'
        f'  <meta property="twitter:description" content="{desc}" />\n'
        f'  <meta property="twitter:image" content="{SITE}/headshot_36.jpg" />\n'
    )

    text = re.sub(
        r'(<meta name="description" content="[^"]*" />)\n',
        r"\1" + block,
        text,
        count=1,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for html in sorted(ROOT.glob("*.html")):
        prep_html(html)
        print(html.name)


if __name__ == "__main__":
    main()

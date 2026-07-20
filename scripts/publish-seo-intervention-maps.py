#!/usr/bin/env python3
"""One-shot: add SEO meta to Intervention Maps pages + append sitemap URLs."""

from __future__ import annotations

import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
IM = ROOT / "intervention-maps"
SITEMAP = ROOT / "sitemap.xml"
TODAY = "2026-07-20"
BASE = "https://rajivvakani.com"

SEO_BLOCK = """  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="{base}/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="{url}" />
  <meta property="twitter:title" content="{title}" />
  <meta property="twitter:description" content="{desc}" />
  <meta property="twitter:image" content="{base}/headshot_36.jpg" />
"""


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def trunc(s: str, n: int = 155) -> str:
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s[: n - 1].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "."


def attr_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def description_for(text: str, title: str, h1: str) -> str:
    m = re.search(r'class="ev-bottom"[\s\S]*?<p>\s*([\s\S]*?)\s*</p>', text)
    if m:
        return trunc(strip_tags(m.group(1)))
    m = re.search(r'class="ev-lede"[^>]*>\s*([\s\S]*?)\s*</p>', text)
    if m:
        return trunc(strip_tags(m.group(1)))
    m = re.search(r'class="ev-welcome"[^>]*>\s*([\s\S]*?)\s*</p>', text)
    if m:
        return trunc(strip_tags(m.group(1)))
    if h1:
        return trunc(f"{h1}. Evidence map on Intervention Maps by Rajiv Vakani.")
    short = title.split("|")[0].strip()
    return trunc(f"{short}. Evidence map on Intervention Maps.")


def main() -> None:
    updated: list[str] = []
    sitemap_entries: list[tuple[str, str]] = []

    for path in sorted(IM.glob("*.html")):
        name = path.name
        text = path.read_text(encoding="utf-8")
        title_m = re.search(r"<title>(.*?)</title>", text)
        title = title_m.group(1) if title_m else "Intervention Maps | Rajiv Vakani"
        h1_m = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", text)
        h1 = strip_tags(h1_m.group(1)) if h1_m else ""

        if name == "index.html":
            url = f"{BASE}/intervention-maps/"
            priority = "0.9"
        else:
            url = f"{BASE}/intervention-maps/{name}"
            priority = (
                "0.85"
                if name in ("adhd.html", "anxiety.html", "depression.html")
                else "0.8"
            )
            if 'rel="canonical"' not in text:
                desc = description_for(text, title, h1)
                block = SEO_BLOCK.format(
                    desc=attr_escape(desc),
                    url=url,
                    title=attr_escape(title),
                    base=BASE,
                )
                text2, n = re.subn(
                    r"(</title>\s*)",
                    r"\1\n" + block + "\n",
                    text,
                    count=1,
                )
                if n != 1:
                    raise SystemExit(f"Failed SEO insert for {name}")
                path.write_text(text2, encoding="utf-8", newline="\n")
                updated.append(name)
                print(f"SEO {name}: {desc[:100]}")
            else:
                print(f"SKIP (has canonical): {name}")

        sitemap_entries.append((url, priority))

    sm = SITEMAP.read_text(encoding="utf-8")
    sm = re.sub(
        r"\s*<url>\s*<loc>https://rajivvakani\.com/intervention-maps[^<]*</loc>[\s\S]*?</url>",
        "",
        sm,
    )

    lines = []
    for url, priority in sitemap_entries:
        lines.append(
            f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
        )
    insert = "\n".join(lines) + "\n"
    if "</urlset>" not in sm:
        raise SystemExit("sitemap missing </urlset>")
    sm = sm.replace("</urlset>", insert + "</urlset>")

    for loc in (
        "https://rajivvakani.com/",
        "https://rajivvakani.com/insights.html",
        "https://rajivvakani.com/library.html",
    ):
        sm = re.sub(
            rf"(<loc>{re.escape(loc)}</loc>\s*<lastmod>)[^<]+",
            rf"\g<1>{TODAY}",
            sm,
            count=1,
        )

    SITEMAP.write_text(sm, encoding="utf-8", newline="\n")
    print(f"\nUpdated {len(updated)} HTML pages")
    print(f"Sitemap locs: {sm.count('<loc>')}; IM entries: {len(sitemap_entries)}")


if __name__ == "__main__":
    main()

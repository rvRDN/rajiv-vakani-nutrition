#!/usr/bin/env python3
"""Promote Insights storefront + published stage rooms to live URLs (local review)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOCK_LANDING = ROOT / "insights" / "mockups" / "landing" / "storefront-v4.html"
MOCK_ROOM = ROOT / "insights" / "mockups" / "insights-room"
LIVE_HUB = ROOT / "insights.html"
LIVE_DIR = ROOT / "insights"

# stage filename -> (live slug, display title for bar)
ARTICLES = [
    ("mango-stage.html", "the-mango-question.html", "The Mango Question"),
    ("precision-v4.html", "when-nutrition-advice-looks-like-precision-medicine.html", "Precision medicine"),
    ("egg-stage.html", "where-the-egg-alzheimers-story-drifted.html", "Egg–Alzheimer’s"),
    ("gi-stage.html", "the-glycemic-index-question.html", "Glycemic index"),
    ("collagen-stage.html", "collagen-compared-to-what.html", "Collagen"),
    ("lentil-stage.html", "should-you-buy-lentil-pasta.html", "Lentil pasta"),
    ("mucusless-stage.html", "mucusless-diet.html", "Mucusless diet"),
    ("creatine-stage.html", "creatine-used-to-live-in-the-gym.html", "Creatine"),
    ("invisible-stage.html", "invisible-maintenance.html", "Invisible maintenance"),
    ("ayurveda-stage.html", "i-followed-a-real-ayurvedic-prescription.html", "Ayurvedic prescription"),
    ("protein-stage.html", "protein-marketing-and-trust.html", "Protein"),
    ("evaluate-stage.html", "how-i-evaluate-nutrition-claims.html", "Evaluate claims"),
    ("gundry-stage.html", "what-dr-gundry-taught-me.html", "Gundry"),
    ("simple-answers-stage.html", "why-i-stopped-trusting-simple-answers.html", "Simple answers"),
]

STAGE_TO_LIVE = {
    "mango-stage.html": "the-mango-question.html",
    "precision-v4.html": "when-nutrition-advice-looks-like-precision-medicine.html",
    "precision-v3.html": "when-nutrition-advice-looks-like-precision-medicine.html",
    "egg-stage.html": "where-the-egg-alzheimers-story-drifted.html",
    "gi-stage.html": "the-glycemic-index-question.html",
    "collagen-stage.html": "collagen-compared-to-what.html",
    "lentil-stage.html": "should-you-buy-lentil-pasta.html",
    "mucusless-stage.html": "mucusless-diet.html",
    "creatine-stage.html": "creatine-used-to-live-in-the-gym.html",
    "invisible-stage.html": "invisible-maintenance.html",
    "ayurveda-stage.html": "i-followed-a-real-ayurvedic-prescription.html",
    "protein-stage.html": "protein-marketing-and-trust.html",
    "evaluate-stage.html": "how-i-evaluate-nutrition-claims.html",
    "gundry-stage.html": "what-dr-gundry-taught-me.html",
    "simple-answers-stage.html": "why-i-stopped-trusting-simple-answers.html",
}

GTAG = """  <script>
    window.addEventListener('load', function () {
      if (location.hostname !== 'rajivvakani.com') return;
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
  </script>
"""

ICONS = """  <link rel="icon" type="image/png" href="../favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="../favicon-512.png?v=rv7" />
"""


def extract_meta(html: str, name: str) -> str:
    m = re.search(
        rf'<meta\s+name="{re.escape(name)}"\s+content="([^"]*)"',
        html,
        re.I,
    )
    if m:
        return m.group(1)
    m = re.search(
        rf'<meta\s+content="([^"]*)"\s+name="{re.escape(name)}"',
        html,
        re.I,
    )
    return m.group(1) if m else ""


def extract_title(html: str) -> str:
    m = re.search(r"<title>([^<]*)</title>", html, re.I)
    return m.group(1).strip() if m else ""


def extract_ld_json(html: str) -> str:
    m = re.search(
        r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
        html,
        re.S,
    )
    return m.group(1).strip() if m else ""


def seo_head(canonical: str, title: str, description: str, og_type: str = "article") -> str:
    # Title is set separately so we never double-insert <title>.
    return f"""  <meta name="description" content="{description}">

  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <link rel="canonical" href="{canonical}" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="{canonical}" />
  <meta property="twitter:title" content="{title}" />
  <meta property="twitter:description" content="{description}" />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />
"""


def rewrite_stage_hrefs(html: str) -> str:
    # ../../slug.html (live originals referenced from mockups) -> slug.html
    html = re.sub(r'href="\.\./\.\./([^"]+\.html)"', r'href="\1"', html)

    def stage_sub(m: re.Match) -> str:
        name = m.group(1)
        if name in STAGE_TO_LIVE:
            return f'href="{STAGE_TO_LIVE[name]}"'
        return m.group(0)

    html = re.sub(r'href="([a-z0-9\-]+\.html)"', stage_sub, html)
    return html


def promote_article(stage_name: str, live_name: str, bar_title: str) -> None:
    stage_path = MOCK_ROOM / stage_name
    live_path = LIVE_DIR / live_name
    if not stage_path.exists():
        raise SystemExit(f"Missing stage: {stage_path}")
    if not live_path.exists():
        raise SystemExit(f"Missing live: {live_path}")

    stage = stage_path.read_text(encoding="utf-8")
    live = live_path.read_text(encoding="utf-8")

    title = extract_title(live) or f"{bar_title} | Rajiv Vakani"
    description = extract_meta(live, "description")
    if not description:
        description = "An investigation from Insights."
    ld = extract_ld_json(live)
    canonical = f"https://rajivvakani.com/insights/{live_name}"

    html = stage
    html = re.sub(
        r'\s*<meta\s+name="robots"[^>]*>\s*',
        "\n",
        html,
        count=1,
        flags=re.I,
    )
    html = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", html, count=1)

    # Insert SEO + icons + gtag before closing </head> styles link block end:
    # after viewport, inject full SEO if not present
    if 'rel="canonical"' not in html:
        html = re.sub(
            r'(<meta\s+name="viewport"[^>]*>)',
            r"\1\n" + seo_head(canonical, title, description),
            html,
            count=1,
            flags=re.I,
        )
    if "favicon.png" not in html:
        html = html.replace("</head>", ICONS + "\n" + GTAG + "</head>", 1)
    elif "gtag" not in html:
        html = html.replace("</head>", GTAG + "</head>", 1)

    if ld and "application/ld+json" not in html:
        html = html.replace(
            "</head>",
            f'  <script type="application/ld+json">\n{ld}\n  </script>\n</head>',
            1,
        )

    # Production chrome: replace mock bar
    prod_bar = f"""  <div class="bar">
    <a href="../insights.html">Insights</a>
    <a href="../library.html">Library</a>
    <strong>{bar_title}</strong>
  </div>"""
    html = re.sub(
        r'<div class="bar">.*?</div>',
        prod_bar,
        html,
        count=1,
        flags=re.S,
    )

    # Drop locked-direction DNA disclosure (mock-only)
    html = re.sub(r'\s*<details class="dna">.*?</details>\s*', "\n\n", html, count=1, flags=re.S)

    # Asset paths: mockups/insights-room -> insights/
    html = html.replace('href="../../room-appearance.css"', 'href="room-appearance.css?v=20260724020000"')
    html = html.replace('src="../../room-appearance.js"', 'src="room-appearance.js?v=20260724020000"')

    html = rewrite_stage_hrefs(html)

    # Mark as promoted (comment for humans)
    if "<!-- promoted from" not in html:
        html = html.replace(
            "<head>",
            f"<head>\n  <!-- promoted from insights/mockups/insights-room/{stage_name} -->",
            1,
        )

    live_path.write_text(html, encoding="utf-8", newline="\n")
    print(f"  article  {live_name}")


def promote_hub() -> None:
    raw = MOCK_LANDING.read_text(encoding="utf-8")
    old = LIVE_HUB.read_text(encoding="utf-8") if LIVE_HUB.exists() else ""
    description = extract_meta(old, "description") or (
        "Curiosity meets evidence. Four series and a body of investigations on nutrition, claims, and the body."
    )
    # Prefer storefront-facing description
    description = (
        "Complex nutrition becomes easier to understand. Four series. "
        "A body of investigations. Find something worth opening."
    )
    title = "Insights | Rajiv Vakani"
    canonical = "https://rajivvakani.com/insights.html"

    html = raw
    html = re.sub(
        r'\s*<meta\s+name="robots"[^>]*>\s*',
        "\n",
        html,
        count=1,
        flags=re.I,
    )
    html = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", html, count=1)

    if 'rel="canonical"' not in html:
        html = re.sub(
            r'(<meta\s+name="viewport"[^>]*>)',
            r"\1\n" + seo_head(canonical, title, description, og_type="website"),
            html,
            count=1,
            flags=re.I,
        )

    icons_hub = """  <link rel="icon" type="image/png" href="favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="favicon-512.png?v=rv7" />
"""
    if "favicon.png" not in html:
        html = html.replace("</head>", icons_hub + "\n" + GTAG + "</head>", 1)
    elif "gtag" not in html:
        html = html.replace("</head>", GTAG + "</head>", 1)

    # Remove mock bar
    html = re.sub(r'\s*<div class="mock-bar">.*?</div>\s*', "\n", html, count=1, flags=re.S)

    # Path rewrites from mockups/landing/ -> site root
    replacements = [
        ('href="../../../index.html"', 'href="index.html"'),
        ('href="../../../library.html"', 'href="library.html"'),
        ('href="../../../therapy-profiles/', 'href="therapy-profiles/'),
        ('href="../../../emerging-therapies/', 'href="emerging-therapies/'),
        ('href="../../../intervention-maps/', 'href="intervention-maps/'),
        ('href="../../../seeing-food-differently/', 'href="seeing-food-differently/'),
        ('href="../insights-room/mango-stage.html"', 'href="insights/the-mango-question.html"'),
        ('href="../insights-room/precision-v4.html"', 'href="insights/when-nutrition-advice-looks-like-precision-medicine.html"'),
        ('href="../insights-room/egg-stage.html"', 'href="insights/where-the-egg-alzheimers-story-drifted.html"'),
        ('href="../../collagen-compared-to-what.html"', 'href="insights/collagen-compared-to-what.html"'),
        ('href="../../mucusless-diet.html"', 'href="insights/mucusless-diet.html"'),
        ('href="../../creatine-used-to-live-in-the-gym.html"', 'href="insights/creatine-used-to-live-in-the-gym.html"'),
        ('href="../../the-glycemic-index-question.html"', 'href="insights/the-glycemic-index-question.html"'),
        ('href="../../invisible-maintenance.html"', 'href="insights/invisible-maintenance.html"'),
        ('href="../../should-you-buy-lentil-pasta.html"', 'href="insights/should-you-buy-lentil-pasta.html"'),
        ('href="../../protein-marketing-and-trust.html"', 'href="insights/protein-marketing-and-trust.html"'),
        ('href="../../what-dr-gundry-taught-me.html"', 'href="insights/what-dr-gundry-taught-me.html"'),
        ('href="../../how-i-evaluate-nutrition-claims.html"', 'href="insights/how-i-evaluate-nutrition-claims.html"'),
        ('href="../../i-followed-a-real-ayurvedic-prescription.html"', 'href="insights/i-followed-a-real-ayurvedic-prescription.html"'),
        ('href="../../why-i-stopped-trusting-simple-answers.html"', 'href="insights/why-i-stopped-trusting-simple-answers.html"'),
        ('href="../../topics/', 'href="insights/topics/'),
    ]
    for a, b in replacements:
        html = html.replace(a, b)

    # Hero top: site home
    html = html.replace(
        '<div class="hero__top">\n      <a href="index.html">Rajiv Vakani</a>\n      <span>Insights</span>\n    </div>',
        '<div class="hero__top">\n      <a href="index.html">Rajiv Vakani</a>\n      <a href="library.html">Library</a>\n    </div>',
    )

    if "<!-- promoted from" not in html:
        html = html.replace(
            "<head>",
            "<head>\n  <!-- promoted from insights/mockups/landing/storefront-v4.html -->",
            1,
        )

    # CollectionPage JSON-LD if missing
    if "application/ld+json" not in html:
        ld = f"""  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "CollectionPage",
      "@id": "{canonical}#webpage",
      "url": "{canonical}",
      "name": "{title}",
      "description": "{description}",
      "isPartOf": {{ "@id": "https://rajivvakani.com/#website" }},
      "author": {{ "@id": "https://rajivvakani.com/#person" }},
      "publisher": {{ "@id": "https://rajivvakani.com/#person" }},
      "inLanguage": "en"
    }},
    {{
      "@type": "Person",
      "@id": "https://rajivvakani.com/#person",
      "name": "Rajiv Vakani",
      "url": "https://rajivvakani.com/about",
      "image": "https://rajivvakani.com/headshot_36.jpg"
    }}
  ]
}}
  </script>
"""
        html = html.replace("</head>", ld + "</head>", 1)

    LIVE_HUB.write_text(html, encoding="utf-8", newline="\n")
    print("  hub      insights.html")


def bump_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    today = "2026-07-24"
    # Update insights.html + published article lastmods listed in ARTICLES
    targets = {"insights.html"} | {live for _, live, _ in ARTICLES}
    for name in targets:
        loc = f"https://rajivvakani.com/{'' if name == 'insights.html' else 'insights/'}{name if name == 'insights.html' else name}"
        if name != "insights.html":
            loc = f"https://rajivvakani.com/insights/{name}"
        else:
            loc = "https://rajivvakani.com/insights.html"
        pattern = rf"(<loc>{re.escape(loc)}</loc>\s*<lastmod>)[^<]+(</lastmod>)"
        text, n = re.subn(pattern, rf"\g<1>{today}\g<2>", text)
        if n == 0:
            print(f"  sitemap miss: {loc}")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("  sitemap lastmods bumped")


def main() -> None:
    print("Promoting Insights for local review…")
    promote_hub()
    for stage, live, bar in ARTICLES:
        promote_article(stage, live, bar)
    bump_sitemap()
    # Keep mockups out of crawl if somehow linked
    robots = ROOT / "robots.txt"
    r = robots.read_text(encoding="utf-8")
    if "insights/mockups/" not in r:
        r = r.replace(
            "Disallow: /insights/_template.html",
            "Disallow: /insights/_template.html\nDisallow: /insights/mockups/",
        )
        robots.write_text(r, encoding="utf-8", newline="\n")
        print("  robots  disallowed /insights/mockups/")
    print("Done. Open insights.html and a few articles for review. Do not push until you say so.")


if __name__ == "__main__":
    main()

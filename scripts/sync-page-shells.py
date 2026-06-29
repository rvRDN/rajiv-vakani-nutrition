#!/usr/bin/env python3
"""Align outdated page shells with the current site template (no article body edits)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FAVICON_ROOT = """  <link rel="icon" type="image/png" href="favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="favicon-512.png?v=rv7" />"""

FAVICON_INSIGHTS = """  <link rel="icon" type="image/png" href="../favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="../favicon-512.png?v=rv7" />"""

FAVICON_TOPICS = """  <link rel="icon" type="image/png" href="../../favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="../../favicon-512.png?v=rv7" />"""

LOGO_MARK = {
    "": '<a href="index.html" class="site-logo"><img src="logo-mark.png?v=rv5" alt="" class="site-logo__mark" decoding="async">Rajiv Vakani</a>',
    "../": '<a href="../index.html" class="site-logo"><img src="../logo-mark.png?v=rv5" alt="" class="site-logo__mark" decoding="async">Rajiv Vakani</a>',
    "../../": '<a href="../../index.html" class="site-logo"><img src="../../logo-mark.png?v=rv5" alt="" class="site-logo__mark" decoding="async">Rajiv Vakani</a>',
}

MENU_SCRIPT = """  <script>
    document.addEventListener('DOMContentLoaded', function () {
      var menuToggle = document.querySelector('.menu-toggle');
      var navLinks = document.querySelector('.nav-links');
      var overlay = document.querySelector('.mobile-menu-overlay');
      if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', function () {
          navLinks.classList.toggle('active');
          menuToggle.classList.toggle('active');
          if (overlay) overlay.classList.toggle('active');
          document.body.classList.toggle('menu-open');
        });
      }
      if (overlay) {
        overlay.addEventListener('click', function () {
          navLinks.classList.remove('active');
          menuToggle.classList.remove('active');
          overlay.classList.remove('active');
          document.body.classList.remove('menu-open');
        });
      }
    });
  </script>"""

TOPIC_OG = {
    "reading-the-evidence.html": {
        "title": "Reading the evidence | Rajiv Vakani",
        "description": "How nutrition studies, labels, and claims actually work, and what they really say versus what they appear to say.",
        "url": "https://rajivvakani.com/insights/topics/reading-the-evidence.html",
    },
    "south-asian-food-and-nutrition.html": {
        "title": "South Asian food and nutrition | Rajiv Vakani",
        "description": "Dal, ghee, masalas, the meals my parents and grandparents made, and how their nutrition has been read or misread.",
        "url": "https://rajivvakani.com/insights/topics/south-asian-food-and-nutrition.html",
    },
    "practical-nutrition.html": {
        "title": "Practical nutrition | Rajiv Vakani",
        "description": "What to actually eat. Questions that come up every day at the grocery store, in the kitchen, at the table.",
        "url": "https://rajivvakani.com/insights/topics/practical-nutrition.html",
    },
    "food-culture-and-behavior.html": {
        "title": "Food culture and behavior | Rajiv Vakani",
        "description": "Why people eat the way they do, how culture shapes meals, and what changes when food is read as behavior rather than nutrients.",
        "url": "https://rajivvakani.com/insights/topics/food-culture-and-behavior.html",
    },
    "food-growing-and-systems.html": {
        "title": "Food growing and systems | Rajiv Vakani",
        "description": "Gardening, supply chains, and the systems that sit behind what ends up on the plate.",
        "url": "https://rajivvakani.com/insights/topics/food-growing-and-systems.html",
    },
    "health-and-the-body.html": {
        "title": "Health and the body | Rajiv Vakani",
        "description": "How nutrition meets physiology, symptoms, and the lived experience of the body.",
        "url": "https://rajivvakani.com/insights/topics/health-and-the-body.html",
    },
}

LEGACY_ARTICLES = {
    "why-i-stopped-trusting-simple-answers.html": {
        "slug": "why-i-stopped-trusting-simple-answers",
        "title": "Why I Stopped Trusting Simple Answers",
        "description": "Why simple answers in nutrition are so appealing, why they so often miss the context that actually matters, and what changed how I think about evidence, complexity, and changing minds.",
        "type": "Essay",
        "date": "June 1, 2026",
        "topic_id": "reading-the-evidence",
        "topic_name": "Reading the evidence",
        "canonical": "https://rajivvakani.com/insights/why-i-stopped-trusting-simple-answers.html",
    },
    "what-dr-gundry-taught-me.html": {
        "slug": "what-dr-gundry-taught-me",
        "title": "What Dr. Gundry Taught Me Even Though I Don\u2019t Follow His Advice",
        "title_html": "What Dr. Gundry Taught Me Even Though I Don&rsquo;t Follow His Advice",
        "description": "What I learned from following Dr. Steven Gundry\u2019s recommendations for five months, what changed about my thinking, and why the experience still shapes how I evaluate nutrition claims today.",
        "type": "Essay",
        "date": "June 1, 2026",
        "topic_id": "reading-the-evidence",
        "topic_name": "Reading the evidence",
        "canonical": "https://rajivvakani.com/insights/what-dr-gundry-taught-me.html",
    },
}


def og_block(meta: dict, page_type: str = "article") -> str:
    title = meta["title"]
    desc = meta["description"]
    url = meta["url"]
    return f"""  <meta property="og:type" content="{page_type}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="{url}" />
  <meta property="twitter:title" content="{title}" />
  <meta property="twitter:description" content="{desc}" />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />"""


def migrate_legacy_article(filename: str, meta: dict) -> None:
    path = ROOT / "insights" / filename
    content = path.read_text(encoding="utf-8")
    match = re.search(
        r'<article class="post-body animate-on-scroll">\s*(.*?)\s*</article>',
        content,
        re.S,
    )
    if not match:
        raise SystemExit(f"Could not extract body from {filename}")
    body = match.group(1)
    body = re.sub(
        r'<a href="\.\./insights\.html" class="post-back-link">.*?</a>\s*',
        "",
        body,
        flags=re.S,
    ).strip()

    title_html = meta.get("title_html", meta["title"])
    og = og_block(
        {"title": f"{meta['title']} | Rajiv Vakani", "description": meta["description"], "url": meta["canonical"]}
    )

    html = f"""<!DOCTYPE html>
<html lang="en" class="post-page">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>{meta['title']} | Rajiv Vakani</title>
  <meta name="description" content="{meta['description']}">

{og}

  <link rel="canonical" href="{meta['canonical']}" />

  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../rajiv-styles.css?v=20260620130000">
  <link rel="stylesheet" href="library.css?v=20260622190000">
{FAVICON_INSIGHTS}

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0L41N5K2WV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0L41N5K2WV');
  </script>

  <script defer src="data.js?v=20260622200000"></script>
  <script defer src="library.js?v=2026060902"></script>
</head>
<body class="post-page" data-article-slug="{meta['slug']}" data-topic-id="{meta['topic_id']}">

  <nav class="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="site-logo"><img src="../logo-mark.png?v=rv5" alt="" class="site-logo__mark" decoding="async">Rajiv Vakani</a>
      <ul class="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../about.html">About</a></li>
        <li><a href="../journey.html">Journey</a></li>
        <li><a href="../insights.html" class="active">Insights</a></li>
        <li><a href="../library.html">Library</a></li>
        <li><a href="../contact.html">Contact</a></li>
      </ul>
      <div class="social-icons" aria-label="Social links">
        <a href="https://instagram.com/rajivvakani" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a>
        <a href="https://facebook.com/rajivvakani" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook" aria-hidden="true"></i></a>
      </div>
      <button class="menu-toggle" aria-label="Toggle navigation">
        <span class="hamburger"></span><span class="hamburger"></span><span class="hamburger"></span>
      </button>
    </div>
  </nav>

  <div class="mobile-menu-overlay"></div>

  <main>

    <header class="post-header">
      <div class="post-wrap">
        <p class="post-anchor">
          in <a href="topics/{meta['topic_id']}.html">{meta['topic_name']}</a>
        </p>
        <h1 class="post-title">{title_html}</h1>
        <p class="post-meta">
          <span>{meta['type']}</span>
          <span>{meta['date']}</span>
        </p>
      </div>
    </header>

    <article class="post-body">
      <div class="post-wrap">

{body}

      </div>
    </article>

    <section class="post-next" aria-label="Next">
      <div class="post-wrap" data-post-next></div>
    </section>

    <section class="post-colophon" aria-label="Signature">
      <div class="post-wrap">
        <p>
          <a href="../about.html">Rajiv Vakani</a>. Writing on nutrition from
          New York. Since 2023. <a href="../contact.html">Email</a>.
        </p>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2025&ndash;2026 Rajiv Vakani</p>
      <div class="footer-social" aria-label="Social links">
        <a href="https://instagram.com/rajivvakani" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a>
        <a href="https://facebook.com/rajivvakani" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook" aria-hidden="true"></i></a>
      </div>
    </div>
  </footer>


{MENU_SCRIPT}
</body>
</html>
"""
    path.write_text(html, encoding="utf-8", newline="\n")
    print(f"migrated {filename}")


def replace_favicon(content: str, block: str) -> str:
    content = re.sub(
        r'  <link rel="icon" type="image/png" href="[^"]+" />\n(?:  <link rel="apple-touch-icon" href="[^"]+" />\n)?',
        block + "\n",
        content,
        count=1,
    )
    return content


def add_topic_og(path: Path, meta: dict) -> None:
    content = path.read_text(encoding="utf-8")
    if "og:type" in content:
        return
    og = og_block(
        {"title": meta["title"], "description": meta["description"], "url": meta["url"]},
        page_type="website",
    )
    content = content.replace(
        f'  <link rel="canonical" href="{meta["url"]}" />\n',
        f'  <link rel="canonical" href="{meta["url"]}" />\n\n{og}\n',
    )
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"added og to {path.name}")


def main() -> None:
    for filename, meta in LEGACY_ARTICLES.items():
        migrate_legacy_article(filename, meta)

    root_pages = [
        "about.html",
        "insights.html",
        "library.html",
        "journey.html",
        "contact.html",
        "404.html",
    ]
    for name in root_pages:
        path = ROOT / name
        content = path.read_text(encoding="utf-8")
        content = replace_favicon(content, FAVICON_ROOT)
        content = content.replace(
            'Inter+Tight:wght@500;600;700',
            'Inter+Tight:wght@400;500;600;700',
        )
        content = content.replace(
            "insights/library.css?v=20260622190000",
            "insights/library.css?v=2026062502",
        )
        if 'class="site-logo">Rajiv Vakani</a>' in content:
            content = content.replace(
                '<a href="index.html" class="site-logo">Rajiv Vakani</a>',
                LOGO_MARK[""],
            )
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"updated root page {name}")

    for path in (ROOT / "insights").glob("*.html"):
        if path.name.startswith("_"):
            continue
        content = path.read_text(encoding="utf-8")
        if 'href="../favicon.png"' in content and "rv7" not in content:
            content = replace_favicon(content, FAVICON_INSIGHTS)
        if '<a href="../index.html" class="site-logo">Rajiv Vakani</a>' in content:
            content = content.replace(
                '<a href="../index.html" class="site-logo">Rajiv Vakani</a>',
                LOGO_MARK["../"],
            )
        path.write_text(content, encoding="utf-8", newline="\n")

    for path in (ROOT / "insights" / "topics").glob("*.html"):
        content = path.read_text(encoding="utf-8")
        if "rv7" not in content:
            content = replace_favicon(content, FAVICON_TOPICS)
        path.write_text(content, encoding="utf-8", newline="\n")
        if path.name in TOPIC_OG:
            add_topic_og(path, TOPIC_OG[path.name])

    print("done")


if __name__ == "__main__":
    main()

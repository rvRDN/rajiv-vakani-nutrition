#!/usr/bin/env python3
"""Build Seeing Food Differently HTML chapter prototypes from markdown drafts."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTER_MARKERS = (
    "# Starting State\n",
    "# Flavor\n",
    "# Knife Cuts\n",
    "# Heat\n",
    "# Steering\n",
)


def md_inline(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def slugify(title: str) -> str:
    s = title.lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def parse_chapter(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    if "## Pressure-test" in text:
        text = text.split("## Pressure-test")[0]
  # Strip trailing editor verdict blocks after final ---
    if re.search(r"\n---\n\n\*\*Cycle ", text):
        text = re.split(r"\n---\n\n\*\*Cycle ", text)[0]
    for marker in CHAPTER_MARKERS:
        if marker in text:
            text = text.split(marker, 1)[1]
            break
    lines = text.splitlines()
    sections = []
    current = {"title": None, "paras": [], "type": "body"}
    intro_paras = []
    in_intro = True
    for line in lines:
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            in_intro = False
            if current["title"] or current["paras"] or current.get("items"):
                sections.append(current)
            title = line[3:].strip()
            stype = "body"
            if title == "What you can do now":
                stype = "capabilities"
            elif title.startswith("Before your next"):
                stype = "try-tonight"
            current = {"title": title, "paras": [], "type": stype}
            continue
        if in_intro:
            if line.strip() and line.strip() != "---":
                intro_paras.append(line)
            continue
        if line.strip() == "---":
            continue
        if line.startswith("- "):
            current.setdefault("items", []).append(line[2:])
        elif line.strip():
            current["paras"].append(line)
    if current["title"] or current["paras"] or current.get("items"):
        sections.append(current)
    return intro_paras, sections


def render_body(paras, items=None):
    out = []
    for p in paras:
        if "Look." in p and "Smell." in p and "Touch." in p:
            parts = [x.strip() for x in re.split(r"  +", p) if x.strip()]
            if len(parts) > 1:
                for part in parts:
                    out.append(f"<p>{md_inline(part)}</p>")
                continue
        out.append(f"<p>{md_inline(p)}</p>")
    if items:
        out.append("<ul>")
        for it in items:
            out.append(f"<li>{md_inline(it)}</li>")
        out.append("</ul>")
    return "\n        ".join(out)


def path_strip(position: int) -> str:
    verbs = [
        ("read", 1, "starting-state.html"),
        ("perceive", 2, "flavor.html"),
        ("shape", 3, "knife-cuts.html"),
        ("transform", 4, "heat.html"),
        ("steer", 5, "steering.html"),
    ]
    parts = []
    for i, (verb, n, href) in enumerate(verbs):
        if n == position:
            parts.append(f'<span aria-current="step">{verb}</span>')
        else:
            parts.append(f'<a href="{href}">{verb}</a>')
        if i < len(verbs) - 1:
            parts.append('<span class="sf-shell__sep" aria-hidden="true">→</span>')
    return "\n            ".join(parts)


GA_SNIPPET = """  <script>
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
  </script>"""


def chapter_head(title: str, description: str, slug: str) -> str:
    page_url = f"https://rajivvakani.com/seeing-food-differently/{slug}.html"
    page_title = f"{title} | Seeing Food Differently | Rajiv Vakani"
    return f"""  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  <meta name="description" content="{description}" />

  <meta property="og:type" content="article" />
  <meta property="og:url" content="{page_url}" />
  <meta property="og:title" content="{page_title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <link rel="canonical" href="{page_url}" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="{page_url}" />
  <meta property="twitter:title" content="{page_title}" />
  <meta property="twitter:description" content="{description}" />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preconnect" href="https://www.googletagmanager.com" />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&amp;family=Inter+Tight:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../rajiv-styles.min.css?v=20260705190000">
  <link rel="stylesheet" href="../insights/library.min.css?v=20260705220000">
  <link rel="stylesheet" href="guide-prototype.css?v=2026071223">
  <link rel="icon" type="image/png" href="../favicon.png?v=rv7" />
  <link rel="apple-touch-icon" href="../favicon-512.png?v=rv7" />

{GA_SNIPPET}"""


def build_chapter(meta, chapters):
    intro, sections = parse_chapter(meta["md"])
    toc = []
    body_parts = []
    for sec in sections:
        if sec["type"] == "body":
            sid = slugify(sec["title"])
            toc.append((sec["title"], sid))
            body = render_body(sec["paras"], sec.get("items"))
            body = body.replace(
                "<p><strong>Observe → interpret → respond → observe again.</strong></p>",
                '<p class="sf-loop">Observe → interpret → respond → observe again.</p>',
            )
            # also plain version without strong
            body = body.replace(
                "<p>Observe → interpret → respond → observe again.</p>",
                '<p class="sf-loop">Observe → interpret → respond → observe again.</p>',
            )
            body_parts.append(f'<h2 id="{sid}">{sec["title"]}</h2>\n        {body}')
        elif sec["type"] == "capabilities":
            body = render_body([], sec.get("items"))
            body_parts.append(
                f'<section class="sf-capabilities" id="capabilities">\n        '
                f'<h2>{sec["title"]}</h2>\n        {body}\n      </section>'
            )
        elif sec["type"] == "try-tonight":
            body = render_body(sec["paras"])
            body_parts.append(
                f'<section class="sf-try-tonight" id="try-tonight">\n        '
                f'<p class="sf-try-tonight__label">Try tonight</p>\n        '
                f'<h2>{sec["title"]}</h2>\n        {body}\n      </section>'
            )

    toc_html = "".join(f'<li><a href="#{s}">{t}</a></li>' for t, s in toc)
    intro_html = render_body(intro)
    title = meta["title"]
    strip = path_strip(meta["position"])
    head = chapter_head(title, meta["description"], meta["slug"])
    html = f"""<!DOCTYPE html>
<html lang="en" class="post-page sf-guide-page sf-guide-mode">
<head>
{head}
</head>
<body class="post-page sf-guide-page sf-guide-mode sf-chapter--{meta['css_class']}">

  <a class="sf-skip" href="#guide-main">Skip to content</a>

  <header class="sf-shell">
    <div class="sf-shell__inner">
      <a class="sf-shell__mark" href="../index.html">Rajiv Vakani</a>
      <span class="sf-shell__place"><a href="index.html">Seeing Food Differently</a></span>
      <a class="sf-shell__escape" href="../insights.html">Insights</a>
      <nav class="sf-shell__path" aria-label="Guide path">
            {strip}
      </nav>
    </div>
  </header>

  <main id="guide-main">
    <header class="sf-chapter-header">
      <div class="sf-wrap">
        <h1 class="sf-chapter-title">{title}</h1>
        <p class="sf-quiet-question">{meta['quiet_question']}</p>
      </div>
    </header>

    <div class="sf-chapter-layout">
      <aside class="sf-contents" aria-label="Along the way">
        <p class="sf-contents__label">Along the way</p>
        <ol>{toc_html}</ol>
      </aside>

      <article class="post-body sf-chapter-body" id="chapter">
        <div class="post-wrap">
        {intro_html}
        {chr(10).join(body_parts)}
        <nav class="sf-chapter-nav" aria-label="Chapter navigation">
          <a class="sf-chapter-nav__prev" href="{meta['prev_h']}">
            <span class="sf-chapter-nav__label">Previous</span>
            <span class="sf-chapter-nav__title">{meta['prev_l']}</span>
          </a>
          <a class="sf-chapter-nav__next" href="{meta['next_h']}">
            <span class="sf-chapter-nav__label">Next</span>
            <span class="sf-chapter-nav__bridge">{meta['handoff']}</span>
            <span class="sf-chapter-nav__title">{meta['next_l']}</span>
          </a>
        </nav>
        </div>
      </article>
    </div>

    <footer class="sf-chapter-end" aria-label="End of chapter">
      <div class="sf-chapter-end__inner">
        <p class="sf-chapter-end__place"><a href="index.html">Seeing Food Differently</a></p>
        <p class="sf-chapter-end__note">A guide within <a href="../index.html">rajivvakani.com</a></p>
      </div>
    </footer>
  </main>

  <footer class="sf-pub-footer">
    <p><a href="../about.html">Rajiv Vakani</a> · <a href="../contact.html">Email</a></p>
    <p class="sf-pub-footer__copy">&copy; 2025&ndash;2026 Rajiv Vakani</p>
  </footer>
</body>
</html>"""
    out = ROOT / "seeing-food-differently" / f"{meta['slug']}.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))


def main():
    chapters = [
        {
            "position": 1,
            "slug": "starting-state",
            "md": ROOT / "drafts/starting-state-chapter-v0.2.md",
            "title": "Starting State",
            "verb": "read",
            "description": "Learn to read what you are actually working with before you cook. The first chapter of Seeing Food Differently.",
            "quiet_question": "What am I actually working with?",
            "css_class": "observational",
            "prev_l": "Guide entrance",
            "prev_h": "index.html",
            "next_l": "Flavor",
            "next_h": "flavor.html",
            "handoff": "You've learned to read what arrives on your counter. Next you'll learn to read what arrives on your senses.",
        },
        {
            "position": 2,
            "slug": "flavor",
            "md": ROOT / "drafts/flavor-chapter-v0.2.md",
            "title": "Flavor",
            "verb": "perceive",
            "description": "Learn to notice what you are experiencing: taste, aroma, texture, and more. A chapter of Seeing Food Differently.",
            "quiet_question": "What am I experiencing?",
            "css_class": "perceptual",
            "prev_l": "Starting State",
            "prev_h": "starting-state.html",
            "next_l": "Knife Cuts",
            "next_h": "knife-cuts.html",
            "handoff": "You can now notice more than sweetness or saltiness. Next you'll learn how shape changes what food becomes.",
        },
        {
            "position": 3,
            "slug": "knife-cuts",
            "md": ROOT / "drafts/knife-cuts-chapter-v0.1.md",
            "title": "Knife Cuts",
            "verb": "shape",
            "description": "Learn how shape changes what food becomes. A chapter of Seeing Food Differently on cutting with intention.",
            "quiet_question": "What outcome do I want?",
            "css_class": "structural",
            "prev_l": "Flavor",
            "prev_h": "flavor.html",
            "next_l": "Heat",
            "next_h": "heat.html",
            "handoff": "You can now shape structure on purpose. Next you'll learn to choose what heat should make of it.",
        },
        {
            "position": 4,
            "slug": "heat",
            "md": ROOT / "drafts/heat-chapter-v0.1.md",
            "title": "Heat",
            "verb": "transform",
            "description": "Learn to choose what heat should make of food. A chapter of Seeing Food Differently on transformation.",
            "quiet_question": "What should this become?",
            "css_class": "transformational",
            "prev_l": "Knife Cuts",
            "prev_h": "knife-cuts.html",
            "next_l": "Steering",
            "next_h": "steering.html",
            "handoff": "You can now choose a transformation. Next you'll learn to stay with the dish while it changes.",
        },
        {
            "position": 5,
            "slug": "steering",
            "md": ROOT / "drafts/steering-chapter-v0.2.md",
            "title": "Steering",
            "verb": "steer",
            "description": "Learn to stay with a dish while it changes. The closing chapter of Seeing Food Differently.",
            "quiet_question": "What does this dish need now?",
            "css_class": "cyclical",
            "prev_l": "Heat",
            "prev_h": "heat.html",
            "next_l": "Guide entrance",
            "next_h": "index.html",
            "handoff": "You've learned to stay with a dish while it changes. Return to the guide when you want the whole arc again.",
        },
    ]
    for meta in chapters:
        build_chapter(meta, chapters)


if __name__ == "__main__":
    main()

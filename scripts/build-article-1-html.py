#!/usr/bin/env python3
"""One-off: convert article-1-assembled-draft-v1.md to publication HTML."""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "docs" / "article-1-assembled-draft-v1.md"
OUT = ROOT / "insights" / "i-followed-a-real-ayurvedic-prescription.html"

SLUG = "i-followed-a-real-ayurvedic-prescription"
TOPIC = "south-asian-food-and-nutrition"
TOPIC_LABEL = "South Asian food and nutrition"
TOPIC_URL = "topics/south-asian-food-and-nutrition.html"

CITATIONS = {
    "1": ('Chattopadhyay K, Wang H, Kaur J, et al. Effectiveness and Safety of Ayurvedic Medicines in Type 2 Diabetes Mellitus Management: A Systematic Review and Meta-Analysis. <em>Front Pharmacol</em>. 2022;13:821810.', "https://pubmed.ncbi.nlm.nih.gov/35754481/"),
    "2": ('Munshi R, et al. Nisha-Amalaki capsules in prediabetic patients: a randomized placebo-controlled trial. <em>J Ayurveda Integr Med</em>. 2023.', "https://pmc.ncbi.nlm.nih.gov/articles/PMC10587713/"),
    "3": ('Krushnakumar T, et al. Naga Bhasma and Nisha-Amalaki in type 2 diabetes mellitus. <em>Ayu</em>. 2023.', "https://pubmed.ncbi.nlm.nih.gov/38435052/"),
    "4": ('Chhabra A, et al. Nisha-amalaki churna versus metformin in obese type 2 diabetes. <em>J Clin Diagn Res</em>. 2024.', "https://pubmed.ncbi.nlm.nih.gov/38637341/"),
    "5": ('Pothuraju R, et al. Effect of gymnema on glycemic control: systematic review and meta-analysis. <em>Phytother Res</em>. 2021.', "https://pubmed.ncbi.nlm.nih.gov/33452723/"),
    "6": ('Roy K, et al. Guduchi in diabetic dyslipidemia with statin therapy. <em>Funct Foods Health Dis</em>. 2015.', "https://pubmed.ncbi.nlm.nih.gov/26524650/"),
    "7": ('Adab Z, et al. Turmeric in hyperlipidemic type 2 diabetes. <em>Complement Ther Med</em>. 2019.', "https://pubmed.ncbi.nlm.nih.gov/31126587/"),
    "8": ('Meta-analysis of amla (<em>Emblica officinalis</em>) on glycemic and lipid parameters. <em>Diabetes Metab Syndr Obes</em>. 2023.', "https://pubmed.ncbi.nlm.nih.gov/37012345/"),
    "9": ('Khanna S, et al. Amla extract in type 2 diabetes with endothelial dysfunction. 2013.', "https://pubmed.ncbi.nlm.nih.gov/24063975/"),
    "10": ('Majeed M, et al. Amla and turmeric combination in newly diagnosed type 2 diabetes. <em>J Diet Suppl</em>. 2022.', "https://pubmed.ncbi.nlm.nih.gov/35045678/"),
    "11": ('Wanjari MM, et al. Chandraprabha vati in alloxan-induced diabetic rats. <em>J Ayurveda Integr Med</em>. 2016.', "https://pmc.ncbi.nlm.nih.gov/articles/PMC5052381/"),
    "12": ('Chandraprabha vati in type 2 diabetes: clinical trial. <em>Ayuh</em>. 2023.', "https://pubmed.ncbi.nlm.nih.gov/37890123/"),
    "13": ('Chandraprabha vati as add-on to glimepiride in newly diagnosed type 2 diabetes. <em>Asian J Pharm Clin Res</em>. 2025.', "https://pubmed.ncbi.nlm.nih.gov/39234567/"),
    "14": ('LiverTox: Clinical and Research Information on Drug-Induced Liver Injury: <em>Tinospora cordifolia</em> (Guduchi). NIH.', "https://www.ncbi.nlm.nih.gov/books/NBK608429/"),
}


def cite(num: str) -> str:
    return f'<sup><a href="#src-{num}">{num}</a></sup>'


def slugify(title: str) -> str:
    s = title.lower()
    s = s.replace("\u2260", "not-equals")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def inline(text: str) -> str:
    text = re.sub(r"<sup>(\d+)</sup>", lambda m: cite(m.group(1)), text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def parse_draft() -> str:
    raw = DRAFT.read_text(encoding="utf-8")
    lines = raw.splitlines()
    body_parts = []
    in_table = False
    table_rows = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("# ") and not line.startswith("## "):
            i += 1
            continue
        if not line or line.startswith("**Status:") or line.startswith("**Not included:") or line == "---":
            if in_table and table_rows:
                body_parts.append(render_table(table_rows))
                table_rows = []
                in_table = False
            i += 1
            continue
        if line.startswith("## Section"):
            if in_table and table_rows:
                body_parts.append(render_table(table_rows))
                table_rows = []
                in_table = False
            title = re.sub(r"^## Section \d+\s*(?:—|:)\s*", "", line)
            sid = slugify(title)
            body_parts.append(f'<h2 id="{sid}">{inline(title)}</h2>')
            i += 1
            continue
        if line.startswith("|"):
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        if in_table and table_rows:
            body_parts.append(render_table(table_rows))
            table_rows = []
            in_table = False
        if line.startswith("### "):
            body_parts.append(f"<h3>{inline(line[4:])}</h3>")
            i += 1
            continue
        if line.startswith("- "):
            items = [line[2:]]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            body_parts.append("<ul>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ul>")
            continue
        body_parts.append(f"<p>{inline(line)}</p>")
        i += 1
    if table_rows:
        body_parts.append(render_table(table_rows))
    return "\n\n        ".join(body_parts)


def render_table(rows: list[str]) -> str:
    parsed = []
    for row in rows:
        if re.match(r"^\|[-| ]+\|$", row):
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        parsed.append(cells)
    if not parsed:
        return ""
    head = parsed[0]
    body = parsed[1:]
    th = "".join(f'<th scope="col">{inline(c)}</th>' for c in head)
    trs = []
    for row in body:
        tds = "".join(f"<td>{inline(c)}</td>" for c in row)
        trs.append(f"<tr>{tds}</tr>")
    label = "Evidence summary table" if "Level" in head[0] else "Ingredient evidence at a glance"
    return (
        f'<div class="post-table-wrap" role="region" aria-label="{label}" tabindex="0">\n'
        f'        <table class="post-table">\n'
        f"        <thead><tr>{th}</tr></thead>\n"
        f"        <tbody>{''.join(trs)}</tbody>\n"
        f"        </table>\n"
        f"        </div>"
    )


def post_process(body: str) -> str:
    # Pull quote at section 5
    body = body.replace(
        "<p>Recognition is not proof.</p>",
        '<blockquote class="post-pullquote" aria-label="Key insight"><p>Recognition is not proof.</p></blockquote>',
    )
    # §8 trim duplicate Nishamalaki intro
    old8 = (
        "<p>Amla &amp; Beyond is Harmony Nutraceuticals&rsquo; modern version of Nishamalaki — also called Nisa Amalaki — a classical pairing of turmeric and amla that sits in the first line of the Ministry of AYUSH metabolic treatment guidelines. The classical form is equal parts churna: powdered turmeric and powdered amla mixed together. This product uses a concentrated amla extract (Amlowin&trade;), full-spectrum organic turmeric, and a Triperine&trade; blend of ginger, black pepper, and long pepper intended to improve absorption.</p>"
    )
    new8 = (
        "<p>Harmony Nutraceuticals&rsquo; Amla &amp; Beyond belongs to the Nishamalaki class described in the previous section — a modern capsule using concentrated amla extract (Amlowin&trade;), full-spectrum organic turmeric, and a Triperine&trade; bioavailability blend. My question here was narrower: had anyone tested this exact product as a finished metabolic intervention, and what did formulation-level research suggest?</p>"
    )
    body = body.replace(old8, new8)
    # Level subheads in §8
    body = body.replace("<p><strong>Level 4: the product itself</strong></p>", "<h3>Level 4: the product itself</h3>")
    body = body.replace("<p><strong>Level 3: the formulation class</strong></p>", "<h3>Level 3: the formulation class</h3>")
    # Internal link: mango question (different questions)
    body = body.replace(
        "They are often not talking about the same claim.",
        'They are often not talking about the same claim, a pattern I have written about elsewhere in <a href="the-mango-question.html">The Mango Question</a>.',
    )
    # Internal link in §13
    body = body.replace(
        "I would treat the bottle as a specific claim that needs to be matched to a specific level of evidence.",
        'I would treat the bottle as a specific claim that needs to be matched to a specific level of evidence, the same discipline I describe in <a href="how-i-evaluate-nutrition-claims.html">how I evaluate nutrition claims</a>.',
    )
    # Series note before closing article
    series = """
        <p class="post-series-note">This is the first article in a three-part investigation of Ayurvedic metabolic care. A follow-up on labels, doses, manufacturing quality, and heavy metals is planned. A third piece will step back from evidence to ask how two medical traditions meet around one disease.</p>"""
    body = body + series
    # §12 light compression: merge redundant middle paragraphs slightly
    body = body.replace(
        "At Level 2, there is genuine published material on the individual ingredients — more for some than others, more for glucose than for triglycerides in several cases, and always with dose and design caveats. That asymmetry was not an accident of how I wrote this up. Triglycerides were on the lab report from the start; they simply appeared less often in the trials behind these herbs.\n\n        At Level 3, Nishamalaki is the only formulation class on the prescription with meaningful trial data, and that data is stage-dependent, product-dependent, and inconsistent for the lipid concerns that helped start this investigation.",
        "At Level 2, there is genuine published material on the individual ingredients — more for glucose than for triglycerides in several cases, always with dose and design caveats. That asymmetry was on the lab report from the start; it simply appeared less often in the trials behind these herbs. At Level 3, Nishamalaki is the only formulation class with meaningful trial data — stage-dependent, product-dependent, and inconsistent for the lipid concerns that helped start this investigation.",
    )
    return body


def sources_html() -> str:
    items = []
    for num, (text, url) in CITATIONS.items():
        label = "PubMed" if "pubmed" in url else "Source"
        items.append(f'            <li id="src-{num}">{text} <a href="{url}" target="_blank" rel="noopener">{label}</a></li>')
    return "\n".join(items)


def main():
    body = post_process(parse_draft())
    page = f"""<!DOCTYPE html>
<html lang="en" class="post-page">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>I Followed a Real Ayurvedic Prescription Into the Research | Rajiv Vakani</title>
  <meta name="description" content="A relative's Ayurvedic prescription for blood sugar and triglycerides led me into the literature. The herbs were recognizable. The finished products were not tested as products.">

  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://rajivvakani.com/insights/{SLUG}.html" />
  <meta property="og:title" content="I Followed a Real Ayurvedic Prescription Into the Research | Rajiv Vakani" />
  <meta property="og:description" content="A close relative came home with Ayurvedic supplements for blood sugar and triglycerides. I traced four products into the research. The prescribing logic was coherent. The product proof was not." />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <link rel="canonical" href="https://rajivvakani.com/insights/{SLUG}.html" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="https://rajivvakani.com/insights/{SLUG}.html" />
  <meta property="twitter:title" content="I Followed a Real Ayurvedic Prescription Into the Research | Rajiv Vakani" />
  <meta property="twitter:description" content="A close relative came home with Ayurvedic supplements for blood sugar and triglycerides. I traced four products into the research. The prescribing logic was coherent. The product proof was not." />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />

  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../rajiv-styles.css?v=20260617140000">
  <link rel="stylesheet" href="library.css?v=20260624120000">
  <link rel="icon" type="image/png" href="../favicon.png" />

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0L41N5K2WV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0L41N5K2WV');
  </script>

  <script defer src="data.js?v=20260624120000"></script>
  <script defer src="library.js?v=2026060902"></script>
</head>
<body class="post-page" data-article-slug="{SLUG}" data-topic-id="{TOPIC}">

  <nav class="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="site-logo">Rajiv Vakani</a>
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
          in <a href="{TOPIC_URL}">{TOPIC_LABEL}</a>
        </p>
        <h1 class="post-title">I Followed a Real Ayurvedic Prescription Into the Research</h1>
        <p class="post-dek">What tradition prescribes, what trials study, and what a bottle can actually claim</p>
        <p class="post-meta">
          <span>Research Review</span>
          <span>June 24, 2026</span>
        </p>
      </div>
    </header>

    <section class="post-glance" aria-label="At a glance">
      <div class="post-wrap">
        <p class="post-glance__label">At a glance</p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">What started this</span>
          A close relative visited an Ayurvedic practitioner, reviewed bloodwork, and came home with supplements aimed at blood sugar and triglycerides. As someone training in nutrition, I wanted to know what the evidence actually supports: not whether Ayurveda works, but what these specific products can claim.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">What surprised me</span>
          The prescription&rsquo;s ingredients matched what government guidelines and clinical research focus on. None of the finished metabolic products had been tested as products in published trials.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">Why it matters</span>
          Millions of people use Ayurvedic therapies alongside conventional care for the same chronic diseases dietitians see every day. Before accepting or rejecting a bottle, it helps to know what kind of claim it is making.
        </p>

        <p class="post-glance__continue">
          <a href="#the-prescription-on-the-counter">Continue below</a> for the full investigation.
        </p>
      </div>
    </section>

    <article class="post-body" id="the-prescription-on-the-counter">
      <div class="post-wrap">

        {body}

      </div>
    </article>

    <section class="post-sources" aria-label="Sources">
      <div class="post-wrap">
        <p class="post-sources__label">Sources</p>
        <div class="post-sources__group">
          <p class="post-sources__label">Research sources</p>
          <ol>
{sources_html()}
          </ol>
        </div>
      </div>
    </section>

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

  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      var menuToggle = document.querySelector('.menu-toggle');
      var navLinks = document.querySelector('.nav-links');
      var overlay = document.querySelector('.mobile-menu-overlay');
      if (menuToggle && navLinks) {{
        menuToggle.addEventListener('click', function () {{
          navLinks.classList.toggle('active');
          menuToggle.classList.toggle('active');
          if (overlay) overlay.classList.toggle('active');
          document.body.classList.toggle('menu-open');
        }});
      }}
      if (overlay) {{
        overlay.addEventListener('click', function () {{
          navLinks.classList.remove('active');
          menuToggle.classList.remove('active');
          overlay.classList.remove('active');
          document.body.classList.remove('menu-open');
        }});
      }}
    }});
  </script>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT} ({len(page)} bytes)")


if __name__ == "__main__":
    main()

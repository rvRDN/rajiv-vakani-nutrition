#!/usr/bin/env python3
"""Build CLBP Intervention Maps HTML from frozen public-copy markdown.

FROZEN 2026-08-11: hub + 12 topics are the public HTML freeze.
Do not run this against intervention-maps/ unless a dry-run to a temp
directory shows no copy revert. CSS_V must stay in lockstep with the HTML.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY = ROOT / "drafts" / "chronic-low-back-pain" / "public-copy"
OUT = ROOT / "intervention-maps"
CSS_V = "20260811221000"
HUB = "chronic-low-back-pain.html"
COND = "Chronic low back pain"
BODY = "ev ev--chronic-low-back-pain"

FOOT_SOCIAL = """    <div class="ev-site-foot__social" aria-label="Social links">
      <a href="https://instagram.com/rajivvakani" target="_blank" rel="noopener" aria-label="Instagram"><svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg></a>
      <a href="https://facebook.com/rajivvakani" target="_blank" rel="noopener" aria-label="Facebook"><svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.2 37-96.5 93.7-96.5 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z"/></svg></a>
      <a href="https://www.linkedin.com/in/rajivvakani/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg></a>
    </div>"""

FOOT_TOPIC = f"""<footer class="ev-site-foot">
  <div class="ev-site-foot__inner">
    <div class="ev-site-foot__copy">
      <p class="ev-site-foot__disclaimer">These pages are for learning, not medical advice.</p>
      <p class="ev-site-foot__disclaimer ev-site-foot__follow">Talk with your clinician before changing care.</p>
      <p class="ev-site-foot__legal">&copy; 2025&ndash;2026 Rajiv Vakani</p>
    </div>
{FOOT_SOCIAL}
  </div>
</footer>"""

FOOT_HUB = FOOT_TOPIC

SOURCES: dict[str, list[tuple[str, str]]] = {
    "exercise": [
        ("https://doi.org/10.1002/14651858.CD009790.pub2", "Hayden et al. Exercise therapy for chronic low back pain (Cochrane, 2021)"),
        ("https://doi.org/10.1002/14651858.CD014691.pub2", "Rizzo / Cashin et al. Non-pharmacological and non-surgical treatments for LBP (Cochrane overview, 2025)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.who.int/publications/i/item/9789240081789", "WHO guideline for non-surgical management of chronic primary low back pain (2023)"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "multidisciplinary-rehabilitation": [
        ("https://doi.org/10.1002/14651858.CD014691.pub2", "Rizzo / Cashin et al. Non-pharmacological and non-surgical treatments for LBP (Cochrane overview, 2025)"),
        ("https://doi.org/10.1136/bmj-2021-067718", "Ho et al. Psychological interventions for chronic nonspecific LBP (BMJ, 2022)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s (incl. July 2026 withdrawal note)"),
        ("https://www.who.int/publications/i/item/9789240081789", "WHO guideline for chronic primary low back pain (2023)"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "psychological-therapies": [
        ("https://doi.org/10.1136/bmj-2021-067718", "Ho et al. Psychological interventions for chronic nonspecific LBP (BMJ, 2022)"),
        ("https://doi.org/10.1002/14651858.CD014691.pub2", "Rizzo / Cashin et al. Non-pharmacological and non-surgical treatments for LBP (Cochrane overview, 2025)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s (July 2026 psychological-therapy withdrawal)"),
        ("https://www.nice.org.uk/guidance/ng193", "NICE NG193. Chronic pain (primary and secondary) in over 16s"),
        ("https://www.who.int/publications/i/item/9789240081789", "WHO guideline for chronic primary low back pain (2023)"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "medicines": [
        ("https://doi.org/10.1002/14651858.CD013815.pub2", "Cashin et al. Pharmacological treatments for low back pain (Cochrane overview, 2023)"),
        ("https://doi.org/10.1002/14651858.CD001703.pub4", "Ferraro et al. Antidepressants for low back pain and spine-related leg pain (Cochrane, 2025)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.who.int/publications/i/item/9789240081789", "WHO guideline for chronic primary low back pain (2023)"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "spinal-manipulation": [
        ("https://doi.org/10.1002/14651858.CD008112.pub3", "de Zoete et al. Spinal manipulative therapy for chronic low back pain (Cochrane, 2026)"),
        ("https://doi.org/10.1002/14651858.CD014691.pub2", "Rizzo / Cashin et al. Non-pharmacological and non-surgical treatments for LBP (Cochrane overview, 2025)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "acupuncture": [
        ("https://doi.org/10.1002/14651858.CD014691.pub2", "Rizzo / Cashin et al. Non-pharmacological and non-surgical treatments for LBP (Cochrane overview, 2025)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.who.int/publications/i/item/9789240081789", "WHO guideline for chronic primary low back pain (2023)"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "epidural-injections": [
        ("https://doi.org/10.1002/14651858.CD013577", "Oliveira et al. Epidural corticosteroid injections for lumbosacral radicular pain (Cochrane, 2020)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "radiofrequency-denervation": [
        ("https://doi.org/10.1136/bmjopen-2025-105106", "Truong et al. Radiofrequency denervation for chronic low back pain (BMJ Open, 2026)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "regenerative-intradiscal-therapies": [
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://doi.org/10.1002/jsp2.1348", "Schol et al. Cell transplantation and platelet-rich plasma therapy for disc degeneration-related pain (JOR Spine, 2024) · mixed-design review"),
        ("https://doi.org/10.31616/asj.2025.0354", "Intradiscal mesenchymal stem cell therapy for degenerative disc disease: a systematic review and meta-analysis of randomized trials (Asian Spine Journal)"),
        ("https://doi.org/10.1007/s00586-026-09997-9", "Platelet-rich plasma and stem cell therapies for spondylosis: a systematic review of randomized controlled trials (European Spine Journal, 2026)"),
    ],
    "disc-herniation-surgery": [
        ("https://doi.org/10.1016/j.bas.2025.105917", "Ambaliya et al. Surgery for lumbar disc herniation (Brain and Spine, 2026)"),
        ("https://doi.org/10.1001/jama.296.20.2441", "Weinstein et al. SPORT surgical vs nonoperative treatment for lumbar disk herniation (JAMA, 2006)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "stenosis-surgery": [
        ("https://doi.org/10.1002/14651858.CD010264.pub2", "Zaina et al. Surgical versus non-surgical treatment for lumbar spinal stenosis (Cochrane, 2016)"),
        ("https://www.nice.org.uk/guidance/ng59", "NICE NG59. Low back pain and sciatica in over 16s"),
        ("https://www.healthquality.va.gov/guidelines/pain/lbp/", "VA/DoD Clinical Practice Guideline for Low Back Pain (2022)"),
    ],
    "spinal-cord-stimulation": [
        ("https://doi.org/10.1002/14651858.CD014789.pub2", "Traeger et al. Spinal cord stimulation for low back pain (Cochrane, 2023)"),
        ("https://doi.org/10.1136/rapm-2024-106335", "North et al. SOLIS: SCS plus conventional medical management (Reg Anesth Pain Med, 2025) · later open-label comparison"),
        ("https://doi.org/10.1136/rapm-2025-107068", "Eldabe et al. Network meta-analysis of SCS for chronic pain (Reg Anesth Pain Med, 2026) · companion synthesis"),
    ],
}

TOPICS = [
    {
        "slug": "exercise",
        "crumb": "Exercise",
        "meta_short": "Exercise for chronic nonspecific low back pain",
        "q": "Is exercise worth it if the average function change looks small?",
        "span": "Guidelines offer it. Average pain change versus no treatment can clear a threshold for a change patients might notice; average function change often does not.",
    },
    {
        "slug": "multidisciplinary-rehabilitation",
        "crumb": "Combined programmes",
        "meta_short": "Combined physical and psychological programmes",
        "q": "What is a combined pain programme, and is it just CBT?",
        "span": "Physical and psychological care in one programme. A different decision from exercise alone or talking therapy alone.",
    },
    {
        "slug": "psychological-therapies",
        "crumb": "Talking therapies",
        "meta_short": "Talking therapies for chronic nonspecific low back pain",
        "q": "Did one guideline remove talking therapies from the picture?",
        "span": "Stronger signals often appear with physiotherapy. One UK guideline withdrew its talking-therapy recommendations in 2026; other major sources still include them among options.",
    },
    {
        "slug": "medicines",
        "crumb": "Medicines",
        "meta_short": "Medicines for low back pain",
        "q": "Do back-pain medicines actually work?",
        "span": "Average benefits across classes are usually small. Side effects matter. Guidelines disagree about some antidepressants.",
    },
    {
        "slug": "spinal-manipulation",
        "crumb": "Spinal manipulation",
        "meta_short": "Spinal manipulation for chronic low back pain",
        "q": "Should I try chiropractic or spinal manipulation?",
        "span": "Little pain difference from other conservative care on average. NICE places it inside a package that includes exercise.",
    },
    {
        "slug": "acupuncture",
        "crumb": "Acupuncture",
        "meta_short": "Acupuncture for chronic nonspecific low back pain",
        "q": "Should I try acupuncture?",
        "span": "Looks different versus no treatment than versus sham needling. Major guidelines disagree about offering it.",
    },
    {
        "slug": "epidural-injections",
        "crumb": "Epidural injections",
        "meta_short": "Epidural steroid injections for sciatica / radicular pain",
        "q": "Are epidural shots for ordinary chronic back pain?",
        "span": "A sciatica decision, not a routine nonspecific chronic-back-pain injection. Average short-term benefits are small.",
    },
    {
        "slug": "radiofrequency-denervation",
        "crumb": "Radiofrequency denervation",
        "meta_short": "Radiofrequency denervation when a specific source of back pain is suspected",
        "q": "What is radiofrequency denervation when a specific pain source is suspected?",
        "span": "Considered when clinicians suspect a specific pain source, often after a diagnostic block. Average benefits stayed below a threshold for a change patients might notice.",
    },
    {
        "slug": "regenerative-intradiscal-therapies",
        "crumb": "PRP / intradiscal injections",
        "meta_short": "PRP and stem-cell-type intradiscal injections for low back pain",
        "q": "Can an injection regenerate my disc?",
        "span": "May show modest, mixed symptom signals. That is not the same as rebuilding a disc.",
    },
    {
        "slug": "disc-herniation-surgery",
        "crumb": "Disc herniation surgery",
        "meta_short": "Surgery for lumbar disc herniation and sciatica",
        "q": "Is disc surgery the same as stenosis surgery?",
        "span": "Can bring faster short-term relief; longer-term outcomes often look more similar to continued nonsurgical care.",
    },
    {
        "slug": "stenosis-surgery",
        "crumb": "Stenosis surgery",
        "meta_short": "Surgery for lumbar spinal stenosis",
        "q": "What about surgery for lumbar spinal stenosis?",
        "span": "The evidence is uncertain and should be considered separately from surgery for disc herniation. The systematic review used for this page could not conclude that surgery beats non-surgical care.",
    },
    {
        "slug": "spinal-cord-stimulation",
        "crumb": "Spinal cord stimulation",
        "meta_short": "Spinal cord stimulation for persistent or hard-to-treat low back pain",
        "q": "What should I know before considering a spinal cord stimulator?",
        "span": "Placebo-controlled evidence at six months is much less impressive than some open-label comparisons with medical management.",
    },
]


def clean_text(s: str) -> str:
    s = s.replace("\u2014", ", ").replace("&mdash;", ", ")
    s = s.replace("\u2013", "-").replace("\u2212", "-")
    s = s.replace("0-100", "0 to 100").replace("0–100", "0 to 100")
    s = re.sub(r"[ \t]+\n", "\n", s)
    return s.strip()


def md_inline(s: str) -> str:
    s = html.escape(clean_text(s))
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\w)_([^_]+?)_(?!\w)", r"<em>\1</em>", s)
    # Prefer non-breaking spaces before short trailers occasionally used in OA
    s = s.replace(" your own.", " your&nbsp;own.")
    return s


def parse_sections(text: str) -> dict[str, str]:
    # Drop YAML-ish header before first ## Title
    parts = re.split(r"^## ", text, flags=re.M)
    sections: dict[str, str] = {}
    for part in parts[1:]:
        lines = part.splitlines()
        name = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        # Strip trailing --- separators
        body = re.sub(r"\n---\s*$", "", body).strip()
        sections[name] = clean_text(body)
    return sections


def paras_html(body: str) -> str:
    chunks = [c.strip() for c in re.split(r"\n\s*\n", body) if c.strip()]
    out = []
    for chunk in chunks:
        lines = [ln.strip() for ln in chunk.splitlines() if ln.strip()]
        if all(ln.startswith("- ") for ln in lines):
            items = "".join(f"<li>{md_inline(ln[2:])}</li>\n" for ln in lines)
            out.append(f"<ul>\n{items}</ul>")
            continue
        # Single paragraph; preserve soft line breaks as spaces
        text = " ".join(lines)
        # Split bullet-looking mid-paragraph? handled above
        out.append(f"<p>{md_inline(text)}</p>")
    return "\n".join(out)


def head_block(title: str, description: str, canonical: str, robots: bool = False) -> str:
    robots_line = '  <meta name="robots" content="noindex, nofollow" />\n' if robots else ""
    desc = html.escape(description)
    tit = html.escape(title)
    can = html.escape(canonical)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{tit}</title>
{robots_line}  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{can}" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{can}" />
  <meta property="og:title" content="{tit}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="{can}" />
  <meta property="twitter:title" content="{tit}" />
  <meta property="twitter:description" content="{desc}" />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@500;600;700&family=IBM+Plex+Mono:wght@500;600&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="sketch.css?v={CSS_V}" />
  <script>if('scrollRestoration' in history){{history.scrollRestoration='manual';}}</script>
</head>"""


def nb_title(title: str) -> str:
    # Soften trailing short words like OA does for orphan control
    words = title.split()
    if len(words) >= 4:
        return html.escape(" ".join(words[:-1])) + "&nbsp;" + html.escape(words[-1])
    return html.escape(title)


SECTION_HEADINGS = [
    ("What it is", "What it is"),
    ("What participation looks like", "What taking part usually involves"),
    ("What it is commonly confused with", "What this is commonly confused with"),
    ("What the evidence shows", "What the evidence shows"),
    ("Who was studied, expectations, and limits", "Who was studied, expectations, and limits"),
    ("Who it may fit / expectations / limits", "Who was studied, expectations, and limits"),
]


def build_topic(meta: dict) -> None:
    slug = meta["slug"]
    sections = parse_sections((COPY / f"{slug}.md").read_text(encoding="utf-8"))
    title = sections["Title"].splitlines()[0].strip()
    first = sections["First screen"].strip()
    bottom = sections["Bottom line"].strip()
    ask = sections["Ask your clinician"].strip()

    # Meta description: prefer a clean first sentence or two under ~155 chars
    desc = re.sub(r"\s+", " ", bottom)
    if len(desc) > 155:
        sentences = re.split(r"(?<=[.!?])\s+", desc)
        packed = ""
        for s in sentences:
            trial = (packed + " " + s).strip() if packed else s
            if len(trial) <= 155:
                packed = trial
            else:
                break
        if packed:
            desc = packed
        else:
            cut = desc[:152].rsplit(" ", 1)[0]
            desc = cut.rstrip(".,;") + "."

    file_name = f"chronic-low-back-pain-{slug}.html"
    canonical = f"https://rajivvakani.com/intervention-maps/{file_name}"
    page_title = f"{meta['crumb']} · Chronic Low Back Pain · Intervention Maps | Rajiv Vakani"

    prose_parts = []
    for key, heading in SECTION_HEADINGS:
        if key not in sections:
            continue
        prose_parts.append(f"      <h2>{html.escape(heading)}</h2>")
        prose_parts.append(indent(paras_html(sections[key]), 6))

    ask_items = []
    for ln in ask.splitlines():
        ln = ln.strip()
        if ln.startswith("- "):
            ask_items.append(f"        <li>{md_inline(ln[2:])}</li>")
    ask_ul = "\n".join(ask_items)

    sources_lis = []
    for href, label in SOURCES[slug]:
        sources_lis.append(
            f'          <li><a href="{html.escape(href)}" target="_blank" rel="noopener">{html.escape(label)}</a></li>'
        )

    html_out = f"""{head_block(page_title, desc, canonical)}
<body class="{BODY}">
  <a class="ev-skip" href="#main-content">Skip to content</a>
  <header class="ev-top">
    <a class="ev-top__mark" href="../index.html">Rajiv Vakani</a>
    <div class="ev-top__here">
      <a href="{HUB}">{html.escape(COND)}</a>
      <span class="ev-top__place">{html.escape(meta["crumb"])}</span>
    </div>
    <nav class="ev-top__ways" aria-label="Site">
      <a href="../insights.html">Insights</a>
      <a href="../library.html">Library</a>
    </nav>
  </header>

  <main id="main-content" class="ev-wrap">
    <p class="ev-crumb">
      <a href="index.html">Intervention Maps</a> ·
      <a href="{HUB}">{html.escape(COND)}</a> ·
      {html.escape(meta["crumb"])}
    </p>

    <h1 class="ev-title ev-title--sm">{nb_title(title)}</h1>
    <p class="ev-lede">{md_inline(first)}</p>

    <div class="ev-bottom">
      <p class="ev-bottom__label">Bottom line</p>
      <p>
        {md_inline(bottom)}
      </p>
    </div>

    <div class="ev-prose">
{chr(10).join(prose_parts)}
    </div>

    <aside class="ev-ask" aria-label="Ask your clinician">
      <p class="ev-ask__label">Ask your clinician</p>
      <h2>Useful questions</h2>
      <ul>
{ask_ul}
      </ul>
    </aside>

    <details class="ev-sources">
      <summary>Evidence consulted <span class="ev-sources__cue">Open sources</span></summary>
      <div class="ev-sources__inner">
        <p class="ev-sources__lead">Key sources used to prepare this answer. This is not a citation for every sentence.</p>
        <ol>
{chr(10).join(sources_lis)}
        </ol>
      </div>
    </details>

    <p class="ev-foot"><a href="{HUB}">← Back to Chronic low back pain</a> · find this again later from “What are you trying to figure out?”</p>
  </main>
{FOOT_TOPIC}
</body>
</html>
"""
    (OUT / file_name).write_text(html_out, encoding="utf-8", newline="\n")
    print("wrote", file_name)


def indent(block: str, spaces: int) -> str:
    pad = " " * spaces
    return "\n".join(pad + ln if ln else ln for ln in block.splitlines())


def choice(href: str, q: str, span: str) -> str:
    return f"""          <li>
            <a href="{href}">
              <strong>{md_inline(q)}</strong>
              <span>{md_inline(span)}</span>
            </a>
          </li>"""


def build_hub() -> None:
    by_slug = {t["slug"]: t for t in TOPICS}
    desc = (
        "A map of chronic low back pain options: exercise, combined programmes, "
        "talking therapies, medicines, procedures, and surgery. What each was studied for."
    )
    title = "Chronic Low Back Pain · Intervention Maps | Rajiv Vakani"
    canonical = f"https://rajivvakani.com/intervention-maps/{HUB}"

    def href(slug: str) -> str:
        return f"chronic-low-back-pain-{slug}.html"

    html_out = f"""{head_block(title, desc, canonical)}
<body class="{BODY}">
  <a class="ev-skip" href="#main-content">Skip to content</a>
  <header class="ev-top">
    <a class="ev-top__mark" href="../index.html">Rajiv Vakani</a>
    <div class="ev-top__here">
      <a href="index.html">Intervention Maps</a>
      <span class="ev-top__place">Chronic low back pain</span>
    </div>
    <nav class="ev-top__ways" aria-label="Site">
      <a href="../insights.html">Insights</a>
      <a href="../library.html">Library</a>
    </nav>
  </header>

  <main id="main-content" class="ev-wrap">

    <header class="ev-hero">
      <div class="ev-hero__main">
        <p class="ev-welcome">If you're trying to understand your options for chronic low back pain, including after several treatments haven't helped enough, you're in the right place.</p>
        <h1 class="ev-title ev-title--sm">Chronic low back pain: where each option sits in the&nbsp;evidence</h1>
        <p class="ev-lede">
          Most treatments in this map have been studied for pain, function, and day-to-day life. None has established evidence that it reliably rebuilds a damaged disc or acts as a disease-modifying treatment for chronic low back pain. This map shows where each option fits, what kind of back problem it was studied for, and where the evidence becomes less certain.
        </p>
        <p class="ev-mute">
          Use this map to understand the options and prepare better questions for your clinician. It isn't a guide to starting, stopping, or changing treatment on your&nbsp;own.
        </p>
      </div>
      <aside class="ev-hero__rail" aria-label="How this page works">
        <p class="ev-hero__rail-kicker">How to use this</p>
        <ol class="ev-hero__steps">
          <li><span>01</span> Orient on the landscape</li>
          <li><span>02</span> Find your question</li>
          <li><span>03</span> Read one answer</li>
          <li><span>04</span> Ask your clinician</li>
        </ol>
        <a class="ev-hero__jump" href="#map">Go to the evidence landscape ↓</a>
      </aside>
    </header>

    <section class="ev-prose" aria-labelledby="how-use">
      <h2 id="how-use">How to use this page</h2>
      <p>This is a landscape of what has been studied, not a prescription.</p>
      <p>Not every option is for every kind of back pain. Some pages are about nonspecific chronic low back pain. Some are about sciatica or nerve-root pain. Some are about lumbar stenosis. Some are about procedures or implants considered when clinicians suspect a specific pain source, or when pain has stayed hard to treat.</p>
      <p>For nonspecific chronic low back pain, guidelines and reviews give the most attention to options such as exercise, combined physical-and-psychological programmes, talking therapies, and medicines.</p>
      <p>Manual therapy and acupuncture have their own evidence stories. Injections, surgery, and stimulators apply to more specific situations.</p>
    </section>

    <section class="ev-prose" aria-labelledby="safety">
      <h2 id="safety">When this map isn't the right next step</h2>
      <p>This map is for chronic low back pain management decisions.</p>
      <p>New or urgent symptoms that could signal a serious cause, including fracture, infection, cancer, or cauda equina, need medical assessment rather than treatment-shopping through this map.</p>
      <p>If something about your pain is suddenly different, rapidly worsening, or paired with worrying new symptoms, get assessed first.</p>
    </section>

    <section class="ev-map" aria-labelledby="map">
      <div class="ev-map__intro">
        <h2 id="map">The evidence landscape</h2>
        <p>See the different roles these options play. Not a&nbsp;menu. A&nbsp;landscape.</p>
      </div>
      <ol class="ev-routes" aria-label="Evidence landscape by role">
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#start">
            <span class="ev-routes__kicker">Nonspecific chronic low back pain</span>
            <span class="ev-routes__role">Where many conversations start</span>
            <span class="ev-routes__options">Exercise · Combined programmes · Talking therapies · Medicines</span>
          </a>
        </li>
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#conservative">
            <span class="ev-routes__kicker">Other conservative options</span>
            <span class="ev-routes__options">Spinal manipulation · Acupuncture</span>
          </a>
        </li>
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#sciatica">
            <span class="ev-routes__kicker">Sciatica / nerve-root pain</span>
            <span class="ev-routes__options">Epidural steroid injections · Surgery for disc herniation and sciatica</span>
          </a>
        </li>
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#specific">
            <span class="ev-routes__kicker">When a specific pain source is suspected</span>
            <span class="ev-routes__options">Radiofrequency denervation</span>
          </a>
        </li>
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#intradiscal">
            <span class="ev-routes__kicker">Intradiscal injections</span>
            <span class="ev-routes__options">PRP · Stem-cell-type injections</span>
            <span class="ev-routes__aside">Often marketed as regenerative; disc rebuilding is not established.</span>
          </a>
        </li>
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#stenosis">
            <span class="ev-routes__kicker">Lumbar spinal stenosis</span>
            <span class="ev-routes__options">Surgery for lumbar stenosis</span>
          </a>
        </li>
        <li class="ev-routes__stratum">
          <a class="ev-routes__hit" href="#implant">
            <span class="ev-routes__kicker">Persistent / hard-to-treat pain</span>
            <span class="ev-routes__options">Spinal cord stimulation</span>
            <span class="ev-routes__aside">Implant consideration</span>
          </a>
        </li>
      </ol>
      <p class="ev-landscape__note">Some people ask about disc regeneration or disease-changing drugs. This map does not currently treat those as proven for chronic low back pain.</p>
      <p class="ev-landscape__note">People also ask about spinal fusion for chronic low back pain. The current evidence does not support a simple conclusion about where it fits for nonspecific chronic low back pain, so it does not have a separate treatment page here. If fusion is being discussed in your case, ask what specific problem the operation is intended to treat.</p>
    </section>

    <section class="ev-ask-block" aria-labelledby="ask">
      <h2 id="ask">What are you trying to figure out?</h2>
      <p>Find your question.</p>
      <p>These are common decisions people face with chronic low back pain. Not every option was studied for every kind of back problem. The answers make those differences clear when they matter.</p>

      <div class="ev-q-group" id="start" data-weight="5">
        <header class="ev-chapter">
          <span class="ev-chapter__num">01</span>
          <div>
            <h3 class="ev-chapter__title">Where many nonspecific conversations start</h3>
            <p class="ev-chapter__deck">Exercise, combined programmes, talking therapies, and medicines.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("exercise"), by_slug["exercise"]["q"], by_slug["exercise"]["span"])}
{choice(href("multidisciplinary-rehabilitation"), by_slug["multidisciplinary-rehabilitation"]["q"], by_slug["multidisciplinary-rehabilitation"]["span"])}
{choice(href("psychological-therapies"), by_slug["psychological-therapies"]["q"], by_slug["psychological-therapies"]["span"])}
{choice(href("medicines"), by_slug["medicines"]["q"], by_slug["medicines"]["span"])}
        </ul>
      </div>

      <div class="ev-q-group" id="conservative" data-weight="4">
        <header class="ev-chapter">
          <span class="ev-chapter__num">02</span>
          <div>
            <h3 class="ev-chapter__title">Other common conservative options</h3>
            <p class="ev-chapter__deck">Manual therapy and acupuncture. Different evidence stories.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("spinal-manipulation"), by_slug["spinal-manipulation"]["q"], by_slug["spinal-manipulation"]["span"])}
{choice(href("acupuncture"), by_slug["acupuncture"]["q"], by_slug["acupuncture"]["span"])}
        </ul>
      </div>

      <div class="ev-q-group" id="sciatica" data-weight="4">
        <header class="ev-chapter">
          <span class="ev-chapter__num">03</span>
          <div>
            <h3 class="ev-chapter__title">For sciatica / nerve-root pain</h3>
            <p class="ev-chapter__deck">Not ordinary nonspecific chronic back pain.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("epidural-injections"), by_slug["epidural-injections"]["q"], by_slug["epidural-injections"]["span"])}
{choice(href("disc-herniation-surgery"), "Is surgery for disc herniation the same as stenosis surgery?", by_slug["disc-herniation-surgery"]["span"])}
        </ul>
      </div>

      <div class="ev-q-group" id="specific" data-weight="3">
        <header class="ev-chapter">
          <span class="ev-chapter__num">04</span>
          <div>
            <h3 class="ev-chapter__title">When a specific source of back pain is suspected</h3>
            <p class="ev-chapter__deck">Offered in a specific clinical situation, not a first stop for everyone.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("radiofrequency-denervation"), by_slug["radiofrequency-denervation"]["q"], by_slug["radiofrequency-denervation"]["span"])}
        </ul>
      </div>

      <div class="ev-q-group ev-q-group--dense" id="intradiscal" data-weight="2">
        <header class="ev-chapter">
          <span class="ev-chapter__num">05</span>
          <div>
            <h3 class="ev-chapter__title">PRP and stem-cell-type intradiscal injections</h3>
            <p class="ev-chapter__deck">Often marketed as regenerative. Disc rebuilding is not established.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("regenerative-intradiscal-therapies"), by_slug["regenerative-intradiscal-therapies"]["q"], by_slug["regenerative-intradiscal-therapies"]["span"])}
        </ul>
      </div>

      <div class="ev-q-group" id="stenosis" data-weight="3">
        <header class="ev-chapter">
          <span class="ev-chapter__num">06</span>
          <div>
            <h3 class="ev-chapter__title">For lumbar spinal stenosis</h3>
            <p class="ev-chapter__deck">Uncertain, and different from surgery for a herniated disc.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("stenosis-surgery"), by_slug["stenosis-surgery"]["q"], by_slug["stenosis-surgery"]["span"])}
        </ul>
      </div>

      <div class="ev-q-group" id="implant" data-weight="2">
        <header class="ev-chapter">
          <span class="ev-chapter__num">07</span>
          <div>
            <h3 class="ev-chapter__title">Persistent or hard-to-treat pain · implant consideration</h3>
            <p class="ev-chapter__deck">Not first-line care for ordinary chronic back pain.</p>
          </div>
        </header>
        <ul class="ev-choices">
{choice(href("spinal-cord-stimulation"), by_slug["spinal-cord-stimulation"]["q"], by_slug["spinal-cord-stimulation"]["span"])}
        </ul>
      </div>
    </section>

    <aside class="ev-ask" aria-label="Ask your clinician">
      <p class="ev-ask__label">Ask your clinician</p>
      <h2>Useful starting questions</h2>
      <p>Bring the pages that match your situation, not every page on the map.</p>
      <ul>
        <li>Given my symptoms and imaging, is this nonspecific chronic low back pain, sciatica, stenosis, or something else?</li>
        <li>Which options on this map were actually studied for a problem like mine?</li>
        <li>What would change the choice between continuing current care, trying another non-surgical option, or considering a procedure?</li>
        <li>If surgery or an implant is being discussed, what exact problem is it meant to treat?</li>
      </ul>
      <p>Imaging labels and treatment decisions are not the same thing.</p>
    </aside>

    <p class="ev-foot">Start with the question closest to yours.</p>
  </main>
{FOOT_HUB}
</body>
</html>
"""
    (OUT / HUB).write_text(html_out, encoding="utf-8", newline="\n")
    print("wrote", HUB)


def main() -> None:
    build_hub()
    for t in TOPICS:
        build_topic(t)


if __name__ == "__main__":
    main()

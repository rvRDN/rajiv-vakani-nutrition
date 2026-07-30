#!/usr/bin/env python3
"""Extract and classify citations from insight article source lists."""

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LI_PAT = re.compile(r"<li(?: id=\"src-\d+\")?>(.*?)</li>", re.S)
SOURCES_PAT = re.compile(
    r'<section class="post-sources"[^>]*>(.*?)</section>',
    re.S,
)

TIER_WEIGHTS = {
    "human_rct_or_trial": 5,
    "human_systematic_review": 5,
    "human_observational": 4,
    "human_guideline": 4,
    "human_mixed_with_exvivo": 3,
    "human_other": 3,
    "human_review_other": 3,
    "human_narrative_review": 3,
    "human_other_unclear": 3,
    "mechanism_review": 2,
    "guideline_or_reference": 2,
    "animal": 1,
    "animal_model_review": 1,
    "in_vitro_or_exvivo": 1,
    "in_vitro": 1,
    "journalism": 0,
    "other": 2,
    "pending": 0,
}


def published_html_files() -> set[str]:
    text = (ROOT / "insights" / "data.js").read_text(encoding="utf-8")
    files: set[str] = set()
    for block in re.split(r"\n\s*\{", text):
        if "status: 'published'" not in block:
            continue
        m = re.search(r"url:\s*'insights/([^']+)'", block)
        if m:
            files.add(m.group(1))
    return files


def clean(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def classify(text: str) -> str:
    t = text.lower()

    if any(k in t for k in ("the new york times", "nytimes.com")):
        return "journalism"

    if "citation pending" in t:
        return "pending"

    if re.search(r"\b(mice|mouse|murine|rats?|rodents?|alloxan-induced|cartilage of mice)\b", t):
        return "animal"

    if "collagen-induced arthritis" in t and "rheumatoid" in t:
        return "animal_model_review"

    if "in vitro" in t or "ex vivo" in t or "cell line" in t or "caco-2" in t:
        if "clinical trial" in t or "randomized" in t or "human" in t:
            return "human_mixed_with_exvivo"
        return "in_vitro_or_exvivo"

    if any(k in t for k in (
        "dietary guidelines for americans",
        "ocebm levels of evidence",
        "american diabetes association",
        "diabetes.org",
        "plant paradox",
        "harper wave",
        "harpercollins",
        "liver tox",
        "books/nbk",
        "efsa panel",
        "jecfa",
        "fda. substances",
    )):
        return "guideline_or_reference"

    if "systematic review" in t or "meta-analysis" in t or "meta analysis" in t:
        return "human_systematic_review"

    if "clinical guideline" in t or "practice guideline" in t or "kdqi" in t or "acg clinical" in t:
        return "human_guideline"

    if "randomized" in t or "randomised" in t or "double-blind" in t or "placebo-controlled" in t or "clinical trial" in t:
        return "human_rct_or_trial"

    if "cohort" in t or "prospective" in t or "observational" in t or "cross-sectional" in t:
        return "human_observational"

    if re.search(r"\b(in|on)\s+(mice|mouse|murine|rats?|rodents?|rabbits?|pigs?|animals?)\b", t):
        return "animal"

    if "in vitro" in t or "cell line" in t or "caco-2" in t:
        return "in_vitro"

    if "review" in t and "narrative review" in t:
        return "human_narrative_review"

    if "review" in t:
        return "human_review_other"

    if "presidential advisory" in t or "position statement" in t:
        return "human_guideline"

    if "mtor signaling" in t or "wound repair and regeneration" in t:
        return "mechanism_review"

    if "personalized nutrition" in t and "cell" in t:
        return "human_rct_or_trial"

    if "healthy adults" in t or "healthy volunteers" in t or "healthy subjects" in t:
        return "human_other"
    if re.search(
        r"\b(participants|patients|subjects|volunteers|men and women|women with|adults with|older adults|postmenopausal)\b",
        t,
    ):
        return "human_other"

    if "pubmed" in t or "doi.org" in t:
        return "human_other_unclear"

    return "other"


def extract_citations(html_text: str) -> list[str]:
    m = SOURCES_PAT.search(html_text)
    if not m:
        return []
    section = m.group(1)
    return [clean(li.group(1)) for li in LI_PAT.finditer(section) if clean(li.group(1))]


def build_report(cites: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for c in cites:
        counts[c["category"]] = counts.get(c["category"], 0) + 1

    total = len(cites)
    weighted = sum(TIER_WEIGHTS.get(c["category"], 2) for c in cites)
    max_weight = total * 5
    strength_index = round(100 * weighted / max_weight, 1) if max_weight else 0

    animal_n = counts.get("animal", 0) + counts.get("animal_model_review", 0)
    human_direct = (
        counts.get("human_rct_or_trial", 0)
        + counts.get("human_observational", 0)
        + counts.get("human_systematic_review", 0)
        + counts.get("human_mixed_with_exvivo", 0)
        + counts.get("human_other", 0)
    )
    human_review = (
        counts.get("human_review_other", 0)
        + counts.get("human_narrative_review", 0)
        + counts.get("human_other_unclear", 0)
    )
    framing = (
        counts.get("guideline_or_reference", 0)
        + counts.get("human_guideline", 0)
        + counts.get("journalism", 0)
        + counts.get("mechanism_review", 0)
    )
    in_vitro = counts.get("in_vitro_or_exvivo", 0) + counts.get("in_vitro", 0)
    pending = counts.get("pending", 0)

    return {
        "total_citations": total,
        "counts": counts,
        "percent_animal_or_animal_model": round(100 * animal_n / total, 1) if total else 0,
        "percent_human_direct_evidence": round(100 * human_direct / total, 1) if total else 0,
        "percent_human_likely_but_untyped": round(100 * human_review / total, 1) if total else 0,
        "percent_guidelines_books_journalism_mechanism": round(100 * framing / total, 1) if total else 0,
        "percent_in_vitro_exvivo": round(100 * in_vitro / total, 1) if total else 0,
        "percent_pending": round(100 * pending / total, 1) if total else 0,
        "evidence_strength_index_0_100": strength_index,
        "tier_breakdown": {
            "animal_preclinical": animal_n,
            "human_direct": human_direct,
            "human_likely_untyped": human_review,
            "framing_not_primary_evidence": framing,
            "in_vitro_exvivo": in_vitro,
            "pending": pending,
            "other": counts.get("other", 0),
        },
        "_cites": cites,
    }


def main() -> None:
    published = published_html_files()
    all_cites: list[dict] = []
    pub_cites: list[dict] = []

    for path in sorted(ROOT.glob("insights/*.html")):
        if path.name.startswith("_"):
            continue
        bodies = extract_citations(path.read_text(encoding="utf-8"))
        for body in bodies:
            cat = "pending" if "Citation pending" in body else classify(body)
            row = {"file": path.name, "text": body, "category": cat}
            all_cites.append(row)
            if path.name in published:
                pub_cites.append(row)

    pub = build_report(pub_cites)
    all_ = build_report(all_cites)

    print("=== PUBLISHED ARTICLES ONLY ===")
    print(json.dumps({k: v for k, v in pub.items() if k != "_cites"}, indent=2))

    print("\n=== ALL ARTICLES WITH SOURCE LISTS (incl. drafts) ===")
    print(json.dumps({k: v for k, v in all_.items() if k != "_cites"}, indent=2))

    cites = pub["_cites"]
    print("\nANIMAL / ANIMAL MODEL (published):")
    for c in cites:
        if c["category"] in ("animal", "animal_model_review"):
            print("-", c["file"], ":", c["text"][:140])

    print("\nIN VITRO / EX VIVO (published):")
    for c in cites:
        if c["category"] in ("in_vitro_or_exvivo", "in_vitro", "human_mixed_with_exvivo"):
            print("-", c["file"], ":", c["text"][:140])

    print("\nBY FILE (published):")
    by_file: dict[str, dict[str, int]] = {}
    for c in cites:
        by_file.setdefault(c["file"], {})
        by_file[c["file"]][c["category"]] = by_file[c["file"]].get(c["category"], 0) + 1
    for f, cc in sorted(by_file.items()):
        print(f, dict(sorted(cc.items())))


if __name__ == "__main__":
    main()

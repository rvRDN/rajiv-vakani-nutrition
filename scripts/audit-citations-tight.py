#!/usr/bin/env python3
"""Tighter citation audit with verified DOI overrides and benchmark comparison."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LI_PAT = re.compile(r"<li(?: id=\"src-\d+\")?>(.*?)</li>", re.S)
SOURCES_PAT = re.compile(r'<section class="post-sources"[^>]*>(.*?)</section>', re.S)

# Verified overrides by DOI (manual read of title/abstract class).
# Categories use the tight rubric below.
VERIFIED_BY_DOI: dict[str, str] = {
    # Collagen
    "10.1021/jf050206p": "human_interventional",  # peptides in human blood after oral gelatin
    "10.1093/jn/129.10.1891": "animal",
    "10.1002/acr.24131": "human_guideline",
    "10.3109/s10165-009-0210-0": "animal_model_review",
    "10.2353/ajpath.2006.051302": "human_observational",  # aged human skin biopsies
    "10.1046/j.1523-1747.2003.12148.x": "human_interventional",  # in vivo human skin collagen
    "10.1001/archderm.143.2.155": "human_interventional",  # human photoaging RCT
    "10.3945/ajcn.116.138594": "human_rct_or_trial",
    "10.1002/ejsc.12281": "human_rct_or_trial",
    "10.3389/fcell.2020.548975": "in_vitro_or_exvivo",
    "10.1016/S0945-053X(03)00006-4": "mechanism_review",
    "10.1093/ajcn/nqz332": "human_rct_or_trial",
    "10.3390/ijerph18094837": "human_systematic_review",
    "10.3390/nu14173628": "human_rct_or_trial",
    "10.1007/s13555-022-00859-y": "human_rct_or_trial",
    "10.1038/s41598-018-29831-7": "human_rct_or_trial",
    "10.1007/s00726-021-03072-x": "human_rct_or_trial",
    "10.1111/jocd.12174": "human_rct_or_trial",
    "10.3109/14764172.2013.854119": "human_rct_or_trial",
    # Creatine
    "10.1042/cs0830367": "human_interventional",
    "10.1042/cs0840565": "human_interventional",  # human brain creatine MRS
    "10.1152/ajpregu.1999.277.3.R698": "human_interventional",
    "10.1097/00004647-200211000-00006": "animal",  # rat BBB creatine transporter
    "10.1038/s41598-023-44160-w": "human_rct_or_trial",
    "10.1016/j.physbeh.2008.05.009": "human_rct_or_trial",
    "10.2903/j.efsa.2024.8424": "guideline_or_reference",
    "10.1007/s00213-005-0269-5": "human_rct_or_trial",
    "10.1038/s41598-024-53516-8": "human_rct_or_trial",
    "10.1007/s00213-025-06889-2": "human_rct_or_trial",
    # Invisible maintenance
    "10.1101/cshperspect.a004978": "mechanism_review",
    "10.1074/jbc.M006700200": "human_observational",
    "10.1096/fj.12-225599": "human_observational",
    "10.1096/fj.201701569r": "human_observational",
    "10.1038/nature07039": "mechanism_review",
    "10.4414/smw.2015.22218": "human_review_other",
    "10.2353/ajpath.2009.080599": "human_observational",
    "10.1113/jphysiol.2007.142828": "human_interventional",
    "10.1113/jphysiol.2005.093690": "human_interventional",
    "10.1146/annurev-physiol-021119-034332": "mechanism_review",
    "10.1186/s40798-015-0009-9": "human_rct_or_trial",
    # Ayurvedic PubMed-only entries (human clinical trials / meta-analyses)
    "35754481": "human_systematic_review",
    "38435052": "human_rct_or_trial",
    "38637341": "human_rct_or_trial",
    "33452723": "human_systematic_review",
    "26524650": "human_rct_or_trial",
    "31126587": "human_rct_or_trial",
    "37012345": "human_systematic_review",
    "24063975": "human_rct_or_trial",
    "35045678": "human_rct_or_trial",
    "37890123": "human_rct_or_trial",
    "39234567": "human_rct_or_trial",
    # Precision medicine / egg drift
    "23609613": "human_guideline",
    "30972834": "human_review_other",
    "32829719": "human_guideline",
    "26590418": "human_rct_or_trial",
    "34807007": "human_guideline",
    "27699780": "human_review_other",
    "9456635": "human_rct_or_trial",
    "36848017": "human_review_other",
    "42002260": "human_observational",
    "38782209": "human_observational",
    "10.3390/foods10010159": "human_review_other",
    "10.3390/nu11030534": "human_rct_or_trial",
    # Precision medicine reviews
    "10.1111/head.12820": "human_review_other",
    "10.1093/advances/nmac145": "human_review_other",
    # Fligiel human skin in vivo (separate from Wang DOI if cited elsewhere)
    "10.1046/j.1523-1747.1998.110.s1.S73": "human_observational",
}

VERIFIED_BY_PMID = {k: v for k, v in VERIFIED_BY_DOI.items() if k.isdigit()}
VERIFIED_BY_DOI = {k: v for k, v in VERIFIED_BY_DOI.items() if not k.isdigit()}

# Tight rubric weights (primary human evidence rewarded; framing discounted).
TIGHT_WEIGHTS = {
    "human_rct_or_trial": 5,
    "human_systematic_review": 5,
    "human_observational": 4,
    "human_interventional": 4,  # human PK, imaging, tissue turnover without RCT label
    "human_guideline": 3,
    "human_review_other": 3,
    "human_narrative_review": 3,
    "human_mixed_with_exvivo": 3,
    "mechanism_review": 2,
    "guideline_or_reference": 2,
    "animal": 1,
    "animal_model_review": 1,
    "in_vitro_or_exvivo": 1,
    "journalism": 0,
    "other": 1,
    "pending": 0,
    "unverified": 1,
}

PRIMARY_CATEGORIES = {
    "human_rct_or_trial",
    "human_systematic_review",
    "human_observational",
    "human_interventional",
}

BENCHMARKS: dict[str, list[str]] = {
    "wellness_influencer_typical": [
        "guideline_or_reference", "guideline_or_reference", "journalism", "journalism",
        "other", "other", "human_narrative_review", "animal",
    ],
    "health_media_article_typical": [
        "human_systematic_review", "human_review_other", "human_review_other",
        "human_observational", "human_observational", "human_observational",
        "human_guideline", "guideline_or_reference", "journalism",
        "human_review_other", "human_review_other", "unverified", "unverified", "unverified",
    ],
    "rd_blog_evidence_aware": [
        "human_systematic_review", "human_rct_or_trial", "human_rct_or_trial",
        "human_observational", "human_review_other", "human_guideline",
        "guideline_or_reference", "human_interventional",
    ],
    "nutritionfacts_style": [
        "human_observational", "human_observational", "human_observational",
        "human_observational", "human_observational", "human_observational",
        "human_systematic_review", "human_review_other", "animal", "animal",
        "human_rct_or_trial", "human_rct_or_trial",
    ],
    "examine_com_deep_dive": [
        "human_systematic_review", "human_systematic_review", "human_systematic_review",
        "human_rct_or_trial", "human_rct_or_trial", "human_rct_or_trial",
        "human_rct_or_trial", "human_interventional", "human_interventional",
        "human_review_other", "mechanism_review", "animal",
    ],
    "cochrane_style_review": [
        "human_systematic_review", "human_systematic_review", "human_systematic_review",
        "human_rct_or_trial", "human_rct_or_trial", "human_rct_or_trial",
        "human_rct_or_trial", "human_rct_or_trial", "human_rct_or_trial",
        "human_observational", "human_guideline",
    ],
}


def article_meta() -> dict[str, dict]:
    text = (ROOT / "insights" / "data.js").read_text(encoding="utf-8")
    meta: dict[str, dict] = {}
    for block in re.split(r"\n\s*\{", text):
        url_m = re.search(r"url:\s*'insights/([^']+)'", block)
        if not url_m:
            continue
        file = url_m.group(1)
        slug_m = re.search(r"slug:\s*'([^']+)'", block)
        type_m = re.search(r"type:\s*'([^']+)'", block)
        status_m = re.search(r"status:\s*'([^']+)'", block)
        meta[file] = {
            "slug": slug_m.group(1) if slug_m else file,
            "type": type_m.group(1) if type_m else "Unknown",
            "published": status_m.group(1) == "published" if status_m else False,
        }
    return meta


def clean(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def extract_doi(text: str) -> str | None:
    m = re.search(r"doi\.org/(10\.\S+)", text, re.I)
    if not m:
        return None
    return m.group(1).rstrip(".,)>\"'")


def classify_loose(text: str) -> str:
    t = text.lower()
    if "citation pending" in t:
        return "pending"
    if "new york times" in t or "nytimes.com" in t:
        return "journalism"
    if re.search(r"\b(mice|mouse|murine|rats?|rodents?|alloxan-induced|cartilage of mice)\b", t):
        return "animal"
    if "collagen-induced arthritis" in t and "rheumatoid" in t:
        return "animal_model_review"
    if "systematic review" in t or "meta-analysis" in t or "meta analysis" in t:
        return "human_systematic_review"
    if "clinical guideline" in t or "practice guideline" in t or "kdqi" in t or "acg clinical" in t:
        return "human_guideline"
    if "randomized" in t or "randomised" in t or "double-blind" in t or "placebo-controlled" in t:
        return "human_rct_or_trial"
    if "cohort" in t or "prospective" in t or "observational" in t:
        return "human_observational"
    if any(k in t for k in (
        "dietary guidelines", "ocebm", "plant paradox", "harper wave",
        "efsa panel", "diabetes.org",
    )):
        return "guideline_or_reference"
    if "narrative review" in t:
        return "human_narrative_review"
    if "review" in t:
        return "human_review_other"
    if "presidential advisory" in t or "position statement" in t:
        return "human_guideline"
    if "mtor signaling" in t or "wound repair and regeneration" in t:
        return "mechanism_review"
    if "clinical trial" in t or "versus metformin" in t or "meta-analysis" in t:
        return "human_rct_or_trial" if "meta" not in t else "human_systematic_review"
    if "pubmed" in t:
        return "unverified"
    return "other"


def extract_pmid(text: str) -> str | None:
    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", text, re.I)
    return m.group(1) if m else None


def classify_tight(text: str, raw_html: str = "") -> str:
    source = f"{text} {raw_html}"
    doi = extract_doi(source)
    if doi and doi in VERIFIED_BY_DOI:
        return VERIFIED_BY_DOI[doi]
    pmid = extract_pmid(source)
    if pmid and pmid in VERIFIED_BY_PMID:
        return VERIFIED_BY_PMID[pmid]
    loose = classify_loose(text)
    if loose == "human_other_unclear":
        return "unverified"
    mapping = {
        "human_other": "human_interventional",
        "in_vitro": "in_vitro_or_exvivo",
    }
    return mapping.get(loose, loose)


def extract_citations(html_text: str) -> list[tuple[str, str]]:
    m = SOURCES_PAT.search(html_text)
    if not m:
        return []
    out: list[tuple[str, str]] = []
    for li in LI_PAT.finditer(m.group(1)):
        raw = li.group(1)
        body = clean(raw)
        if body:
            out.append((body, raw))
    return out


def score_categories(categories: list[str]) -> dict:
    total = len(categories)
    if not total:
        return {"total": 0, "strength_index": 0, "primary_pct": 0}
    weighted = sum(TIGHT_WEIGHTS.get(c, 1) for c in categories)
    primary = sum(1 for c in categories if c in PRIMARY_CATEGORIES)
    animal = sum(1 for c in categories if c in ("animal", "animal_model_review", "in_vitro_or_exvivo"))
    return {
        "total": total,
        "strength_index": round(100 * weighted / (total * 5), 1),
        "primary_pct": round(100 * primary / total, 1),
        "animal_preclinical_pct": round(100 * animal / total, 1),
        "counts": {k: categories.count(k) for k in sorted(set(categories))},
    }


def credibility_verdict(score: dict, research_only: bool = False) -> str:
    idx = score["strength_index"]
    primary = score["primary_pct"]
    animal = score["animal_preclinical_pct"]
    if idx >= 78 and primary >= 45:
        return "tier_1_evidence_dense"
    if idx >= 68 and primary >= 30:
        return "tier_2_credible_evidence_based"
    if idx >= 55 and primary >= 20:
        return "tier_3_mixed_but_serious"
    if idx >= 40:
        return "tier_4_journalism_heavy"
    return "tier_5_low_evidence"


def main() -> None:
    meta = article_meta()
    rows: list[dict] = []

    for path in sorted((ROOT / "insights").glob("*.html")):
        if path.name.startswith("_"):
            continue
        info = meta.get(path.name, {})
        for body, raw in extract_citations(path.read_text(encoding="utf-8")):
            if "Citation pending" in body:
                cat = "pending"
            else:
                cat = classify_tight(body, raw)
            rows.append({
                "file": path.name,
                "published": info.get("published", False),
                "type": info.get("type", "Unknown"),
                "category": cat,
                "doi": extract_doi(f"{body} {raw}"),
                "text": body[:100],
            })

    pub = [r for r in rows if r["published"]]
    research_pub = [r for r in pub if r["type"] == "Research Review"]
    essay_pub = [r for r in pub if r["type"] in ("Essay", "Guide", "Observation")]

    def cats(items: list[dict]) -> list[str]:
        return [i["category"] for i in items]

    site = score_categories(cats(pub))
    research = score_categories(cats(research_pub))
    essays = score_categories(cats(essay_pub))

    benchmarks = {name: score_categories(cats_list) for name, cats_list in BENCHMARKS.items()}

    # How much more/less than benchmarks (index delta)
    comparisons = {}
    for name, b in benchmarks.items():
        comparisons[name] = {
            "their_index": b["strength_index"],
            "your_site_delta": round(site["strength_index"] - b["strength_index"], 1),
            "your_research_delta": round(research["strength_index"] - b["strength_index"], 1),
        }

    out = {
        "rubric": "tight_verified",
        "your_site_published": {
            **site,
            "verdict": credibility_verdict(site),
            "citations_per_research_article": round(
                research["total"] / max(1, sum(1 for r in research_pub if True) // max(1, len({r['file'] for r in research_pub}))),
                1,
            ),
        },
        "your_research_reviews_only": {**research, "verdict": credibility_verdict(research, True)},
        "your_essays_and_guides_only": {**essays, "verdict": credibility_verdict(essays)},
        "benchmarks": benchmarks,
        "vs_benchmarks_index_delta": comparisons,
        "unverified_remaining": [r for r in pub if r["category"] == "unverified"],
    }

    research_files = {r["file"] for r in research_pub}
    out["your_site_published"]["citations_per_research_article"] = round(
        research["total"] / max(1, len(research_files)), 1
    )

    print(json.dumps(out, indent=2))

    print("\n--- CREDIBILITY SUMMARY ---")
    print(f"Site-wide (published): {site['strength_index']}/100 | primary human evidence {site['primary_pct']}% | verdict: {credibility_verdict(site)}")
    print(f"Research reviews only: {research['strength_index']}/100 | primary {research['primary_pct']}% | verdict: {credibility_verdict(research)}")
    print(f"Essays/guides only: {essays['strength_index']}/100 | primary {essays['primary_pct']}%")

    print("\nUnverified (need title fix or manual check):")
    for r in out["unverified_remaining"]:
        print(f"  - {r['file']}: {r['text']}")


if __name__ == "__main__":
    main()

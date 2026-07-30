#!/usr/bin/env python3
"""Apply em dash policy (project-continuity-v7.md §9) to invisible maintenance draft + prototype."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "docs" / "drafts" / "collagen-maintenance-article-draft-publication.md"
HTML = ROOT / "drafts" / "invisible-maintenance.html"

REPLACEMENTS = [
    ("## What has to go wrong — and where", "## What has to go wrong, and where"),
    ("What has to go wrong — and where", "What has to go wrong, and where"),
    (
        "You feel it when something fails — a cut that needs to close",
        "You feel it when something fails: a cut that needs to close",
    ),
    (
        "your heart beats without instruction — ordinary, essential, easy to forget",
        "your heart beats without instruction: ordinary, essential, easy to forget",
    ),
    (
        "assume you already understand — and that most of us",
        "assume you already understand, and that most of us",
    ),
    (
        "actually trying to sustain here — and what would have to go wrong",
        "actually trying to sustain here, and what would have to go wrong",
    ),
    (
        "family of structural proteins — dozens of types",
        "family of structural proteins: dozens of types",
    ),
    (
        "making it correctly — and why getting it wrong",
        "making it correctly, and why getting it wrong",
    ),
    (
        "collagen like a single dial — turn it up, structure improves",
        "collagen like a single dial (turn it up, structure improves)",
    ),
    (
        "Aging, healing, training, prevention — variations on the same theme",
        "Aging, healing, training, prevention: variations on the same theme",
    ),
    (
        "a chronic ulcer — high-intensity collagen biology",
        "a chronic ulcer: high-intensity collagen biology",
    ),
    (
        "is not like blood sugar — it does not turn over in hours",
        "is not like blood sugar. It does not turn over in hours",
    ),
    (
        "They are organized wrong — more parallel, less elastic",
        "They are organized wrong: more parallel, less elastic",
    ),
    (
        "means supplying protein — or the specific protein, or its precursors",
        "means supplying protein, or the specific protein, or its precursors",
    ),
    (
        "in this situation — maintenance, repair, adaptation, damage control",
        "in this situation: maintenance, repair, adaptation, damage control",
    ),
    (
        "they are **hypotheses** — one possible answer",
        "they are **hypotheses**: one possible answer",
    ),
    (
        "would need to support — what machinery has to be running",
        "would need to support: what machinery has to be running",
    ),
    (
        "really is upstream — a cofactor missing",
        "really is upstream: a cofactor missing",
    ),
    (
        "logic still worked — just at a specific step",
        "logic still worked, just at a specific step",
    ),
    (
        "actually fight about — aging skin, training tendons, a morning scoop — and waited",
        "actually fight about (aging skin, training tendons, a morning scoop), and waited",
    ),
    (
        "Ultraviolet light — including doses that never burn — activates",
        "Ultraviolet light (including doses that never burn) activates",
    ),
    (
        "have normal vitamin C — and still lose collagen",
        "have normal vitamin C, and still lose collagen",
    ),
    (
        "experimental settings — not by feeding them collagen",
        "experimental settings, not by feeding them collagen",
    ),
    (
        "assemble fibrils badly — same quantity, poor mechanics",
        "assemble fibrils badly: same quantity, poor mechanics",
    ),
    (
        "is a balance — making, organizing, cross-linking, breaking apart, reassembling — not a level in a tank",
        "is a balance (making, organizing, cross-linking, breaking apart, reassembling), not a level in a tank",
    ),
    (
        "tend to be downstream — assembly, cross-linking quality",
        "tend to be downstream: assembly, cross-linking quality",
    ),
    (
        "the individual edits — and vulnerable in places",
        "the individual edits, and vulnerable in places",
    ),
    (
        "to adapt at all — not whether it had enough raw material",
        "to adapt at all, not whether it had enough raw material",
    ),
    (
        "sensed through osteocytes — tiny cells embedded",
        "sensed through osteocytes, tiny cells embedded",
    ),
    (
        "Halved — within weeks — sometimes before the tendon",
        "Halved, within weeks, sometimes before the tendon",
    ),
    (
        "modulus over months — often more clearly than they increase",
        "modulus over months, often more clearly than they increase",
    ),
    (
        "organization, cross-linking — downstream of whether procollagen",
        "organization, cross-linking, downstream of whether procollagen",
    ),
    (
        "Tendinopathy — tendon disease — is associated",
        "Tendinopathy (tendon disease) is associated",
    ),
    (
        "from the other direction — disorganized matrix, failed healing",
        "from the other direction: disorganized matrix, failed healing",
    ),
    (
        "in different places — and I only saw that when I stopped",
        "in different places, and I only saw that when I stopped",
    ),
    (
        "It is repairing — high turnover, phased, urgent",
        "It is repairing: high turnover, phased, urgent",
    ),
    (
        "high-demand context — not the same as a healthy person",
        "high-demand context, not the same as a healthy person",
    ),
    (
        "Not wounded — being asked to carry more load",
        "Not wounded, being asked to carry more load",
    ),
    (
        "during a training block — remodeling in motion, not a simple build-up",
        "during a training block: remodeling in motion, not a simple build-up",
    ),
    (
        "looked degradation-heavy — the loop I had already met — compounded",
        "looked degradation-heavy, the loop I had already met, compounded",
    ),
    (
        "under ongoing damage — three kinds of invisible work",
        "under ongoing damage: three kinds of invisible work",
    ),
    (
        "a map was useful — not as a protocol, just as a compass",
        "a map was useful, not as a protocol, just as a compass",
    ),
    (
        "**Modifiability varies** — slowing further loss",
        "**Modifiability varies**: slowing further loss",
    ),
    (
        "kept coming anyway — in ads, in studies, in conversations — and I could not resist",
        "kept coming anyway (in ads, in studies, in conversations), and I could not resist",
    ),
    (
        "against real claims — the way you test whether a map helps",
        "against real claims, the way you test whether a map helps",
    ),
    (
        "trying to do? Maintenance — not wound closure",
        "trying to do? Maintenance, not wound closure",
    ),
    (
        "reaching fibroblasts — an early pipeline step",
        "reaching fibroblasts: an early pipeline step",
    ),
    (
        "So I tried a harder one — **collagen plus resistance training",
        "So I tried a harder one: **collagen plus resistance training",
    ),
    (
        "different evidence shape — and yet it sits on the same shelf",
        "different evidence shape, and yet it sits on the same shelf",
    ),
    (
        "watching one hold up — or fail — case by case",
        "watching one hold up or fail, case by case",
    ),
    (
        "mechanisms sharing a word — substrate powders",
        "mechanisms sharing a word: substrate powders",
    ),
    (
        "already inside it — and, I suspect, inside a way",
        "already inside it, and I suspect inside a way",
    ),
    (
        "collagen interventions — largely missing",
        "collagen interventions: largely missing",
    ),
    (
        "structural outcomes** — absence of demonstrated harm",
        "structural outcomes:** absence of demonstrated harm",
    ),
    (
        "a collagen claim — or any structural-health claim — shows up in an ad",
        "a collagen claim, or any structural-health claim, shows up in an ad",
    ),
    (
        "accumulated structural change — or none of the above",
        "accumulated structural change, or none of the above",
    ),
    (
        "endpoint, funding — all fair game",
        "endpoint, funding: all fair game",
    ),
    (
        "that sequence run — on skin powder, on collagen with training, on a joint product that is not really the same thing at all — even if you did not",
        "that sequence run on skin powder, on collagen with training, on a joint product that is not really the same thing at all, even if you did not",
    ),
    (
        "load and insult and repair — and because naming one protein",
        "load and insult and repair, and because naming one protein",
    ),
    (
        "rebuilding is **for** — and what, in your situation",
        "rebuilding is **for**, and what, in your situation",
    ),
]


def apply_replacements(text: str) -> str:
    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new)
    return text


def html_variants(old: str, new: str) -> list[tuple[str, str]]:
    pairs = [(old, new)]
    h_old = (
        old.replace("'", "&rsquo;")
        .replace('"', "&ldquo;", 1)
        if '"' in old
        else old.replace("'", "&rsquo;")
    )
    h_new = new.replace("'", "&rsquo;")
    if "—" in old:
        h_old = h_old.replace("—", "&mdash;")
        h_new = h_new.replace("—", "&mdash;")
    if h_old != old:
        pairs.append((h_old, h_new))
    # quoted phrases in html
    h_old2 = old.replace('"', "&ldquo;", 1).replace('"', "&rdquo;")
    h_new2 = new.replace('"', "&ldquo;", 1).replace('"', "&rdquo;")
    if "—" in h_old2:
        h_old2 = h_old2.replace("—", "&mdash;")
        h_new2 = h_new2.replace("—", "&mdash;")
    if h_old2 not in [p[0] for p in pairs]:
        pairs.append((h_old2, h_new2))
    return pairs


def main():
    if DRAFT.exists():
        draft = DRAFT.read_text(encoding="utf-8")
        before = draft.count("\u2014")
        draft = apply_replacements(draft)
        after = draft.count("\u2014")
        DRAFT.write_text(draft, encoding="utf-8")
        print(f"Draft em dashes: {before} -> {after}")
        if after:
            for i, line in enumerate(draft.splitlines(), 1):
                if "\u2014" in line:
                    print(f"  L{i}: {line[:100]}")

    if HTML.exists():
        html = HTML.read_text(encoding="utf-8")
        hb = html.count("\u2014") + html.count("&mdash;")
        for old, new in REPLACEMENTS:
            html = apply_replacements(html)
            for h_old, h_new in html_variants(old, new):
                html = html.replace(h_old, h_new)
        ha = html.count("\u2014") + html.count("&mdash;")
        HTML.write_text(html, encoding="utf-8")
        print(f"HTML em dashes: {hb} -> {ha}")


if __name__ == "__main__":
    main()

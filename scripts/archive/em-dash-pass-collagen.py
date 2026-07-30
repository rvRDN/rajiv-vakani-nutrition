#!/usr/bin/env python3
"""Apply em dash policy (project-continuity-v7.md §9) to collagen draft."""

from pathlib import Path

DRAFT = Path(__file__).resolve().parents[1] / "docs" / "drafts" / "collagen-article-draft.md"
HTML = Path(__file__).resolve().parents[1] / "drafts" / "collagen.html"

REPLACEMENTS = [
    ("# Collagen — Article Draft", "# Collagen: Article Draft"),
    (
        "helps — her skin, her joints, aging well",
        "helps: her skin, her joints, aging well",
    ),
    (
        "grounded in something real — and whether people",
        "grounded in something real, and whether people",
    ),
    (
        "useful to my friend — or decide whether a tub is worth the money — I had",
        "useful to my friend, or decide whether a tub is worth the money, I had",
    ),
    (
        "into ordinary amino acids — if nothing specific survives digestion — then there probably",
        "into ordinary amino acids (if nothing specific survives digestion), then there probably",
    ),
    (
        "after people take a dose — small linked chains",
        "after people take a dose: small linked chains",
    ),
    (
        "explanation had held — disappears completely, nothing to follow — I would",
        "explanation had held (disappears completely, nothing to follow), I would",
    ),
    (
        "they looked good — and I want to be honest",
        "they looked good, and I want to be honest",
    ),
    (
        "something else entered — not cynicism about collagen, and not disbelief. Context.",
        "something else entered: not cynicism about collagen, and not disbelief. Context.",
    ),
    (
        "also become popular fast — faster than most therapies",
        "also become popular fast, faster than most therapies",
    ),
    (
        "complicated the trials themselves — separate from the adoption question",
        "complicated the trials themselves, separate from the adoption question",
    ),
    (
        "vitamin C and biotin — all of it gets pooled",
        "vitamin C and biotin. All of it gets pooled",
    ),
    (
        "often yes — for some outcomes",
        "often yes, for some outcomes",
    ),
    (
        'collagen "works" — works compared to what?',
        'collagen "works": works compared to what?',
    ),
    (
        "My question — the one that would help my friend, and me, decide whether to buy a tub — was something else:",
        "My question, the one that would help my friend, and me, decide whether to buy a tub, was something else:",
    ),
    (
        "truthful explanation — whatever that turns out to be.",
        "truthful explanation, whatever that turns out to be.",
    ),
    (
        "For skin — the whole reason my friend buys it — I couldn't",
        "For skin, the whole reason my friend buys it, I couldn't",
    ),
    (
        "on body composition — but lost head-to-head",
        "on body composition, but lost head-to-head",
    ),
    (
        "quietly for muscle — maybe the benefit",
        "quietly for muscle, maybe the benefit",
    ),
    (
        "increasing fragility — in skin, in joints, in the things people actually notice and worry about.",
        "increasing fragility: in skin, in joints, in the things people actually notice and worry about.",
    ),
    (
        "What I didn't have — what the broad picture couldn't give me — was enough detail",
        "What I didn't have, what the broad picture couldn't give me, was enough detail",
    ),
    (
        "trials often beat placebo — why do the comparisons",
        "trials often beat placebo, why do the comparisons",
    ),
    (
        "interpret recommendations — the context you need",
        "interpret recommendations: the context you need",
    ),
    (
        "net of those two — plus whether new collagen",
        "net of those two, plus whether new collagen",
    ),
    (
        "drops sharply — and the enzymes that break collagen apart rise",
        "drops sharply, and the enzymes that break collagen apart rise",
    ),
    (
        "managing it — making, breaking, repairing, responding to damage.",
        "managing it: making, breaking, repairing, responding to damage.",
    ),
    (
        "become so complicated — and why *compared to what I would actually do*",
        "become so complicated, and why *compared to what I would actually do*",
    ),
    (
        "are driving loss — not just slow production — then eating",
        "are driving loss (not just slow production), then eating",
    ),
    (
        "as daily prevention — a habit, a proactive thing — not as something",
        "as daily prevention (a habit, a proactive thing), not as something",
    ),
    (
        "fibers fragment — from enzymes, from UV, from time — the cells that make collagen",
        "fibers fragment (from enzymes, from UV, from time), the cells that make collagen",
    ),
    (
        "in the dermis — with filler, not oral collagen — re-stretched those cells",
        "in the dermis (with filler, not oral collagen), re-stretched those cells",
    ),
    (
        "may not do nothing — some imaging studies report less fragmentation in the dermis; wound trials suggest peptide content matters — but for the healthy person",
        "may not do nothing. Some imaging studies report less fragmentation in the dermis; wound trials suggest peptide content matters. But for the healthy person",
    ),
    (
        "supplement actually help — and where probably wouldn't it?",
        "supplement actually help, and where probably wouldn't it?",
    ),
    (
        "It gives patterns — or that's how it looked",
        "It gives patterns, or that's how it looked",
    ),
    (
        "results I found — especially when products differed",
        "results I found, especially when products differed",
    ),
    (
        "prevent skin aging — my friend's situation — had the thinnest",
        "prevent skin aging, my friend's situation, had the thinnest",
    ),
    (
        "already remodeling — healing, adapting under load, managing symptoms.",
        "already remodeling: healing, adapting under load, managing symptoms.",
    ),
    (
        "buying collagen — me included, if I were buying it — aren't in ulcer",
        "buying collagen (me included, if I were buying it) aren't in ulcer",
    ),
    (
        "high turnover — the body already rebuilding, extra input meeting real demand.",
        "high turnover: the body already rebuilding, extra input meeting real demand.",
    ),
    (
        "for someone like me — or my friend — doing what we're actually trying to do?",
        "for someone like me, or my friend, doing what we're actually trying to do?",
    ),
    (
        "trying to prevent decline — is the tub worth the money?",
        "trying to prevent decline, is the tub worth the money?",
    ),
    (
        "against placebo — rarely against food — gets harder to justify.",
        "against placebo, rarely against food, gets harder to justify.",
    ),
    (
        "amino acids don't — nudging cell behavior",
        "amino acids don't: nudging cell behavior",
    ),
    (
        "measure hydration — which could mean better water content",
        "measure hydration, which could mean better water content",
    ),
    (
        "I'd actually want — high-peptide collagen versus matched amino acids",
        "I'd actually want: high-peptide collagen versus matched amino acids",
    ),
    (
        "evidence backs that — or if her mostly vegetarian diet",
        "evidence backs that, or if her mostly vegetarian diet",
    ),
    (
        "amino acids in many foods — lentils, beans, dairy, eggs if you eat them, tofu, normal varied eating.",
        "amino acids in many foods: lentils, beans, dairy, eggs if you eat them, tofu, normal varied eating.",
    ),
    (
        "from amino acids alone — no collagen.",
        "from amino acids alone, no collagen.",
    ),
    (
        "won't make her compromise — I didn't find evidence",
        "won't make her compromise, I didn't find evidence",
    ),
    (
        "not what this earned — and it's not what I'd want",
        "not what this earned, and it's not what I'd want",
    ),
    (
        "with fundamentals — the boring layer most tubs hope you'll skip past.",
        "with fundamentals: the boring layer most tubs hope you'll skip past.",
    ),
    (
        "situation from repair — a wound, a loaded tendon, symptomatic joints.",
        "situation from repair: a wound, a loaded tendon, symptomatic joints.",
    ),
    (
        "whether collagen — or any specific product — offers something",
        "whether collagen, or any specific product, offers something",
    ),
    (
        "**If you're actively healing or adapting** — a wound, an ulcer, symptomatic joints, heavy training with tendon goals — collagen may",
        "**If you're actively healing or adapting:** a wound, an ulcer, symptomatic joints, heavy training with tendon goals. Collagen may",
    ),
    (
        "**If you're healthy and buying for prevention** — daily powder for skin, joints before they're a problem — the evidence looks",
        "**If you're healthy and buying for prevention:** daily powder for skin, joints before they're a problem. The evidence looks",
    ),
    (
        "**If you're vegetarian or vegan** — I didn't find strong evidence",
        "**If you're vegetarian or vegan:** I didn't find strong evidence",
    ),
    (
        "training, sun protection — that's where I'd put attention first.",
        "training, sun protection. That's where I'd put attention first.",
    ),
    (
        "**When the next collagen claim shows up** — I'd ask two things: compared to what? And for which situation — prevention in a mostly intact body, or repair where turnover is already high?",
        "**When the next collagen claim shows up:** I'd ask two things: compared to what? And for which situation: prevention in a mostly intact body, or repair where turnover is already high?",
    ),
    (
        "for daily prevention — the case most buyers are actually making — is as strong",
        "for daily prevention, the case most buyers are actually making, is as strong",
    ),
    (
        "gap in the evidence — and a path through ordinary nutrition",
        "gap in the evidence, and a path through ordinary nutrition",
    ),
    (
        "bovine collagen? No — not from where I landed.",
        "bovine collagen? No, not from where I landed.",
    ),
    (
        "Some people — my friend included — may reasonably decide",
        "Some people, my friend included, may reasonably decide",
    ),
    (
        "question that stuck — the one I suspect I'll still be turning over — isn't",
        "question that stuck, the one I suspect I'll still be turning over, isn't",
    ),
    (
        "for someone like me — or is it built for a biological situation I'm not actually in?",
        "for someone like me, or is it built for a biological situation I'm not actually in?",
    ),
    (
        "understanding your options — not inheriting mine.",
        "understanding your options, not inheriting mine.",
    ),
]


def apply_replacements(text: str) -> str:
    for old, new in REPLACEMENTS:
        if old not in text:
            continue
        text = text.replace(old, new)
    return text


def main():
    draft = DRAFT.read_text(encoding="utf-8")
    before = draft.count("\u2014")
    draft = apply_replacements(draft)
    after = draft.count("\u2014")
    DRAFT.write_text(draft, encoding="utf-8")
    print(f"Draft em dashes: {before} -> {after}")
    if after:
        for i, line in enumerate(draft.splitlines(), 1):
            if "\u2014" in line:
                print(f"  L{i}: {line[:120]}")

    if HTML.exists():
        html = HTML.read_text(encoding="utf-8")
        hb = html.count("\u2014")
        html = apply_replacements(html)
        # HTML entity forms that may differ from markdown
        html_replacements = [
            (old.replace("'", "&rsquo;"), new.replace("'", "&rsquo;"))
            for old, new in REPLACEMENTS
        ]
        for old, new in html_replacements:
            if old in html:
                html = html.replace(old, new)
        ha = html.count("\u2014")
        HTML.write_text(html, encoding="utf-8")
        print(f"HTML em dashes: {hb} -> {ha}")


if __name__ == "__main__":
    main()

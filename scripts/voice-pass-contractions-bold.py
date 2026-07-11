"""One-shot voice pass: contractions + strip prose bold in SFD chapter drafts."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "drafts/starting-state-chapter-v0.2.md",
    ROOT / "drafts/flavor-chapter-v0.2.md",
    ROOT / "drafts/knife-cuts-chapter-v0.1.md",
    ROOT / "drafts/heat-chapter-v0.1.md",
    ROOT / "drafts/steering-chapter-v0.2.md",
]

CONTRACTIONS = [
    (r"\bwill not\b", "won't"),
    (r"\bWill not\b", "Won't"),
    (r"\bwould not\b", "wouldn't"),
    (r"\bWould not\b", "Wouldn't"),
    (r"\bcannot\b", "can't"),
    (r"\bCannot\b", "Can't"),
    (r"\bdo not\b", "don't"),
    (r"\bDo not\b", "Don't"),
    (r"\bdoes not\b", "doesn't"),
    (r"\bDoes not\b", "Doesn't"),
    (r"\bdid not\b", "didn't"),
    (r"\bDid not\b", "Didn't"),
    (r"\bhave not\b", "haven't"),
    (r"\bHave not\b", "Haven't"),
    (r"\bhas not\b", "hasn't"),
    (r"\bHas not\b", "Hasn't"),
    (r"\bhad not\b", "hadn't"),
    (r"\bHad not\b", "Hadn't"),
    (r"\bare not\b", "aren't"),
    (r"\bAre not\b", "Aren't"),
    (r"\bwas not\b", "wasn't"),
    (r"\bWas not\b", "Wasn't"),
    (r"\bwere not\b", "weren't"),
    (r"\bWere not\b", "Weren't"),
    (r"\bis not\b", "isn't"),
    (r"\bIs not\b", "Isn't"),
    (r"\byou are\b", "you're"),
    (r"\bYou are\b", "You're"),
    (r"\bwe are\b", "we're"),
    (r"\bWe are\b", "We're"),
    (r"\bthey are\b", "they're"),
    (r"\bThey are\b", "They're"),
    (r"\bit is\b", "it's"),
    (r"\bIt is\b", "It's"),
    (r"\bthat is\b", "that's"),
    (r"\bThat is\b", "That's"),
    (r"\bwhat is\b", "what's"),
    (r"\bWhat is\b", "What's"),
    (r"\bhere is\b", "here's"),
    (r"\bHere is\b", "Here's"),
    (r"\bthere is\b", "there's"),
    (r"\bThere is\b", "There's"),
    (r"\bI am\b", "I'm"),
    (r"\blet us\b", "let's"),
    (r"\bLet us\b", "Let's"),
]

KEEP_FORMAL = [
    "## Do not judge an ingredient in isolation",
    "Unripe is not failed ripe. Jar is not dish. Easy to peel is not the only useful form.",
    "Fresh is not always best. Frozen is not always worse.",
]


def protect(text: str):
    holders = {}
    for i, phrase in enumerate(KEEP_FORMAL):
        key = f"___KEEP{i}___"
        if phrase in text:
            text = text.replace(phrase, key)
            holders[key] = phrase
    return text, holders


def unprotect(text: str, holders: dict):
    for k, v in holders.items():
        text = text.replace(k, v)
    return text


def strip_bold(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"\1", text)


def apply_contractions(text: str) -> str:
    for pat, repl in CONTRACTIONS:
        text = re.sub(pat, repl, text)
    return text


def process_body(body: str) -> str:
    body, holders = protect(body)
    body = strip_bold(body)
    body = apply_contractions(body)
    body = unprotect(body, holders)

    # Restore emphasis heading if eaten
    body = body.replace(
        "## Don't judge an ingredient in isolation",
        "## Do not judge an ingredient in isolation",
    )
    body = body.replace(
        "Unripe isn't failed ripe. Jar isn't dish. Easy to peel isn't the only useful form.",
        "Unripe is not failed ripe. Jar is not dish. Easy to peel is not the only useful form.",
    )
    body = body.replace(
        "Fresh isn't always best. Frozen isn't always worse.",
        "Fresh is not always best. Frozen is not always worse.",
    )

    # Quiet questions: italics (were bold)
    for q in (
        "What am I actually working with?",
        "What outcome am I trying to create?",
        "What should this ingredient become?",
        "What does this dish need now?",
    ):
        body = re.sub(rf"^{re.escape(q)}$", f"*{q}*", body, flags=re.M)

    # Keep formal "It is" before the carried quiet question (emphasis beat)
    body = re.sub(
        r"(The question worth carrying is not \*[^*]+\*\. )It's (\*[^*]+\*)",
        r"\1It is \2",
        body,
    )
    body = re.sub(
        r"(The question worth carrying is not \*[^*]+\*\? )It's (\*[^*]+\*)",
        r"\1It is \2",
        body,
    )

    # Opening Starting State quiet question may sit after "first:"
    body = body.replace(
        "We rarely ask a quieter question first:\n\nWhat am I actually working with?",
        "We rarely ask a quieter question first:\n\n*What am I actually working with?*",
    )

    # Closing echo of quiet question
    body = re.sub(
        r"^(What am I actually working with\?)( Ask it)",
        r"*\1*\2",
        body,
        flags=re.M,
    )

    # Heat one-sentence thesis: was bold whole sentence; leave plain (already stripped)
    # Restore a couple of lesson lines that read better slightly formal
    body = body.replace(
        "That's the first steering lesson: cooked isn't finished.",
        "That's the first steering lesson: cooked is not finished.",
    )
    body = body.replace(
        "Understanding what they *do* isn't.",
        "Understanding what they *do* is not.",
    )

    return body


def main():
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        m = re.search(
            r"\n(# (?:Starting State|Flavor|Knife Cuts|Heat|Steering)\n)",
            text,
        )
        if not m:
            print("NO START", path.name)
            continue
        start = m.start(1)
        end_m = re.search(r"\n---\n\n## Pressure-test checklist", text[start:])
        if not end_m:
            end_m = re.search(r"\n---\n\n\*\*Cycle 2 verdict", text[start:])
        if not end_m:
            print("NO END", path.name)
            continue
        end = start + end_m.start()
        head, body, tail = text[:start], text[start:end], text[end:]
        new_body = process_body(body)
        path.write_text(head + new_body + tail, encoding="utf-8")
        print(
            "OK",
            path.name,
            "prose ** left:",
            len(re.findall(r"\*\*[^*]+\*\*", new_body)),
        )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path
import re

IM = Path(__file__).resolve().parents[1] / "intervention-maps"

FIXES = {
    "adhd.html": (
        "Maps lifestyle and nutrition evidence for ADHD: skills training, "
        "sleep, exercise, diet, and supplements. Not a medication guide."
    ),
    "anxiety.html": (
        "Maps non-drug and adjunctive evidence for anxiety: psychotherapy, "
        "digital CBT, mindfulness, exercise, and herbals. Medication is backdrop, not the subject."
    ),
    "depression.html": (
        "Maps non-drug and adjunctive evidence for depression: psychotherapy, "
        "exercise, sleep, diet, light, and nutraceuticals. Medication remains an important first-line option."
    ),
}


def replace_attr_content(text: str, attr_prefix: str, new_value: str) -> str:
    pattern = re.compile(re.escape(attr_prefix) + r'[^"]*"')
    text2, n = pattern.subn(attr_prefix + new_value + '"', text, count=1)
    if n != 1:
        raise SystemExit(f"missed prefix: {attr_prefix}")
    return text2


def tidy_head(text: str) -> str:
    text = text.replace("\n<link rel=\"preconnect\"", "\n  <link rel=\"preconnect\"")
    text = re.sub(
        r"</title>\n\n  <meta name=\"description\"",
        "</title>\n  <meta name=\"description\"",
        text,
    )
    return text


def main() -> None:
    for name, desc in FIXES.items():
        path = IM / name
        text = path.read_text(encoding="utf-8")
        text = replace_attr_content(text, 'name="description" content="', desc)
        text = replace_attr_content(text, 'property="og:description" content="', desc)
        text = replace_attr_content(
            text, 'property="twitter:description" content="', desc
        )
        text = tidy_head(text)
        path.write_text(text, encoding="utf-8", newline="\n")
        print("hub", name)

    for path in IM.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        text2 = tidy_head(text)
        if text2 != text:
            path.write_text(text2, encoding="utf-8", newline="\n")
            print("tidy", path.name)


if __name__ == "__main__":
    main()

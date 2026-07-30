#!/usr/bin/env python3
"""Add intentional mobile line break to library-family colophons."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATTERNS = [
    (
        re.compile(
            r'(<a href="about\.html">Rajiv Vakani</a>\. Writing on nutrition from)\s+'
            r'New York\. (Since 2023\. <a href="contact\.html">Email</a>\.)'
        ),
        r'\1 New York.<br class="colophon-break" aria-hidden="true">\n          \2',
    ),
    (
        re.compile(
            r'(<a href="\.\./about\.html">Rajiv Vakani</a>\. Writing on nutrition from)\s+'
            r'New York\. (Since 2023\. <a href="\.\./contact\.html">Email</a>\.)'
        ),
        r'\1 New York.<br class="colophon-break" aria-hidden="true">\n          \2',
    ),
    (
        re.compile(
            r'(<a href="\.\./\.\./about\.html">Rajiv Vakani</a>\. Writing on nutrition from)\s+'
            r'New York\. (Since 2023\. <a href="\.\./\.\./contact\.html">Email</a>\.)'
        ),
        r'\1 New York.<br class="colophon-break" aria-hidden="true">\n          \2',
    ),
]

SKIP = {"index.html"}


def main() -> None:
    targets = [
        ROOT / "insights.html",
        ROOT / "library.html",
        *sorted((ROOT / "insights").glob("*.html")),
        *sorted((ROOT / "insights" / "topics").glob("*.html")),
    ]
    updated = []
    for path in targets:
        if path.name in SKIP or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "Writing on nutrition from" not in text or "colophon-break" in text:
            continue
        new = text
        for pattern, repl in PATTERNS:
            new = pattern.sub(repl, new)
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            updated.append(str(path.relative_to(ROOT)))

    print(f"Updated {len(updated)} files:")
    for name in updated:
        print(f"  {name}")


if __name__ == "__main__":
    main()

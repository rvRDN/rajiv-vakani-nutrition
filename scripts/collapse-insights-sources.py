#!/usr/bin/env python3
"""Collapse every Insights article bibliography behind one disclosure."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSIGHTS = ROOT / "insights"
VERSION = "20260719173000"

SECTION_RE = re.compile(
    r'(?P<open><section class="post-sources"(?P<attrs>[^>]*)>\s*'
    r'<div class="post-wrap">)'
    r'(?P<inner>.*?)'
    r'(?P<close>\s*</div>\s*</section>)',
    re.DOTALL,
)

DISCLOSURE_RE = re.compile(
    r'<details class="post-sources__disclosure">\s*'
    r'<summary>.*?</summary>\s*'
    r'<div class="post-sources__disclosure-body">\s*'
    r'(?P<body>.*?)'
    r'\s*</div>\s*</details>',
    re.DOTALL,
)

PLAIN_SOURCES_LABEL_RE = re.compile(
    r'\s*<p class="post-sources__label">Sources</p>\s*',
    re.IGNORECASE,
)


def normalize_inner(inner: str) -> str:
    """Remove any prior disclosure wrapper before rebuilding one."""

    def unwrap(match: re.Match[str]) -> str:
        return match.group("body")

    inner = DISCLOSURE_RE.sub(unwrap, inner)
    inner = PLAIN_SOURCES_LABEL_RE.sub("\n", inner)
    return textwrap.dedent(inner).strip()


def collapse_section(match: re.Match[str]) -> str:
    if '<details class="post-sources__disclosure">' in match.group("inner"):
        return match.group(0)

    attrs = match.group("attrs")
    aria_match = re.search(r'aria-label="([^"]+)"', attrs)
    label = aria_match.group(1) if aria_match else "Sources"
    if label.lower() == "sources":
        label = "Sources"

    inner = normalize_inner(match.group("inner"))
    indented = "\n".join(
        ("          " + line if line else "") for line in inner.splitlines()
    )

    return (
        f'{match.group("open")}\n'
        '        <details class="post-sources__disclosure">\n'
        f'          <summary>{label} '
        '<span class="post-sources__cue" aria-hidden="true">Open sources</span>'
        "</summary>\n"
        '          <div class="post-sources__disclosure-body">\n'
        f"{indented}\n"
        "          </div>\n"
        "        </details>"
        f"{match.group('close')}"
    )


def update_asset_versions(text: str) -> str:
    text = re.sub(
        r'library(?:\.min)?\.css\?v=[0-9]+',
        f"library.min.css?v={VERSION}",
        text,
    )
    text = re.sub(
        r'library\.js\?v=[0-9]+',
        f"library.js?v={VERSION}",
        text,
    )
    return text


def validate_pages() -> None:
    errors: list[str] = []

    for path in sorted(INSIGHTS.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        section_count = text.count('<section class="post-sources"')
        disclosure_count = text.count('<details class="post-sources__disclosure">')
        if section_count != disclosure_count:
            errors.append(
                f"{path.name}: {section_count} source sections but "
                f"{disclosure_count} disclosures"
            )

        refs = set(re.findall(r'href="#(src-[0-9]+)"', text))
        ids = set(re.findall(r'id="(src-[0-9]+)"', text))
        missing = sorted(refs - ids)
        if missing:
            errors.append(f"{path.name}: missing targets for {', '.join(missing)}")

        if '<details class="post-sources__disclosure" open' in text:
            errors.append(f"{path.name}: sources disclosure is open by default")

    if errors:
        raise SystemExit("\n".join(errors))


def main() -> None:
    changed = 0
    converted = 0

    for path in sorted(INSIGHTS.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        updated, count = SECTION_RE.subn(collapse_section, text)
        updated = update_asset_versions(updated)

        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
        converted += count

    validate_pages()
    print(f"Found {converted} source sections; updated {changed} Insights files.")
    print("Validated source disclosures and inline citation targets.")


if __name__ == "__main__":
    main()

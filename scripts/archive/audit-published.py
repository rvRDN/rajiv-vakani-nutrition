"""Audit all published articles + key library pages for publish readiness."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = "http://127.0.0.1:8765"
VIEWPORT = {"width": 390, "height": 844}

PUBLISHED = [
    "insights/how-i-evaluate-nutrition-claims.html",
    "insights/why-i-stopped-trusting-simple-answers.html",
    "insights/what-dr-gundry-taught-me.html",
    "insights/should-you-buy-lentil-pasta.html",
    "insights/where-the-egg-alzheimers-story-drifted.html",
    "insights/when-nutrition-advice-looks-like-precision-medicine.html",
]

LIBRARY_PAGES = [
    "insights.html",
    "library.html",
    "insights/topics/reading-the-evidence.html",
    "insights/topics/practical-nutrition.html",
]


def audit_page(page, path):
    url = f"{BASE}/{path}"
    issues = []
    page.goto(url, wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(1500)

    html = page.content().lower()
    if "noindex" in html:
        issues.append("has noindex")
    if ">draft<" in html or "draft</span>" in html.replace(" ", ""):
        # check visible draft markers in post-meta / library lists
        draft_visible = page.locator(".post-meta span:has-text('Draft'), .library-archive__draft, .start__draft").count()
        if draft_visible:
            issues.append(f"visible Draft marker ({draft_visible})")

    overflow = page.evaluate(
        """() => ({
          docScrollWidth: document.documentElement.scrollWidth,
          viewportWidth: window.innerWidth,
          hasHorizontalOverflow: document.documentElement.scrollWidth > window.innerWidth + 1
        })"""
    )
    if overflow["hasHorizontalOverflow"]:
        issues.append(f"horizontal overflow ({overflow['docScrollWidth']}px > {overflow['viewportWidth']}px)")

    canonical = page.locator('link[rel="canonical"]').get_attribute("href")
    if not canonical:
        issues.append("missing canonical")

    title = page.title()
    if not title or title.strip() == "":
        issues.append("empty title")

    h1 = page.locator("h1").first.text_content() if page.locator("h1").count() else None
    if not h1:
        issues.append("missing h1")

    # Library pages: egg article should appear without Draft tag
    if "reading-the-evidence" in path or path == "library.html":
        egg_link = page.locator('a[href*="where-the-egg-alzheimers-story-drifted"]')
        if egg_link.count() == 0:
            issues.append("egg article not listed")
        elif page.locator('a[href*="where-the-egg-alzheimers-story-drifted"] >> xpath=ancestor::*[contains(@class,"library-archive__item") or contains(@class,"topic-cluster")]//span[contains(text(),"Draft")]').count():
            issues.append("egg article shows Draft in listing")

    embed = page.locator(".post-claim-card__embed")
    if embed.count():
        box = embed.bounding_box()
        if box and box["width"] > overflow["viewportWidth"]:
            issues.append("claim embed wider than viewport")

    return {
        "path": path,
        "title": title,
        "canonical": canonical,
        "issues": issues,
        "overflow": overflow,
    }


def main():
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        for path in PUBLISHED + LIBRARY_PAGES:
            try:
                results.append(audit_page(page, path))
            except Exception as e:
                results.append({"path": path, "issues": [f"ERROR: {e}"], "title": None, "canonical": None})
        browser.close()

    print("=== PUBLISHED ARTICLE AUDIT (390x844) ===\n")
    for r in results:
        status = "OK" if not r["issues"] else "ISSUES"
        print(f"[{status}] {r['path']}")
        if r.get("title"):
            print(f"  title: {r['title'][:70]}")
        if r.get("canonical"):
            print(f"  canonical: yes")
        for issue in r.get("issues", []):
            print(f"  ! {issue}")
        print()

    ok = sum(1 for r in results if not r["issues"])
    print(f"Summary: {ok}/{len(results)} pages clean")


if __name__ == "__main__":
    main()

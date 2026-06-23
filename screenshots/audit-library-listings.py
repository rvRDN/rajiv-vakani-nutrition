from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8765"

PUBLISHED_SLUGS = [
    "how-i-evaluate-nutrition-claims",
    "why-i-stopped-trusting-simple-answers",
    "what-dr-gundry-taught-me",
    "should-you-buy-lentil-pasta",
    "where-the-egg-alzheimers-story-drifted",
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 390, "height": 844})
    page.goto(f"{BASE}/library.html", wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(2000)

    print("=== LIBRARY LISTING CHECK ===")
    for slug in PUBLISHED_SLUGS:
        link = page.locator(f'a[href*="{slug}"]')
        count = link.count()
        item = page.locator(f'.library-archive__item:has(a[href*="{slug}"])')
        draft_in_item = item.locator(".library-archive__draft").count() if item.count() else 0
        title = link.first.text_content().strip() if count else "(missing)"
        print(f"{slug}: listed={count > 0}, draft_tag={draft_in_item > 0}, title={title[:60]}")

    print("\n=== READING THE EVIDENCE TOPIC ===")
    page.goto(f"{BASE}/insights/topics/reading-the-evidence.html", wait_until="networkidle")
    page.wait_for_timeout(2000)
    for slug in ["how-i-evaluate-nutrition-claims", "why-i-stopped-trusting-simple-answers", "what-dr-gundry-taught-me", "where-the-egg-alzheimers-story-drifted"]:
        link = page.locator(f'a[href*="{slug}"]')
        print(f"{slug}: {link.count() > 0}")

    browser.close()

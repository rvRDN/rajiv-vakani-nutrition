from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
URL = "http://127.0.0.1:8765/insights/when-nutrition-advice-looks-like-precision-medicine.html"
VIEWPORTS = [
    ("390x844", 390, 844),
    ("430x932", 430, 932),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, width, height in VIEWPORTS:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(2000)
        embed = page.locator(".post-claim-card__embed")
        embed.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path=str(OUT / f"precision-medicine-mobile-{name}-claim-card.png"), full_page=False)
        page.screenshot(path=str(OUT / f"precision-medicine-mobile-{name}-top.png"), full_page=True)
        overflow = page.evaluate(
            """() => {
              const img = document.querySelector('.post-claim-card__embed img');
              return {
                docScrollWidth: document.documentElement.scrollWidth,
                viewportWidth: window.innerWidth,
                hasHorizontalOverflow: document.documentElement.scrollWidth > window.innerWidth + 1,
                imgWidth: img ? img.getBoundingClientRect().width : null,
                embedClientWidth: document.querySelector('.post-claim-card__embed')?.clientWidth ?? null
              };
            }"""
        )
        print(f"{name}: {overflow}")
        page.close()
    browser.close()

print("Screenshots written to", OUT)

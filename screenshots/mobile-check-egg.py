from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
URL = "http://127.0.0.1:8765/insights/where-the-egg-alzheimers-story-drifted.html"
VIEWPORTS = [
    ("390x844", 390, 844),
    ("430x932", 430, 932),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, width, height in VIEWPORTS:
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(3000)
        embed = page.locator(".post-claim-card__embed")
        embed.scroll_into_view_if_needed()
        page.wait_for_timeout(1500)
        page.screenshot(path=str(OUT / f"egg-mobile-{name}-claim-card.png"), full_page=False)
        page.screenshot(path=str(OUT / f"egg-mobile-{name}-top.png"), full_page=True)
        box = embed.bounding_box()
        print(f"{name}: embed box={box}")
        intro = page.locator(".post-claim-card__intro").bounding_box()
        meta = page.locator(".post-claim-card__meta").bounding_box()
        print(f"{name}: intro bottom={intro['y'] + intro['height'] if intro else None}, meta top={meta['y'] if meta else None}")
        overflow = page.evaluate(
            """() => {
              const el = document.querySelector('.post-claim-card__embed');
              if (!el) return null;
              const iframe = el.querySelector('iframe');
              return {
                embedClientWidth: el.clientWidth,
                embedScrollWidth: el.scrollWidth,
                iframeHeight: iframe ? iframe.offsetHeight : null,
                viewportWidth: window.innerWidth
              };
            }"""
        )
        print(f"{name}: layout={overflow}")
        page.close()
    browser.close()

print("Screenshots written to", OUT)

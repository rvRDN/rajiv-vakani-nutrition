#!/usr/bin/env python3
"""Assemble published insights/invisible-maintenance.html from draft body."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
body = Path(ROOT / "_tmp_im_body.html").read_text(encoding="utf-8")
CACHE = "20260628100000"

html = f"""<!DOCTYPE html>
<html lang="en" class="post-page">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>Invisible Maintenance | Rajiv Vakani</title>
  <meta name="description" content="Most of what holds you together runs invisibly. Collagen was the entry point; this investigation asks what the body is sustaining, and what has to go wrong for structure to fail.">

  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://rajivvakani.com/insights/invisible-maintenance.html" />
  <meta property="og:title" content="Invisible Maintenance | Rajiv Vakani" />
  <meta property="og:description" content="Most of what holds you together runs invisibly. Collagen was the entry point; this investigation asks what the body is sustaining, and what has to go wrong for structure to fail." />
  <meta property="og:image" content="https://rajivvakani.com/headshot_36.jpg" />
  <meta property="og:site_name" content="Rajiv Vakani" />

  <link rel="canonical" href="https://rajivvakani.com/insights/invisible-maintenance.html" />

  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="https://rajivvakani.com/insights/invisible-maintenance.html" />
  <meta property="twitter:title" content="Invisible Maintenance | Rajiv Vakani" />
  <meta property="twitter:description" content="Most of what holds you together runs invisibly. Collagen was the entry point; this investigation asks what the body is sustaining, and what has to go wrong for structure to fail." />
  <meta property="twitter:image" content="https://rajivvakani.com/headshot_36.jpg" />

  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="../rajiv-styles.css?v=20260620130000">
  <link rel="stylesheet" href="library.css?v={CACHE}">
  <link rel="icon" type="image/png" href="../favicon.png" />

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0L41N5K2WV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0L41N5K2WV');
  </script>

  <script defer src="data.js?v={CACHE}"></script>
  <script defer src="library.js?v=2026060902"></script>
</head>
<body class="post-page post-layout--inquiry" data-article-slug="invisible-maintenance" data-topic-id="reading-the-evidence">

  <nav class="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="site-logo">Rajiv Vakani</a>
      <ul class="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../about.html">About</a></li>
        <li><a href="../journey.html">Journey</a></li>
        <li><a href="../insights.html" class="active">Insights</a></li>
        <li><a href="../library.html">Library</a></li>
        <li><a href="../contact.html">Contact</a></li>
      </ul>
      <div class="social-icons" aria-label="Social links">
        <a href="https://instagram.com/rajivvakani" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a>
        <a href="https://facebook.com/rajivvakani" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook" aria-hidden="true"></i></a>
      </div>
      <button class="menu-toggle" aria-label="Toggle navigation">
        <span class="hamburger"></span><span class="hamburger"></span><span class="hamburger"></span>
      </button>
    </div>
  </nav>

  <div class="mobile-menu-overlay"></div>

  <main>

    <header class="post-header">
      <div class="post-wrap">
        <p class="post-anchor">
          in <a href="topics/reading-the-evidence.html">Reading the evidence</a>
        </p>
        <h1 class="post-title">Invisible Maintenance</h1>
        <p class="post-dek">Collagen was only the beginning.</p>
        <p class="post-meta">
          <span>Essay</span>
          <span>June 28, 2026</span>
        </p>
      </div>
    </header>

    <section class="post-glance" aria-label="At a glance">
      <div class="post-wrap">
        <p class="post-glance__label">At a glance</p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">What started this</span>
          Most of what holds you together, you never notice. Collagen is everywhere in conversations about aging, skin, and joints, but naming it is not the same as understanding how structure is maintained over a lifetime.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">What caught my attention</span>
          Maintenance, repair, and adaptation are not the same biological job. The tank-is-emptying picture breaks in sun-exposed skin even when nutrition is adequate. Often the limit is downstream of input: architecture, signal, ongoing damage.
        </p>

        <p class="post-glance__beat">
          <span class="post-glance__beat-label">Why it matters</span>
          This is not a shopping list. It is a way to ask what your body is trying to do in a given situation, and what process might actually be limiting it, before any product claim earns your attention.
        </p>

        <p class="post-glance__continue">
          <a href="#journey">Continue below</a> for the full investigation.
        </p>
      </div>
    </section>

    <article class="post-body" id="journey">
      <div class="post-wrap">

{body}

      </div>
    </article>

    <section class="post-next" aria-label="Next">
      <div class="post-wrap" data-post-next></div>
    </section>

    <section class="post-colophon" aria-label="Signature">
      <div class="post-wrap">
        <p>
          <a href="../about.html">Rajiv Vakani</a>. Writing on nutrition from
          New York. Since 2023. <a href="../contact.html">Email</a>.
        </p>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2025&ndash;2026 Rajiv Vakani</p>
      <div class="footer-social" aria-label="Social links">
        <a href="https://instagram.com/rajivvakani" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a>
        <a href="https://facebook.com/rajivvakani" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook" aria-hidden="true"></i></a>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      var menuToggle = document.querySelector('.menu-toggle');
      var navLinks = document.querySelector('.nav-links');
      var overlay = document.querySelector('.mobile-menu-overlay');
      if (menuToggle && navLinks) {{
        menuToggle.addEventListener('click', function () {{
          navLinks.classList.toggle('active');
          menuToggle.classList.toggle('active');
          if (overlay) overlay.classList.toggle('active');
          document.body.classList.toggle('menu-open');
        }});
      }}
      if (overlay) {{
        overlay.addEventListener('click', function () {{
          navLinks.classList.remove('active');
          menuToggle.classList.remove('active');
          overlay.classList.remove('active');
          document.body.classList.remove('menu-open');
        }});
      }}
    }});
  </script>
</body>
</html>
"""

out = ROOT / "insights" / "invisible-maintenance.html"
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({len(html)} bytes)")

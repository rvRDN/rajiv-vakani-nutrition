/**
 * Home hero entrance — Certainty weather
 *
 * Additive only. Welcome + constellation stay intact underneath.
 * Claims: slow open → gradual build → late rush.
 * Thesis: arrives right → left into the real lede seat.
 * Plays once per tab session; hard refresh still replays.
 */
(function () {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const CLAIMS = [
    { text: 'Cut carbs. Forever.', sx: -0.08, sy: 0.22, ex: 0.38, ey: 0.36, ox: 1.12, oy: 0.18, rot: -6, hot: true },
    { text: 'Seed oils are poison.', sx: 1.1, sy: 0.18, ex: 0.62, ey: 0.28, ox: -0.12, oy: 0.08, rot: 4 },
    { text: 'Just eat clean.', sx: 0.5, sy: -0.1, ex: 0.48, ey: 0.42, ox: 0.55, oy: 1.15, rot: -2, hot: true },
    { text: 'Protein fixes everything.', sx: -0.12, sy: 0.62, ex: 0.34, ey: 0.52, ox: 1.15, oy: 0.7, rot: 5 },
    { text: 'Detox starts Monday.', sx: 1.12, sy: 0.55, ex: 0.68, ey: 0.48, ox: -0.15, oy: 0.9, rot: -4, hot: true },
    /* Build: still readable, pace picking up. */
    { text: 'Breakfast is mandatory.', sx: 0.15, sy: 1.12, ex: 0.42, ey: 0.58, ox: 0.1, oy: -0.12, rot: 3 },
    { text: "Calories. That's it.", sx: 0.88, sy: 1.1, ex: 0.58, ey: 0.56, ox: 0.95, oy: -0.1, rot: -5, hot: true },
    { text: 'One study settled it.', sx: -0.1, sy: 0.4, ex: 0.3, ey: 0.4, ox: 1.18, oy: 0.45, rot: 7 },
    { text: 'Natural means safe.', sx: 1.08, sy: 0.35, ex: 0.7, ey: 0.38, ox: -0.18, oy: 0.3, rot: -3, hot: true },
    { text: 'Supplements close the gap.', sx: 0.72, sy: -0.08, ex: 0.55, ey: 0.32, ox: 0.2, oy: 1.12, rot: 2 },
    { text: 'Inflammation is everything.', sx: -0.05, sy: 0.78, ex: 0.36, ey: 0.62, ox: 1.1, oy: 0.95, rot: -7 },
    { text: 'Fasting is the answer.', sx: 1.05, sy: 0.72, ex: 0.64, ey: 0.6, ox: -0.1, oy: 0.55, rot: 4, hot: true },
    { text: 'Sugar is the villain.', sx: 0.28, sy: -0.06, ex: 0.44, ey: 0.3, ox: 0.8, oy: 1.14, rot: -2 },
    { text: 'Trust the protocol.', sx: 0.6, sy: 1.08, ex: 0.52, ey: 0.66, ox: 0.05, oy: -0.14, rot: 6, hot: true },
    { text: 'Meat heals. Plants fail.', sx: -0.12, sy: 0.3, ex: 0.26, ey: 0.34, ox: 1.15, oy: 0.75, rot: 4 },
    { text: 'Cholesterol is solved.', sx: 1.1, sy: 0.62, ex: 0.72, ey: 0.54, ox: -0.14, oy: 0.18, rot: -5, hot: true },
    { text: 'Your gut runs everything.', sx: 0.2, sy: -0.08, ex: 0.46, ey: 0.26, ox: 0.9, oy: 1.12, rot: 2 },
    { text: 'Hormones first. Always.', sx: 0.85, sy: 1.08, ex: 0.6, ey: 0.7, ox: 0.08, oy: -0.12, rot: -3, hot: true },
    /* Late rush. */
    { text: 'Gluten is the problem.', sx: -0.14, sy: 0.48, ex: 0.28, ey: 0.44, ox: 1.14, oy: 0.22, rot: 5, hot: true },
    { text: 'Eat like your ancestors.', sx: 1.14, sy: 0.48, ex: 0.74, ey: 0.44, ox: -0.16, oy: 0.62, rot: -4 },
    { text: 'The food pyramid lied.', sx: 0.08, sy: -0.12, ex: 0.4, ey: 0.24, ox: 0.88, oy: 1.16, rot: 3, hot: true },
    { text: 'Biohacking beats medicine.', sx: 0.94, sy: -0.1, ex: 0.66, ey: 0.26, ox: 0.12, oy: 1.14, rot: -6 },
    { text: 'Willpower is all you need.', sx: -0.1, sy: 0.88, ex: 0.32, ey: 0.7, ox: 1.16, oy: 0.4, rot: 4, hot: true },
    { text: 'Superfoods will save you.', sx: 1.12, sy: 0.86, ex: 0.7, ey: 0.68, ox: -0.14, oy: 0.2, rot: -3 },
    { text: 'Toxins are everywhere.', sx: -0.08, sy: 0.15, ex: 0.3, ey: 0.2, ox: 1.12, oy: 0.85, rot: 6, hot: true },
    { text: 'One hack. Done.', sx: 1.08, sy: 0.28, ex: 0.68, ey: 0.34, ox: -0.12, oy: 0.9, rot: -2 },
    { text: 'Science says so.', sx: 0.4, sy: 1.1, ex: 0.5, ey: 0.72, ox: 0.15, oy: -0.1, rot: 3, hot: true },
    { text: 'Doubt is weakness.', sx: 0.75, sy: -0.06, ex: 0.58, ey: 0.18, ox: 0.25, oy: 1.14, rot: -4 }
  ];

  /**
   * Emotional arc (1-based phrases):
   * 1–5   SLOW  — readable, confident
   * 6–12  BUILD — progressively faster, confidence thinning
   * 13+   RUSH  — overwhelm → whirlwind tail
   * Then explode phases (crowd → blowout → thesis).
   */
  const SLOW_COUNT = 5;   /* indices 0..4 */
  const BUILD_END = 12;   /* indices 5..11 build; 12+ = phrase 13 rush */

  function claimDelay(i) {
    if (i === 0) return 0;
    if (i < SLOW_COUNT) return i * 1150;

    let d = (SLOW_COUNT - 1) * 1150;
    const buildLen = BUILD_END - SLOW_COUNT;

    for (let k = SLOW_COUNT; k <= i && k < BUILD_END; k++) {
      const t = (k - SLOW_COUNT) / Math.max(buildLen - 1, 1);
      /* Early build still readable; pace picks up sooner than before. */
      d += Math.round(780 - easeInQuad(t) * (780 - 260));
    }

    if (i < BUILD_END) return d;

    const rushLen = CLAIMS.length - BUILD_END;
    for (let k = BUILD_END; k <= i; k++) {
      const t = (k - BUILD_END) / Math.max(rushLen - 1, 1);
      /* Whirlwind: gaps collapse a beat sooner toward the end. */
      d += Math.round(155 - easeInQuad(t) * (155 - 22));
    }
    return d;
  }

  function claimTravelMs(i) {
    if (i < SLOW_COUNT) return 1040 - i * 35;
    if (i < BUILD_END) {
      const t = (i - SLOW_COUNT) / Math.max(BUILD_END - SLOW_COUNT - 1, 1);
      return Math.round(700 - easeInQuad(t) * (700 - 390));
    }
    const rushLen = Math.max(CLAIMS.length - BUILD_END - 1, 1);
    const t = (i - BUILD_END) / rushLen;
    return Math.round(290 - easeInQuad(t) * (290 - 165));
  }

  const TIMING = {
    voidMs: 480,
    overwhelmMs: 880,
    collapseMs: 780,
    /* Arrive ~920ms, then hold so the line can be read. */
    thesisArriveMs: 920,
    thesisHoldMs: 850,
    fadeMs: 950
  };
  TIMING.thesisMs = TIMING.thesisArriveMs + TIMING.thesisHoldMs;
  TIMING.barrageMs = claimDelay(CLAIMS.length - 1) + claimTravelMs(CLAIMS.length - 1) + 220;

  function clamp(n, a, b) {
    return Math.max(a, Math.min(b, n));
  }

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function easeInOutCubic(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  function easeInQuad(t) {
    return t * t;
  }

  const SEEN_KEY = 'rv-home-weather-seen';

  function hasSeenWeather() {
    try {
      return sessionStorage.getItem(SEEN_KEY) === '1';
    } catch (e) {
      return false;
    }
  }

  function markWeatherSeen() {
    try {
      sessionStorage.setItem(SEEN_KEY, '1');
    } catch (e) { /* private mode / blocked storage */ }
  }

  function isHardReload() {
    try {
      const nav = performance.getEntriesByType('navigation')[0];
      return !!(nav && nav.type === 'reload');
    } catch (e) {
      return false;
    }
  }

  function shouldPlayWeather() {
    /* First open in the session, or hard refresh. Skip same-tab returns home. */
    return isHardReload() || !hasSeenWeather();
  }

  function finish(hero, opts) {
    if (finish.sent) return;
    finish.sent = true;
    const instant = opts && opts.instant;
    if (hero) {
      hero.classList.add('is-phase-done');
      if (instant) {
        hero.classList.add('is-dismissed');
      } else {
        window.setTimeout(function () {
          hero.classList.add('is-dismissed');
        }, TIMING.fadeMs + 40);
      }
    }
    document.body.classList.remove('home-hero-active');
    document.dispatchEvent(new CustomEvent('homehero:complete'));
  }

  function init() {
    const hero = document.querySelector('.home-hero--entrance');
    if (!hero) {
      document.body.classList.remove('home-hero-active');
      document.dispatchEvent(new CustomEvent('homehero:complete'));
      return;
    }

    if (reduceMotion || !shouldPlayWeather()) {
      finish(hero, { instant: true });
      return;
    }

    markWeatherSeen();

    const claimsLayer = hero.querySelector('.home-hero__claims');
    const thesisEl = hero.querySelector('.home-hero__thesis');
    const ledeEl = document.querySelector('.lede-primary--from-weather');
    if (!claimsLayer || !thesisEl) {
      finish(hero, { instant: true });
      return;
    }

    document.body.classList.add('home-hero-active');

    /* Never leave the page trapped under a black overlay. */
    const failsafe = window.setTimeout(function () {
      if (!hero.classList.contains('is-phase-done')) {
        finish(hero);
      }
    }, 28000);

    const claimNodes = CLAIMS.map(function (c, i) {
      const el = document.createElement('p');
      el.className = 'home-hero__claim' + (c.hot ? ' is-hot' : '');
      el.textContent = c.text;
      claimsLayer.appendChild(el);
      return {
        el: el,
        c: c,
        i: i,
        delay: claimDelay(i),
        travel: claimTravelMs(i),
        x: c.sx,
        y: c.sy,
        rot: c.rot,
        opacity: 0,
        blur: 0
      };
    });

    const thesis = {
      el: thesisEl,
      startX: 0,
      startY: 0,
      endX: 0,
      endY: 0,
      x: 0,
      y: 0,
      opacity: 0,
      blur: 2.2,
      width: 0
    };

    let phase = 'void';
    let phaseStart = performance.now();
    let raf = 0;
    let w = 1;
    let h = 1;
    let completed = false;

    function setPhase(name) {
      phase = name;
      phaseStart = performance.now();
      hero.classList.remove(
        'is-phase-void',
        'is-phase-barrage',
        'is-phase-overwhelm',
        'is-phase-collapse',
        'is-phase-thesis',
        'is-phase-done'
      );
      hero.classList.add('is-phase-' + name);
    }

    function measure() {
      const rect = hero.getBoundingClientRect();
      w = Math.max(rect.width, 1);
      h = Math.max(rect.height, 1);
    }

    /** Seat the flying thesis on the real welcome lede box. */
    function measureThesisSeat() {
      measure();
      const heroRect = hero.getBoundingClientRect();
      if (!ledeEl) {
        thesis.endX = Math.min(160, w * 0.1);
        thesis.endY = h * 0.42;
        thesis.width = Math.min(840, w * 0.72);
      } else {
        const ledeRect = ledeEl.getBoundingClientRect();
        thesis.endX = ledeRect.left - heroRect.left;
        thesis.endY = ledeRect.top - heroRect.top;
        thesis.width = Math.max(ledeRect.width, 1);
        const cs = window.getComputedStyle(ledeEl);
        thesisEl.style.fontSize = cs.fontSize;
        thesisEl.style.lineHeight = cs.lineHeight;
        thesisEl.style.letterSpacing = cs.letterSpacing;
        thesisEl.style.fontWeight = cs.fontWeight;
        thesisEl.style.maxWidth = thesis.width + 'px';
        thesisEl.style.width = thesis.width + 'px';
      }
      /* Enter from the right; land exactly on the seat. */
      thesis.startX = w + Math.min(120, w * 0.12);
      thesis.startY = thesis.endY;
      thesis.x = thesis.startX;
      thesis.y = thesis.startY;
    }

    function placeClaim(node) {
      node.el.style.transform =
        'translate3d(' + (node.x * w) + 'px,' + (node.y * h) + 'px,0) translate(-50%,-50%) rotate(' + node.rot + 'deg)';
      node.el.style.opacity = String(node.opacity);
      node.el.style.filter = node.blur > 0.05 ? 'blur(' + node.blur + 'px)' : 'none';
    }

    function placeThesis() {
      thesis.el.style.transform =
        'translate3d(' + thesis.x + 'px,' + thesis.y + 'px,0)';
      thesis.el.style.opacity = String(thesis.opacity);
      thesis.el.style.filter = thesis.blur > 0.05 ? 'blur(' + thesis.blur + 'px)' : 'none';
    }

    function advancePhase(now) {
      const elapsed = now - phaseStart;
      if (phase === 'void' && elapsed >= TIMING.voidMs) {
        setPhase('barrage');
        return;
      }
      if (phase === 'barrage' && elapsed >= TIMING.barrageMs) {
        setPhase('overwhelm');
        return;
      }
      if (phase === 'overwhelm' && elapsed >= TIMING.overwhelmMs) {
        setPhase('collapse');
        return;
      }
      if (phase === 'collapse' && elapsed >= TIMING.collapseMs) {
        measureThesisSeat();
        setPhase('thesis');
        thesis.opacity = 0;
        thesis.blur = 2.2;
        placeThesis();
        return;
      }
      if (phase === 'thesis' && elapsed >= TIMING.thesisMs && !completed) {
        completed = true;
        window.clearTimeout(failsafe);
        /* Snap to seat so the crossfade has no drift. */
        thesis.x = thesis.endX;
        thesis.y = thesis.endY;
        thesis.opacity = 1;
        thesis.blur = 0;
        placeThesis();
        finish(hero);
        if (raf) {
          cancelAnimationFrame(raf);
          raf = 0;
        }
      }
    }

    function updateClaims(now) {
      const t0 = phaseStart;

      claimNodes.forEach(function (node) {
        const c = node.c;
        const local = now - t0 - node.delay;

        if (phase === 'void') {
          node.opacity = 0;
          node.x = c.sx;
          node.y = c.sy;
          node.rot = c.rot;
          node.blur = 0;
        } else if (phase === 'barrage') {
          if (local < 0) {
            node.opacity = 0;
            node.x = c.sx;
            node.y = c.sy;
          } else {
            const t = clamp(local / node.travel, 0, 1);
            const e = easeOutCubic(t);
            node.x = lerp(c.sx, c.ex, e);
            node.y = lerp(c.sy, c.ey, e);
            node.rot = lerp(c.rot * 1.8, c.rot, e);
            node.opacity = clamp(t * 1.35, 0, c.hot ? 0.95 : 0.78);
            node.blur = (1 - t) * 1.1;
          }
        } else if (phase === 'overwhelm') {
          /* Explode prep: crush toward center, lose legibility. */
          const t = clamp((now - t0) / TIMING.overwhelmMs, 0, 1);
          const e = easeInOutCubic(t);
          const crush = 0.38;
          node.x = lerp(c.ex, lerp(c.ex, 0.5, crush), e);
          node.y = lerp(c.ey, lerp(c.ey, 0.48, crush * 0.85), e);
          node.rot = c.rot + Math.sin((now + node.delay) * 0.012) * (2.2 + t * 4);
          node.opacity = c.hot ? lerp(0.95, 0.55, e) : lerp(0.78, 0.22, e);
          node.blur = c.hot ? 0.6 + e * 2.4 : 1.4 + e * 4.5;
        } else if (phase === 'collapse') {
          /* Blowout: fast exit, heavy spin, gone. */
          const stagger = (node.i % 5) * 28;
          const t = clamp((now - t0 - stagger) / 520, 0, 1);
          const e = easeInQuad(clamp(t, 0, 1));
          const fromX = lerp(c.ex, 0.5, 0.38);
          const fromY = lerp(c.ey, 0.48, 0.32);
          node.x = lerp(fromX, c.ox, e);
          node.y = lerp(fromY, c.oy, e);
          node.rot = c.rot + e * (c.rot >= 0 ? 22 : -22);
          node.opacity = lerp(c.hot ? 0.55 : 0.22, 0, e);
          node.blur = 2.5 + e * 8;
        } else {
          node.opacity = 0;
        }

        placeClaim(node);
      });
    }

    function updateThesis(now) {
      if (phase !== 'thesis') {
        if (phase !== 'collapse') {
          thesis.opacity = 0;
          placeThesis();
        }
        return;
      }

      const t = clamp((now - phaseStart) / TIMING.thesisArriveMs, 0, 1);
      const e = easeOutCubic(t);
      thesis.x = lerp(thesis.startX, thesis.endX, e);
      thesis.y = lerp(thesis.startY, thesis.endY, e);
      thesis.opacity = clamp(t * 1.15, 0, 1);
      thesis.blur = (1 - e) * 2.0;
      placeThesis();
    }

    function frame(now) {
      if (!completed) advancePhase(now);
      updateClaims(now);
      updateThesis(now);
      if (!completed) raf = requestAnimationFrame(frame);
    }

    measure();
    window.addEventListener('resize', function () {
      measure();
      if (phase === 'thesis' || phase === 'done') {
        measureThesisSeat();
        thesis.x = thesis.endX;
        thesis.y = thesis.endY;
        placeThesis();
      }
    });
    setPhase('void');
    raf = requestAnimationFrame(frame);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

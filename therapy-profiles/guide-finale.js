/* Scroll finale — split hero: subtle rise, hold runway, hint fade */

var HERO_HOLD_VH = 0.50;

window.HeroProgress = function (stage) {
  return function () {
    var vh = window.innerHeight;
    var total = stage.offsetHeight - vh;
    if (total <= 0) return 0;
    var holdPx = vh * HERO_HOLD_VH;
    var animH = Math.max(vh * 0.35, total - holdPx);
    var scrolled = Math.max(0, -stage.getBoundingClientRect().top);
    if (scrolled >= animH) return 1;
    return Math.min(1, scrolled / animH);
  };
};

window.HeroFinale = function (stage, climax, hint) {
  function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

  var resolution = stage.querySelector('.guide-resolution');
  var riseStart = window.matchMedia('(min-width: 56rem)').matches ? 30 : 22;

  return function applyFinale(p) {
    var resolve = easeOut(clamp((p - 0.22) / 0.48, 0, 1));
    if (resolution) {
      resolution.style.transform = 'translateY(' + lerp(riseStart, 0, resolve) + 'px)';
    }
    if (climax) {
      climax.style.color = 'rgba(255, 253, 246, ' + (resolve * 0.94).toFixed(3) + ')';
      climax.style.borderLeftColor = 'rgba(184, 96, 46, ' + (resolve * 0.55).toFixed(3) + ')';
    }
    if (hint) {
      hint.style.opacity = String(1 - clamp((p - 0.08) / 0.16, 0, 1));
    }
  };
};

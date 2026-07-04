(function () {
  'use strict';

  var stage = document.querySelector('.guide-overture');
  if (!stage) return;

  var arcs = stage.querySelectorAll('[data-guide-arc]');
  var remnant = stage.querySelector('[data-guide-remnant]');
  var ringPath = stage.querySelector('[data-guide-ring-path]');
  var resolution = stage.querySelector('.guide-resolution');
  var climax = resolution ? resolution.querySelector('.guide-resolution__climax') : null;
  var hint = stage.querySelector('.guide-scroll-hint');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var CX = 120;
  var CY = 120;

  function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function easeInOut(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

  var ringLen = 0;
  if (ringPath) {
    ringLen = typeof ringPath.getTotalLength === 'function' ? ringPath.getTotalLength() : 565;
    ringPath.style.strokeDasharray = String(ringLen);
    ringPath.style.strokeDashoffset = String(ringLen);
  }

  function progress() {
    var h = stage.offsetHeight - window.innerHeight;
    if (h <= 0) return 0;
    return clamp(-stage.getBoundingClientRect().top / h, 0, 1);
  }

  function arcTransform(x, y, deg) {
    return 'translate(' + x + ' ' + y + ') rotate(' + deg + ' ' + CX + ' ' + CY + ')';
  }

  function scaleAbout(s) {
    return 'translate(' + CX + ' ' + CY + ') scale(' + s + ') translate(' + (-CX) + ' ' + (-CY) + ')';
  }

  function apply() {
    var p = progress();
    var converge = easeInOut(clamp((p - 0.06) / 0.32, 0, 1));
    var remnantT = easeOut(clamp((p - 0.36) / 0.12, 0, 1));
    var ringT = easeOut(clamp((p - 0.44) / 0.14, 0, 1));
    var resolve = easeOut(clamp((p - 0.54) / 0.26, 0, 1));

    if (reduced) {
      if (climax) {
        climax.style.color = 'rgba(255, 253, 246, 0.94)';
        climax.style.borderLeftColor = 'rgba(184, 96, 46, 0.55)';
      }
      if (remnant) {
        remnant.style.opacity = '1';
        remnant.setAttribute('transform', scaleAbout(1));
      }
      if (ringPath) {
        ringPath.style.strokeDashoffset = '0';
        ringPath.style.opacity = '1';
      }
      arcs.forEach(function (arc) {
        var base = parseFloat(arc.getAttribute('data-rot-base') || '0');
        arc.setAttribute('transform', arcTransform(0, 0, base));
        arc.style.opacity = '1';
      });
      return;
    }

    var spreadX = 52;
    var spreadY = 44;

    arcs.forEach(function (arc) {
      var fx = parseFloat(arc.getAttribute('data-fx') || '0');
      var fy = parseFloat(arc.getAttribute('data-fy') || '0');
      var base = parseFloat(arc.getAttribute('data-rot-base') || '0');
      var x = lerp(fx * spreadX, 0, converge);
      var y = lerp(fy * spreadY, 0, converge);

      arc.setAttribute('transform', arcTransform(x, y, base));
      arc.style.opacity = String(lerp(0.72, 1, converge));
    });

    if (remnant) {
      remnant.style.opacity = String(remnantT);
      remnant.setAttribute('transform', scaleAbout(lerp(0.92, 1, remnantT)));
    }

    if (ringPath) {
      ringPath.style.strokeDashoffset = String(ringLen * (1 - ringT));
      ringPath.style.opacity = String(ringT);
    }

    if (resolution) {
      resolution.style.transform = 'translateY(' + lerp(14, 0, resolve) + 'px)';
    }
    if (climax) {
      climax.style.color = 'rgba(255, 253, 246, ' + (resolve * 0.94).toFixed(3) + ')';
      climax.style.borderLeftColor = 'rgba(184, 96, 46, ' + (resolve * 0.55).toFixed(3) + ')';
    }
    if (hint) {
      hint.style.opacity = String(1 - clamp((p - 0.26) / 0.22, 0, 1));
    }
  }

  window.addEventListener('scroll', apply, { passive: true });
  window.addEventListener('resize', apply);
  apply();
})();

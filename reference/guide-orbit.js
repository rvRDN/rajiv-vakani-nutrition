/**
 * Guide Orbit — parameterized hero wheel.
 * Set window.GuideOrbitConfig before this script loads.
 *
 * components: number of color groups (1 = single-ingredient mode)
 * colors: [[r,g,b], ...] one RGB triplet per component
 * segmentsPerComponent: arc segments per component (default 5)
 */
(function () {
  'use strict';

  var defaults = {
    components: 3,
    colors: [
      [196, 131, 82],
      [255, 253, 246],
      [138, 125, 104]
    ],
    segmentsPerComponent: 5
  };

  var user = window.GuideOrbitConfig || {};
  var components = Math.max(1, user.components || defaults.components);
  var COLORS = user.colors && user.colors.length ? user.colors : defaults.colors;
  while (COLORS.length < components) {
    COLORS.push(COLORS[COLORS.length - 1]);
  }
  COLORS = COLORS.slice(0, components);

  var SEGMENTS = components * (user.segmentsPerComponent || defaults.segmentsPerComponent);
  var COUNT = 720;

  var stage = document.querySelector('.guide-overture');
  var canvas = document.getElementById('guide-orbit-canvas');
  if (!stage || !canvas) return;

  var brackets = stage.querySelector('.focus-brackets');
  var outerRing = stage.querySelector('[data-focus-outer]');
  var innerRing = stage.querySelector('[data-focus-inner]');
  var climax = stage.querySelector('.guide-resolution__climax');
  var hint = stage.querySelector('.guide-scroll-hint');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var progress = HeroProgress(stage);
  var finale = HeroFinale(stage, climax, hint);
  var ctx = canvas.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var dots = [];
  var time = 0;
  var smoothP = 0;

  var HUB_X = 0.5;
  var HUB_Y = 0.5;

  var CLOUDS = [];
  for (var c = 0; c < components; c++) {
    var angle = (c / components) * Math.PI * 2 - Math.PI / 2;
    var radius = components === 1 ? 0 : 0.1;
    CLOUDS.push({
      x: 0.5 + Math.cos(angle) * radius,
      y: 0.5 + Math.sin(angle) * radius
    });
  }

  var SEG_WEIGHTS = [];
  for (var s = 0; s < SEGMENTS; s++) {
    SEG_WEIGHTS.push(0.9 + (s % 3) * 0.06);
  }

  var outerLen = 0;
  var innerLen = 0;
  if (outerRing && outerRing.getTotalLength) {
    outerLen = outerRing.getTotalLength();
    outerRing.style.strokeDasharray = String(outerLen);
    outerRing.style.strokeDashoffset = String(outerLen);
  }
  if (innerRing && innerRing.getTotalLength) {
    innerLen = innerRing.getTotalLength();
    innerRing.style.strokeDasharray = String(innerLen);
    innerRing.style.strokeDashoffset = String(innerLen);
  }

  function rgba(rgb, a) {
    return 'rgba(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ',' + a + ')';
  }

  function clamp(t, lo, hi) {
    return Math.min(hi, Math.max(lo, t));
  }

  function smoothstep(t) {
    t = clamp(t, 0, 1);
    return t * t * (3 - 2 * t);
  }

  function easeOut(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function lerp(a, b, t) {
    return a + (b - a) * t;
  }

  function lerpAngle(a, b, t) {
    var d = Math.atan2(Math.sin(b - a), Math.cos(b - a));
    return a + d * t;
  }

  function gauss() {
    var u = 0;
    var v = 0;
    while (u === 0) u = Math.random();
    while (v === 0) v = Math.random();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  function segmentCount(seg) {
    var base = Math.floor(COUNT / SEGMENTS);
    return Math.max(12, Math.round(base * SEG_WEIGHTS[seg]));
  }

  function hubDistance(d) {
    return d.hubR * 1.55 + 0.042;
  }

  function targetAngle(seg) {
    var slice = (Math.PI * 2) / SEGMENTS;
    var base = seg * slice - Math.PI / 2;
    return base + Math.random() * slice * 0.88 + slice * 0.06;
  }

  function colorForSegment(seg) {
    return seg % components;
  }

  function seed() {
    dots = [];
    for (var seg = 0; seg < SEGMENTS; seg++) {
      var colorIdx = colorForSegment(seg);
      var cloud = CLOUDS[colorIdx];
      var perSeg = segmentCount(seg);
      for (var i = 0; i < perSeg; i++) {
        var ta = targetAngle(seg);
        var tr = 0.19 + Math.random() * 0.13;
        var spread = components === 1 ? 0.07 : 0.09 + Math.random() * 0.05;
        var ox = gauss() * spread;
        var oy = gauss() * spread;
        var roll = Math.random();
        var straggler = roll < 0.07;
        var edgeWander = !straggler && Math.random() < 0.045;
        var innerA = Math.random() * Math.PI * 2;
        var innerR = 0.028 + Math.random() * 0.085;
        dots.push({
          c: colorIdx,
          ta: ta,
          tr: tr,
          tx: HUB_X + Math.cos(ta) * tr,
          ty: HUB_Y + Math.sin(ta) * tr,
          sx: cloud.x + ox,
          sy: cloud.y + oy,
          startA: Math.atan2(cloud.y + oy - HUB_Y, cloud.x + ox - HUB_X),
          orbitSpeed: (Math.random() > 0.5 ? 1 : -1) * (0.35 + Math.random() * 0.9),
          hubR: 0.018 + Math.random() * 0.045,
          delay: (seg / SEGMENTS) * 0.09 + Math.random() * 0.06,
          phase: Math.random() * Math.PI * 2,
          straggler: straggler,
          edgeWander: edgeWander,
          innerA: innerA,
          innerR: innerR,
          ix: HUB_X + Math.cos(innerA) * innerR,
          iy: HUB_Y + Math.sin(innerA) * innerR,
          wander: 0.5 + Math.random() * 0.85
        });
      }
    }
  }

  function resize() {
    var rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function phaseWeights(p) {
    return {
      breathe: smoothstep(p / 0.12),
      inward: smoothstep((p - 0.04) / 0.22),
      orbit: smoothstep((p - 0.12) / 0.26),
      exchange: smoothstep((p - 0.28) / 0.30),
      expand: smoothstep((p - 0.44) / 0.26),
      settle: smoothstep((p - 0.60) / 0.28)
    };
  }

  function inwardAmount(w) {
    return w.inward * 0.82;
  }

  function stragglerPos(d, w) {
    var x = d.sx;
    var y = d.sy;
    var inAmt = inwardAmount(w);
    var hubDist = hubDistance(d);

    if (w.breathe < 0.95) {
      var drift = (1 - w.breathe) * 0.01;
      x += Math.sin(time * 0.6 + d.phase) * drift;
      y += Math.cos(time * 0.5 + d.phase) * drift;
    }

    var orbitA = d.innerA + time * d.orbitSpeed * 0.12 * w.orbit;
    var orbitR = lerp(hubDist * 0.85, d.innerR, w.orbit);
    var hubX = HUB_X + Math.cos(d.startA) * hubDist * 0.72;
    var hubY = HUB_Y + Math.sin(d.startA) * hubDist * 0.72;
    var orbitX = HUB_X + Math.cos(orbitA) * orbitR;
    var orbitY = HUB_Y + Math.sin(orbitA) * orbitR;

    x = lerp(x, hubX, inAmt);
    y = lerp(y, hubY, inAmt);
    x = lerp(x, orbitX, w.orbit);
    y = lerp(y, orbitY, w.orbit);

    var hold = Math.max(w.orbit, w.settle);
    x = lerp(x, d.ix, hold * 0.85);
    y = lerp(y, d.iy, hold * 0.85);

    if (w.settle > 0.35 || smoothP >= 0.92) {
      x += Math.sin(time * 0.28 + d.phase) * 0.011 * d.wander;
      y += Math.cos(time * 0.24 + d.phase * 1.1) * 0.009 * d.wander;
    }

    return { x: x, y: y, lock: hold * 0.7, inner: true };
  }

  function ringPos(d, p, w) {
    // smoothP approaches 1 asymptotically and rarely crosses it, so snap
    // once settle is complete (same threshold used in stragglerPos).
    if (reduced || p >= 0.92) {
      if (d.edgeWander) {
        return {
          x: d.tx + Math.sin(time * 0.42 + d.phase) * 0.018 * d.wander,
          y: d.ty + Math.cos(time * 0.36 + d.phase) * 0.015 * d.wander,
          lock: 0.88,
          inner: false
        };
      }
      return { x: d.tx, y: d.ty, lock: 1, inner: false };
    }

    var cx = d.sx;
    var cy = d.sy;
    if (w.breathe < 0.92) {
      var drift = (1 - w.breathe) * 0.01;
      cx += Math.sin(time * 0.65 + d.phase) * drift;
      cy += Math.cos(time * 0.5 + d.phase) * drift;
    }

    var inAmt = inwardAmount(w);
    var hubDist = hubDistance(d);
    var cloudR = Math.sqrt((cx - HUB_X) * (cx - HUB_X) + (cy - HUB_Y) * (cy - HUB_Y)) || 0.001;
    var cloudA = Math.atan2(cy - HUB_Y, cx - HUB_X);
    var spin = time * d.orbitSpeed * 0.2 * w.orbit * (1 - w.expand * 0.9);
    var orbitA = d.startA + spin;

    var angle = lerpAngle(cloudA, orbitA, w.orbit);
    angle = lerpAngle(angle, d.ta, w.exchange);

    var r = lerp(cloudR, hubDist, inAmt);
    r = lerp(r, hubDist + 0.052, w.orbit);
    r = lerp(r, d.tr * 0.62, w.exchange * (1 - w.expand * 0.35));
    r = lerp(r, d.tr, w.expand);

    var x = HUB_X + Math.cos(angle) * r;
    var y = HUB_Y + Math.sin(angle) * r;

    var early = 1 - inAmt;
    x = lerp(cx, x, 1 - early * 0.3);
    y = lerp(cy, y, 1 - early * 0.3);

    var lockStart = 0.62 + d.delay;
    var lockP = smoothstep(clamp((p - lockStart) / 0.28, 0, 1));
    if (d.edgeWander) lockP = Math.min(lockP, 0.86);

    x = lerp(x, d.tx, lockP);
    y = lerp(y, d.ty, lockP);

    if (d.edgeWander && lockP > 0.45) {
      var live = (lockP - 0.45) * 1.8;
      x += Math.sin(time * 0.44 + d.phase) * 0.02 * live * d.wander;
      y += Math.cos(time * 0.38 + d.phase) * 0.016 * live * d.wander;
    }

    return { x: x, y: y, lock: lockP, inner: false };
  }

  function draw(p) {
    var w = canvas.getBoundingClientRect().width;
    var h = canvas.getBoundingClientRect().height;
    var weights = phaseWeights(p);
    var sharp = easeOut(clamp((p - 0.4) / 0.14, 0, 1));
    var ringT = easeOut(clamp((p - 0.44) / 0.14, 0, 1));

    ctx.clearRect(0, 0, w, h);

    for (var i = 0; i < dots.length; i++) {
      var d = dots[i];
      var pos = d.straggler ? stragglerPos(d, weights) : ringPos(d, p, weights);
      var soft = (1 - pos.lock) * 2.2;
      var alpha = 0.14 + weights.inward * 0.2 + pos.lock * 0.46;
      if (pos.inner) alpha *= 0.72 + Math.sin(time * 0.3 + d.phase) * 0.08;
      var rad = (pos.inner ? 0.62 : 0.75) + pos.lock * 0.55 + soft * 0.05;

      ctx.beginPath();
      ctx.arc(pos.x * w, pos.y * h, rad, 0, Math.PI * 2);
      ctx.fillStyle = rgba(COLORS[d.c], alpha);
      ctx.fill();
    }

    if (outerRing) {
      outerRing.style.strokeDashoffset = String(outerLen * (1 - ringT));
      outerRing.style.opacity = String(ringT);
    }
    if (innerRing) {
      innerRing.style.strokeDashoffset = String(innerLen * (1 - Math.min(1, ringT * 1.05)));
      innerRing.style.opacity = String(ringT * 0.95);
    }
    if (brackets) brackets.style.opacity = String(sharp * 0.9);

    finale(p);
  }

  function frame() {
    time += 0.016;
    var targetP = reduced ? 1 : progress();
    var delta = Math.abs(targetP - smoothP);
    var blend = delta > 0.02 ? 0.28 : 0.38;
    smoothP += (targetP - smoothP) * blend;
    draw(smoothP);
    requestAnimationFrame(frame);
  }

  seed();
  resize();
  window.addEventListener('resize', function () {
    resize();
    seed();
  });
  requestAnimationFrame(frame);
})();

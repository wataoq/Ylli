// ================= Record: the symbol, hung and stitched, and the path its crossing point draws =================
// Six rigid pieces (A: the heavy path, B: the hairline path), stitched at the seams, the crossing tied,
// the two top pieces hung from pins. Units are the symbol's own: 1 unit = 1 mm.
(function(){
  const rs = document.getElementById('rs'), rec = document.getElementById('rec');
  const rc = document.getElementById('rc'), rctx = rc.getContext('2d');
  const C = D.cross;
  const bodies = Object.entries(D.pieces).map(([id, p]) => ({
    id, m: p.area / 100, I: p.I / 100, c: p.c, x: p.c[0], y: p.c[1], a: 0, vx: 0, vy: 0, va: 0, fx: 0, fy: 0, t: 0, d: p.d,
    g: el('g', {}, null),
    // per-visit character: how this piece answers to the visitor's movement
    sx: rnd(-1, 1), sr: rnd(-1, 1), ph: rnd(0, 6.28)
  }));
  const B = Object.fromEntries(bodies.map(b => [b.id, b]));
  const springs = [];
  D.seams.forEach(([a, b, px, py]) => springs.push({a: B[a], b: B[b], pa: [px, py], pb: [px, py], k: 3000, c: 30, seam: true, open: 0}));
  springs.push({a: B.A2, b: B.B2, pa: C, pb: C, k: 1100, c: 14, seam: false, open: 0});
  const pins = [{b: B.A1, p: [8.5, 0], at: [8.5, 0]}, {b: B.B1, p: [51.6, 0], at: [51.6, 0]}];

  const gSeam = el('g', {}, rs), gPieces = el('g', {}, rs);
  bodies.forEach(b => { gPieces.appendChild(b.g); el('path', {d: b.d, fill: SO}, b.g); });
  const stitch = springs.map(() => el('line', {stroke: SO, 'stroke-width': .7, 'stroke-dasharray': '2 1.6', 'vector-effect': 'non-scaling-stroke', opacity: 0}, gSeam));
  const pinMarks = pins.map(() => el('line', {stroke: NIBI, 'stroke-width': .7, 'vector-effect': 'non-scaling-stroke'}, gSeam));

  const world = (b, p) => {
    const cs = Math.cos(b.a), sn = Math.sin(b.a), rx = p[0] - b.c[0], ry = p[1] - b.c[1];
    return [b.x + rx * cs - ry * sn, b.y + rx * sn + ry * cs, rx * cs - ry * sn, rx * sn + ry * cs];
  };
  const velAt = (b, r) => [b.vx - b.va * r[1], b.vy + b.va * r[0]];
  const force = (b, r, fx, fy) => { b.fx += fx; b.fy += fy; b.t += r[0] * fy - r[1] * fx; };

  // the symbol hangs from the top edge of the record; the trace is drawn in the same coordinates, over it
  let vb = {x: 0, y: 0, w: 1, h: 1}, box = {w: 1, h: 1};
  const trace = [];
  function layout() {
    const r = rec.getBoundingClientRect(); box = {w: r.width, h: r.height};
    const h = D.h / .8, w = h * (r.width / Math.max(1, r.height));
    vb = {x: C[0] - w / 2, y: -h * .08, w, h};
    rs.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
    pins.forEach((p, i) => { const L = pinMarks[i]; L.setAttribute('x1', p.at[0]); L.setAttribute('x2', p.at[0]); L.setAttribute('y1', vb.y); L.setAttribute('y2', p.at[1]); });
    const dpr = Math.min(2, devicePixelRatio || 1);
    rc.width = Math.round(r.width * dpr); rc.height = Math.round(r.height * dpr); rctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    redraw();
  }
  const MAG = 4;   // the path is drawn around the crossing, magnified
  const toPx = p => { const x = C[0] + (p[0] - C[0]) * MAG, y = C[1] + (p[1] - C[1]) * MAG; return [(x - vb.x) / vb.w * box.w, (y - vb.y) / vb.h * box.h]; };
  function redraw() {
    rctx.clearRect(0, 0, box.w, box.h);
    rctx.strokeStyle = SO; rctx.lineWidth = .8; rctx.lineJoin = 'round'; rctx.beginPath();
    trace.forEach((p, i) => { const q = toPx(p); i ? rctx.lineTo(q[0], q[1]) : rctx.moveTo(q[0], q[1]); });
    rctx.stroke();
  }
  addEventListener('resize', layout); layout();

  const G = 60;
  let time = 0, opened = 0;
  function step(dt) {
    time += dt;
    bodies.forEach(b => {
      b.fx = 0; b.fy = b.m * G; b.t = 0;
      if (!reduceMotion) {   // air: a slow, never-repeating drift, small
        const n = Math.sin(time * .5 + b.ph) + Math.sin(time * 1.13 + b.ph * 2.1) * .6 + Math.sin(time * 2.3 + b.ph * .7) * .25;
        b.fx += n * b.m * 1.6;
      }
    });
    springs.forEach(s => {
      if (s.open > 0) { s.open -= dt; return; }
      const A = world(s.a, s.pa), Bw = world(s.b, s.pb);
      const dx = Bw[0] - A[0], dy = Bw[1] - A[1];
      const va = velAt(s.a, [A[2], A[3]]), vbv = velAt(s.b, [Bw[2], Bw[3]]);
      const fx = s.k * dx + s.c * (vbv[0] - va[0]), fy = s.k * dy + s.c * (vbv[1] - va[1]);
      force(s.a, [A[2], A[3]], fx, fy); force(s.b, [Bw[2], Bw[3]], -fx, -fy);
      if (s.seam && Math.hypot(dx, dy) > 40) { s.open = rnd(1, 2.4); opened++; }   // pulled too far: opens, then is sewn again
    });
    pins.forEach(p => {
      const W = world(p.b, p.p), v = velAt(p.b, [W[2], W[3]]);
      force(p.b, [W[2], W[3]], -9000 * (W[0] - p.at[0]) - 60 * v[0], -9000 * (W[1] - p.at[1]) - 60 * v[1]);
    });
    bodies.forEach(b => {
      b.fx += -3 * b.m * (b.x - b.c[0]); b.fy += -3 * b.m * (b.y - b.c[1]); b.t += -1.6 * b.I * Math.sin(b.a);
      b.vx += b.fx / b.m * dt; b.vy += b.fy / b.m * dt; b.va += b.t / b.I * dt;
      const damp = Math.exp(-1.8 * dt); b.vx *= damp; b.vy *= damp; b.va *= Math.exp(-2.4 * dt);
      b.x += b.vx * dt; b.y += b.vy * dt; b.a += b.va * dt;
    });
  }

  // the visitor's movement: scrolling anywhere on the page, the pointer over the record
  let lastScroll = scrollY, pointer = null;
  addEventListener('scroll', () => {
    const dy = scrollY - lastScroll; lastScroll = scrollY;
    if (reduceMotion) return;
    const k = Math.max(-40, Math.min(40, dy));
    bodies.forEach(b => { b.vx += k * .55 * b.sx; b.vy += k * .2; b.va += k * .004 * b.sr; });
  }, {passive: true});
  rec.addEventListener('pointermove', e => {
    const r = rec.getBoundingClientRect();
    const x = vb.x + (e.clientX - r.left) / r.width * vb.w, y = vb.y + (e.clientY - r.top) / r.height * vb.h;
    if (pointer && !reduceMotion) {
      const dt = Math.max(.008, (e.timeStamp - pointer.t) / 1000);
      const pvx = (x - pointer.x) / dt, pvy = (y - pointer.y) / dt;
      bodies.forEach(b => {
        const W = world(b, b.c), f = Math.max(0, 1 - Math.hypot(W[0] - x, W[1] - y) / 50);
        if (f > 0) { b.vx += pvx * f * .035; b.vy += pvy * f * .035; }
      });
    }
    pointer = {x, y, t: e.timeStamp};
  });
  rec.addEventListener('pointerleave', () => { pointer = null; });

  const qN = document.getElementById('q-n'), qS = document.getElementById('q-s'), qD = document.getElementById('q-d'), qT = document.getElementById('q-t'), qO = document.getElementById('q-o');
  let prev = performance.now(); const t0 = prev; let dist = 0, lastC = null;
  function frame(now) {
    const dtf = Math.max(0, Math.min(.05, (now - prev) / 1000)); prev = now;
    for (let i = 0; i < 16; i++) step(dtf / 16);
    bodies.forEach(b => b.g.setAttribute('transform', `translate(${b.x} ${b.y}) rotate(${b.a * 57.2958}) translate(${-b.c[0]} ${-b.c[1]})`));
    let maxd = 0, intact = 0;
    springs.forEach((s, i) => {
      const A = world(s.a, s.pa), Bw = world(s.b, s.pb), d = Math.hypot(Bw[0] - A[0], Bw[1] - A[1]), L = stitch[i];
      L.setAttribute('x1', A[0]); L.setAttribute('y1', A[1]); L.setAttribute('x2', Bw[0]); L.setAttribute('y2', Bw[1]);
      if (s.open > 0) { L.setAttribute('stroke', NIBI); L.setAttribute('opacity', .7); }
      else { L.setAttribute('stroke', SO); L.setAttribute('opacity', Math.min(1, Math.max(0, (d - .8) / 4))); }
      if (s.seam) { maxd = Math.max(maxd, d); if (s.open <= 0) intact++; }
    });
    // the crossing point writes its path over the symbol, magnified around the crossing
    const cp = world(B.A2, C);
    if (!lastC || Math.hypot(cp[0] - lastC[0], cp[1] - lastC[1]) > .05) {
      if (lastC) {
        dist += Math.hypot(cp[0] - lastC[0], cp[1] - lastC[1]);
        const a = toPx(lastC), b2 = toPx(cp);
        rctx.strokeStyle = SO; rctx.lineWidth = .8; rctx.beginPath(); rctx.moveTo(a[0], a[1]); rctx.lineTo(b2[0], b2[1]); rctx.stroke();
      }
      trace.push([cp[0], cp[1]]); if (trace.length > 60000) trace.shift();
      lastC = [cp[0], cp[1]];
    }
    qN.textContent = maxd.toFixed(1) + ' mm'; qS.textContent = intact + ' / 8'; qD.textContent = (dist / 1000).toFixed(2) + ' m'; qO.textContent = opened;
    const sec = Math.floor((now - t0) / 1000); qT.textContent = String(Math.floor(sec / 60)).padStart(2, '0') + ':' + String(sec % 60).padStart(2, '0');
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();

// ================= band-cut heading: moved by the visitor's speed, not by position =================
(function(){
  const bands = [...document.querySelectorAll('.shift')].map(h => {
    const txt = h.textContent; h.textContent = '';
    const src = document.createElement('span'); src.className = 'src'; src.textContent = txt; h.appendChild(src);
    const cuts = [0, .18, .31, .47, .55, .72, .86, 1];
    return cuts.slice(0, -1).map((a, i) => {
      const b = document.createElement('span'); b.className = 'band'; b.setAttribute('aria-hidden', 'true'); b.textContent = txt;
      b.style.clipPath = `inset(${a * 100}% 0 ${(1 - cuts[i + 1]) * 100}% 0)`; h.appendChild(b);
      return {b, x: 0, v: 0, k: rnd(-1, 1)};
    });
  }).flat();
  let lastY = scrollY, prev = performance.now();
  function frame(now) {
    const dt = Math.max(0, Math.min(.05, (now - prev) / 1000)); prev = now;
    const dy = Math.max(-40, Math.min(40, scrollY - lastY)); lastY = scrollY;
    bands.forEach(s => { s.v += (reduceMotion ? 0 : dy * s.k * 1.2) - s.x * 90 * dt - s.v * 8 * dt; s.x += s.v * dt * 6; s.b.style.transform = `translateX(${s.x.toFixed(1)}px)`; });
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();

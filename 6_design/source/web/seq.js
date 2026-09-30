// --- the sequence
const st = document.getElementById('st');
const IDS = ['A1','A2','A3','B1','B2','B3'];
const P = D.pieces, C = D.cross;
// drift direction per piece (fractions of view width / height) and rotation (deg) at full displacement
const DRIFT = {A1:[-.30,-.02,-22], B1:[.31,.03,26], A2:[.13,.12,34], B2:[-.15,.16,-38], A3:[.24,.20,9], B3:[-.28,.10,-12]};
// grain rotation on the marker: the diagonals turn to vertical
const GRAIN = {A1:0, B1:0, A2:45, B2:-45, A3:0, B3:0};
const ORDER = ['A3','B3','A2','B2','A1','B1'];
const LABEL = {A1:'A-1',A2:'A-2',A3:'A-3',B1:'B-1',B2:'B-2',B3:'B-3'};

const gFab = el('g', {}, st), gSeam = el('g', {}, st), gPieces = el('g', {}, st), gTop = el('g', {}, st);
const fab = el('rect', {fill: 'none', stroke: NIBI, 'stroke-width': .5, 'vector-effect': 'non-scaling-stroke'}, gFab);
const fabTxt = el('text', {fill: NIBI, 'font-family': 'Noto Sans JP, sans-serif', 'font-size': 3.2, 'letter-spacing': .3}, gFab); fabTxt.textContent = 'SELVEDGE';
const grain = []; for (let i = 0; i < 6; i++) grain.push(el('path', {fill: 'none', stroke: NIBI, 'stroke-width': .5, 'vector-effect': 'non-scaling-stroke'}, gFab));
const nodes = {};
IDS.forEach(id => {
  const g = el('g', {}, gPieces);
  const path = el('path', {d: P[id].d, fill: INK}, g);
  const t = el('text', {fill: INK, 'font-family': 'Noto Sans JP, sans-serif', 'font-size': 3.4, 'letter-spacing': .2}, g); t.textContent = LABEL[id];
  nodes[id] = {g, path, t};
});
const seams = D.seams.map(() => el('line', {stroke: INK, 'stroke-width': .6, 'stroke-dasharray': '2 1.6', 'vector-effect': 'non-scaling-stroke'}, gSeam));
const crossLine = el('line', {stroke: INK, 'stroke-width': .6, 'stroke-dasharray': '2 1.6', 'vector-effect': 'non-scaling-stroke'}, gSeam);
const ring = el('circle', {r: 9, fill: 'none', stroke: SHIN, 'stroke-width': 1.2, 'vector-effect': 'non-scaling-stroke', opacity: 0}, gTop);

let vb = {x: 0, y: 0, w: 1, h: 1};
function layout() {
  const r = st.getBoundingClientRect(); const aspect = r.width / Math.max(1, r.height);
  const h = D.h / .74; const w = h * aspect;
  vb = {x: C[0] - w / 2, y: -1, w, h};
  st.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
}
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const ease = t => t < .5 ? 2*t*t : 1 - Math.pow(-2*t + 2, 2) / 2;
const lerp = (a, b, t) => a + (b - a) * t;

function slot(id) {
  // centroid position and rotation of each piece on the fabric marker
  const fw = Math.min(vb.w * .86, 300), fx = C[0] - fw / 2, fy = 30, fh = 176;
  const i = ORDER.indexOf(id);
  const xs = [.09, .26, .45, .63, .80, .93];
  return {x: fx + xs[i] * fw, y: fy + fh * .5 + (i > 3 ? -40 : 0), r: GRAIN[id], fab: {x: fx, y: fy, w: fw, h: fh}};
}

// transform of a piece as a function of scroll progress
function pose(id, p, jit, i) {
  const c = P[id].c;
  let dx = 0, dy = 0, r = 0;
  const e1 = Math.pow(clamp((p - .06) / .46), 1.9);            // 02 displaced
  const [fx, fy, fr] = DRIFT[id];
  const drift = {dx: fx * vb.w * e1, dy: fy * vb.h * e1, r: fr * e1};
  const e2 = ease(clamp((p - .56) / .22));                      // 03 marker
  const s = slot(id);
  const mk = {dx: s.x - c[0], dy: s.y - c[1], r: s.r};
  dx = lerp(drift.dx, mk.dx, e2); dy = lerp(drift.dy, mk.dy, e2); r = lerp(drift.r, mk.r, e2);
  if (id === 'A2' || id === 'B2') {                             // 04 joint: the crossing goes back and closes
    const e3 = ease(clamp((p - .82) / .14));
    dx = lerp(dx, 0, e3); dy = lerp(dy, 0, e3); r = lerp(r, 0, e3);
  }
  const k = (1 - e2) * clamp(p / .06);                          // the viewer's speed shakes the pieces before the marker
  dx += jit * k * Math.sin(i * 2.1 + 1) ; dy += jit * k * Math.cos(i * 1.7);
  return {dx, dy, r, c};
}
const apply = (q, x, y) => {
  const a = q.r * Math.PI / 180, cs = Math.cos(a), sn = Math.sin(a);
  const ux = x - q.c[0], uy = y - q.c[1];
  return [q.c[0] + q.dx + ux * cs - uy * sn, q.c[1] + q.dy + ux * sn + uy * cs];
};

const seq = document.querySelector('.seq');
const railv = document.getElementById('railv'), delta = document.getElementById('delta');
const phs = [0,1,2,3].map(i => document.getElementById('ph' + i));
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
let lastY = scrollY, vel = 0, forced = null;
const m = /^#p(\d{1,3})$/.exec(location.hash); if (m) forced = +m[1] / 100;

function progress() {
  if (forced !== null) return forced;
  const r = seq.getBoundingClientRect(); const span = r.height - innerHeight;
  return clamp(-r.top / Math.max(1, span));
}
function frame() {
  const y = scrollY; vel = lerp(vel, Math.abs(y - lastY), .18); lastY = y;
  const jit = reduce ? 0 : Math.min(vel * .09, 22);
  const p = progress();
  const poses = {};
  let maxd = 0;
  IDS.forEach((id, i) => {
    const q = pose(id, p, jit, i); poses[id] = q;
    nodes[id].g.setAttribute('transform', `translate(${q.dx + q.c[0]} ${q.dy + q.c[1]}) rotate(${q.r}) translate(${-q.c[0]} ${-q.c[1]})`);
    maxd = Math.max(maxd, Math.hypot(q.dx, q.dy));
    const b = P[id].b; nodes[id].t.setAttribute('x', b[2] + 2); nodes[id].t.setAttribute('y', b[1] + 4);
    nodes[id].t.setAttribute('opacity', clamp((p - .1) / .08) * ((id === 'A2' || id === 'B2') ? 1 - clamp((p - .8) / .04) : 1));
  });
  // seams: the same point on two pieces, stitched across the gap
  const eJ = clamp((p - .84) / .1);
  D.seams.forEach(([a, b, x, yy], k) => {
    const pa = apply(poses[a], x, yy), pb = apply(poses[b], x, yy);
    const L = seams[k]; L.setAttribute('x1', pa[0]); L.setAttribute('y1', pa[1]); L.setAttribute('x2', pb[0]); L.setAttribute('y2', pb[1]);
    L.setAttribute('stroke', eJ > 0 ? NIBI : INK); L.setAttribute('opacity', clamp((p - .08) / .06) * (1 - .55 * eJ));
  });
  const ca = apply(poses.A2, C[0], C[1]), cb = apply(poses.B2, C[0], C[1]);
  crossLine.setAttribute('x1', ca[0]); crossLine.setAttribute('y1', ca[1]); crossLine.setAttribute('x2', cb[0]); crossLine.setAttribute('y2', cb[1]);
  crossLine.setAttribute('opacity', clamp((p - .08) / .06));
  // fabric
  const s = slot('A1'), f = s.fab, eF = ease(clamp((p - .56) / .2));
  fab.setAttribute('x', f.x); fab.setAttribute('y', f.y); fab.setAttribute('width', f.w); fab.setAttribute('height', f.h);
  gFab.setAttribute('opacity', eF * (1 - .5 * eJ));
  fabTxt.setAttribute('x', f.x + 2); fabTxt.setAttribute('y', f.y - 2);
  grain.forEach((g, i) => { const gx = f.x + f.w * (.05 + i * .18), gy = f.y + f.h - 26; g.setAttribute('d', `M${gx} ${gy} v20 M${gx-1.6} ${gy+3} L${gx} ${gy} L${gx+1.6} ${gy+3} M${gx-1.6} ${gy+17} L${gx} ${gy+20} L${gx+1.6} ${gy+17}`); });
  // the rest of the pieces recede once the joint closes
  IDS.forEach(id => { if (id !== 'A2' && id !== 'B2') nodes[id].path.setAttribute('fill', eJ > 0 ? mix(INK, NIBI, eJ) : INK); });
  ring.setAttribute('cx', C[0]); ring.setAttribute('cy', C[1]); ring.setAttribute('opacity', eJ);
  // readouts
  railv.style.height = (p * 100) + '%';
  delta.textContent = maxd.toFixed(1) + ' mm';
  const ph = p < .06 ? 0 : p < .56 ? 1 : p < .82 ? 2 : 3;
  phs.forEach((e, i) => e.classList.toggle('on', i === ph));
  requestAnimationFrame(frame);
}
function mix(a, b, t) {
  const h = s => [1, 3, 5].map(i => parseInt(s.slice(i, i + 2), 16));
  const x = h(a), y = h(b); return 'rgb(' + x.map((v, i) => Math.round(v + (y[i] - v) * t)).join(',') + ')';
}
addEventListener('resize', layout); layout(); requestAnimationFrame(frame);
addEventListener('hashchange', () => { const m = /^#p(\d{1,3})$/.exec(location.hash); forced = m ? +m[1] / 100 : null; });


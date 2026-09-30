// --- Collection: quiet frames. A rectangle with one 45° cut corner; the displacement is drawn in ink and turns 深青 on touch.
const FLATS = {
  shirt: 'M80 30 L60 38 L30 55 L14 150 L32 153 L50 85 L55 225 L145 225 L150 85 L168 153 L186 150 L170 55 L140 38 L120 30 M80 30 L100 50 L120 30 M60 38 L100 50 L140 38 M16 140 L33 143 M167 143 L184 140',
  tee: 'M78 34 L58 40 L28 62 L40 88 L56 80 L56 222 L144 222 L144 80 L160 88 L172 62 L142 40 L122 34 Q100 50 78 34 Z',
  trousers: 'M50 30 L150 30 L150 44 L50 44 Z M50 44 L42 225 L92 225 L100 95 L108 225 L158 225 L150 44',
  coat: 'M76 26 L56 34 L34 60 L22 205 L40 207 L52 100 L52 232 L148 232 L148 100 L160 207 L178 205 L166 60 L144 34 L124 26 M76 26 L90 70 L100 110 L110 70 L124 26 M100 110 L100 232'
};
const ITEMS = [
  {co:[115,100, 170,45, 196,"+15 mm"], no:'01', name:'Shirt', flat:'shirt', base:'', dx:'M115 50 L115 225', spec:['Placket', '+15 mm'], buttons:115},
  {co:[33,145, 8,170, 48,"−8 mm"], no:'02', name:'Shirt', flat:'shirt', base:'M100 50 L100 225', dx:'M15 142 L33 145', spec:['Left sleeve', '−8 mm'], buttons:100, trimLeft:true},
  {co:[108,46, 140,14, 194,"+8 mm"], no:'03', name:'T-shirt', flat:'tee', base:'', dx:'M90 37 Q108 55 126 37', spec:['Neck rib', '+8 mm']},
  {co:[70,190, 40,220, 6,"fwd 20 mm"], no:'04', name:'T-shirt', flat:'tee', base:'M82 36 Q100 54 118 36', dx:'M70 92 L70 222', spec:['Side seam', 'forward 20 mm']},
  {co:[118,70, 160,28, 194,"+14 mm"], no:'05', name:'Trousers', flat:'trousers', base:'', dx:'M114 44 Q120 70 114 95', spec:['Fly', '+14 mm']},
  {co:[133,213, 113,233, 166,"−12 mm"], no:'06', name:'Trousers', flat:'trousers', base:'M100 44 Q106 70 100 95', dx:'M108 213 L158 213', spec:['Right hem', '−12 mm'], shortRight:true},
  {co:[112,164, 84,192, 56,"reversed"], no:'07', name:'Coat', flat:'coat', base:'M62 170 L88 170', dx:'M112 170 L138 170 L138 158 L112 158 Z', spec:['Right pocket', 'reversed']},
  {co:[119,41, 145,15, 194,"−6 mm"], no:'08', name:'Coat', flat:'coat', base:'M62 170 L88 170 M112 170 L138 170', dx:'M124 26 L114 56', spec:['Right lapel', '−6 mm']}
];
(function plates(){
  const box = document.getElementById('plates');
  const cols = () => innerWidth <= 520 ? 1 : innerWidth <= 1100 ? 2 : 4;
  const render = () => {
    box.textContent = '';
    const n = cols();
    ITEMS.forEach((it, i) => {
      if (i % n === 0) { const r = document.createElement('div'); r.className = 'rowrail'; r.setAttribute('aria-hidden', 'true'); box.appendChild(r); }
      const a = document.createElement('article'); a.className = 'plate'; a.tabIndex = 0;
      a.setAttribute('aria-label', `No.${it.no} ${it.name}. ${it.spec[0]} ${it.spec[1]}`);
      const fig = document.createElement('div'); fig.className = 'fig';
      const s = el('svg', {viewBox: '0 0 200 266.67', preserveAspectRatio: 'none', 'aria-hidden': 'true'});
      const g = el('g', {transform: 'translate(0 8)'}, s);
      let d = FLATS[it.flat];
      if (it.trimLeft) d = d.replace('L14 150 L32 153', 'L15 142 L33 145').replace('M16 140 L33 143', '');
      if (it.shortRight) d = d.replace('L108 225 L158 225', 'L108 213 L158 213');
      el('path', {class: 'flat', d}, g);
      if (it.base) el('path', {class: 'flat', d: it.base}, g);
      if (it.buttons) for (let k = 0; k < 6; k++) el('circle', {class: 'flat', cx: it.buttons + 5, cy: 64 + k * 28, r: 1.8}, g);
      el('path', {class: 'dx', d: it.dx}, g);
      // one callout per garment, at 45° as on a tech pack, always rising to the right like the hairline of the symbol
      const [ax, ay, ex, ey, tx, lab] = it.co;
      el('circle', {class: 'cod', cx: ax, cy: ay, r: 1.6}, g);
      el('path', {class: 'co', d: `M${ax} ${ay} L${ex} ${ey} L${tx} ${ey}`}, g);
      const t = el('text', {class: 'cot', x: tx > ex ? tx : tx, y: ey - 3, 'text-anchor': tx > ex ? 'end' : 'start'}, g); t.textContent = lab;
      fig.appendChild(s); a.appendChild(fig);
      a.insertAdjacentHTML('beforeend', `<h3><span class="lb">No.${it.no}</span>${it.name}</h3>
        <dl class="spec lb"><dt class="dxrow">${it.spec[0]}</dt><dd class="dxrow">${it.spec[1]}</dd><dt>Fabric</dt><dd>[素材]</dd><dt>Size</dt><dd>1 / 2 / 3</dd><dt>Price</dt><dd>[価格]</dd></dl>`);
      box.appendChild(a);
    });
  };
  let last = cols(); render();
  addEventListener('resize', () => { const n = cols(); if (n !== last) { last = n; render(); } });
})();


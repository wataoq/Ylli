from bx.pcommon import *
from bx.glyph import *
# SHIFT — the mark at full sheet scale, sliced into bands that drift further the lower they go.
m=markgeo(); s=1880/205.31
m=sscale(m,s,s,origin=(0,0)); m=translate(m,500-57.31*s/2+30,-250)
edges=[-300,120,260,330,470,560,700,790,930,1010,1150,1230,1414+300]
shifts=[0,0,14,-26,52,-84,130,-190,250,-330,410,-520]
bands=[translate(b,dx,0) for b,dx in zip(slices(m,edges),shifts)]
M=unary_union(bands)
# the word, sliced with the same edges and pushed the other way
ws,wx=word('SHIFT',900,62,-10,560)
W=unary_union(ws); W=translate(W,(1000-wx)/2,540)
wb=[translate(b,-dx*0.6,0) for b,dx in zip(slices(W,edges),shifts)]
W=unary_union(wb)
geo=M.symmetric_difference(W)
svg_=f'<svg class="a" style="left: 0; top: 0; width: 1000px; height: 1414px" viewBox="0 0 1000 1414" aria-hidden="true">{svgpath(geo,INK,"evenodd")}'
for e,dx in zip(edges[1:-1],shifts[1:]):
    svg_+=f'<line x1="0" x2="1000" y1="{e}" y2="{e}" stroke="{INK}" stroke-width="0.6"/>'
svg_+='</svg>'
b=svg_
for e,dx in zip(edges[1:-1],shifts[1:]):
    b+=T(f'{dx:+d}',944,e-15,10,500,100,PAPER,1,'text-align: right; width: 40px; left: 916px; mix-blend-mode: difference')
b+=T('SHIFT',40,40,13,700,100)+T('How far can a form move<br>before it stops being itself?',40,62,13,400,100,INK,1.35)
b+=T('Ylli — Collection 01 — Launch',600,1352,11,500,100,INK,1.4)
b+=T('01 / 05',905,1384,10,500,100,GREY)
poster('PZ01Shift.dc.html','Ylli Poster Z01 — Shift',b,bt='Z01 — SHIFT（ロゴ：全面）')

from bx.pcommon import *
from bx.glyph import *
import math
# SHIFT v2 — bands in an irregular rhythm (thin / thick / thin-thin / thick), shifts that oscillate
# and accelerate, some bands squeezed; a hairline ghost keeps the position it came from.
m0=markgeo(); s=1900/205.31
M0=translate(sscale(m0,s,s,origin=(0,0)),500-57.31*s/2+26,-236)
ws,wx=word('SHIFT',900,62,-10,600)
W0=unary_union(ws); W0=translate(W0,(1000-wx)/2,560)
# rhythm of band heights (px)
H=[118,6,30,6,70,14,96,4,22,48,8,120,10,36,6,64,92,12,30,140,8,54,18,160,40]
edges=[-300]; y=118
for h in H[1:]: edges.append(y); y+=h
edges=[-300]+[118]+[e for e in edges[2:]]+[1414+300]
edges=sorted(set(edges))
n=len(edges)-1
shifts=[];sq=[]
for i in range(n):
    t=i/(n-1)
    amp=4+620*t**2.2
    sgn=1 if (i*7)%3!=0 else -1
    shifts.append(0 if i<2 else sgn*amp*(0.55+0.45*math.sin(i*1.9))*(0.35 if i<12 else 1))
    sq.append(1.0 if i<12 else [1,0.46,1.7,1,0.26,1.3,0.8][i%7])   # below the word, bands are squeezed / stretched
def band_apply(G,k=1.0):
    out=[]
    for (a,b),dx,q in zip(zip(edges,edges[1:]),shifts,sq):
        piece=G.intersection(box(-2000,a,3000,b))
        if piece.is_empty: continue
        cx=500
        piece=sscale(piece,q,1,origin=(cx,0))
        out.append(translate(piece,dx*k,0))
    return unary_union(out)
M=band_apply(M0,1.0)
W=band_apply(W0,-0.55)
G=M.symmetric_difference(W)
defs=''
svg_=f'<svg class="a" style="left: 0; top: 0; width: 1000px; height: 1414px" viewBox="0 0 1000 1414" aria-hidden="true">'
# ghost: the undisturbed outline
ghost=M0.symmetric_difference(W0)
svg_+=f'<path d="{path(ghost)}" fill="none" stroke="{INK}" stroke-width="0.7" fill-rule="evenodd"/>'
svg_+=svgpath(G,INK,'evenodd')
svg_+='</svg>'
b=svg_
# band annotations: index + shift, only on a few rhythmic bands
for i,((a,bb),dx) in enumerate(zip(zip(edges,edges[1:]),shifts)):
    if bb-a<40 or a<100 or a>1360: continue
    b+=f'<div class="a" style="left: 900px; top: {a:.0f}px; width: 100px; height: 1px; background: {PAPER}; mix-blend-mode: difference"></div>'
    b+=T(f'{i:02d}　{dx:+.0f}',900,a+3,9,500,100,PAPER,1,'mix-blend-mode: difference; width: 70px; text-align: right')
DF='mix-blend-mode: difference'
b+=T('SHIFT',40,34,13,800,100,PAPER,1,DF)+T('How far can a form move<br>before it stops being itself?',40,54,13,400,100,PAPER,1.35,DF)
b+=T('01',760,34,13,800,100,PAPER,1,DF)+T('Ylli — Collection 01<br>Launch',800,34,13,400,100,PAPER,1.35,DF)
b+=T('Form, displaced. — The ghost line marks where it was.',560,1382,10,400,100,PAPER,1,'mix-blend-mode: difference')
poster('PZ01bShift.dc.html','Ylli Poster Z01b — Shift',b,bt='Z01b — SHIFT（ブラッシュアップ）')

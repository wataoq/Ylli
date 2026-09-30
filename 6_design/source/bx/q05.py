from bx.pcommon import *
from bx.glyph import *
import math
# UNRESOLVED — the letters are pulled out of shape; the more they bend, the less they settle.
lines=[('UNRE',0),('SOL',1),('VED.',2)]
geo=[]
y=40
for s,i in lines:
    ws,wx=word(s,900,62 if i!=1 else 125,-10,1000)
    W=unary_union(ws); x0,y0,x1,y1=W.bounds
    kx=940/(x1-x0); ky=[430,300,470][i]/(y1-y0)
    W=translate(sscale(W,kx,ky,origin=(0,0)),0,0); a0,b0,a1,b1=W.bounds
    W=translate(W,30-a0,y-b0)
    amp=[6,28,70][i]; lam=[90,60,40][i]
    def fn(px,py,amp=amp,lam=lam,y=y):
        t=(py-y)/lam
        return (px+amp*math.sin(t)*(0.3+0.7*(px/1000)), py+ amp*0.25*math.sin(px/70))
    geo.append(warp(W,fn,3))
    y+=[430,300,470][i]+36
G=unary_union(geo)
m=markgeo(); s=2000/205.31; m=translate(sscale(m,s,s,origin=(0,0)),520,-420)
G=G.symmetric_difference(m)
b=f'<svg class="a" style="left: 0; top: 0; width: 1000px; height: 1414px" viewBox="0 0 1000 1414" aria-hidden="true">{svgpath(G,INK,"evenodd")}</svg>'
b+=T('UNRESOLVED',40,1320,13,700,100,PAPER,1,'mix-blend-mode: difference')+T('It bends before it settles. It does not settle.',40,1342,13,400,100,PAPER,1,'mix-blend-mode: difference')
b+=T('Ylli — Collection 01 — Launch',600,1320,11,500,100,PAPER,1.4,'mix-blend-mode: difference')
b+=T('05 / 05',905,1384,10,500,100,PAPER,1,'mix-blend-mode: difference')
poster('PZ05Unresolved.dc.html','Ylli Poster Z05 — Unresolved',b,bt='Z05 — UNRESOLVED（ロゴ：全面・反転）')

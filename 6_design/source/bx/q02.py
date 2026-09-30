from bx.pcommon import *
from bx.glyph import *
# APART — each letter is cut on a grid; pieces drift apart more with every letter.
ws,wx=word('APART',900,62,0,560)
k=(900)/wx
geo=[];labels=[]
dists=[0,8,30,90,230]
for i,(g,d) in enumerate(zip(ws,dists)):
    gx0,gy0,gx1,gy1=g.bounds; hh=gy1-gy0; kk=232/hh
    g=sscale(g,kk,kk,origin=(0,0)); gx0,gy0,gx1,gy1=g.bounds
    g=translate(g,450-(gx0+gx1)/2,170+i*252-gy0)
    x0,y0,x1,y1=g.bounds; cx,cy=(x0+x1)/2,(y0+y1)/2
    nx,ny=3,5
    for a in range(nx):
        for c in range(ny):
            cell=g.intersection(box(x0+(x1-x0)*a/nx,y0+(y1-y0)*c/ny,x0+(x1-x0)*(a+1)/nx,y0+(y1-y0)*(c+1)/ny))
            if cell.is_empty: continue
            px,py=cell.centroid.x,cell.centroid.y
            vx,vy=(px-cx)/(x1-x0),(py-cy)/(y1-y0)
            geo.append(translate(cell,vx*d*3.0,vy*d*0.55))
    labels.append(((y0+y1)/2,d))
G=unary_union(geo)
# the logo: stretched to a single tall hairline figure, running the full height at the left edge
L=nibmark(2400,1900); lh=1414+30; s=lh/L.bounds[3]
L=translate(sscale(L,s,s,origin=(0,0)),940,-12)
svg_=f'<svg class="a" style="left: 0; top: 0; width: 1000px; height: 1414px" viewBox="0 0 1000 1414" aria-hidden="true">{svgpath(G,INK)}{svgpath(L,INK)}'
for y,d in labels:
    svg_+=f'<line x1="40" x2="96" y1="{y:.1f}" y2="{y:.1f}" stroke="{INK}" stroke-width="0.8"/>'
svg_+='</svg>'
b=svg_
for y,d in labels: b+=T(f'd = {d}',40,y+6,11,500,100)
b+=T('APART',40,40,13,700,100)+T('Pulled apart, is it still a letter?<br>At what distance do you stop reading?',40,62,13,400,100,INK,1.35)
b+=T('Ylli — Collection 01 — Launch',640,1346,11,500,100,INK,1.35)
b+=T('02 / 05',860,1384,10,500,100,GREY)
poster('PZ02Apart.dc.html','Ylli Poster Z02 — Apart',b,bt='Z02 — APART（ロゴ：極細の縦長）')

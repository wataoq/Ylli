from bx.pcommon import *
from bx.glyph import *
# TOO CLOSE — letters pushed into each other; wherever two forms overlap, both disappear (even-odd).
def line(s,size,y,overlaps,wght=900,wdth=62,x0=0):
    out=[];x=x0
    for i,ch in enumerate(s):
        g,a=glyph(ch,wght,wdth); k=size/1000
        g=translate(sscale(g,k,k,origin=(0,0)),x,y); out.append(g)
        x+=a*k-(overlaps[i] if i<len(overlaps) else 0)
    return out,x
parts=[]
too,_=line('TOO',640,560,[40,160],x0=10)
close,_=line('CLOSE',640,1240,[120,190,250,320],x0=-20)
parts=too+close
# the logo, hidden: it only exists where it cancels the letters
m=markgeo(); s=1300/205.31; m=translate(sscale(m,s,s,origin=(0,0)),620,40)
parts.append(m)
# even-odd accumulate
G=Polygon()
for p in parts: G=G.symmetric_difference(p)
b=f'<svg class="a" style="left: 0; top: 0; width: 1000px; height: 1414px" viewBox="0 0 1000 1414" aria-hidden="true">{svgpath(G,INK,"evenodd")}</svg>'
b+=T('TOO CLOSE',40,40,13,700,100,PAPER,1,'mix-blend-mode: difference')+T('Pushed together, two forms become a third.<br>Neither of them is still there.',40,62,13,400,100,PAPER,1.35,'mix-blend-mode: difference')
b+=T('Ylli — Collection 01 — Launch',40,1372,11,500,100,PAPER,1,'mix-blend-mode: difference')
b+=T('03 / 05',905,1372,10,500,100,PAPER,1,'mix-blend-mode: difference')
poster('PZ03Close.dc.html','Ylli Poster Z03 — Too close',b,bt='Z03 — TOO CLOSE（ロゴ：図形に溶かす）')

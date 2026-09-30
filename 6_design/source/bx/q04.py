from bx.pcommon import *
from bx.glyph import *
from shapely.geometry import MultiPolygon
# FORM — the outline becomes geometry in four steps. Where does the letter end?
def strips(g,n):
    x0,y0,x1,y1=g.bounds; out=[]
    for i in range(n):
        c=g.intersection(box(x0-5,y0+(y1-y0)*i/n,x1+5,y0+(y1-y0)*(i+1)/n))
        if not c.is_empty:
            for p in getattr(c,'geoms',[c]):
                if p.area>1: out.append(box(*p.bounds))
    return unary_union(out)
glyphs=[glyph(c,900,62)[0] for c in 'FORM']
m=markgeo(); glyphs.append(sscale(m,688/205.31,688/205.31,origin=(0,0)))
rowh=250; top=150
stages=[lambda g:g, lambda g:strips(g,7), lambda g:g.convex_hull, lambda g:box(*g.bounds)]
names=['outline','strip','hull','box']
geo=[]; RH=[330,150,300,460]; OFF=[0,-70,110,-40]; rows_y=[]
y=top
for r,fn in enumerate(stages):
    x=40+OFF[r]; rows_y.append(y)
    for i,g in enumerate(glyphs):
        x0,y0,x1,y1=g.bounds; k=212/(y1-y0); ky=RH[r]/(y1-y0)
        gg=sscale(g,k,ky,origin=(0,0)); a0,b0,a1,b1=gg.bounds
        gg=translate(gg,x-a0,y-b0)
        geo.append(fn(gg))
        x+= (a1-a0)+ (22 if i<3 else 70)
    y+=RH[r]+22
G=unary_union(geo)
b=f'<svg class="a" style="left: 0; top: 0; width: 1000px; height: 1414px" viewBox="0 0 1000 1414" aria-hidden="true">{svgpath(G,INK)}</svg>'
for r,nm in enumerate(names):
    b+=T(f'0{r+1}　{nm}',905,rows_y[r],11,500,100,PAPER,1,'mix-blend-mode: difference')
b+=T('FORM',40,40,13,700,100)+T('Trace the outline, then simplify it.<br>The letter leaves before the shape does.',40,62,13,400,100,INK,1.35)
b+=T('Ylli — Collection 01 — Launch',640,40,11,500,100,INK,1.4)
b+=T('04 / 05',905,62,10,500,100,GREY)
poster('PZ04Form.dc.html','Ylli Poster Z04 — Form',b,bt='Z04 — FORM（ロゴ：図形に紛れる）')

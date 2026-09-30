import sys; sys.path.insert(0,'.')
from bx.pcommon import *
from bx.glyph import *
from bx.proj import *
import json, math, random
SW,SH=1080,1920
DF='mix-blend-mode: difference'
CROSS=(28.657,46.657)
M=markgeo()
def wrap(inner): return f'<svg class="a" style="left: 0; top: 0; width: {SW}px; height: {SH}px" viewBox="0 0 {SW} {SH}" aria-hidden="true">{inner}</svg>'
FRAME=box(0,0,SW,SH)
def place(s,x,y): return translate(sscale(M,s,s,origin=(0,0)),x,y)
def cpt(s,x,y): return (x+CROSS[0]*s,y+CROSS[1]*s)
def ring(x,y,r,w=1.0): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" stroke="{PAPER}" stroke-width="{w}" style="{DF}"/>'
out=[]
# 01 — PROJECT: a fan of wedges from the vanishing point, xor'd with the projected mark (op-art perspective)
s=12.5; m=place(s,SW/2-57.31*s/2,-40)
H=rect_to(m,[(250,140),(830,140),(1300,2050),(-220,2050)])
g=happly(m,H)
vp=(540,-1400)
wed=[]
n=46
for i in range(n):
    a0=math.radians(90-38+76*i/n); a1=math.radians(90-38+76*(i+0.5)/n)
    R=5000
    wed.append(Polygon([vp,(vp[0]+R*math.cos(a0),vp[1]+R*math.sin(a0)),(vp[0]+R*math.cos(a1),vp[1]+R*math.sin(a1))]))
fan=unary_union(wed).intersection(box(0,0,SW,SH))
G=g.symmetric_difference(fan)
x0,y0,_,_=m.bounds; cx,cy=hp(H,*cpt(s,x0,y0)) if False else hp(H,x0+CROSS[0]*s,y0+CROSS[1]*s)
out.append(('XSTORY01',wrap(svgpath(G,INK,'evenodd')+ring(cx,cy,34,1.4))))
# 02 — SIMULTANEITY: seven viewpoints at once
random.seed(7)
gs=[];cs=[]
for i in range(7):
    s=random.uniform(3.6,7.8); x=random.uniform(-120,760); y=random.uniform(-200,900)
    m=place(s,x,y); X0,Y0,X1,Y1=m.bounds; w=X1-X0; h=Y1-Y0
    j=lambda k: random.uniform(-k,k)
    q=[(X0+j(220),Y0+j(160)),(X1+j(220),Y0+j(160)),(X1+j(320),Y1+j(260)+200),(X0+j(320),Y1+j(260)+200)]
    H=rect_to(m,q); gs.append(happly(m,H)); cs.append(hp(H,X0+CROSS[0]*s,Y0+CROSS[1]*s))
G=xor_all(gs).intersection(FRAME.buffer(200))
inner=svgpath(G,INK,'evenodd')
pts=' '.join(f'{x:.1f},{y:.1f}' for x,y in cs+[cs[0]])
inner+=f'<polyline points="{pts}" fill="none" stroke="{PAPER}" stroke-width="0.8" style="{DF}"/>'
for x,y in cs: inner+=ring(x,y,16)
out.append(('XSTORY02',wrap(inner)))
# 03 — JOIN: a table of joinings. rows = the other form, columns = the rule
s=1.55
forms=[lambda cx,cy: Point(cx-20,cy+10).buffer(62,48),
       lambda cx,cy: box(cx-120,cy-16,cx+120,cy+16),
       lambda cx,cy: Polygon([(cx-10,cy-120),(cx+130,cy+120),(cx-130,cy+120)]),
       lambda cx,cy: box(cx+4,cy-200,cx+60,cy+200),
       lambda cx,cy: Point(cx+40,cy-60).buffer(90,48).difference(Point(cx+40,cy-60).buffer(50,48)),
       lambda cx,cy: rotate(box(cx-150,cy-12,cx+150,cy+12),-45,origin=(cx,cy))]
ops=[lambda a,b:a.union(b), lambda a,b:a.symmetric_difference(b), lambda a,b:a.difference(b), lambda a,b:b.difference(a)]
cw,ch=SW/4,SH/6
geo=[]
for r,fm in enumerate(forms):
    for c,op in enumerate(ops):
        cx,cy=c*cw+cw/2,r*ch+ch/2
        m=place(s,cx-CROSS[0]*s,cy-CROSS[1]*s-40)
        cell=op(m,fm(cx,cy)).intersection(box(c*cw+4,r*ch+4,(c+1)*cw-4,(r+1)*ch-4))
        geo.append(cell)
inner=svgpath(unary_union(geo),INK)
for c in range(1,4): inner+=f'<line x1="{c*cw:.1f}" y1="0" x2="{c*cw:.1f}" y2="{SH}" stroke="{INK}" stroke-width="0.6"/>'
for r in range(1,6): inner+=f'<line x1="0" y1="{r*ch:.1f}" x2="{SW}" y2="{r*ch:.1f}" stroke="{INK}" stroke-width="0.6"/>'
out.append(('XSTORY03',wrap(inner)))
# 04 — MULTIPLY: a spiralling projection, iterated 26 times, xor'd
s=10.5; m=place(s,SW/2-57.31*s/2,-120)
F=(560,1040); th=math.radians(11); k=0.86
def Hspiral():
    c,sn=math.cos(th)*k,math.sin(th)*k
    T1=np.array([[1,0,-F[0]],[0,1,-F[1]],[0,0,1.0]]); R=np.array([[c,-sn,0],[sn,c,0],[0.00005,-0.00003,1]]); T2=np.array([[1,0,F[0]],[0,1,F[1]],[0,0,1.0]])
    return T2@R@T1
Hs=Hspiral()
gs=[];g=m
for i in range(26):
    gs.append(g); g=happly(g,Hs,3)
G=xor_all(gs).intersection(FRAME.buffer(100))
out.append(('XSTORY04',wrap(svgpath(G,INK,'evenodd'))))
# 05 — VANISH: chronophotograph of one turn — 28 exposures sweeping across the frame
L=nibmark(640,480); Lh=L.bounds[3]; s=(SH+40)/Lh
geo=[]
N=28
for i in range(N):
    t=i/(N-1); th=t*math.pi/2*0.995
    c=math.cos(th); w=57.31*s
    x=40+t*(SW-160)
    m=translate(sscale(L,s,s,origin=(0,0)),0,-20); X0,Y0,X1,Y1=m.bounds
    ww=max(1.0,w*c); tilt=0.12*math.sin(th)*(Y1-Y0)
    H=rect_to(m,[(x,Y0),(x+ww,Y0+tilt),(x+ww,Y1-tilt),(x,Y1)])
    geo.append(happly(m,H,8))
out.append(('XSTORY05',wrap(svgpath(xor_all(geo),INK,'evenodd'))))
# 06 — WHAT REMAINS: only the crossings — every incidence point of the series, nothing else
random.seed(3)
inner=''
s=3.2
pts=[(540,960,1.0)]+[(random.uniform(80,1000),random.uniform(120,1800),random.uniform(0.18,0.55)) for _ in range(23)]
for x,y,k in pts:
    sc=s*k*(3.0 if k==1.0 else 1)
    m=place(sc,0,0); X0,Y0,_,_=m.bounds; cx,cy=X0+CROSS[0]*sc,Y0+CROSS[1]*sc
    r=70*k*(1.6 if k==1.0 else 1)
    crop=translate(m.intersection(Point(cx,cy).buffer(r,48)),x-cx,y-cy)
    inner+=svgpath(crop,INK)+f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" stroke="{INK}" stroke-width="0.7"/>'
out.append(('XSTORY06',wrap(inner)))
for n,body in out: poster(f'{n}.dc.html',f'Ylli Story {n}',body,w=SW,h=SH)
print('ok')

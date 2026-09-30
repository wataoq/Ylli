import sys; sys.path.insert(0,'.')
from bx.pcommon import *
from bx.glyph import *
from bx.proj import *
import json
SW,SH=1080,1920
DF='mix-blend-mode: difference'
P2=json.load(open('nib/paths.json'))
CROSS=(28.657,46.657)   # the crossing, in mark coordinates
def svgwrap(inner): return f'<svg class="a" style="left: 0; top: 0; width: {SW}px; height: {SH}px" viewBox="0 0 {SW} {SH}" aria-hidden="true">{inner}</svg>'
def hair(x1,y1,x2,y2,w=0.8,c=INK): return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}"/>'
def marker(x,y,label=None,r=30):
    s=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="none" stroke="{PAPER}" stroke-width="1.2" style="{DF}"/>'
    s+=f'<line x1="{x-r-14:.1f}" y1="{y:.1f}" x2="{x+r+14:.1f}" y2="{y:.1f}" stroke="{PAPER}" stroke-width="0.8" style="{DF}"/>'
    return s
def label(x,y,t,sz=13,wt=500): return ''
def _label(x,y,t,sz=13,wt=500): return T(t,x,y,sz,wt,100,PAPER,1.2,DF+'; white-space: nowrap')
def head(i,title):
    return ''
    return (T(f'{i:02d} / 06',56,262,15,800,100,PAPER,1,DF)+T(title,140,262,15,800,100,PAPER,1,DF)
            +T('Ylli — Collection 01',760,262,15,400,100,PAPER,1,DF+'; width: 264px; text-align: right'))
def copy(big,small,y=1430,sz=76):
    return ''
    return (T(big,56,y,sz,900,62,PAPER,0.9,DF+'; white-space: nowrap; letter-spacing: -0.005em')
            +T(small,56,1640,15,400,100,PAPER,1.35,DF))
M=markgeo()
frames=[]
# ---------- 01 BEFORE YOU SEE IT — one projection; rays to the vanishing point
s=12.5; m=translate(sscale(M,s,s,origin=(0,0)),SW/2-57.31*s/2,-40)
quad=[(250,140),(830,140),(1300,2050),(-220,2050)]
H=rect_to(m,quad); g=happly(m,H)
x0,y0,x1,y1=m.bounds
vp=hp(H,SW/2,-1e7)  # image of the vertical direction at infinity
inner=''
for t in [i/12 for i in range(-3,16)]:
    bx_=x0+(x1-x0)*t; a=hp(H,bx_,y0); b=hp(H,bx_,y1+400)
    inner+=hair(a[0],a[1],b[0],b[1],0.9)
inner+=svgpath(g,INK)
cx,cy=hp(H,x0+CROSS[0]*s,y0+CROSS[1]*s)
inner+=marker(cx,cy)
b=svgwrap(inner)+head(1,'PROJECT')+label(cx+50,cy-8,'incidence — the only thing that survives',12)
b+=copy('BEFORE YOU SEE IT,<br>YOU HAVE ALREADY MOVED.','To place a form is to imagine the movement that would reach it.<br>— after Henri Poincaré　／　Tap: the movement is yours, not the form’s.')
frames.append(('PSTORY01',b))
# ---------- 02 THREE VIEWPOINTS AT ONCE — cubist simultaneity: three projections, xor
s=6.6; m=translate(sscale(M,s,s,origin=(0,0)),SW/2-57.31*s/2,120)
x0,y0,x1,y1=m.bounds; w=x1-x0; h=y1-y0
quads=[[(x0-260,y0+60),(x1-120,y0-90),(x1-60,y1+260),(x0-340,y1+40)],
       [(x0+40,y0+220),(x1+300,y0+300),(x1+180,y1+120),(x0+120,y1-40)],
       [(x0-40,y0-40),(x1+40,y0-40),(x1+160,y1+420),(x0-160,y1+420)]]
gs=[];marks=[]
for q in quads:
    H=rect_to(m,q); gs.append(happly(m,H)); marks.append(hp(H,x0+CROSS[0]*s,y0+CROSS[1]*s))
inner=svgpath(xor_all(gs),INK,'evenodd')
for (ax,ay),(bx2,by2) in zip(marks,marks[1:]+marks[:1]): inner+=f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx2:.1f}" y2="{by2:.1f}" stroke="{PAPER}" stroke-width="0.8" style="{DF}"/>'
for x,y in marks: inner+=marker(x,y,r=22)
b=svgwrap(inner)+head(2,'SIMULTANEITY')
b+=copy('THREE VIEWPOINTS,<br>AT ONCE.','None of them is the wrong one. The three circles are the same crossing.')
frames.append(('PSTORY02',b))
# ---------- 03 JOIN — insisted upon (union) / erased (xor)
def comp(dy):
    s=3.3; m=translate(sscale(M,s,s,origin=(0,0)),SW/2-57.31*s/2+60,dy)
    x0,y0,x1,y1=m.bounds
    H=rect_to(m,[(x0-40,y0),(x1+160,y0+40),(x1+80,y1),(x0-120,y1-50)]); mm=happly(m,H)
    disc=Point(360,dy+230).buffer(200,64)
    bar=box(-20,dy+330,1100,dy+400)
    wedge=Polygon([(700,dy+30),(1100,dy+10),(1100,dy+480)])
    return [mm,disc,bar,wedge], hp(H,x0+CROSS[0]*s,y0+CROSS[1]*s)
top,c1=comp(340); bot,c2=comp(900)
inner=svgpath(unary_union(top),INK)+svgpath(xor_all(bot),INK,'evenodd')
inner+=hair(0,880,SW,880,1)
inner+=marker(*c1,r=18)+marker(*c2,r=18)
b=svgwrap(inner)+head(3,'JOIN')
b+=label(56,846,'∪　joined — insisted upon')+label(56,896,'⊕　joined — erased')
b+=copy('JOINED, A FORM IS<br>INSISTED UPON — OR ERASED.','The same four forms, twice. Only the rule of joining changed.',1470,64)
frames.append(('PSTORY03',b))
# ---------- 04 MULTIPLY — iterated projection toward a fixed point
s=9.0; m=translate(sscale(M,s,s,origin=(0,0)),SW/2-57.31*s/2,-60)
F=(560,360)
Hs=homog([(0,0),(SW,0),(SW,SH),(0,SH)],[(F[0]-420,F[1]-200),(F[0]+300,F[1]-260),(F[0]+380,F[1]+1080),(F[0]-340,F[1]+1000)])
gs=[];cs=[];g=m;x0,y0,_,_=m.bounds;c=(x0+CROSS[0]*s,y0+CROSS[1]*s)
for i in range(9):
    gs.append(g); cs.append(c)
    g=happly(g,Hs,3); c=hp(Hs,*c)
inner=svgpath(xor_all(gs),INK,'evenodd')
pts=' '.join(f'{x:.1f},{y:.1f}' for x,y in cs)
inner+=f'<polyline points="{pts}" fill="none" stroke="{PAPER}" stroke-width="0.8" style="{DF}"/>'
for x,y in cs[:5]: inner+=marker(x,y,r=max(4,20-3*cs.index((x,y))))
b=svgwrap(inner)+head(4,'MULTIPLY')
b+=copy('IT MULTIPLIES<br>TOWARD INFINITY.','Each copy is the last one, seen from further away.')
frames.append(('PSTORY04',b))
# ---------- 05 VANISH — rotated toward edge-on: a plane becomes a line
L=nibmark(640,480); Lh=L.bounds[3]; s=(SH-120)/Lh
angles=[0,32,54,70,82,89.4]
inner='';x=70
for i,th in enumerate(angles):
    c=math.cos(math.radians(th)); w=57.31*s
    m=translate(sscale(L,s,s,origin=(0,0)),0,-10); x0,y0,x1,y1=m.bounds
    ww=max(1.2,w*c); tilt=0.10*math.sin(math.radians(th))*(y1-y0)
    H=rect_to(m,[(x,y0),(x+ww,y0+tilt),(x+ww,y1-tilt),(x,y1)])
    inner+=svgpath(happly(m,H,6),INK)
    inner+=f'<text x="{x:.1f}" y="1630" font-family="Archivo" font-size="12" fill="{INK}" style="display:none">{th}</text>'
    x+=ww+[46,40,36,32,30,0][i]
b=svgwrap(inner)+head(5,'VANISH')
xs=70
for i,th in enumerate(angles):
    pass
b+=copy('SEEN EDGE-ON,<br>A PLANE IS A LINE.','0° — 32° — 54° — 70° — 82° — 89.4°　Turn it once more and there is nothing to see.')
frames.append(('PSTORY05',b))
# ---------- 06 WHAT REMAINS — only the crossing
s=4.2; m=translate(sscale(M,s,s,origin=(0,0)),0,0); x0,y0,_,_=m.bounds
cx,cy=x0+CROSS[0]*s,y0+CROSS[1]*s
crop=m.intersection(Point(cx,cy).buffer(70,64))
crop=translate(crop,SW/2-cx,880-cy)
inner=svgpath(crop,INK)+f'<circle cx="{SW/2}" cy="880" r="70" fill="none" stroke="{INK}" stroke-width="0.8"/>'
b=svgwrap(inner)+head(6,'WHAT REMAINS')
mk=P2['mark']; wd=P2['word']
mh=150; mw=mh*mk['w']/mk['h']; wdw=64; wdh=wdw*wd['h']/wd['w']
b+=f'<svg class="a" style="left: {SW/2-mw/2:.1f}px; top: 1380px; width: {mw:.1f}px; height: {mh}px" viewBox="0 0 {mk["w"]} {mk["h"]}"><path d="{mk["d"]}" fill="{INK}"/></svg>'
frames.append(('PSTORY06',b))
for n,body in frames: poster(f'{n}.dc.html',f'Ylli Story {n}',body,w=SW,h=SH)
print('ok')

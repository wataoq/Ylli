import math, json
from shapely.geometry import Polygon, LineString, box
from shapely.ops import unary_union
from shapely.affinity import translate, scale as sscale
exec(open('ref/gen.py').read().split('def d(pts)')[0])
TH=math.radians(45)
def sweep(pts,L,th=TH,hair=None):
    hx,hy=L/2*math.cos(th),-L/2*math.sin(th)
    ps=[Polygon([(x0+hx,y0+hy),(x1+hx,y1+hy),(x1-hx,y1-hy),(x0-hx,y0-hy)]).buffer(0) for (x0,y0),(x1,y1) in zip(pts,pts[1:])]
    g=unary_union(ps)
    hair=L*0.065 if hair is None else hair
    if hair:
        ls=LineString(pts); t=L*0.36
        if ls.length>2*t:
            from shapely.ops import substring
            ls=substring(ls,t,ls.length-t)
        g=g.union(ls.buffer(hair/2,cap_style=2,join_style=1))
    return g
def arc(cx,cy,r,a0,a1,n=48):
    return [(cx+r*math.cos(math.radians(a0+(a1-a0)*i/n)),cy+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
def path(g,prec=2):
    g=g.simplify(0.02)
    s=''
    for p in getattr(g,'geoms',[g]):
        if p.geom_type!='Polygon': continue
        for ring in [p.exterior,*p.interiors]:
            c=list(ring.coords)[:-1]; s+='M'+'L'.join(f'{x:.{prec}f} {y:.{prec}f}' for x,y in c)+'Z'
    return s
def norm(g,pad=0):
    x0,y0,x1,y1=g.bounds; g=translate(g,-x0+pad,-y0+pad); return g,(x1-x0+2*pad,y1-y0+2*pad)
# ---- mark ----
L=16; LANE=46; TOP=18; R=18
def mark(leg=130,legB=None,crossing=True,parts=False):
    xl,xr=0,LANE; lb=legB if legB is not None else leg
    A=fillet([(xl,0),(xl,TOP),(xr,TOP+LANE),(xr,TOP+LANE+leg)],R,24)
    B=fillet([(xr,0),(xr,TOP),(xl,TOP+LANE),(xl,TOP+LANE+lb)],R,24)
    gA=sweep(A,L); gB=sweep(B,L)
    g=unary_union([gA,gB])
    if not crossing:  # absence: remove the diagonal zone
        g=g.difference(box(-50,TOP-1,LANE+50,TOP+LANE+1))
    return g
def word(Lw=13):
    cap=100; gs=[]; arm=52
    gs.append(sweep([(0,0),(29,arm)],Lw)); gs.append(sweep([(58,0),(29,arm)],Lw)); gs.append(sweep([(29,arm),(29,cap)],Lw))
    x=29+42
    for _ in range(2):
        gs.append(sweep([(x,-6),(x,cap)],Lw)); x+=34
    gs.append(sweep([(x,40),(x,cap)],Lw)); gs.append(sweep([(x,10),(x,10+Lw*0.5)],Lw))
    return unary_union(gs)
out={}
def put(name,g,pad=0):
    g,(w,h)=norm(g,pad); out[name]={'d':path(g),'w':round(w,2),'h':round(h,2)}; return g
put('mark',mark(130,90))
put('mark_sym',mark(130))
for n,(a,b) in {'hang1':(130,90),'hang2':(230,170),'hang3':(380,290),'hang4':(620,470)}.items(): put(n,mark(a,b))
put('absent',mark(130,90,crossing=False))
put('absent2',mark(260,190,crossing=False))
put('absent3',mark(420,310,crossing=False))
put('word',word())
# nib diagram strokes
put('nib_v',sweep([(0,0),(0,60)],L)); put('nib_d1',sweep([(0,0),(42,42)],L)); put('nib_d2',sweep([(42,0),(0,42)],L)); put('nib_h',sweep([(0,0),(60,0)],L))
# ---- icons (24 grid, nib 3.4) ----
Li=2.3
def I(*strokes): return unary_union([sweep(s,Li,hair=0.45) for s in strokes])
icons={
 'home':I([(4,11),(12,4),(20,11)],[(6,10),(6,20),(18,20),(18,10)],[(10,20),(10,14),(14,14),(14,20)]),
 'search':I(arc(10,10,6,0,360,64),[(14.5,14.5),(20,20)]),
 'bag':I([(5,8),(19,8),(19,20),(5,20),(5,8)],arc(12,8,4,180,360,32)),
 'account':I(arc(12,8,4,0,360,48),arc(12,21,7.5,180,360,48)),
 'menu':I([(4,7),(20,7)],[(4,12),(20,12)],[(4,17),(20,17)]),
 'close':I([(6,6),(18,18)],[(18,6),(6,18)]),
 'arrow':I([(4,12),(20,12)],[(14,6),(20,12),(14,18)]),
 'plus':I([(12,4),(12,20)],[(4,12),(20,12)]),
 'hanger':I(arc(12,6,2.4,180,400,24),[(12,8.6),(12,10),(3,17),(21,17),(12,10)]),
 'store':I(arc(12,10,6,160,380,48),[(6.4,12.1),(12,21),(17.6,12.1)],arc(12,10,2,0,360,24)),
}
for k,g in icons.items():
    out['ic_'+k]={'d':path(g),'w':24,'h':24}
json.dump(out,open('nib/paths.json','w'))
print({k:(v['w'],v['h'],len(v['d'])) for k,v in out.items()})

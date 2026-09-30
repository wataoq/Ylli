import json, math
from shapely.geometry import box, LineString, Point
from shapely.ops import unary_union
from shapely.affinity import translate
src=open('nib/geo.py').read().split('out={}')[0]
ns={}; exec(src,ns)
fillet=ns['fillet']; sweep=ns['sweep']; L=ns['L']; LANE=ns['LANE']; TOP=ns['TOP']; R=ns['R']
xl,xr=0,LANE; leg,legB=130,90
A=fillet([(xl,0),(xl,TOP),(xr,TOP+LANE),(xr,TOP+LANE+leg)],R,24)
B=fillet([(xr,0),(xr,TOP),(xl,TOP+LANE),(xl,TOP+LANE+legB)],R,24)
gA=sweep(A,L); gB=sweep(B,L)
full=unary_union([gA,gB]); ox,oy=-full.bounds[0],-full.bounds[1]
c1,c2=TOP,TOP+LANE
def cut(g,a,b): return g.intersection(box(-100,a,200,b))
def poly_d(g):
    s=''
    for p in getattr(g,'geoms',[g]):
        if p.geom_type!='Polygon' or p.is_empty: continue
        p=p.simplify(0.02)
        for ring in [p.exterior,*p.interiors]:
            s+='M'+'L'.join(f'{x+ox:.2f} {y+oy:.2f}' for x,y in list(ring.coords)[:-1])+'Z'
    return s
pieces={}
for name,g in [('A',gA),('B',gB)]:
    for i,(a,b) in enumerate([(-50,c1),(c1,c2),(c2,400)]):
        pg=cut(g,a,b); c=pg.centroid
        pieces[f'{name}{i+1}']={'d':poly_d(pg),'c':[round(c.x+ox,2),round(c.y+oy,2)],'b':[round(v,2) for v in (pg.bounds[0]+ox,pg.bounds[1]+oy,pg.bounds[2]+ox,pg.bounds[3]+oy)]}
seams=[]
for name,g in [('A',gA),('B',gB)]:
    for k,y in enumerate([c1,c2]):
        seg=g.intersection(LineString([(-100,y),(200,y)]))
        x0,_,x1,_=seg.bounds
        for x in (x0,x1): seams.append([f'{name}{k+1}',f'{name}{k+2}',round(x+ox,2),round(y+oy,2)])
cross=[round(LANE/2+ox,2),round(TOP+LANE/2+oy,2)]
W,H=full.bounds[2]-full.bounds[0],full.bounds[3]-full.bounds[1]
json.dump({'pieces':pieces,'seams':seams,'cross':cross,'w':round(W,2),'h':round(H,2)},open('web/pieces.json','w'))
print({k:(v['c'],v['b']) for k,v in pieces.items()},seams,cross,W,H)

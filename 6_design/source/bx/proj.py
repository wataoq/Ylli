import numpy as np, math
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union
from shapely.affinity import translate, scale as sscale, rotate
def homog(src,dst):
    A=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y,-u]); A.append([0,0,0,x,y,1,-v*x,-v*y,-v])
    _,_,V=np.linalg.svd(np.array(A,float)); H=V[-1].reshape(3,3); return H/H[2,2]
def hp(H,x,y):
    u,v,w=H@np.array([x,y,1.0]); return (u/w,v/w)
def happly(g,H,seg=4):
    g=g.segmentize(seg); out=[]
    for p in getattr(g,'geoms',[g]):
        if p.geom_type!='Polygon' or p.is_empty: continue
        ext=[hp(H,x,y) for x,y in p.exterior.coords]; ints=[[hp(H,x,y) for x,y in r.coords] for r in p.interiors]
        out.append(Polygon(ext,ints).buffer(0))
    return unary_union(out)
def rect_to(g,quad):
    x0,y0,x1,y1=g.bounds
    return homog([(x0,y0),(x1,y0),(x1,y1),(x0,y1)],quad)
def xor_all(gs):
    G=Polygon()
    for g in gs: G=G.symmetric_difference(g)
    return G

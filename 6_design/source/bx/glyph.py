import math
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.recordingPen import DecomposingRecordingPen
from shapely.geometry import Polygon, MultiPolygon, box
from shapely.ops import unary_union
from shapely.affinity import translate, scale as sscale, skew, rotate
import functools
SRC='fonts/b9202932174a.woff2'
@functools.lru_cache(None)
def font(wght=900,wdth=62):
    f=TTFont(SRC); return instancer.instantiateVariableFont(f,{'wght':wght,'wdth':wdth})
def _flatten(ops,n=10):
    rings=[];cur=[];p0=None
    for op,args in ops:
        if op=='moveTo': cur=[args[0]]; p0=args[0]
        elif op=='lineTo': cur.append(args[0])
        elif op=='qCurveTo':
            pts=list(args); start=cur[-1]
            # implied on-curve points
            offs=pts[:-1]; end=pts[-1]
            seq=[]
            for i,o in enumerate(offs):
                if i<len(offs)-1:
                    nxt=offs[i+1]; mid=((o[0]+nxt[0])/2,(o[1]+nxt[1])/2); seq.append((o,mid))
                else: seq.append((o,end))
            for o,e in seq:
                s=cur[-1]
                for k in range(1,n+1):
                    t=k/n; cur.append(((1-t)**2*s[0]+2*(1-t)*t*o[0]+t*t*e[0],(1-t)**2*s[1]+2*(1-t)*t*o[1]+t*t*e[1]))
        elif op=='curveTo':
            c1,c2,e=args; s=cur[-1]
            for k in range(1,n+1):
                t=k/n; mt=1-t
                cur.append((mt**3*s[0]+3*mt*mt*t*c1[0]+3*mt*t*t*c2[0]+t**3*e[0],mt**3*s[1]+3*mt*mt*t*c1[1]+3*mt*t*t*c2[1]+t**3*e[1]))
        elif op in('closePath','endPath'):
            if len(cur)>2: rings.append(cur)
            cur=[]
    return rings
def glyph(ch,wght=900,wdth=62):
    f=font(wght,wdth); gs=f.getGlyphSet(); cmap=f.getBestCmap(); name=cmap[ord(ch)]
    pen=DecomposingRecordingPen(gs); gs[name].draw(pen)
    rings=_flatten(pen.value)
    # even-odd assembly
    g=Polygon()
    for r in rings:
        p=Polygon(r).buffer(0)
        g=g.symmetric_difference(p)
    adv=gs[name].width
    # flip y (font units, y up) -> y down, baseline at 0, cap ~ 700
    from shapely.affinity import scale as sc
    g=sc(g,1,-1,origin=(0,0))
    return g,adv
def word(s,wght=900,wdth=62,track=0,size=1000):
    """returns list of (glyph geometry, x offset) in font units scaled so 1000upm -> size"""
    out=[];x=0;k=size/1000
    for ch in s:
        if ch==' ': g,a=glyph('n',wght,wdth); x+=a*0.6*k; continue
        g,a=glyph(ch,wght,wdth)
        out.append(translate(sscale(g,k,k,origin=(0,0)),x,0)); x+=(a+track)*k
    return out,x
def path(g,prec=1):
    s=''
    for p in getattr(g,'geoms',[g]):
        if p.geom_type!='Polygon' or p.is_empty: continue
        for ring in [p.exterior,*p.interiors]:
            c=list(ring.coords)[:-1]; s+='M'+'L'.join(f'{x:.{prec}f} {y:.{prec}f}' for x,y in c)+'Z'
    return s
def warp(g,fn,seg=4):
    """non-linear distortion: fn(x,y)->(x,y)"""
    g=g.segmentize(seg)
    def w(p):
        ext=[fn(x,y) for x,y in p.exterior.coords]; ints=[[fn(x,y) for x,y in r.coords] for r in p.interiors]
        return Polygon(ext,ints).buffer(0)
    return unary_union([w(p) for p in getattr(g,'geoms',[g]) if p.geom_type=='Polygon'])
def slices(g,ys,axis='y'):
    x0,y0,x1,y1=g.bounds; out=[]
    for a,b in zip(ys,ys[1:]):
        out.append(g.intersection(box(x0-10,a,x1+10,b)) if axis=='y' else g.intersection(box(a,y0-10,b,y1+10)))
    return out
import json, re
_P=json.load(open('nib/paths.json'))
def from_d(d):
    g=Polygon()
    for ring in re.findall(r'M([^Z]+)Z',d):
        pts=[tuple(map(float,p.split())) for p in ring.split('L')]
        g=g.symmetric_difference(Polygon(pts).buffer(0))
    return g
def markgeo(name='mark'): return from_d(_P[name]['d'])
def nibmark(leg,legB):
    """long-legged mark geometry built with the same nib rules"""
    import importlib.util,sys
    src=open('nib/geo.py').read().split('out={}')[0]
    ns={}; exec(src,ns); g=ns['mark'](leg,legB)
    x0,y0,_,_=g.bounds; return translate(g,-x0,-y0)
def svgpath(g,fill='#0A0A0A',rule='nonzero',extra=''):
    return f'<path d="{path(g)}" fill="{fill}" fill-rule="{rule}"{extra}/>'

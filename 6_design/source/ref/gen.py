import math, pymupdf as fitz
BG='#F5F3EF'; FG='#0A0A0A'
def fillet(pts,r,n=10):
    # polyline with circular-ish fillets (quadratic approx via sampled arc)
    out=[pts[0]]
    for i in range(1,len(pts)-1):
        p0,p1,p2=pts[i-1],pts[i],pts[i+1]
        v1=(p0[0]-p1[0],p0[1]-p1[1]);v2=(p2[0]-p1[0],p2[1]-p1[1])
        l1=math.hypot(*v1);l2=math.hypot(*v2)
        u1=(v1[0]/l1,v1[1]/l1);u2=(v2[0]/l2,v2[1]/l2)
        ang=math.acos(max(-1,min(1,u1[0]*u2[0]+u1[1]*u2[1])))
        t=r/math.tan(ang/2) if r>0 else 0
        t=min(t,l1*0.95,l2*0.95)
        a=(p1[0]+u1[0]*t,p1[1]+u1[1]*t); b=(p1[0]+u2[0]*t,p1[1]+u2[1]*t)
        for k in range(n+1):
            s=k/n  # quadratic bezier a->p1->b
            x=(1-s)**2*a[0]+2*(1-s)*s*p1[0]+s*s*b[0]; y=(1-s)**2*a[1]+2*(1-s)*s*p1[1]+s*s*b[1]
            out.append((x,y))
    out.append(pts[-1]); return out
def d(pts): return 'M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in pts)
def st(pts,w,c=FG,cap='butt'): return f'<path d="{d(pts)}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="{cap}" stroke-linejoin="round"/>'
def mark(ox=0,oy=0,w=14,lane=47.6,top=14,leg=35,r=19.6,gap=0.76,w2=None,legL=None,legR=None,topL=None,topR=None,cutAngle=0,bg=BG,fg=FG):
    w2=w2 or w
    xl,xr=ox+19,ox+19+lane
    tl=topL if topL is not None else top; tr=topR if topR is not None else top
    y0=oy+12
    # thread1 (over): top-right -> bottom-left
    yb1=y0+tr; yc1=yb1+lane; ye1=yc1+(legL if legL is not None else leg)
    T1=fillet([(xr,y0),(xr,yb1),(xl,yc1),(xl,ye1)],r)
    yb2=y0+tl; yc2=yb2+lane; ye2=yc2+(legR if legR is not None else leg)
    T2=fillet([(xl,y0),(xl,yb2),(xr,yc2),(xr,ye2)],r)
    g=gap*w
    s=st(T2,w2,fg)+st(T1,w+2*g,bg)+st(T1,w,fg)
    # optional angled cuts: mask ends with bg polygons
    if cutAngle:
        k=math.tan(math.radians(cutAngle))*w
        for x,yy,sgn in [(xl,y0,1),(xr,y0,1)]:
            s+=f'<polygon points="{x-w},{yy-1} {x+w},{yy-1} {x+w},{yy+k*0.5} {x-w},{yy-k*0.5}" fill="{bg}"/>'
    return s
def render(name,items,W,H,bg=BG,scale=1.5):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><rect width="100%" height="100%" fill="{bg}"/>{items}</svg>'
    open(f'ref/{name}.svg','w').write(svg)
    fitz.open(f'ref/{name}.svg')[0].get_pixmap(matrix=fitz.Matrix(scale,scale)).save(f'ref/{name}.png')

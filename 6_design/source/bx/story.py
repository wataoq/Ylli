import sys; sys.path.insert(0,'.')
import bx.pcommon as pc
from bx.pcommon import *
from bx.glyph import *
import math, json
SW,SH=1080,1920
P2=json.load(open('nib/paths.json'))
def sv(name,x,y,h,fill):
    p=P2[name]; w=h*p['w']/p['h']
    return f'<svg class="a" style="left: {x-w/2:.1f}px; top: {y:.1f}px; width: {w:.1f}px; height: {h:.1f}px" viewBox="0 0 {p["w"]} {p["h"]}" aria-hidden="true"><path d="{p["d"]}" fill="{fill}"/></svg>', w
# 1) wordmark, 2) symbol — each on 玄 and 素
for bg,fg,tag in [(INK,PAPER,'k'),(PAPER,INK,'w')]:
    p=P2['word']; ww=560; wh=ww*p['h']/p['w']
    s,_=sv('word',SW/2,SH/2-wh/2,wh,fg)
    poster(f'ST_word_{tag}.dc.html','Ylli Story Wordmark',s,bg=bg,fg=fg,w=SW,h=SH)
    s,_=sv('mark',SW/2,-8,1180,fg)
    poster(f'ST_mark_{tag}.dc.html','Ylli Story Symbol',s,bg=bg,fg=fg,w=SW,h=SH)
# 3) SHIFT, in place and shifted — recomposed for 9:16
def shift_story(shifted):
    m0=markgeo(); s=2600/205.31
    M0=translate(sscale(m0,s,s,origin=(0,0)),SW/2-57.31*s/2+28,-330)
    ws,wx=word('SHIFT',900,62,-10,660)
    W0=unary_union(ws); x0,y0,x1,y1=W0.bounds; k=(SW+40)/(x1-x0)
    W0=translate(sscale(W0,k,k,origin=(0,0)),-20-x0*k,0); _,a,_,bb=W0.bounds
    W0=translate(W0,0,760-bb)
    H=[160,8,40,8,94,18,128,6,30,64,10,160,14,48,8,86,124,16,40,188,10,72,24,214,54,120]
    edges=[-400]; y=160
    for h in H[1:]: edges.append(y); y+=h
    edges=sorted(set(edges+[160,SH+400]))
    n=len(edges)-1; shifts=[]; sq=[]
    for i in range(n):
        t=i/(n-1); amp=5+680*t**2.2; sgn=1 if (i*7)%3!=0 else -1
        shifts.append(0 if i<2 else sgn*amp*(0.55+0.45*math.sin(i*1.9))*(0.35 if i<12 else 1))
        sq.append(1.0 if i<12 else [1,0.46,1.7,1,0.26,1.3,0.8][i%7])
    def band(G,kk):
        out=[]
        for (a,b),dx,q in zip(zip(edges,edges[1:]),shifts,sq):
            pc_=G.intersection(box(-3000,a,4000,b))
            if pc_.is_empty: continue
            out.append(translate(sscale(pc_,q,1,origin=(SW/2,0)),dx*kk,0))
        return unary_union(out)
    if shifted: M,Wd=band(M0,1.0),band(W0,-0.55)
    else: M,Wd=M0,W0
    G=M.symmetric_difference(Wd)
    body=f'<svg class="a" style="left: 0; top: 0; width: {SW}px; height: {SH}px" viewBox="0 0 {SW} {SH}" aria-hidden="true">'
    if shifted: body+=f'<path d="{path(M0.symmetric_difference(W0))}" fill="none" stroke="{INK}" stroke-width="0.9" fill-rule="evenodd"/>'
    body+=svgpath(G,INK,'evenodd')+'</svg>'
    DF='mix-blend-mode: difference'
    if shifted:
        for i,((a,bb2),dx) in enumerate(zip(zip(edges,edges[1:]),shifts)):
            if bb2-a<50 or a<260 or a>1640: continue
            body+=f'<div class="a" style="left: 960px; top: {a:.0f}px; width: 120px; height: 1px; background: {PAPER}; {DF}"></div>'
            body+=T(f'{i:02d}　{dx:+.0f}',960,a+4,11,500,100,PAPER,1,f'{DF}; width: 84px; text-align: right')
    # story safe area: keep type between y 250 and 1670
    body+=T('SHIFT',56,262,16,800,100,PAPER,1,DF)+T('How far can a form move<br>before it stops being itself?',56,288,16,400,100,PAPER,1.35,DF)
    body+=T('Ylli — Collection 01<br>Launch',800,262,16,400,100,PAPER,1.35,DF)
    body+=T('Form, displaced.' if shifted else 'Form, in place.',640,1630,14,400,100,PAPER,1,DF)
    poster('ST_shift.dc.html' if shifted else 'ST_shift0.dc.html','Ylli Story Shift',body,w=SW,h=SH)
shift_story(False); shift_story(True)

import json, math, os
P=json.load(open('nib/paths.json'))
K='#0A0A0A'; W='#F5F3EF'; S='#8A877F'; B='#1A2A4A'; T2='#4A4843'; T3='#6B6862'; RULE='#D9D5CD'; GROUND='#E6E3DC'
COL=[56+i*230 for i in range(8)]  # 8 cols, 198 + 32 gutter
CW=198
OUT='canvas/project'
HEAD='''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@300;400;500;600&amp;family=Noto+Sans+JP:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{bg}}}
.m{{font-family:"Noto Serif JP","Hiragino Mincho ProN","Yu Mincho",serif}}
.s{{font-family:"Noto Sans JP","Hiragino Sans",sans-serif}}
.a{{position:absolute}}
.hd{{position:absolute;top:44px;font-family:"Noto Serif JP",serif;font-size:14px;line-height:20px}}
.ds{{position:absolute;font-family:"Noto Serif JP",serif;font-size:14px;line-height:26px}}
.lb{{font-family:"Noto Sans JP",sans-serif;font-size:11px;line-height:16px;letter-spacing:0.04em}}
.sm{{font-family:"Noto Serif JP",serif;font-size:13px;line-height:22px}}
.card{{position:absolute;overflow:hidden}}
.sh{{box-shadow:0 18px 40px rgba(10,10,10,0.14),0 2px 4px rgba(10,10,10,0.08)}}
</style>
</helmet>
<div style="position: relative; width: 1920px; height: 1080px; overflow: hidden; background: {bg}; color: {fg}">
'''
TAIL='''</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1920,"height":1080}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
'''
def f(v): return f'{v:.1f}'.rstrip('0').rstrip('.')
def svg(name,x,y,h=None,w=None,fill=K,extra=''):
    p=P[name]
    if h is None and w is None: h=p['h']
    if h is None: h=w*p['h']/p['w']
    if w is None: w=h*p['w']/p['h']
    return f'<svg class="a" style="left: {f(x)}px; top: {f(y)}px; width: {f(w)}px; height: {f(h)}px{extra}" viewBox="0 0 {p["w"]} {p["h"]}" aria-hidden="true"><path d="{p["d"]}" fill="{fill}"/></svg>'
def size(name,h=None,w=None):
    p=P[name]
    if h is not None: return h*p['w']/p['h'],h
    return w,w*p['h']/p['w']
# signature horizontal: word bottom aligned to short leg end
MK=P['mark']; WD=P['word']
SHORT_END=18+46+90+5.657  # y of short leg end in mark coords
def sig_h(x,y,h,fill=K):
    s=h/MK['h']; out=svg('mark',x,y,h=h,fill=fill)
    wh=WD['h']*s*0.62; wx=x+MK['w']*s+46*s*0.9
    wy=y+SHORT_END*s-wh
    return out+svg('word',wx,wy,h=wh,fill=fill)
def sig_h_w(h): s=h/MK['h']; return MK['w']*s+46*s*0.9+WD['w']*s*0.62
def sig_v(cx,y,h,fill=K):
    w,_=size('mark',h=h); out=svg('mark',cx-w/2,y,h=h,fill=fill)
    wh=h*0.2; ww,_=size('word',h=wh)
    return out+svg('word',cx-ww/2,y+h+h*0.16,h=wh,fill=fill)
def vstroke(x,y0,y1,L,fill=K):
    h=L/2*0.70711
    return f'<polygon points="{f(x-h)},{f(y0+h)} {f(x+h)},{f(y0-h)} {f(x+h)},{f(y1-h)} {f(x-h)},{f(y1+h)}" fill="{fill}"/>'
def header(part,partname,sec,secname,page,fg=K,sub=T3):
    return (f'<div class="hd" style="left: {COL[0]}px; color: {fg}">{part}</div>'
            f'<div class="hd" style="left: {COL[0]+90}px; color: {fg}">{partname}</div>'
            f'<div class="hd" style="left: {COL[2]}px; color: {fg}">{sec}</div>'
            f'<div class="hd" style="left: {COL[2]+60}px; color: {fg}">{secname}</div>'
            f'<div class="hd" style="left: {COL[4]}px; color: {sub}">{page:02d}</div>')
def desc(title,body,y=200,fg=K,sub=T2,w=CW*2+32):
    return (f'<div class="ds" style="left: {COL[0]}px; top: {y}px; width: {w}px; color: {fg}">'
            f'<div style="font-size: 14px; line-height: 22px; margin-bottom: 14px">{title}</div>'
            f'<div style="color: {sub}; font-size: 13px; line-height: 24px">{body}</div></div>')
BOARDS=[]
def page(fname,title,body,bg=W,fg=K,board_title=None,part='A'):
    html=HEAD.format(title=title,bg=bg,fg=fg)+body+TAIL
    open(os.path.join(OUT,fname),'w').write(html)
    BOARDS.append((fname,board_title or title,part))
PAT=[0.93,0.66,0.84,0.58,1.0,0.72,0.88,0.61,0.97,0.69,0.8,0.55]
def kvA(x,y,w,h,s,fill=K,bg=None,mark_at=3,mark='hang2',n=None,offset=0,cls='a',sp=2.0,maxl=0.8):
    """Type A 懸: verticals hung from the top edge; one pair replaced by the mark."""
    lane=46*s; L=16*s; out=''; step=lane*sp
    if bg: out+=f'<rect width="{f(w)}" height="{f(h)}" fill="{bg}"/>'
    cnt=n or int(w/lane)+2
    i=0; xx=step*0.4+offset
    while xx< w+lane:
        if i==mark_at:
            p=P[mark]; sc=h*1.02/p['h']; sc=min(sc,s*1.0) if False else sc
            sc=s
            mh=p['h']*sc
            out+=f'<g transform="translate({f(xx-5.657*sc)},{f(-5.657*sc)}) scale({f(sc)})"><path d="{p["d"]}" fill="{fill}"/></g>'
            xx+=lane+step; i+=1; continue
        ln=PAT[i%len(PAT)]*h*maxl
        out+=vstroke(xx,-L,ln,L,fill)
        xx+=step; i+=1
    return f'<svg class="{cls}" style="left: {f(x)}px; top: {f(y)}px; width: {f(w)}px; height: {f(h)}px" viewBox="0 0 {f(w)} {f(h)}" aria-hidden="true">{out}</svg>'
def kvB(x,y,w,h,fill=K,bg=None,zoom=1.0,cls='a'):
    """Type B 交: crop of the crossing"""
    p=P['mark']; sc=h/60*zoom
    cx=(23+5.657)*sc; cy=(18+23+5.657)*sc
    out=(f'<rect width="{f(w)}" height="{f(h)}" fill="{bg}"/>' if bg else '')+f'<g transform="translate({f(w/2-cx)},{f(h*0.46-cy)}) scale({f(sc)})"><path d="{p["d"]}" fill="{fill}"/></g>'
    return f'<svg class="{cls}" style="left: {f(x)}px; top: {f(y)}px; width: {f(w)}px; height: {f(h)}px" viewBox="0 0 {f(w)} {f(h)}" aria-hidden="true">{out}</svg>'
def kvC(x,y,w,h,fill=K,bg=None,cls='a',hname='absent'):
    """Type C 不在: the mark without its crossing, hung from the top"""
    p=P[hname]; sc=h*1.0/p['h']
    out=(f'<rect width="{f(w)}" height="{f(h)}" fill="{bg}"/>' if bg else '')+f'<g transform="translate({f(w/2-p["w"]*sc/2)},{f(-12*sc)}) scale({f(sc)})"><path d="{p["d"]}" fill="{fill}"/></g>'
    return f'<svg class="{cls}" style="left: {f(x)}px; top: {f(y)}px; width: {f(w)}px; height: {f(h)}px" viewBox="0 0 {f(w)} {f(h)}" aria-hidden="true">{out}</svg>'
def icon(name,x,y,sz,fill=K):
    return svg('ic_'+name,x,y,h=sz,w=sz,fill=fill)

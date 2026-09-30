import sys; sys.path.insert(0,'.')
from bx.pcommon import *
import json
SW,SH=1080,1920
P2=json.load(open('nib/paths.json'))
def sv(name,cx,y,h,fill):
    p=P2[name]; w=h*p['w']/p['h']
    return f'<svg class="a" style="left: {cx-w/2:.1f}px; top: {y:.1f}px; width: {w:.1f}px; height: {h:.1f}px" viewBox="0 0 {p["w"]} {p["h"]}" aria-hidden="true"><path d="{p["d"]}" fill="{fill}"/></svg>'
for bg,fg,tag in [(INK,PAPER,'k'),(PAPER,INK,'w')]:
    mh=1040; ww=180; wh=ww*P2['word']['h']/P2['word']['w']
    b=sv('mark',SW/2,-8,mh,fg)+sv('word',SW/2,1490,wh,fg)
    poster(f'ST_sig_{tag}.dc.html','Ylli Story Signature',b,bg=bg,fg=fg,w=SW,h=SH)

import sys; sys.path.insert(0,'.')
from bx.common import P, svg, size, sig_h, sig_h_w, f, K, W, S, B, vstroke
import os
PW,PH=1000,1414
INK='#0A0A0A'; PAPER='#F5F3EF'; GREY='#8A877F'
PHEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{bg}}}
.g{{font-family:"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif}}
.a{{position:absolute}}
.r{{transform-origin:0 0}}
</style>
</helmet>
<div class="g" style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: {bg}; color: {fg}">
'''
PTAIL='''</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
POSTERS=[]
def poster(fname,title,body,bg=PAPER,fg=INK,w=PW,h=PH,bt=None):
    open(os.path.join('canvas/project',fname),'w').write(PHEAD.format(title=title,bg=bg,fg=fg,w=w,h=h)+body+PTAIL.format(w=w,h=h))
    POSTERS.append((fname,bt or title,w,h))
def T(s,x,y,sz,wt=400,wd=100,fg=INK,lh=1.0,extra='',cls='a g'):
    return f'<div class="{cls}" style="left: {f(x)}px; top: {f(y)}px; font-size: {f(sz)}px; font-weight: {wt}; font-stretch: {wd}%; line-height: {lh}; color: {fg}; {extra}">{s}</div>'
STORY=('The question “who are you?” always asks for an answer. Names, titles, affiliations and styles are offered as proof, and clothing has long been one of them: I wear this, therefore I am this. '
 'But has the answer ever matched you completely? The mirror agrees for a moment; the next morning, a slight discomfort. You have changed, yet the clothes return yesterday’s outline. A small gap opens between the answer and yourself. '
 'Ylli does not fill that gap. The gap is not a defect but the most honest trace of the fact that you are in flux. Ylli does not present a finished image of who you are; it designs a structure that lets you remain unresolved — held in tension, never fully fixed, never collapsing. '
 'In that suspension, the questions of what it is to wear and what it is to be a self rise without answers. We call that moment Gen: dark, deep, inexhaustible.')
FOOT_FACTS=['Ylli','Collection 01','Launch','[DATE] — [DATE]','[VENUE]','ylli.[domain]']

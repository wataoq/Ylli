from bx.pcommon import *
def R(s,x,y,sz,wt=900,wd=75,fg=INK,extra='',lh=0.78):
    return T(s,x,y,sz,wt,wd,fg,lh,f'transform: rotate(-90deg); transform-origin: 0 0; white-space: nowrap; {extra}')
grad='background: linear-gradient(90deg, #0A0A0A 0%, #0A0A0A 30%, #8A877F 72%, #D9D5CD 100%); -webkit-background-clip: text; background-clip: text; color: transparent'
grad2='background: linear-gradient(90deg, #BDB8AE 0%, #6F6C65 60%, #0A0A0A 100%); -webkit-background-clip: text; background-clip: text; color: transparent'
b=''
b+=svg('word',64,56,h=44)+T('A garment that lets you remain inside the question.',64,124,15,500,100)
b+=R('WAIT',40,1372,352,900,72)
b+=R('FOR',268,1100,352,900,62,extra=grad2+'; mix-blend-mode: multiply')
b+=R('MEANING,',470,1392,352,900,62,extra=grad+'; mix-blend-mode: multiply')
b+=R('for it does not arrive on time.',745,1380,26,300,100,GREY,lh=1)
b+=svg('mark',900,-6,h=230)
facts=[('Fluidity',330),('Suspension',452),('Depth',600)]
for t,y in facts: b+=R(t,880,y+120,13,500,100,lh=1)
b+=T(STORY,0,0,10,400,90,INK,1.32,'transform: rotate(-90deg); transform-origin: 0 0; width: 500px; text-align: justify; left: 884px; top: 1372px; hyphens: auto')
b+=T('[DATE] — [DATE]<br>[VENUE]',64,1330,12,500,100,INK,1.35,'display: none')
b+=R('Ylli — Collection 01 — Launch — [DATE] — [VENUE]',838,1372,11,600,110,lh=1)
b+=T('01 / 06',64,1388,11,500,100,GREY)
poster('PS01Wait.dc.html','Ylli Poster 01 — Wait for meaning',b,bt='Poster 01 — WAIT FOR MEANING')

from bx.pcommon import *
# SUSPENDED: each letter hung from the top edge on a hairline, at a different depth
letters='SUSPENDED'
drops=[0.26,0.50,0.12,0.40,0.60,0.20,0.46,0.32,0.78]
b=''
x=40; cw=102
for i,(ch,d) in enumerate(zip(letters,drops)):
    y=110+d*820
    b+=f'<div class="a" style="left: {f(x+cw/2-0.5)}px; top: 0; width: 1px; height: {f(y+18)}px; background: {INK}"></div>'
    b+=T(ch,x-14,y,300,880,62,INK,0.86,f'width: {cw+28}px; text-align: center')
    x+=cw+0.5
b+=T('Neither falling,<br>nor landing.',40,1190,54,300,100,INK,1.02)
b+=T('Ylli<br>Collection 01<br>Launch',640,1196,13,600,100,INK,1.4)
b+=T('[DATE] — [DATE]<br>[VENUE]<br>ylli.[domain]',800,1196,13,400,100,INK,1.4)
b+=svg('word',640,1300,h=60)
b+=T('sus·pend·ed　<i>adj.</i>　1 hanging from above, without support from below.　2 held between two states.',40,1340,12,400,100,GREY)+T('02 / 06',905,1338,11,500,100,GREY)
poster('PS02Suspended.dc.html','Ylli Poster 02 — Suspended',b,bt='Poster 02 — SUSPENDED')

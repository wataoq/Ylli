from bx.pcommon import *
# UNRESOLVED with the middle band removed (Type C 不在)
b=''
lines=[('UN',0),('RESOL',1),('VED.',2)]
b+=T('UN',28,40,470,900,100,INK,0.80,'letter-spacing: -0.02em')
b+=T('RESOL',28,430,420,900,62,INK,0.80,'letter-spacing: -0.02em; white-space: nowrap')
b+=T('VED.',28,800,470,900,100,INK,0.80,'letter-spacing: -0.02em')
# the removed band
b+=f'<div class="a" style="left: 0; top: 548px; width: {PW}px; height: 150px; background: {PAPER}"></div>'
b+=T('What happened is not written.',40,612,18,400,100,INK,1)
b+=T('Remain, unresolved.',650,612,18,700,100,INK,1)
b+=f'<div class="a" style="left: 0; top: 1200px; width: {PW}px; height: 1px; background: {INK}"></div>'
b+=T('Ylli',40,1222,13,700,100)+T('Collection 01<br>Launch',140,1222,13,400,100,INK,1.4)+T('[DATE] — [DATE]<br>[VENUE]',400,1222,13,400,100,INK,1.4)+T('ylli.[domain]',700,1222,13,400,100)
b+=svg('absent',900,1180,h=230)
b+=T('03 / 06',40,1370,11,500,100,GREY)
poster('PS03Unresolved.dc.html','Ylli Poster 03 — Unresolved',b,bt='Poster 03 — UNRESOLVED')

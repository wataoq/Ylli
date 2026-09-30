from bx.pcommon import *
# Thickness is decided by direction: heavy line down-right over a hairline line up-right
b=''
thin='THICKNESS IS DECIDED BY DIRECTION — THICKNESS IS DECIDED BY DIRECTION — THICKNESS IS DECIDED BY DIRECTION'
b+=T(thin,-300,1520,64,100,125,INK,1,'white-space: nowrap; transform: rotate(-45deg); transform-origin: 0 0')
b+=T('THICKNESS<br>IS DECIDED<br>BY DIRECTION.',-40,-120,190,900,70,INK,0.86,'white-space: nowrap; transform: rotate(45deg); transform-origin: 0 0; left: 150px; top: -40px')
b+=T('The same pen, held at forty-five degrees,<br>draws a heavy line and a line that almost disappears.<br>Thickness is not a property of the line.<br>It is a relation.',40,40,14,400,100,INK,1.45,'left: 600px; top: 1150px')
b+=svg('mark',910,-6,h=240)
b+=T('Ylli — Collection 01 — Launch<br>[DATE] — [DATE]　[VENUE]',40,1330,13,500,100,INK,1.4)
b+=T('04 / 06',905,1370,11,500,100,GREY)
poster('PS04Direction.dc.html','Ylli Poster 04 — Direction',b,bt='Poster 04 — DIRECTION')

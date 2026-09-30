from bx.pcommon import *
# REMAIN, — one word, rhythm from width and weight only
rows=[(62,900),(80,700),(125,100),(70,900),(100,300),(62,600),(125,900),(90,200),(62,900)]
b=''; y=26
for i,(wd,wt) in enumerate(rows):
    b+=T('REMAIN,',30,y,150,wt,wd,INK,0.80,'white-space: nowrap; letter-spacing: -0.01em')
    y+=120
b+=T('UNRESOLVED.',30,y+10,150,900,62,PAPER,0.80,f'white-space: nowrap; background: {INK}; padding: 0 12px 6px 0')
b+=T('Ylli',30,1300,13,700,100)+T('Collection 01 — Launch<br>[DATE] — [DATE]<br>[VENUE]',120,1300,13,400,100,INK,1.4)+T('05 / 06',905,1370,11,500,100,GREY)
b+=svg('mark',922,-6,h=210)
poster('PS05Remain.dc.html','Ylli Poster 05 — Remain',b,bt='Poster 05 — REMAIN, UNRESOLVED.')

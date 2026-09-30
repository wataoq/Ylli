from bx.pcommon import *
p=P['word']; sc=13.2
# wordmark rotated 90deg clockwise, hung from the top, cropped by the sheet
b=f'<svg class="a" style="left: 0; top: 0; width: {PW}px; height: {PH}px" viewBox="0 0 {PW} {PH}" aria-hidden="true"><g transform="translate(-120,-70) scale({sc})"><path d="{p["d"]}" fill="{INK}"/></g></svg>'
frag=[('NOT AN ANSWER.',40,40,58,900,62,INK),
('A PLACE TO STAY.',40,104,58,200,125,INK),
('Clothing that does not say who you are.',44,190,15,500,100,INK),
('The gap is not a defect.',430,760,15,500,100,INK),
('It is the most honest trace',430,780,15,300,100,INK),
('of being in flux.',430,800,15,300,100,INK),
('Gen 玄',42,1010,64,300,125,INK),
('dark, deep, inexhaustible',44,1086,14,400,100,INK),
('COLLECTION',430,1120,44,900,62,INK),('01',430,1162,150,100,125,INK),
('[DATE] — [DATE]',44,1300,13,600,100,INK),('[VENUE]',44,1320,13,400,100,INK),('ylli.[domain]',44,1340,13,400,100,INK),
('06 / 06',905,1370,11,500,100,GREY)]
for s,x,y,sz,wt,wd,c in frag: b+=T(s,x,y,sz,wt,wd,(PAPER if c==INK else c),1.0,'white-space: nowrap'+('; mix-blend-mode: difference' if c==INK else ''))
poster('PS06Collage.dc.html','Ylli Poster 06 — Not an answer',b,bt='Poster 06 — NOT AN ANSWER.')

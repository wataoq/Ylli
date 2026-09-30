from bx.common import *
def divider(fname,p,nm,bt):
    b=f'<div class="a m" style="left: {COL[2]}px; top: 250px; font-size: 44px; line-height: 60px; color: {W}">{p}<br>{nm}</div>'
    b+=svg('mark',COL[7]-10,-10,h=1100,fill='#141414')
    page(fname,f'Ylli {p}',b,bg=K,fg=W,board_title=bt,part='B')
divider('BXB00Divider.dc.html','Part B','BX Design Elements','Part B — BX Design Elements')
H=lambda sec,nm,i,fg=K: header('Part B','BX Design Elements',sec,nm,i,fg=fg)
CX0=COL[2]; CX1=1864; CY0=196; CY1=1024
# ---- Overview ----
b=H('','Overview',1)
b+=desc('Design Elements Overview','Ylliのアイデンティティを構成する六つの資産。すべての要素は「45°に構えた一本の平筆」という同じ規則から生まれています。線の太さは線そのものではなく、ペンに対する向き＝関係で決まる。')
tiles=[('Logo',lambda x,y:sig_h(x+20,y+20,260)),
('Color',lambda x,y:''.join(f'<div class="a" style="left: {x+20+i*48}px; top: {y+20}px; width: 40px; height: 260px; background: {c}; {"box-shadow: inset 0 0 0 1px "+RULE if c==W else ""}"></div>' for i,c in enumerate([K,W,S,B]))),
('Typography',lambda x,y:f'<div class="a m" style="left: {x+20}px; top: {y+10}px; font-size: 58px; line-height: 78px">玄あい<br>AaBb<br>123</div>'),
('Key Visual',lambda x,y:kvA(x,y,420,300,0.9,mark='hang1',mark_at=2)),
('Iconography',lambda x,y:''.join(icon(n,x+20+i*80,y+40,56) for i,n in enumerate(['bag','hanger','arrow','close']))),
('Photography',lambda x,y:f'<div class="a" style="left: {x}px; top: {y}px; width: 420px; height: 300px; background: #2A2926"></div><div class="a" style="left: {x+230}px; top: {y}px; width: 120px; height: 300px; background: #3B3935"></div><div class="lb a" style="left: {x+16}px; top: {y+270}px; color: {S}">低照度・縦位置・身体は画面の外へ</div>')]
for i,(nm,fn) in enumerate(tiles):
    x=COL[2+(i%3)*2]; y=196+(i//3)*420
    b+=f'<div class="a m" style="left: {x}px; top: {y}px; font-size: 13px">{nm}</div>'
    b+=f'<div class="a" style="left: {x}px; top: {y+36}px; width: 420px; height: 300px; overflow: hidden">'+fn(0,0).replace('class="a" style="left: 0px; top: 0px','class="a" style="left: 0px; top: 0px')+'</div>'
page('BXB01Overview.dc.html','Ylli B Overview',b,board_title='B Overview',part='B')
# ---- B.1.1 Signature ----
b=H('B.1','Logo System — Signature',2)
b+=desc('Brand Logo','Ylliのロゴは、シンボルとワードマークで構成されます。どちらも45°に構えた同じ一本の平筆で書かれ、機械的な等幅の線を持ちません。<br><br>ワードマークはシンボルの短い脚の先端に下端を揃えて置きます。届かなかった脚の高さに、名前が吊られます。')
hh=640; sw=sig_h_w(hh)
b+=sig_h((CX0+CX1)/2-sw/2,250,hh)
page('BXB11Signature.dc.html','Ylli B.1 Signature',b,board_title='B.1 Logo — Signature',part='B')
# ---- B.1.2 Concept ----
b=H('B.1','Logo System — Concept',3)
b+=desc('太さは、向きが決める','P3までのマークは「糸が撚られる」様子を描いていました。v1.0では何かを描くことをやめ、書く規則だけを残します。<br><br>45°に傾けた平筆で書くと、縦の線は0.71、右下がりの線は1.00、右上がりの線はほとんど消える髪の線になります。同じ一本のペンから、太い線と消えそうな線が生まれる。太さは線の性質ではなく、ペンとの関係で決まる — 自己が固定された像ではなく、関係によって揺れ続けるように。')
ox=CX0; oy=260; sc=3.2
b+=f'<div class="a" style="left: {ox}px; top: {oy}px; width: 150px; height: 150px"><svg class="a" style="left: 30px; top: 30px; width: 90px; height: 90px" viewBox="-10 -10 20 20"><polygon points="-8,8 8,-8 8.6,-7.4 -7.4,8.6" fill="{K}"/></svg></div>'
b+=f'<div class="lb a" style="left: {ox}px; top: {oy+160}px; width: 160px; color: {T3}">ペン先　幅 L・角度 45°</div>'
for j,(nm,lab) in enumerate([('nib_v','縦　0.71 L'),('nib_d1','右下がり　1.00 L'),('nib_d2','右上がり　≒ 0（髪）'),('nib_h','横　0.71 L')]):
    x=ox+200+j*190
    b+=svg(nm,x,oy+20,h=P[nm]['h']*sc if P[nm]['h']*sc<=200 else 200)
    b+=f'<div class="lb a" style="left: {x}px; top: {oy+240}px; color: {T3}">{lab}</div>'
y2=620
pts=[('一度だけ交わる','右下がりの太い線が、消えかけた髪の線の上を一度だけ横切る。重なりに切れ目はない。'),('片方は地面に届かない','左の脚は右より短く終わる。落ちてもいないし、着地もしていない。「懸」の状態。'),('縦に吊る','上端から吊られ、下へ伸びる力だけを持つ。大きさが変わるとき、伸びるのは脚だけ。')]
for i,(t,c) in enumerate(pts):
    x=CX0+i*460
    b+=f'<div class="a" style="left: {x}px; top: {y2}px; width: 420px; border-top: 1px solid {K}; padding-top: 16px"><div class="m" style="font-size: 22px; line-height: 34px">{t}</div><div class="m" style="font-size: 14px; line-height: 26px; color: {T2}; margin-top: 10px">{c}</div></div>'
page('BXB12Concept.dc.html','Ylli B.1 Concept',b,board_title='B.1 Logo — Concept',part='B')
# ---- B.1.3 Construction ----
b=H('B.1','Logo System — Construction',4)
b+=desc('Construction','すべての寸法はペン幅 L を単位とします。自由曲線は使わず、直線と半径 1.1 L の角丸のみで構成します。<br><br>L = ペン幅（角度 45°）<br>上端の脚　1.1 L<br>二本の間隔　2.9 L<br>交差の高さ　2.9 L<br>長い脚　8.1 L<br>短い脚　5.6 L')
mh=780; s=mh/P['mark']['h']; mx=COL[3]+80; my=220
U=lambda v: my+(v+5.657)*s
X=lambda v: mx+(v+5.657)*s
for yy,lab in [(0,'上端'),(18,'1.1 L'),(64,'交差 2.9 L'),(154,'短い脚 5.6 L'),(194,'長い脚 8.1 L')]:
    b+=f'<div class="a" style="left: {COL[3]}px; top: {f(U(yy))}px; width: 900px; border-top: 1px dashed {S}"></div><div class="lb a" style="left: {COL[6]+40}px; top: {f(U(yy)-18)}px; color: {T3}">{lab}</div>'
for xx in [0,46]:
    b+=f'<div class="a" style="left: {f(X(xx))}px; top: {my-20}px; height: {mh+40}px; border-left: 1px dashed {S}"></div>'
b+=svg('mark',mx,my,h=mh)
b+=f'<div class="lb a" style="left: {f(X(0))}px; top: {my+mh+26}px; width: {f(46*s)}px; text-align: center; color: {T3}">2.9 L</div>'
page('BXB13Construction.dc.html','Ylli B.1 Construction',b,board_title='B.1 Logo — Construction',part='B')
# ---- B.1.4 Types ----
b=H('B.1','Logo System — Logo Types',5)
b+=desc('Logo Types','四つの組み合わせを用意します。シンボル単体を基本とし、名前を伝える必要がある接点でのみワードマークを添えます。')
tl=[('Symbol　シンボル',lambda x,y: svg('mark',x+180,y+50,h=300)),
('Wordmark　ワードマーク',lambda x,y: svg('word',x+120,y+150,h=110)),
('Signature — Horizontal',lambda x,y: sig_h(x+130,y+60,280)),
('Signature — Vertical',lambda x,y: sig_v(x+330,y+30,220))]
for i,(nm,fn) in enumerate(tl):
    x=CX0+(i%2)*690; y=196+(i//2)*410
    b+=f'<div class="a" style="left: {x}px; top: {y}px; width: 660px; height: 380px; background: {GROUND}"></div>'+fn(x,y)
    b+=f'<div class="lb a" style="left: {x+16}px; top: {y+350}px; color: {T3}">{nm}</div>'
page('BXB14Types.dc.html','Ylli B.1 Types',b,board_title='B.1 Logo — Types',part='B')
# ---- B.1.5 Suspension ----
b=H('B.1','Logo System — Suspension',6)
b+=desc('交わりは一度だけ。<br>変わるのは、吊りの長さ。','旧案の「撚りの回数 k」は廃止します。交差はどの大きさでも一度だけ。面が縦に長くなるほど、脚だけが長く垂れ下がります。<br><br>シンボルは常に面の上端から吊り、下端には着けません。')
fr=[('Icon 1:1','mark',160,160,120),('Card 91×55','hang1',180,110,96),('Poster B2','hang2',300,424,370),('Banner 1:4','hang3',150,600,560),('Signage 1:8','hang4',110,800,760)]
x=CX0
for nm,mk,w,h,mhh in fr:
    y=196
    bgc=K if nm.startswith(('Poster','Signage')) else (B if nm.startswith('Banner') else GROUND)
    fg=W if bgc!=GROUND else K
    b+=f'<div class="a" style="left: {x}px; top: {y}px; width: {w}px; height: {h}px; background: {bgc}; overflow: hidden">'
    mw,_=size(mk,h=mhh)
    b+=svg(mk,(w-mw)/2 if not nm.startswith('Card') else 24,-4 if not nm.startswith('Icon') else 20,h=mhh,fill=fg)
    b+='</div>'
    b+=f'<div class="lb a" style="left: {x}px; top: {y+h+14}px; color: {T3}">{nm}<br>{mk}</div>'
    x+=w+40
page('BXB15Suspension.dc.html','Ylli B.1 Suspension',b,board_title='B.1 Logo — Suspension',part='B')
# ---- B.1.6 Clear space / min ----
b=H('B.1','Logo System — Clear Space / Minimum Size',7)
b+=desc('Clear Space','シンボルの周囲には、二本の間隔（2.9 L）と同じ余白を確保します。上端だけは例外で、面の端に接してよい（吊る）。<br><br>Minimum Size<br>髪の線が消えることは許容します（不在）。ただし太い線と脚の長短が読める大きさを最小とします。')
mh=520; s=mh/P['mark']['h']; mx=CX0+200; my=260; pad=46*s
b+=f'<div class="a" style="left: {f(mx-pad)}px; top: {f(my-pad)}px; width: {f(P["mark"]["w"]*s+2*pad)}px; height: {f(mh+2*pad)}px; border: 1px dashed {S}"></div>'
b+=f'<div class="a" style="left: {f(mx)}px; top: {f(my)}px; width: {f(P["mark"]["w"]*s)}px; height: {f(mh)}px; background: {GROUND}"></div>'
b+=svg('mark',mx,my,h=mh)
b+=f'<div class="lb a" style="left: {f(mx-pad)}px; top: {f(my+mh+pad+12)}px; color: {T3}">余白 = 2.9 L</div>'
mins=[('Symbol','mark',60,'印刷 10 mm／画面 48 px'),('Wordmark','word',22,'印刷 3 mm／画面 16 px'),('Signature','sig',40,'印刷 8 mm／画面 40 px')]
x=COL[5]
for i,(nm,mk,hh,t) in enumerate(mins):
    y=260+i*180
    b+=f'<div class="a" style="left: {x}px; top: {y-20}px; width: 660px; border-top: 1px solid {K}"></div>'
    b+=(sig_h(x,y,hh) if mk=='sig' else svg(mk,x,y,h=hh))
    b+=f'<div class="a m" style="left: {x+260}px; top: {y}px; font-size: 16px">{nm}<div style="font-size: 13px; color: {T2}; margin-top: 8px">{t}</div></div>'
page('BXB16ClearSpace.dc.html','Ylli B.1 Clear Space',b,board_title='B.1 Logo — Clear Space / Min',part='B')
# ---- B.1.7 Color & misuse ----
b=H('B.1','Logo System — Color / Misuse',8)
b+=desc('Color Variation','玄の上に素、素の上に玄を基本とします。深青の地は一つの面に一度だけ。鈍の地には置きません。')
cv=[(W,K,'玄 on 素'),(K,W,'素 on 玄'),(B,W,'素 on 深青')]
for i,(bg,fg,l) in enumerate(cv):
    x=CX0+i*460
    b+=f'<div class="a" style="left: {x}px; top: 196px; width: 420px; height: 380px; background: {bg}; {"box-shadow: inset 0 0 0 1px "+RULE if bg==W else ""}; overflow: hidden">'+svg('hang1',184,-4,h=300,fill=fg)+'</div>'
    b+=f'<div class="lb a" style="left: {x}px; top: 590px; color: {T3}">{l}</div>'
ng=[('縦横比を変える','<g transform="scale(1.9,0.75)">'),('回転・横倒し','<g transform="translate(40,40) rotate(-90 30 60)">'),('単線（等幅）に置き換える',None),('鈍の地・低コントラスト','S')]
for i,(l,tf) in enumerate(ng):
    x=CX0+i*345; y=660
    bgc=S if tf=='S' else GROUND
    inner=''
    p=P['mark']
    if tf and tf!='S': inner=f'<svg class="a" style="left: 0; top: 0; width: 320px; height: 250px" viewBox="-60 -20 260 210">{tf}<path d="{p["d"]}" fill="{K}"/></g></svg>'
    elif tf=='S': inner=svg('mark',130,30,h=190,fill='#6E6B64')
    else: inner='<svg class="a" style="left: 0; top: 0; width: 320px; height: 250px" viewBox="-60 -20 180 210"><path d="M0 0 V18 L46 64 V194 M46 0 V18 L0 64 V154" fill="none" stroke="#0A0A0A" stroke-width="10"/></svg>'
    b+=f'<div class="a" style="left: {x}px; top: {y}px; width: 320px; height: 250px; background: {bgc}; overflow: hidden">{inner}</div>'
    b+=f'<div class="lb a" style="left: {x}px; top: {y+262}px; color: {K}">NG　{l}</div>'
page('BXB17ColorMisuse.dc.html','Ylli B.1 Color Misuse',b,board_title='B.1 Logo — Color / Misuse',part='B')
# ---- B.2.1 Palette ----
b=H('B.2','Color System — Color Palette',9)
b+=desc('Color Palette','四色で構成します。名前はそれぞれの状態を指し、色相ではありません。<br><br>正確な色再現のため、印刷時は紙・インキ濃度を確認し、色校正で判断してください。PANTONEは参考値です。')
pal=[('玄','Gen','#0A0A0A','R10 G10 B10','C40 M30 Y30 K100（リッチブラック）','PANTONE Black 6 C（参考）',K,W),
('素','So','#F5F3EF','R245 G243 B239','紙の地色。インキを載せない','—',W,K),
('鈍','Nibi','#8A877F','R138 G135 B127','C45 M40 Y45 K5','PANTONE Warm Gray 8 C（参考）',S,K),
('深青','Shinsei','#1A2A4A','R26 G42 B74','C100 M85 Y40 K40','PANTONE 2767 C（参考）',B,W)]
for i,(nm,ro,hx,rgb,cmyk,pt,bg,fg) in enumerate(pal):
    x=CX0+i*345
    b+=f'<div class="a" style="left: {x}px; top: 196px; width: 320px; height: 560px; background: {bg}; {"box-shadow: inset 0 0 0 1px "+RULE if bg==W else ""}"><div class="m a" style="left: 20px; top: 20px; font-size: 40px; color: {fg}">{nm}</div><div class="m a" style="left: 20px; top: 80px; font-size: 13px; color: {fg}; opacity: 0.8">{ro}</div></div>'
    b+=f'<div class="a m" style="left: {x}px; top: 780px; width: 320px; font-size: 13px; line-height: 24px">{hx}<br>{rgb}<br>{cmyk}<br><span style="color: {T3}">{pt}</span></div>'
page('BXB21Palette.dc.html','Ylli B.2 Palette',b,board_title='B.2 Color — Palette',part='B')
# ---- B.2.2 Ratio ----
b=H('B.2','Color System — Ratio / Rules',10)
b+=desc('Ratio','素が面をつくり、玄が線と重さを持ちます。鈍は写真と紙の受けに。深青は「不在に気づけ」の色であり、一つの面に一度だけ、小さく現れます。')
b+=f'<div class="a" style="left: {CX0}px; top: 196px; width: 1348px; height: 120px; display: flex"><div style="width: 62%; background: {W}; box-shadow: inset 0 0 0 1px {RULE}"></div><div style="width: 30%; background: {K}"></div><div style="width: 6%; background: {S}"></div><div style="width: 2%; background: {B}"></div></div>'
b+=f'<div class="lb a" style="left: {CX0}px; top: 328px; width: 1348px; display: flex; color: {T3}"><span style="width: 62%">素 62</span><span style="width: 30%">玄 30</span><span style="width: 6%">鈍 6</span><span style="width: 2%">深青 2</span></div>'
rules=[('深青は一面に一度','ポスターなら一点、名刺なら裏面の一辺、ウェブなら一つのリンク色だけ。二度使わない。'),('深青は見えない場所へ','衣服では裏地・内タグなど、着た人にしか見えない位置に。グラフィックでも、手に取って初めて気づく位置（封筒の内側、箱の底）を優先する。'),('グラデーション・透明度は使わない','色は常に不透明の平面。重ねるときは切れ目ではなく、上下関係（太い線が上）で示す。')]
for i,(t,c) in enumerate(rules):
    x=CX0+i*460
    b+=f'<div class="a" style="left: {x}px; top: 440px; width: 420px; border-top: 1px solid {K}; padding-top: 16px"><div class="m" style="font-size: 20px; line-height: 32px">{t}</div><div class="m" style="font-size: 14px; line-height: 26px; color: {T2}; margin-top: 10px">{c}</div></div>'
b+=f'<div class="a" style="left: {CX0}px; top: 720px; width: 420px; height: 260px; background: {W}; box-shadow: inset 0 0 0 1px {RULE}">'+svg('hang1',30,-4,h=250)+f'<div class="a" style="left: 380px; top: 0; width: 40px; height: 4px; background: {B}"></div></div>'
b+=f'<div class="a" style="left: {CX0+460}px; top: 720px; width: 420px; height: 260px; background: {K}">'+svg('hang1',30,-4,h=250,fill=W)+f'<div class="a" style="left: 0; bottom: 0; width: 420px; height: 6px; background: {B}"></div></div>'
page('BXB22Ratio.dc.html','Ylli B.2 Ratio',b,board_title='B.2 Color — Ratio / Rules',part='B')
# ---- B.3 Typography ----
b=H('B.3','Typography — Japanese',11)
b+=desc('Japanese Typeface<br>Noto Serif JP','和文・欧文ともに Noto Serif JP を指定書体とします。ハネやウロコを持つ明朝体は、ロゴの平筆と同じく「書かれた線」の抑揚を持ち、等幅的なデジタルの印象を避けられます。<br><br>見出しは Medium 500、本文は Regular 400、長い引用は Light 300。')
b+=f'<div class="a m" style="left: {CX0}px; top: 180px; font-size: 96px; line-height: 132px; font-weight: 400">玄に在ること<br>宙吊り　不在　意味</div>'
b+=f'<div class="a m" style="left: {CX0}px; top: 480px; font-size: 44px; line-height: 70px; font-weight: 300; color: {T2}">あいうえおかきくけこさしすせそ<br>アイウエオカキクケコサシスセソ<br>永流懸玄素鈍深青撚糸衣服</div>'
b+=f'<div class="a" style="left: {CX0}px; top: 760px; width: 1348px; display: flex; gap: 40px">'+''.join(f'<div class="m" style="font-weight: {w}; font-size: 30px">{w}<div class="lb" style="color: {T3}; margin-top: 6px">{nm}</div></div>' for w,nm in [(300,'Light'),(400,'Regular'),(500,'Medium'),(600,'SemiBold')])+'</div>'
page('BXB31TypeJP.dc.html','Ylli B.3 Type JP',b,board_title='B.3 Typography — Japanese',part='B')
b=H('B.3','Typography — Latin',12)
b+=desc('Latin Typeface<br>Noto Serif JP (Latin)','欧文も同じ書体の欧文部分を使い、和欧の間で線の抑揚を揃えます。ブランド名は必ずワードマークで表記し、書体で「Ylli」と組むのは本文中のみとします。')
b+=f'<div class="a m" style="left: {CX0}px; top: 180px; font-size: 92px; line-height: 118px">ABCDEFGHIJKLMNOP<br>QRSTUVWXYZ<br>abcdefghijklmnopq<br>rstuvwxyz<br>1234567890 .,;:?!%<br>()&amp;©™®¾½</div>'
page('BXB32TypeLatin.dc.html','Ylli B.3 Type Latin',b,board_title='B.3 Typography — Latin',part='B')
b=H('B.3','Typography — Hierarchy',13)
b+=desc('Hierarchy / Functional','文字は上端から吊るように、左揃え・上揃えで組みます。中央揃えはワードマークのみ。<br><br>フォーム・価格・注意書きなど機能的な小さい文字には Noto Sans JP を補助書体として使います。等幅書体は使いません。')
hier=[('Display','Noto Serif JP 500　96 / 120','意味を待て',96,500,'m'),('Heading','Noto Serif JP 500　40 / 56','宙吊りの中に在り続けるための衣服',40,500,'m'),('Body','Noto Serif JP 400　15 / 30','答えが出ないまま問いの中にとどまることを可能にする衣服である。',15,400,'m'),('Caption','Noto Sans JP 400　11 / 16　字間 0.04em','価格は税込です。交換・返品は到着後 14 日以内に承ります。',11,400,'s')]
y=196
for nm,spec,t,sz,wt,cl in hier:
    b+=f'<div class="a" style="left: {CX0}px; top: {y}px; width: 1348px; border-top: 1px solid {K}"></div><div class="a lb" style="left: {CX0}px; top: {y+14}px; width: 220px; color: {T3}">{nm}<br>{spec}</div>'
    b+=f'<div class="a {cl}" style="left: {CX0+300}px; top: {y+10}px; font-size: {sz}px; font-weight: {wt}; line-height: 1.3; width: 1040px">{t}</div>'
    y+= max(100,int(sz*1.4)+60)
page('BXB33TypeHier.dc.html','Ylli B.3 Type Hierarchy',b,board_title='B.3 Typography — Hierarchy',part='B')
# ---- B.4 Key Visual ----
b=H('B.4','Key Visual — Overview',14)
b+=desc('Key Visual Overview','キービジュアルは三つのタイプを持ち、接点と環境に応じて選びます。いずれもシンボルの規則（45°の平筆・一度の交差・吊り）から取り出したもので、糸や撚りを描写しません。')
kv=[('Type A　懸 Suspension','上端から吊られた縦線の列。長さだけが違い、その中に一度だけ交差（シンボル）が現れる。',lambda x,y:kvA(x,y,420,560,1.0,mark='hang2',mark_at=3)),
('Type B　交 Crossing','交差の一点だけを大きく切り取る。太い線と、消えかけた髪の線。',lambda x,y:kvB(x,y,420,560,zoom=0.9)),
('Type C　不在 Absence','交差だけを抜いたシンボル。何が起きたかは描かず、前と後だけを残す。',lambda x,y:kvC(x,y,420,560,hname='absent2'))]
for i,(t,c,fn) in enumerate(kv):
    x=CX0+i*460
    b+=f'<div class="a" style="left: {x}px; top: 196px; width: 420px; height: 560px; background: {GROUND}; overflow: hidden">'+fn(0,0)+'</div>'
    b+=f'<div class="a m" style="left: {x}px; top: 780px; width: 420px"><div style="font-size: 18px">{t}</div><div style="font-size: 13px; line-height: 24px; color: {T2}; margin-top: 8px">{c}</div></div>'
page('BXB41KVOverview.dc.html','Ylli B.4 Key Visual',b,board_title='B.4 Key Visual — Overview',part='B')
def kvpage(fn,sec_i,t,nm,desc_t,desc_b,items,bt):
    b=H('B.4',nm,sec_i)+desc(desc_t,desc_b)
    for (x,y,w,h,bg,draw,lab,txt,tfg) in items:
        b+=f'<div class="a sh" style="left: {x}px; top: {y}px; width: {w}px; height: {h}px; background: {bg}; overflow: hidden">'+draw(w,h)+(txt or '')+'</div>'
        if lab: b+=f'<div class="lb a" style="left: {x}px; top: {y+h+12}px; color: {T3}">{lab}</div>'
    page(fn,t,b,board_title=bt,part='B')
tx=lambda s,fg,x=28,y=28,sz=22: f'<div class="a m" style="left: {x}px; top: {y}px; font-size: {sz}px; line-height: 1.5; color: {fg}">{s}</div>'
kvpage('BXB42KVA.dc.html',15,'Ylli B.4 Type A','Key Visual — Type A　懸','Type A　懸 Suspension','縦線は常に上端より上から始まり、面の中で終わる。長さの比は 0.55〜1.0 の範囲で、同じ長さを隣に並べない。シンボルは列の中に一度だけ、左右の余白の広い側に置く。<br><br>用途：ポスター、ショッパー、包装紙、ウェブのヒーロー。',
 [(CX0,196,440,622,K,lambda w,h:kvA(0,0,w,h,1.25,fill=W,mark='hang2',mark_at=2),'Poster B2　玄',tx('意味を待て',W,28,540,24),W),
  (CX0+480,196,440,622,W,lambda w,h:kvA(0,0,w,h,1.25,fill=K,mark='hang2',mark_at=1,offset=10),'Poster B2　素',tx('Collection 01',K,28,560,15),K),
  (CX0+960,196,388,622,B,lambda w,h:kvA(0,0,w,h,1.25,fill=W,mark='hang2',mark_at=1),'Poster B2　深青（一度）',None,W)],'B.4 Key Visual — Type A 懸')
kvpage('BXB43KVB.dc.html',16,'Ylli B.4 Type B','Key Visual — Type B　交','Type B　交 Crossing','交差の中心を面の中心よりわずかに上に置き、太い線は必ず面の外へ抜ける。髪の線が消えて見える大きさまで拡大してよい。文字は交差の外側の余白に。<br><br>用途：名刺裏、ギフトボックス天面、SNS、ラベル。',
 [(CX0,196,622,622,W,lambda w,h:kvB(0,0,w,h,zoom=1.0),'1:1',None,K),(CX0+660,196,340,622,K,lambda w,h:kvB(0,0,w,h,fill=W,zoom=0.7),'9:16',None,W),(CX0+1040,196,308,622,S,lambda w,h:kvB(0,0,w,h,fill=K,zoom=1.6),'写真の受け（鈍）',None,K)],'B.4 Key Visual — Type B 交')
kvpage('BXB44KVC.dc.html',17,'Ylli B.4 Type C','Key Visual — Type C　不在','Type C　不在 Absence','シンボルから交差だけを抜く。抜いた場所は説明せず、余白として残す。コピーを置く場合は抜いた高さに一行だけ。<br><br>用途：シーズンの告知、展示、キャンペーンの最初の一枚。',
 [(CX0,196,440,622,W,lambda w,h:kvC(0,0,w,h,hname='absent2'),'Poster　素',None,K),(CX0+480,196,440,622,K,lambda w,h:kvC(0,0,w,h,fill=W,hname='absent2'),'Poster　玄',tx('何が起きたかは、<br>書かない。',W,26,58,14),W),(CX0+960,196,388,622,GROUND,lambda w,h:kvC(0,0,w,h,hname='absent3'),'Banner',None,K)],'B.4 Key Visual — Type C 不在')
# ---- B.5 Iconography ----
b=H('B.5','Iconography',18)
b+=desc('Iconography','アイコンもロゴと同じ45°の平筆（24 px グリッドで L = 2.3）で書きます。縦横の線は同じ太さ、右下がりは太く、右上がりは髪の線に。角丸・塗りつぶし・影は使いません。<br><br>最小 16 px。ラベルは Noto Sans JP 11 px。')
names=[('home','ホーム'),('search','検索'),('bag','カート'),('account','アカウント'),('menu','メニュー'),('close','閉じる'),('arrow','進む'),('plus','追加'),('hanger','商品'),('store','店舗')]
for i,(nm,lab) in enumerate(names):
    x=CX0+(i%5)*270; y=210+(i//5)*330
    b+=f'<div class="a" style="left: {x}px; top: {y}px; width: 230px; height: 230px; background: {GROUND}"></div>'+icon(nm,x+35,y+35,160)
    b+=f'<div class="lb a" style="left: {x}px; top: {y+244}px; color: {T3}">{lab}　{nm}</div>'
b+=f'<div class="a" style="left: {CX0}px; top: 880px; display: flex; gap: 36px; align-items: center">'+''.join(icon(nm,0,0,24).replace('class="a" style="left: 0px; top: 0px; ','style="') for nm,_ in names)+f'<span class="lb" style="color: {T3}">24 px</span></div>'
page('BXB51Icons.dc.html','Ylli B.5 Iconography',b,board_title='B.5 Iconography（10）',part='B')
# ---- B.6 Photography ----
b=H('B.6','Photography',19)
b+=desc('Photography Direction','写真は「確定した像」を返さないように撮ります。<br><br>1　縦位置のみ。身体は画面の上下で切れる<br>2　低照度。影の中に形がある（玄）<br>3　顔を正面から写さない<br>4　背景は素・鈍・壁の地。小物で説明しない<br>5　ロゴは写真の上に置かない。余白側へ')
ph=[('低照度の布の重なり','#1E1D1B','#34322E'),('肩から下、画面の外へ','#2B2A27','#4A4843'),('素の壁に落ちる影','#D9D5CD','#BEB9AF'),('手と袖口、動きの途中','#3A3833','#5C5952')]
for i,(cap,c1,c2) in enumerate(ph):
    x=CX0+i*345
    b+=f'<div class="a" style="left: {x}px; top: 196px; width: 320px; height: 560px; background: linear-gradient(180deg,{c1},{c2})"></div>'
    b+=f'<div class="a" style="left: {x}px; top: 196px; width: 320px; height: 560px; background: linear-gradient(to top right, transparent calc(50% - 0.5px), rgba(138,135,127,0.5) 50%, transparent calc(50% + 0.5px))"></div>'
    b+=f'<div class="lb a" style="left: {x}px; top: 770px; color: {T3}">PHOTO {i+1:02d}　{cap}</div>'
b+=f'<div class="a m" style="left: {CX0}px; top: 850px; width: 1348px; font-size: 13px; line-height: 24px; color: {T2}; border-top: 1px solid {K}; padding-top: 14px">NG　明るい均一なライティング／全身の正面カット／ロゴの上に写真を重ねる／糸・織機・撚りなど素材を説明するカット</div>'
page('BXB61Photo.dc.html','Ylli B.6 Photography',b,board_title='B.6 Photography',part='B')

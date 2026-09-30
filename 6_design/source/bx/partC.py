from bx.common import *
b=f'<div class="a m" style="left: {COL[2]}px; top: 250px; font-size: 44px; line-height: 60px; color: {W}">Part C<br>BX Design Application</div>'
b+=svg('mark',COL[7]-10,-10,h=1100,fill='#141414')
page('BXC00Divider.dc.html','Ylli Part C',b,bg=K,fg=W,board_title='Part C — BX Design Application',part='C')
H=lambda sec,nm,i: header('Part C','BX Design Application',sec,nm,i)
CX0=COL[2]
GR=f'background: {GROUND}'
def box(x,y,w,h,bg=W,inner='',extra='',cls='card sh'):
    return f'<div class="{cls}" style="left: {f(x)}px; top: {f(y)}px; width: {f(w)}px; height: {f(h)}px; background: {bg}; {extra}">{inner}</div>'
def t(s,x,y,sz=12,fg=K,cls='m',extra=''):
    return f'<div class="a {cls}" style="left: {f(x)}px; top: {f(y)}px; font-size: {sz}px; line-height: 1.6; color: {fg}; {extra}">{s}</div>'
def spec(items,y=620):
    return f'<div class="ds" style="left: {COL[0]}px; top: {y}px; width: 428px; font-size: 13px; line-height: 24px; color: {T2}">'+''.join(f'<div style="border-top: 1px solid {RULE}; padding: 8px 0; display: flex"><span style="width: 110px; color: {K}">{a}</span><span style="flex: 1">{c}</span></div>' for a,c in items)+'</div>'
def stage(inner): return f'<div class="a" style="left: {CX0}px; top: 150px; width: 1348px; height: 880px; {GR}">{inner}</div>'
# C.1 Business card 91x55 (x5)
s=5; cw,ch=91*s,55*s
front=svg('hang1',28,-4,h=ch+4)+t('[氏名]',200,40,18)+t('[肩書き]',200,72,11,T3)+t('[mail]<br>[tel]<br>ylli.[domain]',200,200,10,K,'s')
back=kvB(0,0,cw,ch,fill=W,zoom=0.75)+f'<div class="a" style="left: 0; bottom: 0; width: {cw}px; height: 5px; background: {B}"></div>'
inner=box(150,160,cw,ch,W,front)+box(740,160,cw,ch,K,back)+box(150,520,cw,ch,W,front,'transform: rotate(-4deg)')+box(740,520,cw,ch,K,kvA(0,0,cw,ch,0.55,fill=W,mark='hang1',mark_at=2))
b=H('C.1','Business Card',1)+desc('Business Card','表はシンボルを紙の上端から吊り、情報は短い脚の右側に。裏は玄の地に交差（Type B）または懸（Type A）。深青は裏面の下辺に一本だけ。')+spec([('Format','91 × 55 mm'),('Paper','非塗工 ラフ紙 350 g/㎡（素）'),('Print','活版 墨1色／裏 深青 1辺'),('Type','Noto Serif JP 18 / 11 pt・Noto Sans JP 7 pt')])+stage(inner)
page('BXC01Card.dc.html','Ylli C.1 Business Card',b,board_title='C.1 Business Card',part='C')
# C.2 ID card 54x86 (x5)
s=5; iw,ih=54*s,86*s
idf=svg('hang1',24,-4,h=250)+f'<div class="a" style="left: 130px; top: 40px; width: 110px; height: 140px; background: {S}"></div>'+t('[氏名]',130,200,16)+t('[所属]',130,228,10,T3)+t('ID 000000',24,390,10,T3,'s')
idb=kvC(0,0,iw,ih,fill=W,hname='absent2')+t('拾得された方は下記までご連絡ください<br>[連絡先]',24,380,8,S,'s')
slot=lambda x: f'<div class="a" style="left: {x+iw/2-30}px; top: 196px; width: 60px; height: 8px; border-radius: 4px; background: {GROUND}; box-shadow: inset 0 0 0 1px {RULE}"></div>'
inner=box(240,210,iw,ih,W,idf)+box(620,210,iw,ih,K,idb)+f'<div class="a" style="left: {240+iw/2-8}px; top: 0; width: 16px; height: 212px; background: {B}"></div><div class="a" style="left: {620+iw/2-8}px; top: 0; width: 16px; height: 212px; background: {B}"></div>'
b=H('C.2','Identification Card',2)+desc('Identification Card','社員証も上端から吊られる。ストラップは深青 — 身につけたとき、本人には見えない首の後ろに色が回る。')+spec([('Format','54 × 86 mm（縦）'),('Material','PVC マット／表 素・裏 玄'),('Strap','深青 15 mm 綾織'),('Photo','鈍の地、無表情・正面から少し外す')])+stage(inner)
page('BXC02ID.dc.html','Ylli C.2 ID Card',b,board_title='C.2 Identification Card',part='C')
# C.3 Envelopes
s=1.35; ew,eh=240*s,332*s
big=svg('hang2',30,-4,h=eh*0.62)+t('Ylli',0,0,1,W)+t('[住所]<br>[社名]',ew-150,eh-80,10,T2,'s')+svg('word',ew-150,eh-120,h=26)
small_w,small_h=235*2,120*2
sm=svg('hang1',26,-4,h=small_h*0.8)+t('[宛名]',200,90,14)+t('〒 [郵便番号]',200,60,10,T3,'s')
flap=f'<div class="a" style="left: 0; top: 0; width: {small_w}px; height: 60px; background: {B}"></div>'
inner=box(120,140,ew,eh,W,big)+box(640,140,small_w,small_h,W,sm)+box(640,460,small_w,small_h,W,flap+t('内側 深青',16,72,10,T3,'s'),'')
b=H('C.3','Envelopes',3)+desc('Envelopes — L / S','角2と長3の二種。表は白い紙の上端からシンボルを吊る。深青は封を開けた人だけが見る、フラップの内側に刷る。')+spec([('Large','角2　240 × 332 mm'),('Small','長3　120 × 235 mm'),('Paper','非塗工 ラフ紙 100 g/㎡'),('Print','表 墨1色／内側 深青 ベタ')])+stage(inner)
page('BXC03Envelopes.dc.html','Ylli C.3 Envelopes',b,board_title='C.3 Envelopes（L / S）',part='C')
# C.4 Letterhead
s=2.3; lw,lh=210*s,297*s
lines=''.join(f'<div class="a" style="left: 120px; top: {200+i*18}px; width: {300 if i%6!=5 else 180}px; height: 3px; background: #E2DED6"></div>' for i,_ in enumerate(range(16)))
lt=svg('hang2',30,-4,h=lh*0.55)+t('[日付]<br>[宛名]',120,120,10,T2,'s')+lines+svg('word',lw-110,lh-60,h=24)+t('ylli.[domain]',120,lh-54,9,T3,'s')
inner=box(200,90,lw,lh,W,lt)+box(760,150,lw*0.9,lh*0.9,W,t('2枚目以降<br>シンボルなし',40,40,10,T3,'s')+''.join(f'<div class="a" style="left: 108px; top: {90+i*18}px; width: 300px; height: 3px; background: #E2DED6"></div>' for i in range(20)),'')
b=H('C.4','Letterhead',4)+desc('Letterhead A4','シンボルは左端から吊り、本文はその脚の右側、短い脚の終わる高さより下から始める。ワードマークは右下に一度だけ。')+spec([('Format','A4 210 × 297 mm'),('Margin','左 52 mm（脚の列）／上 30 mm'),('Body','Noto Serif JP 10 / 18 pt'),('Paper','非塗工 ラフ紙 90 g/㎡')])+stage(inner)
page('BXC04Letterhead.dc.html','Ylli C.4 Letterhead',b,board_title='C.4 Letterhead',part='C')
# C.5 Shopping bag
def bag(x,y,w,h,bg,fg,content,gus=60):
    handle=f'<svg class="a" style="left: {x+w*0.28}px; top: {y-110}px; width: {w*0.44}px; height: 120px" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M5 100 C5 10 95 10 95 100" fill="none" stroke="{fg if bg!=W else K}" stroke-width="2.4"/></svg>'
    side=f'<div class="a" style="left: {x+w}px; top: {y}px; width: {gus}px; height: {h}px; background: {bg}; filter: brightness(0.86)"></div>'
    return handle+box(x,y,w,h,bg,content,'','card')+side
bw,bh=360,470
inner=bag(170,230,bw,bh,K,W,kvA(0,0,bw,bh,0.95,fill=W,mark='hang2',mark_at=1)+svg('word',bw-120,bh-60,h=34,fill=W))
inner+=bag(700,300,300,390,W,K,svg('hang2',30,-4,h=330)+svg('word',200,340,h=26),50)
b=H('C.5','Shopping Bag',5)+desc('Shopping Bag','玄のバッグは Type A の縦線を全面に。持ち手は素の綿紐。素のバッグは小物用で、シンボルを上端から吊る。底マチの内側だけ深青。')+spec([('Size','L 360 × 470 × 120 mm／S 300 × 390 × 100 mm'),('Paper','玄 染め紙 180 g/㎡・素 未晒し 150 g/㎡'),('Print','素インキ 1色（L）／墨 1色（S）'),('Handle','綿紐 φ5 mm（素）')])+stage(inner)
page('BXC05Bag.dc.html','Ylli C.5 Shopping Bag',b,board_title='C.5 Shopping Bag',part='C')
# C.6 Gift box
gw=420
top=kvB(0,0,gw,gw,fill=W,zoom=0.8)
inner=box(160,150,gw,gw,K,top)+f'<div class="a" style="left: 160px; top: {150+gw}px; width: {gw}px; height: 60px; background: #1C1C1C"></div>'
inner+=box(700,210,520,340,W,f'<div class="a" style="left: 20px; top: 20px; width: 480px; height: 300px; background: {B}"></div><div class="a" style="left: 20px; top: 20px; width: 480px; height: 300px; background: repeating-linear-gradient(90deg, transparent 0 60px, rgba(245,243,239,0.08) 60px 61px)"></div>'+t('内側 深青の薄葉紙',24,300,10,W,'s'),'')
inner+=t('蓋（天面）',160,660,11,T3,'s')+t('開けたとき',700,570,11,T3,'s')
b=H('C.6','Gift Box',6)+desc('Gift Box','天面に交差（Type B）を大きく。箱を開けて初めて深青が現れる — 「不在に気づけ」を体験に置き換える。')+spec([('Size','300 × 300 × 45 mm（天地かぶせ）'),('Material','玄 染め貼箱／素 箔押し'),('Inner','深青 薄葉紙'),('Seal','素 丸シール Ø 30 mm（シンボル）')])+stage(inner)
page('BXC06GiftBox.dc.html','Ylli C.6 Gift Box',b,board_title='C.6 Gift Box',part='C')
# C.7 Paper label
s=4; tw,th=55*s,100*s
hole=f'<div class="a" style="left: {tw/2-7}px; top: 16px; width: 14px; height: 14px; border-radius: 7px; background: {GROUND}"></div>'
tag1=hole+svg('hang2',tw/2-35,40,h=260,fill=W)+t('Collection 01',20,th-70,10,S,'s')+t('[品番]　[サイズ]',20,th-50,10,S,'s')
tag2=hole+t('[品名]',20,50,16)+t('素材　[　　]<br>原産国　[　　]<br>[品番]',20,90,10,T2,'s')+t('¥ [価格]',20,th-60,18)+t('税込',20,th-32,9,T3,'s')
care=f'<div class="a" style="left: 0; top: 0; width: 120px; height: 3px; background: {B}"></div>'+svg('mark',20,20,h=110)+t('[組成]<br>[洗濯表示]',60,40,8,T2,'s')
inner=box(190,160,tw,th,K,tag1)+box(460,160,tw,th,W,tag2)+box(760,160,120,300,W,care)
inner+=f'<div class="a" style="left: {190+tw/2-1}px; top: 60px; width: 2px; height: 116px; background: {K}"></div><div class="a" style="left: {460+tw/2-1}px; top: 60px; width: 2px; height: 116px; background: {K}"></div>'
inner+=t('下げ札（表）',190,580,11,T3,'s')+t('下げ札（裏）',460,580,11,T3,'s')+t('ネームラベル<br>裏側に深青の一線',760,480,11,T3,'s')
b=H('C.7','Paper Label',7)+desc('Paper Label','下げ札はシンボルそのものを紙の形に。紐で上から吊られ、脚だけが長く垂れる。価格と組成は Noto Sans JP で機能的に。')+spec([('Hang tag','55 × 100 mm／玄 染め紙 400 g/㎡'),('Print','素インキ 1色'),('String','綿糸 素'),('Name label','織ネーム 20 × 50 mm')])+stage(inner)
page('BXC07Label.dc.html','Ylli C.7 Paper Label',b,board_title='C.7 Paper Label',part='C')
# C.8 Coupon
cw,ch=560,250
cp=kvC(0,0,200,ch,fill=W,hname='absent')+t('10%',230,60,48,W)+t('Collection 01 のご購入に',230,140,12,S,'s')+t('有効期限　[日付]　／　[コード]',230,200,10,S,'s')
perf=f'<div class="a" style="left: {cw-120}px; top: 0; width: 0; height: {ch}px; border-left: 1px dashed {S}"></div>'
cp+=perf+t('No.<br>0000',cw-100,90,11,S,'s')
inner=box(200,200,cw,ch,K,cp)+box(200,520,cw,ch,W,kvC(0,0,200,ch,hname='absent')+t('Invitation',230,60,32)+t('[会期]　[会場]',230,140,12,T2,'s')+perf.replace(S,RULE))
b=H('C.8','Coupon',8)+desc('Coupon','クーポンは Type C（不在）。割引の数字を大きく扱わず、交差の抜けた高さに一行だけ置く。ミシン目の右側は控え。')+spec([('Format','180 × 80 mm'),('Paper','玄 染め紙 250 g/㎡'),('Print','素インキ／ナンバリング'),('Variation','招待状（素）')])+stage(inner)
page('BXC08Coupon.dc.html','Ylli C.8 Coupon',b,board_title='C.8 Coupon',part='C')
# C.9 Exchange / Return form
s=2.3; fw,fh=210*s,297*s
rows=''.join(f'<div class="a s" style="left: 40px; top: {170+i*48}px; width: {fw-80}px; border-bottom: 1px solid {RULE}; font-size: 9px; color: {T3}; padding-bottom: 20px">{l}</div>' for i,l in enumerate(['ご注文番号','お名前','ご住所','お電話番号','商品名・品番','サイズ・カラー']))
chk=''.join(f'<div class="a s" style="left: 40px; top: {480+i*22}px; font-size: 9px; color: {K}">□　{l}</div>' for i,l in enumerate(['交換（サイズ違い）','返品（イメージ違い）','不良品','その他 [　　　　]']))
fm=svg('mark',40,-4,h=110)+t('交換・返品申込書',100,40,18)+t('Exchange / Return Form',100,70,10,T3,'s')+rows+chk+t('到着後 14 日以内に、本書を同封のうえご返送ください。',40,fh-60,9,T2,'s')+f'<div class="a" style="left: 0; bottom: 0; width: 40px; height: 4px; background: {B}"></div>'
inner=box(420,90,fw,fh,W,fm)
b=H('C.9','Exchange / Return Form',9)+desc('Exchange / Return Form','機能的な書類ほど、ブランドの抑制が伝わる。見出しだけを明朝に、記入欄と説明は Noto Sans JP。罫線は細く、枠で囲まない。')+spec([('Format','A4'),('Paper','上質 70 g/㎡'),('Print','墨 1色＋深青（左下 1点）'),('Type','見出し Noto Serif JP／本文 Noto Sans JP 9 pt')])+stage(inner)
page('BXC09Form.dc.html','Ylli C.9 Return Form',b,board_title='C.9 Exchange / Return Form',part='C')
# C.10 Horizontal banners
def hb(x,y,w,h,bg,fg,copy,sz=22):
    return box(x,y,w,h,bg,kvA(0,0,w*0.55,h,h/210*0.9,fill=fg,mark='hang1',mark_at=2,maxl=0.85)+t(copy,w*0.6,h*0.22,sz,fg)+svg('word',w-24-h*0.28*148/115,h-24-h*0.28,h=h*0.28,fill=fg),'','card')
inner=hb(60,60,1200,300,K,W,'意味を待て<br><span style="font-size: 14px; color: #8A877F">Collection 01　[日付]</span>',30)
inner+=hb(60,410,970,250,W,K,'太さは、向きが決める。',24)+hb(60,720,728,90,K,W,'Collection 01',14)
inner+=t('1200 × 300　ウェブ ヒーロー',60,370,11,T3,'s')+t('970 × 250',60,670,11,T3,'s')+t('728 × 90',60,820,11,T3,'s')
b=H('C.10','Banner — Horizontal',10)+desc('Horizontal Banner System','横長でも縦の力は変えない。Type A の縦線を左 55% に吊り、右側にコピーとワードマーク。バナーの高さが変わっても、縦線の本数と間隔の比は一定。')+spec([('Grid','左 55% 図／右 45% 文字'),('Copy','1行・Noto Serif JP'),('Logo','ワードマーク 右下・高さ 28%'),('Color','玄／素（深青は告知の1枚のみ）')])+stage(inner)
page('BXC10BannerH.dc.html','Ylli C.10 Banner Horizontal',b,board_title='C.10 Banner — Horizontal',part='C')
# C.11 Vertical banners
def vb(x,y,w,h,bg,fg,mk,copy=''):
    mw,_=size(mk,h=h*0.94)
    return box(x,y,w,h,bg,svg(mk,w*0.14,-4,h=h*0.94,fill=fg)+t(copy,w*0.14+mw+w*0.08,h*0.08,max(12,w/22),fg)+svg('word',w-w*0.1-w*0.3,h-w*0.1-w*0.3*115/148,w=w*0.3,fill=fg),'','card')
inner=vb(60,40,300,600,K,W,'hang3','意味を<br>待て')+vb(400,40,160,600,W,K,'hang3')+vb(600,40,338,600,B,W,'hang3','Collection<br>01')+vb(980,40,300,540,W,K,'hang2','一度だけ')
inner+=t('300 × 600',60,660,11,T3,'s')+t('160 × 600',400,660,11,T3,'s')+t('1080 × 1920 ストーリーズ（深青・告知）',600,660,11,T3,'s')+t('店頭 垂れ幕 900 × 1600',980,600,11,T3,'s')
b=H('C.11','Banner — Vertical',11)+desc('Vertical Banner System','縦長の面ではシンボルの脚を伸ばす（B.1 Suspension）。交差はいつも一度、上端近くに。コピーは脚の間ではなく右の余白の上部に。')+spec([('Mark','hang2〜hang4 を面の高さで選ぶ'),('Top','上端に接して吊る'),('Bottom','下端から 6% 以上離す'),('Copy','右上・最大2行')])+stage(inner)
page('BXC11BannerV.dc.html','Ylli C.11 Banner Vertical',b,board_title='C.11 Banner — Vertical',part='C')
# C.12 Website main
def browser(x,y,w,h,content):
    bar=f'<div class="a" style="left: 0; top: 0; width: {w}px; height: 28px; background: #DAD6CE"></div>'+''.join(f'<div class="a" style="left: {12+i*16}px; top: 10px; width: 8px; height: 8px; border-radius: 4px; background: #B5B0A6"></div>' for i in range(3))
    return box(x,y,w,h,W,bar+f'<div class="a" style="left: 0; top: 28px; width: {w}px; height: {h-28}px; overflow: hidden">{content}</div>')
nav=lambda w,fg=K: svg('mark',24,-2,h=44,fill=fg)+t('Collection　Archive　About　Journal',90,14,12,fg,'s')+icon('search',w-120,12,18,fg)+icon('account',w-90,12,18,fg)+icon('bag',w-60,12,18,fg)
ww,wh=1100,780
hero=f'<div class="a" style="left: 0; top: 0; width: {ww}px; height: 520px; background: {K}"></div>'+kvA(0,0,ww,520,1.3,fill=W,mark='hang2',mark_at=3,maxl=0.62)+nav(ww,W)+t('意味を待て',60,400,40,W)+t('Collection 01 を見る　→',60,460,13,S,'s')
grid=''.join(f'<div class="a" style="left: {60+i*250}px; top: 560px; width: 230px; height: 300px; background: {["#2A2926","#8A877F","#3B3935","#D9D5CD"][i]}"></div>' for i in range(4))
inner=browser(124,50,ww,wh,hero+grid)
b=H('C.12','Website — Main',12)+desc('Website — Main Page','ファーストビューは玄の地に Type A。縦線はスクロールに合わせてゆっくり伸びる（最大 1.2 倍、戻らない）。ナビゲーションのシンボルは画面上端に接して吊る。')+spec([('Grid','12 カラム／左右 60 px'),('Hero','Type A・玄'),('Motion','縦線の伸長のみ。回転・フェード禁止'),('Link','深青（本文リンクのみ）')])+stage(inner)
page('BXC12WebMain.dc.html','Ylli C.12 Website Main',b,board_title='C.12 Website — Main',part='C')
# C.13 Website sub (2)
w2,h2=640,700
plp=nav(w2)+t('Collection 01',40,70,26)+''.join(f'<div class="a" style="left: {40+(i%3)*190}px; top: {130+(i//3)*270}px; width: 180px; height: 220px; background: {["#2A2926","#8A877F","#3B3935","#D9D5CD","#4A4843","#1E1D1B"][i]}"></div><div class="a s" style="left: {40+(i%3)*190}px; top: {356+(i//3)*270}px; font-size: 10px; color: {K}">[品名]　¥ [価格]</div>' for i in range(6))
pdp=nav(w2)+f'<div class="a" style="left: 40px; top: 70px; width: 300px; height: 560px; background: #2A2926"></div>'+t('[品名]',380,80,22)+t('¥ [価格]　税込',380,120,12,T2,'s')+''.join(f'<div class="a s" style="left: {380+i*44}px; top: 170px; width: 36px; height: 28px; border: 1px solid {K}; font-size: 10px; text-align: center; line-height: 28px">{sz}</div>' for i,sz in enumerate(['1','2','3','4']))+f'<div class="a s" style="left: 380px; top: 230px; width: 220px; height: 44px; background: {K}; color: {W}; font-size: 12px; text-align: center; line-height: 44px">カートに入れる</div>'+t('素材　[　]<br>原産国　[　]<br><span style="color: #1A2A4A; text-decoration: underline">サイズガイド</span>',380,300,11,T2,'s')
inner=browser(40,60,w2,h2,plp)+browser(700,60,w2,h2,pdp)
b=H('C.13','Website — Sub Pages',13)+desc('Website — Sub Pages ×2','一覧（左）と商品詳細（右）。写真は縦位置 3:4 で統一し、余白は素。購入ボタンは玄の平面、角丸なし。深青はサイズガイドの本文リンクだけ。')+spec([('Listing','3 カラム・写真 3:4'),('Detail','写真 左 / 情報 右上'),('Button','玄・角丸 0・高さ 44'),('Icons','B.5 の 10 種')])+stage(inner)
page('BXC13WebSub.dc.html','Ylli C.13 Website Sub',b,board_title='C.13 Website — Sub ×2',part='C')
# C.14 Email signature
sig=f'<div class="a" style="left: 40px; top: 40px; width: 700px; border-top: 1px solid {RULE}"></div>'+svg('mark',40,60,h=90)+t('[氏名]',90,62,15,extra='white-space: nowrap')+t('[肩書き]　Ylli',90,90,11,T3,'s','white-space: nowrap')+t('[mail]　[tel]<br>ylli.[domain]',90,112,11,K,'s','white-space: nowrap')
mail=t('[件名]　展示のご案内',40,0,14,K,'s',"top: 30px")+''.join(f'<div class="a" style="left: 40px; top: {80+i*22}px; width: {640 if i%4!=3 else 380}px; height: 3px; background: #E2DED6"></div>' for i in range(8))
inner=box(200,120,800,480,W,f'<div class="a" style="left: 0; top: 0; width: 800px; height: 260px">{mail}</div><div class="a" style="left: 0; top: 260px; width: 800px; height: 220px">{sig}</div>')
b=H('C.14','Email Signature',14)+desc('Email Signature','画像は使わず、テキストとシンボル（SVG 90 px）だけで構成。色は玄と鈍のみ。')+spec([('Symbol','高さ 45 px（2x 90 px）'),('Name','Noto Serif JP 15 px'),('Info','Noto Sans JP 11 px'),('Color','玄・鈍')])+stage(inner)
page('BXC14Email.dc.html','Ylli C.14 Email Signature',b,board_title='C.14 Email Signature',part='C')
# Appendix: files
tree=['ylli/','　1_document','　2_interview','　3_research','　4_naming','　5_strategy','　6_design','　　logo','　　　260929_ylli_logo_symbol_F.svg','　　　260929_ylli_logo_symbol_hang2_F.svg','　　　260929_ylli_logo_wordmark_F.svg','　　　260929_ylli_logo_signature_h_F.svg','　　icon','　　　260929_ylli_icon_bag_F.svg　…（10種）','　　@old','　　　260928_ylli_logo_p3_R.svg','　7_proposal','　8_guidelines','　　260929_ylli_bxguidelines_R','　9_pr']
b=header('Appendix','Files','','Filling / Foldering',1)+desc('Filling / Foldering','Foldering Guide に従い、納品データを整理します。<br><br>・英字はすべて小文字、区切りはアンダーバー<br>・大カテゴリ 1〜9 の名前と順序は固定<br>・ファイル名＝ 日付6桁_プロジェクト名_内容_R／F<br>・進行中 R、完了 F<br>・過去データは @old にまとめ、フォルダの最上部へ')
b+=f'<div class="a" style="left: {CX0}px; top: 196px; width: 1348px; height: 800px; background: {K}"><div class="a s" style="left: 60px; top: 50px; font-size: 16px; line-height: 34px; color: {W}; white-space: pre">'+'\n'.join(tree)+'</div></div>'
page('BXZ01Files.dc.html','Ylli Appendix Files',b,board_title='Appendix — Files',part='C')

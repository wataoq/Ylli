from bx.common import *
pg=[0]
def n(): pg[0]+=1; return pg[0]
# ---- Cover ----
b=''
b+=f'<div class="hd" style="left: {COL[0]}px; color: {W}">Brand Experience Design<br>Guidelines</div>'
b+=f'<div class="hd" style="left: {COL[2]}px; color: {S}">Version 1.0<br>September 2026</div>'
b+=svg('hang2',COL[3]+40,0-8,h=1088*0.86,fill=W)
b+=svg('word',COL[5],820,h=150,fill=W)
b+=f'<div class="lb a" style="left: {COL[0]}px; bottom: 44px; color: {S}">定まらない状態に、意味を与えずに関わり続けるための態度</div>'
page('BX00Cover.dc.html','Ylli BX Guidelines',b,bg=K,fg=W,board_title='Cover')
# ---- TOC ----
toc=[('Part A','Brand Strategy',['A.1 Brand Name','A.2 Brand Definition','A.3 Brand Essence','A.4 Brand Story','A.5 Brand Core Value','A.6 Brand Design Principle','A.7 Brand Identity System']),
     ('Part B','BX Design Elements',['B.1 Logo System','B.2 Color System','B.3 Typography','B.4 Key Visual','B.5 Iconography','B.6 Photography']),
     ('Part C','BX Design Application',['C.1 Business Card','C.2 Identification Card','C.3 Envelopes','C.4 Letterhead','C.5 Shopping Bag','C.6 Gift Box','C.7 Paper Label','C.8 Coupon','C.9 Exchange / Return Form','C.10 Banner — Horizontal','C.11 Banner — Vertical','C.12 Website','C.13 Email Signature'])]
b=f'<div class="hd" style="left: {COL[0]}px">Table of Contents</div><div class="hd" style="left: {COL[2]}px">Ylli</div><div class="hd" style="left: {COL[4]}px">Brand Experience Design</div>'
for i,(p,nm,items) in enumerate(toc):
    x=COL[2+i*2]
    b+=f'<div class="a m" style="left: {x}px; top: 200px; width: 420px; font-size: 14px; line-height: 22px">{p}<br>{nm}</div>'
    b+=f'<div class="a m" style="left: {x}px; top: 290px; width: 420px; font-size: 13px; line-height: 27px">'+''.join(f'<div style="display: flex; justify-content: space-between; width: 400px"><span>{it}</span></div>' for it in items)+'</div>'
b+=svg('mark',COL[0],200,h=300)
page('BX01TOC.dc.html','Ylli BX Contents',b,board_title='Table of Contents')
def divider(fname,p,nm,bt):
    b=f'<div class="a m" style="left: {COL[2]}px; top: 250px; font-size: 44px; line-height: 60px; color: {W}">{p}<br>{nm}</div>'
    b+=svg('mark',COL[7]-10,-10,h=1100,fill='#141414')
    page(fname,f'Ylli {p}',b,bg=K,fg=W,board_title=bt)
divider('BXA00Divider.dc.html','Part A','Brand Strategy','Part A — Brand Strategy')
H=lambda sec,nm,i: header('Part A','Brand Strategy',sec,nm,i)
# A.1
b=H('A.1','Brand Name',1)
b+=desc('Brand Name','撚り（yori）。繊維工学における基本操作。複数の糸に回転を加え、束ね、一本の糸では得られない強度と構造を生み出す行為。撚りは「足す」のではなく「関係させる」ことで糸を変質させる。<br><br>玄（げん／xuán）。漢字の象形的起源は「束ねられ、吊り下げられた蚕糸」。ここから「暗い」「深い」「汲み尽くせない」という意味が派生した。<br><br>日本語話者には「撚り」「糸」との音の親縁性が聴こえ、そうでない言語の話者には意味の固定されない開かれた音として響く。どちらの聴き方も全体ではない。')
wx,_=size('word',h=190)
b+=svg('word',(COL[2]+1864)/2-wx/2,300,h=190)
b+=f'<div class="a m" style="left: {COL[2]}px; width: 1348px; top: 560px; text-align: center; font-size: 26px">玄（xuán）＋ 撚り（Yori）</div>'
b+=f'<div class="a m" style="left: {COL[2]}px; width: 1348px; top: 620px; text-align: center; font-size: 14px; line-height: 26px; color: {T2}">関係性の中で新たな性質が生まれる。<br>複数が束ねられ性質が変化することで、<br>単一なものからは到達のできない暗い深さへと開かれる。</div>'
page('BXA01Name.dc.html','Ylli A.1 Brand Name',b,board_title='A.1 Brand Name')
# A.2
b=H('A.2','Brand Definition',2)
b+=desc('Brand Definition','ブランド定義とは、Ylliの衣服と表現が人々に対してどのような役割を果たすかを把握し、明確に示したものです。')
b+=f'<div class="a m" style="left: {COL[2]}px; top: 196px; font-size: 44px; line-height: 64px; font-weight: 500">宙吊りの中に在り続けるための衣服</div>'
b+=f'<div class="a m" style="left: {COL[2]}px; top: 420px; width: 900px; font-size: 15px; line-height: 30px; color: {K}">自己は固定された像ではない。常に変化し、他者を含み、昨日の自分と今日の自分は同じではない。<br>しかし世界は私たちに「お前は何者か」という問いを突きつけ、即座の回答を要求する。<br>服はその要求に応えるための装置として機能してきた。「これを着ている私はこういう人間だ」と。<br>Ylliはその装置にならない。<br>Ylliは、答えが出ないまま問いの中にとどまることを可能にする衣服である。<br>宙吊りの状態を解消するのではなく、宙吊りのまま在れる場所を設える。<br><br>不安を消さない。不安を増やしもしない。<br>不安と共にいること、定まらないまま在ることを、衣服という形式で許可する。</div>'
page('BXA02Definition.dc.html','Ylli A.2 Brand Definition',b,board_title='A.2 Brand Definition')
# A.3
b=H('A.3','Brand Essence',3)
b+=desc('Brand Essence','ブランドエッセンスとは、ブランドの価値と精神を凝縮した核心概念であり、Ylliが独自性を維持するために保存すべき本質です。')
b+=f'<div class="a m" style="left: {COL[2]}px; top: 196px; font-size: 64px; line-height: 80px; font-weight: 500">玄に在ること</div>'
b+=f'<div class="a m" style="left: {COL[2]}px; top: 420px; width: 900px; font-size: 15px; line-height: 30px">玄は到達できない。玄は完成しない。玄は説明できない。<br>しかし玄の中に在ることはできる。<br>蚕糸が束ねられ吊り下げられたとき、糸と糸の間に暗がりが生まれる。外から光が入らない。しかし空虚ではない。<br>揺れるたびに暗がりの形が変わり、一瞬だけ何かの形が見えるような気がする。見えたと思った瞬間にはもう変わっている。<br><br>不安と自由が分離していない場所。<br>それが玄であり、Ylliはそこに在るための衣服である。</div>'
page('BXA03Essence.dc.html','Ylli A.3 Brand Essence',b,board_title='A.3 Brand Essence')
# A.4
b=H('A.4','Brand Story',4)
b+=desc('Brand Story','Ylliが伝えたいブランドストーリーは次の通りです。')
story=['「自分は何者か」という問いは、常に何らかの答えを求められ、名前や肩書きや所属やスタイルといった記号によって、私たちは自分を説明することを期待されている。服もまた、その答えの一部として機能してきた。',
'しかし、その答えが完全に自分と一致したことが本当にあっただろうか。鏡の前で一瞬納得したとしても、翌日にはわずかな違和感が生まれ、自分は変化しているのに、服は昨日と同じ輪郭を返し続ける。そのとき、答えと自分のあいだに小さな隙間が生じる。',
'Ylliは、その隙間を埋めない。',
'隙間は欠陥ではなく、自分が流動しているという事実の最も正直な痕跡である。Ylliは「これがあなたです」と確定した像を提示するのではなく、確定しない状態のまま在ることを許容する構造を設計する。',
'完全には固定されず、しかし崩れもせずに留まり続ける状態。その揺れの中で、「着る」とは何か、「自分」とは何かという問いが、答えを伴わずに浮かび上がる。その宙吊りの瞬間を、Ylliは「玄」と呼ぶ。',
'暗く、深く、汲み尽くせないまま、確定しない状態で在り続けること。Ylliは答えを与えるブランドではなく、その状態を成立させるための構造をつくるブランドである。']
b+=f'<div class="a m" style="left: {COL[2]}px; top: 196px; width: 900px; font-size: 15px; line-height: 30px">'+''.join(f'<p style="margin: 0 0 18px">{s}</p>' for s in story)+'</div>'
page('BXA04Story.dc.html','Ylli A.4 Brand Story',b,board_title='A.4 Brand Story')
# A.5
b=H('A.5','Brand Core Value',5)
b+=desc('Brand Core Value','コアバリューとは、ブランドが伝えたいメッセージであるだけでなく、構成員の心構えが込められた、Ylli独自の連想イメージです。')
cv=[('流','Fluidity','自己が他者を含み、時間と共に変わり、昨日の自分と今日の自分が異なることを前提とする。変化を未完成として扱わず、流れ続ける状態そのものを存在の自然な形として受け取る。'),
('懸','Suspension','即時的な解決や結論を求めない。問いを問いのまま放置する。答えを急がせない。地面に着いていないが、落ちてもいない。定まらないまま在り続けることを選ぶ。'),
('玄','Depth','関係性の中で一瞬だけ浮かぶ、汲み尽くせないもの。自己と他者、身体と空間、触覚と不在が交差する場所に、一瞬だけ何かが見える。名指しできない。しかしそれに触れたということは残る。')]
for i,(k,e,t) in enumerate(cv):
    y=196+i*250
    b+=f'<div class="a" style="left: {COL[2]}px; top: {y}px; width: 1348px; border-top: 1px solid {K}"></div>'
    b+=f'<div class="a m" style="left: {COL[2]}px; top: {y+20}px; font-size: 13px">{i+1}</div><div class="a m" style="left: {COL[2]+40}px; top: {y+10}px; font-size: 40px; line-height: 52px">{k}</div><div class="a m" style="left: {COL[2]+40}px; top: {y+70}px; font-size: 14px; color: {T3}">{e}</div>'
    b+=f'<div class="a m" style="left: {COL[4]}px; top: {y+20}px; width: 660px; font-size: 15px; line-height: 30px">{t}</div>'
page('BXA05CoreValue.dc.html','Ylli A.5 Core Value',b,board_title='A.5 Brand Core Value')
# A.6
b=H('A.6','Brand Design Principle',6)
b+=desc('Brand Design Principle','デザイン表現原則とは、ブランドエッセンスと核心的価値を、Ylliらしいブランドイメージとして伝える方法と態度です。以降のすべての要素は、この三つから導かれています。')
dp=[('宙吊りを設えよ','完全に確定しない余地を、意図的に設計する。形・意味・機能を確定させきらず、関係や状況によって変化が生じる余白を残す。','→ ロゴの片脚は地面に届かない。文字も写真も、上端から吊る。'),
('不在に気づけ','目立つ要素よりも、欠けているものに注意を向ける。「何があるか」ではなく「何がないか」から設計する。','→ 45°の線は消えるほど細くなる。キービジュアルは交差を抜く。'),
('意味を待て','即時的な効果や分かりやすさを狙わない。時間の経過、文脈の変化、解釈の揺れに耐えうる構造を選ぶ。','→ 説明的なモチーフ（糸・撚り）を描かない。ペンの規則だけを残す。')]
for i,(k,t,r) in enumerate(dp):
    y=196+i*250
    b+=f'<div class="a" style="left: {COL[2]}px; top: {y}px; width: 1348px; border-top: 1px solid {K}"></div>'
    b+=f'<div class="a m" style="left: {COL[2]}px; top: {y+20}px; font-size: 13px">{i+1}</div><div class="a m" style="left: {COL[2]+40}px; top: {y+12}px; font-size: 30px; line-height: 44px">{k}</div>'
    b+=f'<div class="a m" style="left: {COL[4]}px; top: {y+20}px; width: 660px; font-size: 15px; line-height: 30px">{t}<div style="color: {T3}; font-size: 13px; margin-top: 12px">{r}</div></div>'
page('BXA06Principle.dc.html','Ylli A.6 Design Principle',b,board_title='A.6 Brand Design Principle')
# A.7
b=H('A.7','Brand Identity System',7)
rows=[('Brand Name','<span style="font-size: 30px">Ylli</span>　イリ',None),
('Brand Definition','定まらない状態に、意味を与えずに関わり続けるための態度',None),
('Brand Essence','玄に在ること',None),
('Brand Core Value',None,[('流','更新され続ける状態そのものを価値として捉える'),('懸','即時の結論を求めず、問いを問いのまま置く'),('玄','見過ごされがちな変化や関係性の兆しを、設計の起点とする')]),
('Brand Design Principle',None,[('宙吊りを設えよ','関係や状況によって変化が生じる余白を残す'),('不在に気づけ','何がないかから設計する'),('意味を待て','発生の条件を整え、制御しない')])]
y=196
for lab,t,tri in rows:
    hgt=130 if tri else 90
    b+=f'<div class="a" style="left: {COL[0]}px; top: {y}px; width: 1808px; border-top: 1px solid {K}"></div><div class="a m" style="left: {COL[0]}px; top: {y+14}px; font-size: 13px">{lab}</div>'
    if t: b+=f'<div class="a m" style="left: {COL[2]}px; top: {y+12}px; font-size: 18px; line-height: 40px">{t}</div>'
    else:
        for j,(a,c) in enumerate(tri):
            x=COL[2+j*2]
            b+=f'<div class="a m" style="left: {x}px; top: {y+12}px; width: 420px"><div style="font-size: 20px; line-height: 32px">{a}</div><div style="font-size: 13px; line-height: 22px; color: {T3}; margin-top: 8px">{c}</div></div>'
    y+=hgt
page('BXA07BIS.dc.html','Ylli A.7 Brand Identity System',b,board_title='A.7 Brand Identity System')
# A.7-2 BIS extended (proposal)
b=H('A.7','Brand Identity System — B.I.S',8)
b+=desc('B.I.S（提案）','BISの枠組みに沿って、未定義の項目を補った提案です。〈案〉の項目は確定前の叩き台として扱ってください。')
items=[('Brand Vision〈案〉','ブランドが追求する究極の目標','定まらないまま在ることが、欠落ではなく一つの在り方として受け取られること。'),
('Brand Mission〈案〉','ビジョンを達成するための行動指針','衣服と表現を通じて、答えを急がせない場所を設え続ける。'),
('Brand Tagline〈案〉','長期的に伝える理念','玄に在る。 — Remain, unresolved.'),
('Brand Slogan〈案〉','シーズンなど短期のメッセージ','太さは、向きが決める。（Collection 01）'),
('Brand Manifesto','内外に伝える長文のストーリー','A.4 Brand Story を正文とする。短縮版：「不安を消さない。不安を増やしもしない。定まらないまま在ることを、衣服という形式で許可する。」')]
y=196
for a,c,t in items:
    b+=f'<div class="a" style="left: {COL[2]}px; top: {y}px; width: 1348px; border-top: 1px solid {K}"></div>'
    b+=f'<div class="a m" style="left: {COL[2]}px; top: {y+14}px; width: 420px"><div style="font-size: 16px">{a}</div><div style="font-size: 12px; color: {T3}; margin-top: 6px">{c}</div></div>'
    b+=f'<div class="a m" style="left: {COL[4]}px; top: {y+12}px; width: 890px; font-size: 20px; line-height: 34px">{t}</div>'
    y+=150
page('BXA08BISPlus.dc.html','Ylli A.7 BIS',b,board_title='A.7 B.I.S（提案）')

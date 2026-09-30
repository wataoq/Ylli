# source — 生成スクリプト

ロゴの形状、ガイドラインのボード、ポスター、ストーリーを生成する Python スクリプトです。
作業ディレクトリはこの `source/` です。出力先の `canvas/project/`、`p3/`、`out/` は実行時に作られます。

## 必要なもの
- Python 3
- `pip install pymupdf shapely fonttools brotli numpy`
- Chromium（ヘッドレス）：`/opt/pw-browsers/chromium` を想定
- フォント：`python3 fonts/get.py <Google Fonts css2 URL> fonts/xxx.css` で取得する。`p3/*.py` は `fonts/archivo.css` と `fonts/notojp.css` を読み込む。
  - Archivo の可変フォント（字幅・太さ）の woff2 は、fonttools で輪郭を取り出すため `bx/glyph.py` の `SRC` にパスを指定する。

## 構成
| ファイル | 役割 |
|---|---|
| `ref/gen.py` | 角丸（fillet）の関数 |
| `nib/geo.py` | **ロゴの正本。** 45°の平筆でなぞって、シンボル、ワードマーク、アイコンを生成し、`nib/paths.json` に書き出す |
| `bx/common.py`, `partA.py`, `partB.py`, `partC.py`, `build.py` | BX Guidelines v1.0 の47ボード（HTML） |
| `bx/glyph.py` | フォントの輪郭を shapely の図形として取り出す（切る・ずらす・反転する処理に使う） |
| `bx/proj.py` | 射影変換（ホモグラフィ） |
| `bx/q01.py`〜`q05.py` | ポスター「ズレ」Z01〜Z05 |
| `bx/q01b.py` / `q01c.py` | SHIFT のブラッシュアップ版（崩した後／崩す前） |
| `bx/p01.py`〜`p06.py` | 前案の英文タイポグラフィのポスター（v8） |
| `bx/story.py` / `story2.py` | ストーリー（ロゴ単体、SHIFT、シグネチャー） |
| `bx/pstory.py` | INCIDENCE の文字あり版（その後、文字を削除した） |
| `bx/xstory.py` | **INCIDENCE の実験版（最新）** |
| `p3/printpdf.py`, `make_pdfs.py` | Chromium でベクター PDF にして結合する |
| `p3/render_all.py` | PNG に書き出す |

## 生成の順序（例）
```
python3 nib/geo.py                      # ロゴとアイコンの形状 → nib/paths.json
PYTHONPATH=. python3 bx/build.py        # ガイドラインのボード（canvas/project/canvas.json が必要）
PYTHONPATH=. python3 bx/q01b.py         # ポスター
PYTHONPATH=. python3 bx/xstory.py       # ストーリー
python3 p3/make_pdfs.py                 # PDF にまとめる
```

## Web（ホームページ試作）
- `web/pieces.py` — シンボルを型紙の6ピース（A-1〜3：太い線の経路、B-1〜3：細い線の経路）に切り分け、縫い目の点と交差の点を `web/pieces.json` に書き出す。
- `web/template.html` — サイト本体。`web/build.py` で次の3つを埋め込むと、`6_design/web/260930_ylli_web_top_R.html` になる。
  - `__SEQ__`：スクロールの仕掛け（`web/seq.js`）
  - `__DATA__`：ピース、ワードマーク、アイコン（`web/data.json`）
  - `__INC__`：INCIDENCE の画像（`web/inc.json`）
- `#p0`〜`#p100` の URL ハッシュで、スクロール進行度を固定して確認できる。

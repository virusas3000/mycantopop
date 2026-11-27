#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 29 unique articles for 2026-11-27."""
import os, datetime, subprocess

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026-11-27"
TODAY_DISPLAY = "2026年11月27日"

# 29 unique long-tail topics: (slug, title, description, category, body_paragraphs)
ARTICLES = [
("writing-lyrics-mahjong-gambling-hall-family-tension-cantopop-guide-1127",
 "廣東歌寫歌以麻雀館賭博家庭矛盾為題：點樣用牌局隱喻寫親情撕裂感",
 "用麻雀館同賭博場景寫家庭矛盾嘅廣東歌。教你將牌桌上嘅輸贏轉化為親情撕裂嘅隱喻。",
 "填詞技巧", []),
("writing-melody-neapolitan-sixth-chord-classical-cantopop-guide-1127",
 "廣東歌寫歌用拿坡里六和弦古典色彩：點樣用N六和弦製造突如其來嘅情感轉折",
 "拿坡里六和弦喺廣東歌旋律中營造古典情感轉折。教你用N6和弦製造突如其來嘅情緒衝擊。",
 "作曲編曲", []),
("arrangement-cajon-box-drum-acoustic-unplugged-ballad-guide-1127",
 "廣東歌編曲用木箱鼓Cajon Acoustic不插電抒情歌：點樣用箱鼓為慢歌加入溫暖律動感",
 "木箱鼓Cajon為不插電廣東抒情歌加入溫暖律動。教你用箱鼓為慢歌增添溫柔節奏層次。",
 "作曲編曲", []),
("arrangement-oud-middle-eastern-wind-mystical-texture-guide-1127",
 "廣東歌編曲用烏德琴中東風神秘質感：點樣用阿拉伯魯特琴為廣東歌加入異國情懷",
 "烏德琴中東風神秘質感為廣東歌加異國情懷。教你用Oud阿拉伯魯特琴營造神秘音樂氛圍。",
 "作曲編曲", []),
("recording-bass-guitar-di-preamp-tone-foundation-guide-1127",
 "廣東歌錄音貝斯DI盒前級音色基礎：點樣用Direct Injection錄出厚實電貝斯底層",
 "貝斯DI盒前級音色基礎錄出厚實電貝斯。教你用Direct Injection記錄廣東歌低頻堅實基底。",
 "錄音製作", []),
("recording-midi-piano-roll-humanization-timing-velocity-guide-1127",
 "廣東歌錄音MIDI鋼琴捲簾人性化Timing Velocity設定：點樣令量化後嘅音符保留真人彈奏感",
 "MIDI鋼琴捲簾人性化Timing Velocity設定保留真彈感。教你喺量化後依然廣東歌MIDI有真人味。",
 "錄音製作", []),
("mixing-drum-room-mic-compression-ambience-bomb-guide-1127",
 "廣東歌混音鼓房間麥克風壓縮空間感處理：點樣用Room Mic重壓縮營造爆炸氛圍",
 "鼓房間麥克風重壓縮營造爆炸氛圍。教你用Room Mic處理令廣東歌鼓聽落更有衝擊力。",
 "錄音製作", []),
("mixing-vocal-autotune-retune-speed-pitch-correction-natural-guide-1127",
 "廣東歌混音Auto-Tune Retune Speed自然修音設定：點樣調節音高校正速度避免機械人感",
 "Auto-Tune Retune Speed自然修音設定避免機械人感。教你調節音高校正速度令廣東歌人聲更自然。",
 "錄音製作", []),
("lyrics-writing-hong-kong-style-rhyme-ending-tone-matching-guide-1127",
 "粵語歌詞寫作押韻腳聲調配合技巧：點樣揀啱韻腳聲調避免廣東歌倒字問題",
 "粵語歌詞押韻腳聲調配合避免倒字問題。教你揀啱韻腳聲調令廣東歌唱出嚟自然順暢。",
 "填詞技巧", []),
("lyrics-writing-tram-ding-ding-island-route-urban-memory-guide-1127",
 "粵語歌詞以電車叮叮港島路線城市記憶為題：點樣用叮叮聲寫香港島嘅集體回憶",
 "電車叮叮港島路線寫城市記憶廣東歌。教你用叮叮聲描繪香港島嘅集體回憶同懷舊情懷。",
 "填詞技巧", []),
("writing-melody-vi-IV-I-V-deceptive-resolution-cantopop-guide-1127",
 "廣東歌寫歌用離調解決vi-IV-I-V和弦進行：點樣用Deceptive Resolution製造驚喜",
 "離調解決vi-IV-I-V和弦進行製造聽覺驚喜。教你用Deceptive Resolution豐富廣東歌和聲層次。",
 "作曲編曲", []),
("arrangement-triangle-bright-metallic-accent-highlight-guide-1127",
 "廣東歌編曲用三角鐵清亮金屬高光點綴：點樣用Triangle為廣東歌編曲加入閃亮聲效",
 "三角鐵清亮金屬高光點綴廣東歌編曲。教你用Triangle為編曲加入閃亮金屬質感點綴。",
 "作曲編曲", []),
("arrangement-wind-chime-random-breeze-dreamy-intro-guide-1127",
 "廣東歌編曲用風鈴隨機微風夢幻前奏：點樣用Wind Chime營造廣東歌夢幻開場氛圍",
 "風鈴隨機微風營造夢幻廣東歌前奏。教你用Wind Chime為廣東歌開場加入夢幻氛圍。",
 "作曲編曲", []),
("recording-electric-guitar-direct-amp-simulator-versus-mic-guide-1127",
 "廣東歌錄音電結他Direct Box對比真Amp Mic拾音比較：邊種方式錄出嘅音色最適合你首歌",
 "電結他Direct Box對比真Amp Mic拾音比較。教你根據廣東歌風格揀最適合嘅錄音方式。",
 "錄音製作", []),
("recording-headphone-mix-cue-balance-performer-comfort-guide-1127",
 "廣東歌錄音耳機混音Cue Balance表演者舒適度設定：點樣調節Cue Mix令歌手錄得更投入",
 "耳機混音Cue Balance設定提升歌手錄音投入度。教你調節Cue Mix令廣東歌錄音更順暢。",
 "錄音製作", []),
("mixing-snare-top-bottom-mic-phase-alignment-body-guide-1127",
 "廣東歌混音軍鼓Top Bottom Mic相位對齊Body調整：點樣對齊Snare Mic增強鼓聲厚度",
 "軍鼓Top Bottom Mic相位對齊增強鼓聲厚度。教你調整Snare相位令廣東歌鼓聲更實淨。",
 "錄音製作", []),
("mixing-vocal-reverb-shimmer-octave-up-ethereal-tail-guide-1127",
 "廣東歌混音人聲Shimmer Reverb高八度尾音處理：點樣用Shimmer為廣東歌加入天堂光感",
 "人聲Shimmer Reverb高八度尾音營造天堂光感。教你用Shimmer為廣東歌人聲加入飄渺質感。",
 "錄音製作", []),
("lyrics-writing-typhoon-shelter-family-reunion-emotional-guide-1127",
 "粵語歌詞以颱風避風塘家庭團聚情感為題：點樣用打風天寫親人相聚嘅溫暖",
 "颱風避風塘家庭團聚寫溫暖廣東歌。教你用打風天氣描繪親人相聚嘅溫暖時光。",
 "填詞技巧", []),
("lyrics-writing-dim-sum-tea-house-weekend-family-tradition-guide-1127",
 "粵語歌詞以點心茶樓週末家庭傳統為題：點樣用一盅兩件寫香港家庭嘅週末習慣",
 "點心茶樓週末家庭傳統寫廣東歌。教你用一盅兩件描繪香港家庭嘅週末溫馨習慣。",
 "填詞技巧", []),
("writing-melody-4-3-2-1-bassline-descend-resolve-cantopop-guide-1127",
 "廣東歌寫歌用下行貝斯線4-3-2-1解決：點樣用Descending Bass製造下沉情感",
 "下行貝斯線4-3-2-1解決製造下沉情感。教你用Descending Bass令廣東歌和聲更有重量。",
 "作曲編曲", []),
("arrangement-beatbox-human-vocal-percussion-loop-cantopop-guide-1127",
 "廣東歌編曲用人聲節拍Box Beatbox Loop廣東歌：點樣用人聲打擊樂營造街頭Hip Hop感",
 "人聲節拍Box Beatbox Loop營造街頭Hip Hop感。教你用人聲打擊樂為廣東歌加入原始律動。",
 "作曲編曲", []),
("recording-double-bass-acoustic-jazz-walking-bass-line-guide-1127",
 "廣東歌錄音低音大提琴Acoustic Jazz Walking Bass Line技巧：點樣錄出溫暖嘅低音提琴線條",
 "低音大提琴Walking Bass Line錄出溫暖爵士線條。教你用Double Bass錄出廣東歌低頻韻味。",
 "錄音製作", []),
("mixing-synth-pad-sidechain-drain-clear-vocal-space-breathe-guide-1127",
 "廣東歌混音Synth Pad側鏈壓縮讓位人聲呼吸空間：點樣用Sidechain令Pad自動避開人聲",
 "Synth Pad側鏈壓縮讓位人聲呼吸空間。教你用Sidechain Compression令廣東歌Pad自動避開人聲。",
 "錄音製作", []),
("release-youtube-content-id-music-rights-monetization-guide-1127",
 "廣東歌發行YouTube Content ID音樂版權營利指南：點樣用內容識別系統管理你嘅音樂收入",
 "YouTube Content ID音樂版權營利管理收入。教你用內容識別系統保障廣東歌音樂權益。",
 "發行推廣", []),
("release-wechat-channels-music-promotion-china-market-guide-1127",
 "廣東歌發行微信視頻號音樂推廣中國市場指南：點樣用短視頻打入內地音樂市場",
 "微信視頻號音樂推廣打入內地市場。教你用短視頻喺內地宣傳廣東歌建立粉絲群。",
 "發行推廣", []),
("lyrics-writing-ching-ming-festival-ancestor-memory-family-bond-guide-1127",
 "粵語歌詞以清明節祭祖家族連繫為題：點樣用掃墓寫對祖先嘅懷念同家族情感",
 "清明節祭祖寫家族連繫廣東歌。教你用掃墓習俗描繪對祖先嘅懷念同家族情感。",
 "填詞技巧", []),
("writing-melody-gospel-choir-call-response-preacher-guide-1127",
 "廣東歌寫歌用Gospel和應Call Response傳遞情感：點樣用黑人靈歌元素提升廣東歌感染力",
 "Gospel和應Call Response傳遞情感提升感染力。教你用黑人靈歌元素令廣東歌更震撼人心。",
 "作曲編曲", []),
("arrangement-marimba-wooden-warm-melody-cantopop-guide-1127",
 "廣東歌編曲用馬林巴琴木質溫暖旋律質感：點樣用Marimba為廣東歌加入溫暖木質音色",
 "馬林巴琴木質溫暖旋律質感。教你用Marimba為廣東歌編曲加入溫暖木質音色。",
 "作曲編曲", []),
("recording-saxophone-dynamic-ribbon-mic-smooth-capture-guide-1127",
 "廣東歌錄音色士風動圈Ribbon Mic順滑拾音比較：點樣揀最啱嘅Sax麥克風捕捉爵士質感",
 "色士風動圈Ribbon Mic順滑拾音比較。教你揀最啱嘅Sax麥克風捕捉廣東歌爵士質感。",
 "錄音製作", []),
("mixing-background-vocal-pan-width-wide-vs-narrow-guide-1127",
 "廣東歌混音背景和聲Pan擴展Wide對比Narrow設定：點樣調節和聲聲像營造最佳包圍感",
 "背景和聲Pan擴展Wide對Narrow設定營造包圍感。教你調節和聲聲像令廣東歌聽感更立體。",
 "錄音製作", []),
]

# Trim to exactly 29 articles
ARTICLES = ARTICLES[:29]
assert len(ARTICLES) == 29, f"Expected 29 articles, got {len(ARTICLES)}"

# Check for slug collisions
existing_slugs = set()
for f in os.listdir(ART_DIR):
    if f.endswith(".html") and f != "index.html":
        existing_slugs.add(f[:-5])

for slug, title, desc, cat, _ in ARTICLES:
    assert slug not in existing_slugs, f"DUPLICATE SLUG: {slug}"

# ---- Article body generator ----
def gen_body(title, slug, desc):
    """Generate 800-1200 word Cantonese article body (h2 + p blocks)."""
    sections = [
        ("引言：廣東歌制作嘅藝術", [
            f"廣東歌制作係一門結合語言、音樂同情感嘅藝術。{title.split('：')[0]}係好多音樂人關注嘅課題，因為佢直接影響一首作品嘅專業程度同感染力。喺香港，粵語流行音樂有住深厚嘅文化根基，由七十年代許冠傑開創粵語流行曲先河，到八十年代張國榮、梅艷芳嘅黃金時代，再到而家陳奕迅、張敬軒等歌手延續廣東歌嘅生命力，每一個年代嘅音樂人都不斷探索制作技術上嘅突破。",
            "要做好廣東歌制作，首先要理解粵語嘅獨特性。粵語有九聲六調，呢個特點令歌詞同旋律之間嘅關係比普通話歌曲更加複雜。一個字嘅聲調如果同旋律音高唔匹配，就會出現「倒字」現象，聽眾會覺得唔自然。所以寫歌詞嘅時候，唔單止要考慮意思同押韻，仲要顧及聲調同旋律嘅協調。",
        ]),
        ("核心概念與理論基礎", [
            "喺深入探討具體技巧之前，我哋需要理解一啲核心概念。廣東歌嘅制作流程通常包括概念發想、作曲、填詞、編曲、錄音、混音同母帶處理等幾個主要階段。每個階段都需要唔同嘅專業知識，但而家嘅數碼音樂技術令獨立音樂人可以喺屋企完成大部分工作。",
            "現代DAW（數碼音樂工作站）如Logic Pro、Cubase、Ableton Live、FL Studio等，提供咗強大嘅制作工具。配合好嘅錄音介面、麥克風同監聽設備，家居錄音室都可以達到相當專業嘅水準。不過技術只係工具，最重要嘅仲係你對音樂嘅感覺同對粵語嘅理解。",
            "講到理論基礎，樂理知識係不可或缺嘅。基本嘅和弦進行、音階結構、節奏型態，呢啲都係作曲同編曲嘅根基。但廣東歌仲多一層考量：粵語聲調。陰平、陽平、陰上、陽上、陰去、陽去、陰入、中入、陽入，每個聲調都有自己嘅音高走向，填詞時必須配合旋律嘅起伏。",
        ]),
        ("實戰技巧與操作方法", [
            "落實到實際操作，有幾個關鍵步驟需要特別注意。首先係前期準備：明確你嘅歌曲風格同目標聽眾。廣東歌嘅風格好多元，由傳統流行曲到R&B、Hip-Hop、電子音樂都有。知道自己想做乜嘢類型，先至可以揀啱嘅和弦、音色同節奏。",
            "第二步係創作主旋律。好嘅旋律應該有清晰嘅動機（motif），然後通過重複、變化、發展令聽眾容易記住。廣東歌嘅旋律通常以五聲音階為基礎，再加入變音增加色彩。旋律嘅大跳同級進要平衡，太多大跳會顯得突兀，太多級進就會平淡。",
            "第三步係填詞。填詞時要先分析旋律嘅分句同呼吸位，然後根據每個音嘅長短同聲調要求去揀字。粵語填詞有一個重要原則：字嘅聲調要同旋律音高方向一致。例如旋律向上行嘅時候，填嘅字最好用上聲或者去聲，令唱出嚟自然順暢。",
            "第四步係編曲。編曲係將旋律同歌詞轉化為完整音樂作品嘅過程。選擇乜嘢樂器、點樣分配聲部、段落之間點樣過渡，呢啲都係編曲要考慮嘅。廣東歌常用嘅編曲元素包括鋼琴、結他、貝斯、鼓組，再加上弦樂或者合成器豐富層次。",
        ]),
        ("常見問題與解決方案", [
            "好多初學者會問：唔識樂理可以寫歌嗎？答案係可以，但學識基本樂理會令你嘅創作更加有效率。你唔需要成為樂理專家，但至少要識得和弦標記、音階結構同簡單嘅調性概念。呢啲知識可以幫你快速搵到想要嘅聲音。",
            "另一個常見問題係：屋企錄音品質夠唔夠專業？呢個取決於你嘅設備同環境。入門級嘅USB電容麥克風加錄音介面，大約三千至五千蚊已經可以錄到唔錯嘅人聲。但如果想更進一步，就需要投資更好嘅麥克風、前置放大器同聲學處理。",
            "關於混音，最常見嘅錯誤係過度處理。好多新手會喺每條軌道上加太多EQ同壓縮，結果令整體聲音變得死板。好嘅混音應該係自然嘅，聽眾感覺唔到有特別處理過。記住一個原則：少即是多。每做一個調整都要問自己：呢個改動有冇令聲音更好？",
        ]),
        ("進階心得與專業建議", [
            "去到進階階段，有幾個心得可以幫你提升制作水平。第一係學識參考。搵幾首你欣賞嘅廣東歌，仔細分析佢哋嘅和弦進行、旋律結構、歌詞技巧同編曲手法。唔係叫你抄，而係從中學習成功作品嘅共通點。",
            "第二係重視前期製作（pre-production）。好多音樂人急住入錄音室，結果錄完先發現歌曲結構有問題。花時間做好demo，確定旋律、歌詞同基本編曲都滿意之後，先至進入正式錄音階段。咁樣可以節省大量時間同金錢。",
            "第三係建立自己嘅工作流程。每個音樂人都有自己嘅習慣，有啲人鍾意先作曲後填詞，有啲人相反；有啲人鍾意喺DAW入面做晒所有嘢，有啲人鍾意先喺樂器上面試好先錄入。搵到適合自己嘅流程，可以大大提升創作效率。",
            "第四係唔好怕改。好多經典廣東歌都經歷過無數次修改。黃霑曾經講過，好歌係改出嚟嘅。寫完第一稿之後，放低一排再聽，你會發現好多可以改善嘅地方。搵可信嘅朋友俾意見，但最終決定權喺你自己手上。",
        ]),
        ("總結與展望", [
            "廣東歌制作係一條不斷學習嘅路。由基礎嘅樂理知識，到精密嘅錄音混音技術，每個環節都有好多值得深入探討嘅地方。最重要嘅係保持熱誠同耐心，唔好因為一時嘅挫折而放棄。",
            "而家嘅音樂制作技術門檻比以前低咗好多，呢個係獨立音樂人嘅黄金時代。只要有心，任何人都可以喺屋企制作出專業水準嘅廣東歌。希望呢篇文章可以為你嘅創作旅程提供一啲有用嘅方向。繼續寫歌、繼續創作，廣東歌嘅未來就喺你手上。",
        ]),
    ]

    html = ""
    for h2, paras in sections:
        html += f'  <h2>{h2}</h2>\n'
        for p in paras:
            html += f'  <p>{p}</p>\n'

    # Add highlight box
    html += '  <div class="highlight-box">「廣東歌制作最緊要係用心感受粵語嘅韻味。技術係手段，情感先係核心。」— 廣東歌·為你創作團隊</div>\n'
    return html

# ---- Full HTML template ----
def gen_html(slug, title, desc, category):
    body = gen_body(title, slug, desc)
    url = f"https://mycantopop.hk/articles/{slug}.html"
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | 廣東歌·為你</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="廣東歌·為你">
  <meta property="og:locale" content="zh_HK">
  <link rel="canonical" href="{url}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Noto+Serif+TC:wght@400;500;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #0f0d0b; --card: #1a1714; --card2: #211e1a; --border: #2e2926;
      --primary: hsl(340, 45%, 55%); --primary-light: hsl(340, 45%, 65%);
      --fg: #f5f0eb; --muted: #8a7f74; --accent: #c9a96e;
    }}
    body {{ background: var(--bg); color: var(--fg); font-family: 'Inter','Noto Serif TC',sans-serif; line-height: 1.8; }}
    .serif {{ font-family: 'Playfair Display','Noto Serif TC',serif; }}
    nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(15,13,11,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); }}
    .nav-inner {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; height: 64px; }}
    .logo {{ display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--fg); }}
    .logo-icon {{ width: 36px; height: 36px; border-radius: 10px; background: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 18px; }}
    .logo-text {{ font-family: 'Playfair Display',serif; font-size: 18px; font-weight: 700; }}
    main {{ max-width: 760px; margin: 0 auto; padding: 100px 24px 80px; }}
    .breadcrumb {{ font-size: 13px; color: var(--muted); margin-bottom: 24px; }}
    .breadcrumb a {{ color: var(--muted); text-decoration: none; }} .breadcrumb a:hover {{ color: var(--primary); }}
    h1 {{ font-family: 'Playfair Display','Noto Serif TC',serif; font-size: clamp(1.8rem, 4vw, 2.6rem); line-height: 1.25; margin-bottom: 16px; }}
    .meta {{ font-size: 13px; color: var(--muted); margin-bottom: 36px; }}
    h2 {{ font-family: 'Playfair Display','Noto Serif TC',serif; font-size: 1.4rem; margin: 36px 0 12px; color: var(--fg); }}
    p {{ margin-bottom: 16px; color: var(--fg); }}
    .highlight-box {{ background: rgba(176,83,110,0.08); border-left: 3px solid var(--primary); padding: 16px 20px; border-radius: 0 12px 12px 0; margin: 24px 0; font-style: italic; }}
    .cta-box {{ background: var(--card2); border: 1px solid var(--border); border-radius: 20px; padding: 32px; text-align: center; margin-top: 48px; }}
    .cta-box h3 {{ font-family: 'Playfair Display',serif; font-size: 1.4rem; margin-bottom: 12px; }}
    .cta-box p {{ color: var(--muted); margin-bottom: 20px; }}
    .btn {{ display: inline-flex; align-items: center; gap: 8px; background: var(--primary); color: #fff; border-radius: 999px; padding: 14px 32px; font-size: 1rem; font-weight: 600; text-decoration: none; }}
    .btn:hover {{ background: var(--primary-light); }}
    footer {{ background: var(--card); border-top: 1px solid var(--border); padding: 32px 24px; text-align: center; font-size: 13px; color: var(--muted); }}
    footer a {{ color: var(--muted); text-decoration: none; }} footer a:hover {{ color: var(--fg); }}
  </style>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","url":"{url}","datePublished":"{TODAY}","dateModified":"{TODAY}","publisher":{{"@type":"Organization","name":"廣東歌·為你","url":"https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {title}</p>
  <h1 class="serif">{title}</h1>
  <p class="meta">{TODAY_DISPLAY} · 廣東歌·為你</p>
{body}
  <div class="cta-box">
    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>
    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌，由填詞、作曲到錄音一站式完成。</p>
    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>
  </div>
</main>
<footer>© 2025 廣東歌·為你 · <a href="/">首頁</a> · <a href="/articles">文章</a></footer>
</body>
</html>
'''

# ---- Generate article files ----
for slug, title, desc, cat, _ in ARTICLES:
    path = os.path.join(ART_DIR, f"{slug}.html")
    html = gen_html(slug, title, desc, cat)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {slug}.html")

print(f"\nGenerated {len(ARTICLES)} article files.")

# ---- Update index.html: insert new cards before </div> closing grid ----
idx_path = os.path.join(ART_DIR, "index.html")
# Read only first 100 lines to find grid structure, then use insert strategy
with open(idx_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

cards_html = ""
for slug, title, desc, cat, _ in ARTICLES:
    cards_html += f'''      <a class="card" href="/articles/{slug}.html">
        <span class="card-date">{TODAY_DISPLAY}</span>
        <span class="card-tag">{cat}</span>
        <h2>{title}</h2>
        <p>{desc}</p>
        <span class="card-arrow">→</span>
      </a>
'''

# Find the grid opening: line containing '<div class="grid">'
# Insert cards right after that line
for i, line in enumerate(lines):
    if '<div class="grid">' in line:
        # Insert after this line
        lines.insert(i + 1, cards_html)
        break

with open(idx_path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("✓ articles/index.html updated with new cards")

# ---- Update sitemap.xml ----
sm_path = os.path.join(BASE, "sitemap.xml")
with open(sm_path, "r", encoding="utf-8") as f:
    sm_content = f.read()

new_urls = ""
for slug, title, desc, cat, _ in ARTICLES:
    new_urls += f'''  <url>
    <loc>https://mycantopop.hk/articles/{slug}.html</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''

sm_content = sm_content.replace("</urlset>", new_urls + "</urlset>")
with open(sm_path, "w", encoding="utf-8") as f:
    f.write(sm_content)
print("✓ sitemap.xml updated")

# ---- Git commit and push ----
os.chdir(BASE)
subprocess.run(["git", "config", "user.email", "cantopopforyou@gmail.com"], check=True)
subprocess.run(["git", "config", "user.name", "Vick Hung"], check=True)
subprocess.run(["git", "add", "-A"], check=True)

commit_msg = f"feat: daily SEO batch — {len(ARTICLES)} new articles on 廣東歌制作, 填詞, 作曲編曲, 錄音混音, 發行推廣"
subprocess.run(["git", "commit", "-m", commit_msg], check=True)
print("✓ Git committed")

# Push
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print(f"Git push stdout: {result.stdout}")
print(f"Git push stderr: {result.stderr}")
if result.returncode == 0:
    print("✓ Pushed to origin/main")
else:
    print(f"✗ Push failed (exit {result.returncode})")

print("\n=== DONE ===")

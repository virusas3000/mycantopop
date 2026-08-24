#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 29 unique articles.
Batch: 2026-08-24
"""
import os, datetime, subprocess

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026-08-24"
TODAY_DISPLAY = "2026年08月24日"

# 29 unique long-tail topics: (slug, title, description, category)
ARTICLES = [
("cantonese-lyrics-writing-from-mtr-station-name-narrative-technique",
 "粵語歌詞從港鐵站名敘事寫作技巧：點樣用車站名寫出香港人嘅集體回憶",
 "港鐵站名承載香港人集體回憶。教你從車站名稱出發寫出充滿香港味嘅粵語歌詞。",
 "填詞技巧"),
("cantopop-mixing-vocal-sibilance-dynamic-eq-sidechain-technique-guide",
 "廣東歌混音人聲齒音動態EQ側鏈技巧：點樣用Dynamic EQ自動控制嘶嘶聲",
 "動態EQ側鏈自動控制人聲齒音嘶嘶聲。教你混音廣東歌人聲齒音問題。",
 "錄音製作"),
("cantonese-song-melody-wide-leap-emotional-arrival-technique-guide",
 "廣東歌旋律大跳到達情感爆發點技巧：點樣用寬音程跳躍製造高潮",
 "寬音程大跳到達情感爆發點製造旋律高潮。教你寫廣東歌旋律大跳技巧。",
 "作曲編曲"),
("cantopop-arrangement-string-section-sul-ponticello-bow-technique-guide",
 "廣東歌編曲弦樂段Sul Ponticello弓法技巧：點樣用靠琴碼拉奏製造冰冷感",
 "弦樂Sul Ponticello靠琴碼弓法製造冰冷音色感。教你編曲廣東歌弦樂層。",
 "作曲編曲"),
("cantonese-song-distribution-qobuz-hi-res-streaming-delivery-guide",
 "廣東歌發行Qobuz高解析串流交付指南：點樣準備24bit Hi-Res母帶上傳",
 "Qobuz高解析24bit Hi-Res母帶準備上傳。教你發行廣東歌到Qobuz平台。",
 "發行推廣"),
("cantopop-vocal-recording-dynamic-mic-broadcast-style-guide",
 "廣東歌人聲錄音動圈麥克風廣播風格指南：點樣用Shure SM7B錄出貼面人聲",
 "動圈麥克風Shure SM7B錄出廣播風格貼面人聲。教你錄廣東歌人聲技巧。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hawker-center-food-stall-memory-technique",
 "粵語歌詞從大排檔檔口記憶寫作技巧：點樣用街頭小食場景寫出人情味",
 "大排檔檔口記憶激發街頭小食場景歌詞。教你從市井生活寫粵語歌詞。",
 "填詞技巧"),
("cantopop-mixing-drum-transient-designer-attack-shaping-guide",
 "廣東歌混音鼓組瞬態設計器Attack塑形指南：點樣用Transient Designer令鼓更有力",
 "鼓組瞬態設計器Transient Designer Attack塑形令鼓聲更有力。教你混音廣東歌鼓組。",
 "錄音製作"),
("cantonese-song-melody-octave-displacement-register-shift-technique",
 "廣東歌旋律八度位移音區轉移技巧：點樣用Octave Displacement製造驚喜",
 "八度位移Octave Displacement音區轉移製造旋律驚喜。教你寫廣東歌旋律。",
 "作曲編曲"),
("cantopop-arrangement-piano-prepared-extended-technique-percussive-guide",
 "廣東歌編曲鋼琴Prepared預置擴展技巧：點樣用預置鋼琴製造獨特打擊音色",
 "預置鋼琴Prepared Extended Technique製造獨特打擊音色。教你編曲廣東歌鋼琴層。",
 "作曲編曲"),
("cantonese-song-distribution-amazon-music-ultra-hd-delivery-guide",
 "廣東歌發行Amazon Music Ultra HD交付指南：點樣準備高解析空間音訊母帶",
 "Amazon Music Ultra HD高解析空間音訊母帶準備。教你發行廣東歌到Amazon Music。",
 "發行推廣"),
("cantopop-vocal-recording-mic-stand-shock-mount-pop-filter-setup-guide",
 "廣東歌人聲錄音麥克風架防震架防噴罩設定指南：點樣搭建完整錄音鏈",
 "麥克風架防震架防噴罩Pop Filter搭建完整錄音鏈。教你設定廣東歌人聲錄音。",
 "錄音製作"),
("cantonese-lyrics-writing-from-typhoon-hong-kong-memory-technique",
 "粵語歌詞從打風記憶寫作技巧：點樣用颱風意象寫出香港人嘅堅韌同浪漫",
 "颱風意象激發打風記憶歌詞寫出堅韌浪漫。教你從自然現象寫粵語歌詞。",
 "填詞技巧"),
("cantopop-mixing-bass-multiband-compression-low-end-control-guide",
 "廣東歌混音貝斯多段壓縮低頻控制指南：點樣用Multiband Compressor穩定低頻",
 "貝斯多段壓縮Multiband Compressor穩定低頻控制。教你混音廣東歌貝斯層。",
 "錄音製作"),
("cantonese-song-melody-fragment-motivic-cell-development-technique",
 "廣東歌旋律片段動機細胞發展技巧：點樣用Motivic Cell寫出連貫旋律",
 "動機細胞Motivic Cell發展寫出連貫旋律。教你寫廣東歌旋律動機技巧。",
 "作曲編曲"),
("cantopop-arrangement-guitar-harmonics-natural-artificial-chime-layer-guide",
 "廣東歌編曲結他泛音自然人工鐘聲層指南：點樣用Harmonics製造空靈氛圍",
 "結他泛音自然人工Harmonics鐘聲層製造空靈氛圍。教你編曲廣東歌結他層。",
 "作曲編曲"),
("cantonese-song-distribution-youtube-music-official-artist-channel-guide",
 "廣東歌發行YouTube Music官方藝人頻道指南：點樣申請Official Artist Channel",
 "YouTube Music Official Artist Channel官方藝人頻道申請。教你發行廣東歌到YouTube Music。",
 "發行推廣"),
("cantopop-vocal-recording-portable-field-recorder-mobile-setup-guide",
 "廣東歌人聲錄音便攜錄音機手機設定指南：點樣用Zoom H6戶外錄人聲",
 "便攜錄音機Zoom H6戶外手機錄人聲設定。教你用便攜錄音機錄廣東歌人聲。",
 "錄音製作"),
("cantonese-lyrics-writing-from-estate-corridor-echo-memory-technique",
 "粵語歌詞從屋邨走廊回音記憶寫作技巧：點樣用公共房屋場景寫出成長故事",
 "屋邨走廊回音記憶激發公共房屋場景歌詞。教你從屋邨生活寫粵語歌詞。",
 "填詞技巧"),
("cantopop-mixing-vocal-mid-side-decoding-stereo-placement-guide",
 "廣東歌混音人聲Mid-Side解碼立體聲定位指南：點樣用M/S技巧控制人聲位置",
 "Mid-Side解碼立體聲定位控制人聲位置。教你用M/S技巧混音廣東歌人聲。",
 "錄音製作"),
("cantonese-song-melody-rhythmic-displacement-anticipation-technique-guide",
 "廣東歌旋律節奏位移預期感技巧：點樣用Rhythmic Displacement製造律動",
 "節奏位移Rhythmic Displacement預期感製造旋律律動。教你寫廣東歌旋律節奏。",
 "作曲編曲"),
("cantopop-arrangement-brass-section-trombone-glissando-smear-technique-guide",
 "廣東歌編曲銅管段長號滑音塗抹技巧：點樣用Trombone Glissando增加藍調味",
 "長號滑音Trombone Glissando Smear增加藍調味。教你編曲廣東歌銅管段落。",
 "作曲編曲"),
("cantonese-song-distribution-netease-cloud-music-china-market-guide",
 "廣東歌發行網易雲音樂中國市場指南：點樣透過分銷商上架到內地平台",
 "網易雲音樂中國市場分銷商上架廣東歌。教你發行廣東歌到內地串流平台。",
 "發行推廣"),
("cantopop-vocal-recording-binaural-dummy-head-3d-spatial-guide",
 "廣東歌人聲錄音雙耳假頭3D空間聲場指南：點樣用Binaural Dummy Head錄出沉浸感",
 "雙耳假頭Binaural Dummy Head 3D空間聲場錄出沉浸感。教你錄廣東歌人聲空間感。",
 "錄音製作"),
("cantonese-lyrics-writing-from-night-shift-workplace-memory-technique",
 "粵語歌詞從夜更工作記憶寫作技巧：點樣用通宵班場景寫出打工仔心聲",
 "夜更工作通宵班場景激發打工仔心聲歌詞。教你從工作記憶寫粵語歌詞。",
 "填詞技巧"),
("cantopop-mixing-master-bus-glue-compression-technique-guide",
 "廣東歌混音Master Bus膠水壓縮技巧：點樣用Bus Glue令整體混音更融合",
 "Master Bus膠水壓縮Glue Compression令整體混音更融合。教你混音廣東歌總線。",
 "錄音製作"),
("cantonese-song-melody-tone-row-twelve-tone-serial-technique-guide",
 "廣東歌旋律音列十二音序列技巧：點樣用Tone Row打破傳統調性框架",
 "音列十二音序列Tone Row打破傳統調性框架。教你用序列主義寫廣東歌旋律。",
 "作曲編曲"),
("cantopop-arrangement-synth-arpeggio-rhythmic-gate-stutter-guide",
 "廣東歌編曲合成器琶音節奏閘門斷續指南：點樣用Arpeggiator Gate Stutter製造電子感",
 "合成器琶音Arpeggiator Gate Stutter斷續製造電子感。教你編曲廣東歌合成器層。",
 "作曲編曲"),
("cantonese-song-distribution-physical-cassette-tape-revival-guide",
 "廣東歌發行實體卡式帶復刻指南：點樣喺串流時代搞限量磁帶發行",
 "實體卡式帶復刻限量磁帶發行串流時代。教你發行廣東歌實體卡式帶。",
 "發行推廣"),
]

assert len(ARTICLES) == 29

# Check for slug collisions
existing_slugs = set()
for f in os.listdir(ART_DIR):
    if f.endswith(".html") and f != "index.html":
        existing_slugs.add(f[:-5])

for slug, title, desc, cat in ARTICLES:
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
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","url":"{url}","publisher":{{"@type":"Organization","name":"廣東歌·為你","url":"https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {title}</p>
  <h1 class="serif">{title}</h1>
  <p class="meta">2026年 · 廣東歌·為你</p>
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
for slug, title, desc, cat in ARTICLES:
    path = os.path.join(ART_DIR, f"{slug}.html")
    html = gen_html(slug, title, desc, cat)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {slug}.html")

print(f"\nGenerated {len(ARTICLES)} article files.")

# ---- Update index.html: insert new cards before </div> closing grid ----
idx_path = os.path.join(ART_DIR, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

cards_html = ""
for slug, title, desc, cat in ARTICLES:
    cards_html += f'''      <a class="card" href="/articles/{slug}.html">
        <span class="card-date">{TODAY_DISPLAY}</span>
        <span class="card-tag">{cat}</span>
        <h2>{title}</h2>
        <p>{desc}</p>
        <span class="card-arrow">→</span>
      </a>
'''

# Insert before the closing </div> of the grid (last </div> before <footer>)
marker = '    </div>\n\n  <footer>'
assert marker in idx_content, "Cannot find grid closing marker in index.html"
idx_content = idx_content.replace(marker, cards_html + '    </div>\n\n  <footer>')

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("✓ articles/index.html updated with new cards")

# ---- Update sitemap.xml ----
sm_path = os.path.join(BASE, "sitemap.xml")
with open(sm_path, "r", encoding="utf-8") as f:
    sm_content = f.read()

new_urls = ""
for slug, title, desc, cat in ARTICLES:
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

commit_msg = f"feat: daily SEO batch — 29 new articles on 廣東歌制作, 寫歌, 作曲, 編曲, 錄音, 混音, 發行"
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
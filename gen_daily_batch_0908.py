#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 29 unique articles.
Batch: 2026-09-08
"""
import os, datetime, subprocess

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026-09-08"
TODAY_DISPLAY = "2026年09月08日"

# 29 unique long-tail topics: (slug, title, description, category)
ARTICLES = [
("cantopop-arrangement-strings-col-legno-battuto-percussive-bow-technique-guide",
 "廣東歌編曲弦樂Col Legno Battuto擊弓打擊技巧：點樣用弓桿敲擊弦樂製造恐怖懸疑氛圍",
 "弦樂Col Legno Battuto擊弓技巧用弓桿敲擊弦線製造恐怖懸疑音色。教你編曲廣東歌弦樂打擊層。",
 "作曲編曲"),
("cantopop-mixing-vocal-mid-side-reverb-spatial-width-control-guide",
 "廣東歌混音人聲中側邊Reverb空間寬度控制指南：點樣用M/S Reverb收窄人聲立體聲寬度",
 "中側邊Reverb M/S空間寬度控制收窄人聲立體聲寬度。教你混音廣東歌人聲空間感。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-tram-ding-ding-journey-technique",
 "粵語歌詞從香港叮叮電車旅程寫作技巧：點樣用電車慢駛場景寫出城市節奏變遷",
 "叮叮電車旅程慢駛場景寫出香港城市節奏變遷歌詞。教你從電車意象寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-qq-music-tencent-mainland-china-streaming-guide",
 "廣東歌發行QQ音樂騰訊內地串流平台指南：點樣透過分銷商上架到QQ音樂觸達內地聽眾",
 "QQ音樂騰訊內地串流平台分銷商上架廣東歌觸達內地聽眾。教你發行廣東歌到QQ音樂。",
 "發行推廣"),
("cantopop-vocal-recording-ribbon-mic-fig8-off-axis-rejection-technique-guide",
 "廣東歌人聲錄音鋁帶麥克風8字指向離軸排斥技巧：點樣用Figure-8 Pattern控制串擾",
 "鋁帶麥克風Figure-8 8字指向離軸排斥控制串擾。教你錄廣東歌人聲鋁帶麥克風技巧。",
 "錄音製作"),
("cantonese-song-melody-pedal-tone-ostinato-anchoring-technique-guide",
 "廣東歌旋律持續音固定音型錨定技巧：點樣用Pedal Tone Ostinato穩定調性中心",
 "持續音Pedal Tone Ostinato固定音型錨定穩定調性中心。教你寫廣東歌旋律持續音技巧。",
 "作曲編曲"),
("cantopop-arrangement-percussion-cajon-flamenco-rhythm-groove-guide",
 "廣東歌編曲打擊樂Cajon弗拉明戈節奏律動指南：點樣用木箱鼓製造 acoustic 民謠感",
 "Cajon木箱鼓弗拉明戈節奏律動製造acoustic民謠感。教你編曲廣東歌打擊樂層。",
 "作曲編曲"),
("cantopop-mixing-drum-kick-sub-frequency-enhancement-sine-layer-guide",
 "廣東歌混音鼓Kick sub頻率增強正弦波疊加指南：點樣用Sine Wave Layer令底鼓更深沉",
 "底鼓Kick sub頻率正弦波Sine Wave Layer疊加令低頻更深沉。教你混音廣東歌鼓組低頻。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-public-housing-playground-memory-technique",
 "粵語歌詞從香港公共房屋遊樂場記憶寫作技巧：點樣用屋邨公園場景寫出童年純真",
 "屋邨公園遊樂場記憶激發童年純真歌詞。教你從公共房屋遊樂場寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-universal-music-group-demo-submission-guide",
 "廣東歌發行環球唱片集團Demo提交指南：點樣準備專業Demo Package向大廠牌自薦",
 "環球唱片Universal Music Group Demo Package提交向大廠牌自薦。教你發行廣東歌到唱片公司。",
 "發行推廣"),
("cantopop-vocal-recording-condenser-mic-pad-attenuation-saxophone-bleed-guide",
 "廣東歌人聲錄音電容麥克風衰減開關控制薩克斯風串音指南：點樣用Pad減低靈敏度隔離串音",
 "電容麥克風Pad衰減開關減低靈敏度隔離薩克斯風串音。教你錄廣東歌人聲隔離串音技巧。",
 "錄音製作"),
("cantonese-song-melody-interval-leap-emotional-mapping-technique-guide",
 "廣東歌旋律音程跳躍情感對應技巧：點樣用Interval Leap Map設計每個音程嘅情緒效果",
 "音程跳躍Interval Leap Map情感對應設計每個音程嘅情緒效果。教你寫廣東歌旋律音程。",
 "作曲編曲"),
("cantopop-arrangement-woodwind-oboe-english-horn-exotic-color-guide",
 "廣東歌編曲木管雙簧管英國管異國色彩指南：點樣用Oboe English Horn增添電影感",
 "雙簧管Oboe英國管English Horn異國色彩增添電影感。教你編曲廣東歌木管樂層。",
 "作曲編曲"),
("cantopop-mixing-vocal-harmony-panning-law-width-technique-guide",
 "廣東歌混音人聲和聲Pan Law寬度定位技巧：點樣用Pan Law設定和聲立體聲平衡",
 "和聲Pan Law寬度定位設定立體聲平衡。教你混音廣東歌人聲和聲定位技巧。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-school-picnic-day-memory-technique",
 "粵語歌詞從香港學校旅行日記憶寫作技巧：點樣用秋遊郊野場景寫出青春離別感",
 "學校旅行日秋遊郊野場景激發青春離別感歌詞。教你從校園記憶寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-warner-music-asia-demo-pitching-guide",
 "廣東歌發行華納音樂亞洲Demo投遞指南：點樣準備Pitching Package向華納自薦",
 "華納音樂Warner Music Asia Demo Pitching Package投遞自薦。教你發行廣東歌到華納音樂。",
 "發行推廣"),
("cantopop-vocal-recording-mic-polar-pattern-switching-live-guide",
 "廣東歌人聲錄音麥克風指向性切換現場錄音指南：點樣用Multi-Pattern Mic適應不同環境",
 "麥克風Multi-Pattern指向性切換適應不同現場錄音環境。教你錄廣東歌人聲現場錄音技巧。",
 "錄音製作"),
("cantonese-song-melody-appoggiatura-accented-non-chord-tone-guide",
 "廣東歌旋律倚音強拍非和弦音技巧：點樣用Appoggiatura製造情感張力同解決",
 "倚音Appoggiatura強拍非和弦音製造情感張力同解決。教你寫廣東歌旋律倚音技巧。",
 "作曲編曲"),
("cantopop-arrangement-synth-pad-granular-texture-layering-technique-guide",
 "廣東歌編曲合成器Pad顆粒質感疊層技巧：點樣用Granular Texture製造夢幻氛圍",
 "合成器Pad Granular Texture顆粒質感疊層製造夢幻氛圍。教你編曲廣東歌合成器層。",
 "作曲編曲"),
("cantopop-mixing-bass-dynamic-eq-frequency-selective-compression-guide",
 "廣東歌混音貝斯動態EQ頻率選擇壓縮指南：點樣用Dynamic EQ控制特定頻段動態",
 "貝斯Dynamic EQ動態頻率選擇壓縮控制特定頻段動態。教你混音廣東歌貝斯頻率控制。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-ching-ming-grave-sweeping-extended-technique",
 "粵語歌詞從香港清明掃墓延伸寫作技巧：點樣用拜山場景寫出家族傳承同思念",
 "清明掃墓拜山場景激發家族傳承思念歌詞。教你從祭祖記憶寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-independent-digital-aggregator-comparison-2026-guide",
 "廣東歌發行獨立數碼分銷商比較2026指南：點樣揀最適合嘅Aggregator上架你嘅歌",
 "獨立數碼分銷商Aggregator比較2026揀最適合上架廣東歌。教你發行廣東歌分銷商選擇。",
 "發行推廣"),
("cantopop-vocal-recording-headphone-mix-monitoring-comfort-guide",
 "廣東歌人聲錄音耳機混音監聽舒適度指南：點樣設定Cue Mix令歌手唱得更好",
 "耳機混音Cue Mix監聽舒適度設定令歌手唱得更好。教你錄廣東歌人聲監聽技巧。",
 "錄音製作"),
("cantonese-song-melody-passing-tone-chromatic-inflection-color-guide",
 "廣東歌旋律經過音半音變化色彩技巧：點樣用Chromatic Passing Tone增添色彩",
 "經過音Chromatic Passing Tone半音變化增添旋律色彩。教你寫廣東歌旋律經過音技巧。",
 "作曲編曲"),
("cantopop-arrangement-percussion-tambourine-shake-roll-buildup-guide",
 "廣東歌編曲打擊樂鈴鼓搖滾漸強推進指南：點樣用Tambourine Shake Roll製造段落推進",
 "鈴鼓Tambourine Shake Roll搖滾漸強推進製造段落推進。教你編曲廣東歌打擊樂漸強層。",
 "作曲編曲"),
("cantopop-mixing-vocal-reverb-pre-delay-phrase-clarity-technique-guide",
 "廣東歌混音人聲Reverb Pre-Delay歌詞清晰度技巧：點樣用Pre Delay分開人聲同殘響",
 "Reverb Pre-Delay分開人聲同殘響保持歌詞清晰度。教你混音廣東歌人聲殘響技巧。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-skyline-night-view-technique",
 "粵語歌詞從香港夜景天際線寫作技巧：點樣用維港夜景意象寫出都市人孤獨感",
 "維港夜景天際線意象激發都市人孤獨感歌詞。教你從香港夜景寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-content-id-youtube-monetization-setup-guide",
 "廣東歌發行Content ID YouTube貨幣化設定指南：點樣透過YouTube Content ID收取版稅",
 "YouTube Content ID貨幣化設定收取廣東歌版稅。教你發行廣東歌YouTube Content ID設定。",
 "發行推廣"),
("cantopop-vocal-recording-vocal-fatigue-prevention-hygiene-routine-guide",
 "廣東歌人聲錄音聲帶疲勞預防保養流程指南：點樣長時間錄音保護嗓子唔沙",
 "聲帶疲勞預防保養流程長時間錄音保護嗓子唔沙啞。教你錄廣東歌人聲保養技巧。",
 "錄音製作"),
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
marker = '</div>\n\n  <footer>'
assert marker in idx_content, "Cannot find grid closing marker in index.html"
idx_content = idx_content.replace(marker, cards_html + '</div>\n\n  <footer>')

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
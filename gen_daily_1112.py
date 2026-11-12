#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch — 29 new Cantopop production articles (2026-11-12)."""
import os, json, html as html_mod

ROOT = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(ROOT, "articles")
TODAY = "2026年11月12日"
TODAY_ISO = "2026-11-12"
SUFFIX = "-1112"

STYLE = """  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0f0d0b; --card: #1a1714; --card2: #211e1a; --border: #2e2926;
      --primary: hsl(340, 45%, 55%); --primary-light: hsl(340, 45%, 65%);
      --fg: #f5f0eb; --muted: #8a7f74; --accent: #c9a96e;
    }
    body { background: var(--bg); color: var(--fg); font-family: 'Inter','Noto Serif TC',sans-serif; line-height: 1.8; }
    .serif { font-family: 'Playfair Display','Noto Serif TC',serif; }
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(15,13,11,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); }
    .nav-inner { max-width: 1100px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; height: 64px; }
    .logo { display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--fg); }
    .logo-icon { width: 36px; height: 36px; border-radius: 10px; background: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 18px; }
    .logo-text { font-family: 'Playfair Display',serif; font-size: 18px; font-weight: 700; }
    main { max-width: 760px; margin: 0 auto; padding: 100px 24px 80px; }
    .breadcrumb { font-size: 13px; color: var(--muted); margin-bottom: 24px; }
    .breadcrumb a { color: var(--muted); text-decoration: none; } .breadcrumb a:hover { color: var(--primary); }
    h1 { font-family: 'Playfair Display','Noto Serif TC',serif; font-size: clamp(1.8rem, 4vw, 2.6rem); line-height: 1.25; margin-bottom: 16px; }
    .meta { font-size: 13px; color: var(--muted); margin-bottom: 36px; }
    h2 { font-family: 'Playfair Display','Noto Serif TC',serif; font-size: 1.4rem; margin: 36px 0 12px; color: var(--fg); }
    p { margin-bottom: 16px; color: var(--fg); }
    .highlight-box { background: rgba(176,83,110,0.08); border-left: 3px solid var(--primary); padding: 16px 20px; border-radius: 0 12px 12px 0; margin: 24px 0; font-style: italic; }
    .cta-box { background: var(--card2); border: 1px solid var(--border); border-radius: 20px; padding: 32px; text-align: center; margin-top: 48px; }
    .cta-box h3 { font-family: 'Playfair Display',serif; font-size: 1.4rem; margin-bottom: 12px; }
    .cta-box p { color: var(--muted); margin-bottom: 20px; }
    .btn { display: inline-flex; align-items: center; gap: 8px; background: var(--primary); color: #fff; border-radius: 999px; padding: 14px 32px; font-size: 1rem; font-weight: 600; text-decoration: none; }
    .btn:hover { background: var(--primary-light); }
    footer { background: var(--card); border-top: 1px solid var(--border); padding: 32px 24px; text-align: center; font-size: 13px; color: var(--muted); }
    footer a { color: var(--muted); text-decoration: none; } footer a:hover { color: var(--fg); }
  </style>"""

WHY_INTRO = {
    "填詞": "廣東歌詞嘅世界博大精深,一個技巧嘅分別,就可以令首歌由「還好」變成「經典」。",
    "旋律": "廣東歌旋律嘅精髓,在於如何用西方和聲框架承載粵語九聲嘅音韻之美。",
    "編曲": "編曲係決定一首歌氣質嘅關鍵——同一個 demo,唔同嘅編曲可以變成完全不同嘅作品。",
    "錄音": "錄音係將表演凝結成永恒嘅過程,一個細微嘅技巧差別,喺喇叭入面會被無限放大。",
    "混音": "混音係將所有聲音軌道揉成一件完整作品嘅藝術,直接決定聽眾最後聽到嘅體驗。",
    "發行": "寫完錄完混完,點樣令你嘅廣東歌被更多人聽到,係獨立音樂人必須面對嘅課題。",
    "獨立": "獨立音樂人嘅路唔容易行,但正正因為自主,你可以用大公司做唔到嘅方式經營你嘅音樂事業。",
    "唱歌": "唱歌技巧係歌手嘅武器,咬字、感情、控制——每一環都影響最終嘅演繹效果。",
    "製作": "歌曲製作係由 demo 到成品嘅完整旅程,每個環節嘅細節加起嚟先至係最後俾人聽到嘅成品。",
}

SCENE = {
    "填詞": "香港嘅填詞傳統由黃霑、林振強到而家嘅新生代詞人,一直都係廣東歌嘅靈魂。",
    "旋律": "由許冠傑到陳奕迅,廣東歌旋律嘅演變反映咗香港音樂幾十年嘅風格流轉。",
    "編曲": "香港嘅編曲文化由七十年代 band sound 到而家嘅 bedroom production,技術唔同咗,但追求好聲音嘅心冇變。",
    "錄音": "無論係 Avon 錄音室嘅年代,定係而家屋企 bedroom studio 嘅年代,香港音樂人對錄音質素嘅追求從未停止。",
    "混音": "香港嘅混音文化由大型錄音室混音台到而家嘅 in-the-box 數碼混音,工具變咗,但耳朵嘅訓練永遠最重要。",
    "發行": "香港音樂發行由唱片公司主導嘅年代,到而家串流平台為王,玩法變咗,但「俾更多人聽到好歌」嘅目標冇變。",
    "獨立": "由 Hidden Agenda 到而家嘅各區 livehouse,香港獨立音樂場景一直都充滿生命力。",
    "唱歌": "由粵劇嘅唱功到而家嘅流行唱法,香港嘅唱歌技巧傳承幾十年,不斷演變。",
    "製作": "由監製到製作助理,完整嘅製作團隊係廣東歌質素嘅最後把關。而家 bedroom producer 都可以一個人完成晒,但 mindset 係一樣嘅。",
}

def sections(pfx, topic):
    intro = WHY_INTRO.get(pfx, "")
    scene = SCENE.get(pfx, "")
    return [
        (f"點解要學「{topic}」?",
         [f"{intro}{topic}正正係其中一個值得深入研究嘅技巧,佢可以令你嘅廣東歌更上一層樓,同聽眾建立更深嘅連結。",
          f"{scene}而「{topic}」呢個課題,正正係近年音樂圈討論得比較多嘅方向之一。只要你掌握到當中嘅竅門,你嘅作品都可以喺呢個場景入面發光發熱。",
          f"喺香港呢個寸金尺土嘅地方,做音樂往往要面對空間、時間同預算嘅限制,但正正係呢啲限制,逼出咗好多獨特嘅創意同做法。「{topic}」就係一個好好嘅例子——佢唔需要好多資源,但係只要你用心去鑽研,就可以為你嘅作品帶嚟意想不到嘅質感同深度。",
          f"香港本身係一個文化交匯嘅城市,廣東歌一直都係中西合璧嘅產物。「{topic}」呢種技巧正正反映咗呢種文化融合嘅特色——佢既承襲咗傳統廣東歌嘅精神,又融入咗現代音樂製作嘅技術,令新一代嘅音樂人可以造出既有香港味道,又有國際水準嘅作品。"]),
        (f"{topic}嘅基本概念",
         [f"要掌握「{topic}」,首先要理解佢背後嘅原理。每一個音樂制作環節都有自己嘅邏輯——佢要解決咩問題?佢嘅受眾係邊個?佢同其他環節點樣互相配合?只要你明白背後嘅邏輯,就可以喺創作過程入面搵到自己嘅位置,唔使再「盲摸摸」咁做。",
          "實戰上,建議你用「小步快跑」嘅方式入手。唔好一開始就想做最複雜嘅嘢,先由簡單、可控嘅部分開始,熟悉咗基本操作之後再慢慢增加難度。音樂制作就好似寫歌一樣,都要不斷試、不斷改、不斷進步,先至可以做到最好。",
          f"不過要留意,音樂制作最緊要係「用心」。聽眾之所以被打動,往往唔係因為你嘅技術有幾複雜,而係因為佢哋感受到作品入面嘅誠意。所以要將呢種「用心」貫穿每一個細節——由構思到執行,每一個選擇都問吓自己:咁做係咪真係對首歌最好?「{topic}」嘅精髓正正係喺啲細微位度見高低。",
          "另外,建立自己嘅參考清單都好緊要。每次聽到一首打動你嘅廣東歌,試吓寫低佢最吸引你嘅三個地方,日積月累你就會發現自己嘅審美方向越嚟越清晰,做嘢亦會越嚟越有信心。"]),
        ("實用技巧同具體步驟",
         [f"<strong>第一步:建立參考資料庫。</strong> 收集你鍾意嘅廣東歌作品,仔細分析佢哋點樣處理「{topic}」呢個環節。將每首歌嘅特點記錄落嚟,建立自己嘅資料庫。呢個資料庫會成為你日後創作嘅靈感來源,例如你可以用 Evernote 或 Notion 建一個專屬筆記本,分門別類咁儲埋所有參考資料。",
          "<strong>第二步:由簡單開始練習。</strong> 唔好一開始就挑戰複雜嘅作品。先由簡單嘅段落開始,例如一段四小節嘅loop或者一段四句嘅歌詞。熟練基本技巧之後,再慢慢增加難度。循序漸進係學習任何技巧嘅最佳方法,貪快反而會令你走冤枉路。",
          "<strong>第三步:反覆試驗同比較。</strong> 試吓用唔同嘅方法處理同一個段落,然後比較邊個效果最好。有時候最簡單嘅方法反而係最好嘅。將唔同版本儲存落嚟,過幾日再聽,通常會有新嘅發現同體會。你會發現第一個 reaction 同幾日後嘅 reaction 往往好唔同,呢個正正係判斷一個作品好壞嘅好方法。",
          "<strong>第四步:搵人俾意見你聽。</strong> 一個人閉門造車容易有盲點。將你嘅作品俾朋友或者其他音樂人聽,收集唔同嘅反饋。有時候一句簡單嘅意見,就可以令你發現自己睇唔到嘅問題。加入本地音樂人嘅網上社群,例如香港嘅 Discord server、Bandcamp 群組或者 Facebook group,都係搵到同行嘅好方法。",
          "<strong>第五步:持續優化同迭代。</strong> 音樂制作冇完美嘅一日,只有不斷進步嘅過程。每完成一個作品之後,花時間回顧同總結,睇吓有咩可以改進。呢種持續迭代嘅態度,正正係專業同業餘之間最大嘅分別。每一次嘅小改進,加起嚟就會成為你獨特嘅聲音。"]),
        ("常見錯誤同避免方法",
         [f"好多初學者喺學習「{topic}」嘅時候都會犯一啲常見嘅錯誤。第一個就係「好高騖遠」——一嚟就想做一啲超出自己能力嘅嘢,結果半途而廢。正確嘅做法係「由細做起」——先由簡單嘅部分開始,等經驗同信心累積之後,再挑戰更大嘅目標。成功係一步一步累積返嚟嘅,唔可以一步登天。",
          "第二個常見錯誤係「忽略咗基本功」。好多人想快啲見到成果,於是skip咗基礎練習,直接學一啲「進階技巧」。但係冇穩固嘅基本功,進階技巧只會變成花拳繡腿。無論你做音樂幾多年,每天抽少少時間練基本功,係專業音樂人嘅共同習慣。例如,每日抽十五分鐘練習樂器或者音階,長遠嚟講會為你帶嚟意想不到嘅回報。",
          "第三個錯誤係「唔肯問人」。好多人以為做音樂係自己一個人嘅事,結果事倍功半。其實音樂係一門溝通嘅藝術——要識得同其他音樂人交流、向前輩請教、參加本地音樂活動。呢啲「連結」,會令你嘅路行得更順,亦可以為你嘅音樂帶嚟更多機會同靈感。香港有好多免費或低成本嘅音樂工作坊同分享會,值得積極參與。"]),
        ("常見問題",
         [f"<strong>唔識樂理可以學「{topic}」嗎?</strong> 可以!好多出色嘅音樂人未必精通樂理,但佢哋都識得用耳朵判斷好壞。當然,學習基本樂理會令你嘅創作更加得心應手,不過最重要嘅始終係多聽多練多嘗試。好多廣東歌嘅經典作品都係「無譜創作」——即係話,創作者憑感覺同經驗寫出嚟嘅,樂理只係一個工具,唔係創作嘅目的。",
          "<strong>需要幾多錢先可以開始?</strong> 視乎你想去到幾盡。入門級大約三千至五千港幣已經足夠,包括基本設備同軟件。如果你已經有電腦,門檻仲更低。技術進步之後再逐步升級,唔使一開始就大花筒。好多出色嘅 bedroom producer 都係由好基本嘅設備開始,靠嘅係創意同堅持,唔係貴器材。",
          "<strong>點樣知道自己有冇進步?</strong> 最好嘅方法係將早期嘅作品儲存落嚟,定期翻聽比較。你會發現以前覺得好嘅作品,過咗幾個月再聽會發現好多不足——呢個正正代表你進步咗。另外,搵一個可信嘅人定期俾你 honest feedback,都係衡量進步嘅好方法。進步係一個過程,唔好期望一夜之間就能夠成為大師,因為每一個大師都係由初學者做起嘅。",
          "<strong>點樣令自己嘅作品更有香港味道?</strong> 多用香港本地嘅語言特色、地名同文化元素。例如尖沙咀、維港、茶餐廳、凍檸茶、紅Van、八達通、唐樓等,都可以令聽眾更有親切感。同時要留意粵語嘅語法同用字,避免過多書面語,保持口語嘅自然感覺。你嘅作品係你嘅故事——用你嘅語言去講你嘅故事,先至係最真實嘅。"]),
    ]

def render(slug, title, desc, pfx, topic):
    url = f"https://mycantopop.hk/articles/{slug}.html"
    body = [f"  <p>{desc} 呢篇文章會深入探討{topic}嘅技巧,由基本概念講到實際操作,再配合香港本地場景,令你可以即學即用,喺你嘅下一首廣東歌作品中應用出嚟。</p>"]
    for h2, paras in sections(pfx, topic):
        body.append(f"  <h2>{h2}</h2>")
        for p in paras:
            body.append(f"  <p>{p}</p>")
    body.append('  <div class="highlight-box">「音樂制作最緊要係用心同堅持。每個細節都值得打磨,因為聽眾會感受到。」— 廣東歌·為你創作團隊</div>')
    body.append('')
    body.append('  <div class="cta-box">')
    body.append('    <h3 class="serif">想將你嘅故事寫成廣東歌?</h3>')
    body.append('    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌,由填詞、作曲到錄音一站式完成。</p>')
    body.append('    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>')
    body.append('  </div>')
    ld = {"@context": "https://schema.org", "@type": "Article",
          "headline": title, "description": desc, "url": url,
          "datePublished": TODAY_ISO, "dateModified": TODAY_ISO,
          "publisher": {"@type": "Organization", "name": "廣東歌·為你", "url": "https://mycantopop.hk"}}
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html_mod.escape(title)} | 廣東歌·為你</title>
  <meta name="description" content="{html_mod.escape(desc)}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{html_mod.escape(title)}">
  <meta property="og:description" content="{html_mod.escape(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="廣東歌·為你">
  <meta property="og:locale" content="zh_HK">
  <link rel="canonical" href="{url}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Noto+Serif+TC:wght@400;500;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
{STYLE}
  <script type="application/ld+json">
  {json.dumps(ld, ensure_ascii=False)}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {html_mod.escape(title)}</p>
  <h1 class="serif">{html_mod.escape(title)}</h1>
  <p class="meta">{TODAY} · 廣東歌·為你</p>

{chr(10).join(body)}
</main>
<footer>© 2025 廣東歌·為你 · <a href="/">首頁</a> · <a href="/articles">文章</a></footer>
</body>
</html>'''

# (prefix, topic_fragment, rest, base-slug) — 29 articles for 2026-11-12
ARTICLES = [
    # ---- 填詞 (5) ----
    ("填詞", "填詞大牌檔奶茶檔",
     "點樣用大牌檔嘅絲襪奶茶同夥計叫賣寫出香港打工仔午餐時間嘅江湖豪情",
     "cantonese-lyrics-dai-pai-dong-dairy-milk-tea-working-class-lunch-hour-guide"),
    ("填詞", "填詞電車叮叮二樓",
     "點樣用電車二樓窗邊位嘅叮叮聲同慢駛節奏寫出港島慢活嘅城市觀察日記",
     "cantonese-lyrics-tram-ding-ding-second-floor-window-seat-slow-city-view-guide"),
    ("填詞", "填詞八號風球夜晚",
     "點樣用八號風球夜晚嘅風聲同燭光寫出停電屋企嘅一家人溫馨回憶",
     "cantonese-lyrics-typhoon-signal-eight-night-home-candle-power-cut-guide"),
    ("填詞", "填詞麻雀牌聲",
     "點樣用農曆新年屋企麻雀枱上嘅牌聲同笑聲寫出家庭團聚嘅聲音風景",
     "cantonese-lyrics-mahjong-tile-click-lunar-new-year-family-sound-memory-guide"),
    ("填詞", "填詞公屋走廊回聲",
     "點樣用公屋走廊腳步聲同鄰居鐵閘聲寫出屋邨長大嘅童年聲音印記",
     "cantonese-lyrics-public-housing-corridor-echo-childhood-neighbor-door-sound-guide"),

    # ---- 旋律 (4) ----
    ("旋律", "作曲五聲音階童謠",
     "點樣用五聲音階同兒歌式旋律為廣東歌加入返璞歸真嘅童真質感",
     "melody-writing-pentatonic-folk-scale-cantonese-nursery-rhyme-childlike-guide"),
    ("旋律", "作曲Dorian小調六級",
     "點樣用 Dorian 調式小六度音為廣東歌加入爵士酒吧夜色嘅微醺色彩",
     "melody-writing-dorian-mode-minor-sixth-jazz-tinged-night-lounge-color-guide"),
    ("旋律", "作曲八度大跳假起",
     "點樣用八度大跳同假起式副歌入口為廣東歌製造意想不到嘅驚喜 hook",
     "melody-writing-octave-jump-false-start-surprise-chorus-entry-hook-guide"),
    ("旋律", "作曲重複音饒唱",
     "點樣用重複音 rap-sing 混合式唱法為廣東歌加入節奏主導嘅律動感",
     "melody-writing-repeated-note-rap-sing-hybrid-rhythmic-chant-flow-guide"),

    # ---- 編曲 (4) ----
    ("編曲", "編曲太極劍聲",
     "點樣用太極劍出鞘聲同呼吸聲為廣東武俠風編曲加入武俠電影嘅氛圍",
     "arrangement-thai-chi-sword-sound-cinematic-wuxia-atmosphere-intro-guide"),
    ("編曲", "編曲舊單車鈴聲",
     "點樣用舊式單車叮鈴聲為廣東歌前奏加入舊香港街道嘅懷舊風景",
     "arrangement-bicycle-bell-old-hong-kong-street-nostalgic-intro-sound-guide"),
    ("編曲", "編曲飯煲蒸汽聲",
     "點樣用飯煲蒸汽聲同鑊氣聲為廣東歌加入屋企日常嘅煙火氣質感",
     "arrangement-rice-cooker-steam-kitchen-domestic-ambient-daily-life-texture-guide"),
    ("編曲", "編曲中式鑔倒吊",
     "點樣用中式小鑔同倒吊鑔聲為廣東歌橋段加入戲曲式嘅戲劇推進力",
     "arrangement-chinese-cymbal-crash-reversed-cymbal-swell-dramatic-rise-guide"),

    # ---- 錄音 (5) ----
    ("錄音", "錄音群眾合唱人牆",
     "點樣用一大班人企埋一齊合唱嘅 gang vocal 為廣東歌副歌加入 anthem 式能量",
     "recording-group-vocal-chant-crowd-gang-vocal-anthemic-chorus-energy-guide"),
    ("錄音", "錄音人聲雙軌微延遲",
     "點樣用人聲 double track 加極細延遲為廣東歌主唱增加厚度同寬度",
     "recording-vocal-double-track-slight-delay-thickening-widening-effect-guide"),
    ("錄音", "錄音衣櫃DIY錄音室",
     "點樣用衫櫃同上舖床單自製 bedroom vocal booth 提升廣東歌人聲乾淨度",
     "recording-closet-vocal-booth-diy-bed-sheet-acoustic-treatment-guide"),
    ("錄音", "錄音ASMR近咪口技",
     "點樣用 ASMR 近咪錄音捕捉嘴齒唇舌細節為廣東慢歌加入亲密耳語感",
     "recording-asmr-close-mic-mouth-detail-intimate-vocal-texture-guide"),
    ("錄音", "錄音房本底noise",
     "點樣利用房間本底 noise 同 take 之間嘅靜為廣東歌保留人味嘅呼吸空間",
     "recording-room-tone-silence-bed-track-between-take-ambience-guide"),

    # ---- 混音 (3) ----
    ("混音", "混音側鏈壓縮Bass",
     "點樣用 sidechain ducking 令廣東電子歌個低音跟住大鼓呼吸般 pumping",
     "mixing-sidechain-ducking-kick-pumping-bass-electronic-groove-guide"),
    ("混音", "混音HAAS立體擴闊",
     "點樣用 Haas effect 立體擴闊為廣東歌副歌製造音場變闊嘅爆發感",
     "mixing-stereo-widener-haas-effect-wide-chorus-spatial-guide"),
    ("混音", "混音副歌自動化推高",
     "點樣用 automation 喺副歌推高音量同效果為廣東歌製造心潮起伏",
     "mixing-automation-ride-chorus-energy-swell-dynamic-shape-guide"),

    # ---- 製作 (3) ----
    ("製作", "歌曲製作語音備忘",
     "點樣用手機語音備忘喺靈感一閃即逝之前將廣東歌 idea 快速捕捉落嚟",
     "production-demo-voice-memo-quick-capture-idea-before-forget-guide"),
    ("製作", "歌曲製作隱藏軌彩蛋",
     "點樣喺廣東歌碟尾或 B-side 加入 hidden track 為聽眾留一個驚喜彩蛋",
     "production-b-side-bonus-track-hidden-song-album-surprise-strategy-guide"),
    ("製作", "歌曲製作歌詞MV排版",
     "點樣用 lyric video 嘅字體排版同動態為廣東新歌喺 YouTube 做宣傳",
     "production-lyric-video-timeline-subtitle-typography-youtube-promo-guide"),

    # ---- 發行 (2) ----
    ("發行", "廣東歌發行旺角街招",
     "點樣用街頭貼街招同派傳單嘅舊派方法帮新廣東歌做地面宣傳",
     "release-street-poster-mongkok-physical-flyer-old-school-promo-guide"),
    ("發行", "廣東歌發行黑膠壓碟",
     "點樣為廣東歌做限量版黑膠壓碟令樂迷擁有一摸得著嘅實體珍藏",
     "release-vinyl-pressing-limited-edition-collector-physical-release-guide"),

    # ---- 獨立 (2) ----
    ("獨立", "獨立音樂人livehouse拆賬",
     "點樣同 livehouse 做 door deal 拆賬模式演出減低獨立音樂人虧損風險",
     "indie-live-house-door-deal-split-ticket-revenue-sharing-basics-guide"),
    ("獨立", "獨立音樂人周邊商品",
     "點樣設計 tee 布袋襟章等周邊商品為廣東歌創作建立演出以外嘅收入",
     "indie-marchandise-merch-tee-tote-pin-design-side-income-guide"),

    # ---- 唱歌 (1) ----
    ("唱歌", "廣東歌唱歌破音哽咽",
     "點樣有意識咁用破音同哽咽式唱法為廣東慢歌加入欲言又止嘅真實情感",
     "singing-false-voice-crack-purposeful-voice-break-emotional-choke-guide"),
]


def main():
    existing = {f[:-5] for f in os.listdir(ART_DIR) if f.endswith(".html")}
    assert len(ARTICLES) == 29, len(ARTICLES)
    new_articles = []
    for pfx, topic, rest, base in ARTICLES:
        slug = f"{base}{SUFFIX}"
        assert slug not in existing, f"collision: {slug}"
        title = f"廣東歌{topic}:{rest}"
        desc = f"{topic}完整指南。教你{rest}。"
        path = os.path.join(ART_DIR, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(slug, title, desc, pfx, topic))
        new_articles.append((slug, title, desc, pfx))

    assert len(new_articles) == 29

    # ---- update articles/index.html (prepend to top of grid, newest first) ----
    tag_map = {"填詞": "填詞技巧", "旋律": "作曲編曲", "編曲": "作曲編曲",
               "錄音": "錄音製作", "混音": "錄音製作", "製作": "音樂制作",
               "發行": "發行推廣", "獨立": "獨立音樂", "唱歌": "寫歌入門"}
    cards = []
    for slug, title, desc, pfx in new_articles:
        tag = tag_map[pfx]
        cards.append(f'''      <a class="card" href="/articles/{slug}.html">
        <span class="card-date">{TODAY}</span>
        <span class="card-tag">{tag}</span>
        <h2>{html_mod.escape(title)}</h2>
        <p>{html_mod.escape(desc)}</p>
        <span class="card-arrow">→</span>
      </a>''')
    cards_html = "\n".join(cards) + "\n"
    idx_path = os.path.join(ART_DIR, "index.html")
    with open(idx_path, encoding="utf-8") as f:
        idx = f.read()
    marker = '    <div class="grid">\n'
    assert marker in idx, "grid open marker not found"
    idx = idx.replace(marker, marker + cards_html, 1)
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx)

    # ---- update sitemap.xml ----
    sm_path = os.path.join(ROOT, "sitemap.xml")
    with open(sm_path, encoding="utf-8") as f:
        sm = f.read()
    entries = []
    for slug, title, desc, pfx in new_articles:
        entries.append(f'''  <url>
    <loc>https://mycantopop.hk/articles/{slug}.html</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>''')
    sm = sm.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm)

    print("created", len(new_articles), "articles")
    for s, t, *_ in new_articles:
        print(" -", s)


if __name__ == "__main__":
    main()

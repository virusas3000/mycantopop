#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch — 29 new Cantopop production articles (2026-10-07)."""
import os, json, html as html_mod

ROOT = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(ROOT, "articles")
TODAY = "2026年10月07日"
TODAY_ISO = "2026-10-07"

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
    "填詞": "廣東歌詞嘅世界博大精深，一個技巧嘅分別，就可以令首歌由「還好」變成「經典」。",
    "旋律": "廣東歌嘅旋律創作，既要遷就九聲六調嘅語音特性，又要有令人記住嘅 hook，係技術同感覺嘅結合。",
    "編曲": "編曲係決定一首歌氣質嘅關鍵——同一個 demo，唔同嘅編曲可以變成完全不同嘅作品。",
    "錄音": "錄音係將表演凝結成永恒嘅過程，一個細微嘅技巧差別，喺喇叭入面會被無限放大。",
    "混音": "混音係將所有聲音軌道揉成一件完整作品嘅藝術，直接決定聽眾最後聽到嘅體驗。",
    "發行": "寫完錄完混完，點樣令你嘅廣東歌被更多人聽到，係獨立音樂人必須面對嘅課題。",
    "獨立": "獨立音樂人嘅路唔容易行，但正正因為自主，你可以用大公司做唔到嘅方式經營你嘅音樂事業。",
    "唱歌": "唱歌技巧係歌手嘅武器，咬字、感情、控制——每一環都影響最終嘅演繹效果。",
}

SCENE = {
    "填詞": "香港嘅填詞傳統由黃霑、林振強到而家嘅新生代詞人，一直都係廣東歌嘅靈魂。",
    "旋律": "由許冠傑到陳奕迅，廣東歌旋律嘅演變反映咗香港音樂幾十年嘅風格流轉。",
    "編曲": "香港嘅編曲文化由七十年代 band sound 到而家嘅 bedroom production，技術唔同咗，但追求好聲音嘅心冇變。",
    "錄音": "無論係 Avon 錄音室嘅年代，定係而家屋企 bedroom studio 嘅年代，香港音樂人對錄音質素嘅追求從未停止。",
    "混音": "香港嘅混音文化由大型錄音室混音台到而家嘅 in-the-box 數碼混音，工具變咗，但耳朵嘅訓練永遠最重要。",
    "發行": "香港音樂發行由唱片公司主導嘅年代，到而家串流平台為王，玩法變咗，但「俾更多人聽到好歌」嘅目標冇變。",
    "獨立": "由 Hidden Agenda 到而家嘅各區 livehouse，香港獨立音樂場景一直都充滿生命力。",
    "唱歌": "由粵劇嘅唱功到而家嘅流行唱法，香港嘅唱歌技巧傳承幾十年，不斷演變。",
}

def sections(pfx, topic, base):
    intro = WHY_INTRO.get(pfx, "")
    scene = SCENE.get(pfx, "")
    return [
        (f"點解要學「{topic}」？",
         [f"{intro}{topic}正正係其中一個值得深入研究嘅技巧，佢可以令你嘅廣東歌更上一層樓，同聽眾建立更深嘅連結。",
          f"{scene}而「{topic}」呢個課題，正正係近年音樂圈討論得比較多嘅方向之一。只要你掌握到當中嘅竅門，你嘅作品都可以喺呢個場景入面發光發熱。"]),
        (f"{topic}嘅基本概念",
         [f"要掌握「{topic}」，首先要理解佢背後嘅原理。每一個音樂制作環節都有自己嘅邏輯——佢要解決咩問題？佢嘅受眾係邊個？佢同其他環節點樣互相配合？只要你明白背後嘅邏輯，就可以喺創作過程入面搵到自己嘅位置，唔使再「盲摸摸」咁做。",
          "實戰上，建議你用「小步快跑」嘅方式入手。唔好一開始就想做最複雜嘅嘢，先由簡單、可控嘅部分開始，熟悉咗基本操作之後再慢慢增加難度。音樂制作就好似寫歌一樣，都要不斷試、不斷改、不斷進步，先至可以做到最好。",
          "不過要留意，音樂制作最緊要係「用心」。聽眾之所以被打動，往往唔係因為你嘅技術有幾複雜，而係因為佢哋感受到作品入面嘅誠意。所以要將呢種「用心」貫穿每一個細節——由構思到執行，每一個選擇都問吓自己：咁做係咪真係對首歌最好？",
          "另外，建立自己嘅參考清單都好緊要。每次聽到一首打動你嘅廣東歌，試吓寫低佢最吸引你嘅三個地方，日積月累你就會發現自己嘅審美方向越嚟越清晰，做嘢亦會越嚟越有信心。"]),
        ("實用技巧同具體步驟",
         [f"<strong>第一步：建立參考資料庫。</strong> 收集你鍾意嘅廣東歌作品，仔細分析佢哋點樣處理「{topic}」呢個環節。將每首歌嘅特點記錄落嚟，建立自己嘅參考資料庫。呢個資料庫會成為你創作時嘅靈感來源同技術參考。",
          "<strong>第二步：由簡單開始練習。</strong> 唔好一開始就挑戰複雜嘅作品。先由簡單嘅段落開始，例如一段四小節嘅loop或者一段四句嘅歌詞。熟練基本技巧之後，再慢慢增加難度。循序漸進係學習任何技巧嘅最佳方法。",
          "<strong>第三步：反覆試驗同比較。</strong> 試吓用唔同嘅方法處理同一個段落，然後比較邊個效果最好。有時候最簡單嘅方法反而係最好嘅。將唔同版本儲存落嚟，過幾日再聽，通常會有新嘅發現同體會。",
          "<strong>第四步：搵人俾意見你聽。</strong> 一個人閉門造車容易有盲點。將你嘅作品俾朋友或者其他音樂人聽，收集唔同嘅反饋。有時候一句簡單嘅意見，就可以令你發現自己睇唔到嘅問題。加入本地音樂人嘅網上社群，都係搵到同行嘅好方法。",
          "<strong>第五步：持續優化同迭代。</strong> 音樂制作冇完美嘅一日，只有不斷進步嘅過程。每完成一個作品之後，花時間回顧同總結，睇吓有咩可以改進。呢種持續迭代嘅態度，正正係專業同業餘之間最大嘅分別。"]),
        ("常見錯誤同避免方法",
         [f"好多初學者喺學習「{topic}」嘅時候都會犯一啲常見嘅錯誤。第一個就係「好高騖遠」——一嚟就想做一啲超出自己能力嘅嘢，結果半途而廢。正確嘅做法係「由細做起」——先由簡單嘅部分開始，等經驗同信心累積之後，再挑戰更大嘅目標。成功係一步一步累積返嚟嘅，唔可以一步登天。",
          "第二個常見錯誤係「忽略咗基本功」。好多人想快啲見到成果，於是skip咗基礎練習，直接學一啲「進階技巧」。但係冇穩固嘅基本功，進階技巧只會變成花拳繡腿。无论你做音樂幾多年，每天抽少少時間練基本功，係專業音樂人嘅共同習慣。",
          "第三個錯誤係「唔肯問人」。好多人以為做音樂係自己一個人嘅事，結果事倍功半。其實音樂係一門溝通嘅藝術——要識得同其他音樂人交流、向前輩請教、參加本地音樂活動。呢啲「連結」，會令你嘅路行得更順，亦可以為你嘅音樂帶嚟更多機會同靈感。"]),
        ("常見問題",
         [f"<strong>唔識樂理可以學「{topic}」嗎？</strong> 可以！好多出色嘅音樂人未必精通樂理，但佢哋都識得用耳朵判斷好壞。當然，學習基本樂理會令你嘅創作更加得心應手，不過最重要嘅始終係多聽多練多嘗試。",
          "<strong>需要幾多錢先可以開始？</strong> 視乎你想去到幾盡。入門級大約三千至五千元已經足夠，包括基本設備同軟件。如果你已經有電腦，門檻仲更低。技術進步之後再逐步升級，唔使一開始就大花筒。",
          "<strong>點樣知道自己有冇進步？</strong> 最好嘅方法係將早期嘅作品儲存落嚟，定期翻聽比較。你會發現以前覺得好嘅作品，過咗幾個月再聽會發現好多不足——呢個正正代表你進步咗。另外，搵一個可信嘅人定期俾你 honest feedback，都係衡量進步嘅好方法。",
          "<strong>點樣令自己嘅作品更有香港味道？</strong> 多用香港本地嘅語言特色、地名同文化元素。例如尖沙咀、維港、茶餐廳、凍檸茶等，都可以令聽眾更有親切感。同時要留意粵語嘅語法同用字，避免過多書面語，保持口語嘅自然感覺。"]),
    ]

def render(slug, title, desc, pfx, topic, base):
    url = f"https://mycantopop.hk/articles/{slug}.html"
    body = [f"  <p>{desc} 呢篇文章會深入探討{topic}嘅技巧，由基本概念講到實際操作，再配合香港本地場景，令你可以即學即用。</p>"]
    for h2, paras in sections(pfx, topic, base):
        body.append(f"  <h2>{h2}</h2>")
        for p in paras:
            body.append(f"  <p>{p}</p>")
    body.append('  <div class="highlight-box">「音樂制作最緊要係用心同堅持。每個細節都值得打磨，因為聽眾會感受到。」— 廣東歌·為你創作團隊</div>')
    body.append('')
    body.append('  <div class="cta-box">')
    body.append('    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>')
    body.append('    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌，由填詞、作曲到錄音一站式完成。</p>')
    body.append('    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>')
    body.append('  </div>')
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
          "url": url, "publisher": {"@type": "Organization", "name": "廣東歌·為你", "url": "https://mycantopop.hk"}}
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

# (prefix, topic, rest_hk, base)
ARTICLES = [
    ("填詞", "填詞叮叮電車軌道節奏寫意", "點樣用電車叮叮聲同慢速視角寫出香港情懷", "cantonese-lyrics-ding-ding-tram-track-rhythm-imagery-guide"),
    ("填詞", "填詞深水埗布市場舊區人情寫法", "點樣用深水埗棚仔布販嘅日常寫出社區溫度", "cantonese-lyrics-sham-shui-po-fabric-market-humanity-guide"),
    ("填詞", "填詞紅Van小巴司機人生百態寫法", "點樣用小巴司機嘅日與夜寫出城市眾生相", "cantonese-lyrics-red-minibus-driver-life-stories-guide"),
    ("填詞", "填詞維多利亞港煙花聚散情感寫法", "點樣用跨年煙花嘅盛放同消散比喻關係無常", "cantonese-lyrics-victoria-harbour-fireworks-reunion-parting-guide"),
    ("填詞", "填詞大排檔鐘錶收音機老物件寫法", "點樣用懷舊物件觸發三代同堂嘅記憶", "cantonese-lyrics-dai-pai-dong-clock-radio-vintage-objects-guide"),
    ("填詞", "填詞港式茶餐廳凍檸茶溫度寫法", "點樣用一杯凍檸茶嘅溫度寫出生活餘溫", "cantonese-lyrics-hk-cha-chaan-teng-iced-lemon-tea-temperature-guide"),
    ("填詞", "填詞中秋節維園綵燈會團圓寫法", "點樣用中秋綵燈映照分隔兩地嘅思念", "cantonese-lyrics-mid-autumn-victoria-park-lantern-reunion-guide"),
    ("填詞", "填詞年三十晚倒數花市擠擁寫法", "點樣用年宵花市人潮寫出時間流逝嘅感觸", "cantonese-lyrics-lunar-new-year-flower-market-crowd-guide"),
    ("旋律", "作曲五聲音階中國風旋律設計", "點樣用宮商角徵羽寫出現代中國風廣東歌", "melody-writing-pentatonic-chinese-style-melody-guide"),
    ("旋律", "作曲副歌級進與跳進混合設計", "點樣平衡 conjunct 同 disjunct 令副歌易記又有驚喜", "melody-writing-chorus-stepwise-leap-mixed-contour-guide"),
    ("旋律", "作曲切分節奏嘻哈律動融合", "點樣用 syncopation 為廣東旋律加入 hip-hop 感", "melody-writing-syncopation-hiphop-groove-fusion-guide"),
    ("旋律", "作曲三連音抒情搖擺質感技巧", "點樣用 triplet 三連音營造溫柔搖籃式旋律", "melody-writing-triplet-lyrical-swing-feel-guide"),
    ("旋律", "作曲上行琶音希望感構建技巧", "點樣用 ascending arpeggio 建立勵志歌曲嘅昇華", "melody-writing-ascending-arpeggio-hopeful-climb-guide"),
    ("旋律", "作曲下行半音階憂鬱感設計", "點樣用 descending chromatic line 表達沉鬱情緒", "melody-writing-descending-chromatic-melancholy-guide"),
    ("旋律", "作曲裝飾音顫音哭腔運用", "點樣用 trill 同 vibrato 加強悲情歌嘅感染力", "melody-writing-ornament-trill-crying-tone-guide"),
    ("編曲", "編曲古箏琵琶民樂現代廣東歌", "點樣用 guzheng pipa 為廣東歌加古典詩意", "arrangement-guzheng-pipa-chinese-folk-modern-guide"),
    ("編曲", "編曲口琴藍調民謠都市感編排", "點樣用 harmonica 為廣東民謠加漂泊味道", "arrangement-harmonica-blues-folk-urban-guide"),
    ("編曲", "編曲尤克里里夏威夷度假編排", "點樣用 ukulele 打造夏日度假風廣東歌", "arrangement-ukulele-hawaiian-vacation-vibe-guide"),
    ("編曲", "編曲鋼片琴八音盒夢幻前奏", "點樣用 celesta music box 聲做回憶閃回前奏", "arrangement-celesta-music-box-dreamy-intro-guide"),
    ("編曲", "編曲大提琴低音敘事對話編排", "點樣用 cello 低音同旋律做對話式編曲", "arrangement-cello-bass-narrative-dialogue-guide"),
    ("錄音", "錄音近講效應控制與運用", "點樣善用 proximity effect 錄出親密感又唔會爆咪", "recording-vocal-proximity-effect-management-guide"),
    ("錄音", "錄音雙咪立體聲空間捕捉", "點樣用 spaced pair 錄出樂器嘅空間感", "recording-dual-microphone-stereo-spacing-guide"),
    ("錄音", "錄音隔音棉DIY錄音角落搭建", "點樣用平價物料喺屋企搭建臨時錄音空間", "recording-home-studio-soundproof-diy-booth-guide"),
    ("錄音", "錄音多軌疊加厚度控制技巧", "點樣疊加多層 vocal 又保持清晰度", "recording-multitrack-stacking-thickness-control-guide"),
    ("混音", "混音平行壓縮鼓組衝擊力", "點樣用 parallel compression 令鼓組更 punchy", "mixing-parallel-compression-drum-impact-guide"),
    ("混音", "混音側鏈壓縮電子律動呼吸", "點樣用 sidechain 壓縮造 pumping 效果", "mixing-sidechain-compression-electronic-pumping-guide"),
    ("混音", "混音自動化情緒起伏變化", "點樣用 automation 令歌曲有動態故事線", "mixing-automation-emotional-dynamic-contour-guide"),
    ("獨立", "獨立音樂人迷你專輯發行策略", "點樣用 EP 代替大碟快速建立作品目錄", "indie-music-ep-mini-album-release-strategy-guide"),
    ("唱歌", "廣東歌腹式呼吸穩定支撐", "點樣練 diaphragmatic breathing 支援長句演唱", "singing-diaphragmatic-breathing-support-guide"),
]


def main():
    existing = {f[:-5] for f in os.listdir(ART_DIR) if f.endswith(".html")}
    new_articles = []
    for pfx, topic, rest, base in ARTICLES:
        slug = f"{base}-1007"
        assert slug not in existing, f"collision: {slug}"
        title = f"廣東歌{topic}：{rest}"
        desc = f"{topic}完整指南。教你{rest}。"
        path = os.path.join(ART_DIR, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(slug, title, desc, pfx, topic, base))
        new_articles.append((slug, title, desc, pfx))

    assert len(new_articles) == 29, len(new_articles)

    # ---- update articles/index.html ----
    tag_map = {"填詞": "填詞技巧", "旋律": "作曲編曲", "編曲": "作曲編曲",
               "錄音": "錄音製作", "混音": "錄音製作", "發行": "發行推廣",
               "獨立": "獨立音樂", "唱歌": "寫歌入門"}
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
    marker = "    </div>\n\n  <footer>"
    assert marker in idx, "grid close marker not found"
    idx = idx.replace(marker, cards_html + marker, 1)
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

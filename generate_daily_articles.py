#!/usr/bin/env python3
"""Daily SEO article generator for mycantopop.hk"""

import os
import re
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

ARTICLES_DIR = Path.home() / "Desktop/mycantopop/articles"
SITEMAP_PATH = Path.home() / "Desktop/mycantopop/sitemap.xml"
INDEX_PATH = ARTICLES_DIR / "index.html"
BASE_URL = "https://mycantopop.hk"

TODAY = datetime.now()
DATE_STR = TODAY.strftime("%Y-%m-%d")
DATE_DISPLAY = TODAY.strftime("%Y年%m月%d日").replace("年0", "年").replace("月0", "月")
SLUG_SUFFIX = TODAY.strftime("%m%d")
DATE_TAG = f"guide-{SLUG_SUFFIX}"

# Load existing slugs to avoid duplicates
existing_slugs = {p.stem for p in ARTICLES_DIR.glob("*.html") if p.name != "index.html"}

TOPICS = [
    # 寫歌入門
    ("beginner-songwriting", "寫歌入門", [
        ("點樣用廣東話九聲六調寫出啱音嘅旋律線條", "cantonese-tone-melody-line-matching-guide"),
        ("點樣為廣東歌寫出一句入魂嘅開場白歌詞", "first-line-hook-opening-lyric-guide"),
        ("點樣用日常生活對白提煉廣東歌詞靈感", "daily-conversation-lyric-inspiration-guide"),
        ("點樣用限制寫作法逼自己突破廣東歌創作樽頸", "constraint-writing-breakthrough-guide"),
        ("點樣用情緒日記培養廣東歌創作手感", "emotion-journal-writing-habit-guide"),
    ]),
    # 填詞技巧
    ("cantonese-lyrics", "填詞技巧", [
        ("點樣用廣東話俗語入詞令聽眾一拍即中", "cantonese-slang-lyric-impact-guide"),
        ("點樣寫廣東歌詞入面嘅香港地標而不流於遊客視角", "hongkong-landmark-local-perspective-guide"),
        ("點樣用雙關語寫出廣東歌詞嘅弦外之音", "double-entendre-subtext-technique-guide"),
        ("點樣用數字入詞增加廣東歌嘅畫面感同記憶點", "number-lyric-imagery-memory-guide"),
        ("點樣用廣東話疊字寫出可愛又洗腦嘅歌詞", "reduplication-catchy-lyric-guide"),
    ]),
    # 作曲編曲
    ("melody-writing", "作曲編曲", [
        ("點樣用五聲音階寫出現代廣東流行曲旋律", "pentatonic-modern-cantopop-melody-guide"),
        ("點樣用經過音同輔助音令廣東歌旋律更流暢", "passing-auxiliary-note-smooth-melody-guide"),
        ("廣東歌編曲弦樂四重奏點樣由預錄sample做到真人感", "string-quartet-sample-realistic-guide"),
        ("點樣用合成器pad為廣東抒情歌鋪陳氛圍", "synth-pad-atmosphere-ballad-guide"),
        ("點樣用reverse cymbal同riser做廣東歌轉場張力", "riser-transition-tension-arrangement-guide"),
    ]),
    # 錄音製作
    ("recording", "錄音製作", [
        ("點樣喺香港劏房錄出乾淨嘅廣東歌人聲", "subdivided-flat-clean-vocal-recording-guide"),
        ("廣東歌唱腔咬字點樣平衡清晰同自然", "cantonese-diction-clarity-natural-guide"),
        ("點樣用automation令廣東歌混音有呼吸感", "automation-breathing-mix-guide"),
    ]),
    # 音樂制作
    ("production", "音樂制作", [
        ("點樣為廣東歌demo做一個令監製一聽就明嘅arrangement", "demo-arrangement-producer-communication-guide"),
        ("廣東歌製作預算點樣分配錄音混音mastering比例先合理", "budget-allocation-recording-mixing-mastering-guide"),
        ("點樣用reference track客觀評估自己嘅廣東歌混音質素", "reference-track-mix-quality-assessment-guide"),
        ("廣東歌製作點樣同session musician溝通先唔會有誤會", "session-musician-communication-guide"),
    ]),
    # 發行推廣
    ("release", "發行推廣", [
        ("廣東歌發行點樣寫press release令香港音樂媒體願意報道", "press-release-hk-music-media-guide"),
        ("點樣用Instagram carousel貼文宣傳廣東歌背後故事", "instagram-carousel-storytelling-promo-guide"),
        ("廣東歌點樣透過香港獨立廠牌發行同保持創作自主權", "indie-label-creative-control-guide"),
        ("點樣用YouTube premiere搞廣東歌首播凝聚樂迷", "youtube-premiere-fan-gathering-guide"),
    ]),
    # 獨立音樂
    ("indie-music", "獨立音樂", [
        ("香港獨立音樂人點樣用Bandcamp建立直接同樂迷嘅關係", "bandcamp-direct-fan-relationship-guide"),
        ("點樣為廣東獨立樂隊設計一套有辨識度嘅周邊商品", "band-merch-identity-design-guide"),
        ("香港獨立音樂人點樣由busking開始累積第一批樂迷", "busking-first-fanbase-building-guide"),
        ("廣東獨立音樂點樣透過Discord群組建立死忠樂迷社群", "discord-diehard-fan-community-guide"),
    ]),
]

# Extra topics to reach 29
EXTRA_TOPICS = [
    ("beginner-songwriting", "寫歌入門", [
        ("點樣用AI工具輔助廣東歌創作但唔會失去自己風格", "ai-assisted-writing-style-preservation-guide"),
        ("點樣將一首失敗嘅廣東歌demo變成有價值嘅學習材料", "failed-demo-learning-material-guide"),
    ]),
    ("cantonese-lyrics", "填詞技巧", [
        ("點樣用廣東話嘅語氣助詞令歌詞更地道更生動", "modal-particle-colloquial-lyric-guide"),
        ("點樣寫廣東歌詞入面嘅離別場景而唔會流於俗套", "farewell-scene-cliche-avoidance-guide"),
    ]),
    ("melody-writing", "作曲編曲", [
        ("點樣用chromatic passing chord為廣東歌加入意外和聲色彩", "chromatic-passing-chord-color-guide"),
        ("廣東歌bridge段落點樣寫先可以將情緒推到最高", "bridge-emotional-climax-writing-guide"),
    ]),
    ("recording", "錄音製作", [
        ("點樣用多咪高峰技巧錄製廣東歌acoustic live session", "multi-mic-acoustic-live-session-guide"),
    ]),
    ("release", "發行推廣", [
        ("廣東歌點樣用TikTok sound page令歌曲被二次創作", "tiktok-sound-page-ugc-guide"),
    ]),
]

ALL_TOPICS = TOPICS + EXTRA_TOPICS

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | 廣東歌·為你</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
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
  {{"@context": "https://schema.org", "@type": "Article", "headline": "{title}", "description": "{description}", "url": "{url}", "datePublished": "{date_iso}", "dateModified": "{date_iso}", "publisher": {{"@type": "Organization", "name": "廣東歌·為你", "url": "https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {title}</p>
  <h1 class="serif">{title}</h1>
  <p class="meta">{date_display} · 廣東歌·為你</p>

  <p>{description}。呢篇文章會深入探討「{short_topic}」嘅技巧，由基本概念講到實戰應用，再配合香港本地音樂場景，令你可以即學即用，將呢個技巧融入你嘅廣東歌創作之中。</p>
  <h2>點解要學「{short_topic}」？</h2>
  <p>廣東歌經歷咗半個世紀嘅發展，由許冠傑嘅市井民謠、張國榮梅艷芳嘅華麗舞台，到而家林家謙、MC張天賦、陳蕾呢啲新世代音樂人嘅多元風格，每一代都有自己嘅聲音。「{short_topic}」正正係一個可以令你嘅作品喺芸芸廣東歌之中脫穎而出嘅重要環節——佢唔單止係一個技術，更加係一種態度，一種對音樂嘅執著。</p>
  <p>香港音樂工業由七十年代嘅小本經營，到而家一個人喺房間都可以做完整首歌，技術門檻雖然低咗，但要突圍而出反而變得更加困難。「{short_topic}」呢一個課題，正係近年香港音樂圈入面討論得相當熱烈嘅方向之一。只要你掌握到當中嘅竅門，你嘅廣東歌都有機會喺KKBOX、MOOV、Spotify呢啲串流平台、喺樂迷心中發光發熱。</p>
  <p>特別喺香港呢個市場咁細、競爭咁激烈嘅環境，細節往往決定成敗。一首歌能唔能夠喺聽眾心中留低印象，好多時就係睇你肯唔肯喺「{short_topic}」呢一環落足心機。今次就等我哋一齊由淺入深，拆解呢個題目嘅精髓。</p>
  <h2>「{short_topic}」嘅核心概念</h2>
  <p>要真正掌握「{short_topic}」，首先要理解佢背後嘅邏輯同美學。每一個音樂制作嘅環節都有自己嘅存在價值——佢要解決咩問題？佢嘅受眾係邊類聽眾？佢同歌詞、旋律、編曲、錄音點樣互相配合？只要你明白背後嘅道理，就可以喺創作過程入面搵到自己嘅聲音，唔使再「盲摸摸」咁模仿人哋嘅風格。</p>
  <p>實戰上，建議你用「小步快跑」嘅方式入手。唔好一開始就想一take過做到最完美，先由最簡單、最可控嘅部分做起，熟悉咗基本操作之後再慢慢挑戰複雜嘅變化。音樂創作就好似學功夫一樣，紮馬紮得穩，招式先可以耍得好看。尤其係廣東歌呢種講求精膽細膩嘅曲種，每一個細節都值得花時間打磨。</p>
  <p>不過要記住，技術只係工具，情感先係靈魂。聽眾之所以會被一首廣東歌打動，往往唔係因為你嘅製作有幾複雜、技巧有幾高超，而係因為佢哋感受到作品入面嘅真誠。所以要將呢份「用心」貫穿每一個環節——由構思到執行，每一個細節都問吓自己：咁樣做係咪真係對首歌最好？聽眾聽到嘅時候會有咩反應？</p>
  <p>另外，建立自己嘅參考資料庫都十分重要。每次聽到一首觸動你嘅廣東歌，不妨寫低佢最吸引你嘅三個地方，日積月累你就會發現自己嘅審美方向越嚟越清晰，做嘢亦會越嚟越有自信同方向感。好多成功嘅香港音樂人都係咁樣練成嘅。</p>
  <h2>實用技巧同具體步驟</h2>
  <p><strong>第一步：建立參考資料庫。</strong> 收集你鍾意嘅廣東歌作品，仔細分析佢哋點樣處理「{short_topic}」呢一個環節。將每首歌嘅特點、亮點同你嘅感受記錄落嚟，建立屬於自己嘅參考資料庫。呢個資料庫會成為你創作路上嘅靈感源泉同技術參考，無論係卡關定係想突破，都可以返嚟搵靈感。</p>
  <p><strong>第二步：由簡單開始練習。</strong> 唔好一開始就挑戰最複雜嘅作品。先由簡單嘅段落開始，例如一段四小節嘅loop、一段四句嘅歌詞、一個簡短嘅編曲段落。熟練基本技巧之後，再慢慢增加難度。循序漸進，先係學習任何技巧嘅最佳方法，寫廣東歌都唔例外。</p>
  <p><strong>第三步：反覆試驗同比較。</strong> 試吓用唔同嘅方法處理同一個段落，然後比較邊一個效果最好。有時候最簡單直接嘅做法反而最有力。將唔同版本儲存落嚟，隔幾日再聽，通常會有新嘅發現同體會，慢慢你就會發展出自己嘅判斷力同品味。</p>
  <p><strong>第四步：搵人俾真誠嘅意見。</strong> 一個人閉門造車容易有盲點。將你嘅作品俾朋友、音樂人、甚至網上社群嘅同行聽，收集唔同角度嘅反饋。有時候一句簡單嘅意見，就可以點醒你睇唔到嘅問題。香港有好多音樂人嘅Discord同Telegram群組，都係搵戰友嘅好地方。</p>
  <p><strong>第五步：持續優化同迭代。</strong> 音樂制作冇「完美」呢一日，只有不斷進步嘅過程。每完成一個作品之後，花時間坐低回顧同總結，睇吓有咩可以改進，記錄落嚟下次應用。呢種持續迭代嘅態度，正正係專業同業餘之間最大嘅分別。</p>
  <h2>常見錯誤同避免方法</h2>
  <p>好多初學者喺學習「{short_topic}」嘅時候都會犯一啲常見錯誤。第一個係「好高騖遠」——一嚟就想做啲超出自己能力範圍嘅複雜作品，結果半途而廢。正確做法係「由細做起」——先由簡單嘅部分開始，等經驗同信心累積起嚟之後，再挑戰更大嘅目標。成功係一步一步累積返嚟，唔可以一步登天。</p>
  <p>第二個常見錯誤係「忽略基本功」。好多人想快啲見到成果，於是skip咗基礎練習，直接學一啲「進階技巧」。但係冇穩固嘅基本功，進階技巧只會係花拳繡腿。無論你做音樂幾多年，每日抽少少時間練基本功，係專業音樂人嘅共同習慣，亦係佢哋能夠一直進步嘅秘密。</p>
  <p>第三個錯誤係「唔肯問人、唔肯分享」。好多人以為做音樂係自己一個人嘅事，結果事倍功半。其實音樂係一門溝通嘅藝術——要識得同其他音樂人交流、向前輩請教、參加本地音樂活動同工作坊。呢啲「連結」，會令你嘅路行得更順，亦可以為你嘅音樂帶嚟更多機會同靈感。</p>
  <h2>常見問題</h2>
  <p><strong>唔識樂理可以學「{short_topic}」嗎？</strong> 絕對可以！好多出色嘅廣東音樂人未必精通樂理，但佢哋識得用耳朵判斷好壞。當然，學習基本樂理會令你嘅創作更得心應手，但最重要始終係多聽、多練、多試，靠實戰經驗累積觸覺。</p>
  <p><strong>要幾多預算先可以開始？</strong> 視乎你想去到幾盡。入門級大約三千至五千元港幣已經足夠開展基本嘅創作，包括軟件同基本設備。如果你已經有電腦，門檻仲低，有好多免費嘅DAW同plugin可以俾你起步。技術成熟之後再逐步升級設備，唔使一開始就大花筒。</p>
  <p><strong>點樣知道自己有冇進步？</strong> 最好嘅方法係將你早期嘅作品儲存落嚟，定期翻聽比較。你會發現以前覺得好嘅作品，過幾個月再聽會發現好多不足——呢個正正代表你進步咗。另外，搵一個可信嘅前輩定期俾你真誠嘅feedback，都係衡量進步嘅好方法。</p>
  <p><strong>點樣令作品更有香港味道？</strong> 多用香港本地嘅語言特色、地名、文化符號同生活場景。例如茶餐廳、凍檸茶、維港、廟街呢啲香港人熟悉嘅元素，都可以令聽眾更有親切感同共鳴。同時要留意粵語嘅語法同用字，避免過多書面語，保持口語嘅自然感同生命力。</p>

  <div class="highlight-box">「音樂制作最緊要係用心同堅持。每個細節都值得打磨，因為聽眾會感受到。」— 廣東歌·為你創作團隊</div>

  <div class="cta-box">
    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>
    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌，由填詞、作曲到錄音一站式完成。</p>
    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>
  </div>
</main>
<footer>© 2025 廣東歌·為你 · <a href="/">首頁</a> · <a href="/articles">文章</a></footer>
</body>
</html>"""

def make_title(q, prefix, cat):
    return f"{prefix}{q}"

def make_slug(base, topic):
    return f"{topic}-{base}-{SLUG_SUFFIX}"

def make_description(q):
    return f"{q}"

articles = []
for topic_prefix, category, items in ALL_TOPICS:
    for title_q, slug_base in items:
        title = make_title(title_q, f"廣東歌{category}：", category)
        slug = make_slug(slug_base, topic_prefix)
        if slug in existing_slugs:
            # try alternative
            alt_slug = f"{slug.replace(SLUG_SUFFIX, str(int(SLUG_SUFFIX)+1))}"
            if alt_slug in existing_slugs:
                alt_slug = f"{slug_base}-{topic_prefix}-{SLUG_SUFFIX}"
                if alt_slug in existing_slugs:
                    continue
            slug = alt_slug
        url = f"{BASE_URL}/articles/{slug}.html"
        short_topic = title_q.split("點樣")[-1].split("用")[-1].strip("？?")
        if len(short_topic) > 20:
            short_topic = title_q[:15]
        desc = make_description(title_q)
        articles.append({
            "slug": slug,
            "title": title,
            "description": desc,
            "url": url,
            "short_topic": short_topic,
            "category": category,
            "date_iso": DATE_STR,
            "date_display": DATE_DISPLAY,
        })

# Generate files
for art in articles:
    html = HTML_TEMPLATE.format(**art)
    path = ARTICLES_DIR / f"{art['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    existing_slugs.add(art["slug"])

print(f"Generated {len(articles)} articles")

# Update index.html
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_html = f.read()

new_cards = []
for art in articles:
    card = f'''      <a class="card" href="/articles/{art["slug"]}.html">
        <span class="card-date">{art["date_display"]}</span>
        <span class="card-tag">{art["category"]}</span>
        <h2>{art["title"]}</h2>
        <p>{art["description"]}</p>
        <span class="card-arrow">→</span>
      </a>'''
    new_cards.append(card)

cards_block = "\n".join(new_cards)
marker = '<div class="grid">'
if marker in index_html:
    insert_pos = index_html.index(marker) + len(marker)
    index_html = index_html[:insert_pos] + "\n" + cards_block + index_html[insert_pos:]
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Updated index.html")
else:
    print("Warning: grid marker not found in index.html")

# Update sitemap
with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = []
for art in articles:
    url_block = f'''  <url>
    <loc>{art["url"]}</loc>
    <lastmod>{art["date_iso"]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>'''
    new_urls.append(url_block)

urls_block = "\n".join(new_urls)
sitemap = sitemap.replace("</urlset>", urls_block + "\n</urlset>")
with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(sitemap)
print("Updated sitemap.xml")

# Output list for commit
print("\n".join(art["slug"] for art in articles))

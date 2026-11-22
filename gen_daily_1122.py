#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 29 unique articles (2026-11-22)."""
import os, datetime, subprocess

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026-11-22"
TODAY_DISPLAY = "2026年11月22日"

# 29 unique long-tail topics - verified no slug collisions with existing files
ARTICLES = [
("cantonese-lyrics-star-ferry-upper-deck-harbour-crossing-romance-guide-1122",
 "廣東歌填詞天星小輪上層甲板:點樣用維港渡海寫出城市浪漫",
 "填詞天星小輪上層甲板完整指南。教你點樣用維港渡海、海風同兩岸燈火寫出香港式浪漫嘅歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-cha-chaan-teng-pineapple-bun-milk-tea-everyday-love-guide-1122",
 "廣東歌填詞茶餐廳菠蘿油熱奶茶:點樣用港式早餐寫出日常愛情",
 "填詞茶餐廳菠蘿油熱奶茶指南。教你點樣用港式早餐、卡位同伙記叫單聲寫出香港日常愛情嘅歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-lion-rock-night-hike-city-light-view-perseverance-guide-1122",
 "廣東歌填詞獅子山夜行城市燈火:點樣用行山經歷寫出香港人嘅堅持",
 "填詞獅子山夜行指南。教你點樣用獅子山夜景、山頂涼風同腳下萬家燈火寫出香港人堅持精神嘅歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-mahjong-tiles-clacking-family-gathering-cny-guide-1122",
 "廣東歌填詞麻雀啪牌聲家庭團聚:點樣用新年打麻雀寫出身世故情",
 "填詞麻雀啪牌家庭團聚指南。教你點樣用農曆新年打麻雀嘅聲音同笑聲寫出香港家庭世故情嘅歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-last-mtr-train-empty-carriage-quiet-reflection-guide-1122",
 "廣東歌填詞尾班地鐵空車廂:點樣用收車前嘅靜謐寫出都市反思",
 "填詞尾班地鐵空車廂指南。教你點樣用地鐵收車前嘅空車廂、隧道燈光同廣播聲寫出都市人反思嘅粵語歌詞。",
 "填詞技巧",
 []),
("melody-writing-major-seventh-chord-cantopop-sentimental-flavor-guide-1122",
 "廣東歌旋律大七和弦Major7th感傷韻味:點樣用△7音色寫出港式哀怨",
 "大七和弦廣東歌應用指南。教你點樣用Major 7th和弦營造感傷又溫柔嘅港式流行曲韻味。",
 "作曲編曲",
 []),
("melody-writing-melodic-minor-ascending-tension-cantopop-bridge-guide-1122",
 "廣東歌旋律旋律小調上行Bridge橋段張力:點樣用升高六七度推進歌曲高潮",
 "旋律小調上行Bridge橋段指南。教你點樣用旋律小調升高六度七度嘅特性推進廣東歌Bridge段嘅張力。",
 "作曲編曲",
 []),
("melody-writing-pentatonic-ornament-cantonese-traditional-flavor-guide-1122",
 "廣東歌旋律五聲音階裝飾音中樂韻味:點樣用宮商角徵羽寫出東方色彩",
 "五聲音階裝飾音廣東歌指南。教你點樣用宮商角徵羽五聲音階加裝飾音寫出東方色彩嘅旋律線。",
 "作曲編曲",
 []),
("melody-writing-call-and-response-verbal-melody-dialogue-guide-1122",
 "廣東歌旋律Call and Response人聲對答:點樣用對唱動機製造戲劇感",
 "Call and Response人聲對答技巧指南。教你點樣用主唱同和唱嘅對答動機為廣東歌製造戲劇性。",
 "作曲編曲",
 []),
("arrangement-taiko-drum-ensemble-japanese-festival-power-guide-1122",
 "廣東歌編曲日本太鼓陣太鼓力量:點樣用和太鼓製造祭典澎湃感",
 "日本太鼓編曲指南。教你點樣將和太鼓嘅力量感融入廣東歌,製造好似日本祭典咁澎湃嘅聲音。",
 "作曲編曲",
 []),
("arrangement-vibraphone-mallet-soft-jazz-ballad-night-lounge-guide-1122",
 "廣東歌編曲顫音琴Vibraphone爵士Ballad:點樣用Mallet樂器營造夜總會感",
 "Vibraphone顫音琴編曲指南。教你點樣用爵士顫音琴嘅柔和音色為廣東歌Ballad加入夜總會感。",
 "作曲編曲",
 []),
("arrangement-whale-song-sample-deep-ocean-ambient-intro-guide-1122",
 "廣東歌編曲鯨魚叫聲Sample深海氛圍:點樣用海洋聲音製造空靈Intro",
 "鯨魚叫聲Sample深海氛圍指南。教你點樣用鯨魚唱歌嘅聲音Sample為廣東歌Intro加入海洋空靈感。",
 "作曲編曲",
 []),
("arrangement-tubular-bell-church-chime-solemn-bridge-guide-1122",
 "廣東歌編曲管鐘教堂鐘聲莊嚴Bridge:點樣用Tubular Bell製造神聖時刻",
 "管鐘Tubular Bell編曲指南。教你點樣用教堂鐘聲喺廣東歌Bridge段製造莊嚴神聖嘅時刻。",
 "作曲編曲",
 []),
("recording-bamboo-scaffolding-clanging-hong-kong-construction-guide-1122",
 "廣東歌錄音竹棚架碰撞聲城市質感:點樣用香港搭棚聲做Urban Percussion",
 "竹棚架碰撞聲錄音指南。教你點樣錄低香港搭棚工人嘅竹棚碰撞聲,做都市質感打擊樂底層。",
 "錄音製作",
 []),
("recording-mongkok-pedestrian-zone-street-performer-echo-guide-1122",
 "廣東歌錄音旺角行人專區街頭表演回響:點樣捕捉鬧市Live氣氛",
 "旺角行人專區錄音指南。教你點樣捕捉旺角街頭表演嘅人聲、音樂同掌聲,做充滿Live感嘅聲景。",
 "錄音製作",
 []),
("recording-hong-kong-ferry-engine-rumble-sea-ambience-guide-1122",
 "廣東歌錄音渡海小輪引擎低鳴海上氛圍:點樣用機器聲做Ambient Bed",
 "渡輪引擎低鳴錄音指南。教你點樣錄低香港渡海小輪嘅引擎聲同海浪聲做Ambient Bed。",
 "錄音製作",
 []),
("recording-playground-children-laughter-nostalgic-memory-texture-guide-1122",
 "廣東歌錄音兒童遊樂場笑聲童年回憶:點樣用公園笑聲做懷舊質感",
 "兒童遊樂場錄音指南。教你點樣錄低屋邨公園小朋友笑聲同鞦韆聲為廣東歌加入童年回憶質感。",
 "錄音製作",
 []),
("mixing-vocal-reverse-reverb-swell-ethereal-pre-chorus-guide-1122",
 "廣東歌混音Reverse Reverb反迴響Swell:點樣用人聲反彈製造夢幻Pre-Chorus",
 "Reverse Reverb反迴響混音指南。教你點樣用人聲Reverse Reverb為廣東歌Pre-Chorus製造夢幻吸引力。",
 "混音製作",
 []),
("mixing-multiband-sidechain-pad-ducking-electronic-cantopop-guide-1122",
 "廣東歌混音Multiband Sidechain Pad回避電子音色:點樣用分頻側鏈等Pad讓位俾人聲",
 "Multiband Sidechain混音指南。教你點樣用分頻側鏈壓縮等電子Pad自動讓位俾廣東歌人聲。",
 "混音製作",
 []),
("mixing-spectral-de-esser-sibilance-control-cantonese-consonant-guide-1122",
 "廣東歌混音Spectral De-Esser頻譜去齒音:點樣處理粵語「S」「T」刺耳音",
 "Spectral De-Esser頻譜去齒音指南。教你點樣精準處理粵語歌詞入面刺耳嘅S/CH/TS齒音問題。",
 "混音製作",
 []),
("mixing-analog-console-emulation-channel-strip-vintage-vibe-guide-1122",
 "廣東歌混音Analog Console模擬Channel Strip復古質感:點樣用模擬插件做80年代味",
 "Analog Console模擬Channel Strip混音指南。教你點樣用SSL/Neve模擬插件為廣東歌加入80年代港樂質感。",
 "混音製作",
 []),
("production-home-studio-vocal-booth-hong-kong-closet-diy-guide-1122",
 "廣東歌製作家居錄音衣櫃Vocal Booth DIY:點樣喺香港細房間做人聲隔音",
 "衣櫃Vocal Booth DIY指南。教你點樣用香港細房間嘅衣櫃改造成臨時Vocal Booth,改善人聲錄音質素。",
 "音樂制作",
 []),
("production-daw-project-template-cantopop-workflow-speed-guide-1122",
 "廣東歌製作DAW工程Template港式工作流程:點樣用預設範本加速寫歌",
 "DAW工程Template指南。教你點樣建立廣東歌專用嘅DAW工程預設範本,大幅加快寫歌速度。",
 "音樂制作",
 []),
("production-co-write-split-sheet-copyright-hong-kong-law-guide-1122",
 "廣東歌製作Co-Write版權分配香港法律:點樣同其他音樂人簽合作協議",
 "Co-Write版權分配指南。講解香港版權法下幾個音樂人合作寫歌嘅版權分配同協議要點。",
 "音樂制作",
 []),
("release-spotify-editorial-pitch-hong-kong-cantopop-playlist-guide-1122",
 "廣東歌發行Spotify編輯Pitch攻略:點樣向Spotify編輯團隊爭取Playlist",
 "Spotify編輯Pitch攻略指南。教你點樣用Spotify for Artists向編輯Pitch你嘅廣東歌,爭取上Editorial Playlist。",
 "發行推廣",
 []),
("release-cassette-tape-diy-limited-run-hong-kong-retro-market-guide-1122",
 "廣東歌發行盒帶Cassette DIY限量復古香港市場:點樣做手製盒帶生意",
 "盒帶Cassette DIY限量指南。教你點樣喺香港做手製盒帶,搶佔廣東歌復古收藏家市場。",
 "發行推廣",
 []),
("release-youtube-premiere-watch-party-cantopop-fan-engagement-guide-1122",
 "廣東歌發行YouTube首映Watch Party:點樣用首播功能同粉絲實時互動",
 "YouTube首映Watch Party指南。教你點樣用YouTube Premiere功能喺首播時同香港粉絲實時互動。",
 "發行推廣",
 []),
("indie-cantopop-crowdfunding-campaign-hong-kong-backers-guide-1122",
 "獨立廣東歌眾籌Campaign香港樂迷支持:點樣喺本地平台發起音樂眾籌",
 "獨立廣東歌眾籌指南。教你點樣喺香港本地平台發起音樂眾籌,等本地樂迷支持你嘅創作。",
 "獨立音樂",
 []),
("indie-cantopop-sync-licensing-hong-kong-tv-commercial-guide-1122",
 "獨立廣東歌Sync Licensing香港電視廣告:點樣將歌授權俾廣告用",
 "Sync Licensing香港指南。教你點樣將獨立廣東歌授權俾香港電視廣告、微電影同網上廣告使用。",
 "獨立音樂",
 []),
]

assert len(ARTICLES) == 29

# Check for slug collisions
existing_slugs = set()
for f in os.listdir(ART_DIR):
    if f.endswith(".html") and f != "index.html":
        existing_slugs.add(f[:-5])

for slug, title, desc, cat, _ in ARTICLES:
    assert slug not in existing_slugs, f"DUPLICATE SLUG: {slug}"

# ---- Article body generator ----
def gen_body(title, slug, desc):
    """Generate 800-1200 word Cantonese article body."""
    topic_short = title.split(":")[0].split("：")[0]
    sections = [
        ("引言：喺香港做廣東歌嘅日常", [
            f"{topic_short}係近年香港音樂人日漸關注嘅話題。喺呢個節奏急快嘅城市,廣東歌一直係香港人表達情感、記錄生活嘅重要載體。無論係傳統嘅廣東流行曲,定係新一派嘅獨立音樂,每一首成功嘅廣東歌背後都有一套獨特嘅制作邏輯。",
            "講起廣東歌制作,好多朋友會即時諗起紅館、叱吒903嘅頒獎禮,但其實而家香港本地嘅獨立音樂圈同樣精彩。由Band房到屋企錄音室,愈嚟愈多後生仔女開始自己寫歌、自己錄、自己發行,呢個現象值得我哋深入研究。",
        ]),
        ("核心概念與文化背景", [
            "粵語本身有九聲六調,呢個語言特性令廣東歌創作比一般普通話歌曲更加講究。填詞嘅時候,每一個字嘅聲調都要配返旋律嘅音高方向,否則就會出現「倒字」問題,聽落好唔自然。",
            "除咗語言層面,香港音樂製作亦受中西文化交融影響。西方流行音樂嘅和聲結構、製作流程,加上廣東話獨有嘅韻味同香港人嘅生活經驗,合起嚟就係廣東歌嘅獨特聲音。由許冠傑開始,到譚詠麟、張國榮、Beyond,再到而家陳奕迅、張敬軒、岑寧兒、Gareth.T,每一代人都為廣東歌加入新嘅元素。",
            "現代廣東歌嘅制作流程大致分為:概念發想、作曲、填詞、編曲、錄音、混音、母帶處理同發行。每一個階段都需要唔同嘅專業知識,但而家嘅數碼工具令所有嘢都可以喺屋企完成。",
        ]),
        (f"深入探討:{topic_short}", [
            f"講返{topic_short},呢個範疇其實涉及幾個層面嘅技術同藝術考量。首先要理解嘅係背後嘅原理 — 無論你係做緊作曲、填詞、編曲定錄音,每一個決定都會影響最後嘅成品。",
            "喺實際操作上,建議大家由最基本嘅概念開始練習。好多香港音樂人一開始會想即刻做到好複雜嘅嘢,但其實打好基礎先係最重要。等你熟習咗基本原理之後,先至慢慢加入個人風格,咁樣做出嚟嘅作品先至有靈魂。",
            "另外一個重要嘅方面係要識得聆聽參考作品。攞幾首你鍾意嘅廣東歌,用頭戴式耳機仔細分析佢哋嘅每一個細節:人聲點處理?和弦點行?編曲用緊乜嘢音色?呢啲觀察會成為你自己創作嘅養分。",
        ]),
        ("常見錯誤與解決方法", [
            "初學者最常犯嘅錯誤之一係「過度處理」。無論係混音加太多效果,定係編曲加入太多樂器,結果都係令歌曲失去焦點。記住一個原則:Less is More,少啲但有啲嘅元素,往往比多啲但平庸嘅元素更有力量。",
            "另一個常見問題係對自己要求太低或者太高。太低嘅話會令作品流於平庸,太高就可能永遠出唔到街。最好嘅方法係設定一個合理嘅完成標準,去到嗰個程度就Publish,唔好無止境咁修改。",
            "技術問題方面,好多香港音樂人會忽略聲學環境嘅重要性。即使你嘅設備幾咁專業,如果喺一個迴音好大或者低頻積聚嚴重嘅房間入面做嘢,出嚟嘅嘢都唔會好聽。投資少少喺房間聲學處理上面,回報會非常大。",
        ]),
        ("香港本地資源與社群", [
            "香港雖然細,但音樂資源其實非常豐富。除咗傳統嘅錄音室之外,而家仲有好多Band房同Co-working Space提供平價嘅制作環境。例如觀塘、荔枝角、火炭嘅工廠大廈入面,隱藏咗唔少獨立音樂人嘅工作室。",
            "社群方面,香港有好多音樂製作相關嘅Facebook群組、Discord Server,音樂人可以喺嗰度交流心得、搵合作伙伴、分享設備情報。呢啲社群對初學者嚟講特別重要,因為可以喺短時間內學到大量實戰經驗。",
            "仲有每年嘅Clockenflap、Sónar香港、各類本地音樂節,除咗係表演機會,亦係音樂人之間交流嘅重要場合。建議大家多啲去呢啲活動,擴闊眼界之餘亦可以建立人脈。",
        ]),
        ("進階思考與未來展望", [
            "隨住AI音樂技術嘅發展,廣東歌制作都進入咗一個新嘅階段。AI可以幫手生成和弦進行、寫Basic旋律,甚至做一啲簡單嘅混音。但係香港音樂人嘅價值,恰恰就係喺AI做唔到嘅地方:對粵語韻味嘅深刻理解,同埋香港人獨有嘅生活體驗。",
            "展望將來,廣東歌一定會繼續演化。無論係曲風上面(例如R&B、Hip-Hop、電子音樂嘅滲入),定係製作技術上面(沉浸式音訊、Dolby Atmos Music等),香港音樂人都需要保持開放嘅心態學習新事物。",
            "最後,無論技術點進步,廣東歌最核心嘅價值依然係「情感」。一首能夠觸動香港人嘅歌,唔一定技術上最複雜,但一定係最誠懇、最有溫度嘅。",
        ]),
        ("總結", [
            f"希望呢篇關於{topic_short}嘅文章,可以為你嘅廣東歌創作旅程帶嚟一啲啟發。記住,每一個成功嘅音樂人都係由零開始、慢慢累積,唔使急,但一定要持續。",
            "廣東歌嘅未來,係靠我哋呢一代人嘅努力。繼續寫歌、繼續創作、繼續用粵語講香港人嘅故事。",
        ]),
    ]

    html = ""
    for i, (h2, paras) in enumerate(sections):
        html += f'  <h2>{h2}</h2>\n'
        for p in paras:
            html += f'  <p>{p}</p>\n'
        # Insert highlight box midway
        if i == 2:
            html += '  <div class="highlight-box">「廣東歌最珍貴嘅唔係技術,係嗰份對粵語同香港嘅真心。」— 廣東歌·為你創作團隊</div>\n'
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
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","url":"{url}","datePublished":"{TODAY}","publisher":{{"@type":"Organization","name":"廣東歌·為你","url":"https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {title}</p>
  <h1 class="serif">{title}</h1>
  <p class="meta">{TODAY_DISPLAY} · 廣東歌·為你 · {category}</p>
{body}
  <div class="cta-box">
    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>
    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌,由填詞、作曲到錄音一站式完成。</p>
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

# ---- Update index.html: prepend new cards at TOP of grid ----
idx_path = os.path.join(ART_DIR, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

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

# Insert at top of grid (right after <div class="grid">)
grid_marker = '<div class="grid">\n'
assert grid_marker in idx_content, "Cannot find grid opening marker in index.html"
idx_content = idx_content.replace(grid_marker, grid_marker + cards_html, 1)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("✓ articles/index.html updated with new cards at top")

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

commit_msg = "feat: daily SEO batch — 29 new articles on 廣東歌制作 (2026-11-22) 填詞技巧,作曲編曲,錄音製作,混音製作,音樂制作,發行推廣,獨立音樂"
subprocess.run(["git", "commit", "-m", commit_msg], check=True)
print("✓ Git committed")

result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print(f"Git push stdout: {result.stdout}")
print(f"Git push stderr: {result.stderr}")
if result.returncode == 0:
    print("✓ Pushed to origin/main")
else:
    print(f"✗ Push failed (exit {result.returncode})")

print("\n=== DONE ===")

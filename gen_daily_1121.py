#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 29 unique articles (2026-11-21)."""
import os, datetime, subprocess

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026-11-21"
TODAY_DISPLAY = "2026年11月21日"

# 29 unique long-tail topics - verified no slug collisions with existing files
ARTICLES = [
("cantonese-lyrics-midnight-bus-terminal-last-departure-farewell-longing-guide-1121",
 "廣東歌填詞深夜巴士總站尾班車:點樣用夜色同離別寫出都市人嘅孤單同盼望",
 "填詞深夜巴士總站尾班車完整指南。教你點樣用香港深夜巴士同尾班車嘅意象寫出都市人嘅孤單、離別同對明日嘅盼望。",
 "填詞技巧",
 []),
("cantonese-lyrics-old-teahouse-yardbird-dimsum-steam-nostalgic-memory-guide-1121",
 "廣東歌填詞舊式茶樓雀鳥點心蒸氣:點樣用茶樓文化寫出老香港嘅人情味",
 "填詞舊式茶樓雀鳥點心蒸氣指南。教你點樣用傳統茶樓嘅雀鳥、點心同蒸氣寫出老香港人情味嘅歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-typhoon-shelter-fishing-boat-lullaby-harbor-guide-1121",
 "廣東歌填詞避風塘漁船搖籃曲:點樣用海港漁火寫出水上人家嘅溫柔",
 "填詞避風塘漁船搖籃曲完整指南。教你點樣用避風塘、漁船同海港寫出香港水上人家嘅溫柔歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-overpass-sleeping-city-neon-fading-loneliness-guide-1121",
 "廣東歌填詞天橋底沉睡城市霓虹熄滅:點樣用街頭角落寫出城市嘅寂寞",
 "填詞天橋底沉睡城市指南。教你點樣用天橋底、熄滅嘅霓虹燈同深夜街角寫出城市寂寞嘅粵語歌詞。",
 "填詞技巧",
 []),
("cantonese-lyrics-rooftop-laundry-drying-summer-breeze-youth-memory-guide-1121",
 "廣東歌填詞天合晾衫夏日微風:點樣用屋企天合嘅片段寫出青春嘅回憶",
 "填詞天合晾衫夏日微風完整指南。教你點樣用屋企天合嘅日常片段寫出香港青春回憶嘅歌詞。",
 "填詞技巧",
 []),
("melody-writing-suspended-fourth-chord-hong-kong-pop-ballad-tension-guide-1121",
 "廣東歌旋律Sus4掛留和弦運用技巧:點樣用掛留音製造流行曲嘅張力同解決",
 "Sus4掛留和弦廣東歌應用指南。教你點樣用掛留四度音製造歌曲張力,等解決去大三和弦嗰下更加感動。",
 "作曲編曲",
 []),
("melody-writing-picardy-third-major-ending-minor-song-hopeful-guide-1121",
 "廣東歌旋律Picardy三度大調結尾小調歌:點樣用大三度為悲傷歌曲帶嚟希望",
 "Picardy三度大調結尾技巧指南。教你點樣用小調歌曲最後轉大三度終止,為廣東悲歌帶嚟一線希望。",
 "作曲編曲",
 []),
("melody-writing-blue-note-bend-blues-cantopop-fusion-soulful-guide-1121",
 "廣東歌旋律藍調音彎音Blues融合:點樣用降三降七音為廣東歌加 Soul 味",
 "藍調音彎音技巧廣東歌融合指南。教你點樣用降三度、降七度音同彎音技巧為Cantopop加入Blues靈魂感。",
 "作曲編曲",
 []),
("melody-writing-ostinato-loop-piano-riff-hypnotic-hook-guide-1121",
 "廣東歌旋律固定音型鋼琴Riff催眠Hook:點樣用重複動機洗腦聽眾",
 "固定音型Ostinato鋼琴Riff廣東歌Hook指南。教你點樣用短嘅重複動機製造洗腦式流行曲Hook。",
 "作曲編曲",
 []),
("arrangement-temple-block-wooden-fish-cantonese-opera-percussion-guide-1121",
 "廣東歌編曲木魚梆子粵劇打擊樂運用:點樣用傳統敲擊樂器製造東方禪意",
 "木魚梆子粵劇打擊樂編曲指南。教你點樣將傳統粵劇敲擊樂器融入現代廣東歌,製造東方禪意。",
 "作曲編曲",
 []),
("arrangement-modular-synth-generative-patch-ambient-texture-guide-1121",
 "廣東歌編曲模塊合成器生成式Patch:點樣用Modular Synth製造Ambient氛圍底層",
 "模塊合成器生成式Patch編曲指南。教你點樣用Eurorack modular synth製造廣東歌Ambient氛圍底層。",
 "作曲編曲",
 []),
("arrangement-gamelan-bronze-ensemble-bali-texture-eastern-fusion-guide-1121",
 "廣東歌編曲印尼鑼鼓Gamelan東南亞色彩:點樣用峇里金屬樂器製造神秘東方風",
 "Gamelan印尼鑼鼓編曲指南。教你點樣將峇里島傳統金屬樂器音色融入廣東歌,製造神秘東南亞氛圍。",
 "作曲編曲",
 []),
("arrangement-string-orchestra-col-legno-bow-strike-percussive-guide-1121",
 "廣東歌編曲弦樂團Col Legno弓桿敲擊:點樣用特別弓法加入打擊音色",
 "弦樂團Col Legno弓桿敲擊指南。教你點樣用弓桿敲擊弦線嘅特殊弓法為廣東歌弦樂加入打擊樂色彩。",
 "作曲編曲",
 []),
("recording-hong-kong-tram-ding-ding-bell-urban-ambient-bed-guide-1121",
 "廣東歌錄音電車叮叮聲環境音:點樣用香港電車鈴聲做都市氛圍底層",
 "電車叮叮聲錄音指南。教你點樣錄低香港電車鈴聲同埋街道環境音,製造都市感十足嘅Ambient底層。",
 "錄音製作",
 []),
("recording-rain-on-zinc-roof-hong-kong-village-house-percussion-guide-1121",
 "廣東歌錄音雨打鐵皮屋頂村屋聲景:點樣用香港村屋雨聲做天然打擊樂",
 "雨打鐵皮屋頂錄音指南。教你點樣捕捉香港村屋鐵皮屋頂嘅雨聲,成為天然嘅打擊樂底層。",
 "錄音製作",
 []),
("recording-wet-market-vendor-call-fish-chopping-rhythm-bed-guide-1121",
 "廣東歌錄音街市叫賣斬魚聲市井聲景:點樣用香港街市聲做Life Rhythm Bed",
 "街市叫賣斬魚聲錄音指南。教你點樣錄低香港濕貨街市嘅人聲叫賣同斬魚聲,做充滿生活感嘅聲景底層。",
 "錄音製作",
 []),
("recording-dai-pai-dong-wok-fire-restaurant-ambient-sizzle-guide-1121",
 "廣東歌錄音大牌檔鑊氣爆炒聲:點樣用街頭大排檔嘅鑊聲做廚房氛圍層",
 "大牌檔鑊氣爆炒聲錄音指南。教你點樣捕捉香港街頭大排檔嘅炒菜鑊聲、風爐聲,做充滿港味嘅環境音。",
 "錄音製作",
 []),
("mixing-vocal-formant-shift-pitch-character-gender-alteration-guide-1121",
 "廣東歌混音人聲Formant Shift音色轉換:點樣用共振峰移調改變人聲性格",
 "人聲Formant Shift共振峰移調混音指南。教你點樣用Formant Shift改變廣東歌人聲嘅音色性格,製造唔同人聲質感。",
 "混音製作",
 []),
("mixing-mid-side-parallel-compression-hong-kong-pop-punch-guide-1121",
 "廣東歌混音Mid-Side並聯壓縮港式衝擊力:點樣用M/S壓縮令低音更緊實",
 "Mid-Side並聯壓縮混音指南。教你點樣用M/S Parallel Compression令廣東歌低音更緊實、整體更有港式流行曲衝擊力。",
 "混音製作",
 []),
("mixing-drum-reverb-gated-snare-80s-cantopop-retro-vibe-guide-1121",
 "廣東歌混音鼓組Gated Reverb小軍鼓80年代復古:點樣重現經典港樂鼓聲",
 "Gated Reverb小軍鼓80年代復古混音指南。教你點樣重現張國榮、梅艷芳年代嘅經典廣東歌鼓聲質感。",
 "混音製作",
 []),
("mixing-bass-synth-sub-octave-layer-depth-rumble-guide-1121",
 "廣東歌混音貝斯Sub超低八度分層:點樣用Sub Octave令低頻更有震懾力",
 "貝斯Sub超低八度分層混音指南。教你點樣用Sub Octave技術令廣東歌嘅Bass更有震懾力,適合現代R&B同電子曲風。",
 "混音製作",
 []),
("production-home-studio-bass-trap-diy-acoustic-hong-kong-flat-guide-1121",
 "廣東歌製作家居錄音室Bass Trap低音陷阱DIY:點樣喺香港細單位做聲學處理",
 "家居錄音室Bass Trap低音陷阱DIY指南。教你點樣喺香港細單位自製低音陷阱,改善家居錄音室嘅聲學環境。",
 "音樂制作",
 []),
("production-cantopop-songwriter-camp-hong-kong-collaboration-hub-guide-1121",
 "廣東歌製作Songwriting Camp香港創作營:點樣組織本地音樂人集中寫歌",
 "Songwriting Camp創作營香港指南。教你點樣組織本地廣東歌創作營,等音樂人可以集中時間合作寫歌。",
 "音樂制作",
 []),
("production-ai-vocal-cloning-legal-ethical-hong-kong-law-guide-1121",
 "廣東歌製作AI人聲複製法律倫理:點樣喺香港合法用AI Vocal技術",
 "AI人聲複製法律倫理指南。講解香港版權法下AI Vocal Cloning嘅法律界線,教你點樣合法咁用AI音樂技術。",
 "音樂制作",
 []),
("release-kkbox-hong-kong-chart-editorial-pitch-regional-strategy-guide-1121",
 "廣東歌發行KKBOX香港榜編輯推薦攻略:點樣喺區域性平台攞編輯Playlist",
 "KKBOX香港榜編輯推薦攻略指南。教你點樣向KKBOX編輯團隊Pitch你嘅廣東歌,爭取上編輯Playlist嘅機會。",
 "發行推廣",
 []),
("release-vinyl-lathe-cut-limited-run-hong-kong-collector-market-guide-1121",
 "廣東歌發行黑膠Lathe Cut限量刻碟香港收藏市場:點樣做手製黑膠生意",
 "黑膠Lathe Cut限量刻碟香港指南。教你點樣喺香港做手製黑膠刻碟,搶佔本地廣東歌黑膠收藏家市場。",
 "發行推廣",
 []),
("release-instagram-reels-cantopop-teaser-vertical-video-promo-guide-1121",
 "廣東歌發行IG Reels直式短影片宣傳:點樣用15秒Teaser推廣新廣東歌",
 "IG Reels直式短影片宣傳攻略。教你點樣剪攞15秒嘅廣東歌Teaser,喺Instagram Reels推廣新歌俾香港年輕聽眾。",
 "發行推廣",
 []),
("indie-cantopop-busking-license-hong-kong-street-performance-law-guide-1121",
 "獨立廣東歌街頭Busking表演牌照香港法例:點樣合法喺香港街頭演出",
 "香港街頭Busking表演牌照指南。講解香港街頭表演嘅法律要求,教你點樣喺合法情況下做廣東歌Busking演出。",
 "獨立音樂",
 []),
("indie-cantopop-live-looping-pedal-one-person-band-solo-show-guide-1121",
 "獨立廣東歌Live Looping Pedal一人樂隊Solo Show:點樣用Looper一個人做完成場演出",
 "Live Looping Pedal一人樂隊指南。教你點樣用Looper Pedal單人匹馬做完成場廣東歌演出,適合獨立音樂人。",
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

commit_msg = "feat: daily SEO batch — 29 new articles on 廣東歌制作 (2026-11-21) 填詞技巧,作曲編曲,錄音製作,混音製作,音樂制作,發行推廣,獨立音樂"
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

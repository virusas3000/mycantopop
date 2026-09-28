#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch generator for mycantopop.hk — 2026-09-28"""
import os, re, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ARTICLES_DIR = os.path.join(REPO, "articles")
TODAY = "2026-09-28"
TODAY_DISPLAY = "2026年09月28日"

EXISTING_FILES = set(os.listdir(ARTICLES_DIR))

def slug_free(slug):
    return (slug + ".html") not in EXISTING_FILES

ARTICLES = [
    ("cantopop-lyrics-writing-from-hong-kong-mtr-last-train-night-journey-guide",
     "廣東歌詞創作由香港港鐵尾班車深夜旅程取材指南：點樣用收工後嘅車廂寫出都市人嘅孤獨感同歸屬感",
     "填詞技巧",
     "港鐵尾班車深夜旅程歌詞創作指南。教你由收工後嘅車廂體驗出發,寫出廣東歌中都市人嘅孤獨感同歸屬感。"),
    ("cantopop-arrangement-euclidean-rhythm-generative-pattern-intro-guide",
     "廣東歌編曲歐幾里得節奏生成式 pattern 前奏指南:點樣用 euclidean rhythm 製造數學美感嘅鼓組律動",
     "作曲編曲",
     "歐幾里得節奏生成式 pattern 前奏編曲指南。教你用 euclidean rhythm 喺廣東歌前奏中製造數學美感嘅鼓組律動。"),
    ("cantopop-vocal-recording-headphone-bleed-microphone-isolation-guide",
     "廣東歌人聲錄音耳機洩漏咪高峰隔離指南:點樣避免錄音時耳機伴奏聲漏落人聲咪",
     "錄音製作",
     "耳機洩漏咪高峰隔離人聲錄音指南。教你喺廣東歌錄音時避免耳機伴奏聲漏落人聲咪嘅錄音技巧。"),
    ("cantopop-mixing-de-esser-sibilance-frequency-target-technique-guide",
     "廣東歌混音去齒音 de-esser 頻率瞄準技巧指南:點樣準確壓低粵語「思」「叉」等刺耳齒音",
     "錄音製作",
     "去齒音 de-esser 頻率瞄準混音指南。教你喺廣東歌混音中準確壓低粵語「思」「叉」等刺耳齒音嘅技巧。"),
    ("cantopop-song-distribution-tidal-hifi-plus-audiophile-market-guide",
     "廣東歌發行 TIDAL HiFi Plus 高保真音響發燒友市場指南:點樣針對 audiophile 聽眾發佈廣東歌",
     "發行推廣",
     "TIDAL HiFi Plus 高保真音響發燒友市場發行指南。教你針對 audiophile 聽眾發佈廣東歌嘅市場策略。"),
    ("cantopop-melody-writing-ninth-chord-tension-color-ballad-chorus-guide",
     "廣東歌旋律創作九和弦張力色彩情歌副歌指南:點樣用 9th chord 增添爵士味嘅抒情色彩",
     "作曲編曲",
     "九和弦張力色彩情歌副歌旋律創作指南。教你用 9th chord 喺廣東情歌副歌中增添爵士味嘅抒情色彩。"),
    ("cantopop-arrangement-ukulele-strumming-folk-acoustic-texture-guide",
     "廣東歌編曲烏克丽丽掃弦民謠木結他質感指南:點樣用 ukulele 營造夏日輕快嘅港式小品",
     "作曲編曲",
     "烏克丽丽掃弦民謠木結他質感編曲指南。教你用 ukulele 喺廣東歌中營造夏日輕快嘅港式小品質感。"),
    ("cantopop-lyrics-writing-synecdoche-part-whole-rhetorical-device-guide",
     "廣東歌詞創作提喻法以部分代整體修辭指南:點樣用 synecdoche 借局部細節暗示宏大主題",
     "填詞技巧",
     "提喻法以部分代整體修辭歌詞創作指南。教你用 synecdoche 喺廣東歌詞中借局部細節暗示宏大主題。"),
    ("cantopop-vocal-recording-gain-staging-preamp-input-level-guide",
     "廣東歌人聲錄音增益分級前級輸入電平指南:點樣設定 gain stage 錄出乾淨又有動態嘅人聲",
     "錄音製作",
     "增益分級前級輸入電平人聲錄音指南。教你喺廣東歌錄音中設定 gain stage 錄出乾淨又有動態嘅人聲。"),
    ("cantopop-song-distribution-tiktok-dance-challenge-choreography-hook-guide",
     "廣東歌發行 TikTok 舞蹈挑戰編舞副歌 hook 指南:點樣設計易學嘅副歌舞步帶動 viral 傳播",
     "發行推廣",
     "TikTok 舞蹈挑戰編舞副歌 hook 發行指南。教你設計易學嘅副歌舞步帶動廣東歌 viral 傳播嘅策略。"),
    ("cantopop-arrangement-harmonica-blues-bending-emotional-solo-guide",
     "廣東歌編曲口琴藍調彎音情感獨奏指南:點樣用 blues harp 為廣東苦情歌加滄桑感",
     "作曲編曲",
     "口琴藍調彎音情感獨奏編曲指南。教你用 blues harp 喺廣東苦情歌中加滄桑感嘅編曲技巧。"),
    ("cantopop-mixing-reverse-reverb-ethereal-vocal-intro-effect-guide",
     "廣東歌混音反向殘響空靈人聲前奏效果指南:點樣用 reverse reverb 製造夢幻般嘅聲音漸入",
     "錄音製作",
     "反向殘響空靈人聲前奏效果混音指南。教你用 reverse reverb 喺廣東歌前奏中製造夢幻般嘅聲音漸入。"),
    ("cantopop-lyrics-writing-from-cha-chaan-teng-milk-tea-daily-ritual-guide",
     "廣東歌詞創作由茶餐廳絲襪奶茶日常儀式出發指南:點樣用一杯熱奶茶寫出香港人嘅生活節奏",
     "填詞技巧",
     "茶餐廳絲襪奶茶日常儀式歌詞創作指南。教你由一杯熱奶茶嘅日常體驗出發寫出廣東歌中香港人嘅生活節奏。"),
    ("cantopop-vocal-recording-monitoring-mix-headphone-balance-guide",
     "廣東歌人聲錄音監聽混音耳機平衡指南:點樣喺錄音時調整 monitor mix 令歌手唱得更準",
     "錄音製作",
     "監聽混音耳機平衡人聲錄音指南。教你喺廣東歌錄音時調整 monitor mix 令歌手唱得更準嘅技巧。"),
    ("cantopop-song-distribution-twitch-music-stream-live-performance-guide",
     "廣東歌發行 Twitch 音樂直播現場演出指南:點樣用 Twitch 直播為廣東歌建立忠實粉絲社群",
     "發行推廣",
     "Twitch 音樂直播現場演出發行指南。教你用 Twitch 直播為廣東歌建立忠實粉絲社群嘅直播策略。"),
    ("cantopop-melody-writing-pentatonic-scale-cantonese-tone-matching-guide",
     "廣東歌旋律創作五聲音階粵語聲調匹配指南:點樣用pentatonic寫出既中國風又啱粵語聲調嘅旋律",
     "作曲編曲",
     "五聲音階粵語聲調匹配旋律創作指南。教你用pentatonic寫出既中國風又啱粵語聲調嘅旋律。"),
    ("cantopop-arrangement-kalimba-mbira-thumb-piano-dreamy-texture-guide",
     "廣東歌編曲卡林巴拇指琴夢幻質感指南:點樣用 kalimba 為廣東電視劇式情歌增添童話感",
     "作曲編曲",
     "卡林巴拇指琴夢幻質感編曲指南。教你用 kalimba 喺廣東情歌中增添童話般質感嘅編曲技巧。"),
    ("cantopop-mixing-exciter-harmonic-saturation-air-high-frequency-guide",
     "廣東歌混音激勵器和諧飽和高頻空氣感指南:點樣用 exciter 為人聲加「光澤」但唔會刺耳",
     "錄音製作",
     "激勵器和諧飽和高頻空氣感混音指南。教你用 exciter 喺廣東歌人聲中加「光澤」但唔會刺耳嘅混音技巧。"),
    ("cantopop-song-distribution-patreon-membership-subscription-fan-club-guide",
     "廣東歌發行 Patreon 會員訂閱粉絲俱樂部指南:點樣用月費模式為廣東歌創作者建立穩定收入",
     "獨立音樂",
     "Patreon 會員訂閱粉絲俱樂部發行指南。教你用月費模式為廣東歌創作者建立穩定收入嘅經營策略。"),
    ("cantopop-vocal-recording-vocal-gasp-breath-control-emotional-pause-guide",
     "廣東歌人聲錄音喘息控制情感停頓指南:點樣利用呼吸聲同氣口為廣東歌人聲加戲劇感",
     "錄音製作",
     "喘息控制情感停頓人聲錄音指南。教你利用呼吸聲同氣口喺廣東歌人聲中加戲劇感嘅錄音技巧。"),
    ("cantopop-lyrics-writing-chinese-valentine-qixi-festival-love-theme-guide",
     "廣東歌詞創作七夕情人節中國情人節愛情主題指南:點樣用牛郎織女傳說寫出現代廣東情歌",
     "填詞技巧",
     "七夕情人節中國情人節愛情主題歌詞創作指南。教你用牛郎織女傳說寫出現代廣東情歌。"),
    ("cantopop-arrangement-melodica-wind-keyboard-reggae-ska-texture-guide",
     "廣東歌編曲口風琴 wind keyboard 雷鬼 ska 質感指南:點樣用 melodica 為廣東夏日歌添異國風情",
     "作曲編曲",
     "口風琴 wind keyboard 雷鬼 ska 質感編曲指南。教你用 melodica 喺廣東夏日歌中添異國風情嘅編曲技巧。"),
    ("cantopop-mixing-linear-phase-eq-master-bus-transparency-guide",
     "廣東歌混音線性相位 EQ 母帶匯流排透明度指南:點樣用 linear phase EQ 喺 master bus 保留動態細節",
     "錄音製作",
     "線性相位 EQ 母帶匯流排透明度混音指南。教你用 linear phase EQ 喺 master bus 保留動態細節嘅混音技巧。"),
    ("cantopop-song-distribution-deezer-flow-algorithm-personalization-guide",
     "廣東歌發行 Deezer Flow 演算法個人化推薦指南:點樣優化 metadata 俾 Deezer 嘅 AI 更理解你嘅廣東歌",
     "發行推廣",
     "Deezer Flow 演算法個人化推薦發行指南。教你優化 metadata 俾 Deezer 嘅 AI 更理解你嘅廣東歌嘅發行策略。"),
    ("cantopop-lyrics-writing-from-velodrome-cycling-causeway-bay-memory-guide",
     "廣東歌詞創作由銅鑼灣維園單車徑週末踏單車記憶出發指南:點樣用兩個轆寫出父子情",
     "填詞技巧",
     "銅鑼灣維園單車徑週末踏單車記憶歌詞創作指南。教你由兩個轆嘅體驗出發寫出廣東歌中嘅父子情。"),
    ("cantopop-vocal-recording-dynamic-mic-sm7b-broadcast-podcast-voice-guide",
     "廣東歌人聲錄音動圈咪 Shure SM7B 廣播播客人聲指南:點樣用經典廣播咪錄出溫暖近講嘅人聲",
     "錄音製作",
     "動圈咪 SM7B 廣播播客人聲錄音指南。教你用經典廣播咪喺廣東歌錄音中錄出溫暖近講嘅人聲。"),
    ("cantopop-arrangement-808-sub-bass-boom-trap-modern-production-guide",
     "廣東歌編曲 808 超低音 boom trap 現代製作指南:點樣用 Roland TR-808 為廣東說唱加街頭重量感",
     "作曲編曲",
     "808 超低音 boom trap 現代製作編曲指南。教你用 Roland TR-808 喺廣東說唱中加街頭重量感嘅編曲技巧。"),
    ("cantopop-song-distribution-twitch-sings-cover-community-engagement-guide",
     "廣東歌發行 Twitch 主播翻唱社群互動指南:點樣邀請 Twitch 主播翻唱你嘅廣東歌擴大聽眾層",
     "發行推廣",
     "Twitch 主播翻唱社群互動發行指南。教你邀請 Twitch 主播翻唱你嘅廣東歌擴大聽眾層嘅社群策略。"),
    ("cantopop-mixing-stereo-imager-mono-compatibility-club-playback-guide",
     "廣東歌混音立體聲成像單聲道兼容夜店重播指南:點樣確保你嘅混音喺 club 嘅 mono PA 都打到",
     "錄音製作",
     "立體聲成像單聲道兼容夜店重播混音指南。教你確保你嘅廣東歌混音喺 club 嘅 mono PA 都打到嘅混音技巧。"),
]

assert len(ARTICLES) == 29, f"Expected 29, got {len(ARTICLES)}"

# verify no duplicates
for slug, *_ in ARTICLES:
    fname = slug + ".html"
    assert slug_free(slug), f"DUPLICATE SLUG: {fname} already exists!"
print(f"All {len(ARTICLES)} slugs are unique.\n")

def generate_body(slug, title, desc):
    topic_prefix = title.split('：')[0]
    focus = title.split('：')[-1] if '：' in title else title
    return [
        f"{topic_prefix}係廣東歌制作入面一個技術性但極具創意嘅範疇。好多香港獨立音樂人可能會覺得呢個範疇好抽象或者難入手，但只要掌握咗基本原理同埋操作方法，你就會發現佢可以大大改變你作品嘅專業感同埋藝術表達力。本文會由基本概念講起，再逐步講解實際操作嘅細節，最後會分享一啲喺香港音樂圈實際應用嘅心得同埋常見誤區。無論你係剛起步嘅創作新手，定係已經發行過幾首作品嘅獨立音樂人，都可以喺度搵到對你有用嘅資訊。",
        f"點解要特別關注「{focus}」呢個環節？因為廣東歌同英文流行曲有本質上嘅分別——粵語嘅九聲六調令每一個音樂決定都同詞意有緊密關係。一個聲調處理得唔好，可能整句歌詞嘅意思都被扭曲，或者聽起嚟好突兀。而呢個環節正正係連接音樂技術同語言藝術嘅橋樑，掌握得好嘅話，可以令作品由「業餘」升級到「專業」，由「普通」升級到「動人」。好多經典嘅廣東歌之所以歷久彌新，正正因為佢哋喺呢啲細節上做得極之出色。",
        f"實際操作嘅第一步係充分了解你手上嘅資源同工具。唔係每個音樂人都有條件走入頂級錄音室，但其實現代嘅 DAW 同平價插件都可以做到好多專業級嘅效果，關鍵在於點樣善用。建議你首先整理返自己現有嘅工具清單——你用開邊款 DAW？有咩內置效果器？有邊啲第三方插件？了解返呢啲基本工具嘅特性之後，就可以針對性咁去學習點樣發揮佢哋嘅最大潛力。例如 Reaper、Logic Pro、Ableton Live 同 FL Studio 都有各自嘅優勢同埋工作流程，識得因應自己風格去揀合適嘅工具，會令你嘅工作效率提升好多。",
        f"第二個重要環節係持續嘅聆聽訓練。好多音樂人只顧住創作，冇花時間去分析其他作品，呢個係好大嘅盲點。建議你每星期抽出固定時間做「深度聆聽」——揀返一兩首你欣賞嘅廣東歌，用耳機專心聽，嘗試分析佢哋喺呢個環節上點樣處理。例如可以留意：佢哋喺副歌同主歌之間點樣做過渡？人聲同埋樂器嘅頻率分配係點？點樣營造情感起伏？將你觀察到嘅嘢寫低，逐步建立自己嘅「參考庫」，之後喺自己作品遇到樽頸位嗰陣，就可以去呢個參考庫搵靈感同埋解決方法。",
        f"喺香港做廣東歌，特別要留意本地聽眾嘅口味同埋收聽習慣。香港聽眾對於聲調同詞意嘅敏感度好高，呢個係粵語區嘅獨特優勢——但同時都係挑戰。一個常見嘅做法係喺混音過程中不斷對比參考曲目（reference track），確保你嘅作品喺響度、動態、空間感各方面都符合主流串流平台嘅標準。例如喺 Spotify、Apple Music 同埋 KKBOX 上，廣東歌嘅普遍響度目標大約喺 -10 到 -14 LUFS 之間，超過呢個範圍可能會被平台嘅 loudness normalization 拉低音量，影響聽感。",
        f"最後但同樣重要嘅係實踐同埋反覆修正。所有嘅理論知識，如果冇實際動手去試，都只係紙上談兵。建議你為自己訂立一個持續創作嘅目標，例如每個月完成一首完整作品，由填詞、作曲、編曲、錄音到混音一條龍走完。每次完成之後，都做一次「事後檢討」——記低邊啲環節做得好、邊啲做得唔好、下次點樣改進。呢個持續嘅迭代過程，先至係令一個音樂人真正成長嘅關鍵。喺香港呢個寸金尺土嘅地方，時間同埋資源都係寶貴嘅，但只要用心做，一個人嘅臥室工作室都可以做出令人驚艷嘅廣東歌。",
    ]

def generate_article_html(slug, title, desc, body_paras):
    h2_titles = ["核心概念與背景", "點解廣東歌特別需要留意", "工具與資源準備", "持續聆聽訓練與參考庫建立", "本地市場與平台標準", "實踐路線圖與持續成長"]
    h2_sections = []
    for i, para in enumerate(body_paras):
        h2 = h2_titles[i] if i < len(h2_titles) else f"深入探討（第{i+1}部分）"
        h2_sections.append(f"  <h2>{h2}</h2>\n  <p>{para}</p>")
    body_html = "\n\n".join(h2_sections)

    all_text = " ".join(body_paras)
    cjk_count = len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', all_text))

    template = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)} | 廣東歌·為你</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{html.escape(title)} | 廣東歌·為你">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="https://mycantopop.hk/articles/{slug}.html">
  <meta property="og:site_name" content="廣東歌·為你">
  <meta property="og:locale" content="zh_HK">
  <link rel="canonical" href="https://mycantopop.hk/articles/{slug}.html">
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
  {{"@context":"https://schema.org","@type":"Article","headline":"{html.escape(title)}","description":"{html.escape(desc)}","url":"https://mycantopop.hk/articles/{slug}.html","datePublished":"{TODAY}","publisher":{{"@type":"Organization","name":"廣東歌·為你","url":"https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {html.escape(title)}</p>
  <h1 class="serif">{html.escape(title)}</h1>
  <p class="meta">{TODAY_DISPLAY} · 廣東歌·為你</p>

{body_html}

  <div class="highlight-box">「廣東歌制作嘅每一個細節都值得用心打磨。唔好急於求成，慢慢累積經驗，你嘅作品會越嚟越好。」— 廣東歌·為你創作團隊</div>

  <h2>常見問題</h2>
  <p><strong>呢個技巧需要咩設備？</strong> 基本上只需要你現有嘅 DAW 同埋監聽設備就可以開始練習。進階用法可能需要特定嘅插件或者硬件，但入門階段完全唔使額外投資。</p>
  <p><strong>新手要幾耐先可以掌握？</strong> 視乎你嘅基礎同練習時間。一般嚟講，持續練習兩到三個月就可以有感覺，半年左右可以做到比較自然嘅效果。最重要係多聽多比較多嘗試。</p>
  <p><strong>呢個技巧適用於所有類型嘅廣東歌嗎？</strong> 大部分類型都適用，但具體參數同用法要根據歌曲風格去調整。抒情慢歌同節奏快歌嘅處理方式會有唔同，建議你針對自己嘅風格去做實驗。</p>

  <div class="cta-box">
    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>
    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌，由填詞、作曲到錄音一站式完成。</p>
    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>
  </div>
</main>
<footer>© 2025 廣東歌·為你 · <a href="/">首頁</a> · <a href="/articles">文章</a></footer>
</body>
</html>'''
    return template, cjk_count

# ---- Generate article files ----
word_counts = []
for slug, title, cat, desc in ARTICLES:
    body = generate_body(slug, title, desc)
    html_content, wc = generate_article_html(slug, title, desc, body)
    fpath = os.path.join(ARTICLES_DIR, slug + ".html")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html_content)
    word_counts.append((slug, wc))
    print(f"  ✓ {slug}.html ({wc} CJK chars)")

print(f"\nGenerated {len(ARTICLES)} articles")
issues = 0
for slug, wc in word_counts:
    ok = 600 <= wc <= 2000
    if not ok:
        issues += 1
        print(f"  WARNING: {slug} = {wc} chars")
print(f"CJK counts OK ({issues} warnings)")

# ---- Update articles/index.html ----
index_path = os.path.join(ARTICLES_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

cards_html = ""
for slug, title, cat, desc in ARTICLES:
    cards_html += f'''      <a class="card" href="/articles/{slug}.html">
        <span class="card-date">{TODAY_DISPLAY}</span>
        <span class="card-tag">{cat}</span>
        <h2>{html.escape(title)}</h2>
        <p>{html.escape(desc)}</p>
        <span class="card-arrow">→</span>
      </a>
'''

pos = index_content.rfind("</a>\n    </div>")
assert pos != -1, "Could not find injection point"
new_index = index_content[:pos+len("</a>\n")] + cards_html + index_content[pos+len("</a>\n"):]
assert new_index != index_content, "Failed to inject cards into index.html"

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_index)
print(f"Updated articles/index.html with {len(ARTICLES)} new cards")

# ---- Update sitemap.xml ----
sitemap_path = os.path.join(REPO, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = ""
for slug, *_ in ARTICLES:
    new_urls += f'''  <url>
    <loc>https://mycantopop.hk/articles/{slug}.html</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''

new_sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
assert new_sitemap != sitemap, "Failed to update sitemap"
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(new_sitemap)
print(f"Updated sitemap.xml with {len(ARTICLES)} new URLs")

print("\n✅ All done! Ready for git commit.")

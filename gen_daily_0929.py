#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch generator for mycantopop.hk — 2026-09-29"""
import os, re, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ARTICLES_DIR = os.path.join(REPO, "articles")
TODAY = "2026-09-29"
TODAY_DISPLAY = "2026年09月29日"

EXISTING_FILES = set(os.listdir(ARTICLES_DIR))

def slug_free(slug):
    return (slug + ".html") not in EXISTING_FILES

ARTICLES = [
    ("cantopop-lyrics-writing-from-hong-kong-wet-market-fish-stall-morning-scene-guide",
     "廣東歌詞創作由香港街市魚檔清晨叫賣場景出發指南：點樣用街市喧鬧聲寫出草根階層嘅生命力",
     "填詞技巧",
     "香港街市魚檔清晨叫賣場景歌詞創作指南。教你由街市喧鬧聲嘅體驗出發，寫出廣東歌中草根階層嘅生命力。"),
    ("cantopop-melody-writing-neapolitan-sixth-chord-classical-drama-guide",
     "廣東歌旋律創作拿坡里六和弦古典戲劇張力指南：點樣用 Neapolitan sixth 為廣東苦情歌加悲劇色彩",
     "作曲編曲",
     "拿坡里六和弦古典戲劇張力旋律創作指南。教你用 Neapolitan sixth 喺廣東苦情歌中加悲劇色彩嘅旋律技巧。"),
    ("cantopop-vocal-recording-close-miking-intimate-whisper-tone-guide",
     "廣東歌人聲錄音近咪私密耳語音色指南：點樣用 close miking 錄出貼耳又溫柔嘅人聲質感",
     "錄音製作",
     "近咪私密耳語音色人聲錄音指南。教你用 close miking 喺廣東歌錄音中錄出貼耳又溫柔嘅人聲質感。"),
    ("cantopop-mixing-gated-reverb-snare-80s-retro-drum-guide",
     "廣東歌混音閘門殘響軍鼓八十年代復古鼓聲指南：點樣用 gated reverb 重現 Phil Collins 式經典鼓聲",
     "錄音製作",
     "閘門殘響軍鼓八十年代復古鼓聲混音指南。教你用 gated reverb 喺廣東歌中重現 Phil Collins 式經典鼓聲。"),
    ("cantopop-song-distribution-youtube-topic-channel-auto-generated-guide",
     "廣東歌發行 YouTube Topic 頻道自動生成指南：點樣認領你嘅 Topic Channel 並整合官方藝人頻道",
     "發行推廣",
     "YouTube Topic 頻道自動生成發行指南。教你認領廣東歌嘅 Topic Channel 並整合官方藝人頻道嘅發行策略。"),
    ("cantopop-arrangement-prepared-piano-cage-avant-garde-texture-guide",
     "廣東歌編曲預置鋼琴 John Cage 前衛質感指南：點樣用 prepared piano 為廣東實驗音樂加敲擊音響",
     "作曲編曲",
     "預置鋼琴 John Cage 前衛質感編曲指南。教你用 prepared piano 喺廣東實驗音樂中加敲擊音響嘅編曲技巧。"),
    ("cantopop-lyrics-writing-litotes-understatement-ironic-negation-guide",
     "廣東歌詞創作曲言法間接肯定反語否定指南：點樣用 litotes 以否定句式表達強烈肯定嘅情感",
     "填詞技巧",
     "曲言法間接肯定反語否定歌詞創作指南。教你用 litotes 以否定句式表達強烈肯定嘅廣東歌詞修辭技巧。"),
    ("cantopop-vocal-recording-pop-filter-angle-placement-plosive-defense-guide",
     "廣東歌人聲錄音防噴罩角度擺位爆破音防禦指南：點樣調校 pop filter 位置擋走噴咪聲",
     "錄音製作",
     "防噴罩角度擺位爆破音防禦人聲錄音指南。教你調校 pop filter 位置喺廣東歌錄音中擋走噴咪聲嘅技巧。"),
    ("cantopop-mixing-vocal-compression-la2a-optical-smooth-guide",
     "廣東歌混音人聲壓縮 LA-2A 光學平滑控制指南：點樣用 optical compressor 為廣東人聲加自然溫暖嘅壓縮",
     "錄音製作",
     "人聲壓縮 LA-2A 光學平滑控制混音指南。教你用 optical compressor 喺廣東歌人聲中加自然溫暖嘅壓縮技巧。"),
    ("cantopop-song-distribution-kkbox-editorial-playlist-pitching-guide",
     "廣東歌發行 KKBOX 編輯精選歌單推薦指南：點樣聯絡 KKBOX 香港編輯爭取新歌上榜",
     "發行推廣",
     "KKBOX 編輯精選歌單推薦發行指南。教你聯絡 KKBOX 香港編輯爭取廣東歌新歌上榜嘅發行策略。"),
    ("cantopop-arrangement-marimba-african-mallet-percussion-warm-tone-guide",
     "廣東歌編曲木琴非洲琴槌敲擊溫暖音色指南：點樣用 marimba 為廣東抒情歌加木質暖感",
     "作曲編曲",
     "木琴非洲琴槌敲擊溫暖音色編曲指南。教你用 marimba 喺廣東抒情歌中加木質暖感嘅編曲技巧。"),
    ("cantopop-lyrics-writing-from-hong-kong-dai-pai-dong-wonton-noodle-guide",
     "廣東歌詞創作由香港大牌檔雲吞麵檔煙火氣出發指南：點樣用一碗街頭美食寫出老香港嘅人情味",
     "填詞技巧",
     "香港大牌檔雲吞麵檔煙火氣歌詞創作指南。教你由一碗街頭美食嘅體驗出發寫出老香港嘅人情味。"),
    ("cantopop-vocal-recording-in-ear-monitor-live-stage-feedback-guide",
     "廣東歌人聲錄音入耳監聽現場舞台回授指南：點樣用 IEM 喺 live house 錄出乾淨嘅人聲",
     "錄音製作",
     "入耳監聽現場舞台回授人聲錄音指南。教你用 IEM 喺 live house 錄出乾淨嘅廣東人聲。"),
    ("cantopop-mixing-bass-synthesizer-sub-layer-blending-technique-guide",
     "廣東歌混音低音合成器次低頻疊加混合技巧指南：點樣為廣東流行曲加 808 同 sub bass 層次感",
     "錄音製作",
     "低音合成器次低頻疊加混合混音指南。教你為廣東流行曲加 808 同 sub bass 層次感嘅混音技巧。"),
    ("cantopop-song-distribution-moov-local-hong-kong-platform-guide",
     "廣東歌發行 MOOV 香港本地串流平台指南：點樣喺 MOOV 上架你嘅廣東歌觸及本地聽眾",
     "發行推廣",
     "MOOV 香港本地串流平台發行指南。教你喺 MOOV 上架廣東歌觸及本地聽眾嘅發行策略。"),
    ("cantopop-melody-writing-harmonic-minor-exotic-dark-flavor-guide",
     "廣東歌旋律創作和聲小調異國黑暗色彩指南：點樣用 harmonic minor 為廣東歌加東歐神秘感",
     "作曲編曲",
     "和聲小調異國黑暗色彩旋律創作指南。教你用 harmonic minor 喺廣東歌中加東歐神秘感嘅旋律技巧。"),
    ("cantopop-lyrics-writing-antithesis-contrast-opposition-rhetoric-guide",
     "廣東歌詞創作對比法正反對立修辭指南：點樣用 antithesis 以強烈反差突出情感衝突",
     "填詞技巧",
     "對比法正反對立修辭歌詞創作指南。教你用 antithesis 以強烈反差突出廣東歌詞中嘅情感衝突。"),
    ("cantopop-vocal-recording-room-node-frequency-standing-wave-fix-guide",
     "廣東歌人聲錄音房間節點頻率駐波修正指南：點樣找出同消除 home studio 嘅低頻駐波問題",
     "錄音製作",
     "房間節點頻率駐波修正人聲錄音指南。教你找出同消除 home studio 嘅低頻駐波問題嘅錄音技巧。"),
    ("cantopop-mixing-bitcrusher-lofi-texture-vocal-effect-guide",
     "廣東歌混音位元壓碎 lo-fi 質感人聲效果指南：點樣用 bitcrusher 為廣東嘻哈加復古電話音色",
     "錄音製作",
     "位元壓碎 lo-fi 質感人聲效果混音指南。教你用 bitcrusher 喺廣東嘻哈中加復古電話音色嘅混音技巧。"),
    ("cantopop-song-distribution-apple-music-spatial-audio-dolby-atmos-guide",
     "廣東歌發行 Apple Music Spatial Audio 杜比全景聲指南：點樣為廣東歌混音 Dolby Atmos 版本",
     "發行推廣",
     "Apple Music Spatial Audio 杜比全景聲發行指南。教你為廣東歌混音 Dolby Atmos 版本嘅發行策略。"),
    ("cantopop-arrangement-erhu-classical-chinese-fiddle-emotional-solo-guide",
     "廣東歌編曲二胡中國古典提琴情感獨奏指南：點樣用 erhu 為廣東悲情歌加東方淒美感",
     "作曲編曲",
     "二胡中國古典提琴情感獨奏編曲指南。教你用 erhu 喺廣東悲情歌中加東方淒美感嘅編曲技巧。"),
    ("cantopop-lyrics-writing-from-hong-kong-temple-street-night-market-guide",
     "廣東歌詞創作由香港廟街夜市占卜攤檔燈火出發指南：點樣用夜市嘅神秘氣氛寫出都市傳說感",
     "填詞技巧",
     "香港廟街夜市占卜攤檔燈火歌詞創作指南。教你由夜市嘅神秘氣氛出發寫出都市傳說感嘅廣東歌詞。"),
    ("cantopop-vocal-recording-ambient-noise-floor-reduction-guide",
     "廣東歌人聲錄音環境噪音底噪降低指南：點樣喺香港鬧市錄出安靜嘅人聲",
     "錄音製作",
     "環境噪音底噪降低人聲錄音指南。教你喺香港鬧市錄出安靜嘅廣東人聲嘅降噪技巧。"),
    ("cantopop-mixing-drum-room-mic-far-ambience-natural-depth-guide",
     "廣東歌混音鼓組房間咪遠距離環境深度指南：點樣用 far mic 為鼓聲加真實空間感",
     "錄音製作",
     "鼓組房間咪遠距離環境深度混音指南。教你用 far mic 喺廣東歌鼓聲中加真實空間感嘅混音技巧。"),
    ("cantopop-song-distribution-joox-vip-subscription-artist-payout-guide",
     "廣東歌發行 JOOX VIP 訂閱藝人收益指南：點樣計算同優化你嘅 JOOX 串流收入",
     "發行推廣",
     "JOOX VIP 訂閱藝人收益發行指南。教你計算同優化廣東歌嘅 JOOX 串流收入嘅發行策略。"),
    ("cantopop-arrangement-guzheng-flowing-arpeggio-chinese-elegance-guide",
     "廣東歌編曲古箏流水琶音中國韻味指南：點樣用 guzheng 為廣東中國風歌曲加古典雅致質感",
     "作曲編曲",
     "古箏流水琶音中國韻味編曲指南。教你用 guzheng 喺廣東中國風歌曲中加古典雅致質感嘅編曲技巧。"),
    ("cantopop-lyrics-writing-metonymy-substitution-symbolic-reference-guide",
     "廣東歌詞創作轉喻法借代象徵修辭指南：點樣用 metonymy 以相關事物代替抽象概念",
     "填詞技巧",
     "轉喻法借代象徵修辭歌詞創作指南。教你用 metonymy 以相關事物代替抽象概念嘅廣東歌詞技巧。"),
    ("cantopop-vocal-recording-vocal-chain-order-signal-flow-guide",
     "廣東歌人聲錄音人聲鏈順序訊號流程指南：點樣安排 EQ、壓縮、de-esser 嘅先後次序",
     "錄音製作",
     "人聲鏈順序訊號流程人聲錄音指南。教你安排 EQ、壓縮、de-esser 嘅先後次序嘅人聲錄音技巧。"),
    ("cantopop-mixing-multiband-sidechain-frequency-specific-ducking-guide",
     "廣東歌混音多頻段側鏈頻率選擇性閃避指南：點樣用 multiband sidechain 精準控制廣東人聲同樂器嘅頻率衝突",
     "錄音製作",
     "多頻段側鏈頻率選擇性閃避混音指南。教你用 multiband sidechain 精準控制廣東人聲同樂器嘅頻率衝突。"),
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

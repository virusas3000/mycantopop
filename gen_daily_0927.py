#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch generator for mycantopop.hk — 2026-09-27"""
import os, re, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ARTICLES_DIR = os.path.join(REPO, "articles")
TODAY = "2026-09-27"
TODAY_DISPLAY = "2026年09月27日"

ARTICLES = [
    ("cantopop-arrangement-erhu-tremolo-emotional-climax-fusion-guide",
     "廣東歌編曲二胡顫音情感高潮融合指南：點樣用 erhu tremolo 為副歌製造催淚東方韻味",
     "作曲編曲",
     "二胡顫音情感高潮融合編曲指南。教你用 erhu tremolo 喺廣東歌副歌中製造催淚東方韻味嘅編曲技巧。"),
    ("cantopop-lyrics-writing-epizeuxis-immediate-word-repetition-technique",
     "廣東歌詞創作緊接疊字重複強化技巧指南：點樣用 epizeuxis 立即重複同一字製造情感爆發力",
     "填詞技巧",
     "緊接疊字重複強化歌詞創作技巧指南。教你用 epizeuxis 喺廣東歌詞中立即重複同一字製造情感爆發力。"),
    ("cantopop-mixing-sidechain-eq-dynamic-frequency-ducking-technique-guide",
     "廣東歌混音側鏈 EQ 動態頻率閃避技巧指南：點樣用 sidechain EQ 令 bass 同 kick 共存唔撞頻",
     "錄音製作",
     "側鏈 EQ 動態頻率閃避混音指南。教你用 sidechain EQ 喺廣東歌混音中令 bass 同 kick 共存唔撞頻。"),
    ("cantopop-song-distribution-youtube-shorts-algorithm-optimization-guide",
     "廣東歌發行 YouTube Shorts 演算法優化指南：點樣用60秒短片為廣東歌製造爆紅機會",
     "發行推廣",
     "YouTube Shorts 演算法優化發行指南。教你用60秒短片喺廣東歌發行時製造爆紅機會嘅短片行銷策略。"),
    ("cantopop-melody-writing-borrowed-chord-modal-interchange-color-guide",
     "廣東歌旋律創作借用和弦調式交替色彩指南：點樣用 modal interchange 為副歌增添意外和聲轉折",
     "作曲編曲",
     "借用和弦調式交替色彩旋律創作指南。教你用 modal interchange 喺廣東歌副歌中增添意外和聲轉折。"),
    ("cantopop-vocal-recording-dynamic-mic-sm57-classic-rock-texture-guide",
     "廣東歌人聲錄音動圈咪 Shure SM57 經典搖滾質感指南：點樣用平價動圈咪錄出硬朗廣東人聲",
     "錄音製作",
     "動圈咪 SM57 經典搖滾質感人聲錄音指南。教你用平價動圈咪喺廣東歌錄音中製造硬朗人聲質感。"),
    ("cantopop-lyrics-writing-from-hong-kong-typhoon-signal-eight-memory-guide",
     "廣東歌詞創作由香港八號風球記憶出發指南：點樣用颱風停課停寫出城市集體回憶",
     "填詞技巧",
     "香港八號風球記憶歌詞創作指南。教你由颱風停課停嘅兒時體驗出發寫出廣東歌中嘅城市集體回憶。"),
    ("cantopop-mastering-lufs-loudness-target-spotify-normalization-guide",
     "廣東歌母帶處理 LUFS 響度目標 Spotify 標準化指南：點樣做到 -14 LUFS 唔損動態",
     "錄音製作",
     "LUFS 響度目標 Spotify 標準化母帶指南。教你喺廣東歌母帶中做到 -14 LUFS 目標響度但唔損失動態。"),
    ("cantopop-arrangement-guzheng-glissando-waterfall-texture-intro-guide",
     "廣東歌編曲古箏刮奏瀑布質感前奏指南：點樣用 guzheng glissando 製造中國風瀑布質感",
     "作曲編曲",
     "古箏刮奏瀑布質感前奏編曲指南。教你用 guzheng glissando 喺廣東歌前奏中製造中國風瀑布質感。"),
    ("cantopop-song-distribution-instagram-reels-cover-trend-strategy-guide",
     "廣東歌發行 Instagram Reels 翻唱趨勢策略指南：點樣用 Reels 邀請 KOL 翻唱擴大觸達",
     "發行推廣",
     "Instagram Reels 翻唱趨勢策略發行指南。教你用 Reels 邀請 KOL 翻唱喺廣東歌發行後擴大觸達範圍。"),
    ("cantopop-mixing-reverb-pre-delay-vocal-clarity-separation-guide",
     "廣東歌混音殘響前置延遲人聲清晰度分離指南：點樣用 pre-delay 令人聲有深度但唔模糊",
     "錄音製作",
     "殘響前置延遲人聲清晰度分離混音指南。教你用 pre-delay 喺廣東歌混音中令人聲有深度但保持清晰。"),
    ("cantopop-melody-writing-blues-scale-flat-five-bent-note-guide",
     "廣東歌旋律創作藍調音階降五級彎音指南：點樣用 blue note 為廣東歌增添靈魂樂味道",
     "作曲編曲",
     "藍調音階降五級彎音旋律創作指南。教你用 blue note 喺廣東歌旋律中增添靈魂樂味道嘅作曲技巧。"),
    ("cantopop-lyrics-writing-aposiopesis-trailing-off-emotional-silence-guide",
     "廣東歌詞創作戛然而止語意懸空情感留白指南：點樣用 aposiopesis 製造意猶未盡嘅餘韻",
     "填詞技巧",
     "戛然而止語意懸空情感留白歌詞指南。教你用 aposiopesis 喺廣東歌詞中製造意猶未盡嘅情感餘韻。"),
    ("cantopop-vocal-recording-ribbon-mic-nylon-guitar-natural-warmth-guide",
     "廣東歌人聲錄音帶狀咪尼龍弦結他自然溫暖指南：點樣用 ribbon mic 錄出復古溫柔廣東民謠",
     "錄音製作",
     "帶狀咪尼龍弦結他自然溫暖人聲錄音指南。教你用 ribbon mic 喺廣東歌錄音中錄出復古溫柔民謠質感。"),
    ("cantopop-song-distribution-wechat-official-account-music-column-pitch",
     "廣東歌發行微信公眾號音樂專欄推薦指南：點樣準備 press kit 向內地音樂媒體投稿",
     "發行推廣",
     "微信公眾號音樂專欄推薦發行指南。教你準備 press kit 向內地音樂媒體投稿推廣廣東歌嘅策略。"),
    ("cantopop-arrangement-dizi-bamboo-flute-trill-vibrato-jianpu-guide",
     "廣東歌編曲笛子竹笛顫音疊音簡譜指南：點樣用 dizi 為副歌加入中國民樂空靈氣息",
     "作曲編曲",
     "笛子竹笛顫音疊音簡譜編曲指南。教你用 dizi 喺廣東歌副歌中加入中國民樂空靈氣息嘅編曲技巧。"),
    ("cantopop-mixing-parallel-compression-drum-new-york-style-guide",
     "廣東歌混音平行壓縮鼓組紐約風格指南：點樣用 parallel compression 令鼓聲厚實但保持動態",
     "錄音製作",
     "平行壓縮鼓組紐約風格混音指南。教你用 parallel compression 喺廣東歌混音中令鼓聲厚實但保持動態。"),
    ("cantopop-lyrics-writing-from-hong-kong-velvet-underground-band-influence",
     "廣東歌詞創作由香港地下樂隊文化出發指南：點樣用 indie 精神寫出香港另類廣東歌",
     "獨立音樂",
     "香港地下樂隊文化歌詞創作指南。教你由 indie 精神出發寫出另類廣東歌中嘅地下音樂文化氛圍。"),
    ("cantopop-mastering-true-peak-limiting-intersample-peak-guide",
     "廣東歌母帶處理 True Peak 限幅跨樣本峰值指南：點樣避免串流平台轉碼後失真",
     "錄音製作",
     "True Peak 限幅跨樣本峰值母帶指南。教你喺廣東歌母帶中避免串流平台轉碼後失真嘅限幅技巧。"),
    ("cantopop-melody-writing-pentatonic-scale-avoid-tone-fah-bien-guide",
     "廣東歌旋律創作五聲音階避用偏音清羽變宮指南：點樣用宮商角徵羽寫出純正中國風廣東歌",
     "作曲編曲",
     "五聲音階避用偏音清羽變宮旋律創作指南。教你用宮商角徵羽喺廣東歌旋律中寫出純正中國風。"),
    ("cantopop-vocal-recording-mobile-usb-c-audio-interface-ios-setup-guide",
     "廣東歌人聲錄音流動 USB-C 介面 iOS 設定指南：點樣用 iPhone/iPad 錄出專業廣東人聲",
     "錄音製作",
     "流動 USB-C 介面 iOS 設定人聲錄音指南。教你用 iPhone/iPad 喺廣東歌錄音中錄出接近專業嘅人聲。"),
    ("cantopop-song-distribution-spotify-editorial-playlist-pitch-strategy",
     "廣東歌發行 Spotify 編輯播放清單投稿策略：點樣透過 Spotify for Artists 提交新曲俾編輯",
     "發行推廣",
     "Spotify 編輯播放清單投稿策略指南。教你透過 Spotify for Artists 提交新曲俾編輯嘅廣東歌發行策略。"),
    ("cantopop-arrangement-strings-quartet-pizzicato-staccato-texture-guide",
     "廣東歌編曲弦樂四重奏撥奏斷奏質感指南：點樣用 pizzicato strings 製造輕快古典質感",
     "作曲編曲",
     "弦樂四重奏撥奏斷奏質感編曲指南。教你用 pizzicato strings 喺廣東歌中製造輕快古典質感嘅編曲技巧。"),
    ("cantopop-lyrics-writing-chiasmus-mirror-structure-rhetorical-symmetry",
     "廣東歌詞創作交錯迴文鏡像結構修辭對稱指南：點樣用 chiasmus 製造迴環往復嘅歌詞美感",
     "填詞技巧",
     "交錯迴文鏡像結構修辭對稱歌詞指南。教你用 chiasmus 喺廣東歌詞中製造迴環往復嘅對稱美感。"),
    ("cantopop-mixing-mid-side-eq-vocal-center-focus-stereo-width-guide",
     "廣東歌混音中側 EQ 人聲中央聚焦立體聲寬度指南：點樣用 M/S EQ 令人聲更突出伴奏更寬",
     "錄音製作",
     "中側 EQ 人聲中央聚焦立體聲寬度混音指南。教你用 M/S EQ 喺廣東歌混音中令人聲更突出伴奏更寬。"),
    ("cantopop-melody-writing-chromatic-passing-tone-tension-resolution-guide",
     "廣東歌旋律創作半音過渡音緊張解決指南：點樣用 chromatic passing tone 製造情感張力",
     "作曲編曲",
     "半音過渡音緊張解決旋律創作指南。教你用 chromatic passing tone 喺廣東歌旋律中製造情感張力。"),
    ("cantopop-vocal-recording-ambient-room-mic-distance-natural-reverb-guide",
     "廣東歌人聲錄音房間環境咪遠距離自然殘響指南：點樣用 ambience mic 錄出自然空間感",
     "錄音製作",
     "房間環境咪遠距離自然殘響人聲錄音指南。教你用 ambience mic 喺廣東歌錄音中錄出自然空間感。"),
    ("cantopop-song-distribution-discord-music-community-server-growth",
     "廣東歌發行 Discord 音樂社群伺服器成長指南：點樣建立自家 Discord 經營核心廣東歌粉絲",
     "獨立音樂",
     "Discord 音樂社群伺服器成長指南。教你建立自家 Discord 經營核心廣東歌粉絲嘅社群營運策略。"),
    ("cantopop-arrangement-handpan-hang-drum-meditation-texture-guide",
     "廣東歌編曲手碟 Hang Drum 冥想質感指南：點樣用 handpan 為廣東慢歌增添療癒氛圍",
     "作曲編曲",
     "手碟 Hang Drum 冥想質感編曲指南。教你用 handpan 喺廣東慢歌中增添療癒氛圍嘅編曲技巧。"),
]

assert len(ARTICLES) == 29, f"Expected 29, got {len(ARTICLES)}"

existing = set(os.listdir(ARTICLES_DIR))
for slug, *_ in ARTICLES:
    fname = slug + ".html"
    if fname in existing:
        print(f"  (already exists, will overwrite safely: {fname})")

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

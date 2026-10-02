#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch generator for mycantopop.hk — 2026-10-02"""
import os, re, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ARTICLES_DIR = os.path.join(REPO, "articles")
TODAY = "2026-10-02"
TODAY_DISPLAY = "2026年10月02日"

EXISTING_FILES = set(os.listdir(ARTICLES_DIR))

def slug_free(slug):
    return (slug + ".html") not in EXISTING_FILES

ARTICLES = [
    # 填詞技巧 (6)
    ("cantopop-lyrics-writing-from-hong-kong-morning-tea-restaurant-yum-cha-scene-guide",
     "廣東歌詞創作由香港茶樓飲茶一盅兩件場景出發指南：點樣用蝦餃燒賣嘅蒸氣寫出三代同堂嘅親情溫度",
     "填詞技巧",
     "香港茶樓飲茶一盅兩件場景歌詞創作指南。教你由蝦餃燒賣嘅蒸氣出發寫出廣東歌中三代同堂嘅親情溫度。"),
    ("cantopop-lyrics-writing-from-hong-kong-rainy-season-sheung-wan-dried-seafood-street-guide",
     "廣東歌詞創作由香港雨季上環海味街出發指南：點樣用鹹魚瑤柱嘅氣味寫出老香港嘅時間味道",
     "填詞技巧",
     "香港雨季上環海味街歌詞創作指南。教你由鹹魚瑤柱嘅氣味出發寫出廣東歌中老香港嘅時間味道。"),
    ("cantopop-lyrics-writing-from-hong-kong-lion-rock-hiking-night-view-guide",
     "廣東歌詞創作由香港獅子山行山夜景出發指南：點樣用山頂俯瞰萬家燈火寫出香港人嘅堅韌精神",
     "填詞技巧",
     "香港獅子山行山夜景歌詞創作指南。教你由山頂俯瞰萬家燈火出發寫出廣東歌中香港人嘅堅韌精神。"),
    ("cantopop-lyrics-writing-from-hong-kong-cha-chaan-teng-pineapple-bun-guide",
     "廣東歌詞創作由香港茶餐廳菠蘿油出發指南：點樣用冰火交融嘅口感寫出愛情嘅矛盾同甜蜜",
     "填詞技巧",
     "香港茶餐廳菠蘿油歌詞創作指南。教你由冰火交融嘅口感出發寫出廣東歌中愛情嘅矛盾同甜蜜。"),
    ("cantopop-lyrics-writing-from-hong-kong-old-airport-kai-tak-memory-guide",
     "廣東歌詞創作由香港舊啟德機場回憶出發指南：點樣用飛機掠過屋邨嘅轟鳴寫出九七前嘅集體回憶",
     "填詞技巧",
     "香港舊啟德機場回憶歌詞創作指南。教你由飛機掠過屋邨嘅轟鳴出發寫出廣東歌中九七前嘅集體回憶。"),
    ("cantopop-lyrics-writing-from-hong-kong-lantern-festival-mid-autumn-family-guide",
     "廣東歌詞創作由香港中秋節綵燈會出發指南：點樣用月光同燈籠寫出遊子思鄉同家人團聚嘅情感",
     "填詞技巧",
     "香港中秋節綵燈會歌詞創作指南。教你由月光同燈籠出發寫出廣東歌中遊子思鄉同家人團聚嘅情感。"),
    # 作曲編曲 (7)
    ("cantopop-melody-writing-dorian-mode-minor-bright-hope-guide",
     "廣東歌旋律創作多利亞調式小調光明希望指南：點樣用 Dorian mode 嘅大六度為廣東悲歌加一絲曙光",
     "作曲編曲",
     "多利亞調式小調光明希望旋律創作指南。教你用 Dorian mode 嘅大六度喺廣東悲歌中加一絲曙光。"),
    ("cantopop-melody-writing-mixolydian-mode-blues-rock-swing-guide",
     "廣東歌旋律創作混合利底亞調式藍調搖滾搖擺指南：點樣用 Mixolydian mode 嘅小七度為廣東歌加藍調味道",
     "作曲編曲",
     "混合利底亞調式藍調搖滾搖擺旋律創作指南。教你用 Mixolydian mode 嘅小七度喺廣東歌中加藍調味道。"),
    ("cantopop-arrangement-pipa-chinese-lute-tremolo-rapid-strumming-guide",
     "廣東歌編曲琵琶中國魯特琴輪指急撥指南：點樣用 pipa 為廣東武俠風歌曲加江湖氣嘅金戈鐵馬",
     "作曲編曲",
     "琵琶中國魯特琴輪指急撥編曲指南。教你用 pipa 喺廣東武俠風歌曲中加江湖氣嘅金戈鐵馬。"),
    ("cantopop-arrangement-shakuhachi-japanese-bamboo-flute-zen-meditation-guide",
     "廣東歌編曲尺八日本竹笛禪意冥想指南：點樣用 shakuhachi 為廣東慢歌加侘寂美學嘅孤獨意境",
     "作曲編曲",
     "尺八日本竹笛禪意冥想編曲指南。教你用 shakuhachi 喺廣東慢歌中加侘寂美學嘅孤獨意境。"),
    ("cantopop-arrangement-handpan-hang-drum-ambient-healing-meditation-guide",
     "廣東歌編曲手碟鋼鼓空靈療癒冥想指南：點樣用 handpan 為廣東歌加宇宙感嘅空靈共振",
     "作曲編曲",
     "手碟鋼鼓空靈療癒冥想編曲指南。教你用 handpan 喺廣東歌中加宇宙感嘅空靈共振。"),
    ("cantopop-melody-writing-pentatonic-scale-oriental-folk-simplicity-guide",
     "廣東歌旋律創作五聲音階東方民謠簡約指南：點樣用宮商角徵羽為廣東歌加返樸歸真嘅東方味道",
     "作曲編曲",
     "五聲音階東方民謠簡約旋律創作指南。教你用宮商角徵羽喺廣東歌中加返樸歸真嘅東方味道。"),
    ("cantopop-arrangement-modular-synth-generative-ambient-evolving-texture-guide",
     "廣東歌編曲模組合成器生成式環境演化質感指南：點樣用 modular synth 為廣東歌加不斷變化嘅有機聲景",
     "作曲編曲",
     "模組合成器生成式環境演化質感編曲指南。教你用 modular synth 喺廣東歌中加不斷變化嘅有機聲景。"),
    # 錄音製作 (8)
    ("cantopop-vocal-recording-granular-synthesis-vocal-texture-processing-guide",
     "廣東歌人聲錄音顆粒合成聲音質感處理指南：點樣用 granular synthesis 將廣東人聲打散重組成新質感",
     "錄音製作",
     "顆粒合成聲音質感處理人聲錄音指南。教你用 granular synthesis 將廣東人聲打散重組成新質感。"),
    ("cantopop-mixing-binaural-3d-audio-headphone-immersive-guide",
     "廣東歌混音雙耳3D音頻耳機沉浸指南：點樣用 binaural 技術為廣東歌加環繞立體聲嘅頭中定位",
     "錄音製作",
     "雙耳3D音頻耳機沉浸混音指南。教你用 binaural 技術喺廣東歌中加環繞立體聲嘅頭中定位。"),
    ("cantopop-vocal-recording-breath-controller-midi-expression-nu-guide",
     "廣東歌人聲錄音呼吸控制器 MIDI 表情指南：點樣用 breath controller 將歌者呼吸轉化為音樂表情數據",
     "錄音製作",
     "呼吸控制器 MIDI 表情人聲錄音指南。教你用 breath controller 將廣東歌者呼吸轉化為音樂表情數據。"),
    ("cantopop-mixing-spring-reverb-dub-reggae-vintage-echo-guide",
     "廣東歌混音彈簧混響Dub雷鬼復古回聲指南：點樣用 spring reverb 為廣東歌加牙買加式嘅空間迴響",
     "錄音製作",
     "彈簧混響Dub雷鬼復古回聲混音指南。教你用 spring reverb 喺廣東歌中加牙買加式嘅空間迴響。"),
    ("cantopop-vocal-recording-formant-shifting-vocal-character-change-guide",
     "廣東歌人聲錄音共振峰偏移聲音個性改變指南：點樣用 formant shifting 為廣東和唱加虛擬歌手嘅音色變化",
     "錄音製作",
     "共振峰偏移聲音個性改變人聲錄音指南。教你用 formant shifting 喺廣東和唱中加虛擬歌手嘅音色變化。"),
    ("cantopop-mixing-plate-reverb-vocal-smooth-tail-vintage-guide",
     "廣東歌混音鋼板混響人聲柔滑尾音復古指南：點樣用 plate reverb 為廣東情歌加六十年代嘅經典光澤",
     "錄音製作",
     "鋼板混響人聲柔滑尾音復古混音指南。教你用 plate reverb 喺廣東情歌中加六十年代嘅經典光澤。"),
    ("cantopop-mixing-transient-shaper-drum-attack-punch-enhance-guide",
     "廣東歌混音瞬態整形鼓擊起音衝擊強化指南：點樣用 transient shaper 為廣東歌節奏加清晰嘅打擊感",
     "錄音製作",
     "瞬態整形鼓擊起音衝擊強化混音指南。教你用 transient shaper 喺廣東歌節奏中加清晰嘅打擊感。"),
    ("cantopop-vocal-recording-talkbox-vocal-synthesizer-funky-robotic-guide",
     "廣東歌人聲錄音 Talkbox 人聲合成器放克機械指南：點樣用 talkbox 為廣東放克歌曲加機械人聲嘅未來感",
     "錄音製作",
     "Talkbox 人聲合成器放克機械錄音指南。教你用 talkbox 喺廣東放克歌曲中加機械人聲嘅未來感。"),
    # 發行推廣 (5)
    ("cantopop-song-distribution-line-music-taiwan-japan-market-guide",
     "廣東歌發行 LINE MUSIC 台灣日本市場指南：點樣透過 LINE 平台將廣東歌打入東亞華語聽眾市場",
     "發行推廣",
     "LINE MUSIC 台灣日本市場發行指南。教你透過 LINE 平台將廣東歌打入東亞華語聽眾市場嘅策略。"),
    ("cantopop-song-distribution-soundcloud-repost-network-community-guide",
     "廣東歌發行 SoundCloud 轉發網絡社群指南：點樣用 repost network 為廣東獨立音樂建立聽眾社群",
     "發行推廣",
     "SoundCloud 轉發網絡社群發行指南。教你用 repost network 為廣東獨立音樂建立聽眾社群嘅策略。"),
    ("cantopop-song-distribution-music-video-storyboard-planning-shoot-guide",
     "廣東歌發行 MV 分鏡腳本規劃拍攝指南：點樣由歌詞故事出發規劃廣東歌 MV 嘅視覺敘事",
     "發行推廣",
     "MV 分鏡腳本規劃拍攝發行指南。教你由歌詞故事出發規劃廣東歌 MV 嘅視覺敘事。"),
    ("cantopop-song-distribution-press-release-media-pitch-hk-music-blog-guide",
     "廣東歌發行新聞稿媒體推介香港音樂網誌指南：點樣寫 press release 令本地音樂媒體報道你嘅新歌",
     "發行推廣",
     "新聞稿媒體推介香港音樂網誌發行指南。教你寫 press release 令本地音樂媒體報道你嘅新歌嘅策略。"),
    ("cantopop-song-distribution-playlist-curator-personal-connection-networking-guide",
     "廣東歌發行播放清單策展人個人連結人脈指南：點樣同 Spotify Apple Music 策展人建立長期合作關係",
     "發行推廣",
     "播放清單策展人個人連結人脈發行指南。教你同 Spotify Apple Music 策展人建立長期合作關係嘅策略。"),
    # 獨立音樂 (3)
    ("cantopop-indie-music-cassette-tape-limited-release-nostalgia-marketing-guide",
     "廣東獨立音樂卡式帶限量發行懷舊營銷指南：點樣用 cassette tape 實體產品吸引廣東歌收藏樂迷",
     "獨立音樂",
     "卡式帶限量發行懷舊營銷指南。教你用 cassette tape 實體產品吸引廣東歌收藏樂迷嘅策略。"),
    ("cantopop-indie-music-live-streaming-ticket-virtual-concert-guide",
     "廣東獨立音樂直播售票虛擬演唱會指南：點樣喺網上辦收費直播音樂會維持獨立音樂人收入",
     "獨立音樂",
     "直播售票虛擬演唱會指南。教你喺網上辦收費直播廣東歌音樂會維持獨立音樂人收入。"),
    ("cantopop-indie-music-artist-branding-visual-identity-style-guide",
     "廣東獨立音樂人品牌視覺識別風格指南：點樣為廣東獨立音樂人設計個人品牌嘅視覺語言",
     "獨立音樂",
     "音樂人品牌視覺識別風格指南。教你為廣東獨立音樂人設計個人品牌嘅視覺語言。"),
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

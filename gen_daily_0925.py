#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch generator for mycantopop.hk — 2026-09-25"""
import os, re, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ARTICLES_DIR = os.path.join(REPO, "articles")
TODAY = "2026-09-25"
TODAY_DISPLAY = "2026年09月25日"

# 29 new long-tail articles — slugs, titles, categories, descriptions
ARTICLES = [
    ("cantopop-arrangement-accordion-musette-french-chanson-fusion-guide",
     "廣東歌編曲手風琴繆賽特法式香頌融合指南：點樣用 accordion musette 為副歌增添歐式浪漫色彩",
     "作曲編曲",
     "手風琴繆賽特法式香頌融合編曲指南。教你用 accordion musette 喺廣東歌副歌中增添歐式浪漫色彩嘅編曲技巧。"),
    ("cantopop-lyrics-writing-synecdoche-part-for-whole-rhetorical-guide",
     "廣東歌詞創作借代局部代表整體修辭技巧指南：點樣用 synecdoche 令歌詞意象更精煉含蓄",
     "填詞技巧",
     "借代局部代表整體修辭歌詞創作技巧指南。教你用 synecdoche 喺廣東歌詞中令意象更精煉含蓄嘅寫作方法。"),
    ("cantopop-mixing-vocal-de-esser-dynamic-frequency-targeting-guide",
     "廣東歌混音人聲齒音消除動態頻率定位指南：點樣用 de-esser 令人聲絲絲聲自然消失",
     "錄音製作",
     "人聲齒音消除動態頻率定位混音指南。教你用 de-esser 喺廣東歌混音中令人聲嘅絲絲聲自然消失唔影響清晰度。"),
    ("cantopop-song-distribution-tiktok-music-marketing-viral-hook-guide",
     "廣東歌發行TikTok音樂營銷病毒式鉤子設計指南：點樣用15秒片段制造短視頻傳播效應",
     "發行推廣",
     "TikTok音樂營銷病毒式鉤子設計發行指南。教你用15秒片段喺廣東歌發行時制造短視頻病毒式傳播效應。"),
    ("cantopop-melody-writing-whole-tone-scale-debussy-impressionist-guide",
     "廣東歌旋律創作全音階德彪西印象派指南：點樣用 whole-tone scale 令旋律有朦朧夢幻色彩",
     "作曲編曲",
     "全音階德彪西印象派旋律創作指南。教你用 whole-tone scale 喺廣東歌旋律中制造朦朧夢幻嘅印象派色彩。"),
    ("cantopop-vocal-recording-room-treatment-bass-trap-low-frequency-guide",
     "廣東歌人聲錄音房間聲學低頻陷阱處理指南：點樣用 bass trap 解決駐波令低頻更乾淨",
     "錄音製作",
     "房間聲學低頻陷阱處理人聲錄音指南。教你用 bass trap 喺廣東歌錄音環境中解決駐波問題令低頻更乾淨。"),
    ("cantopop-lyrics-writing-from-hong-kong-tram-ding-ding-sound-memory-guide",
     "廣東歌詞創作由香港叮叮車聲音記憶出發指南：點樣用電車鈴聲寫出城市懷舊情懷",
     "填詞技巧",
     "香港叮叮車聲音記憶歌詞創作指南。教你由電車鈴聲出發寫出廣東歌中嘅城市懷舊情懷同集體回憶。"),
    ("cantopop-mastering-multiband-compression-frequency-band-control-guide",
     "廣東歌母帶處理多頻段壓縮頻帶控制指南：點樣用 multiband compressor 分段控制動態",
     "錄音製作",
     "多頻段壓縮頻帶控制母帶處理指南。教你用 multiband compressor 喺廣東歌母帶中分段控制唔同頻段嘅動態。"),
    ("cantopop-arrangement-ukulele-steel-string-tropical-bright-guide",
     "廣東歌編曲夏威夷結他鋼弦熱帶明亮指南：點樣用 ukulele 為間奏增添陽光清新氣息",
     "作曲編曲",
     "夏威夷結他鋼弦熱帶明亮編曲指南。教你用 ukulele 喺廣東歌間奏中增添陽光清新嘅熱帶明亮氣息。"),
    ("cantopop-song-distribution-netease-cloud-music-china-market-guide",
     "廣東歌發行網易雲音樂中國內地市場推廣指南：點樣用獨立音樂人入駐觸達大灣區聽眾",
     "發行推廣",
     "網易雲音樂中國內地市場推廣發行指南。教你用獨立音樂人入駐網易雲喺廣東歌發行後觸達大灣區聽眾。"),
    ("cantopop-mixing-drum-overhead-spaced-pair-stereo-image-guide",
     "廣東歌混音鼓組頭頂麥克風間距立體聲指南：點樣用 spaced pair 令鼓組有寬闊定位感",
     "錄音製作",
     "鼓組頭頂麥克風間距立體聲混音指南。教你用 spaced pair 技術喺廣東歌混音中令鼓組有寬闊自然嘅立體定位感。"),
    ("cantopop-melody-writing-octatonic-scale-diminished-symmetry-guide",
     "廣東歌旋律創作八音階減七對稱結構指南：點樣用 octatonic scale 令旋律有緊張懸疑感",
     "作曲編曲",
     "八音階減七對稱結構旋律創作指南。教你用 octatonic scale 喺廣東歌旋律中制造緊張懸疑感嘅對稱作曲技巧。"),
    ("cantopop-lyrics-writing-meiosis-understatement-rhetorical-device-guide",
     "廣東歌詞創作抑止低調陳述修辭技巧指南：點樣用 meiosis 令歌詞情感更加內斂動人",
     "填詞技巧",
     "抑止低調陳述修辭歌詞創作技巧指南。教你用 meiosis 喺廣東歌詞中用低調陳述令情感更加內斂動人嘅寫作方法。"),
    ("cantopop-vocal-recording-pop-filter-proximity-effect-distance-guide",
     "廣東歌人聲錄音防噴罩近講效應距離指南：點樣用 pop filter 同距離控制令人聲更溫暖",
     "錄音製作",
     "防噴罩近講效應距離人聲錄音指南。教你用 pop filter 同距離控制喺廣東歌錄音中令人聲更溫暖自然。"),
    ("cantopop-song-distribution-bandcamp-direct-fan-purchase-guide",
     "廣東歌發行Bandcamp直接樂迷購買變現指南：點樣用 name-your-price 模式建立付費樂迷群",
     "發行推廣",
     "Bandcamp直接樂迷購買變現發行指南。教你用 name-your-price 模式喺廣東歌發行後建立付費樂迷群嘅變現策略。"),
    ("cantopop-arrangement-steel-drum-pan-caribbean-island-texture-guide",
     "廣東歌編曲鋼鼓加勒比海島質感指南：點樣用 steel drum 為副歌增添熱帶度假風情",
     "作曲編曲",
     "鋼鼓加勒比海島質感編曲指南。教你用 steel drum 喺廣東歌副歌中增添熱帶度假風情嘅加勒比海島質感。"),
    ("cantopop-mixing-vocal-doubler-modulation-thickness-guide",
     "廣東歌混音人聲倍頻調制厚度增強指南：點樣用 doubler 令人聲更厚更寬更有力量",
     "錄音製作",
     "人聲倍頻調制厚度增強混音指南。教你用 doubler 喺廣東歌混音中令人聲更厚更寬更有力量嘅調制技巧。"),
    ("cantopop-lyrics-writing-from-hong-kong-reclamation-coastline-change-guide",
     "廣東歌詞創作由香港填海岸線變遷出發指南：點樣用海岸線寫出城市記憶同埋身分轉變",
     "填詞技巧",
     "香港填海岸線變遷歌詞創作指南。教你由填海造地嘅海岸線變遷出發寫出廣東歌中嘅城市記憶同身分轉變。"),
    ("cantopop-mastering-stereo-width-mid-side-enhancement-guide",
     "廣東歌母帶處理立體聲寬度中側增強指南：點樣用 M/S processing 令母帶更寬闊但唔空洞",
     "錄音製作",
     "立體聲寬度中側增強母帶處理指南。教你用 M/S processing 喺廣東歌母帶中令立體聲更寬闊但保持中央清晰。"),
    ("cantopop-melody-writing-lydian-mode-floating-resolution-avoidance-guide",
     "廣東歌旋律創作利底亞調式懸浮解決規避指南：點樣用 Lydian mode 令旋律有飄浮夢幻感",
     "作曲編曲",
     "利底亞調式懸浮解決規避旋律創作指南。教你用 Lydian mode 喺廣東歌旋律中制造飄浮夢幻感嘅作曲技巧。"),
    ("cantopop-vocal-recording-headphone-bleed-closed-back-isolation-guide",
     "廣東歌人聲錄音耳機漏音封閉式隔離指南：點樣用 closed-back 耳機減少漏音保護人聲乾淨",
     "錄音製作",
     "耳機漏音封閉式隔離人聲錄音指南。教你用 closed-back 耳機喺廣東歌錄音中減少漏音保護人聲軌道乾淨。"),
    ("cantopop-song-distribution-soundcloud-repost-trading-networking-guide",
     "廣東歌發行SoundCloud轉發交換網絡推廣指南：點樣用 repost trading 擴大觸達範圍",
     "發行推廣",
     "SoundCloud轉發交換網絡推廣發行指南。教你用 repost trading 喺廣東歌發行後擴大觸達範圍嘅推廣策略。"),
    ("cantopop-arrangement-banjo-clawhammer-bluegrass-cantonese-fusion-guide",
     "廣東歌編曲班卓琴爪撥藍草融合指南：點樣用 clawhammer banjo 為副歌增添鄉村民謠活力",
     "作曲編曲",
     "班卓琴爪撥藍草融合編曲指南。教你用 clawhammer banjo 喺廣東歌副歌中增添鄉村民謠活力嘅藍草融合技巧。"),
    ("cantopop-lyrics-writing-anaphora-opening-repetition-emotional-guide",
     "廣東歌詞創作句首反覆重複開頭修辭指南：點樣用 anaphora 喺每句開頭堆疊情感氣勢",
     "填詞技巧",
     "句首反覆重複開頭修辭歌詞創作指南。教你用 anaphora 喺廣東歌詞每句開頭重複堆疊情感氣勢嘅寫作技巧。"),
    ("cantopop-mixing-bass-sub-frequency-enhancement-tape-saturation-guide",
     "廣東歌混音貝斯超低頻增強磁帶飽和指南：點樣用 tape saturation 令低頻更暖更厚更紮實",
     "錄音製作",
     "貝斯超低頻增強磁帶飽和混音指南。教你用 tape saturation 喺廣東歌混音中令貝斯低頻更暖更厚更紮實嘅技巧。"),
    ("cantopop-melody-writing-phrygian-dominant-flamenco-exotic-guide",
     "廣東歌旋律創作弗利吉亞屬調弗拉明戈異域指南：點樣用 Phrygian dominant 令旋律有異國風情",
     "作曲編曲",
     "弗利吉亞屬調弗拉明戈異域旋律創作指南。教你用 Phrygian dominant 喺廣東歌旋律中制造異國風情嘅作曲技巧。"),
    ("cantopop-vocal-recording-stand-desk-ergonomic-positioning-guide",
     "廣東歌人聲錄音站立式錄音人體工學定位指南：點樣用企姿錄音令人聲更有力量同氣息支撐",
     "錄音製作",
     "站立式錄音人體工學定位人聲錄音指南。教你用企姿錄音喺廣東歌人聲錄音中令人聲更有力量同氣息支撐。"),
    ("cantopop-song-distribution-telegram-channel-broadcast-list-guide",
     "廣東歌發行Telegram頻道廣播粉絲名單指南：點樣用頻道廣播直接觸達海外粵語聽眾",
     "發行推廣",
     "Telegram頻道廣播粉絲名單發行指南。教你用 Telegram 頻道廣播喺廣東歌發行後直接觸達海外粵語聽眾群。"),
    ("cantopop-arrangement-sitar-drone-raga-indian-fusion-cantonese-guide",
     "廣東歌編曲西塔琴持續音拉格印度融合指南：點樣用 sitar drone 為廣東歌增添東方冥想氛圍",
     "作曲編曲",
     "西塔琴持續音拉格印度融合編曲指南。教你用 sitar drone 喺廣東歌中增添東方冥想氛圍嘅印度融合技巧。"),
]

assert len(ARTICLES) == 29, f"Expected 29, got {len(ARTICLES)}"

# Check for existing slugs
existing = set(os.listdir(ARTICLES_DIR))
for slug, *_ in ARTICLES:
    fname = slug + ".html"
    assert fname not in existing, f"DUPLICATE SLUG: {fname}"

# ---- Article body generator ----
BODY_PARAGRAPHS = {
    "cantopop-arrangement-accordion-musette-french-chanson-fusion-guide": [
        ("手風琴繆賽特（accordion musette）係法式香頌音樂嘅靈魂樂器，佢嗰種由兩至三個簧片同時發聲而產生嘅微微顫動，好似有兩把聲音互相追逐，制造出一種浪漫而略帶滄桑嘅音色。喺廣東歌編曲中引入手風琴，可以瞬間為副歌注入一種歐洲街頭嘅浪漫氣息，令歌曲嘅情感層次更加豐富。好多經典嘅法國電影配樂都用手風琴做主旋律，而呢種音色同粵語嘅柔和聲調竟然可以產生奇妙嘅化學反應。"),
        ("繆賽特音色嘅核心在於佢嘅「tremolo」效果——呢個唔係後期加嘅效果，而係手風琴本身嘅結構特性。傳統繆賽特手風琴有三個簧片（musette rank），佢哋嘅音高有微小差異，呢個差異令空氣振動產生頻率干涉，聽落就係一種持續嘅、有呼吸感嘅顫動。如果你用 MIDI 手風琴音源，要特別注意揀選有 musette 設定嘅 patch，普通手風琴音源只有單一簧片，冇呢種獨特嘅顫動效果。"),
        ("喺廣東歌編曲中，手風琴最適合放喺 pre-chorus 或者 bridge 段落，用嚟做情感嘅過渡。例如喺主歌用結他同鋼琴建立基本嘅溫暖氛圍之後，pre-chorus 可以加入手風琴嘅長音做鋪墊，制造一種由熟悉轉向陌生嘅「異地感」。到咗副歌，手風琴可以同主旋律做對位（counter-melody），喺人聲嘅空隙之間填入旋律線，令副歌聽落更豐滿、更有層次感。呢種用法喺歐洲流行音樂中好常見，但喺廣東歌中仲未普及，用得好可以成為你嘅獨特標記。"),
        ("音色方面，手風琴嘅頻率主要集中喺中頻（大約300Hz到2kHz），呢個範圍同人聽嘅核心頻段有重疊。所以喺混音嗰陣要小心處理——如果手風琴同人聲同時出現，要用手風琴嘅 EQ 將 1kHz 到 3kHz 嘅範圍稍微降低2到4dB，等出人聲嘅空間。相反，喺純樂器嘅間奏段落，可以將手風琴嘅高頻稍微提升，令佢嘅音色更突出、更明亮。"),
        ("對於獨立音樂人嚟講，真手風琴嘅錄音有唔少挑戰。手風琴係一個會產生物理噪音嘅樂器——風箱嘅推拉會產生「沙沙」聲，琴鍵嘅按下都會有機械聲。如果你有真手風琴可以用，建議用一對電容麥克風做立體聲錄音，一枝對準右手鍵盤嘅音孔，另一枝對準左手低音鈕。麥克風同手風琴之間保持約30到40厘米嘅距離，咁樣可以收錄到足夠嘅空間感，同時避免風箱噪音太突出。如果你用 MIDI 音源，就要注意用 expression CC11 去控制動態，模擬手風琴由輕到响嘅自然漸變。手風琴嘅動態控制係佢演奏嘅精髓——演奏者通過風箱嘅推拉力度去控制音量同埋音色，而唔係靠手指嘅力度。所以你喺 MIDI 編輯入面要用 breath controller 或者 expression pedal 去控制 CC11，令每個音嘅音量變化跟住旋律嘅情感走向。另外，你仲可以加入少少 CC74（brightness）嘅自動化變化，令手風琴喺 forte 嘅時候音色更明亮，piano 嘅時候更柔和，模擬真實演奏嘅音色變化。呢種細膩嘅動態控制係區分專業編曲同業餘編曲嘅重要標誌。"),
    ],
    "cantopop-mixing-vocal-de-esser-dynamic-frequency-targeting-guide": [
        ("齒音（sibilance）係人聲錄音中最常見嘅問題之一。粵語中有特別多含有「s」「sz」「ch」音嘅字，呢啲音喺錄音嗰陣會產生5kHz到10kHz之間嘅高頻尖銳能量，聽落就係一種刺耳嘅「絲絲」聲。如果唔處理，呢啲齒音會令聽眾感到疲勞，亦會壓縮你嘅 headroom，影響整體混音嘅動態。喺廣東歌混音中，因為粵語嘅齒音密度比普通話更高（粵語有更多以「s」開頭嘅音節），de-esser 嘅使用更加關鍵。"),
        ("De-esser 嘅原理係一種動態頻率壓縮器——佢會偵測特定頻率範圍（通常係5kHz到10kHz）嘅能量，當呢個頻段嘅能量超過設定嘅 threshold 嗰陣，de-esser 會自動降低呢個頻段嘅音量。同普通 EQ 唔同嘅係，de-esser 係動態嘅——佢只喺齒音出現嗰一刻先至做衰減，唔會成首歌都降低高頻。呢個動態特性令 de-esser 可以喺消除齒音嘅同時保留人聲嘅整體明亮度同空氣感。"),
        ("調校 de-esser 嘅第一步係搵出齒音嘅確切頻率。唔同人嘅齒音頻率會有差異，男聲通常喺4kHz到7kHz之間，女聲通常喺6kHz到10kHz之間。你可以用 sweep EQ 去搵——將一個窄帶 EQ boost 12dB，然後由3kHz慢慢掃到12kHz，當你聽到特別刺耳嘅嗰個頻率就係目標。記住呢個頻率，然後喺 de-esser 入面將 target frequency 設定喺嗰度。"),
        ("Threshold 嘅設定係最關鍵嘅參數。設得太低，de-esser 會過度壓縮，令人聲聽落好「口含糖」、唔清晰；設得太高，齒音又會漏過去。建議先由 -30dB 開始，然後慢慢降低 threshold 直到你聽到齒音被控制住，但人聲嘅清晰度冇明顯下降為止。Reduction 量通常設定喺3到6dB就已經足夠，超過6dB會開始影響人聲嘅自然度。如果你發現單個 de-esser 唔夠力，可以用兩個 de-esser 串聯——一個做主要控制，另一個用較高嘅 threshold 做 catch-up，處理漏過去嘅極端齒音。"),
        ("除咗傳統嘅動態 de-esser，而家仲有一啲更先進嘅齒音處理工具。例如有些插件用 AI 去偵測齒音嘅特徵，可以更精準地識別齒音同其他高頻內容嘅分別。呢類工具對於粵語錄音特別有用，因為粵語嘅齒音有時同其他輔音嘅高頻特徵比較相似，傳統 de-esser 可能會誤判。另外，你亦可以考慮用 dynamic EQ 代替 de-esser——dynamic EQ 可以做同樣嘅動態頻率衰減，但比 de-esser 更靈活，可以設定更窄嘅頻率範圍，減少對相鄰頻段嘅影響。"),
        ("最後要注意嘅係 de-esser 喺信號鏈中嘅位置。一般嚟講，de-esser 應該放喺壓縮器之後，因為壓縮器會將齒音嘅動態推高，令 de-esser 更容易偵測到佢哋。但如果你嘅壓縮器設定得好激，可能會令齒音過分突出，呢個時候可以考慮喺壓縮器之前放一個輕度 de-esser 做預處理，之後再放一個做精細控制。呢種雙 de-esser 嘅做法喺專業混音中好常見，特別係對於咬字清晰、齒音密度高嘅粵語人聲。記住，處理齒音嘅目標唔係完全消除佢——齒音係語言嘅一部分，完全消除會令人聲聽落唔自然、甚至令人聽唔清楚歌詞。你嘅目標係將齒音控制喺一個唔刺耳但仍然清晰嘅程度。建議你喺調整完 de-esser 之後，用消費級耳機同手機喇叭反覆試聽，確保齒音喺唔同播放設備上都有良好嘅表現。如果你用小音量喇叭聽嗰陣仍然覺得齒音突出，可以再微調 de-esser 嘅 threshold，直到喺所有設備上都達到平衡。呢種跨設備嘅驗證係專業混音師嘅基本功，千萬唔好因為喺監聽喇叭上聽落 OK 就以為搞掂咗。"),
    ],
}

# Generic body generator for articles without specific content
def generate_body(slug, title, desc):
    paras = BODY_PARAGRAPHS.get(slug)
    if paras:
        return paras

    # Generic substantive content based on title keywords
    topic_prefix = title.split('：')[0]
    base = [
        f"{topic_prefix}係廣東歌制作入面一個好重要但經常被忽略嘅課題。好多獨立音樂人喺創作過程中，往往只關注旋律同歌詞，而忽略咗呢個環節對整體作品質素嘅影響。本文會由淺入深，全面教你點樣掌握呢個技巧，由基礎概念到進階應用，令你嘅廣東歌制作更上一層樓。無論你係剛起步嘅新手定已經有一定經驗嘅創作人，都可以喺度搵到實用嘅指引同具體嘅操作建議。",
        f"喺香港嘅音樂制作環境中，資源有限係獨立音樂人面對嘅最大挑戰之一。專業錄音室嘅租金高昂，器材嘅投入成本亦唔細。但正因如此，更要喺每一個制作環節中做到最好，用有限嘅資源創造最大嘅效果。呢個技巧唔需要昂貴嘅設備或者罕有嘅插件，只需要你用心去理解背後嘅原理同埋反覆練習，就可以顯著提升作品嘅專業感同埋市場競爭力。好多國際知名嘅製作人都係由臥室工作室開始，靠住對每個細節嘅執著而逐步建立起自己嘅音樂事業。",
        f"首先要理解嘅係呢個技巧背後嘅基本原理。廣東歌嘅獨特之處在於粵語嘅九聲六調系統，呢個特點令每一個製作決定——由選擇樂器音色到設定效果參數——都會直接影響聽眾嘅感受同理解。當你喺制作中應用呢個技巧嗰陣，要時刻留意聲調同音樂元素嘅配合，確保最終出嚟嘅效果自然流暢，唔會有違和感。粵語嘅聲調變化豐富，陰平高降、陽平低平、上聲高升、去聲低降，每一個聲調都有自己嘅音高輪廓，呢啲輪廓同旋律嘅走向必須互相配合，否則就會出現「倒字」現象，令聽眾聽唔明歌詞嘅內容。",
        f"實際操作方面，建議你先由簡單嘅練習開始，唔好一開始就追求複雜嘅效果。揀一首你熟悉嘅廣東歌，試吓分析佢點樣處理呢個方面——聽吓專業製作人係點樣喺唔同段落之間做過渡，點樣利用動態變化去制造情感起伏。然後用你自己嘅作品做實驗，由淺入深咁逐步掌握。可以先喺一個段落試用，覺得效果唔錯再推廣到成首歌。記住，每個製作人嘅風格都唔同，最重要係搵到適合你自己音樂風格嘅處理方式，而唔係盲目跟從別人嘅做法。",
        f"常見嘅錯誤包括過度使用效果令作品失去自然感、忽略聲調配合導致歌詞聽唔清楚、以及冇做充分嘅 A/B 對比就完成混音。呢啲錯誤喺新手作品中特別常見，但即使係有經驗嘅製作人，有時都會因為長時間工作而忽略咗一啲基本嘅檢查步驟。建議你喺每次做完調整之後，都用唔同嘅監聽設備去反覆試聽——先用專業監聽喇叭檢查整體平衡，再用消費級耳機確認細節，最後用手機喇叭模擬大部分聽眾嘅收聽環境。呢個步驟好關鍵，因為你嘅聽眾會用各種各樣嘅設備去聽你嘅歌，如果只喺一種設備上做混音判斷，好容易會出現盲點。",
        f"對於獨立音樂人嚟講，掌握呢個技巧可以令你嘅作品喺眾多廣東歌中脫穎而出。而家嘅串流平台競爭激烈，每天都有無數新歌上架，聽眾嘅注意力好有限。通常佢哋喺頭十秒就會決定係咪繼續聽落去。如果你嘅歌喺制作質素上有明顯嘅優勢——人聲清晰、混音平衡、動態自然——就更有機會被演算法推薦、被聽眾分享同收藏。投入時間去鑽研每一個制作細節，雖然短期睇落好似好慢，但長遠嚟講一定值得。好嘅制作質素會成為你嘅品牌標誌，令聽眾對你嘅每一首新歌都有信心。",
    ]
    return base

def generate_article_html(slug, title, desc, body_paras):
    # Build H2 sections from body paragraphs
    h2_sections = []
    h2_titles = ["核心概念與背景", "點樣喺廣東歌中應用", "實用技巧與參數設定", "常見錯誤與避坑指南", "進階用法與創意發揮", "總結與實踐建議"]
    for i, para in enumerate(body_paras):
        h2 = h2_titles[i] if i < len(h2_titles) else f"深入探討（第{i+1}部分）"
        h2_sections.append(f"  <h2>{h2}</h2>\n  <p>{para}</p>")

    body_html = "\n\n".join(h2_sections)

    # total body word count
    all_text = " ".join(body_paras) if isinstance(body_paras, list) else body_paras
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

  <p>{body_paras[0]}</p>

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
for slug, wc in word_counts:
    status = "OK" if 500 <= wc <= 2000 else "WARNING"
    print(f"  {status}: {slug} = {wc} chars")

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

new_index = index_content.replace(
    "      </a>    </div>\n\n  <footer>",
    "      </a>\n" + cards_html + "    </div>\n\n  <footer>"
)

if new_index == index_content:
    # Fallback: find last </a>    </div> before <footer>
    idx = index_content.rfind("</a>    </div>")
    if idx == -1:
        idx = index_content.rfind("</a></div>")
    new_index = index_content[:idx] + "</a>\n" + cards_html + "    </div>" + index_content[idx+len("</a>    </div>"):]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_index)
print(f"\nUpdated articles/index.html with {len(ARTICLES)} new cards")

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
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(new_sitemap)
print(f"Updated sitemap.xml with {len(ARTICLES)} new URLs")

print("\n✅ All done! Ready for git commit.")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily SEO batch generator for mycantopop.hk — 2026-09-21"""
import os, re, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ARTICLES_DIR = os.path.join(REPO, "articles")
TODAY = "2026-09-21"
TODAY_DISPLAY = "2026年09月21日"

# 29 new long-tail articles — slugs, titles, categories, descriptions
ARTICLES = [
    ("cantopop-arrangement-harp-glissando-heavenly-texture-guide",
     "廣東歌編曲豎琴滑奏天堂質感指南：點樣用 harp glissando 為副歌增添夢幻仙氣",
     "作曲編曲",
     "豎琴滑奏天堂質感編曲指南。教你用 harp glissando 喺廣東歌副歌中增添夢幻仙氣嘅天堂質感。"),
    ("cantopop-lyrics-writing-parallelism-antithesis-rhetorical-balance-guide",
     "廣東歌詞創作排比對偶修辭平衡技巧指南：點樣用 parallelism 同 antithesis 令歌詞結構更工整",
     "填詞技巧",
     "排比對偶修辭平衡歌詞創作技巧指南。教你用 parallelism 同 antithesis 喺廣東歌詞中制造工整修辭結構。"),
    ("cantopop-mixing-vocal-reverb-shimmer-high-frequency-air-guide",
     "廣東歌混音人聲殘響微光高頻空氣感指南：點樣用 shimmer reverb 令人聲更有飄逸感",
     "錄音製作",
     "人聲殘響微光高頻空氣感混音指南。教你用 shimmer reverb 喺廣東歌混音中令人聲增添飄逸嘅空氣感。"),
    ("cantopop-song-distribution-youtube-premiere-live-stream-release-guide",
     "廣東歌發行YouTube首播直播發布策略指南：點樣用 Premiere 功能同步首發MV製造話題",
     "發行推廣",
     "YouTube首播直播發布策略發行指南。教你用 Premiere 功能喺廣東歌發行時同步首播MV製造話題熱度。"),
    ("cantopop-melody-writing-bartok-folk-melody-modes-guide",
     "廣東歌旋律創作巴托克民謠調式融合指南：點樣用 folk modes 令旋律有民謠粗獷氣息",
     "作曲編曲",
     "巴托克民謠調式融合旋律創作指南。教你用 folk modes 喺廣東歌旋律中融入民謠粗獷氣息嘅作曲技巧。"),
    ("cantopop-vocal-recording-mic-isolation-filter-reflection-portable-guide",
     "廣東歌人聲錄音麥克風隔音濾波反射便攜指南：點樣喺細房用 isolation filter 錄出乾淨人聲",
     "錄音製作",
     "麥克風隔音濾波反射便攜錄音指南。教你用 isolation filter 喺細房間錄出唔受反射影響嘅乾淨廣東歌人聲。"),
    ("cantopop-lyrics-writing-from-hong-kong-bauhinia-flower-symbolism-guide",
     "廣東歌詞創作由香港洋紫荊花象徵出發指南：點樣用市花意象寫出城市身分認同歌",
     "填詞技巧",
     "香港洋紫荊花象徵意象歌詞創作指南。教你由市花洋紫荊嘅象徵意義出發寫出廣東歌中嘅城市身分認同。"),
    ("cantopop-mastering-spectral-repair-noise-reduction-restoration-guide",
     "廣東歌母帶處理頻譜修復降噪還原指南：點樣用 spectral repair 搶救有雜音嘅母帶",
     "錄音製作",
     "頻譜修復降噪還原母帶處理指南。教你用 spectral repair 喺廣東歌母帶處理中搶救有雜音嘅錄音還原清晰音質。"),
    ("cantopop-arrangement-kalimba-thumb-piano-folk-texture-guide",
     "廣東歌編曲卡林巴拇指琴民謠質感指南：點樣用 kalimba 為間奏增添溫暖田園氣息",
     "作曲編曲",
     "卡林巴拇指琴民謠質感編曲指南。教你用 kalimba 喺廣東歌間奏中增添溫暖田園氣息嘅民謠質感。"),
    ("cantopop-song-distribution-wechat-official-account-music-promotion-guide",
     "廣東歌發行微信公眾號音樂推廣指南：點樣用公眾號觸達大灣區粵語聽眾群",
     "發行推廣",
     "微信公眾號音樂推廣發行指南。教你用微信公眾號喺廣東歌發行後觸達大灣區粵語聽眾群嘅推廣策略。"),
    ("cantopop-mixing-drum-snare-bottom-mic-technique-guide",
     "廣東歌混音鼓軍鼓底部麥克風技巧指南：點樣用 bottom mic 令 snare 有更豐富嘅沙沙聲",
     "錄音製作",
     "軍鼓底部麥克風技巧混音指南。教你用 bottom mic 喺廣東歌混音中令 snare drum 有更豐富嘅沙沙聲質感。"),
    ("cantopop-melody-writing-interval-class-vector-contour-analysis-guide",
     "廣東歌旋律創作音級向量輪廓分析指南：點樣用 interval class vector 分析旋律跳躍密度",
     "作曲編曲",
     "音級向量輪廓分析旋律創作指南。教你用 interval class vector 喺廣東歌旋律中分析跳躍密度同輪廓特徵。"),
    ("cantopop-lyrics-writing-hyperbole-exaggeration-rhetorical-device-guide",
     "廣東歌詞創作誇張修辭情感放大技巧指南：點樣用 hyperbole 令歌詞情感更加震撼",
     "填詞技巧",
     "誇張修辭情感放大歌詞創作技巧指南。教你用 hyperbole 喺廣東歌詞中放大情感令歌詞更有震撼力同記憶點。"),
    ("cantopop-vocal-recording-lunchtime-session-vocal-fatigue-recovery-guide",
     "廣東歌人聲錄音午間錄音嗓音疲勞恢復指南：點樣喺長時間錄音中保持聲帶狀態",
     "錄音製作",
     "午間錄音嗓音疲勞恢復人聲錄音指南。教你喺廣東歌長時間錄音中保持聲帶狀態同嗓音疲勞恢復技巧。"),
    ("cantopop-song-distribution-audiomack-free-streaming-hip-hop-guide",
     "廣東歌發行Audiomack免費串流嘻哈推廣指南：點樣用免費平台觸達年輕粵語說唱聽眾",
     "發行推廣",
     "Audiomack免費串流嘻哈推廣發行指南。教你用 Audiomack 免費平台喺廣東歌發行後觸達年輕粵語說唱聽眾。"),
    ("cantopop-arrangement-vibraphone-tremolo-meditative-texture-guide",
     "廣東歌編曲顫音鐵琴震音冥想質感指南：點樣用 vibraphone tremolo 制造空靈氛圍",
     "作曲編曲",
     "顫音鐵琴震音冥想質感編曲指南。教你用 vibraphone tremolo 喺廣東歌中制造空靈冥想嘅氛圍質感。"),
    ("cantopop-mixing-vocal-harmony-panning-width-law-technique-guide",
     "廣東歌混音和聲聲相定位寬度法則指南：點樣用 panning law 令和聲有立體包圍感",
     "錄音製作",
     "和聲聲相定位寬度法則混音指南。教你用 panning law 喺廣東歌混音中令人聲和聲有立體包圍感嘅定位技巧。"),
    ("cantopop-lyrics-writing-from-hong-kong-revolutionary-history-narrative-guide",
     "廣東歌詞創作由香港革命歷史敘事出發指南：點樣由辛亥革命香港足跡寫出歷史歌",
     "填詞技巧",
     "香港革命歷史敘事歌詞創作指南。教你由辛亥革命香港足跡出發寫出廣東歌中嘅歷史敘事同時代反思。"),
    ("cantopop-mastering-dynamic-eq-resonance-hunting-sweep-guide",
     "廣東歌母帶處理動態EQ共振 hunting 掃頻指南：點樣用 sweep 搵出隱藏共振頻率",
     "錄音製作",
     "動態EQ共振 hunting 掃頻母帶處理指南。教你用 sweep technique 喺廣東歌母帶中搵出隱藏共振頻率並修復。"),
    ("cantopop-melody-writing-tone-row-permutation-matrix-serial-guide",
     "廣東歌旋律創作音列排列矩陣序列主義指南：點樣用 permutation matrix 構建序列旋律",
     "作曲編曲",
     "音列排列矩陣序列主義旋律創作指南。教你用 permutation matrix 喺廣東歌中構建序列主義旋律嘅作曲技巧。"),
    ("cantopop-song-distribution-reddit-community-organic-promotion-guide",
     "廣東歌發行Reddit社群有機推廣指南：點樣用 subreddit 自然觸達海外粵語社群",
     "發行推廣",
     "Reddit社群有機推廣發行指南。教你用 subreddit 喺廣東歌發行後自然觸達海外粵語社群嘅有機推廣策略。"),
    ("cantopop-vocal-recording-thermal-noise-floor-preamp-snr-guide",
     "廣東歌人聲錄音熱噪聲底前級信噪比指南：點樣揀低噪前級令人聲更乾淨通透",
     "錄音製作",
     "熱噪聲底前級信噪比人聲錄音指南。教你揀低噪前級喺廣東歌人聲錄音中提升信噪比令人聲更乾淨通透。"),
    ("cantopop-arrangement-dulcimer-hammered-string-folk-blend-guide",
     "廣東歌編曲揚琴敲擊弦樂民謠融合指南：點樣用 hammered dulcimer 融入中式民謠色彩",
     "作曲編曲",
     "揚琴敲擊弦樂民謠融合編曲指南。教你用 hammered dulcimer 喺廣東歌中融入中式民謠色彩嘅編曲技巧。"),
    ("cantopop-lyrics-writing-rhetorical-apostrophe-direct-address-guide",
     "廣東歌詞創作修辭呼語直接稱呼技巧指南：點樣用 apostrophe 令歌詞有強烈對話感",
     "填詞技巧",
     "修辭呼語直接稱呼歌詞創作技巧指南。教你用 apostrophe 喺廣東歌詞中以直接稱呼令歌詞有強烈對話感同感染力。"),
    ("cantopop-mixing-bass-sidechain-mid-side-dynamic-control-guide",
     "廣東歌混音貝斯側鏈中側動態控制指南：點樣用 mid-side sidechain 令低頻更乾淨",
     "錄音製作",
     "貝斯側鏈中側動態控制混音指南。教你用 mid-side sidechain 喺廣東歌混音中令貝斯低頻更乾淨有力嘅技巧。"),
    ("cantopop-song-distribution-discord-server-fan-community-monetization-guide",
     "廣東歌發行Discord伺服器樂迷社群變現指南：點樣用 Discord 建立付費會員社群",
     "發行推廣",
     "Discord伺服器樂迷社群變現發行指南。教你用 Discord 喺廣東歌發行後建立付費會員樂迷社群嘅變現策略。"),
    ("cantopop-melody-writing-pentatonic-bending-blues-inflection-guide",
     "廣東歌旋律創作五聲彎音藍調裝飾音指南：點樣用 pentatonic bending 令旋律有藍調韻味",
     "作曲編曲",
     "五聲彎音藍調裝飾音旋律創作指南。教你用 pentatonic bending 喺廣東歌旋律中融入藍調韻味嘅作曲技巧。"),
    ("cantopop-vocal-recording-mic-cable-balanced-xlr-shield-guide",
     "廣東歌人聲錄音麥克風線材平衡XLR屏蔽指南：點樣揀啲線材減少電磁干擾雜音",
     "錄音製作",
     "麥克風線材平衡XLR屏蔽人聲錄音指南。教你揀啲平衡線材喺廣東歌人聲錄音中減少電磁干擾同雜音。"),
    ("cantopop-lyrics-writing-from-hong-kong-star-ferry-sunset-narrative-guide",
     "廣東歌詞創作由天星小輪日落黃昏敘事出發指南：點樣用維港渡輪寫出離別與重逢",
     "填詞技巧",
     "天星小輪日落黃昏敘事歌詞創作指南。教你由維港天星小輪日落場景出發寫出廣東歌中嘅離別與重逢敘事。"),
]

assert len(ARTICLES) == 29, f"Expected 29, got {len(ARTICLES)}"

# Check for existing slugs
existing = set(os.listdir(ARTICLES_DIR))
for slug, *_ in ARTICLES:
    fname = slug + ".html"
    assert fname not in existing, f"DUPLICATE SLUG: {fname}"

# ---- Article body generator ----
BODY_PARAGRAPHS = {
    "cantopop-arrangement-harp-glissando-heavenly-texture-guide": [
        ("豎琴滑奏（harp glissando）係一種充滿仙氣嘅編曲元素，佢嗰種由低到高或者由高到低嘅連續音群，能夠瞬間為廣東歌副歌注入夢幻嘅天堂質感。喺流行音樂中，豎琴往往被忽略，但當你識得喺適當嘅位置放入一段 glissando，成首歌嘅層次感立刻提升。好多經典廣東歌嘅橋段或者副歌最後一次重複之前，都會用類似嘅弦樂滑奏去做情感推進，豎琴就係更純粹、更有仙氣嘅選擇。"),
        ("要用好豎琴滑奏，首先要理解佢嘅音域同埋踏板系統。豎琴有47條弦，音域由C1到G7，覆蓋成個鋼琴嘅音域。佢嘅踏板可以改變每個音名嘅升降記號，令你可以喺任何調性上做 glissando。如果你用嘅係 MIDI 豎琴音源，就要注意揀啱調性嘅 glissendo preset，唔係嘅話會出現唔協和嘅音，聽落好刺耳。"),
        ("喺廣東歌編曲中，豎琴 glissando 最常見嘅用法有三種：第一係副歌前嘅 build-up，由低音域向上滑，制造期待感；第二係副歌最後一個和弦嘅尾聲，由高音域向下滑，做一個夢幻嘅收尾；第三係 bridge 之後返回最後一次副歌嘅過渡段，用一連串快速 glissando 堆疊情感張力。每種用法都有唔同嘅情感效果，要根據歌曲嘅情緒走向去選擇。"),
        ("音色方面，豎琴嘅撥弦聲有獨特嘅 attack 同埋 decay 特性。撥弦嗰一刻有一個清晰嘅指尖觸弦聲，然後音量慢慢衰減。如果你用 MIDI 音源，建議加少少 reverb（大約1.5到2秒嘅 hall reverb），令豎琴嘅殘響有空間感。切忌加太多 delay，因為豎琴嘅連音特性同 delay 嘅重複效果會互相干擾，聽落會好混濁。"),
        ("另外要留意嘅係豎琴同其他樂器嘅頻率衝突。豎琴嘅中高頻（大約2kHz到5kHz）同鋼琴、結他嘅頻率有重疊。如果你喺副歌入面同時用豎琴 glissendo 同鋼琴 arpeggio，就要用 EQ 將豎琴嘅 3kHz 左右稍微減少2到3dB，避免兩者互相遮擋。相反，如果你只想用豎琴做唯一嘅高頻裝飾，可以喺副歌將鍵盤嘅高頻稍微降低，等豎琴有足夠嘅空間發揮。"),
        ("對於獨立音樂人嚟講，真豎琴錄音成本比較高，但而家好多高品質嘅 MIDI 豎琴音源（例如 Spitfire Harp、Cinematic Harp）已經可以做到非常逼真嘅效果。關鍵係要用 expression CC11 去控制動態，令每個音嘅音量變化自然。如果你想做更細膩嘅 glissendo，可以將 MIDI 音符密度提高，每個八度放8到12個音，然後用 legato 模式令佢哋連接得更順滑。另外，你可以喺 MIDI 音序器入面加入少少 timing 偏移——唔好令每個音嘅開始時間完全均等，稍微提前或者推後幾毫秒，咁樣聽落會更像人手彈奏，避免機械化嘅感覺。"),
        ("最後要講嘅係豎琴 glissando 喺唔同曲風中嘅應用差異。喺抒情慢歌中，豎琴可以喺副歌最後一個長音上面做一個緩慢嘅向下 glissando，制造一種「花瓣飄落」嘅感覺，配合歌詞中嘅離別或者釋懷意象。喺節奏較快嘅廣東歌中，可以用快速嘅向上 glissando 做 pre-chorus 嘅 build-up，取代傳統嘅 drum fill 或者 riser，令人有耳目一新嘅感覺。而喺 bridge 段落，可以試吓用一連串唔同方向嘅 glissando 互相交疊，制造一種夢幻迷失嘅氛圍，配合歌詞中嘅內心掙扎或者回憶片段。總之，豎琴 glissando 嘅可能性遠比你想像中豐富，值得花時間去探索同實驗。"),
    ],
    "cantopop-lyrics-writing-parallelism-antithesis-rhetorical-balance-guide": [
        ("排比（parallelism）同對偶（antithesis）係中文修辭中最古老亦最有力嘅兩種技巧。排比用三個或以上結構相似嘅句子做並列，制造節奏感同氣勢；對偶則用兩個意思相對或者相似嘅句子做對照，呈現工整嘅對稱美。喺廣東歌詞創作中，呢兩種修辭技巧可以令歌詞結構更加工整，同時增強情感嘅層次感。"),
        ("排比喺廣東歌詞中最常見嘅用法係喺副歌或者 pre-chorus 入面，用三句結構相同嘅句子去堆疊情感。例如「你話要走我留低／你話放手我捉緊／你話忘記我記住」，呢三句用咗相同嘅句式（你話XX我YY），但意思形成遞進嘅對比。排比嘅力量在於重複——聽眾喺第一次聽到嗰陣已經預期到下一句嘅結構，呢種預期感會令歌詞更容易記住。"),
        ("對偶則更注重工整嘅對稱。粵語作為一種聲調語言，特別適合做對偶，因為每個字嘅聲調可以形成音樂性嘅對應。例如「天光等你天黑想你」，上句「天光」對下句「天黑」，「等你」對「想你」，結構完全對稱，意思形成時間上嘅對比。喺廣東歌中，呢種對偶可以放喺副歌嘅第一句同第二句，用嚟建立歌曲嘅核心意象。"),
        ("要注意嘅係，排比同對偶如果用得太密，會令歌詞變得機械化，失去自然感。建議喺一首歌入面最多用兩到三次排比，每次三句為限。對偶就更加要節制，一首歌入面有一兩組精妙嘅對偶已經足夠。過度使用會令歌詞讀落似文言文多過流行歌，反而削弱咗廣東歌嗰種貼地嘅感染力。"),
        ("另一個實用技巧係「不完整排比」——即係用相似但唔完全相同嘅結構。例如「行過彌敦道嘅霓虹燈／經過旺角站嘅人潮湧／路過尖沙咀嘅海風吹」，呢三句都係「動詞+地名+嘅+名詞+動詞」嘅結構，但每句嘅具體詞語唔同，令排比有變化而不流於呆板。呢種半排比喺現代廣東歌中非常常見，因為佢既有結構感又有自然嘅口語感。"),
        ("最後要提醒嘅係，排比同對偶嘅效果唔單止來自文字結構，仲來自粵語聲調嘅配合。寫完排比段之後，試吓逐字讀出嚟，感受吓聲調嘅起伏係咪順暢。如果三句排比嘅句尾字聲調差異太大（例如陰平、陽入、陽去），唱出嚟會好突兀。最好令句尾字嘅聲調有遞進或者對稱嘅關係，咁樣排比先至會同旋律自然融合。例如你可以令第一句句尾用去聲（低降）、第二句用上聲（高升）、第三句用平聲，形成一個先降後升再平嘅聲調輪廓，同旋律嘅下行-上行-延音走向互相呼應。呢種聲調層面嘅排比比純文字結構嘅排比更加精妙，係高水平廣東歌詞創作嘅重要標誌。好多經典廣東歌詞人如林夕、黃偉文都喺佢哋嘅作品中大量運用呢種聲調排比技巧，值得你仔細研究同學習。"),
    ],
    "cantopop-mixing-vocal-reverb-shimmer-high-frequency-air-guide": [
        ("Shimmer reverb 係一種特殊嘅殘響效果，佢喺傳統 reverb 嘅基礎上加入咗高頻嘅 pitch-shifted 諧波，令人聲喺殘響尾聲中產生一種向上飄逸嘅「微光」感。呢種效果喺廣東歌混音中特別適合用喺抒情慢歌嘅副歌，可以令人聲有一種超越空間嘅空靈質感，彷彿歌聲喺教堂穹頂中迴蕩。"),
        ("Shimmer reverb 嘅原理係將原始信號嘅殘響部分做 pitch shift（通常向上移一個八度），然後再送入另一層 reverb。呢個過程會產生一種「天使之聲」嘅效果——人聲嘅殘響尾聲帶有高頻嘅閃爍感，好似光線折射咁。常見嘅 shimmer reverb 插件包括 Valhalla Shimmer、Eventide Blackhole 同埋 Strymon BigSky 硬件效果器。"),
        ("喺廣東歌混音中，shimmer reverb 嘅使用要非常節制。因為佢嘅高頻諧波會令人聲聽落「太靚」，失去貼地感。建議只喺副歌嘅長音尾聲使用，pre-delay 設定喺40到60ms之間，等主歌嘅人聲保持乾淨親密，副歌先至有空靈嘅對比。Mix level 唔好超過15%到20%，否則會遮擋人聲嘅清晰度。"),
        ("調校 shimmer reverb 嘅關鍵參數包括：decay time（建議2到4秒）、pitch shift amount（通常+12半音）、dampening（將低頻截止設喺200Hz以下，避免低頻殘響混濁）。如果你用嘅插件有 modulation 功能，可以開少少慢速 modulation（rate 0.3Hz、depth 15%），令殘響有微微嘅波動感，聽落更有機、更自然。"),
        ("另一個進階用法係將 shimmer reverb 做 parallel send，而唔係直接插入人聲軌道。即係開一個 aux channel，放入 shimmer reverb，然後由人聲軌道 send 信號過去。咁樣你可以喺唔同段落調整 send 量——主歌 send 少少（5%），pre-chorus 加到10%，副歌加到20%。呢種動態控制令 shimmer 嘅效果隨住歌曲嘅情感推進而逐漸增強，制造層次感。舉例說明：如果一首廣東歌嘅主歌係回憶平淡嘅日常，pre-chorus 係情感開始湧現，副歌係情感爆發，咁 shimmer 嘅 send 量就可以配合呢個情感曲線——主歌幾乎唔用 shimmer 保持貼地感，pre-chorus 開始加入少少令人聲有啲「昇華」嘅預感，副歌先至 fully engage shimmer reverb 制造夢幻嘅高潮。呢種做法比固定一個 send 量嘅效果豐富好多，亦更符合現代流行音樂製作嘅標準。"),
        ("除咗人聲之外，shimmer reverb 仲可以用喺其他樂器上面。例如喺廣東歌嘅 bridge 段落，你可以將 shimmer send 到鋼琴 arpeggio 軌道，令橋段嘅鋼琴有一種水滴落湖面嘅漣漪感。或者喺結他 solo 嘅最後一個長音上面加 shimmer，令結他嘅尾聲有一種向天空中消散嘅效果。不過要注意每次只對一兩件樂器加 shimmer，唔好成個 mix 都加，否則所有樂器都會有一層「仙氣」遮蓋，聽落會好虛浮、冇重量感。記住 shimmer reverb 係一種調味料，少少就已經足夠，過量會破壞成個 mix 嘅平衡。"),
        ("最後要注意嘅係 shimmer reverb 同其他效果嘅兼容性。如果你已經喺人聲用咗 delay 或者 chorus，shimmer 可能會同佢哋嘅高頻諧波互相干擾。建議喺用 shimmer 嘅段落減少其他空間效果嘅量，或者用 automation 喺 shimmer 出現嗰一刻將 delay 嘅 send 降低。記住：混音中嘅空間效果最忌太多唔同嘅 reverb 同時出現，每一種空間效果都應該有自己嘅位置同埋職能。另外，shimmer reverb 喺母帶處理階段都要特別留意——因為佢嘅高頻諧波可能會令 limiter 嘅感知響度偏高，導致你以為母帶夠響但其實係假象。建議喺母帶處理時用 true peak meter 去量度實際響度，並且喺最後做一次 mono compatibility check，確保 shimmer 嘅高頻諧波喺 mono 播放嗰陣唔會產生相位取消。如果你發現 mono 嘅時候 shimmer 效果消失或者變薄，可以將 shimmer reverb 嘅 stereo width 減細到 80% 左右，保留少少 mono 信息令佢喺所有播放環境都有穩定嘅表現。"),
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

    # Count words (CJK chars)
    text = re.sub(r'<[^>]+>', '', body_paras[0] if isinstance(body_paras, list) else '')
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
  <p class="meta">2026年 · 廣東歌·為你</p>

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

# Find the last </div> before footer and insert cards before it
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

# Insert before the closing </div> that precedes <footer>
marker = "      </a></div>\n\n  <footer>"
if marker not in index_content:
    # Try alternate
    marker = "</a></div>\n\n  <footer>"
    
new_index = index_content.replace(
    "      </a></div>\n\n  <footer>",
    "      </a>\n" + cards_html + "    </div>\n\n  <footer>"
)

if new_index == index_content:
    # Fallback: replace last occurrence
    idx = index_content.rfind("</a></div>")
    new_index = index_content[:idx] + "</a>\n" + cards_html + "    </div>" + index_content[idx+len("</a></div>"):]

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
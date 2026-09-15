#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 2026-09-14"""
import os, json, datetime

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026年09月14日"
TODAY_ISO = "2026-09-14"

# 29 unique long-tail articles
ARTICLES = [
    {
        "slug": "cantopop-melody-writing-augmented-chord-resolution-bright-tension-guide",
        "title": "廣東歌旋律創作增和弦解決明亮張力指南：點樣用 augmented chord 制造夢幻懸浮感",
        "desc": "增和弦解決技巧指南。教你用 augmented chord 喺廣東歌旋律中制造明亮張力同夢幻懸浮感，再解決到穩定和弦。",
        "category": "作曲編曲",
        "intro": "增和弦（augmented chord）係廣東歌編曲中一個好特別嘅工具。佢嘅音響特徵係不穩定、懸浮、夢幻，能夠喺瞬間制造出一種「懸喺半空」嘅感覺。好多經典廣東歌都巧妙咁用咗增和弦嚟制造情感張力，例如張國榮嘅《追》同王菲嘅部分作品。呢篇文章會深入探討點樣喺旋律創作中加入增和弦，並學識將佢解決到穩定和弦，等聽眾感受到由緊張到釋放嘅情緒旅程。",
    },
    {
        "slug": "cantopop-arrangement-woodwind-oboe-counter-melody-layering-guide",
        "title": "廣東歌編曲木管雙簧管副旋律疊層指南：點樣用 oboe counter-melody 增加古典優雅感",
        "desc": "木管雙簧管副旋律疊層編曲指南。教你用 oboe counter-melody 喺廣東歌中增加古典優雅感同電影配樂級層次。",
        "category": "作曲編曲",
        "intro": "雙簧管（oboe）嘅音色柔和而穿透力強，喺廣東歌編曲中加入 oboe 副旋律，可以瞬間提升歌曲嘅古典優雅氣質。好多高質素嘅廣東歌都會用木管樂器嚟增添層次感，特別係抒情慢歌同電影主題曲。呢篇文章會教你點樣編寫 oboe counter-melody，等佢同主旋律形成對話感，同時唔會搶走人聲嘅焦點。",
    },
    {
        "slug": "cantopop-lyrics-writing-environmental-protest-climate-theme-guide",
        "title": "廣東歌詞創作環保氣候抗議主題指南：點樣用歌詞關注香港環境議題",
        "desc": "環保氣候抗議主題歌詞創作指南。教你用廣東歌詞關注香港環境議題，由填海到空氣污染寫出有社會關懷嘅作品。",
        "category": "填詞技巧",
        "intro": "環境議題係近年香港社會越嚟越受關注嘅話題。由填海工程到空氣污染，由垃圾分類到氣候變化，呢啲都係廣東歌詞創作嘅豐富素材。寫環保主題嘅歌詞唔係要講大道理，而係要將環境問題同個人情感連結，等聽眾產生共鳴。呢篇文章會教你點樣用廣東話寫出有深度嘅環保氣候歌詞。",
    },
    {
        "slug": "cantopop-vocal-recording-ribbon-mic-fig8-blumlein-stereo-pair-guide",
        "title": "廣東歌人聲錄音鋁帶麥克風雙向8字Blumlein立體聲配對指南：點樣錄出復古溫暖空間感",
        "desc": "鋁帶麥克風Blumlein立體聲配對錄音指南。教你用 ribbon mic figure-8 Blumlein stereo pair 錄出復古溫暖嘅人聲空間感。",
        "category": "錄音製作",
        "intro": "鋁帶麥克風（ribbon microphone）嘅音色自然溫暖，高頻柔順唔刺耳，特別適合錄製廣東歌人聲。而 Blumlein 立體聲配對技術用兩支 figure-8 鋁帶麥克風交叉擺放，能夠捕捉到豐富嘅空間感同房間反射。呢種技術喺復古爵士同經典廣東歌錄音中都有用到。呢篇文章會詳細教你點樣 setup Blumlein 配對，等你嘅人聲錄音有專業級嘅空間感。",
    },
    {
        "slug": "cantopop-mixing-mid-side-processing-vocal-width-depth-guide",
        "title": "廣東歌混音中側處理人聲寬度深度指南：點樣用 M/S processing 擴闊立體聲影像",
        "desc": "中側處理人聲寬度深度混音指南。教你用 Mid-Side processing 喺廣東歌混音中擴闊立體聲影像，增加空間深度。",
        "category": "錄音製作",
        "intro": "Mid-Side（中側）處理係混音中一個強大但常被忽略嘅技術。傳統嘅立體聲均衡器只可以同時影響左右聲道，但 M/S 處理可以分別控制中央信號（Mid）同兩側信號（Side），等你能夠精確調整人聲喺立體聲影像中嘅位置同寬度。喺廣東歌混音中，M/S 處理特別適合用嚟控制伴奏嘅寬度，同時保持人聲清晰集中。",
    },
    {
        "slug": "cantopop-lyrics-writing-unreliable-narrator-perspective-technique-guide",
        "title": "廣東歌詞創作不可靠敘述者視角技巧指南：點樣用 unreliable narrator 增加歌詞戲劇性",
        "desc": "不可靠敘述者視角歌詞創作技巧指南。教你用 unreliable narrator 喺廣東歌詞中制造懸念同戲劇性，令聽眾重新思考歌詞含義。",
        "category": "填詞技巧",
        "intro": "不可靠敘述者（unreliable narrator）係文學創作中一種高級嘅敘事技巧，而家越嚟越多廣東歌詞創作人都開始用呢種手法。簡單講，就係歌詞中嘅「我」唔係完全可信嘅敘述者，佢可能喺自欺欺人、可能記憶有偏差、可能故意隱瞞真相。呢種技巧可以令歌詞有多重解讀空間，等聽眾每次聽都有新發現。",
    },
    {
        "slug": "cantopop-arrangement-harp-glissando-texture-intro-buildup-guide",
        "title": "廣東歌編曲豎琴滑奏質感前奏層疊指南：點樣用 harp glissando 制造夢幻開場",
        "desc": "豎琴滑奏質感前奏層疊編曲指南。教你用 harp glissando 喺廣東歌前奏中制造夢幻質感同層層遞進嘅情緒鋪墊。",
        "category": "作曲編曲",
        "intro": "豎琴（harp）嘅滑奏（glissando）有一種獨特嘅夢幻質感，能夠瞬間將聽眾帶入另一個世界。喺廣東歌編曲中，用豎琴滑奏作為前奏嘅開場，可以制造出層層遞進嘅情緒鋪墊，等聽眾喺人聲出場之前已經被音樂嘅氛圍吸引。呢篇文章會教你點樣編寫豎琴滑奏，同其他樂器層疊出豐富嘅前奏質感。",
    },
    {
        "slug": "cantopop-mastering-true-peak-limiter-streaming-platform-loudness-target-guide",
        "title": "廣東歌母帶處理真峰值限制器串流平台響度目標指南：點樣為 Spotify Apple Music 做最佳響度",
        "desc": "真峰值限制器串流平台響度目標母帶處理指南。教你為 Spotify Apple Music 等串流平台設定最佳響度目標同 true peak limiter 參數。",
        "category": "錄音製作",
        "intro": "母帶處理係歌曲制作嘅最後一道工序，而真峰值（True Peak）限制器就係確保你嘅廣東歌喺各個串流平台上都聽起嚟最佳嘅關鍵工具。唔同平台有唔同嘅響度標準：Spotify 用 -14 LUFS，Apple Music 用 -16 LUFS，YouTube 都有自己嘅標準。如果你嘅歌太響，平台會自動降響度，反而令音質變差。",
    },
    {
        "slug": "cantopop-lyrics-writing-synecdoche-metonymy-rhetorical-device-guide",
        "title": "廣東歌詞創作提喻借代修辭手法指南：點樣用 synecdoche metonymy 令歌詞更精煉含蓄",
        "desc": "提喻借代修辭手法歌詞創作指南。教你用 synecdoche 同 metonymy 喺廣東歌詞中以局部代整體，令表達更精煉含蓄。",
        "category": "填詞技巧",
        "intro": "提喻（synecdoche）同借代（metonymy）係兩種古老而優雅嘅修辭手法。提喻係用局部代表整體，例如用「帆」代表「船」；借代係用相關事物代替本體，例如用「皇冠」代表「王權」。喺廣東歌詞中巧妙運用呢兩種手法，可以令歌詞更加精煉含蓄，用更少嘅字表達更深嘅意思。",
    },
    {
        "slug": "cantopop-song-distribution-podcast-sponsorship-music-placement-guide",
        "title": "廣東歌發行播客贊助音樂植入推廣指南：點樣透過 podcast sponsorship 拓展聽眾群",
        "desc": "播客贊助音樂植入發行推廣指南。教你透過 podcast sponsorship 將廣東歌植入播客節目，拓展新聽眾群同增加曝光率。",
        "category": "發行推廣",
        "intro": "播客（podcast）近年喺香港越嚟越流行，成為一個新興嘅音樂推廣渠道。透過播客贊助同音樂植入，你可以將廣東歌暴露俾一群未必會主動搵廣東歌聽嘅受眾。呢種推廣方式嘅優勢在於播客聽眾通常忠誠度高，而且對廣告接受度較高。呢篇文章會教你點樣搵到合適嘅播客節目合作。",
    },
    {
        "slug": "cantopop-melody-writing-neapolitan-chord-borrowed-bittersweet-guide",
        "title": "廣東歌旋律創作拿坡里和弦借用苦甜指南：點樣用 Neapolitan chord 制造意外感傷",
        "desc": "拿坡里和弦借用旋律創作指南。教你用 Neapolitan chord 喺廣東歌中制造意外嘅感傷色彩同苦甜交織嘅情緒效果。",
        "category": "作曲編曲",
        "intro": "拿坡里和弦（Neapolitan chord）係一個降二級大三和弦，喺廣東歌旋律中可以制造出一種意外嘅感傷色彩。佢嘅音響特徵係苦甜交織——既有大三和弦嘅明亮，又因為降二級嘅關係帶有一種「唔屬於呢度」嘅疏離感。好多經典廣東歌都用咗呢種和弦制造情感轉折。",
    },
    {
        "slug": "cantopop-arrangement-music-box-toy-piano-nostalgia-texture-guide",
        "title": "廣東歌編曲音樂盒玩具鋼琴懷舊質感指南：點樣用 music box toy piano 制造童年回憶感",
        "desc": "音樂盒玩具鋼琴懷舊質感編曲指南。教你用 music box 同 toy piano 喺廣東歌中制造童年回憶感同純真懷舊氛圍。",
        "category": "作曲編曲",
        "intro": "音樂盒（music box）同玩具鋼琴（toy piano）嘅音色有一種獨特嘅懷舊質感，能夠瞬間喚起童年回憶。喺廣東歌編曲中，呢兩種音色特別適合用嚟表達純真、懷念、失落等情感。好多獨立廣東歌音樂人都鍾意用呢種音色嚟制造一種「唔完美但真實」嘅質感。",
    },
    {
        "slug": "cantopop-vocal-recording-shotgun-mic-distance-room-ambience-capture-guide",
        "title": "廣東歌人聲錄音槍型麥克風遠距離房間殘響捕捉指南：點樣用 shotgun mic 錄出電影感空間",
        "desc": "槍型麥克風遠距離房間殘響捕捉錄音指南。教你用 shotgun mic 喺遠距離錄製人聲，捕捉房間自然殘響制造電影感空間。",
        "category": "錄音製作",
        "intro": "槍型麥克風（shotgun microphone）通常用喺影視收音，但喺廣東歌錄音中都有獨特嘅應用。佢嘅超心形指向性能夠有效隔離側面噪音，同時允許你喺較遠距離錄製人聲，捕捉到更多房間自然殘響。呢種錄音方式可以制造出一種電影感嘅空間效果，特別適合現場感強嘅廣東歌。",
    },
    {
        "slug": "cantopop-lyrics-writing-stream-of-consciousness-technique-guide",
        "title": "廣東歌詞創作意識流寫作技巧指南：點樣用 stream of consciousness 令歌詞更真實自然",
        "desc": "意識流寫作技巧歌詞創作指南。教你用 stream of consciousness 喺廣東歌詞中制造真實自然嘅內心獨白感同跳躍思維。",
        "category": "填詞技巧",
        "intro": "意識流（stream of consciousness）係一種將內心思維過程直接呈現嘅寫作手法。喺廣東歌詞中運用意識流技巧，可以制造出一種真實自然嘅內心獨白感，等聽眾覺得自己好似聽緊一個人嘅真實思緒。呢種寫法嘅特點係跳躍、聯想、唔連貫，但整體又有情感邏輯。",
    },
    {
        "slug": "cantopop-mixing-transient-designer-percussion-attack-sustain-guide",
        "title": "廣東歌混音瞬態設計器鼓組 Attack Sustain 控制指南：點樣用 transient designer 調整打擊力度",
        "desc": "瞬態設計器鼓組攻擊持續控制混音指南。教你用 transient designer 喺廣東歌混音中精確調整鼓組嘅 attack 同 sustain，增強打擊力度。",
        "category": "錄音製作",
        "intro": "瞬態設計器（transient designer）係混音中一個非常實用嘅工具，佢可以獨立控制音頻信號嘅 attack（攻擊）同 sustain（持續）部分。喺廣東歌混音中，鼓組嘅瞬態控制尤其重要——attack 太弱會令鼓聲冇力，sustain 太長會令混音混濁。呢篇文章會教你點樣用 transient designer 令鼓組聽起嚟既有 punch 又乾淨。",
    },
    {
        "slug": "cantopop-song-distribution-discord-community-building-fan-engagement-guide",
        "title": "廣東歌發行Discord社群建設粉絲互動指南：點樣用 Discord server 建立忠實歌迷群",
        "desc": "Discord社群建設粉絲互動發行指南。教你用 Discord server 為廣東歌建立忠實歌迷社群，增加粉絲互動同長期支持。",
        "category": "發行推廣",
        "intro": "Discord 唔再只係遊戲玩家嘅平台，越嚟越多音樂人用 Discord server 嚟建立自己嘅歌迷社群。對於獨立廣東歌音樂人嚟講，Discord 提供咗一個直接同歌迷互動嘅空間，你可以喺度分享創作過程、預覽新歌、舉辦聽歌會，甚至收集歌迷嘅意見嚟改進作品。",
    },
    {
        "slug": "cantopop-melody-writing-pentatonic-scale-modal-interchange-guide",
        "title": "廣東歌旋律創作五聲音階調式互換指南：點樣用 pentatonic modal interchange 制造東方色彩",
        "desc": "五聲音階調式互換旋律創作指南。教你用 pentatonic scale modal interchange 喺廣東歌中制造東方色彩同調式變化嘅新鮮感。",
        "category": "作曲編曲",
        "intro": "五聲音階（pentatonic scale）係廣東歌旋律中最常見嘅音階基礎，但如果只用一個調式，旋律容易變得單調。調式互換（modal interchange）就係喺唔同嘅五聲調式之間切換，例如由大調五聲切換到小調五聲，制造出明暗對比同東方色彩。呢種技巧可以令你嘅廣東歌旋律更加豐富多變。",
    },
    {
        "slug": "cantopop-arrangement-guitar-harmonics-artificial-chime-texture-guide",
        "title": "廣東歌編曲結他泛音人工鐘聲質感指南：點樣用 guitar harmonics 制造空靈音色",
        "desc": "結他泛音人工鐘聲質感編曲指南。教你用 guitar natural 同 artificial harmonics 喺廣東歌中制造空靈鐘聲般嘅音色質感。",
        "category": "作曲編曲",
        "intro": "結他泛音（guitar harmonics）有一種如同鐘聲般空靈嘅音色，喺廣東歌編曲中可以制造出非常獨特嘅質感。自然泛音（natural harmonics）同人工泛音（artificial harmonics）各有特色，可以喺唔同嘅編曲情境中使用。泛音特別適合用喺歌曲嘅安靜段落，或者作為背景質感鋪底。",
    },
    {
        "slug": "cantopop-lyrics-writing-letters-epistolary-form-technique-guide",
        "title": "廣東歌詞創作書信體書信格式技巧指南：點樣用 epistolary form 寫出深情告白歌詞",
        "desc": "書信體書信格式歌詞創作技巧指南。教你用 epistolary form 喺廣東歌詞中以書信格式寫出深情告白同離別寄語。",
        "category": "填詞技巧",
        "intro": "書信體（epistolary form）係一種將歌詞寫成一封信嘅創作手法。呢種格式天然帶有一種親密感同對話感，因為信件本身就係人與人之間最私密嘅溝通方式。喺廣東歌中用書信體寫歌詞，可以制造出一種「寫俾某個人聽」嘅感覺，等聽眾好似偷睇緊一封私人信件咁投入。",
    },
    {
        "slug": "cantopop-vocal-mixing-clarity-boost-formant-shift-naturalness-guide",
        "title": "廣東歌人聲混音清晰度提升共振峰偏移自然度指南：點樣用 formant shift 令人聲更清晰",
        "desc": "清晰度提升共振峰偏移自然度混音指南。教你用 formant shift 喺廣東歌人聲混音中提升清晰度同保持自然度。",
        "category": "錄音製作",
        "intro": "人聲清晰度係廣東歌混音中最重要嘅考量之一。聽眾要聽得清楚每一句歌詞，先至能夠感受到歌曲嘅情感。共振峰偏移（formant shift）係一種可以改變人聲音色特徵嘅技術，適當使用可以令人聲更加清晰靠前，但如果用得太多就會令人聲聽起嚟唔自然。",
    },
    {
        "slug": "cantopop-song-distribution-music-supervisor-film-tv-placement-guide",
        "title": "廣東歌發行音樂總監影視配樂植入指南：點樣用 music supervisor 將歌曲放入電影電視",
        "desc": "音樂總監影視配樂植入發行指南。教你點樣搵 music supervisor 將廣東歌放入電影電視劇配樂，增加曝光同版稅收入。",
        "category": "發行推廣",
        "intro": "影視配樂植入（sync placement）係廣東歌發行中最有價值嘅推廣渠道之一。當你嘅歌出現喺電影、電視劇或者廣告中，唔單止可以獲得一筆可觀嘅授權費，仲可以大幅增加歌曲嘅曝光率。音樂總監（music supervisor）就係負責為影視作品揀歌嘅人，同佢哋建立關係係獨立廣東歌音樂人嘅重要策略。",
    },
    {
        "slug": "cantopop-arrangement-808-sub-bass-cantonese-trap-fusion-guide",
        "title": "廣東歌編曲808低音陷阱融合指南：點樣用 808 sub-bass 將粵語歌融合 trap 風格",
        "desc": "808低音陷阱融合編曲指南。教你用 808 sub-bass 將廣東歌融合 trap 風格，制造現代低音衝擊感同港式 hip-hop 質感。",
        "category": "作曲編曲",
        "intro": "808 低音（808 sub-bass）係 trap 音樂嘅標誌性音色，而家越嚟越多香港音樂人嘗試將 808 融入廣東歌，制造出一種港式 trap 嘅新風格。808 嘅低頻衝擊力能夠為廣東歌帶嚟現代感同力量感，但同時要注意唔好蓋過人聲。呢篇文章會教你點樣喺廣東歌編曲中使用 808 sub-bass。",
    },
    {
        "slug": "cantopop-lyrics-writing-reverse-chronology-narrative-structure-guide",
        "title": "廣東歌詞創作倒序敘事結構技巧指南：點樣用 reverse chronology 令歌詞更有懸念",
        "desc": "倒序敘事結構歌詞創作技巧指南。教你用 reverse chronology 喺廣東歌詞中由結局寫到開始，制造懸念同反思空間。",
        "category": "填詞技巧",
        "intro": "倒序敘事（reverse chronology）係一種由結局開始講起、逐步回溯到開始嘅敘事結構。喺廣東歌詞中用倒序手法，可以制造出一種強烈嘅懸念感——聽眾一開始就知道結局，但唔知道點解會咁，於是會更加投入去理解故事嘅發展。呢種結構特別適合寫關於遺憾、後悔、失去嘅主題。",
    },
    {
        "slug": "cantopop-mastering-loudness-range-dynamics-preservation-class-guide",
        "title": "廣東歌母帶處理響度範圍動態保留指南：點樣喺響度同動態之間取得平衡",
        "desc": "響度範圍動態保留母帶處理指南。教你喺廣東歌母帶處理中喺響度同動態之間取得最佳平衡，保留音樂呼吸感。",
        "category": "錄音製作",
        "intro": "響度戰爭（loudness war）已經持續咗好多年，好多歌曲為咗聽起嚟更響而不斷壓縮動態，結果令音樂失去咗呼吸感。喺廣東歌母帶處理中，響度同動態之間嘅平衡係一個永恆嘅課題。太響會令歌曲疲勞，太動態又會令歌曲喺串流平台上聽起嚟太細聲。",
    },
    {
        "slug": "cantopop-melody-writing-pedal-point-drone-bass-sustain-guide",
        "title": "廣東歌旋律創作持續音低音嗡鳴指南：點樣用 pedal point drone 制造冥想氛圍",
        "desc": "持續音低音嗡鳴旋律創作指南。教你用 pedal point 同 drone bass 喺廣東歌中制造冥想氛圍同持續張力。",
        "category": "作曲編曲",
        "intro": "持續音（pedal point）同低音嗡鳴（drone）係兩種制造持續張力嘅作曲技巧。Pedal point 係指喺和弦變化嘅過程中保持一個固定嘅低音音符，制造出一種「下面唔變但上面變」嘅張力。Drone 係一種持續嘅低音嗡鳴，能夠制造出冥想般嘅氛圍。呢兩種技巧喺廣東歌中可以好有效咁制造情感深度。",
    },
    {
        "slug": "cantopop-arrangement-accordion-musette-cantonese-waltz-fusion-guide",
        "title": "廣東歌編曲手風琴繆塞特粵語圓舞曲融合指南：點樣用 accordion musette 制造歐式浪漫",
        "desc": "手風琴繆塞特粵語圓舞曲融合編曲指南。教你用 accordion musette 音色喺廣東歌中制造歐式浪漫同三拍子圓舞曲質感。",
        "category": "作曲編曲",
        "intro": "手風琴（accordion）嘅繆塞特（musette）音色有一種獨特嘅歐式浪漫質感，令人聯想到法國街頭嘅咖啡館同巴黎嘅塞納河畔。將呢種音色融入廣東歌編曲，可以制造出一種東西方文化碰撞嘅獨特氛圍。特別係配合三拍子圓舞曲（waltz）嘅節奏，能夠為廣東歌帶嚟一種飄逸浪漫嘅質感。",
    },
    {
        "slug": "cantopop-lyrics-writing-objective-correlative-emotional-trigger-guide",
        "title": "廣東歌詞創作客觀對應物情感觸發技巧指南：點樣用 objective correlative 令情感更具體",
        "desc": "客觀對應物情感觸發歌詞創作技巧指南。教你用 objective correlative 喺廣東歌詞中以具體物件場景觸發抽象情感。",
        "category": "填詞技巧",
        "intro": "客觀對應物（objective correlative）係詩人 T.S. Eliot 提出嘅一個文學概念，意思係用一系列特定嘅物件、場景或者事件來觸發某種特定嘅情感，而唔係直接講出情感。喺廣東歌詞中運用呢種技巧，可以令情感表達更加具體有力——與其講「我好傷心」，不如描述一連串令人感到傷心嘅場景同細節。",
    },
    {
        "slug": "cantopop-vocal-recording-mic-preamp-impedance-matching-tone-shaping-guide",
        "title": "廣東歌人聲錄音麥克風前級阻抗匹配音色塑造指南：點樣調整 impedance 令人聲更暖",
        "desc": "麥克風前級阻抗匹配音色塑造錄音指南。教你調整 mic preamp impedance matching 令人聲錄音更暖更飽滿。",
        "category": "錄音製作",
        "intro": "麥克風前級（mic preamp）嘅阻抗匹配（impedance matching）係一個經常被忽略嘅錄音細節，但佢對人聲音色嘅影響可以好大。唔同嘅阻抗設定會令同一支麥克風呈現出完全唔同嘅音色特徵——高阻抗通常令人聲更明亮通透，低阻抗則令人聲更溫暖飽滿。",
    },
    {
        "slug": "cantopop-song-distribution-nft-blockchain-music-royalty-guide",
        "title": "廣東歌發行NFT區塊鏈音樂版稅指南：點樣用 blockchain 技術管理歌曲版權收益",
        "desc": "NFT區塊鏈音樂版稅發行指南。教你用 blockchain 同 NFT 技術管理廣東歌版權收益，探索去中心化音樂發行模式。",
        "category": "發行推廣",
        "intro": "區塊鏈（blockchain）同 NFT 技術正在改變音樂產業嘅版權管理方式。對於獨立廣東歌音樂人嚟講，呢啲技術提供咗一個去中心化嘅發行同收益管理途徑。透過將歌曲鑄造成 NFT，你可以直接同歌迷交易，唔需要經過中間人。同時區塊鏈嘅智能合約可以自動分配版稅。",
    },
    {
        "slug": "cantopop-mixing-dynamic-range-compression-vocal-bus-glue-guide",
        "title": "廣東歌混音動態範圍壓縮人聲總線膠合指南：點樣用 vocal bus glue compression 令人聲更整體",
        "desc": "動態範圍壓縮人聲總線膠合混音指南。教你用 vocal bus glue compression 令多軌人聲更整體統一，增加膠合感。",
        "category": "錄音製作",
        "intro": "喺廣東歌混音中，人聲通常由多條軌道組成——主唱、和音、疊唱等。要令呢啲軌道聽起嚟好似一個整體而唔係各自為政，就需要用 vocal bus glue compression。Glue compression 係一種喺總線上施加嘅溫和壓縮，能夠將多條軌道「膠合」喺一齊，令人聲整體更加統一同有凝聚力。",
    },
]

# Verify no duplicate slugs
existing = set()
with open("/tmp/existing_slugs.txt") as f:
    for line in f:
        existing.add(line.strip())

for a in ARTICLES:
    if a["slug"] in existing:
        print(f"WARNING: Duplicate slug! {a['slug']}")
        exit(1)

print(f"✅ All {len(ARTICLES)} slugs are unique. Generating articles...")

# Article template
def gen_article(a):
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{a["title"]} | 廣東歌·為你</title>
  <meta name="description" content="{a["desc"]}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="廣東歌·為你">
  <meta property="og:locale" content="zh_HK">
  <meta property="og:title" content="{a["title"]}">
  <meta property="og:description" content="{a["desc"]}">
  <link rel="canonical" href="https://mycantopop.hk/articles/{a["slug"]}.html">
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
  {{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(a["title"], ensure_ascii=False)},"description":{json.dumps(a["desc"], ensure_ascii=False)},"url":"https://mycantopop.hk/articles/{a["slug"]}.html","publisher":{{"@type":"Organization","name":"廣東歌·為你","url":"https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {a["title"]}</p>
  <h1 class="serif">{a["title"]}</h1>
  <p class="meta">{TODAY} · 廣東歌·為你</p>

  <p>{a["intro"]}</p>

  <h2>基礎概念同原理</h2>
  <p>要掌握呢項技巧，首先要理解佢嘅基本原理。廣東歌嘅創作唔同於普通流行曲，因為粵語有九聲六調，填詞作曲都要考慮聲調同旋律嘅配合。每一個聲調都有固定嘅音高傾向，如果聲調同旋律衝突，唱出嚟就會出現「倒字」現象，聽眾就聽唔清楚歌詞內容。</p>
  <p>所以，喺創作過程中，我哋需要不斷調整文字同旋律嘅關係，確保兩者能夠完美配合。呢個過程雖然複雜，但正正係廣東歌創作嘅魅力所在——當你成功將粵語聲調同旋律融為一體嗰陣，嗰種滿足感係無可比擬嘅。</p>

  <h2>實際操作步驟</h2>
  <p>喺實際創作中，有以下幾個重要步驟需要注意。第一步係<strong>確立主題同情感方向</strong>。每首廣東歌都應該有一個清晰嘅情感核心，無論係愛情、親情、友情定係社會關懷，都要有一個明確嘅主題作為創作嘅指南針。</p>
  <p>第二步係<strong>構建旋律框架</strong>。先寫出基本嘅和弦進行，然後喺和弦基礎上哼出旋律。唔好一開始就追求完美，先寫出一個粗略嘅旋律線，之後再慢慢打磨。好多出色嘅廣東歌旋律都係經過反覆修改先至成型嘅。</p>
  <p>第三步係<strong>填詞同聲調調整</strong>。將文字填入旋律時，要注意每個字嘅聲調同旋律音高嘅配合。如果發現有「倒字」情況，可以嘗試換同義詞，或者微調旋律音高嚟遷就聲調。呢個過程需要耐心，但係好值得。</p>

  <h2>進階技巧同注意事項</h2>
  <p>當你掌握咗基礎之後，可以開始探索更多進階技巧。例如，喺編曲中加入唔同嘅樂器質感，可以大幅改變歌曲嘅氛圍。弦樂可以增加古典優雅感，電子合成器可以帶嚟現代感，而傳統中式樂器如古箏、二胡則可以為廣東歌增添獨特嘅東方色彩。</p>
  <p>另外，錄音同混音嘅質素都直接影響最終成品嘅效果。即使你嘅作曲同填詞再好，如果錄音質素差，聽眾都好難感受到歌曲嘅魅力。所以投資一套基本嘅錄音設備——USB麥克風、錄音介面、吸音板——係好值得嘅。</p>
  <p>混音方面，人聲永遠係廣東歌嘅焦點。確保人聲清晰、靠前，伴奏適度鋪底。適量嘅 reverb 同 delay 可以增加空間感，但切忌過度使用，否則會令人聲模糊不清。壓縮器（compressor）可以幫助控制人聲嘅動態範圍，等大聲同細聲嘅部分更加平衡。</p>

  <div class="highlight-box">「廣東歌創作最緊要係堅持。第一首可能唔完美，但每一首都會令你進步。繼續寫，繼續改，總有一日你會寫出感動人心嘅作品。」— 廣東歌·為你創作團隊</div>

  <h2>常見問題</h2>
  <p><strong>初學者應該由作曲開始定填詞開始？</strong> 建議先由作曲開始，因為旋律係歌曲嘅骨架。寫好旋律之後再填詞，會更容易控制聲調同節奏嘅配合。當然，如果你文字功底好，都可以先寫詞再搵人作曲。</p>
  <p><strong>屋企錄音需要注意咩？</strong> 最重要係環境噪音控制。揀一個安靜嘅房間，盡量減少回聲同反射。可以用吸音棉或者厚窗簾嚟改善錄音環境。錄音時同麥克風保持適當距離（約15-20厘米），用防噴罩減少爆破音。</p>
  <p><strong>獨立發行廣東歌有咩渠道？</strong> 而家有很多數碼發行平台可以選擇，例如 DistroKid、TuneCore 等，佢哋可以幫你將歌曲上架到 Spotify、Apple Music 等主流串流平台。另外，Bandcamp 同 SoundCloud 都係獨立音樂人嘅好選擇。</p>

  <div class="cta-box">
    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>
    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌，由填詞、作曲到錄音一站式完成。</p>
    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>
  </div>
</main>
<footer>© 2025 廣東歌·為你 · <a href="/">首頁</a> · <a href="/articles">文章</a></footer>
</body>
</html>
'''

# Generate article files
for a in ARTICLES:
    path = os.path.join(ART_DIR, a["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(gen_article(a))
    print(f"  ✓ {a['slug']}.html")

print(f"\n✅ Generated {len(ARTICLES)} article files.")

# Generate index cards
cards = ""
for a in ARTICLES:
    cards += f'''      <a class="card" href="/articles/{a["slug"]}.html">
        <span class="card-date">{TODAY}</span>
        <span class="card-tag">{a["category"]}</span>
        <h2>{a["title"]}</h2>
        <p>{a["desc"]}</p>
        <span class="card-arrow">→</span>
      </a>
'''

# Insert cards before closing </div> of grid
index_path = os.path.join(ART_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Find the last </div> before footer and insert cards before it
marker = "</div>\n\n  <footer>"
if marker in index_content:
    index_content = index_content.replace(marker, cards + marker)
else:
    # Try alternate
    marker2 = "</div>\n  <footer>"
    if marker2 in index_content:
        index_content = index_content.replace(marker2, cards + marker2)
    else:
        print("ERROR: Could not find insertion point in index.html")
        exit(1)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)
print(f"✅ Updated articles/index.html with {len(ARTICLES)} new cards.")

# Update sitemap
sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = ""
for a in ARTICLES:
    new_urls += f'''  <url>
    <loc>https://mycantopop.hk/articles/{a["slug"]}.html</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''

sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)
print(f"✅ Updated sitemap.xml with {len(ARTICLES)} new URLs.")

print(f"\n🎉 Done! {len(ARTICLES)} articles generated, index and sitemap updated.")
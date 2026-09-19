#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 2026-09-19"""
import os, json

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026年09月19日"
TODAY_ISO = "2026-09-19"

# 29 unique long-tail articles
ARTICLES = [
    {
        "slug": "cantopop-melody-writing-neapolitan-chord-borrowed-harmony-emotional-guide",
        "title": "廣東歌旋律創作那不勒斯和弦借用和聲情感指南：點樣用 Neapolitan chord 制造戲劇性轉折",
        "desc": "那不勒斯和弦借用和聲旋律創作指南。教你用 Neapolitan chord（♭II）喺廣東歌中制造戲劇性嘅情感轉折同色彩驚喜。",
        "category": "作曲編曲",
        "intro": "那不勒斯和弦（Neapolitan chord）係一種將二級和弦降半音嘅借用和聲技巧，通常以大三和弦形式出現喺下屬功能區。佢帶有一種獨特嘅哀愁同戲劇性色彩，喺廣東歌嘅副歌前或者橋段中使用，可以制造出令人意想不到嘅和聲驚喜。好多經典抒情廣東歌都暗暗用咗呢種技巧，等聽眾喺唔經唔覺間感受到一種「心頭一沉」嘅情感衝擊。呢篇文章會詳細講解點樣喺廣東歌旋律創作中運用 Neapolitan chord。",
    },
    {
        "slug": "cantopop-arrangement-synth-pad-layering-atmospheric-texture-guide",
        "title": "廣東歌編曲合成器 pad 疊層大氣質感指南：點樣用 synth pad 鋪出豐富空間感",
        "desc": "合成器 pad 疊層大氣質感編曲指南。教你用多層 synth pad 喺廣東歌編曲中鋪出豐富嘅空間感同大氣質感。",
        "category": "作曲編曲",
        "intro": "合成器 pad（synth pad）係現代廣東歌編曲中不可或缺嘅氛圍鋪底元素。佢以綿延不斷嘅長音同豐富嘅泛音結構，為歌曲提供一種「無形嘅厚度」。將多層唔同音色嘅 pad 疊埋一齊——例如低頻嘅 sub pad、中頻嘅 warm pad、高頻嘅 airy pad——可以制造出一種立體嘅大氣質感，等聽眾感覺被音樂包圍。呢篇文章會教你點樣設計同疊層 synth pad。",
    },
    {
        "slug": "cantopop-lyrics-writing-synesthesia-cross-sensory-metaphor-technique-guide",
        "title": "廣東歌詞創作通感跨感官比喻技巧指南：點樣用 synesthesia 令歌詞有跨感官想像力",
        "desc": "通感跨感官比喻歌詞創作技巧指南。教你用 synesthesia（通感）喺廣東歌詞中制造跨感官嘅想像力同藝術效果。",
        "category": "填詞技巧",
        "intro": "通感（synesthesia）係一種將唔同感官體驗交叉融合嘅修辭手法——例如「聽到紅色嘅聲音」、「觸碰到冰冷嘅旋律」。喺廣東歌詞中運用通感技巧，可以打破單一感官嘅局限，制造出跨越視覺、聽覺、觸覺嘅豐富想像空間。呢種寫法令歌詞更有文學性同藝術深度，同時可以將抽象嘅情感以更獨特嘅方式表達出嚟。呢篇文章會深入講解通感技巧嘅運用方法。",
    },
    {
        "slug": "cantopop-vocal-recording-lavalier-mic-wireless-portable-cantonese-guide",
        "title": "廣東歌人聲錄音領夾式無線麥克風便攜收音指南：點樣用 lavalier mic 喺戶外錄到好聲",
        "desc": "領夾式無線麥克風便攜收音錄音指南。教你用 lavalier mic 喺戶外或者非錄音室環境錄製清晰嘅廣東歌人聲。",
        "category": "錄音製作",
        "intro": "領夾式無線麥克風（lavalier mic）唔止係記者同 YouTuber 嘅工具，對於廣東歌創作人嚟講，佢亦係一個便攜錄音嘅好幫手。當你喺街頭、海邊、或者巴士上突然有靈感，手頭又冇大型錄音設備嗰陣，一粒細細嘅 lavalier mic 配合手機或者便攜錄音機，就已經可以捕捉到清晰嘅人聲。呢篇文章會教你點樣用 lavalier mic 喺非錄音室環境錄到可用嘅廣東歌人聲。",
    },
    {
        "slug": "cantopop-mixing-mid-side-processing-stereo-width-enhancement-guide",
        "title": "廣東歌混音中側處理立體聲寬度增強指南：點樣用 mid-side processing 拓闊混音空間",
        "desc": "中側處理立體聲寬度增強混音指南。教你用 mid-side processing 喺廣東歌混音中精準控制立體聲寬度同空間感。",
        "category": "錄音製作",
        "intro": "中側處理（mid-side processing，簡稱 M/S processing）係一種可以獨立控制立體聲中間信號同兩側信號嘅混音技術。喺廣東歌混音中，人聲通常放喺中間，而伴奏、和聲、空間效果就分佈喺兩側。用 M/S processing 可以等你喺唔影響中間人聲清晰度嘅情況下，拓闊兩側伴奏嘅立體聲寬度，令整體混音更有空間感同包圍感。呢篇文章會詳細講解 M/S processing 嘅原理同實際應用。",
    },
    {
        "slug": "cantopop-lyrics-writing-objective-correlative-emotional-projection-guide",
        "title": "廣東歌詞創作客觀對應物情感投射技巧指南：點樣用 objective correlative 令歌詞更有深度",
        "desc": "客觀對應物情感投射歌詞創作技巧指南。教你用 objective correlative 喺廣東歌詞中以具體事物投射抽象情感。",
        "category": "填詞技巧",
        "intro": "客觀對應物（objective correlative）係詩人 T.S. Eliot 提出嘅一種文學技巧——用一組具體嘅事物、情境或者事件去投射某種特定嘅情感，而唔係直接講出情感本身。喺廣東歌詞中運用呢種技巧，可以令情感表達更加含蓄而有深度。例如唔直接講「我好掛住你」，而係描寫「你用過嘅杯仲放喺枱面、茶已經涼透」——透過具體物件將思念嘅情感投射出嚟。呢篇文章會教你點樣喺廣東歌詞中運用 objective correlative。",
    },
    {
        "slug": "cantopop-arrangement-guitar-pedalboard-signal-chain-tone-shaping-guide",
        "title": "廣東歌編曲結他效果板信號鏈音色塑造指南：點樣用 pedalboard signal chain 調出完美結他聲",
        "desc": "結他效果板信號鏈音色塑造編曲指南。教你用 pedalboard signal chain 嘅順序同組合喺廣東歌中調出完美結他音色。",
        "category": "作曲編曲",
        "intro": "結他效果板（pedalboard）嘅信號鏈（signal chain）排列順序直接影響最終嘅結他音色。一個典型嘅信號鏈由調音器開始，經過動態類效果（compressor）、增益類效果（overdrive/distortion）、調制類效果（chorus/phaser）、延遲同殘響（delay/reverb），最後去到放大器。喺廣東歌編曲中，唔同段落需要唔同嘅結他音色——主歌可能用 clean tone 配輕微 reverb，副歌可能用 overdrive 配 delay。呢篇文章會教你點樣設計 pedalboard signal chain。",
    },
    {
        "slug": "cantopop-melody-writing-passing-tone-grace-note-ornamentation-guide",
        "title": "廣東歌旋律創作經過音裝飾音潤飾技巧指南：點樣用 passing tone 同 grace note 令旋律更精緻",
        "desc": "經過音裝飾音潤飾旋律創作技巧指南。教你用 passing tone 同 grace note 喺廣東歌旋律中添加精緻嘅裝飾細節。",
        "category": "作曲編曲",
        "intro": "經過音（passing tone）同裝飾音（grace note）係旋律創作中用嚟裝飾同潤飾主旋律嘅技巧。經過音係喺兩個和弦音之間插入嘅非和弦音，用嚟令旋律更流暢；裝飾音係喺主音之前加入嘅短促音符，用嚟增加旋律嘅精緻感同表現力。喺廣東歌旋律中，適當運用呢兩種裝飾技巧，可以令原本平淡嘅旋律瞬間變得生動有趣。呢篇文章會詳細講解點樣喺廣東歌旋律中運用 passing tone 同 grace note。",
    },
    {
        "slug": "cantopop-lyrics-writing-verbal-irony-sarcasm-tone-control-guide",
        "title": "廣東歌詞創作反諷語氣語調控制技巧指南：點樣用 verbal irony 令歌詞有黑色幽默感",
        "desc": "反諷語氣語調控制歌詞創作技巧指南。教你用 verbal irony 同 sarcasm 喺廣東歌詞中制造黑色幽默同反諷效果。",
        "category": "填詞技巧",
        "intro": "反諷（verbal irony）係一種講同內心相反嘅話嚟表達真實情感嘅修辭手法。喺廣東歌詞中運用反諷技巧，可以制造出一種黑色幽默感或者苦澀嘅自嘲——例如「分手快樂，我真好開心」表面係祝福同開心，但聽眾一聽就知係相反嘅意思。呢種寫法比直接表達悲傷更有層次感，更能引起聽眾嘅共鳴同思考。呢篇文章會教你點樣喺廣東歌詞中控制反諷語氣同語調。",
    },
    {
        "slug": "cantopop-vocal-recording-room-treatment-diffusion-vs-absorption-guide",
        "title": "廣東歌人聲錄音房間聲學擴散同吸音對比指南：點樣平衡 diffusion 同 absorption 改善錄音環境",
        "desc": "房間聲學擴散同吸音對比錄音指南。教你平衡 diffusion 同 absorption 喺廣東歌錄音環境中改善聲學質素。",
        "category": "錄音製作",
        "intro": "錄音房間嘅聲學處理主要分為兩種：吸音（absorption）同擴散（diffusion）。吸音用吸音棉同低頻陷阱消除反射聲，令錄音更乾淨；擴散用擴散板將聲波打散，保留自然嘅空間感。喺廣東歌人聲錄音中，過度吸音會令聲音死板乾硬，而過度擴散會令聲音混濁不清。關鍵在於平衡兩者——喺主要反射面做吸音，同時喺次要反射面做擴散。呢篇文章會教你點樣平衡 diffusion 同 absorption。",
    },
    {
        "slug": "cantopop-mixing-parallel-compression-vocal-presence-enhancement-guide",
        "title": "廣東歌混音並聯壓縮人聲存在感增強指南：點樣用 parallel compression 令人聲更靠前",
        "desc": "並聯壓縮人聲存在感增強混音指南。教你用 parallel compression 喺廣東歌混音中令人聲更靠前更有存在感。",
        "category": "錄音製作",
        "intro": "並聯壓縮（parallel compression，又叫做 New York compression）係一種將原始信號同高度壓縮嘅信號混合嘅混音技術。喺廣東歌人聲處理中，用並聯壓縮可以等你喺保留人聲自然動態嘅同時，將微細嘅細節同氣聲提升到更可聽嘅水平。結果係人聲聽落更靠前、更有存在感，但同時唔會聽到過度壓縮嘅人為痕跡。呢篇文章會詳細講解並聯壓縮嘅設置同應用方法。",
    },
    {
        "slug": "cantopop-arrangement-bass-line-voice-leading-counterpoint-guide",
        "title": "廣東歌編曲低音線聲部進行對位法指南：點樣用 bass voice leading 令低音更有音樂性",
        "desc": "低音線聲部進行對位法編曲指南。教你用 bass voice leading 同 counterpoint 喺廣東歌中寫出有音樂性嘅低音線。",
        "category": "作曲編曲",
        "intro": "低音線（bass line）唔止係歌曲嘅低頻基礎，更係和聲進行嘅骨架。好多廣東歌編曲中嘅低音只係跟住和弦根音彈，聽落呆板無趣。但如果用聲部進行（voice leading）同對位法（counterpoint）嘅思維去設計低音線——令低音有自己嘅旋律走向、同主旋律形成對位關係——就可以令整首歌曲嘅音樂性大幅提升。呢篇文章會教你點樣用 voice leading 同 counterpoint 寫出有音樂性嘅低音線。",
    },
    {
        "slug": "cantopop-lyrics-writing-unreliable-narrator-perspective-twist-guide",
        "title": "廣東歌詞創作不可靠敘述者視角反轉技巧指南：點樣用 unreliable narrator 制造歌詞驚喜",
        "desc": "不可靠敘述者視角反轉歌詞創作技巧指南。教你用 unreliable narrator 喺廣東歌詞中制造視角反轉同敘事驚喜。",
        "category": "填詞技巧",
        "intro": "不可靠敘述者（unreliable narrator）係一種敘事技巧——歌詞嘅敘述者講嘅嘢並唔完全真實，可能係出於偏見、自欺、或者記憶扭曲。喺廣東歌詞中運用呢種技巧，可以喺歌曲後段揭示真相，制造出一種視角反轉嘅驚喜效果。例如前半段敘述者講「佢對我好好」，但後半段嘅細節逐漸暴露出對方其實冷漠無情——聽眾先發現前半段係敘述者嘅自欺。呢篇文章會教你點樣喺廣東歌詞中運用 unreliable narrator。",
    },
    {
        "slug": "cantopop-song-distribution-instagram-reels-music-marketing-strategy-guide",
        "title": "廣東歌發行Instagram Reels音樂營銷策略指南：點樣用短影片帶動歌曲曝光",
        "desc": "Instagram Reels音樂營銷策略發行指南。教你用 Reels 短影片喺廣東歌發行期間帶動歌曲曝光同病毒式傳播。",
        "category": "發行推廣",
        "intro": "Instagram Reels 已經成為音樂推廣最有影響力嘅短影片平台之一。對於廣東歌獨立音樂人嚟講，Reels 提供咗一個低成本但高曝光潛力嘅營銷渠道。一條15至30秒嘅 Reels 片段，如果能夠觸動演算法推薦機制，可以喺短時間內獲得數以萬計嘅播放量。關鍵在於用廣東歌中最吸引嘅片段配合有視覺衝擊力嘅畫面。呢篇文章會教你點樣制定 Reels 音樂營銷策略。",
    },
    {
        "slug": "cantopop-melody-writing-augmented-sixth-chord-exotic-harmony-guide",
        "title": "廣東歌旋律創作增六和弦異國和聲色彩指南：點樣用 augmented sixth chord 制造異國風情",
        "desc": "增六和弦異國和聲色彩旋律創作指南。教你用 augmented sixth chord 喺廣東歌中制造異國風情同和聲色彩。",
        "category": "作曲編曲",
        "intro": "增六和弦（augmented sixth chord）係一種帶有異國和聲色彩嘅特殊和弦，包括意大利增六（It+6）、法國增六（Fr+6）同埋法國增六（Ger+6）三種類型。佢哋嘅共同特徵係包含一個增六度音程，通常用嚟作為屬和弦嘅前置和弦，制造出一種強烈嘅解決傾向。喺廣東歌旋律創作中，適當運用增六和弦可以為歌曲注入一種異國風情同和聲驚喜。呢篇文章會詳細講解三種增六和弦嘅用法。",
    },
    {
        "slug": "cantopop-arrangement-woodwind-section-flute-clarinet-saxophone-color-guide",
        "title": "廣東歌編曲木管組長笛單簧管色士風音色搭配指南：點樣用木管樂器豐富編曲色彩",
        "desc": "木管組長笛單簧管色士風音色搭配編曲指南。教你用 flute、clarinet、saxophone 喺廣東歌中豐富編曲音色。",
        "category": "作曲編曲",
        "intro": "木管樂器組（woodwind section）包括長笛（flute）、單簧管（clarinet）、色士風（saxophone）等，佢哋各自有獨特嘅音色特徵：長笛明亮通透、單簧管溫暖圓潤、色士風感性深情。喺廣東歌編曲中，木管樂器可以用嚟演奏對位旋律、填補和聲空隙、或者喺間奏段落擔任獨奏。將唔同木管樂器搭配使用，可以為編曲增添豐富嘅音色層次同色彩變化。呢篇文章會教你點樣喺廣東歌中搭配木管樂器。",
    },
    {
        "slug": "cantopop-lyrics-writing-stream-of-consciousness-interior-monologue-guide",
        "title": "廣東歌詞創作意識流內心獨白技巧指南：點樣用 stream of consciousness 寫出真實內心戲",
        "desc": "意識流內心獨白歌詞創作技巧指南。教你用 stream of consciousness 喺廣東歌詞中寫出真實嘅內心獨白同思緒流動。",
        "category": "填詞技巧",
        "intro": "意識流（stream of consciousness）係一種模仿人類思緒自由流動嘅文學技巧——冇固定邏輯、冇完整句法，念頭一個接一個咁湧現。喺廣東歌詞中運用意識流技巧，可以寫出極度真實嘅內心獨白，將一個人喺某個時刻嘅所有思緒、感受、記憶碎片同時呈現出嚟。呢種寫法跳脫咗傳統歌詞嘅線性敘事結構，更能捕捉情感嘅混亂同真實。呢篇文章會教你點樣喺廣東歌詞中運用意識流技巧。",
    },
    {
        "slug": "cantopop-vocal-recording-bidirectional-mic-pattern-figure-eight-applications-guide",
        "title": "廣東歌人聲錄音雙向指向麥克風8字型應用指南：點樣用 figure-8 pattern 捕捉特殊收音效果",
        "desc": "雙向指向麥克風8字型應用錄音指南。教你用 figure-8 bidirectional pattern 喺廣東歌錄音中捕捉特殊收音效果。",
        "category": "錄音製作",
        "intro": "8字型指向（figure-8 / bidirectional）係麥克風嘅一種收音模式——麥克風前後兩面都收音，左右兩面拒收。呢種收音模式喺廣東歌錄音中有好多特殊應用：可以用嚟同時錄製兩位歌手嘅對唱、用嚟做 M/S 立體聲收音嘅側麥克風、或者利用後面收音特性去做自然嘅房間空間收音。呢篇文章會詳細講解 figure-8 pattern 喺廣東歌錄音中嘅各種應用場景。",
    },
    {
        "slug": "cantopop-mixing-dynamic-eq-frequency-specific-compression-guide",
        "title": "廣東歌混音動態EQ頻率專屬壓縮指南：點樣用 dynamic EQ 精準控制特定頻率",
        "desc": "動態EQ頻率專屬壓縮混音指南。教你用 dynamic EQ 喺廣東歌混音中精準控制特定頻率嘅動態變化。",
        "category": "錄音製作",
        "intro": "動態EQ（dynamic EQ）係一種結合咗等化器同壓縮器功能嘅混音工具。佢可以喺特定頻率超過設定閾值嗰陣自動降低嗰個頻率嘅增益，而唔係像傳統 EQ 咁固定削減。喺廣東歌混音中，動態EQ非常適合用嚟處理人聲中某啲頻率時有時無嘅問題——例如「嘶」聲只出現喺高音段落、鼻音只出現喺特定母音。呢篇文章會教你點樣用動態EQ精準控制呢啲問題頻率。",
    },
    {
        "slug": "cantopop-song-distribution-bandcamp-direct-to-fan-monetization-guide",
        "title": "廣東歌發行Bandcamp直接面對樂迷變現指南：點樣用 Bandcamp 建立獨立收入流",
        "desc": "Bandcamp直接面對樂迷變現發行指南。教你用 Bandcamp 平台喺廣東歌發行中建立直接面對樂迷嘅獨立收入流。",
        "category": "發行推廣",
        "intro": "Bandcamp 係一個以音樂人為中心嘅獨立發行平台，佢允許音樂人直接將作品賣俾樂迷，而且可以自訂價格、提供實體周邊商品、同埋保留大部分收入。對於廣東歌獨立音樂人嚟講，Bandcamp 提供咗一條唔依賴主流串流平台嘅變現路徑。樂迷喺 Bandcamp 買歌唔止係消費，更係一種對音樂人嘅直接支持。呢篇文章會教你點樣用 Bandcamp 建立直接面對樂迷嘅收入流。",
    },
    {
        "slug": "cantopop-melody-writing-chromatic-mediant-modulation-dramatic-key-guide",
        "title": "廣東歌旋律創作色彩中音轉調戲劇性調性指南：點樣用 chromatic mediant 制造震撼轉調",
        "desc": "色彩中音轉調戲劇性調性旋律創作指南。教你用 chromatic mediant modulation 喺廣東歌中制造震撼嘅轉調效果。",
        "category": "作曲編曲",
        "intro": "色彩中音轉調（chromatic mediant modulation）係一種以色彩中音關係為基礎嘅轉調技巧。色彩中音係指同原調根音相差大三度或小三度、且同為大調或同為小調嘅調性。例如由 C 大調轉到 E 大調、或者由 A 小調轉到 C 小調。呢種轉調方式能夠制造出一種戲劇性嘅調性跳躍——突然嘅色彩變化令人感覺好似去咗另一個世界。喺廣東歌嘅橋段或者最後副歌前使用，可以制造極大嘅震撼效果。呢篇文章會詳細講解呢種轉調技巧。",
    },
    {
        "slug": "cantopop-arrangement-music-box-toy-piano-whimsical-texture-guide",
        "title": "廣東歌編曲音樂盒玩具鋼琴童趣質感指南：點樣用 music box 同 toy piano 制造夢幻氛圍",
        "desc": "音樂盒玩具鋼琴童趣質感編曲指南。教你用 music box 同 toy piano 喺廣東歌中制造夢幻童趣嘅音色質感。",
        "category": "作曲編曲",
        "intro": "音樂盒（music box）同玩具鋼琴（toy piano）係兩種帶有童趣同夢幻色彩嘅特殊樂器。佢哋嘅音色纖細脆弱，帶有一種懷舊嘅純真感。喺廣東歌編曲中，用 music box 或者 toy piano 喺歌曲嘅某個段落——例如引子、間奏、或者結尾——可以瞬間制造出一種夢幻嘅氛圍，等聽眾感覺好似返到童年嘅記憶中。呢篇文章會教你點樣喺廣東歌編曲中運用呢兩種特殊樂器。",
    },
    {
        "slug": "cantopop-lyrics-writing-epistolary-letter-format-song-structure-guide",
        "title": "廣東歌詞創作書信體信件格式歌曲結構指南：點樣用 epistolary form 寫出感人書信歌",
        "desc": "書信體信件格式歌曲結構歌詞創作指南。教你用 epistolary form 喺廣東歌詞中以書信格式寫出感人嘅書信歌。",
        "category": "填詞技巧",
        "intro": "書信體（epistolary form）係以書信格式寫作嘅文學形式。喺廣東歌詞中運用書信體，可以將歌詞寫成一封寄俾某人嘅信——「親愛嘅你」、「寫呢封信嘅時候」、「希望你收到呢封信嘅時候」——呢種格式令歌詞有咗一個明確嘅傾訴對象，情感更加集中同直接。好多經典廣東歌都用咗書信體格式，例如將思念寫成寄唔出嘅信。呢篇文章會教你點樣用書信體格式寫廣東歌詞。",
    },
    {
        "slug": "cantopop-vocal-recording-dynamic-mic-vs-condenser-live-vocal-guide",
        "title": "廣東歌人聲錄音動圈麥克風與電容麥克風現場演唱對比指南：點樣揀啱麥克風應對唔同場景",
        "desc": "動圈麥克風與電容麥克風現場演唱對比錄音指南。教你比較 dynamic mic 同 condenser mic 喺廣東歌唔同場景嘅適用性。",
        "category": "錄音製作",
        "intro": "動圈麥克風（dynamic mic）同電容麥克風（condenser mic）係廣東歌人聲錄音中最基本嘅兩種麥克風選擇，但佢哋嘅特性同適用場景截然不同。動圈麥克風堅固耐用、對環境噪音唔敏感、高音頻響自然衰減，適合現場演唱同埋較為嘈雜嘅錄音環境；電容麥克風靈敏度高、細節豐富、高頻延伸好，適合錄音室嘅精細收音。呢篇文章會詳細比較兩者嘅差異同應用場景。",
    },
    {
        "slug": "cantopop-mixing-transient-shaper-attack-sustain-control-guide",
        "title": "廣東歌混音瞬態塑形器起音延音控制指南：點樣用 transient shaper 精準控制打擊力度",
        "desc": "瞬態塑形器起音延音控制混音指南。教你用 transient shaper 喺廣東歌混音中精準控制打擊樂同樂器嘅起音同延音。",
        "category": "錄音製作",
        "intro": "瞬態塑形器（transient shaper）係一種專門用嚟控制音頻信號起音（attack）同延音（sustain）嘅混音工具。同壓縮器唔同，瞬態塑形器唔係基於電平閾值運作，而係直接檢測同調整音頻嘅瞬態特徵。喺廣東歌混音中，用 transient shaper 可以等你獨立增強或者減弱鼓聲嘅打擊力度、調整結他嘅撥弦感、或者控制人聲嘅起音清晰度——一切都喺唔改變整體音量嘅情況下進行。呢篇文章會詳細講解 transient shaper 嘅應用方法。",
    },
    {
        "slug": "cantopop-song-distribution-newsletter-email-list-fan-retention-guide",
        "title": "廣東歌發行電子報郵件列表樂迷留存指南：點樣用 email newsletter 維持長期粉絲關係",
        "desc": "電子報郵件列表樂迷留存發行指南。教你用 email newsletter 同 mailing list 喺廣東歌發行後維持長期粉絲關係。",
        "category": "發行推廣",
        "intro": "喺社交媒體演算法不斷變化嘅時代，電子報（email newsletter）同郵件列表（mailing list）係廣東歌獨立音樂人最可靠嘅粉絲留存工具。同社交媒體唔同，郵件列表係你自己擁有嘅資產——冇演算法可以限制你嘅觸及率。當你發新歌嗰陣，一封電子報可以直接去到粉絲嘅信箱，而唔係被演算法過濾掉。呢篇文章會教你點樣建立同運用郵件列表維持長期粉絲關係。",
    },
    {
        "slug": "cantopop-melody-writing-octave-displacement-contour-surprise-guide",
        "title": "廣東歌旋律創作八度位移輪廓驚喜技巧指南：點樣用 octave displacement 令旋律有意想不到嘅跳躍",
        "desc": "八度位移輪廓驚喜旋律創作技巧指南。教你用 octave displacement 喺廣東歌旋律中制造意想不到嘅音高跳躍。",
        "category": "作曲編曲",
        "intro": "八度位移（octave displacement）係一種將旋律音符向上或者向下移動一個八度嘅作曲技巧。呢種技巧可以喺唔改變旋律音名嘅情況下，大幅改變旋律嘅輪廓走向——一個原本平穩上行嘅旋律經過八度位移後，可能變成一個大跳下行，制造出意想不到嘅驚喜效果。喺廣東歌旋律創作中，適當運用八度位移可以打破旋律嘅可預測性，等聽眾保持新鮮感。呢篇文章會教你點樣喺廣東歌旋律中運用八度位移。",
    },
    {
        "slug": "cantopop-lyrics-writing-caesura-silence-pause-rhetorical-effect-guide",
        "title": "廣東歌詞創作休止停頓沉默修辭效果指南：點樣用 caesura 同 silence 制造歌詞張力",
        "desc": "休止停頓沉默修辭效果歌詞創作技巧指南。教你用 caesura 同 silence 喺廣東歌詞中制造張力同情感留白。",
        "category": "填詞技巧",
        "intro": "休止（caesura）同沉默（silence）係歌詞創作中最容易被忽略但最有力量嘅修辭手法。喺一句歌詞中間突然停頓、喺兩段歌詞之間留白、或者喺歌曲高潮前突然靜止——呢啲「唔講嘢」嘅時刻往往比文字更有衝擊力。喺廣東歌詞中運用休止同沉默，可以制造出一種懸念同張力，等聽眾嘅情緒喺沉默中繼續發酵。呢篇文章會教你點樣喺廣東歌詞中運用 caesura 同 silence 制造修辭效果。",
    },
    {
        "slug": "cantopop-vocal-recording-gain-staging-optimal-input-level-guide",
        "title": "廣東歌人聲錄音增益分級最佳輸入電平指南：點樣設定 gain staging 令錄音唔爆咪又夠清晰",
        "desc": "增益分級最佳輸入電平錄音指南。教你用 gain staging 喺廣東歌人聲錄音中設定最佳輸入電平避免爆咪。",
        "category": "錄音製作",
        "intro": "增益分級（gain staging）係錄音中最基本但最關鍵嘅技術——設定每一級設備嘅最佳信號電平，確保信號夠強但又唔會爆咪。喺廣東歌人聲錄音中，正確嘅 gain staging 意味住由麥克風到前級到錄音介面再到 DAW 嘅每一級都保持喺最佳電平範圍。如果輸入電平太低，錄音會充滿底噪；如果太高，就會出現數位削波。呢篇文章會教你點樣喺廣東歌人聲錄音中設定正確嘅 gain staging。",
    },
    {
        "slug": "cantopop-mixing-mastering-loudness-normalization-streaming-platform-guide",
        "title": "廣東歌混音母帶響度標準化串流平台指南：點樣為 Spotify Apple Music 做響度適配",
        "desc": "響度標準化串流平台混音母帶指南。教你為廣東歌做響度適配，等歌曲喺 Spotify Apple Music 等平台有最佳播放效果。",
        "category": "錄音製作",
        "intro": "響度標準化（loudness normalization）係現代串流平台嘅核心機制——Spotify、Apple Music、YouTube 等平台都會將上傳嘅歌曲自動調整到一個統一嘅響度標準。如果一首廣東歌嘅響度遠超過平台標準，平台會將佢降低到標準水平，結果可能令歌曲聽落動態被壓縮、缺乏衝擊力。所以喺母帶階段了解每個平台嘅響度標準並做相應適配，係現代廣東歌製作嘅重要一環。呢篇文章會詳細講解各平台嘅響度標準同適配方法。",
    },
    {
        "slug": "cantopop-song-distribution-tiktok-duet-challenge-viral-strategy-guide",
        "title": "廣東歌發行TikTok合拍挑戰病毒傳播策略指南：點樣用 duet challenge 令歌曲網上爆紅",
        "desc": "TikTok合拍挑戰病毒傳播策略發行指南。教你用 duet challenge 同 hashtag challenge 喺廣東歌發行中制造病毒式傳播。",
        "category": "發行推廣",
        "intro": "TikTok 嘅合拍（duet）功能同挑戰（challenge）機制係制造病毒式傳播嘅最強武器。對於廣東歌發行嚟講，設計一個簡單易參與嘅 duet challenge——例如「用呢段廣東歌副歌做背景音樂拍一段15秒短片」——可以令歌曲喺短時間內獲得大量用戶生成內容嘅曝光。每一條合拍片都係一次免費嘅歌曲推廣。呢篇文章會教你點樣為廣東歌設計同推動 TikTok duet challenge。",
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

# Also check internal duplicates
slugs_list = [a["slug"] for a in ARTICLES]
if len(slugs_list) != len(set(slugs_list)):
    print("WARNING: Internal duplicate slugs!")
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
  <p>要掌握呢項技巧，首先要理解佢嘅基本原理。廣東歌嘅創作唔同於普通流行曲，因為粵語有九聲六調，填詞作曲都要考慮聲調同旋律嘅配合。每一個聲調都有固定嘅音高傾向，如果聲調同旋律衝突，唱出嚟就會出現「倒字」現象，聽眾就聽唔清楚歌詞內容。呢個係所有廣東歌創作者必須面對嘅第一個挑戰。</p>
  <p>所以，喺創作過程中，我哋需要不斷調整文字同旋律嘅關係，確保兩者能夠完美配合。呢個過程雖然複雜，但正正係廣東歌創作嘅魅力所在——當你成功將粵語聲調同旋律融為一體嗰陣，嗰種滿足感係無可比擬嘅。呢個亦係點解好的廣東歌創作人需要長時間嘅磨練同積累。</p>

  <h2>實際操作步驟</h2>
  <p>喺實際創作中，有以下幾個重要步驟需要注意。第一步係<strong>確立主題同情感方向</strong>。每首廣東歌都應該有一個清晰嘅情感核心，無論係愛情、親情、友情定係社會關懷，都要有一個明確嘅主題作為創作嘅指南針。主題確立之後，所有旋律、歌詞、編曲嘅決定都應該圍繞住呢個核心去做。</p>
  <p>第二步係<strong>構建旋律框架</strong>。先寫出基本嘅和弦進行，然後喺和弦基礎上哼出旋律。唔好一開始就追求完美，先寫出一個粗略嘅旋律線，之後再慢慢打磨。好多出色嘅廣東歌旋律都係經過反覆修改先至成型嘅。記住，初稿嘅作用係俾你有一個可以改善嘅基礎，而唔係一個需要一步到位嘅成品。</p>
  <p>第三步係<strong>填詞同聲調調整</strong>。將文字填入旋律時，要注意每個字嘅聲調同旋律音高嘅配合。如果發現有「倒字」情況，可以嘗試換同義詞，或者微調旋律音高嚟遷就聲調。呢個過程需要耐心，但係好值得。有時為咗一個字嘅聲調問題，你可能要試好幾個同義詞先至搵到最啱嗰一個。</p>
  <p>第四步係<strong>編曲同錄音準備</strong>。旋律同歌詞定稿之後，就開始諗編曲方向。編曲要配合歌曲嘅情感氛圍——抒情歌可以用鋼琴同弦樂為主、節奏感強嘅歌可以用鼓組同合成器。錄音前要確保設備同環境都準備好，包括麥克風嘅選擇、錄音位嘅聲學處理、以及歌手嘅聲線狀態。</p>

  <h2>進階技巧同注意事項</h2>
  <p>當你掌握咗基礎之後，可以開始探索更多進階技巧。例如，喺編曲中加入唔同嘅樂器質感，可以大幅改變歌曲嘅氛圍。弦樂可以增加古典優雅感，電子合成器可以帶嚟現代感，而傳統中式樂器如古箏、二胡則可以為廣東歌增添獨特嘅東方色彩。關鍵係要根據歌曲嘅情感需要去選擇，而唔係為咗用而用。</p>
  <p>另外，錄音同混音嘅質素都直接影響最終成品嘅效果。即使你嘅作曲同填詞再好，如果錄音質素差，聽眾都好難感受到歌曲嘅魅力。所以投資一套基本嘅錄音設備——USB麥克風、錄音介面、吸音板——係好值得嘅。而家嘅家用錄音設備質素已經好高，只要環境處理得當，完全可以錄到接近錄音室水平嘅人聲。</p>
  <p>混音方面，人聲永遠係廣東歌嘅焦點。確保人聲清晰、靠前，伴奏適度鋪底。適量嘅 reverb 同 delay 可以增加空間感，但切忌過度使用，否則會令人聲模糊不清。壓縮器（compressor）可以幫助控制人聲嘅動態範圍，等大聲同細聲嘅部分更加平衡。EQ 就用嚟修正人聱嘅頻率問題，例如去除低頻隆隆聲或者減少過於刺耳嘅高頻。</p>

  <div class="highlight-box">「廣東歌創作最緊要係堅持。第一首可能唔完美，但每一首都會令你進步。繼續寫，繼續改，總有一日你會寫出感動人心嘅作品。」— 廣東歌·為你創作團隊</div>

  <h2>常見問題</h2>
  <p><strong>初學者應該由作曲開始定填詞開始？</strong> 建議先由作曲開始，因為旋律係歌曲嘅骨架。寫好旋律之後再填詞，會更容易控制聲調同節奏嘅配合。當然，如果你文字功底好，都可以先寫詞再搵人作曲。兩種方式冇絕對嘅好壞，最重要係搵到適合自己嘅創作流程。</p>
  <p><strong>屋企錄音需要注意咩？</strong> 最重要係環境噪音控制。揀一個安靜嘅房間，盡量減少回聲同反射。可以用吸音棉或者厚窗簾嚟改善錄音環境。錄音時同麥克風保持適當距離（約15-20厘米），用防噴罩減少爆破音。如果屋企環境太嘈，可以考慮喺深夜或者清晨錄音，嗰段時間通常最安靜。</p>
  <p><strong>獨立發行廣東歌有咩渠道？</strong> 而家有很多數碼發行平台可以選擇，例如 DistroKid、TuneCore 等，佢哋可以幫你將歌曲上架到 Spotify、Apple Music 等主流串流平台。另外，Bandcamp 同 SoundCloud 都係獨立音樂人嘅好選擇。發行之前記得準備好高質素嘅音檔（WAV格式）、封面圖片、同埋歌曲資料。</p>

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
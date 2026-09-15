#!/usr/bin/env python3
"""Daily SEO batch generator for mycantopop.hk — 2026-09-15"""
import os, json

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026年09月15日"
TODAY_ISO = "2026-09-15"

# 29 unique long-tail articles
ARTICLES = [
    {
        "slug": "cantopop-melody-writing-modal-mixture-borrowed-chord-emotional-shift-guide",
        "title": "廣東歌旋律創作調式混合借用和弦情感轉換指南：點樣用 modal mixture 制造意外情感轉折",
        "desc": "調式混合借用和弦旋律創作指南。教你用 modal mixture 同 borrowed chords 喺廣東歌中制造意外情感轉折同色彩變化。",
        "category": "作曲編曲",
        "intro": "調式混合（modal mixture）係一種將同主音但唔同調式嘅和弦借用過嚟嘅作曲技巧。例如喺大調歌曲中借用小調嘅和弦，可以瞬間制造出一種意外嘅情感轉折——由明亮突然轉為暗沉，或者由開朗突然帶上一絲憂傷。好多經典廣東歌都巧妙咁用咗呢種技巧，等聽眾喺唔經唔覺間感受到情緒嘅微妙變化。",
    },
    {
        "slug": "cantopop-arrangement-string-section-divisi-voicing-layering-guide",
        "title": "廣東歌編曲弦樂組分部排列聲部疊層指南：點樣用 string divisi 制造交響樂級層次感",
        "desc": "弦樂組分部排列聲部疊層編曲指南。教你用 string section divisi voicing 喺廣東歌中制造交響樂級別嘅層次感同厚度。",
        "category": "作曲編曲",
        "intro": "弦樂組分部（divisi）係指將弦樂聲部再細分為更多聲部嘅編曲技巧。喺廣東歌編曲中，用 divisi 可以令弦樂組由簡單嘅五聲部擴展到八聲部甚至更多，制造出交響樂級別嘅層次感同音響厚度。呢種技巧特別適合用喺抒情慢歌嘅高潮段落，或者電影主題曲嘅配樂中。",
    },
    {
        "slug": "cantopop-lyrics-writing-collective-memory-hong-kong-nostalgia-theme-guide",
        "title": "廣東歌詞創作集體回憶香港懷舊主題指南：點樣用集體記憶寫出引發共鳴嘅歌詞",
        "desc": "集體回憶香港懷舊主題歌詞創作指南。教你用集體記憶元素喺廣東歌詞中寫出引發香港人共鳴嘅懷舊情感。",
        "category": "填詞技巧",
        "intro": "集體回憶（collective memory）係一座城市最珍貴嘅情感資產。對於香港人嚟講，天星小輪、雪糕仔、荔園、屋邨走廊——呢啲都係觸發共同情感嘅符號。喺廣東歌詞中運用集體回憶元素，可以瞬間打開聽眾嘅情感開關，等佢哋覺得呢首歌「講緊我嘅故事」。呢篇文章會教你點樣將香港嘅集體回憶融入歌詞創作。",
    },
    {
        "slug": "cantopop-vocal-recording-large-diaphragm-condenser-vs-ribbon-tone-comparison-guide",
        "title": "廣東歌人聲錄音大振膜電容麥克風與鋁帶麥克風音色比較指南：點樣揀啱麥克風令錄音更出色",
        "desc": "大振膜電容麥克風與鋁帶麥克風音色比較錄音指南。教你比較 LDC 同 ribbon mic 嘅音色差異，為廣東歌人聲錄音揀啱麥克風。",
        "category": "錄音製作",
        "intro": "大振膜電容麥克風（LDC）同鋁帶麥克風（ribbon mic）係廣東歌人聲錄音中最常見嘅兩種選擇，但佢哋嘅音色特徵截然不同。LDC 音色明亮通透、細節豐富，適合錄製清晰度要求高嘅人聲；ribbon mic 音色溫暖柔和、高頻自然衰減，適合錄製有復古質感嘅人聲。呢篇文章會詳細比較兩者嘅差異。",
    },
    {
        "slug": "cantopop-mixing-sidechain-compression-vocal-ducking-automation-guide",
        "title": "廣東歌混音側鏈壓縮人聲避讓自動化指南：點樣用 sidechain compression 令人聲伴奏更清晰",
        "desc": "側鏈壓縮人聲避讓自動化混音指南。教你用 sidechain compression 喺廣東歌混音中令人聲同伴奏自動避讓，提升整體清晰度。",
        "category": "錄音製作",
        "intro": "側鏈壓縮（sidechain compression）係混音中一種好實用嘅動態控制技術。佢嘅原理係用一個信號去觸發另一個信號嘅壓縮——當人聲出現時，伴奏會自動降低少少音量，等人聲更加突出。喺廣東歌混音中，呢種技術可以令人聲同伴奏之間嘅關係更加清晰有序，唔需要手動調整音量自動化。",
    },
    {
        "slug": "cantopop-lyrics-writing-magical-realism-surreal-imagery-technique-guide",
        "title": "廣東歌詞創作魔幻現實主義超現實意象技巧指南：點樣用 magical realism 令歌詞更有想像力",
        "desc": "魔幻現實主義超現實意象歌詞創作技巧指南。教你用 magical realism 同 surreal imagery 喺廣東歌詞中制造超現實想像空間。",
        "category": "填詞技巧",
        "intro": "魔幻現實主義（magical realism）係將超現實元素融入日常生活場景嘅文學手法。喺廣東歌詞中運用呢種技巧，可以制造出一種「似真似假」嘅獨特氛圍——雨滴會倒流、時間會停滯、記憶會化成蝴蝶。呢種寫法可以打破現實嘅束縛，令歌詞更有想像力同藝術性，同時保持情感嘅真實感。",
    },
    {
        "slug": "cantopop-arrangement-brass-section-horn-stabs-staccato-accent-guide",
        "title": "廣東歌編曲銅管組短促斷奏重音節奏指南：點樣用 brass horn stabs 增加歌曲爆發力",
        "desc": "銅管組短促斷奏重音節奏編曲指南。教你用 brass section horn stabs 同 staccato accents 喺廣東歌中增加節奏爆發力。",
        "category": "作曲編曲",
        "intro": "銅管組（brass section）嘅短促斷奏（horn stabs）係一種非常有力嘅編曲元素。佢哋可以用短促而精準嘅音符為歌曲注入節奏爆發力，特別適合用喺廣東歌嘅副歌段落或者過門位。Trumpet、trombone、saxophone 嘅組合可以制造出由溫暖到犀利嘅多種音色質感。呢篇文章會教你點樣編寫 brass horn stabs。",
    },
    {
        "slug": "cantopop-mastering-multiband-compression-frequency-range-control-guide",
        "title": "廣東歌母帶處理多頻段壓縮頻率範圍控制指南：點樣用 multiband compression 精確控制整體音色",
        "desc": "多頻段壓縮頻率範圍控制母帶處理指南。教你用 multiband compression 喺廣東歌母帶處理中精確控制低中高頻嘅動態。",
        "category": "錄音製作",
        "intro": "多頻段壓縮（multiband compression）係母帶處理中最強大嘅工具之一。佢可以將音頻信號分為多個頻段（通常三至五個），分別對每個頻段施加獨立嘅壓縮控制。喺廣東歌母帶處理中，呢意味住你可以喺唔影響人聲清晰度嘅情況下控制低頻嘅厚度，或者喺唔影響低頻力度嘅情況下控制高頻嘅亮度。",
    },
    {
        "slug": "cantopop-lyrics-writing-zeugma-syllepsis-rhetorical-device-guide",
        "title": "廣東歌詞創作轭式搭配一詞多用修辭技巧指南：點樣用 zeugma syllepsis 令歌詞更巧妙精煉",
        "desc": "轭式搭配一詞多用修辭歌詞創作技巧指南。教你用 zeugma 同 syllepsis 喺廣東歌詞中以一個詞搭配多個對象，制造巧妙精煉效果。",
        "category": "填詞技巧",
        "intro": "轭式搭配（zeugma）同一詞多用（syllepsis）係兩種巧妙嘅修辭手法。Zeugma 係用一個動詞或形容詞同時搭配兩個或以上嘅名詞，但其中一個搭配係字面意義、另一個係比喻意義。例如「佢沖咗杯咖啡同埋沖咗個涼」——前者係字面，後者係比喻。喺廣東歌詞中用呢種手法可以令表達更加精煉同有趣。",
    },
    {
        "slug": "cantopop-song-distribution-tiktok-sound-pixel-promotion-strategy-guide",
        "title": "廣東歌發行TikTok音效片段像素推廣策略指南：點樣用 sound pixel 拓展病毒傳播",
        "desc": "TikTok音效片段像素推廣發行策略指南。教你用 TikTok sound pixel 同推廣策略將廣東歌制造病毒傳播效果。",
        "category": "發行推廣",
        "intro": "TikTok 已經成為全球最大嘅音樂發現平台之一，而 TikTok 嘅音效片段（sound）就係病毒傳播嘅核心單位。當一首廣東歌嘅某個片段被大量用戶用作背景音樂拍片，呢首歌就有機會爆紅。Sound pixel 推廣策略就係針對呢一點，刻意將歌曲中最有記憶點嘅幾秒片段推廣俾 TikTok 用戶。",
    },
    {
        "slug": "cantopop-melody-writing-retrograde-inversion-twelve-tone-technique-guide",
        "title": "廣東歌旋律創作逆行反轉十二音技巧指南：點樣用 retrograde inversion 令旋律更有變化",
        "desc": "逆行反轉十二音旋律創作技巧指南。教你用 retrograde 同 inversion 喺廣東歌旋律中制造變奏同主題發展。",
        "category": "作曲編曲",
        "intro": "逆行（retrograde）同反轉（inversion）係源自十二音技法嘅旋律變奏手法。逆行係將旋律由尾到頭倒轉播放，反轉係將旋律嘅音程方向顛倒（上行變下行）。雖然呢啲技巧聽落好學術，但其實喺廣東歌創作中都可以好自然咁運用——將副歌旋律逆行或反轉，可以制造出一種「似曾相識但又唔同」嘅效果。",
    },
    {
        "slug": "cantopop-arrangement-vibraphone-tremolo-ambient-pad-texture-guide",
        "title": "廣東歌編曲顫音鐵琴震音氛圍鋪底質感指南：點樣用 vibraphone tremolo 制造夢幻音場",
        "desc": "顫音鐵琴震音氛圍鋪底編曲指南。教你用 vibraphone tremolo 同 ambient pad 喺廣東歌中制造夢幻音場質感。",
        "category": "作曲編曲",
        "intro": "顫音鐵琴（vibraphone）嘅震音（tremolo）效果有一種獨特嘅夢幻質感。當顫音鐵琴嘅震音配合長音合成器（ambient pad）一齊使用，可以制造出一種飄浮、空靈嘅音場效果。喺廣東歌編曲中，呢種質感特別適合用喺歌曲嘅前奏、間奏或者結尾段落，為人聲出場前營造出夢幻氛圍。",
    },
    {
        "slug": "cantopop-vocal-recording-two-mic-spaced-pair-stereo-technique-guide",
        "title": "廣東歌人聲錄音雙麥克風間距立體聲技術指南：點樣用 spaced pair 錄出空間感人聲",
        "desc": "雙麥克風間距立體聲錄音技術指南。教你用 spaced pair stereo technique 為廣東歌人聲錄製自然空間感。",
        "category": "錄音製作",
        "intro": "雙麥克風間距立體聲（spaced pair stereo）係一種用兩支麥克風以一定距離分開擺放嚟錄製立體聲嘅技術。雖然通常用喺樂器收音，但喺廣東歌人聲錄音中都有獨特嘅應用——特別係當你想錄製一種有自然房間空間感嘅人聯時。兩支麥克風捕捉到嘅時間差同相位差可以制造出寬闊嘅立體聲影像。",
    },
    {
        "slug": "cantopop-lyrics-writing-polyphonic-narrative-multiple-perspective-guide",
        "title": "廣東歌詞創作複調敘事多視角技巧指南：點樣用 polyphonic narrative 令歌詞更有深度",
        "desc": "複調敘事多視角歌詞創作技巧指南。教你用 polyphonic narrative 喺廣東歌詞中同時呈現多個角色嘅視角同聲音。",
        "category": "填詞技巧",
        "intro": "複調敘事（polyphonic narrative）係一種喺同一首作品中同時呈現多個角色視角同聲音嘅敘事技巧。喺廣東歌詞中運用呢種手法，可以令一首歌同時講述兩個或者多個人嘅故事，每個角色有自己嘅聲音同立場。呢種寫法可以令歌詞更有層次同深度，等聽眾從多個角度理解故事。",
    },
    {
        "slug": "cantopop-mixing-parallel-processing-dry-wet-blend-technique-guide",
        "title": "廣東歌混音並聯處理乾濕混合技巧指南：點樣用 parallel processing 保持原始音色又增加效果",
        "desc": "並聯處理乾濕混合混音技巧指南。教你用 parallel processing 喺廣東歌混音中保持原始音色同時增加效果處理。",
        "category": "錄音製作",
        "intro": "並聯處理（parallel processing）係混音中一種保持原始信號不變、同時將副本送去效果處理再混合嘅技術。最常見嘅例子係並聯壓縮（parallel compression）——將原始嘅鼓組信號同一條重度壓縮嘅副本混合，可以同時擁有原始嘅動態同壓縮後嘅厚度。喺廣東歌混音中，呢種技術可以應用喺人聲、鼓組、貝斯等各個軌道。",
    },
    {
        "slug": "cantopop-song-distribution-submission-playlist-editor-pitching-guide",
        "title": "廣東歌發行播放清單編輯器推介投稿指南：點樣用 playlist pitching 爭取官方推介",
        "desc": "播放清單編輯器推介投稿發行指南。教你用 playlist pitching 策略將廣東歌推介俾 Spotify Apple Music 編輯器。",
        "category": "發行推廣",
        "intro": "播放清單推介（playlist pitching）係數碼音樂發行中最有效嘅推廣策略之一。Spotify、Apple Music 等平台都有編輯器策劃嘅官方播放清單，如果你嘅廣東歌可以入選，可以帶嚟大量嘅新聽眾。呢篇文章會教你點樣準備推介材料、點樣揀啱嘅播放清單、同埋點樣寫一封令人印象深刻嘅推介信。",
    },
    {
        "slug": "cantopop-melody-writing-passing-tone-neighbor-tone-ornamentation-guide",
        "title": "廣東歌旋律創作經過音鄰音裝飾音技巧指南：點樣用 passing tone 令旋律更流暢豐富",
        "desc": "經過音鄰音裝飾音旋律創作技巧指南。教你用 passing tone 同 neighbor tone 喺廣東歌旋律中加入裝飾音符。",
        "category": "作曲編曲",
        "intro": "經過音（passing tone）同鄰音（neighbor tone）係旋律創作中最基本嘅裝飾音技巧。經過音係喺兩個和弦音之間插入嘅過渡音符，可以令旋律線更加流暢連貫。鄰音係喺和弦音上方或下方一個音階位置加入嘅裝飾音符，可以為旋律增添細微嘅起伏感。喺廣東歌旋律中巧妙運用呢啲裝飾音，可以令簡單嘅旋律變得更加豐富有趣。",
    },
    {
        "slug": "cantopop-arrangement-orchestral-hit-stab-cinematic-impact-guide",
        "title": "廣東歌編曲管弦樂撞擊重音電影感衝擊指南：點樣用 orchestral hit 制造戲劇性爆發",
        "desc": "管弦樂撞擊重音電影感衝擊編曲指南。教你用 orchestral hit 同 stab 喺廣東歌中制造戲劇性爆發效果。",
        "category": "作曲編曲",
        "intro": "管弦樂撞擊（orchestral hit）係一種將整個管弦樂團同時演奏一個強和弦嘅音效，能夠制造出極具衝擊力嘅戲劇性效果。喺廣東歌編曲中，orchestral hit 可以用喺副歌嘅第一拍、或者歌曲嘅情緒轉折點，制造出一種「轟」一聲嘅爆發感。呢種技巧喺八十年代嘅廣東歌中特別流行，而家又開始復古返嚟。",
    },
    {
        "slug": "cantopop-lyrics-writing-apostrophe-direct-address-rhetorical-device-guide",
        "title": "廣東歌詞創作呼告直接對象修辭技巧指南：點樣用 apostrophe 令歌詞更有感染力",
        "desc": "呼告直接對象修辭歌詞創作技巧指南。教你用 apostrophe direct address 喺廣東歌詞中直接呼喚對象增加感染力。",
        "category": "填詞技巧",
        "intro": "呼告（apostrophe）係一種直接向唔在場嘅人、物或者抽象概念發出呼喚嘅修辭手法。例如「啊，時間你點解咁殘忍」、「風啊請你帶我走」——呢種直接呼喚能夠瞬間提升歌詞嘅情感強度同感染力。喺廣東歌詞中運用呼告技巧，可以制造出一種迫切嘅對話感，等聽眾感受到歌手內心嘅激動。",
    },
    {
        "slug": "cantopop-vocal-mixing-de-essing-frequency-selective-compression-guide",
        "title": "廣東歌人聲混音齒音消除頻率選擇性壓縮指南：點樣用 de-essing 令人聲更順耳",
        "desc": "齒音消除頻率選擇性壓縮人聲混音指南。教你用 de-essing 同 frequency selective compression 消除廣東歌人聲齒音。",
        "category": "錄音製作",
        "intro": "齒音（sibilance）係人聲錄音中最常見嘅問題之一，特別係粵語中有大量嘅「s」「sz」「ch」等擦音聲母。過強嘅齒音會令人聲聽起嚟刺耳唔舒服。De-essing 就係一種專門用嚟消除齒音嘅頻率選擇性壓縮技術——佢只會喺齒音頻率（通常 5-10kHz）出現時先至觸發壓縮，唔會影響其他頻段嘅人聲。",
    },
    {
        "slug": "cantopop-song-distribution-youtube-music-video-vevo-channel-monetization-guide",
        "title": "廣東歌發行YouTube音樂影片Vevo頻道營利指南：點樣用 MV 頻道增加廣告收入",
        "desc": "YouTube音樂影片Vevo頻道營利發行指南。教你用 YouTube MV 同 Vevo channel 為廣東歌增加廣告收入同曝光率。",
        "category": "發行推廣",
        "intro": "YouTube 仍然係全球最大嘅音樂影片平台，而 Vevo 頻道就係專為音樂人提供嘅高級別營利渠道。對於獨立廣東歌音樂人嚟講，YouTube MV 唔單止係一個展示作品嘅平台，更係一個重要嘅收入來源。透過 YouTube 廣告分潤、會員訂閱、超級留言等功能，你可以將音樂影片轉化為持續嘅被動收入。",
    },
    {
        "slug": "cantopop-arrangement-synth-pad-arp-layering-cinematic-atmosphere-guide",
        "title": "廣東歌編曲合成器鋪底琶音疊層電影氛圍指南：點樣用 synth pad arp 制造大片質感",
        "desc": "合成器鋪底琶音疊層電影氛圍編曲指南。教你用 synth pad 同 arpeggiator 疊層喺廣東歌中制造電影大片質感。",
        "category": "作曲編曲",
        "intro": "合成器鋪底（synth pad）同琶音器（arpeggiator）嘅疊層係現代廣東歌編曲中制造電影氛圍嘅重要技巧。Synth pad 提供持續嘅和聲背景，而 arpeggiator 則不斷循環演奏和弦內音，兩者疊加可以制造出一種宏大、流動、有如電影配樂般嘅音場效果。呢種技巧特別適合用喺有電子元素嘅廣東歌中。",
    },
    {
        "slug": "cantopop-lyrics-writing-chiasmus-antimetabole-symmetric-rhetoric-guide",
        "title": "廣東歌詞創作交錯排列對稱修辭技巧指南：點樣用 chiasmus 令歌詞更有結構美感",
        "desc": "交錯排列對稱修辭歌詞創作技巧指南。教你用 chiasmus 同 antimetabole 喺廣東歌詞中制造對稱結構美感。",
        "category": "填詞技巧",
        "intro": "交錯排列（chiasmus）同一種反覆（antimetabole）係兩種對稱結構嘅修辭手法。Chiasmus 係將詞語順序顛倒重複，例如「你為咗音樂活，音樂為咗你活」；antimetabole 係用完全相同嘅詞語但顛倒順序，例如「愛嘅人傷害你，你傷害愛嘅人」。喺廣東歌詞中運用呢種對稱結構，可以制造出一種迴旋往復嘅美感。",
    },
    {
        "slug": "cantopop-vocal-recording-mic-preamp-class-a-vs-class-ab-tone-guide",
        "title": "廣東歌人聲錄音麥克風前級A類AB類音色比較指南：點樣揀啱前級令人聲更有特色",
        "desc": "麥克風前級A類AB類音色比較錄音指南。教你比較 Class A 同 Class AB preamp 嘅音色差異，為廣東歌人聲揀啱前級。",
        "category": "錄音製作",
        "intro": "麥克風前級（mic preamp）嘅電路設計對人聲音色有深遠影響。A類（Class A）前級嘅特點係音色溫暖、諧波豐富、失真特性柔和，特別適合錄製有復古質感嘅人聲。AB類（Class AB）前級嘅特點係音色乾淨、線性好、動態範圍大，適合錄製需要高清晰度嘅人聲。呢兩種前級各有優勢，選擇邊種取決於你想要嘅人聲風格。",
    },
    {
        "slug": "cantopop-mixing-mid-side-eq-stereo-width-frequency-control-guide",
        "title": "廣東歌混音中側均衡立體聲寬度頻率控制指南：點樣用 M/S EQ 精確調整空間感",
        "desc": "中側均衡立體聲寬度頻率控制混音指南。教你用 Mid-Side EQ 喺廣東歌混音中精確調整立體聲寬度同頻率。",
        "category": "錄音製作",
        "intro": "Mid-Side EQ（中側均衡器）係一種可以分別對中央信號同兩側信號進行唔同頻率調整嘅混音工具。喺廣東歌混音中，M/S EQ 可以幫你做到傳統均衡器做不到嘅事情——例如只增強兩側嘅高頻令伴奏更寬闊，同時保持中央人聲嘅清晰度不受影響。呢種精確嘅空間控制能力令 M/S EQ 成為現代混音嘅必備工具。",
    },
    {
        "slug": "cantopop-song-distribution-apple-music-lossless-audio-quality-setting-guide",
        "title": "廣東歌發行Apple Music無損音質設定指南：點樣為串流平台提供最佳音質檔案",
        "desc": "Apple Music無損音質設定發行指南。教你為廣東歌準備無損音質檔案並設定 Apple Music 同各串流平台嘅最佳參數。",
        "category": "發行推廣",
        "intro": "Apple Music 支援無損音質（Lossless Audio）播放，包括 ALAC 格式嘅 24-bit/192kHz 高解析音頻。對於廣東歌音樂人嚟講，提供無損音質版本唔單止可以令聽眾享受更好嘅音質，仲可以展示你對作品質素嘅重視。呢篇文章會教你點樣為 Apple Music 同其他串流平台準備最佳音質嘅音頻檔案。",
    },
    {
        "slug": "cantopop-melody-writing-sequence-ostinato-pattern-development-guide",
        "title": "廣東歌旋律創作序列固定音型發展技巧指南：點樣用 sequence ostinato 令旋律更有推進力",
        "desc": "序列固定音型發展旋律創作技巧指南。教你用 sequence 同 ostinato pattern 喺廣東歌中制造旋律推進力同記憶點。",
        "category": "作曲編曲",
        "intro": "序列（sequence）同固定音型（ostinato）係兩種令旋律有推進力嘅作曲技巧。Sequence 係將一個旋律片段喺唔同音高上重複，制造出一種層層遞進嘅效果。Ostinato 係一個不斷重複嘅短小音型，可以作為旋律嘅背景或者動力來源。喺廣東歌創作中，呢兩種技巧可以好有效咁制造旋律嘅記憶點同推進感。",
    },
    {
        "slug": "cantopop-arrangement-percussion-layering-acoustic-electronic-hybrid-guide",
        "title": "廣東歌編曲打擊樂疊層真實電子混合指南：點樣用 acoustic electronic hybrid 制造豐富節奏",
        "desc": "打擊樂疊層真實電子混合編曲指南。教你用 acoustic 同 electronic percussion 疊層喺廣東歌中制造豐富節奏質感。",
        "category": "作曲編曲",
        "intro": "現代廣東歌嘅鼓組編排越嚟越多採用真實樂器同電子音色混合嘅方式。將真實鼓組（acoustic drums）同電子打擊樂（electronic percussion）疊層使用，可以同時擁有真實鼓聲嘅自然動態同電子音色嘅精準衝擊力。例如用真實 kick drum 配合電子 808 sub-bass，或者用真實 snare 配合電子 clap，可以制造出既有機感又有現代感嘅節奏質感。",
    },
    {
        "slug": "cantopop-lyrics-writing-anadiplosis-chain-repetition-rhetorical-guide",
        "title": "廣東歌詞創作頂真鏈鎖重複修辭技巧指南：點樣用 anadiplosis 令歌詞有連鎖推進感",
        "desc": "頂真鏈鎖重複修辭歌詞創作技巧指南。教你用 anadiplosis chain repetition 喺廣東歌詞中制造連鎖推進嘅節奏感。",
        "category": "填詞技巧",
        "intro": "頂真（anadiplosis）係一種將上一句嘅結尾詞語作為下一句嘅開頭嘅修辭手法。例如「雨落下落個不停／不停嘅思念／思念化作歌／歌送俾遠方嘅你」——每句嘅結尾都成為下一句嘅開頭，形成一條連鎖鏈。喺廣東歌詞中運用頂真技巧，可以制造出一種連鎖推進嘅節奏感同邏輯遞進感，等歌詞有一氣呵成嘅效果。",
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
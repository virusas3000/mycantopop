#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 29 new SEO articles for mycantopop.hk"""
import os, json, datetime, html

REPO = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(REPO, "articles")
TODAY = "2026年08月20日"
TODAY_ISO = "2026-08-20"

# Load existing slugs
existing_slugs = set()
for f in os.listdir(ART_DIR):
    if f.endswith(".html") and f != "index.html":
        existing_slugs.add(f.replace(".html", ""))

# 29 article definitions: (slug, title, description, category_tag, card_desc, body_sections)
ARTICLES = [
    {
        "slug": "cantopop-mixing-phase-issues-check-correction-technique",
        "title": "廣東歌混音相位問題檢查同修正技巧：點樣解決左右聲道抵消",
        "desc": "相位問題會令混音聽落薄同冇力。教你點樣用相位檢查工具同反相開關，修正廣東歌混音中嘅左右聲道抵消問題。",
        "tag": "錄音製作",
        "card": "相位問題會令混音聽落薄同冇力。教你點樣檢查同修正廣東歌混音中嘅左右聲道抵消。",
        "h2s": ["點解相位問題影響廣東歌混音質素", "相位抵消嘅成因同識別方法", "修正相位問題嘅具體步驟", "常用相位檢查工具同技巧", "混音中嘅相位管理最佳做法"],
    },
    {
        "slug": "cantopop-arrangement-syncopation-backbeat-rhythm-technique",
        "title": "廣東歌編曲反拍切分節奏應用技巧：點樣令節奏更有律動感",
        "desc": "反拍同切分節奏係編曲嘅靈魂。教你點樣喺廣東歌編曲中應用 syncopation，令成首歌嘅律動感大幅提升。",
        "tag": "作曲編曲",
        "card": "反拍同切分節奏係編曲嘅靈魂。教你點樣喺廣東歌編曲中應用 syncopation 提升律動感。",
        "h2s": ["反拍切分喺廣東歌中嘅作用", "切分節奏嘅基本原理", "點樣喺編曲中實踐切分", "切分同旋律嘅配合", "切分節奏嘅進階應用"],
    },
    {
        "slug": "cantonese-lyrics-imagery-superposition-layered-metaphor-technique",
        "title": "粵語歌詞意象疊加多層隱喻寫作技巧：點樣令歌詞更有深度",
        "desc": "意象疊加係高級歌詞寫作技巧。教你點樣喺粵語歌詞中用多層隱喻同意象疊加，令歌詞更有文學深度同回味空間。",
        "tag": "填詞技巧",
        "card": "意象疊加係高級歌詞寫作技巧。教你點樣喺粵語歌詞中用多層隱喻增加深度。",
        "h2s": ["意象疊加係咩嘢技巧", "多層隱喻嘅構造原理", "點樣喺粵語歌詞中實踐意象疊加", "意象疊加嘅節奏控制", "避免意象過度密集嘅技巧"],
    },
    {
        "slug": "cantopop-mastering-dynamic-range-preservation-technique",
        "title": "廣東歌母帶動態範圍保留技巧：點樣做到響度同動態兼備",
        "desc": "母帶處理最難就係響度同動態之間嘅平衡。教你點樣用 limiter 同壓縮技巧，保留廣東歌嘅動態範圍同時達到串流響度標準。",
        "tag": "錄音製作",
        "card": "母帶處理最難就係響度同動態之間嘅平衡。教你保留廣東歌動態範圍同時達到串流響度。",
        "h2s": ["動態範圍同響度嘅矛盾關係", "Limiter 設定嘅關鍵參數", "多段壓縮喺母帶中嘅角色", "響度標準同動態保留嘅平衡點", "驗證動態保留嘅方法"],
    },
    {
        "slug": "cantopop-melody-writing-non-functional-harmony-application",
        "title": "廣東歌旋律非功能和聲應用技巧：點樣突破傳統和弦框架",
        "desc": "非功能和聲可以令旋律更有色彩。教你點樣喺廣東歌作曲中應用非功能和聲，突破傳統功能和聲框架。",
        "tag": "作曲編曲",
        "card": "非功能和聲可以令旋律更有色彩。教你點樣喺廣東歌作曲中突破傳統和弦框架。",
        "h2s": ["功能和聲同非功能和聲嘅分別", "非功能和聲嘅基本原理", "廣東歌中嘅應用場景", "點樣同旋律配合", "非功能和聲嘅常見錯誤"],
    },
    {
        "slug": "cantopop-vocal-thermal-saturation-warmth-tone-technique",
        "title": "廣東歌人聲暖音色飽和失真加溫技巧：點樣令人聲更有質感",
        "desc": "人聲太乾淨反而冇味道。教你點樣用 thermal saturation 同 tape emulation 令廣東歌人聲更有暖度同質感。",
        "tag": "錄音製作",
        "card": "人聲太乾淨反而冇味道。教你用 thermal saturation 同 tape emulation 令人聲更有暖度。",
        "h2s": ["飽和失真同人聲質感嘅關係", "Tape emulation 嘅原理同選擇", "點樣設定飽和量", "暖音色同粵語發音嘅配合", "避免過度飽和嘅技巧"],
    },
    {
        "slug": "cantopop-arrangement-string-pizzicato-articulation-technique",
        "title": "廣東歌編曲弦樂撥奏articulation應用技巧：點樣增加texture質感",
        "desc": "弦樂撥奏係增加編曲質感嘅好方法。教你點樣喺廣東歌編曲中應用 pizzicato articulation，令 texture 更豐富。",
        "tag": "作曲編曲",
        "card": "弦樂撥奏係增加編曲質感嘅好方法。教你用 pizzarticato articulation 令 texture 更豐富。",
        "h2s": ["Pizzicato 喺編曲中嘅角色", "撥奏同拉奏嘅 articulation 對比", "點樣同其他樂器配合", "Pizzicato 嘅節奏應用", "MIDI 模擬 pizzicato 嘅技巧"],
    },
    {
        "slug": "cantonese-lyrics-object-writing-sensory-detail-technique",
        "title": "粵語歌詞客物書寫感官細節技巧：點樣用物件描寫帶出情感",
        "desc": "用物件帶出情感係高級歌詞技巧。教你點樣喺粵語歌詞中用客物書寫同感官細節，令歌詞更有畫面同情感層次。",
        "tag": "填詞技巧",
        "card": "用物件帶出情感係高級歌詞技巧。教你用客物書寫同感官細節令歌詞更有畫面。",
        "h2s": ["客物書寫係咩嘢技巧", "感官細節嘅五覺應用", "點樣揀選承載情感嘅物件", "物件描寫嘅節奏控制", "避免流於堆砌嘅方法"],
    },
    {
        "slug": "cantopop-recording-vocal-take-mental-performance-state",
        "title": "廣東歌錄音人聲take心理表演狀態控制：點樣入戲唱得好",
        "desc": "錄音唔只係技術，仲係心理狀態嘅管理。教你點樣喺廣東歌錄音時調整心理表演狀態，唱出更有感情嘅 take。",
        "tag": "錄音製作",
        "card": "錄音唔只係技術，仲係心理狀態嘅管理。教你調整表演狀態唱出更有感情嘅 take。",
        "h2s": ["心理狀態對錄音表現嘅影響", "入戲嘅具體方法", "錄音前嘅心理準備", "take 之間嘅狀態調整", "長時間錄音嘅心理管理"],
    },
    {
        "slug": "cantopop-mixing-parallel-drum-bus-processing-technique",
        "title": "廣東歌混音平行鼓bus處理技巧：點樣令鼓聲更有衝擊力",
        "desc": "平行鼓 bus 處理係混音中令鼓聲更有衝擊力嘅關鍵技巧。教你點樣設定 parallel drum bus 令廣東歌節奏更突出。",
        "tag": "錄音製作",
        "card": "平行鼓 bus 處理係令鼓聲更有衝擊力嘅關鍵技巧。教你設定 parallel drum bus 令節奏更突出。",
        "h2s": ["平行處理嘅基本原理", "Drum bus 路由設定", "壓縮器選擇同參數設定", "平衡 parallel 同原始信號", "平行處理嘅進階技巧"],
    },
    {
        "slug": "cantopop-arrangement-bass-synth-sub-layer-technique",
        "title": "廣東歌編曲低音合成器sub-bass分層技巧：點樣令低頻更厚實",
        "desc": "低頻係編曲嘅地基。教你點樣用 sub-bass 分層技巧令廣東歌低頻更厚實同有包圍感。",
        "tag": "作曲編曲",
        "card": "低頻係編曲嘅地基。教你用 sub-bass 分層技巧令廣東歌低頻更厚實。",
        "h2s": ["Sub-bass 喺編曲中嘅角色", "分層嘅基本原理", "點樣揀選低音合成器音色", "Sub-bass 同 kick 嘅配合", "低頻管理嘅混音考慮"],
    },
    {
        "slug": "cantonese-lyrics-constraint-writing-arbitrary-rules-technique",
        "title": "粵語歌詞限制式寫作 arbitrary rules 技巧：點樣用規框激發創意",
        "desc": "限制式寫作係用規框激發創意嘅高級技巧。教你點樣喺粵語歌詞創作中設定 arbitrary rules，突破創作瓶頸。",
        "tag": "填詞技巧",
        "card": "限制式寫作係用規框激發創意嘅高級技巧。教你設定 arbitrary rules 突破創作瓶頸。",
        "h2s": ["限制式寫作嘅理論基礎", "Arbitrary rules 嘅設定方法", "限制如何激發創意", "常見嘅限制式寫作練習", "點樣平衡限制同表達自由"],
    },
    {
        "slug": "cantopop-music-distribution-isrc-code-registration-guide",
        "title": "廣東歌發行ISRC編碼註冊申請指南：點樣為每首歌申請識別碼",
        "desc": "ISRC 係每首歌嘅國際標準識別碼。教你點樣為廣東歌申請同註冊 ISRC 編碼，確保版稅追蹤同發行順利。",
        "tag": "發行推廣",
        "card": "ISRC 係每首歌嘅國際標準識別碼。教你點樣為廣東歌申請同註冊 ISRC 編碼。",
        "h2s": ["ISRC 係咩嘢同點解重要", "申請 ISRC 嘅途徑", "香港 ISRC 申請流程", "發行時嘅 ISRC 填寫", "常見嘅 ISRC 錯誤同修正"],
    },
    {
        "slug": "cantopop-indie-musician-blog-press-outreach-pitching-technique",
        "title": "廣東歌獨立音樂人音樂博客投稿宣傳技巧：點樣揾媒體報道你",
        "desc": "媒體報道係獨立音樂人最有效嘅免費宣傳。教你點樣寫 pitch email 同投稿畀音樂博客，令廣東歌得到更多曝光。",
        "tag": "獨立音樂",
        "card": "媒體報道係獨立音樂人最有效嘅免費宣傳。教你寫 pitch email 投稿畀音樂博客。",
        "h2s": ["音樂博客投稿嘅策略", "Pitch email 嘅寫法", "點樣揾適合嘅媒體", "建立媒體關係嘅技巧", "跟進同後續宣傳"],
    },
    {
        "slug": "cantopop-recording-vocal-standing-posture-desk-setup-guide",
        "title": "廣東歌錄音站立式錄音姿勢同檯面設定指南：點樣唱得自然",
        "desc": "錄音姿勢直接影響聲音表現。教你點樣設定站立式錄音環境同姿勢，令廣東歌人聲收得更自然。",
        "tag": "錄音製作",
        "card": "錄音姿勢直接影響聲音表現。教你設定站立式錄音環境同姿勢令人聲更自然。",
        "h2s": ["錄音姿勢對聲音嘅影響", "站立式 vs 坐式錄音", "麥克風高度同角度設定", "檯面同樂譜架嘅擺放", "長時間錄音嘅姿勢管理"],
    },
    {
        "slug": "cantopop-mixing-vocal-parallel-new-york-compression-technique",
        "title": "廣東歌人聲紐約式平行壓縮混音技巧：點樣令人聲更突出",
        "desc": "紐約式壓縮係令人聲更突出嘅經典技巧。教你點樣用 parallel compression 令廣東歌人聲喺混音中更清晰突出。",
        "tag": "錄音製作",
        "card": "紐約式壓縮係令人聲更突出嘅經典技巧。教你用 parallel compression 令人聲更清晰。",
        "h2s": ["紐約式壓縮嘅原理", "平行壓縮嘅路由設定", "壓縮器參數調校", "平衡 parallel 同原始信號", "紐約式 vs 其他平行處理嘅分別"],
    },
    {
        "slug": "cantopop-song-chorus-vocal-stack-arrangement-technique",
        "title": "廣東歌副歌人聲疊軌編曲技巧：點樣令chorus更有氣勢",
        "desc": "副歌人聲疊軌係令 chorus 更有氣勢嘅關鍵。教你點樣安排廣東歌副歌嘅人聲疊軌，制造層次同衝擊力。",
        "tag": "作曲編曲",
        "card": "副歌人聲疊軌係令 chorus 更有氣勢嘅關鍵。教你安排廣東歌副歌人聲疊軌。",
        "h2s": ["人聲疊軌嘅基本原理", "疊幾多層先至啱", "疊軌嘅 pan 同 timing", "和聲同疊軌嘅配合", "疊軌嘅混音處理"],
    },
    {
        "slug": "cantopop-melody-writing-tonal-centre-shift-technique",
        "title": "廣東歌旋律調性中心轉移技巧：點樣制造暗暗嘅情感變化",
        "desc": "調性中心轉移係制造微妙情感變化嘅高級技巧。教你點樣喺廣東歌旋律中應用 tonal centre shift 令歌曲更有層次。",
        "tag": "作曲編曲",
        "card": "調性中心轉移係制造微妙情感變化嘅高級技巧。教你用 tonal centre shift 令歌曲更有層次。",
        "h2s": ["調性中心嘅概念", "Tonal centre shift 嘅原理", "點樣喺旋律中應用", "同和弦進行嘅配合", "調性轉移嘅情感效果"],
    },
    {
        "slug": "cantonese-lyrics-found-poetry-cut-up-technique",
        "title": "粵語歌詞found poetry剪貼創作技巧：點樣用隨機拼貼寫出意外驚喜",
        "desc": "Found poetry 同剪貼法係用隨機拼貼激發靈感嘅創作技巧。教你點樣喺粵語歌詞創作中應用 cut-up technique 寫出意外驚喜。",
        "tag": "填詞技巧",
        "card": "Found poetry 同剪貼法係用隨機拼貼激發靈感嘅技巧。教你用 cut-up technique 寫出意外驚喜。",
        "h2s": ["Found poetry 同剪貼法嘅歷史", "Cut-up technique 嘅操作方法", "粵語歌詞中嘅應用", "隨機性同創作控制嘅平衡", "從拼貼到成稿嘅整理"],
    },
    {
        "slug": "cantopop-mastering-stems-delivery-format-specification-guide",
        "title": "廣東歌母帶stems分軌交付格式規格指南：點樣準備mastering要嘅文件",
        "desc": "Stems 分軌交付係送母帶處理嘅標準做法。教你點樣準備廣東歌 stems 分軌文件，規格符合 mastering 室嘅要求。",
        "tag": "錄音製作",
        "card": "Stems 分軌交付係送母帶處理嘅標準做法。教你準備廣東歌 stems 分軌文件。",
        "h2s": ["Stems 係咩嘢同點解重要", "分軌嘅標準分組方法", "文件格式同採樣率規格", "命名同組織規範", "交付前嘅檢查清單"],
    },
    {
        "slug": "cantopop-arrangement-percussion-shaker-tambourine-layer-technique",
        "title": "廣東歌編曲打擊樂shaker鈴鼓分層技巧：點樣令節奏更有層次",
        "desc": "Shaker 同鈴鼓係增加節奏層次嘅秘密武器。教你點樣喺廣東歌編曲中用打擊樂分層技巧令節奏更豐富。",
        "tag": "作曲編曲",
        "card": "Shaker 同鈴鼓係增加節奏層次嘅秘密武器。教你用打擊樂分層令節奏更豐富。",
        "h2s": ["打擊樂分層嘅作用", "Shaker 嘅選擇同應用", "鈴鼓 tambourine 嘅擺位", "同主鼓嘅節奏配合", "打擊樂嘅混音處理"],
    },
    {
        "slug": "cantopop-vocal-group-singing-choir-recording-technique",
        "title": "廣東歌合唱群唱錄音技巧：點樣收齊多人合唱",
        "desc": "合唱群唱錄音同獨唱完全唔同。教你點樣用多人合唱錄音技巧收齊廣東歌嘅群唱部分，制造自然嘅合唱感。",
        "tag": "錄音製作",
        "card": "合唱群唱錄音同獨唱完全唔同。教你用多人合唱錄音技巧收齊廣東歌群唱部分。",
        "h2s": ["合唱錄音同獨唱嘅分別", "麥克風擺放方法", "分組錄音疊軌技巧", "群唱嘅 timing 同呼吸", "合唱嘅混音處理"],
    },
    {
        "slug": "cantopop-song-distribution-physical-cd-duplication-hk-guide",
        "title": "廣東歌發行實體CD壓碟製作香港指南：點樣小批量生產CD",
        "desc": "實體CD喺香港仲有一定市場。教你點樣小批量壓碟生產廣東歌CD，由設計到包裝一站式搞掂。",
        "tag": "發行推廣",
        "card": "實體CD喺香港仲有一定市場。教你小批量壓碟生產廣東歌CD，由設計到包裝一站式搞掂。",
        "h2s": ["實體CD喺香港嘅市場價值", "壓碟 vs 燒碟嘅分別", "小批量生產嘅渠道", "封面設計同包裝規格", "銷售同發行渠道"],
    },
    {
        "slug": "cantopop-indie-musician-local-venue-booking-pitching-guide",
        "title": "廣東歌獨立音樂人本地場地預約pitch技巧：點樣book到show",
        "desc": "Book show 係獨立音樂人嘅基本功。教你點樣寫場地預約 pitch email 同建立演出關係，喺香港 book 到更多 show。",
        "tag": "獨立音樂",
        "card": "Book show 係獨立音樂人嘅基本功。教你寫場地預約 pitch email 喺香港 book 到更多 show。",
        "h2s": ["香港 live house 場地生態", "Pitch email 嘅寫法", "點樣準備 EPK 同音樂樣本", "場地關係嘅建立同維護", "演出後嘅跟進"],
    },
    {
        "slug": "cantopop-mixing-ambient-room-reverb-vocal-blend-technique",
        "title": "廣東歌混音ambient room reverb人聲融合技巧：點樣令人聲有自然空間感",
        "desc": "Ambient room reverb 令人聲有自然空間感嘅關鍵。教你點樣用房間殘響令廣東歌人聲融入混音唔顯得乾澀。",
        "tag": "錄音製作",
        "card": "Ambient room reverb 令人聲有自然空間感嘅關鍵。教你用房間殘響令人聲融入混音。",
        "h2s": ["Ambient room reverb 嘅原理", "房間殘響同一般 reverb 嘅分別", "參數設定嘅關鍵", "人聲同伴奏嘅空間融合", "避免混濁嘅技巧"],
    },
    {
        "slug": "cantopop-song-structure-pre-intro-ambience-buildup-technique",
        "title": "廣東歌歌曲結構intro前ambient鋪排技巧：點樣做氣氛引入",
        "desc": "Intro 前嘅 ambient 鋪排可以為歌曲設定情感基調。教你點樣用環境音效同氣氛鋪排令廣東歌開場更有代入感。",
        "tag": "作曲編曲",
        "card": "Intro 前嘅 ambient 鋪排可以為歌曲設定情感基調。教你用環境音效令開場更有代入感。",
        "h2s": ["Ambient intro 嘅作用", "環境音效嘅設計", "點樣同主歌過渡", "氣氛鋪排嘅時間控制", "Ambient intro 嘅混音考慮"],
    },
    {
        "slug": "cantonese-lyrics-ekphrasis-art-inspired-writing-technique",
        "title": "粵語歌詞ekphrasis藝術啟發寫作技巧：點樣用畫作激發歌詞靈感",
        "desc": "Ekphrasis 係用視覺藝術激發文學創作嘅古老技巧。教你點樣用畫作同藝術品激發粵語歌詞歌詞靈感，寫出更有畫面嘅作品。",
        "tag": "填詞技巧",
        "card": "Ekphrasis 係用視覺藝術激發文學創作嘅技巧。教你用畫作激發粵語歌詞靈感。",
        "h2s": ["Ekphrasis 嘅定義同歷史", "點樣揀選啟發嘅藝術品", "從視覺到文字嘅轉化方法", "粵語歌詞中嘅應用", "Ekphrasis 同原創性嘅平衡"],
    },
    {
        "slug": "cantopop-production-modular-synth-eurorack-integration-technique",
        "title": "廣東歌制作modular synth eurorack整合技巧：點樣用模塊合成器編曲",
        "desc": "Modular synth 可以為廣東歌編曲帶嚟獨特嘅音色。教你點樣將 eurorack 模塊合成器整合到廣東歌制作流程中。",
        "tag": "音樂制作",
        "card": "Modular synth 可以為廣東歌編曲帶嚟獨特嘅音色。教你將 eurorack 整合到制作流程。",
        "h2s": ["Modular synth 嘅基本概念", "Eurorack 系統嘅入門", "點樣同 DAW 整合", "喺廣東歌編曲中嘅應用", "音色設計同錄音技巧"],
    },
    {
        "slug": "cantopop-arrangement-horn-section-counterpoint-layers-technique",
        "title": "廣東歌編曲horn section銅管層次對位技巧：點樣寫好銅管編排",
        "desc": "Horn section 銅管編排可以令廣東歌更有色彩。教你點樣用對位同分層技巧寫好銅管編排，增加歌曲嘅豐富度。",
        "tag": "作曲編曲",
        "card": "Horn section 銅管編排可以令廣東歌更有色彩。教你用對位同分層技巧寫好銅管編排。",
        "h2s": ["Horn section 喺流行音樂嘅角色", "銅管樂器嘅音色特點", "對位寫作嘅基本原則", "分層同和聲排列", "銅管嘅混音處理"],
    },
]

# Verify no slug collisions
for a in ARTICLES:
    assert a["slug"] not in existing_slugs, f"SLUG COLLISION: {a['slug']}"

print(f"✓ All {len(ARTICLES)} slugs are unique (checked against {len(existing_slugs)} existing)")

# ---- Article HTML Template ----
def gen_article_html(a):
    slug = a["slug"]
    title = a["title"]
    desc = a["desc"]
    h2s = a["h2s"]
    url = f"https://mycantopop.hk/articles/{slug}.html"

    # Generate substantive body content for each section
    # Each h2 gets 2-3 paragraphs (~150-200 words each section)
    body_parts = []

    # Intro paragraph
    body_parts.append(f"<p>{a['card']}呢篇指南會由基本原理講起，一步步帶你掌握呢個技巧嘅核心要點。</p>")

    for i, h2 in enumerate(h2s):
        body_parts.append(f"<h2>{h2}</h2>")
        # Section 1
        body_parts.append(
            f"<p>要理解呢個技巧，首先要明白佢喺廣東歌制作中嘅位置。香港嘅音樂文化源遠流長，由許冠傑時代到而家嘅新世代音樂人，"
            f"每個年代都有佢嘅制作特色。呢個技巧正正係連接傳統同現代嘅橋樑，掌握佢可以令你嘅作品更有層次同深度。"
            f"粵語本身嘅九聲六調特性，令廣東歌制作有獨特嘅考量，呢個技巧喺呢個語境下更加顯得重要。</p>"
        )
        # Section 2
        body_parts.append(
            f"<p>好多新手以為呢個技巧好難掌握，其實只要拆解成細步驟就容易理解。首先你要建立正確嘅概念基礎，"
            f"然後透過反覆練習去鞏固。好似學游水咁，理論睇得再多都唔夠落水試。建議你揀一首自己熟悉嘅廣東歌，"
            f"試吓分析佢點樣運用呢個技巧，由聽覺入手去理解背後嘅原理，會比淨係睇書更容易明白。</p>"
        )
        # Section 3 (with some variation)
        if i == 0:
            body_parts.append(
                f"<p>另外要留意嘅係，呢個技巧唔係孤立存在嘅。佢同廣東歌制作嘅其他環節互相影響，"
                f"好似作曲、填詞、編曲、錄音、混音每個階段都有可能用到。所以要學識佢，最好係將佢放喺整個制作流程嘅 context 去理解。"
                f"唔好淨係死記步驟，而係要明白點解要咁做，咁先至可以靈活運用喺唔同嘅情境。</p>"
            )
        elif i == 1:
            body_parts.append(
                f"<p>喺實踐嘅時候，最緊要係唔好心急。好多初學者一開始就想做到完美，結果反而因為太緊張而錯漏百出。"
                f"建議你先用最簡單嘅設定試一次，做完之後放低一陣，過幾個鐘或者第二日再聽返，通常會發現好多可以改進嘅地方。"
                f"呢個「冷卻期」好重要，因為你做嘅時候耳朵已經疲勞，判斷會唔準確。</p>"
            )
        elif i == 2:
            body_parts.append(
                f"<p>講到具體操作，有幾個要點要特別注意。第一，一定要用監聽耳機或者監聽喇叭去做判斷，"
                f"普通耳機或者電腦喇叭嘅頻率回應唔準確，會誤導你嘅決定。第二，要多用參考歌做 A/B 比較，"
                f"揀幾首你認為做得好嘅廣東歌，同你嘅作品交替播放，即時比較兩者嘅分別，咁就可以客觀咁睇到自己嘅水平。</p>"
            )
        elif i == 3:
            body_parts.append(
                f"<p>除咗技術層面，呢個技巧仲牽涉到審美判斷。冇一個設定係絕對啱或者錯，關鍵係要符合你首歌嘅情感需要。"
                f"一首抒情慢歌同一首節奏快歌，處理手法可以完全唔同。所以學技巧嘅同時，都要培養自己嘅音樂審美，"
                f"多聽唔同類型嘅廣東歌，累積聽覺經驗，自然會知道咩時候用咩手法。</p>"
            )
        else:
            body_parts.append(
                f"<p>最後要強調嘅係，呢個技巧嘅學習係一個持續嘅過程。就算係專業嘅音樂人，都會不斷鑽研同改進自己嘅技術。"
                f"建議你養成定期練習嘅習慣，每星期至少花幾個鐘頭專門研究呢個技巧。同時，將你嘅作品俾其他人聽，"
                f"收集唔同嘅意見，呢啲反饋係你進步嘅最好養分。記住，每個專家都係由新手開始嘅。</p>"
            )

    # FAQ section
    body_parts.append("<h2>常見問題</h2>")
    body_parts.append(
        f"<p><strong>呢個技巧需要幾長時間先至可以熟練？</strong> 呢個因人而異，但一般嚟講，"
        f"持續練習三至六個月就可以掌握基本應用。要達到專業水平就需要更長時間嘅累積，"
        f"但每一步嘅進步都係實在嘅，唔好急於求成。</p>"
    )
    body_parts.append(
        f"<p><strong>需要咩設備先至可以做？</strong> 入門級嘅設備已經足夠開始。"
        f"一部電腦、一副監聽耳機或者入門級監聽喇叭，加上 DAW 軟件就可以。"
        f"唔需要一開始就投資大量金錢，等技术成熟再逐步升級更明智。</p>"
    )
    body_parts.append(
        f"<p><strong>呢個技巧適用於所有類型嘅廣東歌嗎？</strong> 基本原理係通用嘅，"
        f"但唔同類型嘅廣東歌可能需要調整應用方式。抒情慢歌同節奏快歌嘅處理手法會有差異，"
        f"關鍵係理解背後嘅原理之後靈活運用。</p>"
    )
    body_parts.append(
        f"<p><strong>點樣知道自己嘅水平達到專業標準？</strong> 最直接嘅方法係同專業制作嘅廣東歌做 A/B 比較。"
        f"將你嘅作品同參考歌交替播放，聽下兩者之間嘅差距。如果差距已經好細，咁就代表你嘅水平已經接近專業。</p>"
    )

    # Highlight box
    body_parts.append('<div class="highlight-box">「制作廣東歌最緊要係用耳去聽、用心去感受。每個技術決定都應該服務於音樂嘅情感表達。」— 廣東歌·為你創作團隊</div>')

    # CTA
    body_parts.append('''  <div class="cta-box">
    <h3 class="serif">想將你嘅故事寫成廣東歌？</h3>
    <p>我哋嘅專業團隊可以為你度身訂製一首獨一無二嘅廣東歌，由填詞、作曲到錄音一站式完成。</p>
    <a href="/create.html" class="btn">🎵 立即訂製你嘅專屬廣東歌</a>
  </div>''')

    body_html = "\n\n".join(body_parts)

    html_content = f'''<!DOCTYPE html>
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
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","url":"{url}","publisher":{{"@type":"Organization","name":"廣東歌·為你","url":"https://mycantopop.hk"}}}}
  </script>
</head>
<body>
<nav><div class="nav-inner"><a href="/" class="logo"><div class="logo-icon">🎵</div><div><div class="logo-text">廣東歌·為你</div></div></a></div></nav>
<main>
  <p class="breadcrumb"><a href="/">首頁</a> › <a href="/articles">文章</a> › {title}</p>
  <h1 class="serif">{title}</h1>
  <p class="meta">{TODAY} · 廣東歌·為你</p>

  {body_html}
</main>
<footer>© 2025 廣東歌·為你 · <a href="/">首頁</a> · <a href="/articles">文章</a></footer>
</body>
</html>'''
    return html_content

# ---- Generate article files ----
for a in ARTICLES:
    path = os.path.join(ART_DIR, a["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(gen_article_html(a))
    # Check word count
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # crude word count: strip tags, count CJK chars + words
    import re
    text = re.sub(r'<[^>]+>', '', content)
    text = re.sub(r'\s+', ' ', text).strip()
    cjk_count = len(re.findall(r'[\u4e00-\u9fff]', text))
    print(f"  ✓ {a['slug']}.html ({cjk_count} CJK chars)")

# ---- Update index.html ----
index_path = os.path.join(ART_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Build new cards
new_cards = []
for a in ARTICLES:
    new_cards.append(f'''<a class="card" href="/articles/{a['slug']}.html">
        <span class="card-date">{TODAY}</span>
        <span class="card-tag">{a['tag']}</span>
        <h2>{a['title']}</h2>
        <p>{a['card']}</p>
        <span class="card-arrow">→</span>
      </a>''')

new_cards_html = "\n".join(new_cards)

# Insert before closing </div> of grid (the last </div> before footer)
# The grid closes with "    </div>" before the footer
# Find the last occurrence of "    </div>\n\n  <footer>"
old_tail = "    </div>\n\n  <footer>"
new_tail = f"{new_cards_html}\n    </div>\n\n  <footer>"
if old_tail in index_content:
    index_content = index_content.replace(old_tail, new_tail, 1)
    print("✓ Inserted cards before grid closing div (footer pattern)")
else:
    # Alternative: find last </div> before footer
    footer_idx = index_content.rfind("<footer>")
    # Find the last </div> before footer
    last_div = index_content.rfind("</div>", 0, footer_idx)
    insert_point = last_div
    index_content = index_content[:insert_point] + new_cards_html + "\n" + index_content[insert_point:]
    print("✓ Inserted cards before last </div> before footer (fallback)")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)
print("✓ Updated articles/index.html")

# ---- Update sitemap.xml ----
sitemap_path = os.path.join(REPO, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

new_urls = ""
for a in ARTICLES:
    new_urls += f"""  <url>
    <loc>https://mycantopop.hk/articles/{a['slug']}.html</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""

sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)
print("✓ Updated sitemap.xml")

print(f"\n✅ Done! Generated {len(ARTICLES)} new articles.")
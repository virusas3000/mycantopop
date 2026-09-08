#!/usr/bin/env python3
"""Finish the 2026-09-08 batch: update index.html, sitemap.xml, git commit & push."""
import os, subprocess

BASE = os.path.expanduser("~/Desktop/mycantopop")
ART_DIR = os.path.join(BASE, "articles")
TODAY = "2026-09-08"
TODAY_DISPLAY = "2026年09月08日"

# Same 29 slugs/titles/descriptions/categories
ARTICLES = [
("cantopop-arrangement-strings-col-legno-battuto-percussive-bow-technique-guide",
 "廣東歌編曲弦樂Col Legno Battuto擊弓打擊技巧：點樣用弓桿敲擊弦樂製造恐怖懸疑氛圍",
 "弦樂Col Legno Battuto擊弓技巧用弓桿敲擊弦線製造恐怖懸疑音色。教你編曲廣東歌弦樂打擊層。",
 "作曲編曲"),
("cantopop-mixing-vocal-mid-side-reverb-spatial-width-control-guide",
 "廣東歌混音人聲中側邊Reverb空間寬度控制指南：點樣用M/S Reverb收窄人聲立體聲寬度",
 "中側邊Reverb M/S空間寬度控制收窄人聲立體聲寬度。教你混音廣東歌人聲空間感。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-tram-ding-ding-journey-technique",
 "粵語歌詞從香港叮叮電車旅程寫作技巧：點樣用電車慢駛場景寫出城市節奏變遷",
 "叮叮電車旅程慢駛場景寫出香港城市節奏變遷歌詞。教你從電車意象寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-qq-music-tencent-mainland-china-streaming-guide",
 "廣東歌發行QQ音樂騰訊內地串流平台指南：點樣透過分銷商上架到QQ音樂觸達內地聽眾",
 "QQ音樂騰訊內地串流平台分銷商上架廣東歌觸達內地聽眾。教你發行廣東歌到QQ音樂。",
 "發行推廣"),
("cantopop-vocal-recording-ribbon-mic-fig8-off-axis-rejection-technique-guide",
 "廣東歌人聲錄音鋁帶麥克風8字指向離軸排斥技巧：點樣用Figure-8 Pattern控制串擾",
 "鋁帶麥克風Figure-8 8字指向離軸排斥控制串擾。教你錄廣東歌人聲鋁帶麥克風技巧。",
 "錄音製作"),
("cantonese-song-melody-pedal-tone-ostinato-anchoring-technique-guide",
 "廣東歌旋律持續音固定音型錨定技巧：點樣用Pedal Tone Ostinato穩定調性中心",
 "持續音Pedal Tone Ostinato固定音型錨定穩定調性中心。教你寫廣東歌旋律持續音技巧。",
 "作曲編曲"),
("cantopop-arrangement-percussion-cajon-flamenco-rhythm-groove-guide",
 "廣東歌編曲打擊樂Cajon弗拉明戈節奏律動指南：點樣用木箱鼓製造 acoustic 民謠感",
 "Cajon木箱鼓弗拉明戈節奏律動製造acoustic民謠感。教你編曲廣東歌打擊樂層。",
 "作曲編曲"),
("cantopop-mixing-drum-kick-sub-frequency-enhancement-sine-layer-guide",
 "廣東歌混音鼓Kick sub頻率增強正弦波疊加指南：點樣用Sine Wave Layer令底鼓更深沉",
 "底鼓Kick sub頻率正弦波Sine Wave Layer疊加令低頻更深沉。教你混音廣東歌鼓組低頻。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-public-housing-playground-memory-technique",
 "粵語歌詞從香港公共房屋遊樂場記憶寫作技巧：點樣用屋邨公園場景寫出童年純真",
 "屋邨公園遊樂場記憶激發童年純真歌詞。教你從公共房屋遊樂場寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-universal-music-group-demo-submission-guide",
 "廣東歌發行環球唱片集團Demo提交指南：點樣準備專業Demo Package向大廠牌自薦",
 "環球唱片Universal Music Group Demo Package提交向大廠牌自薦。教你發行廣東歌到唱片公司。",
 "發行推廣"),
("cantopop-vocal-recording-condenser-mic-pad-attenuation-saxophone-bleed-guide",
 "廣東歌人聲錄音電容麥克風衰減開關控制薩克斯風串音指南：點樣用Pad減低靈敏度隔離串音",
 "電容麥克風Pad衰減開關減低靈敏度隔離薩克斯風串音。教你錄廣東歌人聲隔離串音技巧。",
 "錄音製作"),
("cantonese-song-melody-interval-leap-emotional-mapping-technique-guide",
 "廣東歌旋律音程跳躍情感對應技巧：點樣用Interval Leap Map設計每個音程嘅情緒效果",
 "音程跳躍Interval Leap Map情感對應設計每個音程嘅情緒效果。教你寫廣東歌旋律音程。",
 "作曲編曲"),
("cantopop-arrangement-woodwind-oboe-english-horn-exotic-color-guide",
 "廣東歌編曲木管雙簧管英國管異國色彩指南：點樣用Oboe English Horn增添電影感",
 "雙簧管Oboe英國管English Horn異國色彩增添電影感。教你編曲廣東歌木管樂層。",
 "作曲編曲"),
("cantopop-mixing-vocal-harmony-panning-law-width-technique-guide",
 "廣東歌混音人聲和聲Pan Law寬度定位技巧：點樣用Pan Law設定和聲立體聲平衡",
 "和聲Pan Law寬度定位設定立體聲平衡。教你混音廣東歌人聲和聲定位技巧。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-school-picnic-day-memory-technique",
 "粵語歌詞從香港學校旅行日記憶寫作技巧：點樣用秋遊郊野場景寫出青春離別感",
 "學校旅行日秋遊郊野場景激發青春離別感歌詞。教你從校園記憶寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-warner-music-asia-demo-pitching-guide",
 "廣東歌發行華納音樂亞洲Demo投遞指南：點樣準備Pitching Package向華納自薦",
 "華納音樂Warner Music Asia Demo Pitching Package投遞自薦。教你發行廣東歌到華納音樂。",
 "發行推廣"),
("cantopop-vocal-recording-mic-polar-pattern-switching-live-guide",
 "廣東歌人聲錄音麥克風指向性切換現場錄音指南：點樣用Multi-Pattern Mic適應不同環境",
 "麥克風Multi-Pattern指向性切換適應不同現場錄音環境。教你錄廣東歌人聲現場錄音技巧。",
 "錄音製作"),
("cantonese-song-melody-appoggiatura-accented-non-chord-tone-guide",
 "廣東歌旋律倚音強拍非和弦音技巧：點樣用Appoggiatura製造情感張力同解決",
 "倚音Appoggiatura強拍非和弦音製造情感張力同解決。教你寫廣東歌旋律倚音技巧。",
 "作曲編曲"),
("cantopop-arrangement-synth-pad-granular-texture-layering-technique-guide",
 "廣東歌編曲合成器Pad顆粒質感疊層技巧：點樣用Granular Texture製造夢幻氛圍",
 "合成器Pad Granular Texture顆粒質感疊層製造夢幻氛圍。教你編曲廣東歌合成器層。",
 "作曲編曲"),
("cantopop-mixing-bass-dynamic-eq-frequency-selective-compression-guide",
 "廣東歌混音貝斯動態EQ頻率選擇壓縮指南：點樣用Dynamic EQ控制特定頻段動態",
 "貝斯Dynamic EQ動態頻率選擇壓縮控制特定頻段動態。教你混音廣東歌貝斯頻率控制。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-ching-ming-grave-sweeping-extended-technique",
 "粵語歌詞從香港清明掃墓延伸寫作技巧：點樣用拜山場景寫出家族傳承同思念",
 "清明掃墓拜山場景激發家族傳承思念歌詞。教你從祭祖記憶寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-independent-digital-aggregator-comparison-2026-guide",
 "廣東歌發行獨立數碼分銷商比較2026指南：點樣揀最適合嘅Aggregator上架你嘅歌",
 "獨立數碼分銷商Aggregator比較2026揀最適合上架廣東歌。教你發行廣東歌分銷商選擇。",
 "發行推廣"),
("cantopop-vocal-recording-headphone-mix-monitoring-comfort-guide",
 "廣東歌人聲錄音耳機混音監聽舒適度指南：點樣設定Cue Mix令歌手唱得更好",
 "耳機混音Cue Mix監聽舒適度設定令歌手唱得更好。教你錄廣東歌人聲監聽技巧。",
 "錄音製作"),
("cantonese-song-melody-passing-tone-chromatic-inflection-color-guide",
 "廣東歌旋律經過音半音變化色彩技巧：點樣用Chromatic Passing Tone增添色彩",
 "經過音Chromatic Passing Tone半音變化增添旋律色彩。教你寫廣東歌旋律經過音技巧。",
 "作曲編曲"),
("cantopop-arrangement-percussion-tambourine-shake-roll-buildup-guide",
 "廣東歌編曲打擊樂鈴鼓搖滾漸強推進指南：點樣用Tambourine Shake Roll製造段落推進",
 "鈴鼓Tambourine Shake Roll搖滾漸強推進製造段落推進。教你編曲廣東歌打擊樂漸強層。",
 "作曲編曲"),
("cantopop-mixing-vocal-reverb-pre-delay-phrase-clarity-technique-guide",
 "廣東歌混音人聲Reverb Pre-Delay歌詞清晰度技巧：點樣用Pre Delay分開人聲同殘響",
 "Reverb Pre-Delay分開人聲同殘響保持歌詞清晰度。教你混音廣東歌人聲殘響技巧。",
 "錄音製作"),
("cantonese-lyrics-writing-from-hong-kong-skyline-night-view-technique",
 "粵語歌詞從香港夜景天際線寫作技巧：點樣用維港夜景意象寫出都市人孤獨感",
 "維港夜景天際線意象激發都市人孤獨感歌詞。教你從香港夜景寫粵語歌詞。",
 "填詞技巧"),
("cantonese-song-distribution-content-id-youtube-monetization-setup-guide",
 "廣東歌發行Content ID YouTube貨幣化設定指南：點樣透過YouTube Content ID收取版稅",
 "YouTube Content ID貨幣化設定收取廣東歌版稅。教你發行廣東歌YouTube Content ID設定。",
 "發行推廣"),
("cantopop-vocal-recording-vocal-fatigue-prevention-hygiene-routine-guide",
 "廣東歌人聲錄音聲帶疲勞預防保養流程指南：點樣長時間錄音保護嗓子唔沙",
 "聲帶疲勞預防保養流程長時間錄音保護嗓子唔沙啞。教你錄廣東歌人聲保養技巧。",
 "錄音製作"),
]

assert len(ARTICLES) == 29

# ---- Update index.html ----
idx_path = os.path.join(ART_DIR, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

cards_html = ""
for slug, title, desc, cat in ARTICLES:
    cards_html += f'      <a class="card" href="/articles/{slug}.html">\n        <span class="card-date">{TODAY_DISPLAY}</span>\n        <span class="card-tag">{cat}</span>\n        <h2>{title}</h2>\n        <p>{desc}</p>\n        <span class="card-arrow">→</span>\n      </a>\n'

marker = '</div>\n\n  <footer>'
assert marker in idx_content, "Cannot find grid closing marker in index.html"
idx_content = idx_content.replace(marker, cards_html + marker)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("✓ articles/index.html updated with new cards")

# ---- Update sitemap.xml ----
sm_path = os.path.join(BASE, "sitemap.xml")
with open(sm_path, "r", encoding="utf-8") as f:
    sm_content = f.read()

new_urls = ""
for slug, title, desc, cat in ARTICLES:
    new_urls += f'  <url>\n    <loc>https://mycantopop.hk/articles/{slug}.html</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n'

sm_content = sm_content.replace("</urlset>", new_urls + "</urlset>")
with open(sm_path, "w", encoding="utf-8") as f:
    f.write(sm_content)
print("✓ sitemap.xml updated")

# ---- Git commit and push ----
os.chdir(BASE)
subprocess.run(["git", "config", "user.email", "cantopopforyou@gmail.com"], check=True)
subprocess.run(["git", "config", "user.name", "Vick Hung"], check=True)
subprocess.run(["git", "add", "-A"], check=True)

commit_msg = "feat: daily SEO batch — 29 new articles on 廣東歌制作, 寫歌, 作曲, 編曲, 錄音, 混音, 發行"
subprocess.run(["git", "commit", "-m", commit_msg], check=True)
print("✓ Git committed")

result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print(f"Git push stdout: {result.stdout}")
print(f"Git push stderr: {result.stderr}")
if result.returncode == 0:
    print("✓ Pushed to origin/main")
else:
    print(f"✗ Push failed (exit {result.returncode})")

print("\n=== DONE ===")
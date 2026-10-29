import urllib.request
import urllib.parse
import json
import time
import os
import re

CACHE_FILE = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual\scripts\trans_cache.json"

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)
else:
    cache = {}

print(f"Loaded cache entries: {len(cache)}")

def translate_text(text):
    text_clean = text.strip()
    if not text_clean or len(text_clean) < 2:
        return text
    # Skip pure numbers, codes, symbols
    if re.match(r"^[0-9\.\-\_\s\:\,\;\!\?\(\)\#\*\/\%\>\<\=\+\@\&\$]+$", text_clean):
        return text
    if text_clean in cache:
        return cache[text_clean]

    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q=" + urllib.parse.quote(text_clean)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=5) as res:
                data = json.loads(res.read().decode("utf-8"))
                trans = "".join(part[0] for part in data[0] if part[0])
                cache[text_clean] = trans
                return trans
        except Exception as e:
            time.sleep(0.5 * (attempt + 1))
            
    # Fallback to original if network fails
    return text

# Test batch of 5 sentences
test_sentences = [
    "Check whether the accessory drive system components are faulty.",
    "Remove the front gear train belt and try to turn the crankshaft with a wrench.",
    "Does the crankshaft rotate freely?",
    "Remove all spark plugs and check for water, oil or antifreeze in cylinders.",
    "Inspect the cylinder block, cylinder head and cylinder head gasket for cracks."
]

for s in test_sentences:
    res = translate_text(s)
    print(f"EN: {s}")
    print(f"RU: {res}\n")

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

print("Cache saved.")

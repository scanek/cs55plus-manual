import os
import re
import json
import fitz

PDF_PATH = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"
CACHE_PATH = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual\scripts\trans_cache.json"
IMG_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual\docs\public\img"

with open(CACHE_PATH, "r", encoding="utf-8") as f:
    cache = json.load(f)

doc = fitz.open(PDF_PATH)
existing_images = set(os.listdir(IMG_DIR))

def get_trans(text):
    s = text.strip()
    if not s:
        return ""
    if s in cache:
        return cache[s]
    # Check normalized
    s_norm = re.sub(r"\s+", " ", s)
    if s_norm in cache:
        return cache[s_norm]
    # Quick translation if short or in translations dict
    return s

def parse_page(pno):
    page = doc[pno - 1]
    
    # 1. Collect non-icon images with rects
    images = []
    for img_info in page.get_images():
        xref = img_info[0]
        rects = page.get_image_rects(xref)
        for r in rects:
            if (r.y1 - r.y0) > 35 and (r.x1 - r.x0) > 35:
                # Find matching image file
                fname = None
                for ext in ["jpeg", "png", "jpg"]:
                    cand = f"p{pno}_{len(images)+1}.{ext}"
                    if cand in existing_images:
                        fname = cand
                        break
                if not fname:
                    fname = f"p{pno}_{len(images)+1}.png"
                images.append({
                    "y0": r.y0,
                    "y1": r.y1,
                    "x0": r.x0,
                    "fname": fname,
                    "xref": xref
                })
    
    # 2. Collect content blocks (skip headers y < 65 and footers y > 805)
    raw_blocks = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, text, bno, btype = b
        if y0 < 65 or y0 > 805:
            continue
        txt = text.strip()
        if not txt:
            continue
        raw_blocks.append({
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "text": txt
        })

    # Sort blocks vertically
    raw_blocks.sort(key=lambda b: (b["y0"], b["x0"]))
    return raw_blocks, images

print("Prototype script created.")

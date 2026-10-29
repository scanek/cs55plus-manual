import os
import re
import json
import fitz

doc = fitz.open(r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf")
IMG_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual\docs\public\img"
existing_images = set(os.listdir(IMG_DIR))

def test_page(pno):
    page = doc[pno - 1]
    images = []
    for idx, img_info in enumerate(page.get_images()):
        xref = img_info[0]
        rects = page.get_image_rects(xref)
        for r in rects:
            if (r.y1 - r.y0) > 35 and (r.x1 - r.x0) > 35:
                fname = None
                for ext in ["jpeg", "png", "jpg"]:
                    cand = f"p{pno}_{idx+1}.{ext}"
                    if cand in existing_images:
                        fname = cand
                        break
                if not fname:
                    fname = f"p{pno}_{idx+1}.png"
                images.append((r.y0, r.y1, fname))

    blocks = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, text, bno, btype = b
        if y0 < 65 or y0 > 805:
            continue
        txt = text.strip()
        if txt:
            blocks.append((x0, y0, x1, y1, txt))

    blocks.sort(key=lambda b: (b[1], b[0]))
    images.sort(key=lambda img: img[0])
    
    print(f"=== PAGE {pno} ===")
    print(f"Blocks: {len(blocks)}, Images: {len(images)}")
    for b in blocks:
        print(f"  Block (y={b[1]:.0f}, x={b[0]:.0f}): {repr(b[4][:50])}")
    for img in images:
        print(f"  Image (y={img[0]:.0f}..{img[1]:.0f}): {img[2]}")

test_page(68)
test_page(67)
test_page(41)

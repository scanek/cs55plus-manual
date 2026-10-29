import os
import re
import json
import fitz

pdf_path = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"
doc = fitz.open(pdf_path)
total_pages = len(doc)
print(f"Total pages: {total_pages}")

# Let's inspect page 1 table of contents or general structure
# Let's check the first 10 pages for table of contents
toc_pages = []
for p in range(min(20, total_pages)):
    text = doc[p].get_text()
    if "........" in text or "table of contents" in text.lower() or "contents" in text.lower():
        toc_pages.append(p + 1)
print(f"Pages with TOC-like dots/contents: {toc_pages}")

# Analyze header pattern across all pages
# Each page typically has a header with chapter and section
page_info = []
for idx in range(total_pages):
    page = doc[idx]
    text = page.get_text()
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    header_cat = ""
    header_sub = ""
    if len(lines) >= 1:
        header_cat = lines[0]
    if len(lines) >= 2:
        header_sub = lines[1]
    
    # Clean header_sub of trailing digits (page numbers)
    header_sub = re.sub(r'\d+$', '', header_sub).strip()
    page_info.append({
        "page": idx + 1,
        "cat": header_cat,
        "sub": header_sub,
        "first_lines": lines[:4]
    })

# Group consecutive pages with same cat/sub
sections = []
current_sec = None

for p in page_info:
    key = (p["cat"], p["sub"])
    if current_sec is None or (current_sec["cat"], current_sec["sub"]) != key:
        if current_sec:
            current_sec["end_page"] = p["page"] - 1
            current_sec["page_count"] = current_sec["end_page"] - current_sec["start_page"] + 1
            sections.append(current_sec)
        current_sec = {
            "cat": p["cat"],
            "sub": p["sub"],
            "start_page": p["page"],
            "end_page": p["page"],
            "sample": p["first_lines"]
        }
if current_sec:
    current_sec["end_page"] = total_pages
    current_sec["page_count"] = current_sec["end_page"] - current_sec["start_page"] + 1
    sections.append(current_sec)

print(f"Discovered {len(sections)} distinct section blocks.")

with open("sections_summary.json", "w", encoding="utf-8") as f:
    json.dump(sections, f, ensure_ascii=False, indent=2)

# Print high-level categories
categories = {}
for s in sections:
    c = s["cat"]
    categories[c] = categories.get(c, 0) + s["page_count"]

print("\n--- Categories and page count ---")
for c, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"  {c}: {count} pages")

import fitz
import re
import json

pdf_path = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")

# Collect table of contents and major section markers
markers = []
for i in range(len(doc)):
    txt = doc[i].get_text()
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    if not lines:
        continue
    # Look for major chapter headers
    # Lines like "Engine", "Automatic transmission", "Chassis", "Electrical system"
    first = lines[0]
    second = lines[1] if len(lines) > 1 else ""
    
    # Check if page has TOC dots
    if "........" in txt:
        markers.append({"page": i + 1, "type": "TOC", "line1": first, "line2": second})

print("TOC Markers found:")
for m in markers:
    print(m)

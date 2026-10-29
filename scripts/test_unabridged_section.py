import os
import re
import fitz

BASE_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PDF_PATH = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"

doc = fitz.open(PDF_PATH)
print(f"Loaded PDF: {len(doc)} pages")

from extract_unabridged import clean_and_format_page

# Test generating Mechanical Removal and Installation (pages 65 to 91)
p_start = 65
p_end = 91

output_file = os.path.join(DOCS_DIR, "02-engine", "mechanical-removal.md")
content = [
    "# Механическая часть двигателя — Снятие и установка агрегатов (Полная заводская процедура)\n",
    f"> **Страницы оригинального руководства:** {p_start} – {p_end} | **Модель:** Changan CS55 Plus (JL473ZQ7)\n",
    "Данный раздел содержит полный заводской технологический процесс снятия, разборки и установки силового агрегата, элементов ГРМ, клапанной крышки, ГБЦ, поддона и навесного оборудования.\n",
    "---\n"
]

for p in range(p_start, p_end + 1):
    page_text = clean_and_format_page(p)
    if page_text.strip():
        content.append(page_text)
        content.append("\n---\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(content))

print(f"Generated {output_file}: {os.path.getsize(output_file)} bytes")

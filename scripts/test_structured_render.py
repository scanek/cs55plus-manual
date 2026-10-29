import os
import re
import json
import fitz

BASE_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PUBLIC_IMG_DIR = os.path.join(DOCS_DIR, "public", "img")
CACHE_FILE = os.path.join(BASE_DIR, "scripts", "trans_cache.json")
PDF_PATH = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"

with open(CACHE_FILE, "r", encoding="utf-8") as f:
    cache = json.load(f)

doc = fitz.open(PDF_PATH)
existing_images = set(os.listdir(PUBLIC_IMG_DIR))

def get_trans(text):
    s = text.strip()
    if not s or len(s) < 2:
        return text
    if re.match(r"^[0-9\.\-\_\s\:\,\;\!\?\(\)\#\*\/\%\>\<\=\+\@\&\$\\\/\|]+$", s):
        return text
    if s in cache:
        return cache[s]
    # Check normalized spaces
    s_norm = re.sub(r"\s+", " ", s)
    if s_norm in cache:
        return cache[s_norm]
    return s

def format_torque_and_tools(text):
    # Highlight torque specs: e.g. 25 N.m, 50+38° N.m, 120 N·m
    t = re.sub(
        r"(\b\d+(?:[\+\-]\d+°?)?\s*(?:N[\.·]m|Н[\.·]м|N\s*m)\b(?:\s*[\+\-]\s*\d+°?)?)",
        r'<span class="torque-badge">🔧 \1</span>',
        text,
        flags=re.IGNORECASE
    )
    # Highlight special tools: CA\d+-\d+
    t = re.sub(
        r"(\bCA\d{3}-\d{3}\b)",
        r'<span class="tool-badge">🛠️ \1</span>',
        t
    )
    return t

def render_page_structured(pno):
    page = doc[pno - 1]
    
    # 1. Collect valid images with vertical coordinates
    page_images = []
    for idx, img_info in enumerate(page.get_images()):
        xref = img_info[0]
        rects = page.get_image_rects(xref)
        for r in rects:
            # Filter small icons (< 35px)
            if (r.y1 - r.y0) > 35 and (r.x1 - r.x0) > 35:
                fname = None
                for ext in ["jpeg", "png", "jpg"]:
                    cand = f"p{pno}_{idx+1}.{ext}"
                    if cand in existing_images:
                        fname = cand
                        break
                if not fname:
                    cand_png = f"p{pno}_{idx+1}.png"
                    try:
                        base_img = doc.extract_image(xref)
                        if len(base_img["image"]) > 2000:
                            fpath = os.path.join(PUBLIC_IMG_DIR, cand_png)
                            with open(fpath, "wb") as f:
                                f.write(base_img["image"])
                            existing_images.add(cand_png)
                            fname = cand_png
                    except Exception:
                        pass
                if fname:
                    page_images.append({
                        "y0": r.y0,
                        "y1": r.y1,
                        "x0": r.x0,
                        "fname": fname
                    })

    page_images.sort(key=lambda img: img["y0"])

    # 2. Collect content blocks (skip running headers y0 < 65 and footers y0 > 805)
    blocks = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, text, bno, btype = b
        if y0 < 65 or y0 > 805:
            continue
        txt = text.strip()
        if not txt:
            continue
        # Clean stray footer numbers at bottom
        if y0 > 795 and re.match(r"^\d+$", txt):
            continue
        blocks.append({
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "text": txt
        })

    blocks.sort(key=lambda b: (b["y0"], b["x0"]))

    if not blocks and not page_images:
        return ""

    # 3. Check if page is diagnostic table (has ? Yes / ? No / Test conditions)
    has_diagnostic = any("? Yes" in b["text"] or "? No" in b["text"] or "? Да" in b["text"] or "? Нет" in b["text"] for b in blocks)
    
    output_lines = []
    output_lines.append(f'\n<div class="page-header" style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--vp-c-divider); padding:4px 0; margin-top:24px; color:var(--vp-c-text-2); font-size:13px;">')
    output_lines.append(f'  <span>📘 <b>Оригинальная страница: {pno}</b></span>')
    output_lines.append(f'  <span class="page-pill">PDF P.{pno}</span>')
    output_lines.append(f'</div>\n')

    if has_diagnostic:
        # Diagnostic symptom page
        table_rows = []
        curr_step_num = 1
        curr_symptom = None

        for b in blocks:
            txt = b["text"]
            # Check for symptom title
            if "Test conditions" in txt or "Details/Results/Measures" in txt:
                continue
            if b["x0"] < 80 and not re.match(r"^\d+[\.\)]", txt) and not txt.startswith("?") and len(txt) < 80:
                if not any(k in txt for k in ["Reference:", "Check", "Inspect", "Remove"]):
                    curr_symptom = get_trans(txt)
                    output_lines.append(f"\n### 🔍 Симптом: {curr_symptom}\n")
                    continue

            # Check if this block has step question & answers
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            for l in lines:
                if re.match(r"^\d+[\.\)]\s+", l):
                    step_match = re.match(r"^(\d+)[\.\)]\s+(.*)", l)
                    if step_match:
                        curr_step_num = step_match.group(1)
                        step_text = get_trans(step_match.group(2))
                        table_rows.append({"num": curr_step_num, "cond": step_text, "yes": "", "no": ""})
                elif l.startswith("? Yes") or l.startswith("? Да"):
                    action = re.sub(r"^\?\s*(?:Yes|Да)[\.,\:]?\s*", "", l)
                    if table_rows:
                        table_rows[-1]["yes"] = get_trans(action)
                elif l.startswith("? No") or l.startswith("? Нет"):
                    action = re.sub(r"^\?\s*(?:No|Нет)[\.,\:]?\s*", "", l)
                    if table_rows:
                        table_rows[-1]["no"] = get_trans(action)
                else:
                    t_l = get_trans(l)
                    if table_rows and not table_rows[-1]["yes"]:
                        table_rows[-1]["cond"] += " " + t_l

        if table_rows:
            output_lines.append("\n| № | Проверка / Условие | Результат | Мера устранения |")
            output_lines.append("| :-: | :--- | :--- | :--- |")
            for r in table_rows:
                num = r["num"]
                cond = format_torque_and_tools(r["cond"])
                yes = format_torque_and_tools(r["yes"]) if r["yes"] else "Перейдите к следующему шагу"
                no = format_torque_and_tools(r["no"]) if r["no"] else "Перейдите к следующему шагу"
                output_lines.append(f"| **{num}** | {cond} | <span class=\"status-yes\">✅ Да</span> | {yes} |")
                output_lines.append(f"| | | <span class=\"status-no\">❌ Нет</span> | {no} |")
            output_lines.append("\n")

        # Add any images on diagnostic page
        if page_images:
            output_lines.append('<div class="step-gallery">')
            for img in page_images:
                output_lines.append(f'  <img src="/img/{img["fname"]}" alt="Схема к стр. {pno}" />')
            output_lines.append('</div>\n')

        return "\n".join(output_lines)

    # 4. Standard Procedural / Step Pages
    # Interleave text blocks and images chronologically by vertical coordinate y0
    all_items = []
    for b in blocks:
        all_items.append({"type": "block", "y0": b["y0"], "y1": b["y1"], "data": b})
    for img in page_images:
        all_items.append({"type": "img", "y0": img["y0"], "y1": img["y1"], "data": img})

    all_items.sort(key=lambda item: item["y0"])

    # Process items
    i = 0
    while i < len(all_items):
        item = all_items[i]
        
        if item["type"] == "img":
            img = item["data"]
            output_lines.append(f'\n<div class="step-gallery">\n  <img src="/img/{img["fname"]}" alt="Иллюстрация к процедуре (стр. {pno})" />\n</div>\n')
            i += 1
            continue

        b = item["data"]
        txt = b["text"]

        # Check for Warning / Caution
        if txt.strip() in ["Warning", "Внимание", "Caution", "Предостережение", "Note", "Примечание"]:
            # Next block is usually the warning text
            alert_type = "warning" if txt.strip() in ["Warning", "Внимание", "Caution", "Предостережение"] else "tip"
            alert_title = "ВНИМАНИЕ" if alert_type == "warning" else "ПРИМЕЧАНИЕ"
            warn_text = ""
            if i + 1 < len(all_items) and all_items[i+1]["type"] == "block":
                warn_text = get_trans(all_items[i+1]["data"]["text"])
                i += 1
            warn_formatted = format_torque_and_tools(warn_text)
            output_lines.append(f"\n::: {alert_type} {alert_title}\n{warn_formatted}\n:::\n")
            i += 1
            continue

        # Check if text starts with step number (e.g. "4 \nDrain transmission oil" or "4. Drain...")
        step_match = re.match(r"^(\d+)[\.\)]?\s*\n+(.*)", txt, re.DOTALL)
        if not step_match:
            step_match = re.match(r"^(\d+)[\.\)]\s+(.*)", txt, re.DOTALL)

        if step_match:
            step_num = step_match.group(1)
            step_body = step_match.group(2).strip()
            trans_body = get_trans(step_body) if step_body else ""
            formatted_body = format_torque_and_tools(trans_body)

            output_lines.append(f'\n<div class="step-card">')
            output_lines.append(f'  <div class="step-title"><span class="step-badge">ШАГ {step_num}</span> <span>{formatted_body}</span></div>')

            # Check if immediately following items are images belonging to this step
            step_imgs = []
            while i + 1 < len(all_items) and all_items[i+1]["type"] == "img":
                step_imgs.append(all_items[i+1]["data"])
                i += 1

            if step_imgs:
                output_lines.append('  <div class="step-gallery">')
                for s_img in step_imgs:
                    output_lines.append(f'    <img src="/img/{s_img["fname"]}" alt="Шаг {step_num} (стр. {pno})" />')
                output_lines.append('  </div>')

            output_lines.append('</div>\n')
            i += 1
            continue

        # General text / headers
        trans_txt = get_trans(txt)
        formatted_txt = format_torque_and_tools(trans_txt)

        # Format warnings inside general block if any
        if re.match(r"^(warning|внимание)", trans_txt, re.IGNORECASE):
            output_lines.append(f"\n::: warning ВНИМАНИЕ\n{formatted_txt}\n:::\n")
        elif re.match(r"^(caution|предостережение)", trans_txt, re.IGNORECASE):
            output_lines.append(f"\n::: warning ПРЕДОСТЕРЕЖЕНИЕ\n{formatted_txt}\n:::\n")
        elif len(txt) < 60 and not txt.endswith(".") and not txt.endswith(":"):
            output_lines.append(f"\n#### {formatted_txt}\n")
        else:
            output_lines.append(f"\n{formatted_txt}\n")

        i += 1

    return "\n".join(output_lines)

if __name__ == "__main__":
    out65 = render_page_structured(65)
    out67 = render_page_structured(67)
    out68 = render_page_structured(68)
    sample_path = os.path.join(BASE_DIR, "scripts", "sample_output.md")
    with open(sample_path, "w", encoding="utf-8") as f:
        f.write("# Demo Structured Render\n\n" + out65 + "\n\n" + out67 + "\n\n" + out68)
    print("Demo rendered successfully to sample_output.md")

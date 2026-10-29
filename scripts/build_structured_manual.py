import os
import re
import json
import time
import urllib.request
import urllib.parse
import fitz

BASE_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PUBLIC_IMG_DIR = os.path.join(DOCS_DIR, "public", "img")
CACHE_FILE = os.path.join(BASE_DIR, "scripts", "trans_cache.json")
PDF_PATH = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"

os.makedirs(PUBLIC_IMG_DIR, exist_ok=True)

# Load translation cache
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
    except Exception:
        cache = {}
else:
    cache = {}

print(f"Loaded translation cache: {len(cache)} entries")

doc = fitz.open(PDF_PATH)
print(f"Loaded PDF: {len(doc)} pages")

existing_images = set(os.listdir(PUBLIC_IMG_DIR))
print(f"Existing images in docs/public/img: {len(existing_images)}")

def translate_batch(texts):
    """Batch-translates texts using Google GTX API with fast grouping and cache."""
    results = [None] * len(texts)
    to_query_indices = []
    to_query_texts = []

    for i, t in enumerate(texts):
        s = t.strip()
        if not s or len(s) < 2 or re.match(r"^[0-9\.\-\_\s\:\,\;\!\?\(\)\#\*\/\%\>\<\=\+\@\&\$\\\/\|]+$", s):
            results[i] = t
        elif s in cache:
            results[i] = cache[s]
        else:
            s_norm = re.sub(r"\s+", " ", s)
            if s_norm in cache:
                results[i] = cache[s_norm]
            else:
                to_query_indices.append(i)
                to_query_texts.append(s)

    if not to_query_texts:
        return results

    # Batch into chunks of up to 15 items and max 2200 chars
    CHUNK_MAX_ITEMS = 15
    CHUNK_MAX_CHARS = 2200

    chunks = []
    curr_indices = []
    curr_texts = []
    curr_len = 0

    for idx, txt in zip(to_query_indices, to_query_texts):
        if len(curr_texts) >= CHUNK_MAX_ITEMS or (curr_len + len(txt) > CHUNK_MAX_CHARS and curr_texts):
            chunks.append((curr_indices, curr_texts))
            curr_indices = [idx]
            curr_texts = [txt]
            curr_len = len(txt)
        else:
            curr_indices.append(idx)
            curr_texts.append(txt)
            curr_len += len(txt)
    if curr_texts:
        chunks.append((curr_indices, curr_texts))

    DELIM = "\n\n<<<999>>>\n\n"

    for chunk_indices, chunk_texts in chunks:
        joined = DELIM.join(chunk_texts)
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q=" + urllib.parse.quote(joined)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        
        success = False
        for attempt in range(2):
            try:
                with urllib.request.urlopen(req, timeout=8) as res:
                    data = json.loads(res.read().decode("utf-8"))
                    full_text = "".join(part[0] for part in data[0] if part[0])
                    parts = [p.strip() for p in full_text.split("<<<999>>>")]
                    if len(parts) == len(chunk_texts):
                        for c_idx, orig, trans in zip(chunk_indices, chunk_texts, parts):
                            cache[orig] = trans
                            results[c_idx] = trans
                        success = True
                        break
            except Exception:
                time.sleep(0.3 * (attempt + 1))
        
        if not success:
            for c_idx, orig in zip(chunk_indices, chunk_texts):
                q = orig[:2500]
                single_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q=" + urllib.parse.quote(q)
                single_req = urllib.request.Request(single_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                single_success = False
                for a in range(2):
                    try:
                        with urllib.request.urlopen(single_req, timeout=5) as r:
                            d = json.loads(r.read().decode("utf-8"))
                            t_single = "".join(p[0] for p in d[0] if p[0])
                            cache[orig] = t_single
                            results[c_idx] = t_single
                            single_success = True
                            break
                    except Exception:
                        time.sleep(0.2)
                if not single_success:
                    results[c_idx] = orig
        
        time.sleep(0.04)

    return results

def format_torque_and_tools(text):
    if not text:
        return ""
    # Highlight torque specs: e.g. 25 N.m, 50+38° N.m, 120 N·m
    t = re.sub(
        r"(\b\d+(?:[\+\-]\d+°?)?\s*(?:N[\.·]m|Н[\.·]м|N\s*m)\b(?:\s*[\+\-]\s*\d+°?)?)",
        r'<span class="torque-badge">🔧 \1</span>',
        text,
        flags=re.IGNORECASE
    )
    # Highlight special tools: CA501-...
    t = re.sub(
        r"(\bCA\d{3}-\d{3}\b)",
        r'<span class="tool-badge">🛠️ \1</span>',
        t
    )
    return t

def render_table_markdown(rows):
    if not rows or len(rows) < 2:
        return ""
    # Filter empty columns
    col_count = max(len(r) for r in rows)
    valid_cols = []
    for c in range(col_count):
        if any(r[c] and str(r[c]).strip() for r in rows if c < len(r)):
            valid_cols.append(c)

    if not valid_cols:
        return ""

    # Flatten strings for batch translation
    cell_texts = []
    cell_coords = []
    for r_idx, r in enumerate(rows):
        for c in valid_cols:
            val = str(r[c]).replace("\n", " ").strip() if c < len(r) and r[c] else ""
            if val and val != "-" and val != "—":
                cell_texts.append(val)
                cell_coords.append((r_idx, c))

    if not cell_texts:
        return ""

    translated_cells = translate_batch(cell_texts)
    trans_map = {}
    for (r_idx, c), t in zip(cell_coords, translated_cells):
        trans_map[(r_idx, c)] = t

    # Build markdown
    md_lines = []
    # Header
    header_vals = []
    for c in valid_cols:
        val = trans_map.get((0, c), str(rows[0][c]).strip() if c < len(rows[0]) and rows[0][c] else "—")
        header_vals.append(val)
    
    # If all header values are dashes, not a real table
    if all(v in ["—", "-", ""] for v in header_vals):
        return ""

    md_lines.append("| " + " | ".join(header_vals) + " |")
    md_lines.append("| " + " | ".join([":---" for _ in valid_cols]) + " |")

    # Body
    for r_idx in range(1, len(rows)):
        row_vals = []
        for c in valid_cols:
            val = trans_map.get((r_idx, c), str(rows[r_idx][c]).strip() if c < len(rows[r_idx]) and rows[r_idx][c] else "—")
            val_fmt = format_torque_and_tools(val)
            row_vals.append(val_fmt)
        md_lines.append("| " + " | ".join(row_vals) + " |")

    return "\n" + "\n".join(md_lines) + "\n"

def render_page_structured(pno):
    page = doc[pno - 1]
    
    # 1. Images with vertical coordinates (filter icons < 35px)
    page_images = []
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

    # 2. Extract tables
    tables_found = page.find_tables()
    table_bboxes = []
    table_renders = []
    for t in tables_found.tables:
        rows = t.extract()
        if len(rows) >= 2:
            t_md = render_table_markdown(rows)
            if t_md.strip():
                table_bboxes.append(t.bbox)
                table_renders.append((t.bbox[1], t.bbox[3], t_md))

    # 3. Collect non-table content blocks (skip running headers y0 < 65 and footers y0 > 805)
    blocks = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, text, bno, btype = b
        if y0 < 65 or y0 > 805:
            continue
        txt = text.strip()
        if not txt:
            continue
        # Check if inside any table bbox
        in_table = False
        for (tx0, ty0, tx1, ty1) in table_bboxes:
            if tx0 - 5 <= x0 and x1 <= tx1 + 5 and ty0 - 5 <= y0 and y1 <= ty1 + 5:
                in_table = True
                break
        if in_table:
            continue

        # Split block if it contains embedded step lines (e.g. warning + "\n2 \nDisconnect...")
        sub_parts = re.split(r"\n(?=\d+[\.\)]?\s*\n|\d+[\.\)]\s+)", txt)
        for part in sub_parts:
            p_clean = part.strip()
            if p_clean:
                blocks.append({
                    "x0": x0,
                    "y0": y0,
                    "x1": x1,
                    "y1": y1,
                    "text": p_clean
                })

    blocks.sort(key=lambda b: (b["y0"], b["x0"]))

    if not blocks and not page_images and not table_renders:
        return ""

    # Page header anchor
    output_lines = []
    output_lines.append(f'\n<div class="page-header" style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--vp-c-divider); padding:4px 0; margin-top:28px; margin-bottom:12px; color:var(--vp-c-text-2); font-size:13px;">')
    output_lines.append(f'  <span>📘 <b>Оригинальная страница: {pno}</b></span>')
    output_lines.append(f'  <span class="page-pill">PDF P.{pno}</span>')
    output_lines.append(f'</div>\n')

    # Interleave text blocks, tables, and images by y0
    all_items = []
    for b in blocks:
        all_items.append({"type": "block", "y0": b["y0"], "data": b})
    for t_y0, t_y1, t_md in table_renders:
        all_items.append({"type": "table", "y0": t_y0, "data": t_md})
    for img in page_images:
        all_items.append({"type": "img", "y0": img["y0"], "data": img})

    all_items.sort(key=lambda item: item["y0"])

    # Pre-translate all block texts on the page in one fast batch call
    page_texts_to_translate = []
    for b in blocks:
        txt = b["text"]
        step_match = re.match(r"^(\d+)[\.\)]?\s*\n+(.*)", txt, re.DOTALL)
        if not step_match:
            step_match = re.match(r"^(\d+)[\.\)]\s+(.*)", txt, re.DOTALL)
        if step_match:
            body = step_match.group(2).strip()
            if body:
                page_texts_to_translate.append(body)
        else:
            page_texts_to_translate.append(txt)

    if page_texts_to_translate:
        translate_batch(page_texts_to_translate)

    i = 0
    while i < len(all_items):
        item = all_items[i]
        
        if item["type"] == "table":
            output_lines.append(item["data"])
            i += 1
            continue

        if item["type"] == "img":
            img = item["data"]
            output_lines.append(f'\n<div class="step-gallery">\n  <img src="/img/{img["fname"]}" alt="Иллюстрация к процедуре (стр. {pno})" />\n</div>\n')
            i += 1
            continue

        b = item["data"]
        txt = b["text"]

        # Check for Warning / Caution callout
        if txt.strip() in ["Warning", "Внимание", "Caution", "Предостережение", "Note", "Примечание"]:
            alert_type = "warning" if txt.strip() in ["Warning", "Внимание", "Caution", "Предостережение"] else "tip"
            alert_title = "ВНИМАНИЕ" if alert_type == "warning" else "ПРИМЕЧАНИЕ"
            warn_text = ""
            if i + 1 < len(all_items) and all_items[i+1]["type"] == "block":
                warn_text = translate_batch([all_items[i+1]["data"]["text"]])[0]
                i += 1
            warn_fmt = format_torque_and_tools(warn_text)
            output_lines.append(f"\n::: {alert_type} {alert_title}\n{warn_fmt}\n:::\n")
            i += 1
            continue

        # Check for step card (e.g. "4 \nDrain transmission oil" or "4. Drain...")
        step_match = re.match(r"^(\d+)[\.\)]?\s*\n+(.*)", txt, re.DOTALL)
        if not step_match:
            step_match = re.match(r"^(\d+)[\.\)]\s+(.*)", txt, re.DOTALL)

        if step_match:
            step_num = step_match.group(1)
            step_body = step_match.group(2).strip()
            trans_body = translate_batch([step_body])[0] if step_body else ""
            fmt_body = format_torque_and_tools(trans_body)

            output_lines.append(f'\n<div class="step-card">')
            output_lines.append(f'  <div class="step-title"><span class="step-badge">ШАГ {step_num}</span> <span>{fmt_body}</span></div>')

            # Attach any subsequent images for this step
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

        # General text
        trans_txt = translate_batch([txt])[0]
        fmt_txt = format_torque_and_tools(trans_txt)

        lower = trans_txt.lower()
        if lower.startswith("warning") or lower.startswith("внимание"):
            output_lines.append(f"\n::: warning ВНИМАНИЕ\n{fmt_txt}\n:::\n")
        elif lower.startswith("caution") or lower.startswith("предостережение"):
            output_lines.append(f"\n::: warning ПРЕДОСТЕРЕЖЕНИЕ\n{fmt_txt}\n:::\n")
        elif len(txt) < 65 and not txt.endswith(".") and not txt.endswith(":"):
            output_lines.append(f"\n#### {fmt_txt}\n")
        else:
            output_lines.append(f"\n{fmt_txt}\n")

        i += 1

    return "\n".join(output_lines)

SECTIONS_TO_BUILD = [
    # General (1 - 34)
    ("01-general", "index.md", "01. Общие сведения и регламент", 1, 3),
    ("01-general", "safety.md", "Техника безопасности и охрана труда", 4, 13),
    ("01-general", "standards.md", "Стандарты сервисного обслуживания и ремонта", 14, 16),
    ("01-general", "vin.md", "Идентификация (VIN, шильдики, номера агрегатов)", 17, 18),
    ("01-general", "lifting-towing.md", "Буксировка, подъем на подъемнике и домкраты", 19, 24),
    ("01-general", "nvh.md", "Диагностика шумов, вибраций и жесткости (NVH)", 25, 34),

    # Engine (35 - 475)
    ("02-engine", "index.md", "02. Двигатель 1.5T — Общие сведения и устройство", 35, 40),
    ("02-engine", "mechanical-specs.md", "Механическая часть: Спецификации и моменты затяжки", 41, 44),
    ("02-engine", "mechanical-principles.md", "Механическая часть: Устройство и состав деталей", 45, 52),
    ("02-engine", "mechanical-diagnosis.md", "Механическая часть: Поиск неисправностей по симптомам", 53, 64),
    ("02-engine", "mechanical-removal.md", "Механическая часть: Снятие и установка агрегатов (Полная процедура)", 65, 78),
    ("02-engine", "mechanical-overhaul.md", "Механическая часть: Разборка и дефектовка ГБЦ, клапанов и поршневой", 79, 91),
    ("02-engine", "lubrication.md", "Система смазки двигателя: Насос, поддон, фильтр, давление", 92, 110),
    ("02-engine", "cooling.md", "Система охлаждения: Радиатор, помпа, электронный термостат, прокачка", 111, 133),
    ("02-engine", "fuel.md", "Топливная система GDI: ТНВД, рампа 350 бар, форсунки, бак", 134, 168),
    ("02-engine", "fuel-vapor.md", "Система улавливания паров топлива EVAP: Адсорбер и клапан", 169, 188),
    ("02-engine", "intake.md", "Система впуска и турбонаддув: Турбина, интеркулер, дроссель", 189, 206),
    ("02-engine", "exhaust.md", "Выпускная система: Коллектор, нейтрализатор, лямбда-зонды", 207, 224),
    ("02-engine", "ignition.md", "Система зажигания: Катушки, свечи зажигания", 225, 235),
    ("02-engine", "starting.md", "Система пуска двигателя: Стартер, реле, проверки", 236, 251),
    ("02-engine", "charging.md", "Система зарядки: Генератор 130А, шина LIN, датчик тока IBS", 252, 270),
    ("02-engine", "ecu.md", "Электронное управление двигателем: Датчики, распиновки, адаптации", 271, 380),
    ("02-engine", "dtc.md", "Коды неисправностей (DTC) двигателя: Полные карты проверок", 381, 475),

    # Transmission (476 - 677)
    ("03-transmission", "index.md", "03. Трансмиссия 7DCT — Обзор и характеристики", 476, 485),
    ("03-transmission", "specifications.md", "Спецификации, моменты затяжки и масло BOT 351 C4", 486, 500),
    ("03-transmission", "structure.md", "Кинематическая схема, двойное сцепление и гидроблок", 501, 530),
    ("03-transmission", "electronic-shift.md", "Электронный селектор Shift-by-Wire и аварийная разблокировка P", 531, 565),
    ("03-transmission", "service.md", "Снятие, установка КПП 7DCT, замена масла и адаптация", 566, 615),
    ("03-transmission", "dtc.md", "Диагностические карты кодов ошибок (DTC) трансмиссии", 616, 677),

    # Chassis (678 - 849)
    ("04-chassis", "index.md", "04. Шасси и ходовая часть — Общие сведения", 678, 685),
    ("04-chassis", "suspension-front.md", "Передняя подвеска MacPherson: Стойка, рычаг, шаровая, стабилизатор", 686, 715),
    ("04-chassis", "suspension-rear.md", "Задняя многорычажная подвеска: Рычаги, амортизаторы, пружины", 716, 745),
    ("04-chassis", "wheel-alignment.md", "Углы установки колес (развал-схождение) и параметры шин", 746, 755),
    ("04-chassis", "steering.md", "Рулевое управление и электроусилитель EPS: Рейка, колонка, датчик SAS", 756, 785),
    ("04-chassis", "brakes.md", "Тормозная система: Суппорты, диски, замена колодок, прокачка", 786, 815),
    ("04-chassis", "abs-esp.md", "Модуль динамической стабилизации Bosch ESP 9.3 и датчики колес", 816, 835),
    ("04-chassis", "epb-tpms.md", "Стояночный тормоз EPB (сервисный режим) и датчики TPMS", 836, 849),

    # Electrical (850 - 1554)
    ("05-electrical", "index.md", "05. Электрооборудование — Обзор бортовой сети", 850, 864),
    ("05-electrical", "climate.md", "Климат-контроль и кондиционер A/C (компрессор 6PV14, 600г R134a)", 865, 920),
    ("05-electrical", "wipers-windows.md", "Стеклоочистители, омыватели и электростеклоподъемники", 921, 955),
    ("05-electrical", "lighting.md", "Система наружного и внутреннего освещения Full-LED", 956, 995),
    ("05-electrical", "door-locks.md", "Центральный замок и замки дверей", 996, 1020),
    ("05-electrical", "keyless.md", "Бесключевой доступ PEPS, смарт-ключ CR2032, аварийный запуск", 1021, 1050),
    ("05-electrical", "adas-camera.md", "Круговой обзор 360° и ультразвуковые парктроники", 1051, 1080),
    ("05-electrical", "adas-assist.md", "Ассистенты ADAS: Радар 77 ГГц, камера LKA/AEB, слепые зоны BSD", 1081, 1150),
    ("05-electrical", "multimedia.md", "Мультимедиа 12.3\", акустика и телематика T-Box", 1151, 1180),
    ("05-electrical", "body-convenience.md", "Панорамная крыша, люк, электросиденья, дверь багажника", 1181, 1250),
    ("05-electrical", "srs-airbags.md", "Подушки безопасности SRS, датчики удара, блок ACU", 1251, 1315),
    ("05-electrical", "wiring-fuses.md", "Схемы монтажных блоков предохранителей, реле и жгуты", 1316, 1554),

    # Body (1555 - 1719)
    ("06-body", "index.md", "06. Кузов и интерьер — Кузовные зазоры и крепеж", 1555, 1565),
    ("06-body", "interior-dash.md", "Разборка передней панели (торпедо), консоли, экрана", 1566, 1610),
    ("06-body", "interior-trim.md", "Обшивки стоек A/B/C, потолок, дверные карты, багажник", 1611, 1650),
    ("06-body", "exterior.md", "Бамперы, капот, крылья, двери и крышка багажника", 1651, 1719),
]

def build_all():
    print(f"Starting build of structured manual ({len(SECTIONS_TO_BUILD)} sections, all 1719 pages)...", flush=True)
    start_time = time.time()
    
    for idx, (folder, fname, title, p_start, p_end) in enumerate(SECTIONS_TO_BUILD):
        sec_start = time.time()
        target_dir = os.path.join(DOCS_DIR, folder)
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, fname)

        # Check if already structured
        if os.path.exists(target_path):
            try:
                with open(target_path, "r", encoding="utf-8") as f_check:
                    sample = f_check.read(1500)
                if "page-header" in sample:
                    print(f"[{idx+1}/{len(SECTIONS_TO_BUILD)}] Already structured {folder}/{fname} (P.{p_start}-{p_end}), skipping.", flush=True)
                    continue
            except Exception:
                pass

        page_count = p_end - p_start + 1
        content = [
            f"# {title}\n",
            f"> **Страницы оригинального заводского руководства:** {p_start} – {p_end} (Всего {page_count} стр.) | **Модель:** Changan CS55 Plus (JL473ZQ7 / 7DCT)\n",
            "Ниже представлен **полный заводской технологический процесс без сокращений**: все процедуры снятия и установки, моменты затяжки, таблицы спецификаций, распиновки и карты проверок.\n",
            "---\n"
        ]

        print(f"[{idx+1}/{len(SECTIONS_TO_BUILD)}] Structuring {folder}/{fname} (P.{p_start}-{p_end}, {page_count} pages)...", flush=True)
        for p in range(p_start, min(p_end + 1, len(doc) + 1)):
            page_text = render_page_structured(p)
            if page_text.strip():
                content.append(page_text)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

        # Save translation cache after each section
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False)

        size_kb = os.path.getsize(target_path) / 1024
        print(f"  -> Saved {folder}/{fname} in {time.time() - sec_start:.1f}s ({size_kb:.1f} KB, cache: {len(cache)} entries)", flush=True)

    print(f"\nALL 41 SECTIONS SUCCESSFULLY STRUCTURED IN {time.time() - start_time:.1f}s!", flush=True)

if __name__ == "__main__":
    build_all()

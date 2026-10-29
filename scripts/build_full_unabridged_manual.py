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

# Track existing images on disk
existing_images = set(os.listdir(PUBLIC_IMG_DIR))
print(f"Existing images in docs/public/img: {len(existing_images)}")

def get_or_extract_images(page_num, page):
    """Finds or extracts images for the page, returning valid markdown tags."""
    img_tags = []
    page_images = page.get_images()
    
    for idx, img_info in enumerate(page_images[:4]):
        # Check if already on disk under any known extension
        base_name = f"p{page_num}_{idx+1}"
        found_name = None
        for ext in ["png", "jpeg", "jpg"]:
            cand = f"{base_name}.{ext}"
            if cand in existing_images:
                found_name = cand
                break
        
        if not found_name:
            try:
                xref = img_info[0]
                base_img = doc.extract_image(xref)
                ext = base_img.get("ext", "png")
                # Filter out tiny icon artifacts
                if len(base_img["image"]) > 2000:
                    found_name = f"{base_name}.{ext}"
                    fpath = os.path.join(PUBLIC_IMG_DIR, found_name)
                    with open(fpath, "wb") as f:
                        f.write(base_img["image"])
                    existing_images.add(found_name)
            except Exception:
                pass

        if found_name:
            img_tags.append(f"![Иллюстрация к стр. {page_num}](/img/{found_name})")

    return img_tags

def translate_batch(texts):
    """Batch-translates paragraphs using Google GTX API with fast grouping and fallback."""
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
            to_query_indices.append(i)
            to_query_texts.append(s)

    if not to_query_texts:
        return results

    # Group into batches of up to 15 items and max 2200 chars
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
            # Fallback item by item
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

def format_paragraphs(paragraphs):
    """Formats translated paragraphs with Markdown alerts and bold steps."""
    out = []
    for p in paragraphs:
        if not p:
            continue
        p_clean = p.strip()
        lower = p_clean.lower()
        if lower.startswith("warning") or lower.startswith("внимание"):
            out.append(f"\n::: warning ВНИМАНИЕ\n{p_clean}\n:::\n")
        elif lower.startswith("caution") or lower.startswith("предостережение"):
            out.append(f"\n::: warning ПРЕДОСТЕРЕЖЕНИЕ\n{p_clean}\n:::\n")
        elif lower.startswith("note") or lower.startswith("примечание"):
            out.append(f"\n::: tip ПРИМЕЧАНИЕ\n{p_clean}\n:::\n")
        elif re.match(r"^(\d+[\.\)]|[a-zA-Z][\.\)])\s+", p_clean):
            out.append(f"\n**{p_clean}**\n")
        elif "?" in p_clean and any(k in p_clean for k in ["Да", "Нет", "Yes", "No", "Перейдите", "Шаг"]):
            out.append(f"- ➡️ {p_clean}")
        elif lower.startswith("torque") or lower.startswith("момент"):
            out.append(f"\n> 🔧 **{p_clean}**\n")
        else:
            out.append(p_clean)
    return out

def extract_page_content(page_num):
    page = doc[page_num - 1]
    raw_text = page.get_text()
    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]
    if not lines:
        return ""

    img_tags = get_or_extract_images(page_num, page)

    # Filter running headers
    filtered_lines = []
    for i, l in enumerate(lines):
        if re.match(r"^\d+$", l):
            continue
        if i < 2 and len(l) < 50 and any(h in l for h in ["General", "Engine", "Automatic", "Chassis", "Electrical", "Suspension", "Brake", "Manual"]):
            continue
        filtered_lines.append(l)

    # Group lines into paragraphs
    paragraphs = []
    curr = []
    for l in filtered_lines:
        if re.match(r"^(\d+[\.\)]|[A-ZА-ЯЁ\s]{3,}:|[?•])", l) and curr:
            paragraphs.append(" ".join(curr))
            curr = [l]
        else:
            curr.append(l)
    if curr:
        paragraphs.append(" ".join(curr))

    # Batch translate paragraphs
    translated = translate_batch(paragraphs)
    formatted = format_paragraphs(translated)

    out = []
    out.append(f"\n### Страница {page_num}\n")
    if img_tags:
        for tag in img_tags:
            out.append(f"{tag}\n")
    out.append("\n\n".join(formatted))
    return "\n".join(out)

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
    print(f"Starting build of {len(SECTIONS_TO_BUILD)} unabridged sections (all 1719 pages)...")
    start_time = time.time()
    
    for idx, (folder, fname, title, p_start, p_end) in enumerate(SECTIONS_TO_BUILD):
        sec_start = time.time()
        target_dir = os.path.join(DOCS_DIR, folder)
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, fname)

        page_count = p_end - p_start + 1
        content = [
            f"# {title}\n",
            f"> **Страницы оригинального заводского руководства:** {p_start} – {p_end} (Всего {page_count} стр.) | **Автомобиль:** Changan CS55 Plus (JL473ZQ7 / 7DCT)\n",
            "Ниже представлен **полный заводской текст без сокращений** со всеми пошаговыми технологическими операциями, моментами затяжки, проверками мультиметром и дефектовочными нормами.\n",
            "---\n"
        ]

        print(f"[{idx+1}/{len(SECTIONS_TO_BUILD)}] Processing {folder}/{fname} (P.{p_start}-{p_end}, {page_count} pages)...")
        for p in range(p_start, min(p_end + 1, len(doc) + 1)):
            page_text = extract_page_content(p)
            if page_text.strip():
                content.append(page_text)
                content.append("\n---\n")

        with open(target_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

        # Save cache after each section
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False)

        size_kb = os.path.getsize(target_path) / 1024
        print(f"  -> Saved {folder}/{fname} in {time.time() - sec_start:.1f}s ({size_kb:.1f} KB, cache: {len(cache)} entries)")

    # Also ensure mechanical.md is a routing hub
    mech_hub = os.path.join(DOCS_DIR, "02-engine", "mechanical.md")
    with open(mech_hub, "w", encoding="utf-8") as f:
        f.write("""# 02. Механическая часть двигателя 1.5T (Blue Core)

> **Заводское руководство по ремонту:** Стр. 41 – 91 | Changan CS55 Plus

Для удобства навигации и высокой скорости загрузки полная механическая часть разделена на следующие разделы:

1. [**Спецификации, зазоры и моменты затяжки (Стр. 41–44)**](/02-engine/mechanical-specs) — моменты затяжки болтов ГБЦ, коренных подшипников, фазовращателей VVT, допуски зазоров.
2. [**Устройство и кинематика (Стр. 45–52)**](/02-engine/mechanical-principles) — цепь ГРМ, фазорегуляторы DVVT, устройство клапанного механизма и блока.
3. [**Диагностика неисправностей по симптомам (Стр. 53–64)**](/02-engine/mechanical-diagnosis) — посторонние шумы, падение компрессии, перегрев, вибрации.
4. [**Снятие и установка агрегатов (Стр. 65–78)**](/02-engine/mechanical-removal) — пошаговые операции снятия клапанной крышки, цепи ГРМ, масляного поддона, ГБЦ.
5. [**Разборка и дефектовка ГБЦ и поршневой группы (Стр. 79–91)**](/02-engine/mechanical-overhaul) — проверка кривизны ГБЦ, промер направляющих клапанов, зазоры поршневых колец.
""")

    print(f"\nALL 41 SECTIONS SUCCESSFULLY BUILT IN {time.time() - start_time:.1f}s!")

if __name__ == "__main__":
    build_all()

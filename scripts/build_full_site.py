import os
import re
import json
import fitz

BASE_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PUBLIC_IMG_DIR = os.path.join(DOCS_DIR, "public", "img")
os.makedirs(PUBLIC_IMG_DIR, exist_ok=True)

pdf_path = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"
doc = fitz.open(pdf_path)

print(f"Loaded PDF: {len(doc)} pages")

# Major chapters breakdown by page range
CHAPTER_DEFS = [
    {
        "id": "01-general",
        "title": "01. Общие сведения",
        "folder": "01-general",
        "pages": (1, 34),
        "sections": [
            ("index.md", "Общие сведения и регламент", 1, 4),
            ("safety.md", "Техника безопасности и охрана труда", 4, 13),
            ("standards.md", "Стандарты сервисного обслуживания", 13, 16),
            ("vin.md", "Идентификация (VIN, шильдики)", 17, 18),
            ("lifting-towing.md", "Буксировка, подъем и опоры", 19, 24),
            ("nvh.md", "Шум, вибрация и жесткость (NVH)", 25, 34),
        ]
    },
    {
        "id": "02-engine",
        "title": "02. Двигатель 1.5T Blue Core",
        "folder": "02-engine",
        "pages": (35, 475),
        "sections": [
            ("index.md", "Обзор и общие сведения двигателя", 35, 40),
            ("mechanical.md", "Механическая часть и ГРМ", 41, 91),
            ("lubrication.md", "Система смазки", 92, 110),
            ("cooling.md", "Система охлаждения", 111, 133),
            ("fuel.md", "Топливная система прямого впрыска", 134, 168),
            ("fuel-vapor.md", "Система улавливания паров топлива (EVAP)", 169, 188),
            ("intake.md", "Система впуска и турбонаддув", 189, 206),
            ("exhaust.md", "Выхлопная система", 207, 224),
            ("ignition.md", "Система зажигания", 225, 235),
            ("starting.md", "Система пуска (стартер)", 236, 251),
            ("charging.md", "Система зарядки (генератор и АКБ)", 252, 270),
            ("ecu.md", "Электронное управление двигателем (ECU)", 271, 380),
            ("dtc.md", "Коды неисправностей (DTC) двигателя", 381, 475),
        ]
    },
    {
        "id": "03-transmission",
        "title": "03. Трансмиссия (7DCT)",
        "folder": "03-transmission",
        "pages": (476, 677),
        "sections": [
            ("index.md", "Обзор 7-ступенчатой роботизированной КПП (7DCT)", 476, 485),
            ("specifications.md", "Характеристики, моменты затяжки и масло", 486, 500),
            ("structure.md", "Устройство и гидравлический контур", 501, 530),
            ("electronic-shift.md", "Электронный селектор переключения передач", 531, 565),
            ("service.md", "Снятие, установка и обслуживание КПП", 566, 615),
            ("dtc.md", "Коды неисправностей (DTC) трансмиссии", 616, 677),
        ]
    },
    {
        "id": "04-chassis",
        "title": "04. Шасси и ходовая часть",
        "folder": "04-chassis",
        "pages": (678, 849),
        "sections": [
            ("index.md", "Общие сведения о шасси и геометрия", 678, 685),
            ("suspension-front.md", "Передняя подвеска (MacPherson)", 686, 715),
            ("suspension-rear.md", "Задняя многорычажная подвеска", 716, 745),
            ("wheel-alignment.md", "Углы установки колес (развал-схождение)", 746, 755),
            ("steering.md", "Рулевое управление и электроусилитель (EPS)", 756, 785),
            ("brakes.md", "Тормозная система, суппорты и диски", 786, 815),
            ("abs-esp.md", "Антиблокировочная система (ABS) и ESP", 816, 835),
            ("epb-tpms.md", "Стояночный тормоз (EPB) и контроль давления (TPMS)", 836, 849),
        ]
    },
    {
        "id": "05-electrical",
        "title": "05. Электрооборудование",
        "folder": "05-electrical",
        "pages": (850, 1554),
        "sections": [
            ("index.md", "Обзор электрооборудования и бортовая сеть", 850, 864),
            ("climate.md", "Система вентиляции и кондиционирования (A/C)", 865, 920),
            ("wipers-windows.md", "Стеклоочистители, омыватели и стеклоподъемники", 921, 955),
            ("lighting.md", "Система наружного и внутреннего освещения", 956, 995),
            ("door-locks.md", "Центральный замок и противоугонная система", 996, 1020),
            ("keyless.md", "Система бесключевого доступа (PEPS)", 1021, 1050),
            ("adas-camera.md", "Круговой обзор 360° и парктроники", 1051, 1080),
            ("adas-assist.md", "Системы помощи водителю: слепые зоны, полоса, ACC", 1081, 1150),
            ("multimedia.md", "Мультимедиа, акустика и телематика T-Box", 1151, 1180),
            ("body-convenience.md", "Панорамная крыша, электросиденья и электропривод багажника", 1181, 1250),
            ("srs-airbags.md", "Подушки безопасности и преднатяжители (SRS)", 1251, 1315),
            ("wiring-fuses.md", "Предохранители, реле и жгуты проводов", 1316, 1554),
        ]
    },
    {
        "id": "06-body",
        "title": "06. Кузов и интерьер",
        "folder": "06-body",
        "pages": (1555, 1719),
        "sections": [
            ("index.md", "Кузовные зазоры и крепежные элементы", 1555, 1565),
            ("interior-dash.md", "Приборная панель (торпедо) и консоль", 1566, 1610),
            ("interior-trim.md", "Обшивки стоек, потолок и элементы салона", 1611, 1650),
            ("exterior.md", "Бамперы, капот, двери и крышка багажника", 1651, 1719),
        ]
    }
]

# Extract sample images for each section
saved_images = {}

def extract_page_images(p_num, max_imgs=3):
    p_idx = p_num - 1
    if p_idx < 0 or p_idx >= len(doc):
        return []
    page = doc[p_idx]
    imgs = page.get_images()
    results = []
    for idx, img_info in enumerate(imgs[:max_imgs]):
        xref = img_info[0]
        if xref in saved_images:
            results.append(saved_images[xref])
            continue
        try:
            base_img = doc.extract_image(xref)
            ext = base_img["ext"]
            # skip tiny icon images (< 3KB)
            if len(base_img["image"]) < 3000:
                continue
            fname = f"p{p_num}_{idx+1}.{ext}"
            fpath = os.path.join(PUBLIC_IMG_DIR, fname)
            with open(fpath, "wb") as f:
                f.write(base_img["image"])
            web_path = f"/img/{fname}"
            saved_images[xref] = web_path
            results.append(web_path)
        except Exception as e:
            pass
    return results

# Clean and format text to markdown
def format_content(raw_text, p_start, p_end):
    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]
    out = []
    in_warning = False
    
    for l in lines:
        # Skip pure page numbers
        if re.match(r"^\d+$", l):
            continue
        # Skip running header fragments
        if any(h in l for h in ["General", "Workshop Manual", "Engine control", "Chassis", "Suspension system"]):
            if len(l) < 40:
                continue
        
        # Detect Warnings / Cautions
        if re.match(r"^(warning|caution|danger)[:! ]", l, re.IGNORECASE):
            out.append(f"\n::: warning ВНИМАНИЕ\n{l}\n:::\n")
            continue
        if re.match(r"^(note|notice)[:! ]", l, re.IGNORECASE):
            out.append(f"\n::: tip ПРИМЕЧАНИЕ\n{l}\n:::\n")
            continue
        
        # Detect Headings
        if (len(l) < 60 and (l.isupper() or re.match(r"^[A-Z][a-z]+(\s+[A-Z][a-z]+)*$", l))) and not l.endswith("."):
            out.append(f"\n### {l}\n")
            continue
        
        # Detect Torque values
        if "n.m" in l.lower() or "n·m" in l.lower():
            l_t = re.sub(r"(\d+(?:\.\d+)?)\s*(?:N\.m|N·m)", r"**\1 Н·м**", l, flags=re.IGNORECASE)
            out.append(f"- 🔧 {l_t}")
            continue
            
        # Detect Steps
        if re.match(r"^\d+[\.\)]\s+", l):
            out.append(f"\n{l}")
            continue
            
        out.append(l)
        
    return "\n".join(out)

print("Starting documentation generation...")

# Generate all pages
for chap in CHAPTER_DEFS:
    chap_dir = os.path.join(DOCS_DIR, chap["folder"])
    os.makedirs(chap_dir, exist_ok=True)
    
    for filename, title, p_start, p_end in chap["sections"]:
        file_path = os.path.join(chap_dir, filename)
        
        # Aggregate text and images from page range
        raw_chunks = []
        page_images = []
        
        for p in range(p_start, min(p_end + 1, len(doc) + 1)):
            t = doc[p - 1].get_text()
            if t.strip():
                raw_chunks.append(t)
            imgs = extract_page_images(p, max_imgs=2)
            page_images.extend(imgs)
            
        full_raw = "\n".join(raw_chunks)
        formatted_body = format_content(full_raw, p_start, p_end)
        
        # Build Markdown
        md = []
        md.append(f"# {title}\n")
        md.append(f"> **Страницы в оригинале:** {p_start} – {p_end} | **Модель:** Changan CS55 Plus (2-е поколение / Plus)\n")
        
        # Insert image gallery if any images found
        if page_images:
            md.append("## Схемы и иллюстрации раздела\n")
            md.append("<div style=\"display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;\">")
            for img_url in page_images[:6]:
                md.append(f"  <a href=\"{img_url}\" target=\"_blank\" style=\"border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);\">")
                md.append(f"    <img src=\"{img_url}\" alt=\"Иллюстрация\" style=\"max-height: 180px; width: auto; object-fit: contain;\" />")
                md.append(f"  </a>")
            md.append("</div>\n")
        
        md.append("## Содержание и процедуры\n")
        md.append(formatted_body[:8000]) # Cap to readable size per page
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md))
            
print("Generated all chapter pages.")

# Generate DTC Table Page
dtc_dir = os.path.join(DOCS_DIR, "07-dtc")
os.makedirs(dtc_dir, exist_ok=True)

dtc_md = """# Справочник кодов неисправностей (DTC)

> Данный справочник содержит коды ошибок электронных блоков Changan CS55 Plus:
> ЭБУ двигателя (ECU/ECM), блока трансмиссии (TCU), системы стабилизации и тормозов (ESP/ABS), кузовной электроники (BCM) и ассистентов водителя (ADAS).

## Быстрый поиск по коду ошибки

Воспользуйтесь строкой поиска в шапке сайта (нажмите <kbd>Ctrl</kbd> + <kbd>K</kbd>) для мгновенного перехода к алгоритму проверки любого кода.

| Код DTC | Описание неисправности (RU) | Английское наименование | Основная причина / Узел |
|---------|-----------------------------|-------------------------|--------------------------|
| **P0011** | Нарушение фаз газораспределения впускного распредвала | Intake Camshaft Position Timing - Over-Advanced (Bank 1) | Клапан VVT, давление масла, метки цепи ГРМ |
| **P0016** | Несоответствие сигналов датчиков коленвала и впускного распредвала | Crankshaft Position - Camshaft Position Correlation | Растяжение цепи ГРМ, датчик фаз, датчик коленвала |
| **P0087** | Слишком низкое давление в топливной рампе | Fuel Rail/System Pressure - Too Low | ТНВД прямого впрыска, подкачной насос в баке, датчик давления |
| **P0100** | Неисправность цепи датчика массового расхода воздуха (MAF) | Mass or Volume Air Flow Circuit Malfunction | Датчик MAF/MAP, подсос воздуха, обрыв проводки |
| **P0113** | Высокий уровень сигнала датчика температуры воздуха на впуске | Intake Air Temperature Sensor 1 Circuit High | Датчик температуры впуска (IAT), обрыв сигнального провода |
| **P0118** | Высокий уровень сигнала датчика температуры охлаждающей жидкости (ECT) | Engine Coolant Temperature Sensor 1 Circuit High | Датчик температуры ОЖ, термостат, обрыв цепи |
| **P0130** | Неисправность цепи переднего датчика кислорода (Bank 1, Sensor 1) | O2 Sensor Circuit Malfunction (Bank 1 Sensor 1) | Лямбда-зонд до нейтрализатора, жгут проводки |
| **P0171** | Слишком бедная топливовоздушная смесь | System Too Lean (Bank 1) | Подсос воздуха, форсунки, давление топлива, датчик MAF/MAP |
| **P0172** | Слишком богатая топливовоздушная смесь | System Too Rich (Bank 1) | Течь форсунок, залипание клапана EVAP, датчик давления топлива |
| **P0299** | Недостаточное давление наддува турбокомпрессора | Turbocharger/Supercharger Underboost | Актуатор турбины, патрубки интеркулера, клапан сброса байпас |
| **P0300** | Обнаружены случайные/множественные пропуски зажигания | Random/Multiple Cylinder Misfire Detected | Свечи зажигания, индивидуальные катушки, форсунки, компрессия |
| **P0301** | Пропуски зажигания в цилиндре 1 | Cylinder 1 Misfire Detected | Свеча зажигания цил. 1, катушка цил. 1, форсунка |
| **P0302** | Пропуски зажигания в цилиндре 2 | Cylinder 2 Misfire Detected | Свеча зажигания цил. 2, катушка цил. 2, форсунка |
| **P0303** | Пропуски зажигания в цилиндре 3 | Cylinder 3 Misfire Detected | Свеча зажигания цил. 3, катушка цил. 3, форсунка |
| **P0304** | Пропуски зажигания в цилиндре 4 | Cylinder 4 Misfire Detected | Свеча зажигания цил. 4, катушка цил. 4, форсунка |
| **P0500** | Неисправность датчика скорости автомобиля | Vehicle Speed Sensor Malfunction | Датчики скорости колес (ABS), шина CAN |
| **P0700** | Запрос включения индикатора неисправности от блока КПП (TCU) | Transmission Control System (MIL Request) | Проверьте сохраненные коды ошибок в блоке коробки передач |
| **P0841** | Ошибка диапазона/характеристик датчика давления рабочей жидкости КПП | Transmission Fluid Pressure Sensor/Switch "A" Circuit | Датчик давления масла 7DCT, соленоид гидроблока |
| **P1700** | Общая системная ошибка блока управления трансмиссией | Transmission Control Module Error | Внутренняя ошибка контроллера TCU / калибровка сцеплений |
| **C0010** | Ошибка клапана ABS переднего левого колеса | Left Front Inlet ABS Valve Control | Гидроблок ABS/ESP, проводка клапана |
| **C0031** | Неисправность датчика скорости переднего левого колеса | Left Front Wheel Speed Sensor | Датчик ABS, ступичный подшипник (магнитное кольцо) |
| **C0034** | Неисправность датчика скорости переднего правого колеса | Right Front Wheel Speed Sensor | Датчик ABS, проводка датчика правого колеса |
| **U0100** | Потеря связи с блоком управления двигателем (ECM/ECU) | Lost Communication With ECM/PCM "A" | Шина CAN-H / CAN-L, питание ЭБУ двигателя |
| **U0101** | Потеря связи с блоком управления трансмиссией (TCU) | Lost Communication with TCM | Шина CAN, разъем блока управления 7DCT |
| **U0121** | Потеря связи с блоком антиблокировочной системы (ABS/ESP) | Lost Communication With Anti-Lock Brake System (ABS) | Шина CAN, разъем блока ABS/ESP |
| **U0140** | Потеря связи с блоком кузовной электроники (BCM) | Lost Communication With Body Control Module | Шина данных CAN кузова, предохранитель BCM |
| **B1400** | Ошибка цепи датчика фронтального удара водителя | Driver Front Impact Sensor Circuit | Датчик удара на передней панели, проводка SRS |
| **B1401** | Ошибка пиропатрона подушки безопасности водителя | Driver Airbag Igniter Circuit | Подрулевой шлейф («улитка»), подушка безопасности в руле |
"""

with open(os.path.join(dtc_dir, "index.md"), "w", encoding="utf-8") as f:
    f.write(dtc_md)

print("Generated DTC reference table.")

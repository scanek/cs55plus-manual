import os
import re
import json
import fitz

BASE_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PDF_PATH = r"C:\Users\Александр Щеголев\Downloads\CS55PLUS Workshop Manual.pdf"

doc = fitz.open(PDF_PATH)
print(f"Loaded PDF: {len(doc)} pages")

# Dictionary of technical automotive terms for natural Russian translation
PHRASE_REPLACEMENTS = [
    # Common actions and steps
    (r"\bRemoval and installation\b", "Снятие и установка"),
    (r"\bDisassembly and assembly\b", "Разборка и сборка"),
    (r"\bInspection of part structure principle\b", "Устройство и принцип работы компонентов"),
    (r"\bFault symptom diagnosis\b", "Диагностика симптомов неисправностей"),
    (r"\bCommon methods\b", "Общие методы проверки и регулировки"),
    (r"\bSpecifications\b", "Технические характеристики"),
    (r"\bComposition and position distribution\b", "Состав и расположение компонентов"),
    (r"\bSystem functional principle introduction\b", "Принцип работы системы"),
    (r"\bTest conditions\b", "Условия проверки"),
    (r"\bDetails/Results/Measures\b", "Действия / Результат / Мера устранения"),
    (r"\bDisconnect the battery negative cable\b", "Отсоедините отрицательную клемму аккумуляторной батареи"),
    (r"\bConnect the battery negative cable\b", "Подсоедините отрицательную клемму аккумуляторной батареи"),
    (r"\bTurn the ignition switch to the \"ON\" position\b", "Включите зажигание (положение \"ON\")"),
    (r"\bTurn the ignition switch to the \"LOCK\" position\b", "Выключите зажигание (положение \"LOCK\")"),
    (r"\bTurn the ignition switch to \"ON\" position\b", "Включите зажигание (положение \"ON\")"),
    (r"\bTurn the ignition switch to \"LOCK\" position\b", "Выключите зажигание (положение \"LOCK\")"),
    (r"\bConnect diagnostic scanner\b", "Подключите диагностический сканер"),
    (r"\bStandard resistance\b", "Эталонное сопротивление"),
    (r"\bStandard voltage\b", "Эталонное напряжение"),
    (r"\bMeasure the resistance between\b", "Измерьте сопротивление между"),
    (r"\bMeasure the voltage between\b", "Измерьте напряжение между"),
    (r"\bWhether the resistance is\b", "Соответствует ли сопротивление норме"),
    (r"\bWhether the voltage is\b", "Соответствует ли напряжение норме"),
    (r"\bRepair or replace\b", "Отремонтируйте или замените"),
    (r"\bReplace the\b", "Замените"),
    (r"\bGo to step\b", "Перейдите к шагу"),
    (r"\bGo to Step\b", "Перейдите к шагу"),
    (r"\bYes\b", "Да"),
    (r"\bNo\b", "Нет"),
    (r"\bWarning\b", "ВНИМАНИЕ"),
    (r"\bCaution\b", "ПРЕДОСТЕРЕЖЕНИЕ"),
    (r"\bNote\b", "ПРИМЕЧАНИЕ"),
    (r"\bAttention\b", "Внимание"),
    (r"\bCylinder head\b", "Головка блока цилиндров (ГБЦ)"),
    (r"\bCylinder block\b", "Блок цилиндров"),
    (r"\bCrankshaft\b", "Коленчатый вал"),
    (r"\bCamshaft\b", "Распределительный вал"),
    (r"\bPiston\b", "Поршень"),
    (r"\bConnecting rod\b", "Шатун"),
    (r"\bTiming chain\b", "Цепь ГРМ"),
    (r"\bTensioner\b", "Натяжитель"),
    (r"\bSpark plug\b", "Свеча зажигания"),
    (r"\bIgnition coil\b", "Катушка зажигания"),
    (r"\bFuel injector\b", "Топливная форсунка"),
    (r"\bFuel pump\b", "Топливный насос"),
    (r"\bWater pump\b", "Водяной насос (помпа)"),
    (r"\bOil pump\b", "Масляный насос"),
    (r"\bOil pan\b", "Масляный поддон картера"),
    (r"\bTurbocharger\b", "Турбокомпрессор"),
    (r"\bIntercooler\b", "Охладитель наддувочного воздуха (интеркулер)"),
    (r"\bThrottle\b", "Дроссельная заслонка"),
    (r"\bFlywheel\b", "Маховик"),
    (r"\bDrive shaft\b", "Приводной вал (привод колеса / ШРУС)"),
    (r"\bBrake caliper\b", "Тормозной суппорт"),
    (r"\bBrake disc\b", "Тормозной диск"),
    (r"\bBrake pad\b", "Тормозная колодка"),
    (r"\bWheel speed sensor\b", "Датчик скорости колеса (ABS)"),
    (r"\bSteering gear\b", "Рулевая рейка (механизм)"),
    (r"\bFront stabilizer bar\b", "Передний стабилизатор поперечной устойчивости"),
    (r"\bFront strut\b", "Передняя амортизаторная стойка"),
    (r"\bControl arm\b", "Рычаг подвески"),
    (r"\bBall joint\b", "Шаровая опора"),
    (r"\bSubframe\b", "Подрамник"),
    (r"\bTightening torque\b", "Момент затяжки"),
    (r"\bTorque\b", "Момент затяжки"),
    (r"\bN·m\b", "Н·м"),
    (r"\bN\.m\b", "Н·м"),
    (r"\bInstallation\b", "Установка"),
    (r"\bRemoval\b", "Снятие"),
    (r"\bDisassembly\b", "Разборка"),
    (r"\bAssembly\b", "Сборка"),
]

def translate_line(line):
    res = line
    for pat, rep in PHRASE_REPLACEMENTS:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)
    return res

def clean_and_format_page(page_num):
    page = doc[page_num - 1]
    raw = page.get_text()
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    if not lines:
        return ""
    
    # Extract images on this page
    page_img_tags = []
    for idx, img_info in enumerate(page.get_images()[:3]):
        xref = img_info[0]
        try:
            base_img = doc.extract_image(xref)
            ext = base_img["ext"]
            if len(base_img["image"]) > 2000:
                fname = f"p{page_num}_{idx+1}.{ext}"
                fpath = os.path.join(DOCS_DIR, "public", "img", fname)
                if not os.path.exists(fpath):
                    with open(fpath, "wb") as f:
                        f.write(base_img["image"])
                page_img_tags.append(f"![Иллюстрация к шагу](/img/{fname})")
        except Exception:
            pass

    out_lines = []
    out_lines.append(f"\n### [Оригинальная стр. {page_num}]\n")
    
    if page_img_tags:
        out_lines.append("<div style=\"display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0;\">")
        for tag in page_img_tags:
            out_lines.append(f"  <div style=\"max-width: 48%; border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 4px; background: var(--vp-c-bg-soft);\">{tag}</div>")
        out_lines.append("</div>\n")
        
    for l in lines:
        # Skip pure page numbers
        if re.match(r"^\d+$", l):
            continue
        # Skip top running header lines
        if len(l) < 45 and any(h in l for h in ["Mechanical system", "Removal and installation", "General", "Workshop Manual", "Engine control", "Chassis", "Electrical"]):
            continue
            
        translated = translate_line(l)
        
        # Format warnings
        if re.match(r"^(warning|внимание)", translated, re.IGNORECASE):
            out_lines.append(f"\n::: warning ВНИМАНИЕ\n{translated}\n:::\n")
            continue
        if re.match(r"^(caution|предостережение)", translated, re.IGNORECASE):
            out_lines.append(f"\n::: warning ПРЕДОСТЕРЕЖЕНИЕ\n{translated}\n:::\n")
            continue
        if re.match(r"^(note|примечание)", translated, re.IGNORECASE):
            out_lines.append(f"\n::: tip ПРИМЕЧАНИЕ\n{translated}\n:::\n")
            continue
            
        # Format numbered steps
        if re.match(r"^\d+[\.\)]\s*", translated):
            out_lines.append(f"\n**{translated}**")
            continue
            
        # Format torque values
        if "Н·м" in translated or "N·m" in translated:
            out_lines.append(f"- 🔧 `{translated}`")
            continue
            
        out_lines.append(translated)
        
    return "\n".join(out_lines)

print("Page formatter ready.")

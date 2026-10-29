# Электрооборудование автомобиля — Общие сведения

> **Страницы в оригинале:** 850 – 864 | **Модель:** Changan CS55 Plus (Второе поколение)

## Архитектура бортовой сети автомобиля

<div style="display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0;">
  <a href="/img/p856_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p856_1.jpeg" alt="Расположение блоков климат-контроля" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
  <a href="/img/p858_1.jpeg" target="_blank" style="border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 4px; display: inline-block; background: var(--vp-c-bg-soft);">
    <img src="/img/p858_1.jpeg" alt="Схема циркуляции хладагента A/C" style="max-height: 180px; width: auto; object-fit: contain;" />
  </a>
</div>

---

## 1. Общие характеристики бортовой сети

* **Номинальное напряжение:** 12 В (постоянный ток, масса на кузове автомобиля).
* **Рабочий диапазон напряжения:** 11.5 В – 14.8 В при работающем генераторе.
* **Шины передачи данных:**
  * **CAN-C (High-Speed CAN, 500 кбит/с):** моторный отсек и безопасность (ЭБУ двигателя, КПП 7DCT, блок ESP/ABS, датчик угла руля, блок подушек SRS).
  * **CAN-B (Body CAN, 250 кбит/с):** комфорт и кузовная электроника (блок BCM, приборная панель, мультимедиа, климат-контроль, двери).
  * **LIN-bus (локальная сеть, 19.2 кбит/с):** стеклоочистители, генератор, датчик дождя и света, датчик АКБ.

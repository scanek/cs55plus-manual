<script setup>
import { ref, computed } from 'vue'

const selectedKm = ref(10000)

const intervals = [
  { km: 10000, name: 'ТО-1 (10 000 км / 12 мес)' },
  { km: 20000, name: 'ТО-2 (20 000 км / 24 мес)' },
  { km: 30000, name: 'ТО-3 (30 000 км / 36 мес)' },
  { km: 40000, name: 'ТО-4 (40 000 км / 48 мес)' },
  { km: 50000, name: 'ТО-5 (50 000 км / 60 мес)' },
  { km: 60000, name: 'ТО-6 (60 000 км / 72 мес — Большое ТО)' },
  { km: 80000, name: 'ТО-8 (80 000 км / 96 мес)' },
  { km: 100000, name: 'ТО-10 (100 000 км / 120 мес)' }
]

const maintenanceSchedule = {
  10000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP / ILSAC GF-6A', qty: '3.8 – 4.0 л', note: 'Оригинальное синтетическое маловязкое масло' },
      { item: 'Масляный фильтр двигателя', qty: '1 шт.', note: 'Замена кольца O-ring, момент затяжки 18 Н·м' },
      { item: 'Уплотнительная шайба сливной пробки поддона', qty: '1 шт.', note: 'Момент затяжки пробки 55 Н·м' },
      { item: 'Фильтр системы кондиционирования и вентиляции (салонный)', qty: '1 шт.', note: 'Угольный антибактериальный' }
    ],
    checks: [
      'Проверка толщины тормозных колодок (передние мин. 2.0 мм, задние мин. 2.0 мм)',
      'Проверка уровня тормозной жидкости DOT 4 и антифриза',
      'Проверка давления в шинах (220 кПа / 2.2 бар) и момента колесных гаек (125 Н·м)',
      'Осмотр пыльников ШРУС, рулевых наконечников и стоек стабилизатора'
    ]
  },
  20000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр с кольцом', qty: '1 шт.', note: 'Замена' },
      { item: 'Шайба пробки поддона', qty: '1 шт.', note: 'Замена' },
      { item: 'Воздушный фильтр двигателя', qty: '1 шт.', note: 'Замена' },
      { item: 'Салонный фильтр кондиционера', qty: '1 шт.', note: 'Замена' },
      { item: 'Тормозная жидкость DOT 4', qty: '1.0 л', note: 'Полная замена и прокачка гидравлической системы' }
    ],
    checks: [
      'Проверка приводного ремня навесных агрегатов',
      'Осмотр выхлопной системы и подвесов глушителя',
      'Проверка АКБ и плотности электролита тестером',
      'Диагностика электронных блоков сканером (считывание кодов DTC)'
    ]
  },
  30000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр двигателя', qty: '1 шт.', note: 'Замена' },
      { item: 'Салонный фильтр', qty: '1 шт.', note: 'Замена' }
    ],
    checks: [
      'Проверка состояния свечей зажигания (зазор 0.75–0.85 мм)',
      'Проверка углов установки колес (развал-схождение)',
      'Осмотр радиаторов охлаждения и интеркулера на предмет загрязнения'
    ]
  },
  40000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Воздушный и салонный фильтры', qty: '2 шт.', note: 'Замена комплектом' },
      { item: 'Свечи зажигания иридиевые (Iridium)', qty: '4 шт.', note: 'Момент затяжки 20 Н·м на холодном двигателе' },
      { item: 'Тормозная жидкость DOT 4', qty: '1.0 л', note: 'Замена' }
    ],
    checks: [
      'Проверка износа тормозных дисков (перед мин. 26 мм, зад мин. 10 мм)',
      'Проверка сайлентблоков передней и задней подвески',
      'Проверка уровня трансмиссионного масла в коробке 7DCT при 40–50 °C'
    ]
  },
  50000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Салонный фильтр', qty: '1 шт.', note: 'Замена' }
    ],
    checks: [
      'Проверка ремня генератора и натяжного ролика',
      'Диагностика амортизаторов на стенде или осмотр на потеки масла',
      'Проверка батарейки в ключе PEPS (CR2032)'
    ]
  },
  60000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Трансмиссионное масло 7DCT (BOT 351 C4)', qty: '5.3 л', note: 'Полная замена в роботизированной коробке' },
      { item: 'Воздушный фильтр двигателя', qty: '1 шт.', note: 'Замена' },
      { item: 'Салонный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Свечи зажигания (иридиевые)', qty: '4 шт.', note: 'Замена' },
      { item: 'Тормозная жидкость DOT 4', qty: '1.0 л', note: 'Замена' },
      { item: 'Охлаждающая жидкость (Антифриз G12+)', qty: '6.5 л', note: 'Полный слив и заливка нового состава' },
      { item: 'Приводной ремень генератора и компрессора (6PK)', qty: '1 шт.', note: 'Замена вместе с натяжным роликом (50 Н·м)' }
    ],
    checks: [
      'Калибровка точек касания сцеплений 7DCT через сканер',
      'Полная ревизия подвески, протяжка болтов подрамника (140 Н·м)',
      'Проверка герметичности сальников приводов и коленвала'
    ]
  },
  80000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Воздушный и салонный фильтры', qty: '2 шт.', note: 'Замена' },
      { item: 'Свечи зажигания', qty: '4 шт.', note: 'Замена' },
      { item: 'Тормозная жидкость DOT 4', qty: '1.0 л', note: 'Замена' }
    ],
    checks: [
      'Проверка состояния цепи ГРМ и угла рассогласования фаз по сканеру',
      'Проверка сайлентблоков продольных рычагов задней подвески'
    ]
  },
  100000: {
    replacements: [
      { item: 'Моторное масло SAE 0W-20 API SP', qty: '3.8 – 4.0 л', note: 'Замена' },
      { item: 'Масляный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Салонный фильтр', qty: '1 шт.', note: 'Замена' },
      { item: 'Охлаждающая жидкость (Антифриз G12+)', qty: '6.5 л', note: 'Замена' }
    ],
    checks: [
      'Комплексная диагностика турбокомпрессора и люфта актуатора Wastegate',
      'Проверка компрессии в цилиндрах 1.5T',
      'Проверка насоса ТНВД и давления в рампе (норма 40–350 бар)'
    ]
  }
}

const currentPlan = computed(() => {
  return maintenanceSchedule[selectedKm.value] || maintenanceSchedule[10000]
})

const checkedItems = ref({})

const toggleCheck = (idx) => {
  checkedItems.value[idx] = !checkedItems.value[idx]
}

const printPlan = () => {
  if (typeof window !== 'undefined') {
    window.print()
  }
}
</script>

<template>
  <div class="maint-calc">
    <div class="selector-card no-print">
      <label class="label">Выберите текущий пробег автомобиля:</label>
      <div class="btn-group">
        <button 
          v-for="int in intervals" 
          :key="int.km"
          class="km-btn"
          :class="{ active: selectedKm === int.km }"
          @click="selectedKm = int.km; checkedItems = {}"
        >
          {{ (int.km / 1000) }} тыс. км
        </button>
      </div>
    </div>

    <div class="plan-card">
      <div class="plan-header">
        <h2>Регламентные работы для: {{ intervals.find(i => i.km === selectedKm)?.name }}</h2>
        <button class="print-plan-btn no-print" @click="printPlan">
          🖨️ Распечатать чек-лист
        </button>
      </div>

      <h3>🔧 Обязательные расходные материалы и замена:</h3>
      <table class="maint-table">
        <thead>
          <tr>
            <th style="width: 40px;">✓</th>
            <th>Расходный материал / Деталь</th>
            <th style="width: 110px;">Количество</th>
            <th>Примечание / Спецификация</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="(r, idx) in currentPlan.replacements" 
            :key="idx"
            :class="{ completed: checkedItems['r_' + idx] }"
            @click="toggleCheck('r_' + idx)"
            style="cursor: pointer;"
          >
            <td style="text-align: center;">
              <input type="checkbox" :checked="checkedItems['r_' + idx]" />
            </td>
            <td><strong>{{ r.item }}</strong></td>
            <td><code>{{ r.qty }}</code></td>
            <td>{{ r.note }}</td>
          </tr>
        </tbody>
      </table>

      <h3 style="margin-top: 24px;">🔍 Обязательные контрольно-осмотровые проверки:</h3>
      <ul class="checks-list">
        <li 
          v-for="(c, cidx) in currentPlan.checks" 
          :key="cidx"
          :class="{ completed: checkedItems['c_' + cidx] }"
          @click="toggleCheck('c_' + cidx)"
          style="cursor: pointer;"
        >
          <input type="checkbox" :checked="checkedItems['c_' + cidx]" style="margin-right: 8px;" />
          <span>{{ c }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.maint-calc {
  margin: 20px 0;
}

.selector-card {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 24px;
}

.label {
  display: block;
  font-weight: 600;
  margin-bottom: 12px;
}

.btn-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.km-btn {
  padding: 8px 14px;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.km-btn:hover {
  border-color: var(--vp-c-brand-1);
}

.km-btn.active {
  background: var(--vp-c-brand-1);
  color: #ffffff;
  border-color: var(--vp-c-brand-1);
}

.plan-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.print-plan-btn {
  padding: 6px 14px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
}

.maint-table {
  width: 100%;
  border-collapse: collapse;
}

.completed {
  opacity: 0.5;
  text-decoration: line-through;
}

.checks-list {
  list-style: none;
  padding: 0;
}

.checks-list li {
  padding: 8px 12px;
  border-bottom: 1px solid var(--vp-c-divider);
  display: flex;
  align-items: center;
}
</style>

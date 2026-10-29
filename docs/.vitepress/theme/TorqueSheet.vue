<script setup>
import { ref, computed } from 'vue'

const activeCategory = ref('all')
const searchQuery = ref('')

const torqueData = [
  // Двигатель и ГРМ
  { cat: 'engine', part: 'Болты крепления ГБЦ', torque: '25 Н·м + 180°', note: 'Затяжка в 3 этапа: 25 Н·м, затем +90°, затем +90° от центра по спирали' },
  { cat: 'engine', part: 'Болт демпферного шкива коленвала', torque: '120 Н·м + 135°', note: 'Использовать спецфиксатор маховика' },
  { cat: 'engine', part: 'Болты маховика к коленвалу', torque: '40 Н·м + 45°', note: 'Нанести резьбовой герметик' },
  { cat: 'engine', part: 'Болты передней крышки ГРМ к ГБЦ', torque: '50 Н·м', note: 'Болты M10' },
  { cat: 'engine', part: 'Болты передней крышки ГРМ к блоку', torque: '23 Н·м', note: 'Болты M8' },
  { cat: 'engine', part: 'Болты клапанной крышки', torque: '10 Н·м', note: 'От центра к краям' },
  { cat: 'engine', part: 'Болты масляного поддона', torque: '10 Н·м', note: 'Равномерно крест-накрест' },
  { cat: 'engine', part: 'Сливная пробка поддона двигателя', torque: '55 Н·м', note: 'Обязательная замена медной шайбы' },
  { cat: 'engine', part: 'Масляный фильтр двигателя', torque: '18 Н·м', note: 'Смазать уплотнительное кольцо маслом' },
  { cat: 'engine', part: 'Свечи зажигания (иридиевые)', torque: '20 Н·м', note: 'Строго на остывшем двигателе' },
  { cat: 'engine', part: 'Болты катушек зажигания', torque: '10 Н·м', note: 'Болты M6' },
  { cat: 'engine', part: 'Болты водяного насоса (помпы)', torque: '40 Н·м', note: 'Болты M10' },
  { cat: 'engine', part: 'Болты масляного насоса', torque: '23 Н·м', note: 'Болты M8' },
  { cat: 'engine', part: 'Датчик детонации (KS)', torque: '20 Н·м', note: 'Недотяг/перетяг искажает показания' },
  { cat: 'engine', part: 'Болты ТНВД к ГБЦ', torque: '23 Н·м', note: 'Крепление ТНВД прямого впрыска' },
  { cat: 'engine', part: 'Штуцеры топливных трубок высокого давления', torque: '30 Н·м', note: 'Топливная рампа 350 бар' },
  { cat: 'engine', part: 'Крепление турбокомпрессора к ГБЦ', torque: '45 Н·м', note: 'Омедненные жаропрочные гайки' },
  { cat: 'engine', part: 'Дроссельная заслонка', torque: '10 Н·м', note: 'Болты к пластиковому коллектору' },
  { cat: 'engine', part: 'Кислородные датчики (лямбда-зонды)', torque: '45 Н·м', note: 'Высокотемпературная противозадирная паста' },

  // Трансмиссия 7DCT
  { cat: 'trans', part: 'Заливная резьбовая пробка коробки 7DCT', torque: '40 Н·м', note: 'Шестигранник, верхняя часть' },
  { cat: 'trans', part: 'Контрольная (переливная) пробка уровня масла', torque: '25 Н·м', note: 'Проверка при температуре 40–50 °C' },
  { cat: 'trans', part: 'Сливная пробка картера 7DCT', torque: '40 Н·м', note: 'Магнитная пробка, очистить от стружки' },
  { cat: 'trans', part: 'Болты крепления КПП к двигателю (M12)', torque: '75 Н·м', note: 'По контуру колокола' },
  { cat: 'trans', part: 'Болты крепления КПП к двигателю (M10)', torque: '45 Н·м', note: 'Верхние и нижние' },
  { cat: 'trans', part: 'Болты стартера к картеру КПП', torque: '45 Н·м', note: '2 болта' },
  { cat: 'trans', part: 'Левая опора трансмиссии к кронштейну', torque: '65 Н·м', note: 'Подушка коробки передач' },

  // Подвеска и Шасси
  { cat: 'chassis', part: 'Гайка штока переднего амортизатора', torque: '65 Н·м', note: 'Удерживать шток от проворачивания' },
  { cat: 'chassis', part: 'Гайки верхней опоры стойки к кузову', torque: '45 Н·м', note: '3 гайки на стакане' },
  { cat: 'chassis', part: 'Болты стойки MacPherson к кулаку', torque: '120 Н·м', note: '2 болта M14 с гайками' },
  { cat: 'chassis', part: 'Гайка пальца передней шаровой опоры', torque: '70 Н·м', note: 'Конусный палец к кулаку' },
  { cat: 'chassis', part: 'Передний горизонтальный сайлентблок рычага', torque: '110 Н·м', note: 'Затягивать строго под нагрузкой на колесах!' },
  { cat: 'chassis', part: 'Задний вертикальный сайлентблок рычага', torque: '140 Н·м', note: 'Затягивать строго под нагрузкой на колесах!' },
  { cat: 'chassis', part: 'Стойки переднего стабилизатора («косточки»)', torque: '45 Н·м', note: 'Палец стабилизатора' },
  { cat: 'chassis', part: 'Скобы втулок стабилизатора к подрамнику', torque: '35 Н·м', note: 'Болты M10' },
  { cat: 'chassis', part: 'Основные болты подрамника к кузову', torque: '140 Н·м', note: '4 мощных силовых болта' },
  { cat: 'chassis', part: 'Болт продольного рычага задней подвески', torque: '120 Н·м', note: 'Затягивать на колесах' },
  { cat: 'chassis', part: 'Болты поперечных рычагов задней подвески', torque: '90 Н·м', note: 'Затягивать на колесах' },
  { cat: 'chassis', part: 'Эксцентриковый болт схождения сзади', torque: '90 Н·м', note: 'Регулировочный болт' },
  { cat: 'chassis', part: 'Нижний болт заднего амортизатора', torque: '110 Н·м', note: 'К заднему кулаку' },

  // Рулевое и тормоза
  { cat: 'brakes', part: 'Колесные гайки крепления колеса', torque: '125 Н·м', note: 'В 2 этапа крест-накрест (60 Н·м -> 125 Н·м)' },
  { cat: 'brakes', part: 'Скоба переднего тормозного суппорта к кулаку', torque: '110 Н·м', note: 'Болты скобы' },
  { cat: 'brakes', part: 'Направляющие пальцы переднего суппорта', torque: '35 Н·м', note: 'Смазать направляющие' },
  { cat: 'brakes', part: 'Скоба заднего тормозного суппорта', torque: '85 Н·м', note: 'Болты скобы' },
  { cat: 'brakes', part: 'Направляющие пальцы заднего суппорта', torque: '30 Н·м', note: 'Суппорт с электроручником EPB' },
  { cat: 'brakes', part: 'Банджо-болт тормозного шланга к суппорту', torque: '30 Н·м', note: 'Новые медные уплотнительные шайбы' },
  { cat: 'brakes', part: 'Болты рулевой рейки к подрамнику', torque: '90 Н·м', note: 'Крепление рейки' },
  { cat: 'brakes', part: 'Наконечник рулевой тяги к кулаку', torque: '45 Н·м', note: 'Конусный палец' },
  { cat: 'brakes', part: 'Контргайка регулировки схождения тяги', torque: '65 Н·м', note: 'Фиксация рулевой тяги' }
]

const categories = [
  { id: 'all', name: 'Все узлы (сводная)' },
  { id: 'engine', name: '⚙️ Двигатель и ГРМ' },
  { id: 'trans', name: '🔄 Трансмиссия 7DCT' },
  { id: 'chassis', name: '🚗 Подвеска и Шасси' },
  { id: 'brakes', name: '🛑 Тормоза, колеса, рулевое' },
]

const filteredItems = computed(() => {
  return torqueData.filter(item => {
    const matchesCat = activeCategory.value === 'all' || item.cat === activeCategory.value
    const matchesSearch = !searchQuery.value.trim() || 
      item.part.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      item.torque.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      item.note.toLowerCase().includes(searchQuery.value.toLowerCase())
    return matchesCat && matchesSearch
  })
})
</script>

<template>
  <div class="torque-container">
    <div class="controls no-print">
      <input 
        v-model="searchQuery" 
        type="text" 
        class="search-input" 
        placeholder="Быстрый поиск детали или усилия (например, ГБЦ, колесо, 25, суппорт)..." 
      />

      <div class="filter-tabs">
        <button 
          v-for="cat in categories" 
          :key="cat.id"
          class="tab-btn"
          :class="{ active: activeCategory === cat.id }"
          @click="activeCategory = cat.id"
        >
          {{ cat.name }}
        </button>
      </div>
    </div>

    <table class="torque-table">
      <thead>
        <tr>
          <th>Узел / Резьбовое соединение</th>
          <th style="width: 170px;">Момент затяжки</th>
          <th>Особенности затяжки / Примечание</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, idx) in filteredItems" :key="idx">
          <td><strong>{{ item.part }}</strong></td>
          <td>
            <span class="torque-badge">🔧 {{ item.torque }}</span>
          </td>
          <td>{{ item.note }}</td>
        </tr>
        <tr v-if="filteredItems.length === 0">
          <td colspan="3" style="text-align: center; padding: 24px;">Ничего не найдено по вашему запросу.</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.torque-container {
  margin: 20px 0;
}

.controls {
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 10px 14px;
  font-size: 15px;
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  margin-bottom: 12px;
  outline: none;
}

.search-input:focus {
  border-color: var(--vp-c-brand-1);
}

.filter-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tab-btn {
  padding: 6px 12px;
  font-size: 13px;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.2s;
}

.tab-btn:hover {
  border-color: var(--vp-c-brand-1);
}

.tab-btn.active {
  background: var(--vp-c-brand-1);
  color: #ffffff;
  border-color: var(--vp-c-brand-1);
}

.torque-table {
  width: 100%;
  border-collapse: collapse;
}
</style>

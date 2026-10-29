<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isWakeLockActive = ref(false)
const isSupported = ref(false)
let wakeLockSentinel = null

onMounted(() => {
  isSupported.value = typeof navigator !== 'undefined' && 'wakeLock' in navigator
})

const toggleWakeLock = async () => {
  if (!isSupported.value) {
    alert('Ваш браузер не поддерживает Wake Lock API. Рекомендуется использовать Chrome или Safari.')
    return
  }

  try {
    if (!isWakeLockActive.value) {
      wakeLockSentinel = await navigator.wakeLock.request('screen')
      isWakeLockActive.value = true
      wakeLockSentinel.addEventListener('release', () => {
        isWakeLockActive.value = false
      })
    } else {
      if (wakeLockSentinel) {
        await wakeLockSentinel.release()
        wakeLockSentinel = null
      }
      isWakeLockActive.value = false
    }
  } catch (err) {
    console.warn('Wake Lock error:', err)
    isWakeLockActive.value = false
  }
}

const printPage = () => {
  if (typeof window !== 'undefined') {
    window.print()
  }
}

onUnmounted(async () => {
  if (wakeLockSentinel) {
    await wakeLockSentinel.release()
  }
})
</script>

<template>
  <div class="garage-bar no-print">
    <button 
      class="garage-btn" 
      :class="{ active: isWakeLockActive }"
      @click="toggleWakeLock"
      :title="isWakeLockActive ? 'Экран не гаснет (Активно)' : 'Включить режим не угасающего экрана для работы в гараже'"
    >
      <span class="icon">{{ isWakeLockActive ? '💡' : '🌙' }}</span>
      <span class="text">{{ isWakeLockActive ? 'Экран не гаснет' : 'Не гасить экран' }}</span>
    </button>

    <button 
      class="garage-btn print-btn" 
      @click="printPage"
      title="Распечатать текущую процедуру на принтере (А4)"
    >
      <span class="icon">🖨️</span>
      <span class="text">Печать А4</span>
    </button>
  </div>
</template>

<style scoped>
.garage-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-right: 12px;
}

.garage-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  font-size: 13px;
  font-weight: 500;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
  background-color: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.garage-btn:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}

.garage-btn.active {
  background-color: #f59e0b;
  color: #000000;
  border-color: #d97706;
  font-weight: 600;
}

@media (max-width: 1200px) {
  .garage-btn .text {
    display: none;
  }
  .garage-btn {
    padding: 6px 8px;
  }
}
</style>

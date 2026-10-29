import DefaultTheme from 'vitepress/theme'
import { h, onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
import mediumZoom from 'medium-zoom'
import GarageBar from './GarageBar.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'nav-bar-content-after': () => h(GarageBar)
    })
  },
  setup() {
    const route = useRoute()
    const initZoom = () => {
      if (typeof window !== 'undefined') {
        mediumZoom('.vp-doc img', { background: 'rgba(0,0,0,0.85)' })
      }
    }
    onMounted(() => {
      initZoom()
    })
    watch(
      () => route.path,
      () => nextTick(() => initZoom())
    )
  }
}

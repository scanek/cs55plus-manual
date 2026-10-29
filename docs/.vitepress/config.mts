import { defineConfig } from 'vitepress'

const isGitHubPages = process.env.GITHUB_PAGES === 'true'

export default defineConfig({
  title: "Changan CS55 Plus",
  description: "Руководство по ремонту и техническому обслуживанию (Workshop Manual)",
  base: isGitHubPages ? '/cs55plus-manual/' : '/',
  lang: 'ru-RU',
  
  head: [
    ['link', { rel: 'icon', href: '/img/p18_1.png' }],
    ['link', { rel: 'manifest', href: '/manifest.json' }],
    ['meta', { name: 'theme-color', content: '#2563eb' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black-translucent' }],
  ],

  themeConfig: {
    siteTitle: 'CS55 PLUS Manual',
    logo: '/img/p18_1.png',

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: 'Поиск (Ctrl + K)',
                buttonAriaLabel: 'Поиск'
              },
              modal: {
                noResultsText: 'Ничего не найдено по запросу',
                resetButtonTitle: 'Сбросить поиск',
                footer: {
                  selectText: 'выбрать',
                  navigateText: 'навигация',
                  closeText: 'закрыть'
                }
              }
            }
          }
        }
      }
    },

    nav: [
      { text: 'Главная', link: '/' },
      { text: 'Калькулятор ТО', link: '/maintenance/' },
      { text: 'Моменты затяжки', link: '/torque/' },
      { text: '01. Общие сведения', link: '/01-general/' },
      { text: '02. Двигатель 1.5T', link: '/02-engine/' },
      { text: '03. Трансмиссия 7DCT', link: '/03-transmission/' },
      { text: '04. Шасси', link: '/04-chassis/' },
      { text: '05. Электрика', link: '/05-electrical/' },
      { text: '06. Кузов', link: '/06-body/' },
      { text: 'Коды DTC', link: '/07-dtc/' },
    ],

    sidebar: {
      '/01-general/': [
        {
          text: '01. Общие сведения',
          items: [
            { text: 'Общие сведения и регламент', link: '/01-general/' },
            { text: 'Техника безопасности и охрана труда', link: '/01-general/safety' },
            { text: 'Стандарты сервисного обслуживания', link: '/01-general/standards' },
            { text: 'Идентификация (VIN, шильдики)', link: '/01-general/vin' },
            { text: 'Буксировка, подъем и опоры', link: '/01-general/lifting-towing' },
            { text: 'Шум, вибрация и жесткость (NVH)', link: '/01-general/nvh' },
          ]
        }
      ],
      '/02-engine/': [
        {
          text: '02. Двигатель 1.5T Blue Core',
          items: [
            { text: 'Обзор двигателя и характеристики', link: '/02-engine/' },
            { text: 'Механическая часть: Спецификации и моменты', link: '/02-engine/mechanical-specs' },
            { text: 'Механическая часть: Устройство и ГРМ', link: '/02-engine/mechanical-principles' },
            { text: 'Механическая часть: Поиск неисправностей', link: '/02-engine/mechanical-diagnosis' },
            { text: 'Механическая часть: Снятие и установка агрегатов', link: '/02-engine/mechanical-removal' },
            { text: 'Механическая часть: Разборка и дефектовка ГБЦ', link: '/02-engine/mechanical-overhaul' },
            { text: 'Система смазки', link: '/02-engine/lubrication' },
            { text: 'Система охлаждения', link: '/02-engine/cooling' },
            { text: 'Топливная система прямого впрыска', link: '/02-engine/fuel' },
            { text: 'Система улавливания паров (EVAP)', link: '/02-engine/fuel-vapor' },
            { text: 'Система впуска и турбонаддув', link: '/02-engine/intake' },
            { text: 'Выхлопная система', link: '/02-engine/exhaust' },
            { text: 'Система зажигания', link: '/02-engine/ignition' },
            { text: 'Система пуска (стартер)', link: '/02-engine/starting' },
            { text: 'Система зарядки (генератор, АКБ)', link: '/02-engine/charging' },
            { text: 'Электронное управление (ECU)', link: '/02-engine/ecu' },
            { text: 'Коды неисправностей (DTC)', link: '/02-engine/dtc' },
          ]
        }
      ],
      '/03-transmission/': [
        {
          text: '03. Трансмиссия 7DCT',
          items: [
            { text: 'Обзор 7-ступенчатой КПП (7DCT)', link: '/03-transmission/' },
            { text: 'Характеристики, моменты затяжки, масло', link: '/03-transmission/specifications' },
            { text: 'Устройство и кинематическая схема', link: '/03-transmission/structure' },
            { text: 'Электронный селектор передач (Shift-by-Wire)', link: '/03-transmission/electronic-shift' },
            { text: 'Снятие, установка и замена масла', link: '/03-transmission/service' },
            { text: 'Коды неисправностей (DTC) трансмиссии', link: '/03-transmission/dtc' },
          ]
        }
      ],
      '/04-chassis/': [
        {
          text: '04. Шасси и ходовая часть',
          items: [
            { text: 'Общие сведения и геометрия шасси', link: '/04-chassis/' },
            { text: 'Передняя подвеска (MacPherson)', link: '/04-chassis/suspension-front' },
            { text: 'Задняя многорычажная подвеска', link: '/04-chassis/suspension-rear' },
            { text: 'Углы установки колес (развал-схождение)', link: '/04-chassis/wheel-alignment' },
            { text: 'Рулевое управление и электроусилитель (EPS)', link: '/04-chassis/steering' },
            { text: 'Тормозная система, суппорты и диски', link: '/04-chassis/brakes' },
            { text: 'Антиблокировочная система (ABS) и ESP 9.3', link: '/04-chassis/abs-esp' },
            { text: 'Стояночный тормоз (EPB) и контроль TPMS', link: '/04-chassis/epb-tpms' },
          ]
        }
      ],
      '/05-electrical/': [
        {
          text: '05. Электрооборудование',
          items: [
            { text: 'Обзор электрооборудования', link: '/05-electrical/' },
            { text: 'Вентиляция и кондиционирование (A/C)', link: '/05-electrical/climate' },
            { text: 'Стеклоочистители и стеклоподъемники', link: '/05-electrical/wipers-windows' },
            { text: 'Система освещения (Full-LED)', link: '/05-electrical/lighting' },
            { text: 'Центральный замок и сигнализация', link: '/05-electrical/door-locks' },
            { text: 'Бесключевой доступ (PEPS)', link: '/05-electrical/keyless' },
            { text: 'Круговой обзор 360° и парктроники', link: '/05-electrical/adas-camera' },
            { text: 'Ассистенты ADAS: слепые зоны, полоса, ACC', link: '/05-electrical/adas-assist' },
            { text: 'Мультимедиа и телематика T-Box', link: '/05-electrical/multimedia' },
            { text: 'Панорамная крыша, сиденья, багажник', link: '/05-electrical/body-convenience' },
            { text: 'Подушки безопасности (SRS)', link: '/05-electrical/srs-airbags' },
            { text: 'Предохранители, реле и проводка', link: '/05-electrical/wiring-fuses' },
          ]
        }
      ],
      '/06-body/': [
        {
          text: '06. Кузов и интерьер',
          items: [
            { text: 'Кузовные зазоры и крепеж', link: '/06-body/' },
            { text: 'Приборная панель (торпедо) и консоль', link: '/06-body/interior-dash' },
            { text: 'Обшивки стоек, потолок и салон', link: '/06-body/interior-trim' },
            { text: 'Бамперы, капот, двери и крышка багажника', link: '/06-body/exterior' },
          ]
        }
      ],
      '/07-dtc/': [
        {
          text: 'Коды неисправностей (DTC)',
          items: [
            { text: 'Сводный справочник DTC', link: '/07-dtc/' },
            { text: 'Ошибки двигателя (ECU)', link: '/02-engine/dtc' },
            { text: 'Ошибки трансмиссии (TCU)', link: '/03-transmission/dtc' },
          ]
        }
      ],
      '/maintenance/': [
        {
          text: 'Калькулятор ТО',
          items: [
            { text: 'Регламент технического обслуживания', link: '/maintenance/' }
          ]
        }
      ],
      '/torque/': [
        {
          text: 'Моменты затяжки',
          items: [
            { text: 'Шпаргалка моментов затяжки', link: '/torque/' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/scanek/cs55plus-manual' }
    ],

    footer: {
      message: 'Changan CS55 Plus Workshop Manual (Russian Edition)',
      copyright: 'Неофициальное справочное руководство по ремонту и обслуживанию'
    },

    docFooter: {
      prev: 'Предыдущая страница',
      next: 'Следующая страница'
    },

    darkModeSwitchLabel: 'Тема оформления',
    returnToTopLabel: 'Наверх'
  }
})

import './assets/main.css'

import { createApp } from 'vue'
import elementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'


const app = createApp(App)

app.use(elementPlus)

app.mount('#app')
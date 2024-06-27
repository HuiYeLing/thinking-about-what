// 导入主样式文件
import './assets/main.css'

// 导入 Vue 和其他必要的库
import { createApp } from 'vue'
import elementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'

// 导入组件
import Radios from './components/Radios.vue'
import HelloWorld from './components/HelloWorld.vue'
import MyButton from './components/MyButton.vue'
import VueTest from './views/VueTest.vue'

// 定义路由规则
const routes = [
    {
        path: '/Radios', // 当 URL 为 /Radios 时
        name: 'Radios', // 路由的名字
        component: Radios // 使用 Radios 组件
    },
    {
        path: '/HelloWorld', // 当 URL 为 /HelloWorld 时
        name: 'HelloWorld', // 路由的名字
        component: HelloWorld // 使用 HelloWorld 组件
    },
    {
        path: '/MyButton', // 当 URL 为 /MyButton 时
        name: 'MyButton', // 路由的名字
        component: MyButton // 使用 MyButton 组件
    },
    {
        path: '/VueTest',
        name: 'VueTest',
        component:VueTest
    }
]

// 创建一个 Vue Router 实例
const router = createRouter({
    history: createWebHistory(), // 使用 HTML5 History API
    routes // 使用上面定义的路由规则
})

// 创建一个 Vue 应用
const app = createApp(App)

// 使用 Element Plus 插件
app.use(elementPlus)

// 使用 Vue Router
app.use(router)

// 将 Vue 应用挂载到 #app 元素上
app.mount('#app')
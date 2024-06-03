import { createApp } from 'vue';  
import { createRouter, createWebHistory } from 'vue-router';  
import Radios from './components/Radios.vue';  
import HelloWorld from './components/HelloWorld.vue';  
import MyButton from './components/MyButton.vue';  

  
const routes = [  
    { path: '/', component: Home },  
    {  
        path: '/Radios',  
        name: 'Radios',  
        component: Radios  
    },  
    {  
        path: '/HelloWorld',  
        name: 'HelloWorld',  
        component: HelloWorld  
    },  
    {  
        path: '/MyButton',  
        name: 'MyButton',  
        component: MyButton  
    },  
];  
  
const router = createRouter({  
    history: createWebHistory(),  
    routes, // short for `routes: routes`  
});  
  
export default router;  
  
// 在你的 main.js 或 main.ts 文件中，你应该这样使用它：  
const app = createApp(App); // 假设你有一个 App 组件  
app.use(router);  
app.mount('#app');
import { createApp } from 'vue';  

import Radios from './components/Radios.vue';  
import HelloWorld from './components/HelloWorld.vue';  
import MyButton from './components/MyButton.vue';  
import router from './router';
import App from './App.vue';
import ViewTest from './views/VueTest.vue';
const routes = [  
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
  
  
const app = createApp(App); 
app.use(router);  
app.mount('#app');
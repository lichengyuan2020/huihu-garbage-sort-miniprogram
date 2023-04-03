import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import './styles/theme/index.css';
import './styles/output.css';
import './styles/main.css';

const app = createApp(App); // 创建实例

app.use(router);
app.use(ElementPlus);
app.mount('#app');

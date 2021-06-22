import Vue from 'vue';
import VueRouter from 'vue-router';
import Toasted from 'vue-toasted';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/package.css';

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserCircle, faSignOutAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import routes from './routes';
import App from './App.vue';

library.add([faUserCircle, faSignOutAlt])

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false;
Vue.use(Toasted, { theme: 'bubble', position: 'bottom-center', duration : 3000 });
Vue.use(VueRouter);

// element ui language configuration
import ptBr from 'element-ui/lib/locale/lang/pt-br';
import locale from 'element-ui/lib/locale';
locale.use(ptBr);
Vue.use(ElementUI);

const router = new VueRouter({
    mode: 'history',
    routes,
    linkActiveClass: 'active'
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')

import Vue from 'vue'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'

import Toast, {POSITION} from "vue-toastification";

import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import "../public/theme/css/theme.min.css"
import "vue-toastification/dist/index.css";

import '@/../public/static/main.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(Toast, {
    position: POSITION.TOP_CENTER,
    transition: "Vue-Toastification__slideBlurred",
    maxToasts: 20,
    newestOnTop: true,
    hideProgressBar: true
});

const vue = new Vue({
    router,
    store,
    render: h => h(App)
})

vue.$mount('#app')

import Vue from 'vue'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'

import Toast, {POSITION} from "vue-toastification";

import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'

import {CoolSelectPlugin} from 'vue-cool-select'

import Multiselect from 'vue-multiselect'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'vue-cool-select/dist/themes/bootstrap.css'
import "../public/theme/css/theme.min.css"
import "vue-toastification/dist/index.css";

import '@/../public/static/main.css'


Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(CoolSelectPlugin)

Vue.use(Toast, {
    position: POSITION.TOP_CENTER,
    transition: "Vue-Toastification__slideBlurred",
    maxToasts: 10,
    newestOnTop: true,
    hideProgressBar: true
});

Vue.component('multiselect', Multiselect)



const vue = new Vue({
    router,
    store,
    render: h => h(App)
})

vue.$mount('#app')

import Vue from 'vue'
import App from '@/App.vue'
import store from '@/store'
import router from '@/router'

import Toast, {POSITION} from "vue-toastification";

import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'

import Multiselect from 'vue-multiselect'
import vSelect from 'vue-select'


import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import "../public/theme/css/theme.min.css"
import "vue-toastification/dist/index.css";

import 'vue-select/dist/vue-select.css';


import '@/../public/static/main.css'
import Vuelidate from 'vuelidate'

import vueDebounce from 'vue-debounce'

Vue.component('v-select', vSelect)

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(Vuelidate)

Vue.use(vueDebounce)

Vue.use(Toast, {
    position: POSITION.TOP_CENTER,
    transition: "Vue-Toastification__fade",
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

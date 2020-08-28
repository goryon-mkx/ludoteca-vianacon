import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store' 
import router from '@/router'

import { BootstrapVue } from 'bootstrap-vue'

import "../public/theme/css/theme.min.css"

Vue.config.productionTip = false

//Vue.use(VueRouter)

Vue.use(BootstrapVue)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')

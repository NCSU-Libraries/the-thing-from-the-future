import { createApp } from 'vue'
import App from './App.vue'
import PapaParse from 'papaparse'
// import lodash from 'lodash'


createApp(App)
    .provide('papaparse', PapaParse)
    // .provide('lodash', lodash)
    .mount('#app');


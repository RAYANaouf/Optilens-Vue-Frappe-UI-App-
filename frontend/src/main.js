import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

import { Button, Link, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)

app.component('Button', Button)
app.component('Link', Link)
app.mount('#app')

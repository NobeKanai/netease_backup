import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import axios from "axios";

Vue.config.productionTip = false;

axios.defaults.baseURL =
  window.location.protocol + "//" + window.location.hostname + ":5000";
Vue.prototype.$axios = axios;

new Vue({
  vuetify,
  render: h => h(App)
}).$mount("#app");

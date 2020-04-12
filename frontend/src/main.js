import Vue from "vue";
import App from "./App.vue";
import axios from "axios";
import {
  AppBar,
  Icon,
  Tooltip,
  Button,
  Grid,
  Avatar,
  List,
  Pagination
} from "muse-ui";

Vue.config.productionTip = false;

axios.defaults.baseURL =
  window.location.protocol + "//" + window.location.hostname + ":5000";
Vue.prototype.$axios = axios;

Vue.use(AppBar);
Vue.use(Icon);
Vue.use(Tooltip);
Vue.use(Button);
Vue.use(Grid);
Vue.use(Avatar);
Vue.use(List);
Vue.use(Pagination);

new Vue({
  render: h => h(App)
}).$mount("#app");

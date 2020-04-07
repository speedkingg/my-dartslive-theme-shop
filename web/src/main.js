import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import config from "@/config/config";
import vuetify from "./plugins/vuetify";
import { initializeApp } from "firebase";

Vue.config.productionTip = false;

// Initialize Firebase
initializeApp(config.firebase);

new Vue({
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");

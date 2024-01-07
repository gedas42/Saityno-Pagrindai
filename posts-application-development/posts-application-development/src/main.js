import Vue from "vue";
import vueDebounce from "vue-debounce";
import App from "./App.vue";
import router from "./router/index.js";
import store from "./store/store.js";

Vue.use(vueDebounce);

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");

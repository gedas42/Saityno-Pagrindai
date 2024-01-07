import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home.vue";
import cities from "../views/cities.vue";
import login from "../views/login.vue";
import libraries from "../views/libraries.vue";
import books from "../views/books.vue";
Vue.use(VueRouter);

const routes = [

    { path: "/cities", component: cities },
    { path: "/cities/:id/libraries", component: libraries },
    { path: "/cities/:id/libraries/:library_id/books", component: books },
    { path: "/login", component: login },
    { path: "/", component: Home }, 

];

const router = new VueRouter({
    mode: "history",
    routes,
});

export default router;

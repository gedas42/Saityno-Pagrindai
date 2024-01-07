import Vue from "vue";
import Vuex from "vuex";

import modalModule from "./modules/modalModule";
import apiRequestsPlugin from "./plugins/apiRequestsPlugin.js";
import citiesModule from "./modules/citiesModule"; 
import librariesModule from "./modules/libraries"; 
import BooksModules from "./modules/books"; 
Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {

        modalModule,
        citiesModule,
        librariesModule,
        BooksModules
    },
    plugins: [apiRequestsPlugin],
    state: {
        apiURL: SERVER_ADDR,
        notificationData: {
            type: null,
            message: "",
            isVisible: false,
        },
    },
    mutations: {
        setNotification(state, notification) {
            state.notificationData = notification;
        },
    },
    actions: {
        notificationAction({ commit }, notification) {
            commit("setNotification", notification);
            setTimeout(() => {
                commit("setNotification", {
                    type: null,
                    message: "",
                    isVisible: false,
                });
            }, 3000);
        },
    },
    getters: {
        notificationGetter(state) {
            return state.notificationData;
        },
    },
});

export default store;

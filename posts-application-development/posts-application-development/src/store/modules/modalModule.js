const modalModule = {
    state: {
        modalData: {
            component: null,
            isVisible: false,
        },
    },
    mutations: {
        setModalData(state, modalObject) {
            state.modalData = modalObject;
        },
    },
    actions: {
        modalAction({ commit }, modalObject) {
            commit("setModalData", modalObject);
        },
        closeModalAction({ commit }) {
            commit("setModalData", { component: null, isVisible: false });
        },
    },
    getters: {
        modalDataGetter(state) {
            return state.modalData;
        },
    },
};

export default modalModule;

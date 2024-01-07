<template>
    <div id="app">
    
        <Navbar></Navbar>

        <Home></Home>

        <Modal></Modal>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";

import Modal from "./components/modals/Modal.vue";

export default {
    components: {
        Home,
        Navbar,
        Modal,

    },
};
</script>

<style>
@import "bulma/css/bulma.min.css";
body {
    font-family: sans-serif;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
#app {
    width: 70vw;
    margin: 0 auto;
}
.success {
    background-color: green;
}
.error {
    background-color: rgb(184, 0, 0);
}
</style>

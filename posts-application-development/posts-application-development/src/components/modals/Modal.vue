<template>
    <div v-if="modalDataGetter.isVisible" class="modal is-active">
        <div class="modal-background"></div>
        <div class="modal-content">
            <div class="notification is-flex p-6 has-background-white">
                <component :is="modalDataGetter.component"></component>
            </div>
        </div>
        <button
            @click="closeModal"
            class="modal-close button"
            aria-label="close"
        ></button>
    </div>
</template>

<script>
import DeleteVerification from "../DeleteVerification.vue";
import CreateForm from "../forms/CreateForm.vue";
import EditForm from "../forms/EditForm.vue";
import EditLibrary from "../forms/EditLibrary.vue"
import { mapGetters, mapActions } from "vuex";

export default {
    components: {
        DeleteVerification,
        CreateForm,
        EditForm,
        EditLibrary,
    },
    computed: {
        ...mapGetters(["modalDataGetter"]),
    },
    methods: {
        ...mapActions(["closeModalAction"]),
        closeModal() {
            this.closeModalAction();
        },
    },
};
</script>

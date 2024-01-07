<template>
    <div
        class="container is-flex is-align-items-center is-justify-content-center is-flex-direction-column"
    >
        <h1 class="title is-4 mb-6 mr-3 ml-5 has-text-centered mt-5">
            Are you sure that you want to delete "{{ modalDataGetter.name }}"
            {{ modalDataGetter.target }}?
        </h1>

        <button
            class="button is-danger"
            @click="
                modalDataGetter.target === 'library'
                    ? deleteLibrary()
                    : deleteBook()
            "
        >
            Delete
        </button>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
    computed: {
        ...mapGetters(["modalDataGetter"]),
    },
    methods: {
        ...mapActions([
            "deleteArticleAction",
            "closeModalAction",
            "deleteLibraryAction",
        ]),
        async deleteBook() {
            await this.deleteArticleAction(this.modalDataGetter.id);

            if (this.$router.currentRoute.fullPath !== "/") {
                this.$router.push({ path: "/" });
            }

            this.closeModalAction();
        },
        async deleteLibrary() {
            await this.deleteLibraryAction(this.modalDataGetter.id,this.modalDataGetter.city_id);

            this.closeModalAction();
        },
    },
};
</script>

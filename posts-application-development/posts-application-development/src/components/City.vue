<template>
    <div class="card mb-2">
        <div class="card-content">
            <div
                class="content is-flex is-align-items-center is-justify-content-space-between"
            >
                <div>
                    <h3>Name: {{ name }}</h3>
                    <h3>population: {{ population }}</h3>

                </div>

                <div class="is-flex is-flex-direction-column">
                    <button class="button mt-2" @click="navigateToDetailPage">
                        Libraries
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import { mapActions } from "vuex";

export default {
    props: {
        name: {
            type: String,
        },
        population: {
            type: Number,
        },
        id: {
            type: Number,
        },
    },
    methods: {
        ...mapActions(["modalAction"]),
        navigateToDetailPage() {
            this.$router.push({ path: "/cities/" + this.id +'/libraries'});
        },
        showModal() {
            this.modalAction({
                component: "DeleteVerification",
                isVisible: true,
                id: this.id,
                title: this.title,
                target: "article",
            });
        },
        showEditFormModal() {

            $router.push('/cities')
            this.modalAction({
                component: "EditForm",
                isVisible: true,
                id: this.id,
            });
        },
    },
};
</script>

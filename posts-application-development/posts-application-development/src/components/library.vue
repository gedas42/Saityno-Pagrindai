<template>
    <div class="card mb-2">
        <div class="card-content">
            <div
                class="content is-flex is-align-items-center is-justify-content-space-between"
            >
                <div>
                    <h3>Name: {{ name }}</h3>
                    <h3>Address: {{ address }}</h3>
                    <button
                        @click="navigateToDetailPage"
                        class="button is-small"
                    >
                        Books
                    </button>
                </div>

                <div class="is-flex is-flex-direction-column">
                    <button class="button is-danger" @click="showModal">
                        Delete library
                    </button>
                    <button class="button mt-2" @click="showEditFormModal">
                        Edit library
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
        address: {
            type: String,
        },
        id: {
            type: Number,
        },
        city:{
            type:Number,
        }
    },
    methods: {
        ...mapActions(["modalAction"]),

        navigateToDetailPage() {
            this.$router.push({ path: "/cities/" + this.city +'/libraries/'+ this.id + '/books'});
        },
        showModal() {
            this.modalAction({
                component: "DeleteVerification",
                isVisible: true,
                name:this.name,
                id: this.id,
                city_id:this.city,
                target: "library",
            });
        },
        showEditFormModal() {
            this.modalAction({
                component: "EditLibrary",
                isVisible: true,
                id: this.id,
                name:this.name,
                address:this.address,
                city_id:this.city,
            });
        },
    },
};
</script>

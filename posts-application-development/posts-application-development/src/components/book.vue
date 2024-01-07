<template>
    <div class="card mb-2">
        <div class="card-content">
            <div
                class="content is-flex is-align-items-center is-justify-content-space-between"
            >
                <div>
                    <h3>Name: {{ name }}</h3>
                    <h3>Author: {{ author }}</h3>
                   
                </div>

                <div class="is-flex is-flex-direction-column">
                    <button class="button is-danger" @click="showModal">
                        Delete Book
                    </button>
                    <button class="button mt-2" @click="showEditFormModal">
                        Edit Book
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
        author: {
            type: String,
        },
        id: {
            type: Number,
        },
        library_id:{
            type:Number,
        },
        print_year:{
            type:Number,
        },
        pages:{
            type:Number,
        },
        taken_by: {
            type: String,
        },
    },
    methods: {
        ...mapActions(["modalAction"]),
        navigateToDetailPage() {
            this.$router.push({ path: "/postsDetailPage/" + this.id });
        },
        showModal() {
            this.modalAction({
                component: "DeleteVerification",
                isVisible: true,
                name:this.name,
                id: this.id,
                city_id:this.city,
                target: "book",
            });
        },
        showEditFormModal() {
            this.modalAction({
                component: "EditBook",
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

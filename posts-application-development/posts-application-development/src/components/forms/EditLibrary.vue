<template>
    <form @submit.prevent="submitForm">
        <h1 class="title is-4 has-text-centered">
            Edit "{{ initialName }}" library
        </h1>
        <div class="field">
            <label class="label">Name</label>
            <div class="control">
                <input
                    class="input"
                    type="text"
                    placeholder="Text input"
                    v-model="name"
                />
            </div>
        </div>
        <div class="field">
            <label class="label">Address</label>
            <div class="control">
                <input
                    class="input"
                    type="text"
                    placeholder="Text input"
                    v-model="address"
                />
            </div>
        </div>

        <div class="field is-grouped">
            <div class="control">
                <button class="button is-link">Submit</button>
            </div>
        </div>
        <div
            v-if="errors.length"
            class="pt-5 is-flex is-flex-direction-column is-align-items-center"
        >
            <b class="has-text-danger"
                >Please correct the following error(s):</b
            >
            <ul>
                <li
                    v-for="error in errors"
                    :key="error"
                    class="has-text-danger"
                >
                    {{ error }}
                </li>
            </ul>
        </div>
    </form>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
    data() {
        return {
            initialName: "",
            name: "",
            initialAddress:"",
            address:"",
            errors: [],
        };
    },
    computed: {
        ...mapGetters(["modalDataGetter"]),
    },
    methods: {
        ...mapActions(["editLibrary", "closeModalAction"]),
        async submitForm() {
            this.errors = [];

            if (!this.name) {
                this.errors.push("The name field is empty.");
            }

            if (this.name.trim().length > 50) {
                this.errors.push("The name must not exceed 50 characters.");
            }

            if (this.errors.length > 0) {
                return;
            }

            if (
                this.name.replace(/\s+/g, " ").trim() !==
                this.modalDataGetter.name.trim()
            ) {
                const editedAuthor = {
                    name: this.name.replace(/\s+/g, " ").trim(),
                    address:this.address.replace(/\s+/g, " ").trim(),
                };

                await this.editLibrary(editedAuthor);
                this.closeModalAction();
            } else {
                this.errors.push("You haven't changed anything.");
            }
        },
    },
    async created() {
        this.initialName = this.modalDataGetter.name;
        this.name = this.modalDataGetter.name;
        this.initialAddress = this.modalDataGetter.address;
        this.address = this.modalDataGetter.address;
    },
};
</script>

<template>
    <form class="column is-full" @submit.prevent="submitForm">
        <h1 class="title is-4 has-text-centered">Create a new author</h1>
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

        <button class="button is-success is-light">Submit</button>
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
import formValidationMixin from "../../mixins/formValidationMixin.js";

export default {
    data() {
        return {
            name: "",
            errors: [],
        };
    },
    methods: {
        ...mapActions(["postNewAuthor", "closeModalAction"]),
        async submitForm() {
            this.errors = [];

            if (!this.name.trim()) {
                this.errors.push("The name field is empty.");
            }

            if (this.name.trim().length > 50) {
                this.errors.push("The name must not exceed 50 characters.");
            }

            if (this.errors.length > 0) {
                return;
            }

            const newAuthor = {
                name: this.name.replace(/\s+/g, " ").trim(),
                created_at: new Date().toLocaleString("lt-LT").slice(0, 11),
                updated_at: new Date().toLocaleString("lt-LT").slice(0, 11),
            };

            await this.postNewAuthor(newAuthor);

            this.closeModalAction();
        },
    },
    computed: {
        ...mapGetters(["allAuthors"]),
    },
};
</script>

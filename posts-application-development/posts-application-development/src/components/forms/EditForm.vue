<template>
    <form @submit.prevent="submitForm">
        <h1 class="title is-4 has-text-centered">
            Edit "{{ initialTitle }}" article
        </h1>
        <div class="field">
            <label class="label">Title</label>
            <div class="control">
                <input
                    class="input"
                    type="text"
                    placeholder="Text input"
                    v-model="title"
                />
            </div>
        </div>

        <div class="field">
            <label class="label">Content</label>
            <div class="control">
                <textarea
                    class="textarea"
                    placeholder="Textarea"
                    v-model="content"
                ></textarea>
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
import formValidationMixin from "../../mixins/formValidationMixin.js";

export default {
    data() {
        return {
            initialTitle: "",
            title: "",
            content: "",
            errors: [],
        };
    },
    computed: {
        ...mapGetters(["modalDataGetter", "specificArticle", "allAuthors"]),
    },
    methods: {
        ...mapActions([
            "fetchArticleData",
            "editArticle",
            "closeModalAction",
            "fetchAuthorsData",
        ]),
        async submitForm() {
            this.formValidation();

            if (this.errors.length > 0) {
                return;
            }

            if (
                this.title.replace(/\s+/g, " ").trim() !==
                    this.specificArticle.title.trim() ||
                this.content.replace(/\s+/g, " ").trim() !==
                    this.specificArticle.body.trim()
            ) {
                const editedArticle = {
                    id: this.specificArticle.id,
                    title: this.title.replace(/\s+/g, " ").trim(),
                    body: this.content.replace(/\s+/g, " ").trim(),
                    authorId: this.specificArticle.authorId,
                    created_at: this.specificArticle.created_at,
                    updated_at: new Date().toLocaleString("lt-LT").slice(0, 11),
                    author: this.allAuthors.find(
                        (author) => author.id === this.specificArticle.authorId
                    ),
                };

                await this.editArticle(editedArticle);
                this.closeModalAction();
            } else {
                this.errors.push("You haven't changed anything.");
            }
        },
    },
    async created() {
        await this.fetchArticleData(this.modalDataGetter.id);
        await this.fetchAuthorsData();
        this.initialTitle = this.specificArticle.title;
        this.title = this.specificArticle.title;
        this.content = this.specificArticle.body;
    },
    mixins: [formValidationMixin],
};
</script>

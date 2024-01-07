export default {
    methods: {
        formValidation() {
            this.errors = [];

            if (!this.title.trim()) {
                this.errors.push("The title field is empty.");
            }

            if (this.title.trim().length > 50) {
                this.errors.push("The title must not exceed 50 characters.");
            }

            if (!this.content.trim()) {
                this.errors.push("The content field is empty.");
            }
        },
    },
};

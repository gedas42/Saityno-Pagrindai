<template>
    
    <div>
        
        <div v-if="allBooks && allBooks.length > 0">
            <book
                v-for="book in allBooks"
                :id="book.id"
                :library_id="book.library_id"
                :name="book.name"
                :author="book.author"
                :print_year="book.print_year"
                :pages="book.pages"
                :taken_by="book.taken_by"
                :key="book.id"
            ></book>
        </div>
    </div>
</template>

<script>
import book from "../components/book.vue";
import {mapGetters, mapActions } from "vuex";
export default {
    components: {
        book,
    },
    computed: {
        ...mapGetters([
            "allBooks",
        ]),
    },
    methods: {
        ...mapActions([
            "fetchBooksData",
            "setId"
    ]),
    },
    async created() {
        const cityid = this.$route.params
        
        await this.fetchBooksData(cityid);
        this.dataFetched = true;
    },
}
</script>

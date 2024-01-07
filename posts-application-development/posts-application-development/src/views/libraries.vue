<template>
    <div>
        <div v-if="allLibraries && allLibraries.length > 0">
            <library
                v-for="library in allLibraries"
                :id="library.id"
                :city="library.city_id"
                :name="library.name"
                :address="library.address"
            ></library>
        </div>
    </div>
</template>

<script>
import library from "../components/library.vue";
import {mapGetters, mapActions } from "vuex";
export default {
    components: {
        library,
    },
    computed: {
        ...mapGetters([
            "allLibraries",
        ]),
    },
    methods: {
        ...mapActions([
            "fetchLibrariesData"
    ]),
    },
    async created() {
        const cityid = this.$route.params.id;
        await this.fetchLibrariesData(cityid);
        this.dataFetched = true;
    },
}
</script>

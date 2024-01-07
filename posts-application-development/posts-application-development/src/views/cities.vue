<template>
    <div>
        <div v-if="allCities && allCities.length > 0">
            <city
                v-for="city in allCities"
                :id="city.id"
                :name="city.name"
                :population="city.population"
            ></city>
        </div>
    </div>
</template>

<script>
import city from "../components/City.vue";
import {mapGetters, mapActions } from "vuex";
export default {
    components: {
        city,
    },
    computed: {
        ...mapGetters([
            "allCities",
        ]),
    },
    methods: {
        ...mapActions([
            "fetchCitiesData"
    ]),
    },
    async created() {

        await this.fetchCitiesData();
        this.dataFetched = true;
    },
}
</script>

// import axios from "axios";
// const citiesModule = {

//     state: {
//         citiesData:null,
//         cityData: null,
//     },
//     mutations: {
//         setCitiesData(state, data) {
//             state.citiesData = data;
//         },
//     },
//     actions: {
//         async fetchCitiesData({ commit}) {
//             try {
//                 const response = await axios.get(`http://127.0.0.1:5000/api/users`);
//                 commit("setCitiesData", response.data);
//                 console.log(response.data)
//             } catch (error) {
//                 throw new Error(
//                    Console.log("error fetching cities") 
//                 );
//             }
//         },
//     },
//     getters: {
//         allCities: (state) => state.citiesData,
//     },

// }
// export default citiesModule;
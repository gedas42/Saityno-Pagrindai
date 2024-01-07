import axios from "axios";
const BooksModule = {

    state: {
        BooksData:[],
        BookData: null,
        library_id:null
    },
    mutations: {
        setBooksData(state, data) {
            state.BooksData = data;
        },
        setIdData(state, data) {
            state.library_id = data;
        },
    },
    actions: {
        async fetchBooksData({ commit},cityid) {
            try {
                console.log(cityid)
                const response = await axios.get('http://127.0.0.1:5000/api/cities/' + parseInt(cityid.id) +'/libraries/' + parseInt(cityid.library_id) +'/books');
                console.log(response.data)
                commit("setBooksData", response.data);
            } catch (error) {
                console.log(error)
                // throw new Error(
                //    console.log("error fetching cities") 
                // );
            }
        },
        async setId({ commit},lib) {

            commit("setIdData", lib);

        },
        },
      
    
    getters: {
        allBooks: (state) => state.BooksData,
    },

}
export default BooksModule;
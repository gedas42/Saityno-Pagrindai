import axios from "axios";
const librariesModule = {

    state: {
        librariesData:[],
        libraryData: null,
    },
    mutations: {
        setLibrariesData(state, data) {
            state.librariesData = data;
        },
        setLibraryData(state, data) {
            state.libraryData = data;
        },
        setEditedLibraryData(state, editedAuthor) {
            const postIndex = state.librariesData.findIndex(
                (library) => library.id === editedAuthor.id
            );
            if (postIndex !== -1) {
                state.librariesData.splice(postIndex, 1, editedAuthor);
            }
        },
    },
    actions: {
        async fetchLibrariesData({ commit,state,},cityid) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/cities/'+cityid+'/libraries');
                commit("setLibrariesData", response.data);
                console.log(response.data)
            } catch (error) {
                throw new Error(
                   Console.log("error fetching libraries") 
                );
            }
        },
        async fetchLibraryData({ commit,state,},cityid,libraryid) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/cities/'+cityid+'/libraries'+libraryid);
                commit("setLibraryData", response.data);
            } catch (error) {
                throw new Error(
                   Console.log("error fetching library") 
                );
            }
        },
        async editLibrary(
            { getters, dispatch, commit },editedAuthor ) {
            const config = {
                headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
              };
              
                await axios.put(
                    `${SERVER_ADDR}/cities/${getters.modalDataGetter.city_id}/libraries/${getters.modalDataGetter.id}`,
                    editedAuthor,config
                );
                dispatch("fetchLibrariesData", getters.modalDataGetter.city_id);
               
            
        },
        async deleteLibraryAction(
            { dispatch, getters }) {
                const config = {
                    headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
                  };
                  
                    await axios.delete(
                        `${SERVER_ADDR}/cities/${getters.modalDataGetter.city_id}/libraries/${getters.modalDataGetter.id}`,
                        config
                    );
                    dispatch("fetchLibrariesData", getters.modalDataGetter.city_id);
        },
    },
    
    getters: {
        allLibraries: (state) => state.librariesData,
        singleLibrary: (state) => state.libraryData,
    },

}
export default librariesModule;
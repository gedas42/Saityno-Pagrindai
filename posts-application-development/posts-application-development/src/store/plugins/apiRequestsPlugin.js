import axios from "axios";

const apiRequestsPlugin = (store) => {
    store.fetchData = async (url) => {
        try {
            const response = await axios.get(url);
            return response;
        } catch (error) {
            throw new Error(
                `An error occurred while trying to fetch data from the following URL: ${url}. ${error}`
            );
        }
    };

    store.postData = async (url, data) => {
        try {
            await axios.post(url, data);
        } catch (error) {
            throw new Error(
                `An error occurred while trying to post data to the following URL: ${url}. ${error}`
            );
        }
    };

    store.deleteData = async (url) => {
        try {
            await axios.delete(url);
        } catch (error) {
            throw new Error(
                `An error occurred while trying to delete data from the following URL: ${url}. ${error}`
            );
        }
    };

    store.editData = async (url, editedData) => {
        try {
            await axios.put(url, editedData);
        } catch (error) {
            throw new Error(
                `An error occurred while trying to edit data from the following URL: ${url}. ${error}`
            );
        }
    };
};

export default apiRequestsPlugin;

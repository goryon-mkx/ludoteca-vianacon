import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import library from './modules/library'
import router from "@/router";
import authorizationService from "@/services/authorization.service"
import localStorageService from "@/services/localStorage.service"

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        messages,
        library
    },
    actions: {
        /**
         * Do login with username and password
         * In case of success, save tokens to local storage
         * @param commit
         * @param username
         * @param password
         * @returns {Promise<AxiosResponse<any>>}
         */
        login({commit}, {username, password}) {
            return authorizationService.doLogin(username, password).then(response => {
                commit("AUTH_SUCCESS", response.data);
                router.push({name: "home"});
            });
        },
    },

    mutations: {
        SET_CURRENT_USER(state, user) {
            state.currentUser = user;
        },
        AUTH_SUCCESS(state, tokenObj) {
            localStorageService.setRefreshToken(tokenObj.refresh);
            localStorageService.setAccessToken(tokenObj.access);
        },
        AUTH_LOGOUT() {
            localStorageService.clearTokens();
        }
    },
})
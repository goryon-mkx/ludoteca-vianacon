import {unauthApi, authApi} from '@/services/api'

const URL = '/api/library-games/'

export default {
    /**
     * Get all games for the given page
     * @param page
     * @returns {Promise<*>}
     */
    fetchGames(page) {
        return unauthApi.get(URL, {
            params: {
                page: page
            }
        })
            .then(response => response.data)
    },
    /**
     * Get library game by game id
     * @param gameId
     * @returns {Promise<*>}
     */
    fetchGame(gameId){
        return unauthApi.get(URL+`${gameId}`)
            .then(response => response.data)
    },

    filterGames(params){
        return unauthApi.get(URL, {
            params: params
        }).then(response => response.data)
    },
    createGame(payload) {
        return authApi.post(URL, payload)
            .then(response => response.data)
    },
    updateGame(gameId, payload){
      return authApi.patch(URL+ `${gameId}/`, payload)
          .then(response => response.data)
    },
    deleteGame(gameId) {
        return authApi.delete(URL+ `${gameId}/`)
            .then(response => response.data)
    },
}
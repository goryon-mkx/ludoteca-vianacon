import {unauthApi, authApi} from '@/services/api'

const URL = '/api/library-games/'

export default {
    fetchGames() {
        return unauthApi.get(URL)
            .then(response => response.data.results)
    },
    fetchGame(gameId){
        return unauthApi.get(URL+`${gameId}`)
            .then(response => response.data)
    },
    searchGame(search){
        return unauthApi.get(URL, {
            params: { 'search': search}
        }).then(response => response.data.results)
    },
    filterGames(params){
        return unauthApi.get(URL, {
            params: params
        }).then(response => response.data.results)
    },
    createGame(payload) {
        return authApi.post(URL, payload)
            .then(response => response.data)
    },
    deleteGame(gameId) {
        return authApi.delete(URL+ `${gameId}`)
            .then(response => response.data)
    }
}
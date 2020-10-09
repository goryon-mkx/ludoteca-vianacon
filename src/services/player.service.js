import {authApi} from '@/services/api'

const URL = '/api/players/';

export default {
    fetchPlayers() {
        return authApi.get(URL)
            .then(response => response.data)
    },
    fetchPlayer(id){
        return authApi.get(URL+`${id}`)
            .then(response => response.data)
    },
    createPlayer(payload) {
        return authApi.post(URL, payload)
            .then(response => response.data)
    },
    deletePlayer(id) {
        return authApi.delete(URL+ `${id}`)
            .then(response => response.data)
    }
}
import settingsService from '@/services/settings.service'

const state = {
    games: [],
    locations: []
}

const getters = {
    games: state => {
        return state.games
    },
    locations: state => {
        return state.locations
    }
}

const actions = {
    loadLocations({commit}){
        settingsService.getLocations().then(data => {
            commit("setLocations", data)
        })
    }
}

const mutations = {
    setGames(state, games) {
        state.games = games
    },
    addGame(state, game) {
        state.games.push(game)
    },
    deleteGame(state, gameId) {
        state.games = state.games.filter(obj => obj.pk !== gameId)
    },
    setLocations(state, payload){
        state.locations = payload
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
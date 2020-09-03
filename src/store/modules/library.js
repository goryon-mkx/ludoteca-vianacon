import libraryService from '@/services/library.service'

const state = {
    games: []
}

const getters = {
    games: state => {
        return state.games
    }
}

const actions = {
    getGames({commit}) {
        libraryService.fetchGames()
            .then(games => {
                commit('setGames', games)
            })
    },
    addGame({commit}, game) {
        libraryService.postGame(game)
            .then(() => {
                commit('addGame', game)
            })
    },
    deleteGame({commit}, gameId) {
        libraryService.deleteGame(gameId).then(
            commit('deleteGame', gameId)
        )
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
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
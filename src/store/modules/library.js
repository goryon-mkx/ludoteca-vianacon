
const state = {
    games: []
}

const getters = {
    games: state => {
        return state.games
    }
}

const actions = {

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
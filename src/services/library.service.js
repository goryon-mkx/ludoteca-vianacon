import {unauthApi, authApi} from '@/services/api'

export default {
  fetchGames() {
    return unauthApi.get(`library/`)
              .then(response => response.data.results)
  },
  postGame(payload) {
    return authApi.post(`library/`, payload)
              .then(response => response.data)
  },
  deleteGame(gameId) {
    return authApi.delete(`library/${gameId}`)
              .then(response => response.data)
  }
}
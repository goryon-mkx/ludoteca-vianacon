const state = {
  configurations: [],
}

const getters = {
  all: (state) => {
    return state.configurations
  },
  get: (state) => (key) => {
    return state.configurations.filter((config) => (config.key = key))
  },
}

const actions = {
  load() {},
}

const mutations = {
  setConfigurations(state, payload) {
    state.configurations = payload
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}

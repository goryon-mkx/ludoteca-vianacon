const state = {
  page_size: '30'
}

const getters = {
  pageSize: state => {
    return state.page_size
  },
}

const actions = {
  setPageSize({ commit }, payload) {
    commit('setPageSize', payload)
  },
}

const mutations = {
  setPageSize(state, page_size) {
    state.page_size = page_size
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}

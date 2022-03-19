<template>
  <HomeScreenTemplate :title="title" :pre-title="pretitle">
    <template #actions>

      <b-alert class="mb-0 d-inline-block" variant="warning" :show="true"><b-icon-award-fill/> Membership's Price</b-alert>

      <b-button class="d-inline-block ml-3" v-if="isAdmin()" variant="primary" :to="{name: 'StoreAddGame'}">Add game</b-button>
    </template>
    <b-row class="mb-3">
      <!-- Search -->
      <b-col>
        <l-search v-model="search"/>
      </b-col>
    </b-row>

    <Games :loading="loading" :games="games" @update="updateGame" class="pt-5" @delete="deleteGame"/>

    <Pagination v-model="currentPage" :total-count="totalGamesCount"/>
  </HomeScreenTemplate>
</template>

<script>
import Games from "@/pages/store/home/partials/Games"
import HomeScreenTemplate from "@/components/templates/HomeScreenTemplate"
import storeService from "@/services/store.service"
import usersMixin from "@/mixins/users.mixin"
import Pagination from "@/components/Pagination"
import LSearch from "@/components/form/LSearch"

export default {
  name: 'StoreHome',
  components: {
    HomeScreenTemplate,
    Games,
    Pagination,
    LSearch
  },
  mixins: [usersMixin],
  props: ['title', 'pretitle'],
  data() {
    return {
      search: '',
      currentPage: 1,
      games: [],
      loading: true,
      totalGamesCount: 0
    }
  },
  mounted(){
    this.refreshGames()
  },
  computed:{
    associate_discount(){
      const configurations = this.$store.getters['configurations/all']
      if (configurations){
        return configurations.filter(conf => conf.key === 'associate_discount')[0].value
      }
      return 1
    }
  },
  watch: {
    currentPage() {
      this.refreshGames()
    },
    search() {
      // anytime the search string is change we should reset page number
      // otherwise the user could face a 404 because the page is not available for the search results
      this.currentPage = 1

      this.refreshGames()
    },
  },
  methods: {
    getParams() {
      let params = {}

      params['page'] = this.currentPage

      if (this.search) {
        params['search'] = this.search
      }

      // Object.keys(this.filters.filtersSelected).forEach(
      //     (key) => (params[key] = this.filters.filtersSelected[key]),
      // )

      return params
    },
    refreshGames(){
      let params = this.getParams()
      this.loading = true
      storeService.filterGames(params).then(response => {
        this.games = response.results
        this.loading = false
        this.totalGamesCount = response.count
    })
    },
    updateGame(game){
      if (game) {
        const outdatedGameObject = this.games.filter((item) => item.id === game.id)[0]
        this.$set(this.games, this.games.indexOf(outdatedGameObject), game)
      } else {
        storeService.fetchGames(this.currentPage).then(response => this.games = response)
      }
    },
    deleteGame(game_id){
      if (game_id){
        const outdatedGameObject = this.games.filter((item) => item.id === game_id)[0]
        this.games.splice(this.games.indexOf(outdatedGameObject), 1)
      } else {
        storeService.fetchGames(this.currentPage).then(response => this.games = response)
      }
    }
  },
}
</script>

<style scoped></style>

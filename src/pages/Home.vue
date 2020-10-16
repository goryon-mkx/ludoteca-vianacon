<template>
  <div>
    <Header :title="title" :pretitle="pretitle">
      <template v-slot:content-right>
        <b-button variant="primary" :to="{name: 'AddLibraryGame'}">
          <b-icon-plus class="mr-2"></b-icon-plus>
          Add game
        </b-button>
      </template>
    </Header>
    <div class="row align-items-center mb-3">
      <div class="col">

        <!-- Form -->
        <form>
          <div class="input-group input-group-lg input-group-merge">
            <b-form-input v-model="search" type="search" debounce="500" class="form-control-prepended"
                          placeholder="Search"></b-form-input>
            <div class="input-group-prepend">
              <div class="input-group-text">
                <b-icon-search font-scale="0.8"></b-icon-search>
              </div>
            </div>
          </div>
        </form>

      </div>
      <div class="col-auto">
        <!-- Toggle -->
        <b-button v-b-toggle.filters-collapse size="lg" :pressed.sync="filtersOpen" class="btn-white"
                  data-toggle="dropdown" aria-haspopup="true"
                  aria-expanded="false">
          <b-icon-filter></b-icon-filter>
          Filters
          <b-badge class="ml-1" v-show="countFilters>0">{{ countFilters }}</b-badge>
        </b-button>
      </div>

    </div>
    <b-row>
      <b-col>
        <b-collapse id="filters-collapse" class="">
          <div class="bg-light rounded p-4">
            <b-row>
              <b-col sm="12" lg="6">
                <b-form-group label="Location">
                  <multiselect v-model="filters.location"
                               :options="shelves"></multiselect>
                </b-form-group>
              </b-col>
              <b-col sm="12" lg="6">
                <b-form-group label="Owner">
<!--                  <b-button variant="outline-secondary">-->
<!--                    <b-icon-plus class="mr-1" v-b-modal:filter-players-modal></b-icon-plus>-->
<!--                    Add-->
<!--                  </b-button>-->
                                    <multiselect v-model="filters.owner" @search-change="searchPlayers"
                               :options="players" label="name"></multiselect>
                </b-form-group>
              </b-col>

              <div class="d-flex w-100 flex-row justify-content-end">
                <b-link class="text-gray-800" @click="filters = initFilters()">
                  <b-icon-x></b-icon-x>
                  CLEAR FILTERS
                </b-link>
              </div>
            </b-row>


          </div>
        </b-collapse>
      </b-col>
    </b-row>

    <div class="row mt-4">
      <div class="col-12 col-lg-6" v-for="(game,index) in games" :key="index">
        <GameCard :game="game.game">
          <template v-slot:top-right>
            <div class="d-flex align-items-center">

              <b-link :to=" {name: 'WithdrawGame', params: {id: game.id}}"
                      v-show="game.status === 'available'"
                      class="text-uppercase small text-gray-800">
                <b-icon-upload class="mr-1"></b-icon-upload>
                <span> Withdraw</span>
              </b-link>
              <b-link v-b-modal.checkin-modal
                      v-show="game.status === 'not-checked-in'"
                      class="text-uppercase small text-gray-800">
                <b-icon-bag-plus class="mr-1"></b-icon-bag-plus>
                <span> Check-in</span>
              </b-link>
              <b-link href="#" v-show="game.status === 'not-available'"
                      class="text-uppercase small text-gray-800"
                      @click="returnGame(game)">
                <b-icon-download class="mr-2"></b-icon-download>
                <span class="small">return ({{ game.location }})</span></b-link>
            </div>
            <b-dropdown size="sm" variant="link" toggle-class="text-muted text-decoration-none" no-caret>
              <template v-slot:button-content>
                <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
              </template>
              <b-dropdown-item>Edit</b-dropdown-item>
              <b-dropdown-item>Delete</b-dropdown-item>
            </b-dropdown>


          </template>
          <template v-slot:bottom-right>

            <div v-if="game.status  === 'not-available'">
              <span class="text-warning">With {{ game.current_withdraw.requisitor.name }}</span>
            </div>
            <div v-if="game.status === 'available'">
              <span class="text-success">Available</span>
            </div>

          </template>
        </GameCard>
      </div>
      <b-modal id="checkin-modal">
        <b-form-group label="Shelf">
          <multiselect v-model="filters.location" :options="shelves"></multiselect>
        </b-form-group>
      </b-modal>
    </div>
    <ModalPlayerSelect id="filter-players-modal"></ModalPlayerSelect>
  </div>
</template>

<script>
import gamesMixin from "@/mixins/games.mixin"
import withdrawService from '@/services/withdraw.service'
import libraryService from "@/services/library.service"
import Header from "@/components/Header";
import GameCard from "@/components/GameCard";
import ModalPlayerSelect from "@/components/ModalPlayerSelect";
import playerService from "@/services/player.service"

export default {
  name: "Home",
  props: ['title', 'pretitle'],
  data() {
    return {
      search: '',
      games: [],
      allGamesBackup: [],
      players: [],
      filters: this.initFilters(),
      filtersOpen: false,
      shelves: ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5']
    }
  },
  components: {ModalPlayerSelect, GameCard, Header},
  mixins: [gamesMixin],
  mounted() {
    this.loadGames()
  },
  methods: {
    initFilters() {
      return {
        location: ''
      }
    },
    returnGame(game) {
      withdrawService.returnGame(game.current_withdraw.id).then(() => {
        this.loadGames()
        this.$toast.success('Successfuly withdrawn, please return to ' + game.location)
      })
    },
    loadGames() {
      libraryService.fetchGames().then(response => {
        this.games = response
      })
    },
    searchPlayers(query) {
      playerService.searchPlayers(query).then(response => {
        this.players = response
      })
    }
  },
  computed: {
    countFilters() {
      return this.filters.location ? 1 : 0
    }
  },
  watch: {
    search() {
      let params = {}

      if (this.search) {
        params.search = this.search
      }

      if (this.filters.location)
        params.location = this.filters.location

      libraryService.filterGames(params).then(response => this.games = response)
    },
    "filters.location": function () {
      let params = {}
      if (this.search)
        params.search = this.search

      if (this.filters.location)
        params.location = this.filters.location

      libraryService.filterGames(params).then(response => this.games = response)
    }
  },

}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
span.multiselect__tags {
  font-size: 14px;
}
</style>
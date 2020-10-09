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
        <b-button v-b-toggle.filters-collapse size="lg" :pressed.sync="filtersOpen" class="btn-white" data-toggle="dropdown" aria-haspopup="true"
                  aria-expanded="false">
          <b-icon-filter></b-icon-filter>
          Filters
          <b-badge class="ml-1" v-show="countFilters>0">{{countFilters}}</b-badge>
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
                  <b-select :options="shelves" v-model="filters.location"/>
                  <!--                  <div class="d-flex flex-column">-->
                  <!--                    <b-form-checkbox-group-->
                  <!--                        v-model="filters.location.letter"-->
                  <!--                        :options="shelves.letters"-->
                  <!--                        name="buttons-1"-->
                  <!--                        button-variant="info"-->
                  <!--                        buttons-->
                  <!--                    />-->
                  <!--                    <b-form-checkbox-group-->
                  <!--                        :options="shelves.numbers"-->
                  <!--                        v-model="filters.location.number"-->
                  <!--                        name="buttons-2"-->
                  <!--                        buttons class="mt-1"-->
                  <!--                        button-variant="info"-->
                  <!--                    />-->
                  <!--                  </div>-->
                </b-form-group>
              </b-col>
              <b-col sm="12" lg="6">


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
            <div></div>

            <div v-if="game.status  === 'not-available'">
              <span class="fe fe-alert-circle text-warning"></span>

              <span class="text-warning">Being played ({{ game.currentwithdraw.requisitor.name }})</span>
            </div>

            <div class="dropdown ml-1">
              <a class="" type="button"
                 id="dropdownMenuButton"
                 data-toggle="dropdown"
                 aria-haspopup="true"
                 aria-expanded="false">
                <span class="fe fe-more-vertical"></span>
              </a>
              <div class="dropdown-menu dropdown-menu-right"
                   aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Edit</a>
                <a class="dropdown-item" href="#">Delete</a>
              </div>
            </div>
          </template>
          <template v-slot:bottom-right>
            <div>

              <b-link :to=" {name: 'WithdrawGame', params: {id: game.id}}"
                      v-show="game.status === 'available'"
                      class="text-uppercase small text-gray-800">
                <b-icon-upload class="mr-1"></b-icon-upload>
                <span> Withdraw</span>
              </b-link>
              <b-link href="#" v-show="game.status === 'not-available'"
                      class="text-uppercase small text-gray-800"
                      @click="returnGame(game)">
                <b-icon-download class="mr-2"></b-icon-download>
                <span class="small">return ({{ game.location }})</span></b-link>
            </div>
          </template>
        </GameCard>
      </div>
    </div>
  </div>
</template>

<script>
import gamesMixin from "@/mixins/games.mixin"
import withdrawService from '@/services/withdraw.service'
import libraryService from "@/services/library.service"
import Header from "@/components/Header";
import GameCard from "@/components/GameCard";

export default {
  name: "Home",
  props: ['title', 'pretitle'],
  data() {
    return {
      search: '',
      games: [],
      allGamesBackup: [],
      filters: this.initFilters(),
      filtersOpen: false,
      shelves: ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5']
    }
  },
  components: {GameCard, Header},
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
      withdrawService.returnGame(game.currentwithdraw.id).then(() => {
        this.loadGames()
        this.$toast.success('Successfuly withdrawn, please return to ' + game.location)
      })
    },
    loadGames() {
      libraryService.fetchGames().then(response => {
        this.games = response
      })
    },
  },
  computed: {
    countFilters() {
      return this.filters.location ? 1 : 0
    }
  }
  , watch: {
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

<style scoped>

</style>
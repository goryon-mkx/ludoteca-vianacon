<template>
  <div>
    <Header :title="title" :pretitle="pretitle">
      <template v-slot:content-right>
        <b-dropdown variant="white" class="mr-3" no-caret>
          <template #button-content>
            <b-icon-gear/>
          </template>
          <b-dropdown-item-button v-if="!bulk" @click="bulk=true">
            Enable God mode
          </b-dropdown-item-button>
          <b-dropdown-item-button v-else @click="bulk=false">
            Disable God mode
          </b-dropdown-item-button>
        </b-dropdown>

        <b-button variant="primary" :to="{name: 'AddLibraryGame'}">
          <b-icon-plus class="mr-2"></b-icon-plus>
          Add game
        </b-button>
      </template>
    </Header>

    <!-- Search and filters trigger -->
    <div class="row align-items-center mb-3">

      <!-- Search -->
      <div class="col">
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

      <!-- Filters trigger -->
      <div class="col-auto">
        <b-button v-b-toggle.filters-collapse size="lg" :pressed.sync="filtersOpen" class="btn-white"
                  data-toggle="dropdown" aria-haspopup="true"
                  aria-expanded="false">
          <b-icon-filter></b-icon-filter>
          Filters
          <b-badge class="ml-1" v-show="Object.keys(filters).length>0">{{ Object.keys(filters).length }}</b-badge>
        </b-button>
      </div>

    </div>

    <!-- Filters -->
    <b-row>
      <b-col>
        <b-collapse id="filters-collapse" class="">
          <div class="bg-light rounded p-4">
            <b-row>

              <!-- Location -->
              <b-col sm="12" lg="6">
                <b-form-group label="Location">
                  <v-select placeholder="Select an option" :options="shelves_options"
                            v-model="filters['location']"></v-select>
                </b-form-group>
              </b-col>

              <!-- Owner -->
              <b-col sm="12" lg="6">
                <b-form-group label="Owner">
                  <v-select v-model="filters['owner']" value-prop="id"
                            :reduce="player => player.id" :filterable="false" label="name"
                            :options="players" @search="searchPlayers">
                  </v-select>
                </b-form-group>
              </b-col>

              <!-- Status -->
              <!--              <b-col sm="12" lg="6">-->
              <!--                <b-form-group label="Status">-->
              <!--                  <b-form-checkbox-group-->
              <!--                      v-model="filters['status']"-->
              <!--                      :options="status_options"-->
              <!--                      size="md"-->
              <!--                      buttons-->
              <!--                      button-variant="white"-->
              <!--                  ></b-form-checkbox-group>-->
              <!--                </b-form-group>-->
              <!--                {{filters}}-->
              <!--              </b-col>-->


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

    <!-- Content -->
    <div class="row mt-4">

      <!-- Games list -->
      <div class="col-12 col-lg-6" v-for="(game,index) in games" :key="index">
        <LibraryGameCard :game="game" :bulk="bulk" v-model="selected" :value="game.id"/>
      </div>

      <CheckinModal id="checkin-modal" :shelves="shelves_options" :game="selectedGame"
                    v-on:checkin="checkinGame"></CheckinModal>
    </div>

    <!-- Pagination -->
    <b-row v-show="pagination.count > pagination.count_per_page" no-gutters>

      <!-- Pagination (prev) -->
      <ul class="col list-pagination-prev pagination pagination-tabs justify-content-start">
        <li class="page-item">
          <a class="page-link" href="#">
            <i class="fe fe-arrow-left mr-1"></i> Previous
          </a>
        </li>
      </ul>

      <!-- Pagination -->
      <ul class="col list-pagination pagination pagination-tabs justify-content-center">
        <li v-for="(page, index) in pagination.pages" v-bind:key="index"
            v-bind:class="{ active: pagination.active_page === page }">
          <b-link v-if="Number.isInteger(page)" class="page" @click="setPage(page)">{{ page }}</b-link>
          <span class="page" v-else>{{ page }}</span>
        </li>
      </ul>

      <!-- Pagination (next) -->
      <ul class="col list-pagination-next pagination pagination-tabs justify-content-end">
        <li class="page-item">
          <a class="page-link" href="#">
            Next <i class="fe fe-arrow-right ml-1"></i>
          </a>
        </li>
      </ul>
    </b-row>

    <div class="list-alert alert alert-dark alert-dismissible border fade" v-bind:class="{show: bulk}" role="alert">

      <!-- Content -->
      <div class="row align-items-center">
        <div class="col">

          <!-- Checkbox -->
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="listAlertCheckbox" checked="" disabled="">
            <label class="custom-control-label text-white" for="listAlertCheckbox"><span
                class="list-alert-count">{{ selected.length }}</span> game(s)</label>
          </div>

        </div>
        <div class="col-auto mr-n3">

          <!-- Button -->
          <b-button size="sm" v-if="games.length > selected.length" @click="selectAll" class="btn-white-20">
            Select all
          </b-button>
          <b-button size="sm" v-else @click="unselectAll" class="btn-white-20">
            Unselect all
          </b-button>
          <b-button size="sm" class="btn-white-20" @click="checkoutGames">
            Check-out
          </b-button>

        </div>
      </div> <!-- / .row -->

      <!-- Close -->
      <button type="button" class="list-alert-close close" aria-label="Close">
        <span aria-hidden="true">×</span>
      </button>

    </div>

    <ModalPlayerSelect id="filter-players-modal"></ModalPlayerSelect>
  </div>
</template>

<script>
import gamesMixin from "@/mixins/games.mixin"
import libraryService from "@/services/library.service"
import Header from "@/components/Header";
import LibraryGameCard from "@/components/LibraryGameCard";
import ModalPlayerSelect from "@/components/ModalPlayerSelect";
import playerService from "@/services/player.service"
import CheckinModal from "@/components/CheckinModal";

export default {
  name: "Home",
  props: ['title', 'pretitle'],
  data() {
    return {
      search: '',
      games: [],
      loading: true,
      bulk: false,
      selected: [],
      pagination: {
        count: 0,
        count_per_page: 50,
        active_page: 1,
        pages: [],
        number_pages: 5
      },
      selectedGame: {
        game: {}
      },
      players: [],
      filters: this.initFilters(),
      filtersOpen: false,
      shelves_options: ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5'],
      availability_options: [],
      status_options: [
        {value: 'available', text: 'Available'},
        {value: 'not-available', text: 'Withdrawn'},
        {value: 'not-checked-in', text: 'Not checked-in'},
        {value: 'checked-out', text: 'Checked-out'}
      ],
    }
  },
  components: {CheckinModal, ModalPlayerSelect, LibraryGameCard, Header},
  mixins: [gamesMixin],
  mounted() {
    this.refreshGames()
  },
  methods: {
    initFilters() {
      return {}
    },
    selectAll() {
      this.selected = this.games.map(game => game.id)
    },
    unselectAll() {
      this.selected = []
    },
    updatePages() {
      this.pagination.pages = []

      let current = this.pagination.active_page,
          last = Math.ceil(this.pagination.count / this.pagination.count_per_page),
          delta = 2,
          left = current - delta,
          right = current + delta + 1,
          range = [],
          l;

      for (let i = 1; i <= last; i++) {
        if (i === 1 || i === last || i >= left && i < right) {
          range.push(i);
        }
      }

      for (let i of range) {
        if (l) {
          if (i - l === 2) {
            this.pagination.pages.push(l + 1);
          } else if (i - l !== 1) {
            this.pagination.pages.push('...');
          }
        }
        this.pagination.pages.push(i);
        l = i;
      }

    },
    setPage(number) {
      this.pagination.active_page = number
      this.refreshGames()
    },
    refreshGames() {
      this.pagination = this.paginationReset()

      let params = {}
      Object.keys(this.filters)
          .forEach(key => params[key] = Array.isArray(this.filters[key]) ? this.filters[key].toString() : this.filters[key])

      if (this.search)
        params['search'] = this.search

      libraryService.filterGames(params).then(response => {
        this.games = response.results
        this.pagination.count = response.count
        this.updatePages()
      })
    },
    searchPlayers(query) {
      playerService.searchPlayers(query).then(response => {
        this.players = response
      })
    },
    checkinGame(game) {
      this.games.map(item => {
            console.log(game)
            return item.id === game.id ? game : item
          }
      )
    },
    checkoutGames() {

      let promises = this.selected.map(id => libraryService.updateGame(id, {date_checkout: new Date(), location: ''}))

      Promise.all(promises).then(() => {
        this.$toast('Oh yeah!')
        this.bulk = false
        this.refreshGames()
      })
    },
    paginationReset() {
      return {
        count: 0,
        count_per_page: 50,
        active_page: 1,
        pages: [],
        number_pages: 5
      }
    },
    getParams() {
      let params = {}
      if (this.search) {
        params['search'] = this.search
      }

      Object.keys(this.filters)
          .forEach(key => params[key] = this.filters[key])

    }
  },
  watch: {
    search() {
      this.refreshGames()
    },
    filters: {
      handler: function () {
        this.refreshGames()
      },
      deep: true

    }
  },

}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>


.vs__dropdown-toggle {
  border: 1px solid #d2ddec !important;
  background-color: #ffffff !important;
  padding: .5rem .75rem .5rem .75rem !important;
  border-radius: .375rem !important;
}

.vs__selected, .vs__search {
  margin: 0 !important;
  padding: 0 !important;
}

.vs__actions {
  padding: 0 !important;
}
</style>
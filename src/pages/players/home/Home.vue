<template>
  <HomeScreenTemplate title="Players" pre-title="leiriacon">
<!--    <b-card no-body class="mt-5">-->
<!--      <b-card-header>-->
<!--        <b-input-group class="input-group-flush">-->
<!--          <div class="input-group-prepend">-->
<!--            <span class="input-group-text">-->
<!--              <b-icon-search font-scale="0.8" />-->
<!--            </span>-->
<!--          </div>-->
<!--          <b-form-input-->
<!--            class="list-search"-->
<!--            type="search"-->
<!--            placeholder="Search"-->
<!--          />-->
<!--        </b-input-group>-->
<!--      </b-card-header>-->
<!--      <b-table-->
<!--        hover-->
<!--        :fields="['name', 'email', 'last_login', 'groups', 'actions']"-->
<!--        :items="players"-->
<!--      >-->
<!--        <template #cell(last_login)="data">-->
<!--          <time-ago refresh v-if="data.item.last_login" long :datetime="data.item.last_login" locale="en"></time-ago>-->
<!--        </template>-->
<!--        <template #cell(groups)="data">-->
<!--          <b-badge variant="success" class="mr-3" v-if="data.item.is_staff" pill >Staff</b-badge>-->
<!--          <b-badge variant="info" pill v-for="(group, index) in data.item.groups" :key="index">{{group.name}}</b-badge>-->
<!--      </template>-->
<!--        <template #cell(actions)="data">-->
<!--          <b-button-->
<!--              variant="outline-info"-->
<!--              v-b-tooltip.hover title="Not implemented yet"-->
<!--              v-if="!isInGroup(data.item, 'Associate')" size="sm">Promote to Associate</b-button>-->
<!--        </template>-->
<!--      </b-table>-->
<!--    </b-card>-->

      <!-- Card -->
    <b-row class="align-items-center mb-3">
      <!-- Search -->
      <b-col>
        <l-search v-model="search" />
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="6" md="4" v-for="(player, index) in players.results" v-bind:key="index">
        <PlayerCard :player="player"/>
      </b-col>
    </b-row>
    <Pagination :current-page="currentPage" :total-count="players.count" @page-changed="pageChanged"></Pagination>

  </HomeScreenTemplate>
</template>

<script>
import HomeScreenTemplate from "@/components/templates/HomeScreenTemplate.vue"
import userService from "@/services/user.service"
import Pagination from "@/components/Pagination.vue"
import LSearch from "@/components/form/LSearch.vue"
import usersMixin from "@/mixins/users.mixin"
import PlayerCard from "@/pages/players/home/partials/player.vue"

export default {
  name: "PlayersHome",
  components: {PlayerCard, Pagination, HomeScreenTemplate, LSearch},
  mixins: [usersMixin],
  data(){
    return {
      search: '',
      currentPage: 1,
      players: {
        results: [],
        count: 0
      }
    }
  },
  mounted() {
    this.fetchPlayers()
  },
  methods: {
    pageChanged(page){
      this.currentPage = page
      this.fetchPlayers()
    },
    fetchPlayers(){
      userService.fetchUsers(this.getParams()).then((response) => this.players = response)
    },
    getParams() {
      let params = {}

      params['page'] = this.currentPage

      if (this.search) {
        params['search'] = this.search
      }
      params['page_size'] = this.$store.getters["pagination/pageSize"]

      return params
    },
  },
  watch: {
    search() {
      // anytime the search string is change we should reset page number
      // otherwise the user could face a 404 because the page is not available for the search results
      this.currentPage = 1

      this.fetchPlayers()
    },
  }
}
</script>

<style scoped>

</style>
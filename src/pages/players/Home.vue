<template>
  <HomeScreenTemplate title="Players" pre-title="leiriacon 2023">
    <b-card no-body class="mt-5">
      <b-card-header>
        <b-input-group class="input-group-flush">
          <div class="input-group-prepend">
            <span class="input-group-text">
              <b-icon-search font-scale="0.8" />
            </span>
          </div>
          <b-form-input
            class="list-search"
            type="search"
            placeholder="Search"
          />
        </b-input-group>
      </b-card-header>
      <b-table
        hover
        :fields="['name', 'email', 'last_login', 'groups', 'actions']"
        :items="players"
      >
        <template #cell(last_login)="data">
          <time-ago refresh v-if="data.item.last_login" long :datetime="data.item.last_login" locale="en"></time-ago>
        </template>
        <template #cell(groups)="data">
          <b-badge variant="success" class="mr-3" v-if="data.item.is_staff" pill >Staff</b-badge>
          <b-badge variant="info" pill v-for="(group, index) in data.item.groups" :key="index">{{group.name}}</b-badge>
      </template>
        <template #cell(actions)="data">
          <b-button
              variant="outline-info"
              v-b-tooltip.hover title="Not implemented yet"
              v-if="!isInGroup(data.item, 'Associate')" size="sm">Promote to Associate</b-button>
        </template>
      </b-table>
    </b-card>
  </HomeScreenTemplate>
</template>

<script>
import HomeScreenTemplate from "@/components/templates/HomeScreenTemplate"
import userService from "@/services/user.service"

import { TimeAgo } from 'vue2-timeago'

export default {
  name: "PlayersHome",
  components: {HomeScreenTemplate, TimeAgo},
  data(){
    return {
      players: []
    }
  },
  mounted() {
    userService.fetchUsers().then((players) => this.players = players)
  },
  methods: {
    isInGroup(user, groupName){
      return user.is_staff || user.groups.filter(group => group.name === groupName).length > 0
    }
  }
}
</script>

<style scoped>

</style>
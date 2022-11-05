<template>
  <b-card class="w-100">
          <!-- Header -->
          <div class="row align-items-center">
            <div class="col">

              <!-- Checkbox -->
<!--              <div class="form-check form-check-circle">-->
<!--                <input class="form-check-input list-checkbox" type="checkbox" id="cardsCheckboxOne">-->
<!--                <label class="form-check-label" for="cardsCheckboxOne"></label>-->
<!--              </div>-->

            </div>
            <div class="col-auto">

              <b-dropdown variant="link" no-caret>
                <template #button-content>
              <b-icon-three-dots-vertical/>
            </template>
                <b-dropdown-item-button @click.prevent="addQuota">Add paid quota</b-dropdown-item-button>
              </b-dropdown>
              <!-- Dropdown -->

            </div>
          </div> <!-- / .row -->

          <!-- Body -->
          <div class="text-center mb-5">

            <!-- Heading -->
            <h2 class="card-title">
              <a class="item-name" href="#">{{ player.name }}</a>
            </h2>

            <!-- Text -->
            <p class="small text-muted mb-3">
              <span class="item-title">{{player.email}}</span>
            </p>

            <!-- Buttons -->
            <b-badge variant="success" class="mx-1" v-if="player.is_staff" pill >Staff</b-badge>
            <b-badge variant="info" class="mx-1" pill v-for="(group, index) in player.groups" :key="index">{{group}}</b-badge>

          </div>

          <!-- Divider -->
          <hr class="card-divider mb-0" v-if="isUserInGroup(player, 'Associate')">

          <!-- List group -->
          <div class="list-group list-group-flush mb-n3" v-if="isUserInGroup(player, 'Associate')">
            <div class="list-group-item">
              <div class="row">
                <div class="col">

                  <!-- Text -->
                  <small>Quotas</small>

                </div>
                <div class="col-auto">
                  <!-- Text -->
                  <Quotas :quotas="player.quotas"/>
                </div>
              </div> <!-- / .row -->
            </div>
          </div>

          <b-button
              v-if="!player.groups.length"
              @click="addToGroup"
              variant="outline-info"
              block
          >Promote to associate</b-button>
      </b-card>
</template>

<script>
import usersMixin from "@/mixins/users.mixin"
import quotaService from "@/services/quota.service"
import Quotas from "@/components/user/Quotas.vue"
import userService from "@/services/user.service"

export default {
  name: "PlayerCard",
  components: {Quotas},
  mixins: [usersMixin],
  props: {'player': {
    required: true
    }
  },
  methods: {
    addToGroup(){
      userService.addToGroup(this.player.id, "Associate").then((response) => {
        this.emitUpdatedPlayer(response)
      })
    },
    addQuota(){
      let year
      if(this.player.quotas.length){
        year = this.player.quotas.reduce((a, b) => Math.max(a, b), -Infinity) + 1
      } else {
        year = new Date().getFullYear()
      }

      quotaService.create(this.player.id, year).then(() => {
        this.emitUpdatedPlayer()
      })
    },
    emitUpdatedPlayer(player){
      if(player){
        this.$emit("player-updated", player)
      } else {
        userService.fetchUser(this.player.id).then((response)=> {
          this.$emit("player-updated", response)
        })
      }
    }
  }
}
</script>

<style scoped>

</style>

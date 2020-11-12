<template>
  <div>
    <GameCard :game="game.game"
              :bulk="bulk">

      <!-- Image (or checkbox if enabled)-->
      <template v-slot:image>
        <div class="position-relative">
          <div v-if="bulk" class="p-0 position-absolute d-flex text-center justify-content-center align-items-center"
               style="background-color: rgba(255,255,255,0.9); z-index: 1; top:0; left:0; right:0;bottom:0;">

            <!--            <b-button v-if="Array.isArray(checked)" @click="click">{{ checked.includes(value) ? 'X' : 'O' }}</b-button>-->
            <!--            <b-button v-else :variant="checked ? 'outline-primary' : 'primary'" @click="$emit('input', !checked)">{{ checked ? 'X' : 'O' }}</b-button>-->
            <b-button v-if="game.status === 'available'" :pressed="checked.includes(value)" variant="outline-dark"
                      @click="click">
              <b-icon-check/>
            </b-button>
          </div>
          <b-avatar :src="game.game.thumbnail" size="lg" rounded></b-avatar>
        </div>
      </template>

      <!-- Buttons -->
      <template v-slot:top-right>
        <div v-if="isAuthenticated()" class="d-flex flex-row align-items-center flex-nowrap">
          <b-button size="sm" variant="white" :to=" {name: 'WithdrawGame', params: {id: game.id}}"
                    v-show="game.status === 'available'">
            <span class="text-muted">WITHDRAW</span>
          </b-button>
          <b-button v-b-modal.checkin-modal @click="$emit('checkin', game)"
                    v-show="game.status === 'not-checked-in'"
                    size="sm" variant="white">
            <span class="text-muted">CHECK-IN</span>
          </b-button>
          <b-button v-show="game.status === 'not-available'"
                    size="sm"
                    @click="returnGame(game)"
                    variant="white">
            <span class="text-muted">RETURN ({{ game.location }})</span></b-button>
        </div>

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
    <!--      <CheckinModal id="checkin-modal" :shelves="shelves_options" :game="selectedGame"-->
<!--                    v-on:checkin="checkinGame"></CheckinModal>-->
  </div>
</template>

<script>

import withdrawService from '@/services/withdraw.service'
import GameCard from "@/components/GameCard";
import usersMixin from "@/mixins/users.mixin";

export default {

  name: "LibraryGame",
  components: {
    GameCard
  },
mixins: [usersMixin],
  props: ['checked', 'value', 'game', 'bulk'],
  model: {
    prop: 'checked',
    event: 'input'
  },

  methods: {
    click() {
      let checked = [].concat(this.checked)
      if (checked.includes(this.value)) {
        checked.splice(checked.indexOf(this.value), 1)
      } else {
        checked.push(this.value)
      }
      this.$emit('input', checked)
    },
    returnGame(game) {
      withdrawService.returnGame(game.current_withdraw.id).then(() => {
        //TODO: emit to refresh games
        this.$toast.success('Success! Place on ' + game.location)
      })
    }
  }
}
</script>

<style scoped>

</style>
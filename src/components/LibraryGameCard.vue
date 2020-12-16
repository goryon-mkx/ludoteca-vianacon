<template>
  <div>
    <GameCard :bg-variant="bgVariant"
              :bulk="bulk"
              :game="game.game">

      <!-- Image (or checkbox if enabled)-->
      <template v-slot:image>
        <div class="position-relative">
          <div v-if="bulk" class="p-0 position-absolute d-flex text-center justify-content-center align-items-center"
               style="background-color: rgba(255,255,255,0.9); z-index: 1; top:0; left:0; right:0;bottom:0;">

            <b-button v-if="game.status === 'available'" :pressed="checked.includes(value)" variant="outline-dark"
                      @click="click">
              <b-icon-check/>
            </b-button>
          </div>

          <b-avatar :src="game.game.thumbnail" rounded size="lg"></b-avatar>
        </div>
      </template>

      <!-- Buttons -->
      <template v-slot:top-right>
        <div v-if="isAuthenticated()" class="d-flex flex-row align-items-center flex-nowrap">
          <b-button v-show="game.status === 'available'" :to=" {name: 'WithdrawGame', params: {id: game.id}}" size="sm"
                    variant="white">
            <span class="text-muted">WITHDRAW</span>
          </b-button>
          <b-button v-show="game.status === 'not-checked-in'" v-b-modal.checkin-modal
                    size="sm"
                    variant="white" @click="$emit('checkin', game)">
            <span class="text-muted">CHECK-IN</span>
          </b-button>
          <b-button v-show="game.status === 'not-available'"
                    size="sm"
                    variant="white"
                    @click="returnGame(game)">
            <span class="text-muted">RETURN ({{ game.location }})</span></b-button>

          <b-dropdown class="ml-1" no-caret size="sm" toggle-class="text-decoration-none" variant="white">
            <template #button-content>
              <b-icon-three-dots/>
            </template>
            <b-dropdown-item-button>Edit</b-dropdown-item-button>
            <b-dropdown-item-button>Checkout</b-dropdown-item-button>
          </b-dropdown>

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
          <CheckinModal id="checkin-modal" :shelves="shelves_options" :game="selectedGame"
                        v-on:checkin="checkinGame"></CheckinModal>
  </div>
</template>

<script>

import withdrawService from '@/services/withdraw.service'
import GameCard from "@/components/GameCard";
import usersMixin from "@/mixins/users.mixin";
import CheckinModal from "@/components/CheckinModal";

export default {

  name: "LibraryGame",
  components: {
    GameCard,
    CheckinModal
  },
  mixins: [usersMixin],
  props: ['checked', 'value', 'game', 'bulk', 'bgVariant'],
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
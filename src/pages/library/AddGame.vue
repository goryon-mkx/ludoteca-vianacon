<template>
  <div>
    <EndTemplateHeader title="New game" pretitle="library">
      <template v-slot:content-right>
        <b-button variant="white">
          <b-icon-gear-fill></b-icon-gear-fill>
        </b-button>

      </template>
    </EndTemplateHeader>
    <ModalGameSelect @game-selected="assignGame"
                     id="game-select-modal"></ModalGameSelect>
    <form>
      <b-form-group label="Game">
        <b-card v-if="!game.id" class="card-inactive">
          <div class="d-flex flex-row align-items-center justify-content-between"><span class="text-muted">No game selected</span>
            <b-button variant="secondary" v-b-modal.game-select-modal>Search games</b-button>
          </div>
        </b-card>
        <GameCard :game="game" v-else/>
      </b-form-group>
      <b-form-group label="Owner">
        <b-card v-if="!player.id" class="card-inactive">
          <div class="d-flex flex-row align-items-center justify-content-between"><span class="text-muted">No player selected</span>
            <b-button variant="secondary" v-b-modal.player-select-modal>Search players</b-button>
          </div>
        </b-card>
        <ItemCard v-else>
          <template v-slot:title>{{ player.name }}</template>
        </ItemCard>
      </b-form-group>
      <ModalPlayerSelect id="player-select-modal" @player-selected="assignPlayer"></ModalPlayerSelect>
      <b-form-group label="Shelf">
        <b-form-input v-model="game.shelf"></b-form-input>
      </b-form-group>
      <b-form-group label="Notes">
        <b-form-textarea></b-form-textarea>
      </b-form-group>

      <hr class="mt-5 mb-5"/>
      <b-row>
        <b-col>
          <b-form-group label="Check-in">
            <small class="text-muted form-text">If you have the game available to check-in</small>
            <b-form-checkbox v-model="checked" name="check-button" switch>
            </b-form-checkbox>
          </b-form-group>
        </b-col>
        <b-col>
          <b-card bg-variant="light" class="border">
            <div class="d-flex flex-row">
              <b-icon-exclamation-triangle></b-icon-exclamation-triangle>
              <h4 class="ml-1">Warning</h4>
            </div>
            <span class="text-muted small">Once the item is checked-in it will became available for withdraw</span>
          </b-card>
        </b-col>
      </b-row>
      <hr class="mt-5 mb-5"/>

      <b-row class="mt-3">
        <b-col sm="12" lg="12">
          <b-button variant="primary" size="lg" block>Save</b-button>
        </b-col>
      </b-row>
      <b-row class="mt-3">
        <b-col>
          <b-button variant="link" class="text-muted" size="lg" block>Cancel</b-button>
        </b-col>
      </b-row>

    </form>
  </div>
</template>

<script>
import ModalGameSelect from "@/components/ModalGameSelect";
import bggService from '@/services/bgg.service';
import ItemCard from "@/components/ItemCard";
import gamesMixin from "@/mixins/games.mixin";
import ModalPlayerSelect from "@/components/ModalPlayerSelect";
import GameCard from "@/components/GameCard";
import EndTemplateHeader from "@/components/EndTemplateHeader";

export default {
  name: "AddGame",
  components: {ModalPlayerSelect, ItemCard, ModalGameSelect, EndTemplateHeader, GameCard},
  mixins: [gamesMixin],
  data() {
    return {
      game: this.initGame(),
      games: [],
      options: {
        isMultipleGamesActive: false,
        isKeepOwnerActive: false,
        isAddMoreGamesActive: false
      },
      player: {}
    }
  },
  watch: {},
  methods: {
    initGame() {
      return {
        shelf: '',
        id: '',
        name: '',
      }
    },
    assignGame(game) {
      bggService.fetch(game.id).then(response => {
        this.game = response
        this.$bvModal.hide('game-select-modal')
      })
    },
    assignPlayer(player) {
      console.log(player)
      this.player = player
      this.$bvModal.hide('player-select-modal')
    }
  }
}
</script>

<style scoped>


</style>
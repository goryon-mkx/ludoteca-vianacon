<template>
  <InputScreen pre-title="library" title="New game">
    <template #header-actions>
      <b-button variant="white">
        <b-icon-gear-fill></b-icon-gear-fill>
      </b-button>
    </template>
    <template #content>

      <ModalGameSelect @game-selected="assignGame"
                       id="game-select-modal"></ModalGameSelect>
      <form>
        <b-form-group label="Game">
          <div v-if="!game.id" class="d-flex flex-row align-items-center justify-content-between">
            <span class="text-muted">No game selected</span>
            <b-button variant="outline-secondary" v-b-modal.game-select-modal>Search games</b-button>
          </div>

          <GameCard :game="game" v-if="!!game.id"/>
        </b-form-group>
        <b-form-group label="Owner">
          <div v-if="!player.id" class="d-flex flex-row align-items-center justify-content-between">
            <span class="text-muted">No player selected</span>
            <b-button variant="outline-secondary" v-b-modal.player-select-modal>Search players</b-button>
          </div>
          <PersonCard :person="player" v-else/>
        </b-form-group>
        <ModalPlayerSelect id="player-select-modal" @player-selected="assignPlayer"></ModalPlayerSelect>
        <b-form-group label="Shelf">
          <b-form-input v-model="library_game.location"></b-form-input>
        </b-form-group>
        <b-form-group label="Notes">
          <b-form-textarea v-model="library_game.notes"></b-form-textarea>
        </b-form-group>

        <hr class="my-5"/>
        <div class="d-flex flex-row justify-content-between mb-5">
          <b-button variant="white" size="lg" @click="createGame">Cancel</b-button>
          <b-button variant="primary" size="lg" @click="createGame">Create</b-button>

        </div>

      </form>

    </template>
  </InputScreen>

</template>

<script>
import ModalGameSelect from "@/components/ModalGameSelect";
import bggService from '@/services/bgg.service';
import libraryService from '@/services/library.service';
import PersonCard from "@/components/PersonCard";
import gamesMixin from "@/mixins/games.mixin";
import ModalPlayerSelect from "@/components/ModalPlayerSelect";
import GameCard from "@/components/GameCard";
import {required} from 'vuelidate/lib/validators'
import InputScreen from "@/components/templates/InputScreen";

export default {
  name: "AddGame",
  components: {InputScreen, ModalPlayerSelect, PersonCard, ModalGameSelect, GameCard},
  mixins: [gamesMixin],
  data() {
    return {
      game: this.initGame(),
      games: [],
      library_game: {
        location: '',
        owner_id: '',
        notes: '',
        game_id: ''
      },
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
        id: '',
        name: '',
        thumbnail: ''
      }
    },
    assignGame(game) {
      bggService.fetch(game.id).then(response => {
        this.game = response
        this.$bvModal.hide('game-select-modal')
      })
    },
    assignPlayer(player) {
      this.player = player
      this.$bvModal.hide('player-select-modal')
    },
    createGame() {
      this.library_game.game_id = this.game.id
      this.library_game.owner_id = this.player.id

      libraryService.createGame(this.library_game).then(response => {
        this.$toast.success(response.game.name + ' of ' + response.owner.name + ' added to the library in shelf ' + response.location)
        this.$router.push({name: 'Home'});
      }).catch(response => console.log(response))
    },
  },
  validations: {
    library_game: {
      location: {
        required
      }
    }
  }

}
</script>

<style scoped>


</style>
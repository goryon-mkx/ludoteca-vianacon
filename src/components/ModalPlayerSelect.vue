<template>
  <!-- Modal -->

  <ModalSelect :id="id" :title="title">
    <template v-slot:header>
      <div class="d-flex flex-row align-items-center">
        <b-button v-show="isNewPlayer" size="sm" variant="outline-secondary" @click="isNewPlayer=false">
          <b-icon-arrow-left></b-icon-arrow-left>
          back
        </b-button>
        <h4 v-show="isNewPlayer" class="mb-0">New player</h4>
      </div>
      <div v-show="!isNewPlayer" class="input-group input-group-merge">
        <b-form-input flush type="search" debounce="300" class="form-control form-control-prepended search"
                      placeholder="Search" v-model="search"/>
        <div class="input-group-prepend">
          <div class="input-group-text">
            <b-icon-search font-scale="0.8"></b-icon-search>
          </div>
        </div>

      </div>

      <!-- Close -->

    </template>

    <template v-slot:content>

      <div v-show="!isNewPlayer">
        <!-- Select player content -->

        <div class="list-group list-group-flush">
          <a v-on:click="$emit('player-selected', player)" href="#!"
             v-for="(player, index) in players" v-bind:key="index"
             class="list-group-item list-group-item-action px-0">
            <div class="d-flex flex-row align-items-center px-4">
              <div class="avatar avatar-sm">
                                                <span class="avatar-title rounded-circle"
                                                      v-text="initials(player.name)"></span>
              </div>
              <div class="d-flex flex-column ml-3">
                <span class="" v-text="player.name"></span>
                <span v-text="player.email" class="text-muted"></span>
              </div>
            </div>

          </a>
        </div>


      </div>

      <div v-if="isNewPlayer">


        <form novalidate>
          <div class="px-4 mt-4">
            <div class="form-group">
              <label>Name</label>
              <input type="text" class="form-control"
                     placeholder=" eg. John Doe" v-model="player.name"/>
            </div>

            <div class="form-group">

              <label>E-mail</label>
              <input type="text" class="form-control"
                     placeholder="eg. name@mail.com" v-model="player.email"/>

            </div>
          </div>
        </form>
      </div>

    </template>
    <template #footern>
      <button type="button" @click="doNewPlayer" class="btn btn-info">Create
        new player
      </button>

    </template>
  </ModalSelect>

</template>

<script>
import usersMixin from '@/mixins/users.mixin'
import playerService from '@/services/player.service'
import ModalSelect from "@/components/ModalSelect";

export default {
  name: "ModalPlayerSelect", mixins: [usersMixin],
  props: ['id', 'title'],
  components: {ModalSelect},
  data: function () {
    return {
      isNewPlayer: false,
      search: '',
      selectedPlayer: undefined,
      players: [],
      player: {
        name: '',
        email: ''
      }
    }
  },
  methods: {
    doNewPlayer(e) {
      e.preventDefault();
      this.player.name = this.search;
      this.isNewPlayer = true;
    },
    selectPlayer() {

    }
  },

  mounted() {
    playerService.fetchPlayers().then(response => this.players = response);
  }
}
</script>

<style scoped>

</style>

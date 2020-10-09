<template>
  <!-- Modal -->
  <ModalSelect :id="id" :title="title">
    <template v-slot:header>
      <div class="input-group input-group-merge">
        <b-form-input flush type="search" debounce="500" class="form-control form-control-prepended search"
                      placeholder="Search" v-model="search"/>
        <div class="input-group-prepend">
          <div class="input-group-text">
            <b-icon-search font-scale="0.8"></b-icon-search>
          </div>
        </div>
      </div>
    </template>
    <template v-slot:content>

      <!-- Select bgggame content -->
      <b-skeleton-wrapper :loading="false">

        <b-overlay :show="loading" rounded="sm">
          <b-list-group flush>
            <b-list-group-item button data-dismiss="modal" class="px-4" @click="gameSelected(game)" v-bind:key="index"
                               v-for="(game, index) in games">
              {{ game.name }} <span class="text-gray-600" v-if="game.year">({{ game.year }})</span>
            </b-list-group-item>
            <b-list-group-item class="px-4" v-show="games.length === 0 && !loading" >No games found</b-list-group-item>
          </b-list-group>
        </b-overlay>
      </b-skeleton-wrapper>
    </template>
  </ModalSelect>
</template>

<script>
import bggService from '@/services/bgg.service'
import ModalSelect from "@/components/ModalSelect";

export default {
  name: "ModalGameSelect",
  props: ['id', 'title'],
  components: {
    ModalSelect

  },
  data: function () {
    return {
      search: '',
      answer: '',
      games: [],
      loading: false
    }
  },
  watch: {
    search() {
      this.loading = true
      bggService.search(this.search).then(response => {
        this.loading = false
        this.games = response
      })
    }
  },
  created: function () {
  },
  methods: {
    calculateRank: function (data) {
      if (data) {
        let search = this.search.trim().toUpperCase();
        data = data.trim().toUpperCase();

        if (data === search) {
          return 3;
        } else if (data.startsWith(search)) {
          return 2;
        } else if (data.includes(search)) {
          return 1;
        }
      } else {
        return 0;
      }
    },

    gameSelected(game) {
      this.$emit('game-selected', game)
    },
  },
}


</script>

<style scoped>

</style>
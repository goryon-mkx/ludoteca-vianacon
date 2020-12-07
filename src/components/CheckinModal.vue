<template>
  <b-modal :id="id" title="Checkin">
    <template #modal-title>
      <h4 class="mb-0">{{game.game.name}}</h4>
    </template>
    <template #default>
      <b-row>
        <b-col>
          <b-form-group label="Shelf">
<!--            <v-select v-model="game.location" :options="shelves"></v-select>-->
          </b-form-group>
        </b-col>
      </b-row>
    </template>

    <template #modal-footer>
      <b-button variant="secondary" @click="$bvModal.hide(id)">
        Cancel
      </b-button>
      <b-button variant="primary" @click="checkin">
        OK
      </b-button>
    </template>
  </b-modal>
</template>

<script>
import libraryService from "@/services/library.service";

export default {
  name: "CheckinModal",
  props: ['id', 'game', 'shelves'],
  methods: {
    checkin() {
      libraryService.updateGame(this.game.id, {location: this.game.location})
          .then((response) => {
            this.$toast.success('Checked-in, place it on ' + this.game.location)
            this.$bvModal.hide(this.id)
            this.$emit('checkin', response.data)
          })
    }
  }
}
</script>

<style scoped>

</style>
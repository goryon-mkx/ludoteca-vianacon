<template>
  <b-modal :id="id" title="Checkin">
    <template #modal-title>
      <h4 class="mb-0">{{ game.game.name }}</h4>
    </template>
    <template #default>
      <b-row>
        <b-col>
          <b-form-group label="Shelf">
            <FormSelect
                v-model="selected"
                :options="$store.getters['library/locations']"
                option-text="name"
                option-value="id">
            </FormSelect>
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
import FormSelect from "@/components/FormSelect";

export default {
  name: "CheckinModal",
  components: {FormSelect},
  props: ['id', 'game', 'shelves'],
  data: function(){
    return {
      selected: ''
    }
  },
  methods: {
    checkin() {
      libraryService.updateGame(this.game.id, {location: this.selected})
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
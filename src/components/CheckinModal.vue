<template>
  <b-modal no-close-on-backdrop :id="id" :title="game.game.name">
    <template #default>
      <b-form>
        <b-form-group label="Shelf">
          <FormSelect
            v-model="location"
            :options="$store.getters['library/locations']"
            option-text="name"
            option-value="id"
          >
          </FormSelect>
        </b-form-group>
      </b-form>
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
import libraryService from '@/services/library.service'
import FormSelect from '@/components/FormSelect'

export default {
  name: 'CheckinModal',
  components: { FormSelect },
  props: ['id', 'game', 'shelves'],
  data: function() {
    return {
      selected: '',
    }
  },
  computed: {
    location:{
      get() {
        return this.game && this.game.location? this.game.location.id : null
      },
      set(value){
        this.selected = value
      }
    }
  },
  methods: {
    checkin() {
      libraryService
        .updateGame(this.game.id, {
          location_id: this.selected,
          date_checkin: new Date(),
          date_checkout: null
        })
        .then(response => {
          this.$toast.success(
            `Got it! ${response.game.name} on ${response.location.name}`
          )
          this.$bvModal.hide(this.id)
          this.$emit('done', response)
        })
    },
  },
}
</script>

<style scoped></style>

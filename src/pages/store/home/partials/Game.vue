<template>
  <l-game-card
    :game_id="game.id"
    :loading="loading"
    :title="game.game.name"
    :image="game.game.image"
  >
    <template #loading>
      <b-skeleton width="30%" />
      <div v-if="isAdmin()">
        <b-skeleton width="50%" />
      </div>
    </template>
    <template #content>
      <div v-if="isAdmin()">
        <div class="d-flex flex-row mt-2">
          <div class="d-flex flex-column flex-grow-1">
            <div>
              <span class="font-weight font-size-lg"
                >{{ game.selling_price }} €</span
              >
              <div v-if="game.discount_price > 0">
                <b-icon-award-fill class="font-size-lg text-warning mr-2" />
                <span class="font-size-lg text-warning"
                  >{{ game.discount_price }} €</span
                >
              </div>
            </div>

            <span class="text-muted">{{ game.stock }} available</span>
          </div>

          <b-dropdown
            right
            variant="link"
            toggle-class="text-decoration-none"
            no-caret
          >
            <template #button-content>
              <b-icon-three-dots-vertical
                class="text-dark mr-n3"
                font-scale="1"
              />
            </template>
            <b-dropdown-item v-b-modal="`modal-${game.id}`"
              >Edit</b-dropdown-item
            >
            <b-dropdown-item @click="deleteGame(game.id)"
              >Delete</b-dropdown-item
            >
          </b-dropdown>
        </div>
      </div>

      <div v-else>
        <span class="font-weight font-size-lg">{{ game.selling_price }} €</span>
        <br />
        <b-icon-award-fill class="font-size-lg text-warning mr-2" />
        <span class="font-size-lg text-warning"
          >{{ game.discount_price }} €</span
        >

        <span v-if="!game.is_available" class="small d-block text-danger">
          Sold out
        </span>
      </div>
      <b-modal
        :id="`modal-${game.id}`"
        :title="game.game.name"
        @ok="handleOk"
      >
        <b-form @submit="handleSubmit">
        <b-row>
          <b-col>
            <b-form-group class="max-width-2" label="Price">
          <l-form-input-currency v-model="form.selling_price" :state="validateState('selling_price')"/>
        </b-form-group>
          </b-col>
          <b-col>
            <b-form-group class="max-width-2" label="Discount Price" invalid-feedback="Invalid amount">
          <l-form-input-currency  v-model="form.discount_price" :state="validateState('discount_price')" />
        </b-form-group>
          </b-col>
        </b-row>
        <b-form-group class="max-width-2" label="Stock">
          <b-form-spinbutton min="0" v-model="form.stock" />
        </b-form-group>
</b-form>
      </b-modal>
    </template>
  </l-game-card>
</template>

<script>
import gamesMixin from '@/mixins/games.mixin'
import usersMixin from '@/mixins/users.mixin'
import formMixin from '@/mixins/form.mixins'
import storeService from '@/services/store.service'
import LGameCard from '@/components/cards/GameCard'
import LFormInputCurrency from "@/components/form/LFormInputCurrency"
import {minValue, numeric, required} from "vuelidate/lib/validators"

export default {
  name: 'StoreHomePartialGameCard',
  components: {
    LGameCard,
    LFormInputCurrency
  },
  props: {
    loading: {
      default: false,
      type: Boolean,
    },
    game: {
      default: () => {
        return {
          id: '',
          stock: 0,
          selling_price: 0,
          game: {
            image: '',
            name: '',
          },
          is_available: true,
        }
      },
      type: Object,
    },
    selectable: {
      default: false,
      type: Boolean,
    },
    selected: {
      default: false,
      type: Boolean,
    },
  },
  mixins: [gamesMixin, usersMixin, formMixin],
  data() {
    return {
      form: {
        stock: this.game.stock,
        selling_price: this.game.selling_price,
        discount_price: this.game.discount_price,
      },
    }
  },
  computed: {
    gameSelected: {
      get() {
        return this.selected
      },
      // eslint-disable-next-line no-unused-vars
      set(val) {
        this.$emit('selected-change', this.game.id)
      },
    },

    associate_discount() {
      let parcel = 1
      const configurations = this.$store.getters['configurations/all']
      if (configurations) {
        const configuration = configurations.filter(
          (conf) => conf.key === 'associate_discount',
        )[0]
        parcel = configuration.value
      }
      return parcel
    },
  },
  methods: {
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault()
      // Trigger submit handler
      this.handleSubmit()
    },
    handleSubmit(){
      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      storeService
        .updateGame(this.game.id, {
          stock: this.form.stock,
          selling_price: this.form.selling_price,
          discount_price: this.form.discount_price
        })
        .then((response) => {
          console.log('edit success')
          this.$bvModal.hide(`modal-${this.game.id}`)
          this.$emit('update', response)
        })
    },

    deleteGame(game_id) {
      storeService.deleteGame(game_id).then(() => {
        this.$emit('delete', game_id)
      })
    },
  },
  validations:{
    form: {
      selling_price: {
        required,
      },
      discount_price: {
        required,
      },
      stock: {
        required,
        numeric,
        minValue: minValue(0)
      },
    },
  }
}
</script>

<style scoped></style>

<template>
  <b-modal id="buy-tickets-modal" title="Buy Ticket" ok-title="Next" ok-only @ok.prevent="save">
    <b-form>
      <div v-show="currentStep==='personal-details'">
        <b-form-group label="Name">
          <b-input type="text"/>
        </b-form-group>
        <b-form-group label="E-mail">
          <b-input type="text"/>
        </b-form-group>
       </div>

      <div v-show="currentStep==='additional-tickets'">
        <h2>Additional Ticket</h2>
        <b-form-group label="Name">
          <b-input type="text"/>
        </b-form-group>
        <b-form-group label="E-mail">
          <b-input type="text"/>
        </b-form-group>
      </div>
    </b-form>
  </b-modal>
</template>

<script>
export default {
  name: "Modal",
  data(){
    return {
      steps: ["personal-details", "additional-tickets","summary"],
      currentStep: "personal-details"
    }
  },
  methods: {
    save(){
      this.currentStep = "additional-tickets"
    }
  }
}
</script>

<style scoped>

</style>

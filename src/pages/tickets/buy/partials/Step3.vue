<template>
<div>
  <b-card>
    <div class="mb-3">
      <ul class="list-group list-group-flush">
        <li v-for="(person, index) in tickets" v-bind:key="index" class="list-group-item d-flex align-items-center justify-content-between px-0">
          <div>
            <span>{{person.name}}</span>
            <b-icon-award-fill v-if="person.ticket.type==='membership'" class="ml-2 text-info"/>
          </div>
          {{ formatPrice(person.ticket.price) }}€
        </li>
        <li class="list-group-item d-flex align-items-center justify-content-between px-0">
          <span class="font-weight-bold font-size-lg">Total</span> <span class="font-weight-bold font-size-lg">{{formatPrice(total)}}€</span>
        </li>
      </ul>
    </div>
  </b-card>
</div>
</template>

<script>
import {formatPrice} from "@/utils/number.utils"

export default {
  name: "step3",
  props: ['tickets'],
  methods: {
    formatPrice: formatPrice
  },
  data(){
    return {

    }
  },
  computed: {
    total(){
      let value = 0
      this.tickets.forEach(person => value += person.ticket.price)
      return value
    }
  }
}
</script>

<style scoped>

</style>

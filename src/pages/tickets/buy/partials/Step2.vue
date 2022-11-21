<template>
  <div>
    <b-form>
      <div
          class="input-group input-group-lg my-3 input-group-merge"
          v-for="(name, index) in names"
          v-bind:key="index">
        <b-form-input
            :tabindex="index+1"
            size="lg"
            v-model="names[index]"
            class="form-control-appended form-control-prepended"
            placeholder="Enter name"
            type="text"
            @update="onUpdate(index, $event)"
        />
      <div class="input-group-prepend">
        <div class="input-group-text">
          <b-icon-person-fill font-scale="1"/>
        </div>
      </div>
      <div class="input-group-append">
        <div class="input-group-text">
          <b-link>
          <b-icon-x v-if="names[index]" @click="clear(index)" />
            </b-link>
        </div>
      </div>
      </div>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "step2",
  props: ['value'],
  data(){
    return {
      editingPlayerIndex: 0,
      isAddingPlayer: false,
    }
  },
  computed:{
    names: {
      get(){
        return this.value
      },
    }
  },
  methods: {
    clear(index){
      this.names.splice(index, 1)
      if(this.names.filter(Boolean).length === this.names.length) {
        this.addName()
      }
    },
    onUpdate(index, value){
      if(value && this.names.length === index +1) {
        this.addName()
      }
      this.$emit('input',this.names)
    },
    addName(){
      if(this.names.length < 3) {
        this.names.push("")
      }
    }
  }
}
</script>

<style scoped>

</style>

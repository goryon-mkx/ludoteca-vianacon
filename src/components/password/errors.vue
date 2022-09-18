<template>
  <div>
    <div class="text-danger" v-for="(value, index) in errors" v-bind:key="index" >
      <b-icon-x/> <span>{{value}}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "PasswordErrors",
  props: {
    "errors":{
      type: Array
    }
  }
}
</script>

<style scoped>

</style>
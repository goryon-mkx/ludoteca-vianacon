<template>
    <b-form-group :label="label">
      <slot></slot>
    </b-form-group>
</template>

<script>
export default {
  name: "FilterItem",
  props: {
    label: {
      type: String,
      required: true
    }
  },
}
</script>

<style scoped>

</style>

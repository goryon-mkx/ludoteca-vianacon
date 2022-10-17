<template>
  <FilterItem :label="label">
    <b-input-group>
      <b-form-input v-model="filtersModel.filtersSelected['min_'+id]" debounce="500" placeholder="Min" aria-label="Min"/>
      <b-form-input v-model="filtersModel.filtersSelected['max_'+id]" debounce="500" placeholder="Max" aria-label="Max"/>
  </b-input-group>
  </FilterItem>
</template>

<script>
import FilterItem from "@/components/filters/FilterItem.vue"
import Filters from "@/components/filters/Filters.vue"

export default {
  name: "FilterRange",
  components: {FilterItem},
  props: {
    value: {
      type: Filters.Model,
      required: true,
    },
    id: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      default: '',
    },
  },
  computed: {
    filtersModel() {
      return this.value
    },
  },
}
</script>

<style scoped>

</style>
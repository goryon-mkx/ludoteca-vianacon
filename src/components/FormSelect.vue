<template>
  <div>
    <v-select v-model="selected"
              :label="optionText"
              :options="options"
              :placeholder="placeholder"
              :value="optionValue"
              :reduce="option => option[optionValue]"
              :class="{'is-invalid': state === false}"
              @search="$emit('search', $event)"
    >
    </v-select>

  </div>
</template>

<script>

export default {
  name: "FormSelect",
  components: {},
  props: {
    reduce: {
      type: Function,
    },
    value: {},
    state: {
      type: Boolean,
      default: null
    },
    options: {
      type: Array,
      default: () => []
    },
    optionText: {
      type: String,
      default: 'name'
    },
    optionValue: {
      type: String,
      default: 'id'
    },
    placeholder: {
      type: String,
      default: 'Select an option'
    }
  },
  data: () => {
    return {
      selected: ''
    }
  },
  watch: {
    selected: function (val) {
      this.$emit('input', val)
    }
  }
}
</script>

<style>
.vs__dropdown-toggle:has(.vs__search:focus) {
  border-color: #2c7be5 !important;
}

.vs__dropdown-toggle {
  border: 1px solid #d2ddec !important;
  background-color: #ffffff !important;
  padding: .5rem .75rem .5rem .75rem !important;
  border-radius: .375rem;
}

.vs__selected, .vs__search {
  margin: 0 !important;
  padding: 0 !important;
}

.vs__actions {
  padding: 0 !important;
}


.v-select input::-webkit-input-placeholder {
  color: #b1c2d9 !important;
  opacity: 1
}

.v-select input::-moz-placeholder {
  color: #b1c2d9 !important;
  opacity: 1
}

.v-select input::-ms-input-placeholder {
  color: #b1c2d9 !important;
  opacity: 1
}

.v-select input::placeholder {
  color: #b1c2d9 !important;
  opacity: 1
}

.vs--open .vs__dropdown-toggle {
  border-bottom-left-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}

.vs__dropdown-menu {
  border-top-width: 1px;
  border-color: #d2ddec !important;
  box-shadow: none !important;
}

.v-select.is-invalid .vs__dropdown-toggle{
  border-color: red !important;
}

.v-select.is-invalid .vs__dropdown-menu{
  border-color: red !important;
}


</style>
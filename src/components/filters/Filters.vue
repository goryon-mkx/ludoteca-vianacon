<template>
  <!-- Filters -->
  <b-row>
    <b-col>
      <b-collapse :id="collapseId">
        <div class="bg-primary-soft rounded p-4">
          <b-row>
            <b-col cols="12" md="6">
              <slot></slot>
            </b-col>

            <b-col cols="12" md="6">
              <b-form-group label="Order by">
                <b-input-group class="mb-2">
                  <b-form-select v-model="sortByField" :options="sortOptions" />
                  <b-input-group-append>
                    <b-button
                      variant="dark"
                      @click="setOrder('asc')"
                      v-if="filtersModel.sortBy.order === 'desc'"
                      ><b-icon-sort-down
                    /></b-button>
                    <b-button
                      variant="dark"
                      @click="setOrder('desc')"
                      v-if="filtersModel.sortBy.order === 'asc'"
                      ><b-icon-sort-down-alt
                    /></b-button>
                  </b-input-group-append>
                </b-input-group>
              </b-form-group>
              <b-form-group label="Page size">
                  <b-form-select @change="$emit('page-size-change')" v-model="pageSize" :options="[6, 30, 60]" />
              </b-form-group>
            </b-col>
            <div class="d-flex w-100 flex-row justify-content-end">
              <b-link class="text-gray-800" @click="clearFilters">
                <b-icon-x />
                RESET
              </b-link>
            </div>
          </b-row>
        </div>
      </b-collapse>
    </b-col>
  </b-row>
</template>

<script>
import usersMixin from '@/mixins/users.mixin'

export default {
  name: 'Filters',
  mixins: [usersMixin],
  props: {
    value: {
      type: FiltersModel,
      required: true,
    },
    collapseId: {
      type: String,
      default: 'filters-collapse',
    },
    sortOptions: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    filtersModel: {
      get() {
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      },
    },
    sortByField: {
      get() {
        return this.filtersModel.sortBy.fields
      },
      set(value) {
        this.filtersModel.sortBy.fields = value
      },
    },
    pageSize:{
      get() {
        return this.$store.getters["pagination/pageSize"]
      },
      set(value) {
        this.$store.dispatch("pagination/setPageSize", value)
      },
    }
  },
  methods: {
    setOrder(value) {
      this.filtersModel.sortBy.order = value
    },
    clearFilters() {
      this.filtersModel.clear()
      this.$emit('input', this.filtersModel)
    },
  },
  Model: FiltersModel,
}

function FiltersModel() {
  this.filtersSelected = {}
  this.sortBy = {
    fields: 'game__name',
    order: 'asc',
  }
}

FiltersModel.prototype.count = function () {
  return Object.values(this.filtersSelected).filter((value) => !!value).length
}

FiltersModel.prototype.clear = function () {
  this.filtersSelected = {}
  this.sortBy = {
      fields: 'game__name',
      order: 'asc',
  }
}
</script>

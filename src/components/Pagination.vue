<template>
  <!-- Pagination -->
  <b-row v-show="totalCount > perPage" no-gutters>
    <!-- Pagination (prev) -->
    <ul
      class="col list-pagination-prev pagination pagination-tabs justify-content-start"
    >
      <li class="page-item">
        <b-link class="page-link" href="#" :disabled="currentPage === 1"
        @click="setPage(currentPage-1)">
          <i class="fe fe-arrow-left mr-1"/><span class="d-none d-md-inline-block"> Previous</span>
        </b-link>
      </li>
    </ul>

    <!-- Pagination -->
    <ul
      class="col list-pagination pagination pagination-tabs justify-content-center"
    >
      <li
        v-for="(page, index) in pages"
        v-bind:key="index"
        v-bind:class="{ active: currentPage === page }"
      >
        <b-link
          v-if="Number.isInteger(page)"
          class="page"
          @click="setPage(page)"
          >{{ page }}</b-link
        >
        <span v-else class="page">{{ page }}</span>
      </li>
    </ul>

    <!-- Pagination (next) -->
    <ul
      class="col list-pagination-next pagination pagination-tabs justify-content-end"
    >
      <li class="page-item">
        <b-link :disabled="currentPage===lastPage" class="page-link" href="#" @click="setPage(currentPage+1)">
          <span class="d-none d-md-inline-block">Next</span> <i class="fe fe-arrow-right ml-1"></i>
        </b-link>
      </li>
    </ul>
  </b-row>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    currentPage: {
      type: Number,
      required: true
    },
    totalCount: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      pages: [],
    }
  },
  computed: {
    perPage(){
      return this.$store.getters["pagination/pageSize"]
    },
    lastPage() {
      return Math.ceil(this.totalCount / this.perPage)
    },
  },
  beforeUpdate() {
    this.updatePages()
  },
  methods: {
    updatePages() {
      this.pages = []

      let current = this.currentPage,
        last = this.lastPage,
        delta = 2,
        left = current - delta,
        right = current + delta + 1,
        range = [],
        l

      for (let i = 1; i <= last; i++) {
        if (i === 1 || i === last || (i >= left && i < right)) {
          range.push(i)
        }
      }

      for (let i of range) {
        if (l) {
          if (i - l === 2) {
            this.pages.push(l + 1)
          } else if (i - l !== 1) {
            this.pages.push('...')
          }
        }
        this.pages.push(i)
        l = i
      }
    },
    setPage(number) {
      this.$emit("page-changed", number)
    },
  },
}
</script>

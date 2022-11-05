<template>
  <div>
      <span v-if="numberOfQuotasDue === 0" class="text-success font-weight-normal"><b-icon-check-circle-fill/></span>
      <span v-else-if="numberOfQuotasDue < 0" class="text-success font-weight-normal">{{this.getLastPaidQuota(this.quotas)}} <b-icon-check-circle-fill/> </span>
      <span v-else class="text-warning font-weight-normal">{{numberOfQuotasDue}} due</span>
  </div>
</template>

<script>
import usersMixin from "@/mixins/users.mixin"

export default {
  name: "Quotas",
  mixins: [usersMixin],
  props: {
    quotas: {
    }
  },
  computed: {
    numberOfQuotasDue() {
      return this.getNumberOfQuotasDue(this.quotas)
    },
  }
}
</script>

<style scoped>

</style>

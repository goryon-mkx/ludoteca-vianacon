<template>
  <b-card>
    <div class="d-flex column align-items-center w-100">
      <div>
         <i style="font-size: 3rem;" class="bi-ticket-detailed-fill text-info" role="img" aria-label="GitHub"/>
      </div>
      <div class="ml-3 flex-1">
          <p class="font-size-lg mb-0">{{$store.getters["users/current"].name }}</p>
          <p class="text-muted mb-0">Member</p>
      </div>
      <span class="ml-auto" style="font-size: 2rem; font-weight: 200">
          5€
      </span>
    </div>
  </b-card>
</template>

<script>
export default {
  name: "step1"
}
</script>

<style scoped>

</style>

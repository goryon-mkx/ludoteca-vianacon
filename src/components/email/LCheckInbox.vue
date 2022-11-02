<template>
  <div>
    <b-alert variant="info" show><b-icon-inbox-fill class="mr-2" small/> Check your inbox</b-alert>

    <span class="mb-3">
      {{ description }}
    </span>
    </div>
</template>

<script>
export default {
  name: "LCheckInbox",
  props: ['description']
}
</script>

<style scoped>

</style>

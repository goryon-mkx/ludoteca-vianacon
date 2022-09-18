<template>
  <AuthTemplate pretitle="404 error" title="There’s no page here 😭" illustration="img/illustrations/lost.svg">
    <template #content>
<div class="text-center">


      <!-- Subheading -->
      <p class="text-muted mb-4">
        Looks like you ended up here by accident?
      </p>

      <!-- Button -->
      <b-button variant="primary" :to="{name: 'LibraryHome'}" class="btn-lg btn-primary">
        Return to your dashboard
      </b-button>
  </div>
    </template>
</AuthTemplate>
</template>

<script>
import AuthTemplate from "@/pages/auth/AuthTemplate"
export default {
  name: "NotFound",
  components: {AuthTemplate}
}
</script>

<style scoped>

</style>
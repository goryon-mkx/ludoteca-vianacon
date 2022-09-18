<template>
  <div class="min-vh-100 d-flex align-items-center bg-auth border-top border-top-2 border-primary">


    <b-container>
      <b-row class="align-items-center">
        <b-col class="col-12 col-md-6 offset-xl-2 offset-md-1 order-md-2 mb-5 mb-md-0">

          <!-- Image -->
          <div class="text-center">
            <b-img :src="require(`@/assets/${illustration}`)" alt="..." class="img-fluid"/>
          </div>

        </b-col>
        <div class="col-12 col-md-5 col-xl-4 order-md-1 my-5">

          <!-- Preheading -->
          <h6 v-if="pretitle" class="text-uppercase text-center text-muted mb-4">
            {{ pretitle }}
          </h6>

          <!-- Heading -->
          <h1 class="display-4 text-center mb-3">
            {{ title }}
          </h1>

          <!-- Subheading -->
          <p class="text-muted text-center mb-5">
            {{ subtitle }}
          </p>

          <slot name="content">

          </slot>

        </div>
      </b-row> <!-- / .row -->
    </b-container> <!-- / .container -->

  </div>

</template>

<script>

export default {
  name: "AuthTemplate",
  props: ["title", "subtitle", "pretitle", "illustration"],
  data(){
    return {

    }
  },
  methods: {
    onSubmit() {

      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      this.$emit("submit")
    },
  },
}
</script>

<style scoped>

</style>
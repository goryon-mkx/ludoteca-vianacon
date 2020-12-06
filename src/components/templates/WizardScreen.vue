<template>
  <b-container>

    <b-row class="justify-content-center mt-4">
      <b-col>

        <b-button :to="backTo">
          <b-icon-arrow-left/>
          back
        </b-button>
      </b-col>
      <b-col class="text-center d-flex align-items-center" cols="auto">

        <!-- Pretitle -->
        <h6 class=" text-uppercase text-muted">
<!--          {{ preTitle }}-->
        </h6>

      </b-col>
      <b-col class="d-flex justify-content-end align-items-start">
        <UserInfo/>
      </b-col>
    </b-row>

    <b-row class="justify-content-center mt-3">
      <b-col>

      </b-col>
      <b-col class="text-center" cols="auto">


        <!-- Title -->
        <h1 class="mb-3">
          {{ title }}
        </h1>

        <!-- Subtitle -->
<!--        <p class="mb-5 text-muted">-->
<!--          {{ subTitle }}-->
<!--          Yay! A new game full of stories available to play and have fun!-->
<!--        </p>-->
      </b-col>
      <b-col class="d-flex justify-content-end align-items-start">

      </b-col>
    </b-row>

    <b-row class="justify-content-center mt-3">
      <b-col lg="10" md="12" sm="12" xl="8">

        <slot name="content"></slot>
      </b-col>
    </b-row>


  </b-container>
</template>

<script>
import UserInfo from "@/components/UserInfo";

export default {
  name: "InputScreen",
  components: {UserInfo},
  props: {
    preTitle: {},
    title: {},
    subTitle: {},
    backTo:{
      type: Object
    }
}
}
</script>

<style scoped>

</style>
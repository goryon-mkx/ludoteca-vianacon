<template>
  <b-container>
    <!--        <div class="header">-->
    <!--          <div class="header-body">-->
    <!--            <b-row class="align-items-center justify-content-center">-->
    <!--              <b-col class="d-flex flex-column">-->
    <!--                <h6 class="header-pretitle">-->
    <!--                  {{ preTitle }}-->
    <!--                </h6>-->

    <!--                <h1 class="header-title">-->
    <!--                  {{ title }}-->
    <!--                </h1>-->
    <!--              </b-col>-->

    <!--              <div class="col-auto">-->
    <!--                <slot name="header-actions"></slot>-->
    <!--              </div>-->
    <!--            </b-row>-->

    <!--          </div>-->
    <!--        </div>-->

    <b-row class="justify-content-center mt-5">

      <div class="col-12 col-md-10 col-lg-8 col-xl-6 text-center">

        <!-- Pretitle -->
        <h6 class="mb-4 text-uppercase text-muted">
          {{ preTitle }}
        </h6>

        <!-- Title -->
        <h1 class="mb-3">
          {{ title }}
        </h1>

        <!-- Subtitle -->
        <p class="mb-5 text-muted">
          {{ subTitle }}
          Select a player from the list or create a new one if not existing
        </p>

      </div>
    </b-row>

<b-row class="justify-content-center">
  <b-col cols="12" md="10" lg="8" xl="6">
        <slot name="content"></slot>
  </b-col>
</b-row>


  </b-container>
</template>

<script>
export default {
  name: "InputScreen",
  props: ['preTitle', 'title', 'subTitle']
}
</script>

<style scoped>

</style>
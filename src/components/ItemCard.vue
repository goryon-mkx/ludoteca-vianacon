<template>
  <b-card class="card border border-1" :bg-variant="variant">
    <div class="media">
      <!-- left content-->
      <div class="media-left mr-3">
        <slot name="image"></slot>
      </div>

      <!-- body -->
      <div class="media-body">
        <div class="d-flex flex-row">

          <!-- middle content -->
          <div class="d-flex flex-column flex-grow-1">
            <!-- First line -->
            <div class="d-flex justify-content-between">
              <div class="mt-1 d-flex flex-row align-items-center">
                <h4 class="mb-0">
                  <slot name="title"></slot>
                </h4>
                <slot name="badges"></slot>
              </div>
              <div class="d-flex flex-row">
                <slot name="top-right"></slot>
              </div>
            </div>

            <!-- Second line -->
            <div class="d-flex justify-content-between align-items-center">
              <div class="mt-2">
                <slot name="metadata"></slot>
              </div>

              <div class="d-flex flex-row">
                <slot name="bottom-right"></slot>
              </div>
            </div>

          </div>

          <!-- right content-->
          <div class="d-flex align-items-center">
            <slot name="right"></slot>
          </div>
        </div>
      </div>


    </div>

  </b-card>
</template>

<script>
export default {
  name: "ItemCard",
  props: {
    variant: {
      type: String,
      default: 'default',
    }
  }
}
</script>

<style scoped>

</style>
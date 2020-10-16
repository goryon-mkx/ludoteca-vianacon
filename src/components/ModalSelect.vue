<template>
  <!-- Modal -->
  <b-modal :id="id" :title="title" body-class="p-0" hide-footer scrollable>
    <template v-slot:modal-header>
      <slot name="header"></slot>
    </template>
    <template v-slot:default>
      <div style="height: 400px">
      <slot name="content"></slot>
      </div>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: "ModalSelect",
  props: ['id', 'title']
}
</script>

<style scoped>

</style>
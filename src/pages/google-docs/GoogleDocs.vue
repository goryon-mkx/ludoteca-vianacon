<template>
  <div style="min-height:100vh">
    <TopNav/>
      <iframe
          :src="url"
          width="100%" style="overflow:hidden;min-height:calc(100vh - 4.25rem);width:100%" height="100%" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>

</div>
</template>

<script>
import TopNav from "@/components/TopNav"
export default {
  name: 'GoogleDocs',
  props: ['title', 'pretitle'],
  components: {
    TopNav
  },
  computed: {
    url(){
      const base_url =  "https://docs.google.com/spreadsheets/u/0/d/1lHZ6OA-yshGf8GgxmFI-IXygkEvq5a7SZdDl2U8bCcI/edit?embedded=true"
      return base_url + (this.$route.query.page ? `#gid=${this.$route.query.page}` : '')
    }
  }
}
</script>
<style lang="scss"></style>

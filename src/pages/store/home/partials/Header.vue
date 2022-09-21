<template>
    <Header :pretitle="pretitle" :title="title">
      <template v-slot:content-right>
        <div v-if="isStaff()">
          <b-dropdown class="mr-3" no-caret variant="white">
            <template #button-content>
              <b-icon-gear />
            </template>
            <b-dropdown-item-button v-show="!bulk" @click="$emit('bulk-change', true)">
              Enable God mode
            </b-dropdown-item-button>
            <b-dropdown-item-button v-show="bulk" @click="$emit('bulk-change', false)">
              Disable God mode
            </b-dropdown-item-button>
          </b-dropdown>
          <b-button :to="{ name: 'AddLibraryGame' }" variant="primary">
            <b-icon-plus class="mr-2"></b-icon-plus>
            Add game
          </b-button>
        </div>
      </template>
    </Header>
</template>

<script>
import gamesMixin from "@/mixins/games.mixin"
import usersMixin from "@/mixins/users.mixin"
import Header from "@/components/Header"
import {Game} from "@/enums/permissions.enum"

export default {
  name: "StoreHeader",
  components: {
    Header
  },
  data(){
    return {
      permissions: Game.Store
    }
  },
  props: ['title', 'pretitle', 'bulk'],
  mixins: [gamesMixin, usersMixin],
}
</script>

<style scoped>

</style>
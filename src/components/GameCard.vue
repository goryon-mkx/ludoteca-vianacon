<template>
  <ItemCard>
    <template v-slot:image>
      <b-avatar :src="game.thumbnail" size="lg" rounded></b-avatar>
    </template>
    <template v-slot:title><span class="text-truncate">{{ game.name }}</span></template>
    <template v-slot:badges>
      <span v-for="(badge, index) in game.badges" v-bind:key="index" class="ml-2 badge" v-bind:class="{
      'badge-soft-primary': badge.label === 'Recomendado',
      'badge-soft-success': badge.label === 'Jogo do Ano'
      }"
      >{{ badge.label }}</span>
    </template>
    <template v-slot:metadata>
      <b-icon-person-fill class="text-muted fe fe-users mr-2"></b-icon-person-fill>

      <span class=" text-muted">{{ num_players(game.min_players, game.max_players) }}</span>
      <b-icon-clock-fill font-scale="0.8" class="ml-4 mr-2 text-muted fe fe-clock"></b-icon-clock-fill>
      <span class=" text-muted">{{ playtime(game.min_playtime, game.max_playtime) }} </span>
    </template>
    <template v-slot:top-right>
      <slot name="top-right"></slot>
    </template>
    <template v-slot:bottom-right>
      <slot name="bottom-right"></slot>
    </template>
    <template v-slot:right>
      <slot name="right"></slot>
    </template>
  </ItemCard>
</template>

<script>
import ItemCard from "@/components/ItemCard";
import gamesMixin from "@/mixins/games.mixin"

export default {
  name: "GameCard",
  props: ['game'],
  mixins: [gamesMixin],
  components: {
    ItemCard
  }
}
</script>

<style scoped>

</style>
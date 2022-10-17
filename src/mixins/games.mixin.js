export default {
  methods: {
    playtime: function (min, max) {
      return this.range(min, max)
    },
    num_players: function (min, max) {
      return this.range(min, max)
    },
    range: function (min, max) {
      if (!min) {
        return max
      } else if (!max) {
        return min
      } else if (min === max) {
        return min
      } else {
        return min + ' - ' + max
      }
    },
  },
}

import { bggApi } from '@/services/bgg-api'

export default {
  search,
  fetch,
}

const API_URL = 'https://www.boardgamegeek.com/xmlapi2'

function search(search) {
  return bggApi
    .get('/', {
      params: {
        url: API_URL + `/search?type=boardgame&query=${search}`
      },
    })
    .then((response) => {
      if (!response.items || !response.items.item) {
        return []
      }
      let items = response.items.item

      // When only one result is returned by API for some reason it doesn't return as an Array ¯\_(ツ)_/¯
      if (!Array.isArray(items)) {
        items = [items]
      }

      items = items.map((item) => {
        item.name = getGameName(item)
        item.rank = calculateRank(item.name, search)
        return item
      })

      items.sort((a, b) => b.rank - a.rank)

      items = items.slice(0, 30)

      return items.map((item) => mapGame(item))
    })
}

function fetch(id) {
  return bggApi
    .get('/', {
      params: {
        url: API_URL + `/thing?id=${id}`
        // type: 'boardgame',
      },
    })
    .then((response) => {
      if (!response.items || !response.items.item) {
        return {}
      }

      let game = response.items.item

      game.name = getGameName(game)

      return mapGame(response.items.item)
    })
}

function mapGame(game) {
  if(!game.$?.id) console.log(game)
  return {
    id: game.$?.id,
    name: game.name,
    year: game.yearpublished?.$?.value ?? '',
    thumbnail: game.thumbnail ? game.thumbnail : '',
    min_players: game.minplayers ? game.minplayers.value : '',
    max_players: game.maxplayers ? game.maxplayers.value : '',
    min_playtime: game.minplaytime ? game.minplaytime.value : '',
    max_playtime: game.maxplaytime ? game.maxplaytime.value : '',
    rank: game.rank,
  }
}

function calculateRank(name, search) {
  if (name) {
    search = search.trim().toUpperCase()
    name = name.trim().toUpperCase()

    if (name === search) {
      return 4
    } else if (name.startsWith(search)) {
      return 3
    } else if (name.includes(search)) {
      return 2
    } else {
      return 1
    }
  } else {
    return 0
  }
}

function getGameName(game) {
  /*
  "name": {
    "$": {
      "type": "primary",
      "value": "Cambodia (fan expansion for Ticket to Ride)"
    }
  },
  */

  //console.log(Object.values(game.name))

  let result = Object.values(game.name).find(obj => obj.type === "primary")

  if(!result)
    result = Object.values(game.name)[0]

  return result.value
}

//function decodeHTML(value) {
//  return new DOMParser()
//    .parseFromString(value, 'text/html')
//    .querySelector('html').textContent
//}

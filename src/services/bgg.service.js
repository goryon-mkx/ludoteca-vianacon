import {bggApi} from "@/services/bgg-api";

export default {
    search,
    fetch
};

function search(search) {
    return bggApi.get("/search/", {
        params: {
            type: 'boardgame',
            query: search
        }
    }).then(response => {
        if (!response.items || !response.items.item) {
            return [];
        }
        let items = response.items.item;

        items.sort((a, b) => {
            return calculateRank(b.name.value, search) - calculateRank(a.name.value, search)
        });

        items = items.slice(0, 20);

        return items.map(item => mapGame(item))
    })
}

function fetch(id) {
    return bggApi.get('/thing/', {
        params: {
            // type: 'boardgame',
            id: id
        }
    }).then(response => {
        if (!response.items || !response.items.item) {
            return {};
        }
        return mapGame(response.items.item);
    })
}

function mapGame(game) {
    return {
        id: game.id,
        name: Array.isArray(game.name) ? game.name[0].value : game.name.value,
        year: game.yearpublished ? game.yearpublished.value : '',
        thumbnail: game.thumbnail ? game.thumbnail : '',
        min_players: game.minplayers ? game.minplayers.value : '',
        max_players: game.maxplayers ? game.maxplayers.value : '',
        min_playtime: game.minplaytime ? game.minplaytime.value : '',
        max_playtime: game.maxplaytime ? game.maxplaytime.value : '',
    }
}

function calculateRank(name, search) {
    if (name) {
        search = search.trim().toUpperCase();
        name = name.trim().toUpperCase();

        if (name === search) {
            return 3;
        } else if (name.startsWith(search)) {
            return 2;
        } else if (name.includes(search)) {
            return 1;
        }
    } else {
        return 0;
    }
}
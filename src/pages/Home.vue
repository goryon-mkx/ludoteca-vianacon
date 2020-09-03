<template>
    <div>


        <div class="row">
            <div class="col-12">
                <div class="">
                    <div class="input-group input-group-rounded input-group-merge mb-4">
                        <!-- Input -->
                        <input type="search" class="form-control form-control-prepended  dropdown-toggle search"
                               data-toggle="dropdown" placeholder="Search game" aria-label="Search by game"
                               v-model="search">
                        <div class="input-group-prepend">
                            <div class="input-group-text">
                                <i class="fe fe-search"></i>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-12 col-xl-6" v-for="(game,index) in games" :key="index">
                            <ItemCard>
                                <template v-slot:image>
                                    <img :src="game.game.thumbnail" class="rounded"
                                         style="width: 50px; height: 50px"
                                         alt="game image">
                                </template>
                                <template v-slot:title>{{ game.game.name }}</template>
                                <template v-slot:badges>
                                <span v-for="(badge, index) in game.game.badges" v-bind:key="index" class="ml-2 badge"
                                      v-bind:class="{
                                        'badge-soft-primary': badge.label === 'Recomendado',
                                        'badge-soft-success': badge.label === 'Jogo do Ano'
                                      }"
                                >{{badge.label}}</span>
                                </template>
                                <template v-slot:metadata>
<b-icon-person-fill class="text-muted"></b-icon-person-fill>
                                    <span class=" text-muted ml-1">{{ players(game.game) }}</span>
                                   <b-icon-clock class="text-muted ml-3 "></b-icon-clock>
                                    <span class="text-muted ml-1 ">{{ playtime(game.game) }} </span>
                                </template>
                                <template v-slot:top-right>

                                    <div v-if="game.checkedin && ! game.available ">
                                        <span class="fe fe-alert-circle text-warning"></span>

                                        <span class="text-warning">Being played
                                        by {{ game.currentwithdraw.requisitor }}
                                                    </span>

                                    </div>
                                    <div class="dropdown ml-1">
                                        <a class="" type="button"
                                           id="dropdownMenuButton"
                                           data-toggle="dropdown"
                                           aria-haspopup="true"
                                           aria-expanded="false">
                                            <span class="fe fe-more-vertical"></span>
                                        </a>
                                        <div class="dropdown-menu dropdown-menu-right"
                                             aria-labelledby="dropdownMenuButton">
                                            <a class="dropdown-item" href="#">Edit</a>
                                            <a class="dropdown-item" href="#">Delete</a>
                                        </div>
                                    </div>

                                </template>
                                <template v-slot:bottom-right> {% if perms.bglibrary.add_withdraw %}

                                    <a :href="'/library/' + [[ game.id ]] +'/withdraw/new'"
                                       v-show="game.checkedin && game.available "
                                       class="btn btn-outline-secondary btn-sm">
                                        <span class="fe fe-upload filled"></span><span> Withdraw</span>
                                    </a>
                                    <button v-show="game.checkedin && !game.available "
                                            class="btn btn-outline-secondary btn-sm"
                                            @click="doReturn(game)">
                                        <span class="fe fe-download filled"></span>
                                        <span>return ([[ game.location ]])</span></button>

                                    {% else %}
                                    {% endif %}
                                </template>
                            </ItemCard>

                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
    import {mapState} from 'vuex'
    import ItemCard from "@/components/ItemCard";

    export default {
        name: "Home",
        data() {
            return {
                search: ''
            }
        },
        components: {ItemCard},
        computed: mapState({
            games: state => state.library.games
        }),
        created() {
            this.$store.dispatch('library/getGames')
        },
        methods: {
            playtime: function (obj) {
                let msg;
                if (obj.min_playtime === obj.max_playtime) {
                    msg = obj.min_playtime;
                } else {
                    msg = obj.min_playtime + " - " + obj.max_playtime;
                }
                return msg + " min"
            },
            players: function (obj) {
                if (obj.min_players === obj.max_players) {
                    return obj.min_players;
                } else {
                    return obj.min_players + " - " + obj.max_players;
                }
            },
        }
    }
</script>

<style scoped>

</style>
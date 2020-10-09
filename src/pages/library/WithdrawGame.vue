<template>
    <div>
        <EndTemplateHeader :title="title" :pretitle="pretitle"></EndTemplateHeader>
        <div class="row mb-4" v-cloak>
            <div class="col-12 ">
                <h3>Game</h3>
                <ItemCard>
                    <template v-slot:image>
                        <img :src="game.game.thumbnail" class="rounded"
                             style="width: 50px; height: 50px"
                             alt="game image">
                    </template>
                    <template v-slot:title>{{ game.game.name }}</template>
                    <template v-slot:metadata>
                        <b-icon-person-fill class="text-muted fe fe-users mr-2"></b-icon-person-fill>
                        <span class=" text-muted">{{ num_players(game.game.min_players, game.game.max_players) }}</span>
                        <b-icon-clock-fill font-scale="0.8" class="ml-4 mr-2 text-muted fe fe-clock"></b-icon-clock-fill>
                        <span class=" text-muted" >{{ playtime(game.game.min_playtime, game.game.max_playtime) }} </span>
                    </template>
                    <template v-slot:right>
                        <h1 class="mb-0 text-muted">{{ game.location }}</h1>
                    </template>
                </ItemCard>
            </div>
        </div>



        <h3>Player</h3>

        <b-link v-b-modal.player-select>
        <div role="button"
             class="d-flex col-12 card card-inactive "

             v-if="!requisitor.id">

            <div class="card-body btn btn-link align-self-center">
                <span class="fe fe-plus-circle"></span>
                <span class="ml-2">Select a player</span>
            </div>
        </div>
            </b-link>
        <div class="row" v-if="!!requisitor.id" >
            <div class="col">
                <ItemCard v-cloak>
                    <template v-slot:image>
                        <div class="avatar">
                                <span class="avatar-title rounded-circle"
                                      v-text="initials(requisitor.name)"></span>
                        </div>
                    </template>
                    <template v-slot:title>{{ requisitor.name }}</template>
                    <template v-slot:metadata><p class="text-muted mb-0">
                        <b-icon-envelope-fill class="mr-2"></b-icon-envelope-fill>
                        <span v-text="requisitor.email"></span>
                    </p></template>
                </ItemCard>
            </div>

            <div class="col-auto pb-4">
                <div class="btn btn-info d-flex align-items-center h-100 " data-target="#player-select-modal"
                     data-toggle="modal">
                    <b-icon-pencil-fill></b-icon-pencil-fill>
                </div>
            </div>
        </div>

        <div class="row mt-5">
            <div class="col">
                <hr>
            </div>
            <div class="col-auto">
                <button class="btn btn-lg btn-link text-muted">Cancel</button>
                <button class="btn btn-lg btn-primary " v-on:click="doWithdraw">Finish</button>
            </div>
            <div class="col">
                <hr>
            </div>
        </div>
        <ModalPlayerSelect id="player-select" title="Players" v-on:player-selected="setRequisitor">
        </ModalPlayerSelect>
    </div>
</template>

<script>
    import usersMixin from '@/mixins/users.mixin'
    import gamesMixin from '@/mixins/games.mixin'
    import axiosMixin from '@/mixins/axios.mixin'
    import withdrawService from '@/services/withdraw.service'
    import libraryService from "@/services/library.service";
    import ItemCard from "@/components/ItemCard";
    import ModalPlayerSelect from "@/components/ModalPlayerSelect";
    import EndTemplateHeader from "@/components/EndTemplateHeader";

    export default {
        name: "WithdrawGame",
        components: {EndTemplateHeader, ModalPlayerSelect, ItemCard},
        mixins: [usersMixin, axiosMixin, gamesMixin],
        props: ['title', 'pretitle'],
        data() {
            return {
                id: '',
                game: {
                    game: {
                        min_players: 0,
                        max_players: 0
                    },
                    thumbnail: ''
                },
                requisitor: {
                    id: '',
                    name: '',
                    email: ''
                },
            }
        },
        methods: {
            doWithdraw(e) {
                e.preventDefault();

                let data = {
                    requisitor_id: this.requisitor.id,
                    game_id: this.game.id
                };

                withdrawService.withdrawGame(data).then(() => {
                    this.$toast.success('Successfully withdrawn. Game placed in ' + this.game.game.location)
                    this.$router.push({name: 'Home'});
                }).catch(response => (
                    this.$toast(this.getErrorDescription(response)))
                );
            },
            setRequisitor(player){
                this.requisitor = player
                this.$bvModal.hide('player-select')
            }
        },
        mounted() {
            this.id = this.$route.params.id;
            libraryService.fetchGame(this.id)
                .then(response => (this.game = response));
        },
    }
</script>

<style scoped>

</style>

















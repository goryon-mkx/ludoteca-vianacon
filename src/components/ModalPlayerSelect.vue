<template>
    <!-- Modal -->
    <b-modal :id="id" :title="title" body-class="p-0" hide-header hide-footer scrollable>

        <template v-slot:default>
            <slot name="content">
                <div class="modal-card card">

                    <div v-show="!isNewPlayer">
                        <div class="card-header">

                            <div class="input-group input-group-flush input-group-merge">

                                <!-- Input -->
                                <input type="search" class="form-control form-control-prepended list-search"
                                       placeholder="Search">

                                <!-- Prepend -->
                                <div class="input-group-prepend">
                                    <div class="input-group-text">
                                        <b-icon-search font-scale="0.8"></b-icon-search>
                                    </div>
                                </div>

                            </div>
                            <!-- Close -->
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">×</span>
                            </button>
                        </div>
                        <div class="card-body p-0">
                            <!-- Select player content -->
                            <div class="">
                                <div class="list-group list-group-flush">
                                    <a v-on:click="$emit('player-selected', player)" href="#!"
                                       v-for="(player, index) in players" v-bind:key="index"
                                       class="list-group-item list-group-item-action px-0">
                                        <div class="d-flex flex-row align-items-center px-4">
                                            <div class="avatar avatar-sm">
                                                <span class="avatar-title rounded-circle"
                                                      v-text="initials(player.name)"></span>
                                            </div>
                                            <div class="d-flex flex-column ml-3">
                                                <span class="" v-text="player.name"></span>
                                                <span v-text="player.email" class="text-muted"></span>
                                            </div>
                                        </div>

                                    </a>
                                </div>
                            </div>

                        </div>
                        <div class="card-footer">
                            <button type="button" @click="doNewPlayer" class="btn btn-secondary">Create
                                new player
                            </button>
                        </div>
                    </div>

                    <div v-if="isNewPlayer">
                        <div class="card-header">
                            <div class="d-flex flex-row align-items-center flex-grow-1">
<b-button class="" @click="isNewPlayer=false"><b-icon-arrow-left></b-icon-arrow-left>back to search</b-button><h4></h4>
                                </div>

                            <!-- Close -->
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">×</span>
                            </button>
                        </div>
                        <div class="card-body p-0">
                            <form novalidate>
                                <div class="modal-content px-4">

                                    <div class="form-group mt-4">
                                        <label>Name</label>
                                        <input type="text" class="form-control"
                                               placeholder=" eg. John Doe" v-model="player.name"/>
                                    </div>

                                    <div class="form-group">

                                        <label>E-mail</label>
                                        <input type="text" class="form-control"
                                               placeholder="eg. name@mail.com" v-model="player.email"/>

                                    </div>
                                </div>
                            </form>


                        </div>
                        <div class="card-footer d-flex flex-row justify-content-end">
                            <button class="btn btn-primary">Create</button>
                        </div>
                    </div>

                </div>
            </slot>
        </template>
    </b-modal>


</template>

<script>
    import usersMixin from '@/mixins/users.mixin'
    import playerService from '@/services/player.service'

    export default {
        name: "ModalPlayerSelect", mixins: [usersMixin],
        props: ['id', 'title'],
        components: {},
        data: function () {
            return {
                isNewPlayer: false,
                search: '',
                selectedPlayer: undefined,
                players: [],
                player: {
                    name: '',
                    email: ''
                }
            }
        },
        methods: {
            doNewPlayer(e) {
                e.preventDefault();
                this.player.name = this.search;
                this.isNewPlayer = true;
            },
            selectPlayer() {

            }
        },

        mounted() {
            playerService.fetchPlayers().then(response => this.players = response);
        }
    }
</script>

<style scoped>

</style>

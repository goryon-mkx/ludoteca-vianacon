<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>
    import authorizationService from '@/services/authorization.service'
    export default {
        name: "App",
        created(){
          if(authorizationService.isAuthenticated()){
            this.$store.dispatch("users/loadCurrent");
            }
        }
    }
</script>
<style>
</style>

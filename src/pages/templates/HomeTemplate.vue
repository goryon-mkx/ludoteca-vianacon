<template>
    <div>
        <b-nav>
            <b-nav-item :to="{ name: 'library' }">Ludoteca</b-nav-item>
            <b-nav-item :to="{ name: 'store' }">Loja</b-nav-item>
        </b-nav>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script>
    export default {
        name: "HomeTemplate"
    }
</script>

<style scoped>

</style>
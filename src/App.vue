<template>
  <div id="app">
    <div class="container py-3">
      <b-nav>
        <b-nav-item :to="{ name: 'library' }">Ludoteca</b-nav-item>
        <b-nav-item :to="{ name: 'store' }">Loja</b-nav-item>
      </b-nav>
    </div>
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<style>
</style>

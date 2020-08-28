<template>
  <div id="app">




<div class="container py-3">
    <ul class="nav">
  <li class="nav-item">
    <a class="nav-link active font-weight-bold" href="#">Ludoteca</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Loja</a>
  </li>
</ul>
</div>





    <div class="container">
      <div id="nav">
        <router-link :to="{ name: 'home' }">Vue</router-link>|
        <router-link :to="{ name: 'messages' }">Django Rest</router-link>
      </div>
      <router-view />
    </div>
  </div>
</template>

<style>
</style>

<template>
  <nav class="navbar navbar-expand-lg navbar-light" id="topnav">
    <b-container>

      <!-- Toggler -->
      <button class="navbar-toggler mr-auto" type="button" data-toggle="collapse" data-target="#navbar"
              aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Brand -->
      <a class="navbar-brand mr-auto" href="/">
        <!--            <img src="{% static "bglibrary/img/logo.png" %}" alt="..." class="navbar-brand-img">-->
      </a>

      <!-- User -->
      <div class="navbar-user">
        <!-- Toggle -->

        <div class="d-flex flex-row align-items-center">
          <div class="d-flex flex-column align-items-end mr-3">
            <b-link v-if="!isAuthenticated()" class="btn btn-outline-primary" :to="{name: 'Login'}">Login</b-link>
          </div>

          <div v-if="isAuthenticated()">
            <UserInfo />
            <!-- TODO: catch logout event -->
          </div>
        </div>
      </div>

      <!-- Collapse -->
      <div class="collapse navbar-collapse mr-auto order-lg-first" id="navbar">

        <!-- Navigation -->
        <ul class="navbar-nav mr-auto">
          <li class="nav-item ">
            <b-nav-item :to="{ name: 'library' }">Ludoteca</b-nav-item>
          </li>
          <li>
            <b-nav-item :to="{ name: 'store' }">Loja</b-nav-item>
          </li>
        </ul>
      </div>

    </b-container> <!-- / .container -->
  </nav>
</template>

<script>
import usersMixin from '@/mixins/users.mixin'
import authorizationService from '@/services/authorization.service'
import UserInfo from "@/components/UserInfo";

export default {
  name: "TopNav",
  components: {UserInfo},
  mixins: [usersMixin],
  methods: {
    logout() {
      authorizationService.logout()
    }
  }
}
</script>


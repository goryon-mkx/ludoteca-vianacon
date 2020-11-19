<template>
  <nav class="navbar navbar-expand-lg navbar-light" id="topnav">
    <div class="container">

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
            <a v-if="!isAuthenticated()" class="btn btn-outline-primary" href="/login/">Login</a>
          </div>

          <div v-if="isAuthenticated()">

            <b-dropdown toggle-class="py-1 px-2" variant="link" right no-caret>

              <template #button-content>
                <div class="d-flex flex-row text-gray-800 align-items-center">
                  <!--                            <b-avatar size="sm"/>-->

                  {{ $store.getters["users/current"].name }}
                  <b-avatar size="sm" class="ml-2"></b-avatar>
                </div>
              </template>
              <template #default>
                <b-dropdown-item-button>
                  <b-icon-person class="mr-3"></b-icon-person>
                  Profile
                </b-dropdown-item-button>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item-button @click="logout">
                  <b-icon-box-arrow-right class="mr-3"/>
                  Logout
                </b-dropdown-item-button>
              </template>
            </b-dropdown>
            <b-link
            >
              <!--                            <img src="https://randomuser.me/api/portraits/lego/2.jpg" alt="..."-->
              <!--                                 class="avatar-img rounded-circle">-->

            </b-link>
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

    </div> <!-- / .container -->
  </nav>
</template>

<script>
import usersMixin from '@/mixins/users.mixin'
import authorizationService from '@/services/authorization.service'

export default {
  name: "TopNav",
  mixins: [usersMixin],
  methods: {
    logout() {
      authorizationService.logout()
    }
  }
}
</script>

<style scoped>

</style>
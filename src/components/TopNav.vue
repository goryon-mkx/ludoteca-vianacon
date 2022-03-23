<template>

    <b-container fluid class="px-0">
      <b-navbar sticky  toggleable="md" class="px-3 px-xl-5">
      <b-navbar-brand :to="{ name: 'LibraryHome' }" class="mr-3">
        <img src="@/assets/leiriacon.png"/>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" class="w-100" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'LibraryHome' }" active-class="active">
            Library
          </b-nav-item>
          <b-nav-item :to="{ name: 'StoreHome' }" active-class="active">
            Store
          </b-nav-item>
            <b-nav-item href="https://docs.google.com/spreadsheets/u/0/d/1lHZ6OA-yshGf8GgxmFI-IXygkEvq5a7SZdDl2U8bCcI/"
                        target="_blank" active-class="active">Google Docs</b-nav-item>

        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-button
              v-if="!isAuthenticated()"
              :to="{ name: 'Login' }"
              variant="link"
          >Sign in
          </b-button
          >
          <b-nav-item-dropdown
              v-if="isAuthenticated()"
              :text="$store.getters['users/current'].name"
              right
              toggle-class="py-0 d-flex"
          >
            <b-dropdown-item v-if="isAdmin()" :to="{name: 'Dashboard'}">Dashboard</b-dropdown-item>
            <b-dropdown-item v-if="isAdmin()" :to="{name: 'Configurations'}">Configurations</b-dropdown-item>
            <b-dropdown-divider v-if="isAdmin()"></b-dropdown-divider>
            <b-dropdown-item-button @click="logout"
            >Logout
            </b-dropdown-item-button
            >
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
          </b-navbar>
    </b-container>
</template>
<script>
import usersMixin from '@/mixins/users.mixin'
import authorizationService from '@/services/authorization.service'
//import UserInfo from "@/partials/UserInfo";

export default {
  name: 'TopNav',
  components: {},
  mixins: [usersMixin],
  methods: {
    logout() {
      authorizationService.logout()
      location.reload()
    },
  },
}
</script>

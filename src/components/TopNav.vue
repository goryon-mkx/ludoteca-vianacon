<template>
    <b-container fluid class="px-0">
      <b-navbar sticky  toggleable="md" class="px-3 px-xl-5">
        <b-navbar-brand :to="{ name: 'LibraryHome' }" class="mr-3">
          <img src="@/assets/leiriacon_new.png"/>
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" class="w-100" is-nav>
          <b-navbar-nav>
            <b-nav-item :to="{ name: 'LibraryHome' }" active-class="active">
              Library
            </b-nav-item>
            <b-nav-item v-if="hasPermission(game_permissions.Store.View)" :to="{ name: 'StoreHome' }" active-class="active">
              Store
            </b-nav-item>
            <b-nav-item v-if="hasPermission(user_permissions.Add)" :to="{ name: 'PlayersHome' }" active-class="active">
              Players
            </b-nav-item>
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
                class=""
                v-if="isAuthenticated()"
                :text="$store.getters['users/current'].name"
                right
                toggle-class="py-0 pl-0 pt-1 d-flex"
            >
              <b-dropdown-text v-if="isAssociate()" class="font-weight-normal" style="width: 240px;">
                <div class="d-flex justify-content-between">
                  <span>Quotas</span>
                  <span v-if="numberOfQuotasDue === 0" class="text-success small font-weight-normal">Paid</span>
                  <span v-else class="text-warning small font-weight-normal">{{numberOfQuotasDue}} due</span>
                </div>
              </b-dropdown-text>
              <b-dropdown-divider v-if="isAssociate()"></b-dropdown-divider>
              <b-dropdown-item v-if="isStaff()" :to="{name: 'Dashboard'}">Dashboard</b-dropdown-item>
              <b-dropdown-item v-if="isAdmin()" :to="{name: 'Configurations'}">Configurations</b-dropdown-item>
              <b-dropdown-divider v-if="isStaff() || isAdmin()"></b-dropdown-divider>
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
import {GamePermissions, UserPermissions} from '@/enums/permissions.enum'
//import UserInfo from "@/partials/UserInfo";

export default {
  name: 'TopNav',
  components: {},
  mixins: [usersMixin],
  data(){
    return {
      game_permissions: GamePermissions,
      user_permissions: UserPermissions
    }
  },
  methods: {
    logout() {
      authorizationService.logout()
      location.reload()
    },
  },
  computed: {
    numberOfQuotasDue() {
      return this.getNumberOfQuotasDue(this.$store.getters["users/current"].quotas)
    }
  }
}
</script>

<template>

  <AuthTemplate title="Sign in" subtitle="Free access to leiriacon platform" illustration="img/illustrations/happiness.svg">
    <template #content>

        <!-- Form -->
      <form @submit.prevent="doLogin">
        <b-form-group label="E-mail">
          <!-- Input -->
          <b-form-input
            v-model="email"
            placeholder="Enter your e-mail"
            tabindex="1"
            type="text"
          />
        </b-form-group>

        <!-- Password -->
        <b-form-group>
          <div class="row">
            <div class="col">
              <!-- Label -->
              <label>Password</label>
            </div>
            <div class="col-auto">
              <!-- Help text -->
              <b-link
                  :to="{name: 'RequestResetPassword'}"
                class="form-text small text-muted"
              >
                Forgot password?
              </b-link>
            </div>
          </div>
          <!-- / .row -->

          <!-- Input group -->
          <b-input-group class="input-group-merge">
            <!-- Input -->
            <b-form-input
              v-model="password"
              placeholder="Enter your password"
              tabindex="2"
              type="password"
            />
          </b-input-group>
        </b-form-group>

        <!-- Submit -->
        <button class="btn btn-lg btn-block btn-primary mb-3">
          Sign in
        </button>

        <!-- Link -->
        <div class="text-center">
          <small class="text-muted text-center">
            Don't have an account yet? <b-link :to="{name: 'Signup'}">Sign up</b-link>.
          </small>
        </div>
      </form>
    </template>
  </AuthTemplate>
</template>

<script>
import axiosUtils from '@/mixins/axios.utils'
import authorizationService from '@/services/authorization.service'
import router from '@/router'
import AuthTemplate from "@/pages/auth/AuthTemplate"

export default {
  name: 'Login',
  components: {AuthTemplate},
  data: function() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    doLogin() {
      this.loading = true

      return authorizationService
        .doLogin(this.email, this.password)
        .then(response => {
          this.$store.commit('AUTH_SUCCESS', response.data)
          this.$store.dispatch("init")
          router.push({ name: 'LibraryHome' })
        })
        .catch(response => {
          this.$toast.error(axiosUtils.getErrorDescription(response))
        })
        .finally(() => (this.loading = false))
    },
  },
}
</script>

<style scoped></style>

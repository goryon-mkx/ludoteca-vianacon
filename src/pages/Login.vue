<template>

  <AuthTemplate title="Sign in" subtitle="Free access to leiriacon platform" illustration="img/illustrations/happiness.svg">
    <template #content>

        <!-- Form -->
      <form @submit.prevent="doLogin">
        <b-form-group label="E-mail" invalid-feedback="This field is equired">
          <!-- Input -->
          <b-form-input
            v-model="form.email"
            placeholder="Enter your e-mail"
            :state="validateState('email')"
            tabindex="1"
            type="text"
          />
        </b-form-group>

        <!-- Password -->
        <b-form-group invalid-feedback="This field is required">
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

            <b-form-input
              v-model="form.password"
              placeholder="Enter your password"
              :state="validateState('password')"
              tabindex="2"
              type="password"
            />

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
import {required} from "vuelidate/lib/validators"
import formMixin from "@/mixins/form.mixins"

export default {
  name: 'Login',
  components: {AuthTemplate},
  mixins: [formMixin],
  data: function() {
    return {
      form: {
        email: '',
        password: '',
      }
    }
  },
  methods: {
    doLogin() {
      this.loading = true

      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      return authorizationService
        .doLogin(this.form.email, this.form.password)
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
  validations: {
    form: {
      email:{ required, },
      password: { required, }
    }
  }
}
</script>

<style scoped></style>

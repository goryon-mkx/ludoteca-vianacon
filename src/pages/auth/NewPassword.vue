<template>
  <AuthTemplate
      title="New password"
      subtitle="Set a new password for your account"
    :illustration="'img/illustrations/coworking.svg'">
    <template #content>
      <!-- Form -->
      <form @submit.prevent="doChangePassword">
            <b-form-group
                label="Password"
                invalid-feedback="Too short. Minimum of 8 characters">
              <!-- Input -->
              <b-form-input
                v-model="form.password"
                placeholder="Enter a password"
                tabindex="1"
                :state="validateState('password')"
                type="password"

              />
              <PasswordErrors class="mt-2" v-if="errors" :errors="errors"/>
            </b-form-group>

            <!-- Password -->
            <b-form-group label="Password confirmation" invalid-feedback="Passwords doesn't match">

              <!-- Input -->
              <b-form-input
                v-model="form.confirmation"
                placeholder="Repeat your password"
                tabindex="2"
                :state="validateState('confirmation')"
                type="password"
              />
            </b-form-group>

            <!-- Submit -->
            <button class="btn btn-lg btn-block btn-primary mb-3">
              <b-spinner v-if="loading" :disabled="loading" small/> <span v-if="!loading">Update</span>
            </button>

            <!-- Link -->
            <div class="text-center">
              <small class="text-muted text-center">
                Go back to <b-link :to="{name: 'Login'}">Sign in</b-link>
              </small>
            </div>
          </form>
    </template>
  </AuthTemplate>

</template>

<script>
import passwordService from "@/services/password.service"
//import router from "@/router"

import {required, minLength, sameAs} from "vuelidate/lib/validators"
import AuthTemplate from "@/pages/auth/AuthTemplate"
import PasswordErrors from "@/components/password/errors"

import formMixin from "@/mixins/form.mixins"

export default {
  name: "ResetPassword",
  components: {PasswordErrors, AuthTemplate},
  mixins: [formMixin],
  data(){
    return {
      token: this.$route.query.token,
      loading: false,
      form: {
        password: "",
        confirmation: ""
      },
      errors: []
    }
  },
  methods: {
    doChangePassword() {
      this.loading = true

      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      return passwordService
        .changePassword(this.form.password, this.token)
        .then(() => {
          //router.push({ name: 'LibraryHome' })
        })
        .catch(response => {
          if (response.response.status === 404){
            this.$toast.error("Invalid token")
          } else {
            this.errors = response.response.data.password
          }

        })
        .finally(() => (this.loading = false))
    },
  },
  validations: {
    form: {
      password: {required, minLength: minLength(8)},
      confirmation: {required, sameAsPassword: sameAs('password')}
    }
  }
}
</script>

<style scoped>

</style>
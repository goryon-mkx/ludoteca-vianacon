<template>
  <AuthTemplate
      title="New password"
      subtitle="Set a new password for your account"
    :illustration="'img/illustrations/coworking.svg'">
    <template #content>
      <!-- Form -->
      <form @submit.prevent="doChangePassword" v-if="!success">
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
      <div v-if="success">
        <b-alert show variant="success"><b-icon-check2-circle/> Done</b-alert>
        You should be redirected in a few seconds.<br/>
        If not <b-link :to="{ name: 'Login' }">click here</b-link>
      </div>
    </template>
  </AuthTemplate>
</template>

<script>
import passwordService from "@/services/password.service"

import {required, minLength, sameAs} from "vuelidate/lib/validators"
import AuthTemplate from "@/pages/auth/AuthTemplate"
import PasswordErrors from "@/components/password/errors"

import formMixin from "@/mixins/form.mixins"
import {sleep} from "@/utils/promise.utils"

export default {
  name: "ResetPassword",
  components: {PasswordErrors, AuthTemplate},
  mixins: [formMixin],
  data(){
    return {
      token: this.$route.query.token,
      success: false,
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

      this.errors = []

      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      this.loading = true

      return passwordService
        .changePassword(this.form.password, this.token)
        .then(() => {
          this.success = true
          sleep(3000).then(()=>this.$router.push({ name: 'Login' }))
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

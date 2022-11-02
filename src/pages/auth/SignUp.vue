<template>
  <AuthTemplate title="Sign up" subtitle="Free access to leiriacon platform" illustration="img/illustrations/happiness.svg">
    <template #content>
      <!-- Form -->
      <b-alert :show="emailAlreadyRegistered" variant="warning"><b-icon-exclamation-circle-fill/> E-mail already registered</b-alert>
      <form @submit.prevent="signUp" v-if="!submitted">
        <b-form-group label="Name" invalid-feedback="This field is required">
          <!-- Name -->
          <b-form-input
            v-model="form.name"
            placeholder="Enter your name"
            :state="validateState('name')"
            tabindex="1"
            type="text"
          />
        </b-form-group>


        <!-- Email -->
        <b-form-group label="E-mail" invalid-feedback="This field is required">
            <b-form-input
              v-model="form.email"
              placeholder="Enter your email"
              :state="validateState('email')"
              tabindex="2"
              type="email"
            />
        </b-form-group>

        <!-- Submit -->
        <button :disabled="loading" class="btn btn-lg btn-block btn-primary mb-3">
          <b-spinner small v-if="loading"/>
          <span v-if="!loading">Sign up</span>
        </button>

        <!-- Link -->
        <div class="text-center">
          <small class="text-muted text-center">
            Already have an account? <b-link :to="{name: 'Login'}">Sign in</b-link>.
          </small>
        </div>
      </form>
        <l-check-inbox
          v-if="submitted"
          description="We have just sent you a confirmation message to your email inbox."/>
    </template>
  </AuthTemplate>
</template>

<script>
import AuthTemplate from "@/pages/auth/AuthTemplate"
import formMixin from "@/mixins/form.mixins"
import {required, email} from "vuelidate/lib/validators"
import userService from "@/services/user.service"
import axiosUtils from "@/mixins/axios.utils"
import usersMixin from "@/mixins/users.mixin"
import LCheckInbox from "@/components/email/LCheckInbox.vue"
export default {
  name: "SignUp",
  mixins: [formMixin, usersMixin],
  components: {LCheckInbox, AuthTemplate},
  data(){
    return {
      loading: false,
      submitted: false,
      emailAlreadyRegistered: false,
      form: {
        name: "",
        email: ""
      },
    }
  },
  methods: {
    signUp(){
      this.loading = true
      this.emailAlreadyRegistered = false

      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      userService
        .createUser(this.form)
        .then(() => {
          this.submitted = true
        })
        .catch((response) => {
          if (response?.response?.data?.email) {
            this.emailAlreadyRegistered = true
          } else {
            this.$toast.error(
              'Error adding player: ' +
                axiosUtils.getErrorDescription(response),
            )
          }
        }).finally(()=> this.loading = false)

    }
  },
  validations: {
    form: {
      name: {required,},
      email: {required, email}
    }
  }
}
</script>

<style scoped>

</style>

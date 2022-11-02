<template>
  <AuthTemplate
      title="Password reset"
      subtitle="Enter your email to get a password reset link"
      :illustration="'img/illustrations/coworking.svg'">

    <template #content>

      <!-- Form -->
      <form v-if="!success" @submit.prevent="doRequest">
        <b-form-group label="E-mail" invalid-feedback="Please insert a valid e-mail address">
          <!-- Input -->
          <b-form-input
            v-model="form.email"
            placeholder="Enter your e-mail"
            :state="validateState('email')"
            tabindex="1"
            type="text"
          />
        </b-form-group>

        <!-- Submit -->
        <b-button :disabled="loading" type="submit" variant="primary" block size="lg" class="mb-3">
          <b-spinner small v-if="loading"/>
          <span v-if="loading" class="sr-only">Loading...</span>
          <span v-else> Ask for a reset url</span>
        </b-button>
        Remember your password? <b-link :to="{name: 'Login'}">Sign in</b-link>
      </form>
      <l-check-inbox description="If the email that you provided is registered you should have received a message with the next steps."
                     v-if="success"/>
    </template>

  </AuthTemplate>
</template>

<script>
import axiosUtils from '@/mixins/axios.utils'
import passwordService from '@/services/password.service'
import {required, email} from "vuelidate/lib/validators"
import formMixin from "@/mixins/form.mixins"
import AuthTemplate from "@/pages/auth/AuthTemplate"
import LCheckInbox from "@/components/email/LCheckInbox.vue"

export default {
  name: 'Login',
  components: {LCheckInbox, AuthTemplate},
  mixins: [formMixin],
  data: function() {
    return {
      loading: false,
      success: false,
      form: {
        email: '',
      }
    }
  },
  methods: {
    doRequest() {
      this.$v.form.$touch()
      if (this.$v.form.$anyError) {
        return
      }

      this.loading = true

      return passwordService.requestToken(this.form.email)
        .then(() => {
          this.success = true
        })
        .catch(response => {
          this.$toast.error(axiosUtils.getErrorDescription(response))
        })
        .finally(() => (this.loading = false))
    },
  },
  validations: {
    form: {
      email: {
          email, required,
      },
    },
  },
}
</script>

<style scoped></style>

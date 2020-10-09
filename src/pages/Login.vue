<template>
    <!-- CONTENT
    ================================================== -->
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-5 col-xl-4 my-5">

                <!-- Heading -->
                <h1 class="display-4 text-center mb-3">
                    Sign in
                </h1>

                <!-- Subheading -->
                <p class="text-muted text-center mb-5">
                    Free access to our dashboard.
                </p>

                <!-- Form -->
                <ValidationObserver ref="form" v-slot="{ handleSubmit }">
                    <form @submit.prevent="handleSubmit(doLogin)">


                        <!-- Email address -->
                        <ValidationProvider
                                rules="required"
                                v-slot="{ errors }"
                                name="E-mail"
                        >
                            <b-form-group label="Username">

                                <!-- Input -->
                                <b-form-input lab
                                              type="text"
                                              :state="errors[0] ? false : null"
                                              v-model="username"
                                              tabindex="1"
                                              placeholder="Username"/>

                                <b-form-invalid-feedback>{{errors[0]}}</b-form-invalid-feedback>
                            </b-form-group>
                        </ValidationProvider>

                        <!-- Password -->
                        <b-form-group>

                            <div class="row">
                                <div class="col">

                                    <!-- Label -->
                                    <label>Password</label>

                                </div>
                                <div class="col-auto">

                                    <!-- Help text -->
                                    <a href="password-reset.html" class="form-text small text-muted">
                                        Forgot password?
                                    </a>

                                </div>
                            </div> <!-- / .row -->

                            <!-- Input group -->
                            <b-input-group class="input-group-merge">

                                <!-- Input -->
                                <b-form-input type="password" v-model="password" tabindex="2" class="form-control-appended"
                                              placeholder="Enter your password"/>


                            </b-input-group>

                        </b-form-group>

                        <!-- Submit -->
                        <button class="btn btn-lg btn-block btn-primary mb-3">
                            Sign in
                        </button>

                        <!-- Link -->
                        <div class="text-center">
                            <small class="text-muted text-center">
                                Don't have an account yet? <a href="sign-up.html">Sign up</a>.
                            </small>
                        </div>

                    </form>
                </ValidationObserver>

            </div>
        </div> <!-- / .row -->
    </div> <!-- / .container -->
</template>

<script>
    import {ValidationProvider, ValidationObserver, extend} from 'vee-validate';
    import * as rules from "vee-validate/dist/rules";
    import axiosUtils from "@/mixins/axios.utils"

    // install rules
    Object.keys(rules).forEach(rule => {
        extend(rule, rules[rule]);
    });

    export default {
        name: "Login",
        components: {ValidationProvider, ValidationObserver},
        data: function () {
            return {
                username: '',
                password: ''
            }
        },
        methods: {
            doLogin() {
                this.loading = true;
                let username = this.username;
                let password = this.password;
                this.$store
                    .dispatch("login", {username, password})
                    .catch(response => {
                        this.$toast.error(axiosUtils.getErrorDescription(response));
                    })
                    .finally(() => (this.loading = false));
            }
        }
    }
</script>

<style scoped>

</style>
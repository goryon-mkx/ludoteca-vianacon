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
                        <a v-if="!isAuthenticated" class="btn btn-outline-primary" href="/login/">Login</a>
                    </div>


                    <div v-if="isAuthenticated" class="dropdown-toggle" data-toggle="dropdown"
                         aria-haspopup="true" aria-expanded="false">
                        <a href="#" class="avatar avatar-sm avatar-online" role="button"
                        >
                            <b-icon-person-circle font-scale="3"></b-icon-person-circle>
<!--                            <img src="https://randomuser.me/api/portraits/lego/2.jpg" alt="..."-->
<!--                                 class="avatar-img rounded-circle">-->

                        </a>
                    </div>
                    <!-- Menu -->
                    <div class="dropdown-menu dropdown-menu-right">
                        <a href="profile-posts.html" class="dropdown-item">Profile</a>
                        <a href="settings.html" class="dropdown-item">Settings</a>
                        <hr class="dropdown-divider">
                        <!--                        <a href="{% url "bglibrary:logout" %}" class="dropdown-item">Logout</a>-->
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

    export default {
        name: "TopNav",
        mixins: [usersMixin]
    }
</script>

<style scoped>

</style>
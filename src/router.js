import Vue from 'vue'
import VueRouter from 'vue-router'
import StoreHome from '@/pages/store/Home'
import LibraryHome from '@/pages/library/Home'
import Home from '@/pages/Home'
import Login from "./pages/Login";
import authorizationService from "@/services/authorization.service";
import EndTemplate from "@/pages/templates/EndTemplate";
import HomeTemplate from "@/pages/templates/HomeTemplate";

Vue.use(VueRouter)


// Guardians
function guardAuthenticated(to, from, next) {
    if (authorizationService.isAuthenticated()) {
        next();
    } else {
        next({name: "login"});
    }
}


const routes = [

    {
        path: "",
        component: HomeTemplate,
        children: [
            {
                path: "/",
                name: "home",
                component: Home
            },
            {
                path: "/library/",
                name: "libraryHome",
                component: LibraryHome
            },
            {
                path: "/store/",
                name: "StoreHome",
                component: StoreHome
            },
        ]
    },
    {
        path: "",
        component: EndTemplate,
        children: [
            {
                path: "/library/new",
                name: "LibraryGameNew",
                props: {title: "New library game"}
            },
        ]
    }, {
        path: '/library',
        name: 'library',
        component: LibraryHome
    },
    {
        path: '/store',
        name: 'store',
        component: StoreHome
    },


    {
        path: '/login',
        name: 'login',
        component: Login
    },


];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;
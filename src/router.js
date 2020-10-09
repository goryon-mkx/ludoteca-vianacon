import Vue from 'vue'
import VueRouter from 'vue-router'
import StoreHome from '@/pages/store/Home'
import LibraryHome from '@/pages/library/Home'
import Home from '@/pages/Home'
import Login from "./pages/Login";

import EndTemplate from "@/pages/templates/EndTemplate";
import HomeTemplate from "@/pages/templates/HomeTemplate";
import WithdrawGame from "@/pages/library/WithdrawGame";
import AddGame from "@/pages/library/AddGame";

import authorizationService from "@/services/authorization.service";

Vue.use(VueRouter)


//Guardians
function guardAuthenticated(to, from, next) {
    if (authorizationService.isAuthenticated()) {
        next();
    } else {
        next({name: "Login"});
    }
}

const routes = [

    {
        path: "",
        component: HomeTemplate,
        children: [
            {
                path: "/",
                name: "Home",
                component: Home,
                props: {title: 'Library', pretitle: 'leiriacon 2021'}
            },
            {
                path: "/library/",
                name: "LibraryHome",
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
                name: "AddLibraryGame",
                props: {title: "New library game"},
                beforeEnter: guardAuthenticated,
                component: AddGame
            },
            {
                path: "/library/:id/withdraw",
                name: "WithdrawGame",
                props: {title: "Withdraw game", pretitle: "Library"},
                beforeEnter: guardAuthenticated,
                component: WithdrawGame
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
        name: 'Login',
        component: Login
    },


];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;
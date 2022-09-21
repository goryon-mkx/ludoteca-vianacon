import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './pages/Login'
import RequestResetPassword from './pages/RequestResetPassword'

import WithdrawGame from '@/pages/library/WithdrawGame'
import AddGame from '@/pages/library/AddGame'
import LibraryDashboard from '@/pages/library/Dashboard'
import Configurations from '@/pages/admin/Configurations'

import authorizationService from '@/services/authorization.service'
import passwordService from '@/services/password.service'

//import PageNotFound from '@/pages/PageNotFound'
import NotFound from '@/pages/error/NotFound'
import LibraryHome from '@/pages/library/home/LibraryHome'
import PlayersHome from '@/pages/players/Home'
import Dashboard from '@/pages/dashboard/home'
import StoreAddGame from '@/pages/store/new/NewGame'
import StoreHome from '@/pages/store/home/StoreHome'
import NewPassword from '@/pages/auth/NewPassword'
import SignUp from '@/pages/auth/SignUp'

import { GamePermissions, UserPermissions } from '@/enums/permissions.enum'

Vue.use(VueRouter)

//Guardians
function guardAuthenticated(to, from, next) {
  //const is_authenticated = authorizationService.isAuthenticated()
  //const has_permissions = passwordService.isAuthenticated()
  console.log(JSON.stringify(to.meta))

  if (authorizationService.isAuthenticated()) {
    next()
  } else {
    next({ name: 'Login' })
  }
}

function guardNotAuthenticated(to, from, next) {
  if (authorizationService.isAuthenticated()) {
    next({ name: 'NotFound' })
  } else {
    next()
  }
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LibraryHome,
    props: { title: 'Library', pretitle: 'leiriacon 2022' },
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    props: { title: 'Dashboard', pretitle: 'leiriacon 2022' },
  },
  {
    path: '/library',
    name: 'LibraryHome',
    component: LibraryHome,
    props: { title: 'Library', pretitle: 'leiriacon 2022' },
  },
  {
    path: '/library/dashboard',
    name: 'LibraryDashboard',
    beforeEnter: guardAuthenticated,
    component: LibraryDashboard,
  },
  {
    path: '/library/:id/withdraw',
    name: 'WithdrawGame',
    props: { title: 'Withdraw game', pretitle: 'Library' },
    beforeEnter: guardAuthenticated,
    component: WithdrawGame,
  },

  {
    path: '/library/new',
    name: 'AddLibraryGame',
    beforeEnter: guardAuthenticated,
    component: AddGame,
  },
  {
    path: '/store',
    name: 'StoreHome',
    props: { title: 'Store', pretitle: 'Leiriacon 2022' },
    component: StoreHome,
    beforeEnter: guardAuthenticated,
    meta: {
      permission: GamePermissions.Store.View,
    },
  },
  {
    path: '/store/new',
    name: 'StoreAddGame',
    beforeEnter: guardAuthenticated,
    props: { title: 'Add game', pretitle: 'Store' },
    component: StoreAddGame,
  },
  {
    path: '/players',
    name: 'PlayersHome',
    beforeEnter: guardAuthenticated,
    component: PlayersHome,
    meta: {
      permission: UserPermissions.Add,
    },
  },
  {
    path: '/configurations',
    name: 'Configurations',
    props: { title: 'Configurations', pretitle: 'Admin' },
    beforeEnter: guardAuthenticated,
    component: Configurations,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter: guardNotAuthenticated,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
    beforeEnter: guardNotAuthenticated,
  },
  {
    path: '/request-reset-password',
    name: 'RequestResetPassword',
    component: RequestResetPassword,
    beforeEnter: guardNotAuthenticated,
  },
  {
    path: '/new-password',
    name: 'NewPassword',
    component: NewPassword,
    beforeEnter: (to, from, next) => {
      console.log(JSON.stringify(to.query.token))
      passwordService.isTokenValid(to.query.token).then((isValid) => {
        if (isValid) {
          next()
        } else {
          next({ name: 'NotFound' })
        }
      })
    },
  },
  {
    name: 'NotFound',
    path: '*',
    component: NotFound,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: '/',
  routes,
})

export default router

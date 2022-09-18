import { unauthApi } from '@/services/api'

const URL = '/api/password_reset'

export default {
  isTokenValid,
  requestToken,
  changePassword,
}

function requestToken(email) {
  return unauthApi.post(URL + '/', {
    email: email,
  })
}

function isTokenValid(token) {
  return unauthApi
    .post(URL + '/validate_token/', {
      token: token,
    })
    .then(() => {
      return true
    })
    .catch(() => {
      return false
    })
}

function changePassword(password, token) {
  return unauthApi.post(URL + '/confirm/', {
    password: password,
    token: token,
  })
}

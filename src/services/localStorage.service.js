export default {
  getAccessToken,
  getRefreshToken,
  setAccessToken,
  setRefreshToken,
  clear,
  clearTokens,
  setLocale,
  getLocale,
  setUser,
  getUser,
}

const ACCESS_TOKEN = 'access_token'
const REFRESH_TOKEN = 'refresh_token'
const LOCALE = 'locale'
const USER = 'user'

/**
 * Returns access token
 * @returns {string}
 */
function getAccessToken() {
  return localStorage.getItem(ACCESS_TOKEN)
}

/**
 * Returns refresh token
 * @returns {string}
 */
function getRefreshToken() {
  return localStorage.getItem(REFRESH_TOKEN)
}

/**
 * Set access token with the provided token
 * @param token
 */
function setAccessToken(token) {
  localStorage.setItem(ACCESS_TOKEN, token)
}

/**
 * Set refresh token with the provided token
 * @param refreshToken
 */
function setRefreshToken(refreshToken) {
  localStorage.setItem(REFRESH_TOKEN, refreshToken)
}

/**
 * Clear access and refresh tokens
 */
function clear() {
  localStorage.removeItem(LOCALE)
  localStorage.removeItem(USER)
  clearTokens()
}

function clearTokens() {
  localStorage.removeItem(ACCESS_TOKEN)
  localStorage.removeItem(REFRESH_TOKEN)
}

function setLocale(locale) {
  localStorage.setItem(LOCALE, locale)
}

function getLocale() {
  const locale = localStorage.getItem(LOCALE)
  if (!locale) {
    setLocale('en')
  }
  return localStorage.getItem(LOCALE)
}

function setUser(user) {
  return localStorage.setItem(USER, JSON.stringify(user))
}

function getUser() {
  return JSON.parse(localStorage.getItem(USER))
}

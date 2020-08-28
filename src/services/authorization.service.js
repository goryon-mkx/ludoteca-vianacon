import localStorageService from "@/services/localStorage.service";
import { unauthApi } from "@/services/api";

export default {
  refreshToken,
  doLogin,
  isAuthenticated
};

/**
 * Do login with the provided username and password
 * @param username
 * @param password
 * @returns {Promise<AxiosResponse<any>>}
 */
function doLogin(username, password) {
  return unauthApi.post("/token", {
    username: username,
    password: password
  });
}

/**
 * Call refresh token action, save new access token
 * @returns {Promise<((path: PathLike, mode: (number | undefined), callback: NoParamCallback) => void) | ((path: PathLike, callback: NoParamCallback) => void) | ((path: PathLike, mode?: number) => Promise<void>) | access | "public" | "private" | "protected">}
 */
function refreshToken() {
  // call API to get a new token

  return (
    unauthApi
      .post("/token/refresh", {
        refresh: localStorageService.getRefreshToken()
      })
      .then(response => {
        // save new token to LocalStorage
        localStorageService.setAccessToken(response.data.access);
        console.log("refresh token then");
        return Promise.resolve(response.data.access);
      })
      // In case refresh token call returns an error, clear tokens and redirect to login
      .catch(() => {
        console.log("refresh token catch");
        localStorageService.clearTokens();
        this.$route.push({ name: "Login" });
      })
  );
}

/**
 * Checks if user is authenticated based on local storage tokens.
 * NOTE: Ideally it would call API to check token (and refresh token, if necessary)
 * @returns {boolean|boolean}
 */
function isAuthenticated() {
  return (
    !!localStorageService.getAccessToken() &&
    !!localStorageService.getRefreshToken()
  );
}

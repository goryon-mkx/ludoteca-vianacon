import { authApi } from '@/services/api'

const URL = '/api/quotas/'

export default {
  create(user, year) {
    return authApi
      .post(URL, { user: user, year: year })
      .then((response) => response.data)
  },
}

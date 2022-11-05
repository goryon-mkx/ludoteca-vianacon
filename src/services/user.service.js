import { authApi, unauthApi } from '@/services/api'
import { splitName } from '@/utils/name.utils'

const URL = '/api/users/'

export default {
  fetchUsers(params) {
    return authApi
      .get(URL, {
        params: params,
      })
      .then((response) => response.data)
  },
  fetchUser(pk) {
    return authApi.get(URL + `${pk}/`).then((response) => response.data)
  },
  createUser(form) {
    let payload = {
      ...form,
      ...splitName(form['name']),
      username: form['email'],
    }
    delete payload['name']

    return unauthApi.post(URL, payload).then((response) => response.data)
  },
  addToGroup(pk, group) {
    return authApi.patch(URL + `${pk}/`, { add_group: group })
  },
}

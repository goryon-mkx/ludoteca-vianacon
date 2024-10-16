import axios from 'axios'

export { bggApi }

//const API_URL = 'https://www.boardgamegeek.com/xmlapi2'

const TIMEOUT = 9000

//const bggApi = axios.create({
//  baseURL: API_URL,
//  timeout: TIMEOUT,
//})

const bggApi = axios.create({
  baseURL: "https://v1.nocodeapi.com/fabiogasparferreira/xml_to_json/iPPYHrARXkRVcBYv",
  timeout: TIMEOUT,
})

bggApi.interceptors.response.use(response => {
  return response.data
})

import {authApi} from '@/services/api'

const URL = '/api';

export default {
    getLocations() {
        return authApi.get(URL+'/locations/')
            .then(response => response.data)
    },
}
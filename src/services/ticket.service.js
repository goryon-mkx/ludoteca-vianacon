import { unauthApi } from '@/services/api'

const URL = '/api/tickets/'

export default {
  fetchTickets() {
    return unauthApi
      .get(URL)
      .then(response => response.data)
  },
  fetchValidTickets() {
    return unauthApi
      .get(URL)
      .then(response => {
        return response.data.filter(ticket =>
          new Date(ticket.validFrom) <= new Date()
          && new Date(ticket.validUntil) >= new Date()
        )
      })
  }
}

import { authApi } from '@/services/api'

const URL = '/api/orders/'

const TICKET_RESOURSE_TYPE = 'ProductTicket'

export default {
  createOrder(current_user, products) {
    const order = {
      user: current_user.id,
    }

    order.products = products.map((product) => ({
      resourcetype: TICKET_RESOURSE_TYPE,
      value: product.ticket.price,
      ticket: product.ticket.id,
      name: product.name,
    }))

    return authApi.post(URL, order).then((response) => response.data)
  },
  getOrders(filters) {
    return authApi
      .get(URL, { params: filters })
      .then((response) => response.data)
  },
}

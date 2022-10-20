export default {
  getErrorDescription,
}

function getErrorDescription(response) {
  if (!response || !response.response || response.response.status >= 500) {
    return 'Unexpected error, please contact technical support'
  } else if (response.response.status === 400) {
    return Object.values(response.response.data)[0][0]
  } else {
    return response.response.data.detail
  }
}

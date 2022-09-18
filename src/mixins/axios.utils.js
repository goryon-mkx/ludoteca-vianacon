export default {
  getErrorDescription,
}

function getErrorDescription(response) {
  if (!response || !response.response || response.response.status >= 500) {
    return 'Unexpected error, please contact technical support'
  } else if (response.response.status === 400) {
    console.log(Object.values(response.response.data))
    console.log(Object.values(response.response.data)[0])
    return Object.values(response.response.data)[0][0]
  } else {
    console.log(Object.values(response.response))
    return 'error'
  }
}

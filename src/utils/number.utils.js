export function max(list) {
  return list.reduce((a, b) => Math.max(a, b), -Infinity)
}

export function formatPrice(price){
  return price/100
}

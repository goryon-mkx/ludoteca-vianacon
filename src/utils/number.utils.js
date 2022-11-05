export function max(list) {
  return list.reduce((a, b) => Math.max(a, b), -Infinity)
}

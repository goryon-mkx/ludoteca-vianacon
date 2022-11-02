export function splitName(name) {
  const obj = {}
  if (name.indexOf(' ') < 0) {
    obj['first_name'] = name

    // If more than one name was inserted
    // Break on first space, use first element as first name and all the others use as last name
  } else {
    obj['first_name'] = name.substring(0, name.indexOf(' '))
    obj['last_name'] = name.substring(name.indexOf(' ') + 1, name.length)
  }
  return obj
}

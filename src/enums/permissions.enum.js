export const BadgePermissions = Object.freeze({
  View: Symbol('view_badge'),
})

export const LocationPermissions = Object.freeze({
  View: Symbol('view_location'),
})

export const SettingsPermissions = Object.freeze({
  View: Symbol('view_settings'),
})

const LibraryGame = Object.freeze({
  View: Symbol('view_bgggame'),
})

const StoreGame = Object.freeze({
  View: Symbol('view_storegame'),
})

const UsedGame = Object.freeze({
  View: Symbol('view_usedgame'),
  Change: Symbol('change_usedgame'),
  Add: Symbol('add_usedgame'),
  Delete: Symbol('delete_usedgame'),
})

export const UserPermissions = Object.freeze({
  View: Symbol('view_user'),
  Add: Symbol('add_user'),
})

export const WithdrawPermissions = Object.freeze({
  View: Symbol('view_withdraw'),
})

export const GamePermissions = Object.freeze({
  Store: StoreGame,
  Library: LibraryGame,
  Used: UsedGame,
})

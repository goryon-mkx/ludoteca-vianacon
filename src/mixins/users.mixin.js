import authorizationService from '@/services/authorization.service'

export default {
  methods: {
    isAuthenticated: function () {
      return authorizationService.isAuthenticated()
    },
    isAdmin: function () {
      return this.$store.getters['users/current'].is_superuser
    },
    isStaff: function () {
      return this.$store.getters['users/current'].is_staff
    },
    hasPermission: function (permission) {
      return (
        this.isAdmin() ||
        this.isStaff() ||
        this.$store.getters['users/current'].group_permissions.includes(
          permission.description,
        )
      )
    },
  },
}

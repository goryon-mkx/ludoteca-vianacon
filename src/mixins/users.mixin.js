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
    isAssociate: function () {
      return this.isInGroup('Associate')
    },
    isInGroup: function (group) {
      return this.isUserInGroup(this.$store.getters['users/current'], group)
    },
    isUserInGroup(user, group) {
      return user.groups.includes(group)
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
    getNumberOfQuotasDue(quotas) {
      if (!quotas || !quotas.length) {
        return 1
      } else {
        const lastPaidQuota = quotas.reduce((a, b) => Math.max(a, b), -Infinity)
        return new Date().getFullYear() - lastPaidQuota
      }
    },
  },
}

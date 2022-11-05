import authorizationService from '@/services/authorization.service'
import { max } from '@/utils/number.utils'

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
        return new Date().getFullYear() - this.getLastPaidQuota(quotas)
      }
    },
    getLastPaidQuota(quotas) {
      return max(quotas)
    },
  },
}

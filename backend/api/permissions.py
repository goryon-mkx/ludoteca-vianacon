from rest_framework.permissions import BasePermission


class IsCreate(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return request.method == "POST"

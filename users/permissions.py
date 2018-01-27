from rest_framework import permissions
from rest_framework.compat import is_authenticated


class NotLoggedIn(permissions.BasePermission):

    def has_permission(self, request, view):
        return not is_authenticated(request.user)

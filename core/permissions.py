from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow admin of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS

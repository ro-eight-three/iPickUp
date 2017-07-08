from rest_framework import permissions


class IsBuyer(permissions.BasePermission):
    """
    Custom permissions that check if the object's buyer field
    is the request user
    """

    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user

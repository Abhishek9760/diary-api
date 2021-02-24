from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenticated. Please log out and try again."

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrNotAllowed(permissions.BasePermission):
    message = "You are not owner of this diary"

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSelfUserOrAdminUserOrNotAllowed(permissions.BasePermission):
    message = "This diary is not related to this user."

    def has_object_permission(self, request, view, obj):
        if obj.username != request.user.username:
            return False
        return True

    def has_permission(self, reqeust, view):
        username = view.kwargs.get('username')
        auth_username = reqeust.user.username
        if username != auth_username:
            return False
        return True

from rest_framework.permissions import BasePermission, SAFE_METHODS


class OrderPermisson(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.is_staff



class DenyAll(BasePermission):
    def has_permission(self, request, view):
        return False

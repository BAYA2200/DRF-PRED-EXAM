from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender == True:
            return True
        else:
            return False


class ItemPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and obj.profile.user == request.user:
            return True
        return False


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender == False:
            return True
        else:
            return False


class OrderPermission2(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.profile.is_sender == False and obj.profile.user == request.user:
            return True
        return False

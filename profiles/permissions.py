from rest_framework import permissions

class ProfileOwnerUpdateOnly(permissions.BasePermission):
    """allow users to edit their profile only"""
    def has_object_permission(self, request, view, obj):
        """check if the users are editing their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.id

class FeedOwnerUpdateOnly(permissions.BasePermission):
    """allow users to edit their feed only"""
    def has_object_permission(self, request, view, obj):
        """check if the users are editing their own feed"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.owner.id
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'
    
class IsClerkUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'clerk'   

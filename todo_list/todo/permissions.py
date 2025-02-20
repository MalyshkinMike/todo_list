from rest_framework import permissions
from  rest_framework.permissions import BasePermission



class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user:
            return False
        return request.user.is_staff or obj.user == request.user
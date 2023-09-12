from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser :
            return True
        return False
    
class HasManagerAccess(BasePermission):
    def has_object_permission(self, request, view, obj):
        if object.project_manager == request.user.id :
            return True
        return False
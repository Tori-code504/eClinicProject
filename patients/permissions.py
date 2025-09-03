from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    '''
    -Admins can edit/view all patients
    -Patients can only view/edit their own profile
    '''
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Admin':
            return True
        return obj.user == request.user
    
    def has_permission(self, request, view):
        if view.action == 'list' and request.user.role != 'Admin':
            return False
        return True
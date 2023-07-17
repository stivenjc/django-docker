from rest_framework.permissions import BasePermission

class RoleBasic(BasePermission):
    def has_permission(self, request, view):
        if not request.user.groups.filter(name='Intermedio').exists():
            self.message = 'Debes tener el rol intermdio para poder hacer peticiones.'
            return False

        return True

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.has_perm('projects.permision_normal'):
            self.message = 'Lo siento debes tener el permiso requerido para poder hacer peticiones a esta vista'
            return False

        return True
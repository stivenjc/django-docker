from rest_framework.permissions import BasePermission

class RoleBasic(BasePermission):
    def has_permission(self, request, view):

        # Permitir acceso solo a los usuarios con el rol "Administrador"
        return request.user.groups.filter(name='Intermedio').exists()

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('projects.permision_normal')
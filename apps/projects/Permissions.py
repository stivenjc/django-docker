from rest_framework.permissions import BasePermission
from rolepermissions.checkers import has_permission
from rolepermissions.roles import assign_role
from config.roles import UserTest, TaskTest

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

class CanallTaskPermission(BasePermission):
    message = "I sorry, you can't make that action becouse you don't have permission required"
    def has_permission(self, request, view):
        """
        por ejemplo aqui asignas el role al usuario, y el role tien varios permisos, verificas,
        si el usuario tien un permission en especifico
        """
        assign_role(request.user, UserTest)
        assign_role(request.user, TaskTest)
        return has_permission(request.user, 'tests') and has_permission(request.user, "testss")
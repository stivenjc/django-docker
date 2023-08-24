from rolepermissions.roles import AbstractUserRole


class UserTest(AbstractUserRole):
    available_permissions = {
        "test": True,
    }


class TaskTest(AbstractUserRole):
    available_permissions = {
        "tests": True,
        "testss": True,
    }
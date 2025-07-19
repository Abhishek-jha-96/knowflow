from enum import Enum


class PermissionActionName(Enum):
    ALL_OBJECTS = "all objects"


"""
Constants for custom_exception_handler start
"""
THROTTLE_EXEC_DETAILS = "request limit exceeded available in %d seconds"
NOT_FOUND_EXEC_DETAILS = "Item Not Found"
VALIDATION_EXEC_DETAILS = "Validation Error"
INTERNAL_ERROR_EXEC_DETAILS = "Internal Server Error"

API_EXC_DEFAULT_CODE = "error"
"""
Constants for custom_exception_handler ends
"""

"""
Constants for logger_mixin start
"""
ANONYMOUS = "Anonymous"
"""
Constants for logger_mixin ends
"""

"""
Constants for APP Names starts
"""
CORE_APP = "apps.core"
USER_APP = "apps.user"
"""
Constants for APP Names ends
"""
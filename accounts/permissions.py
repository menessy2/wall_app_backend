from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in [ 'create', 'login_user' ]:
            return True

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS or view.action in [ 'create', 'login_user' ]:
            return True

        # Instance must have an attribute named `owner`.
        return obj == request.user
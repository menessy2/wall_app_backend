from rest_framework import permissions

class PostPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS or view.action == 'list':
            return True

        # Instance must have an attribute named `owner`.
        return obj.creator == request.user
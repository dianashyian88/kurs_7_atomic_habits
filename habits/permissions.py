from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user == obj.owner:
                return True


class ViewPublicHabits(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in ['GET']:
            if obj.is_public:
                return True

from rest_framework.permissions import BasePermission


class IsAuthenticatedOrReadOnly(BasePermission):
    """Placeholder permission for future account endpoints."""

    def has_permission(self, request, view):
        return request.method in {"GET", "HEAD", "OPTIONS"} or bool(request.user and request.user.is_authenticated)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserCreateSerializer, UserSerializer


class UserListView(APIView):
    """Placeholder list view for future account endpoints."""

    def get(self, request, *args, **kwargs):
        return Response({"detail": "Accounts endpoints will be implemented in a future phase."})


class RegisterView(APIView):
    """Create a new user account."""

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(user).data
        return Response(user_data, status=status.HTTP_201_CREATED)

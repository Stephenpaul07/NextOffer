from rest_framework import serializers

from .models import User
from .services import register_user


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user read operations."""

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "is_active", "created_at", "updated_at"]
        read_only_fields = fields


class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for user creation input validation."""

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        password = validated_data.pop("password")
        return register_user(password=password, **validated_data)

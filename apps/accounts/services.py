from typing import Any

from .models import User


def register_user(*, email: str, password: str, first_name: str = "", last_name: str = "") -> User:
    """Placeholder service for creating a new user account."""
    return User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )


def update_profile(*, user: User, first_name: str | None = None, last_name: str | None = None) -> User:
    """Placeholder service for updating a user's profile fields."""
    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name

    user.save(update_fields=["first_name", "last_name", "updated_at"])
    return user

from uuid import UUID

from .models import User


def get_user_by_email(*, email: str) -> User | None:
    """Return a user by email address, if one exists."""
    return User.objects.filter(email__iexact=email).first()


def get_user_by_id(*, user_id: UUID | str) -> User | None:
    """Return a user by primary key, if one exists."""
    return User.objects.filter(pk=user_id).first()

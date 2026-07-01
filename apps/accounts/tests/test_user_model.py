import pytest
from django.db import IntegrityError

from apps.accounts.models import User


@pytest.mark.django_db
def test_create_user_with_normalized_email_and_profile_fields():
    user = User.objects.create_user(
        email="Test.User@Example.COM",
        password="StrongPassword123!",
        first_name="Test",
        last_name="User",
    )

    assert user.email == "test.user@example.com"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False
    assert user.check_password("StrongPassword123!") is True


@pytest.mark.django_db
def test_create_superuser_sets_staff_and_superuser_flags():
    user = User.objects.create_superuser(
        email="admin@example.com",
        password="AdminPassword123!",
    )

    assert user.is_staff is True
    assert user.is_superuser is True
    assert user.is_active is True


@pytest.mark.django_db
def test_email_must_be_unique():
    User.objects.create_user(
        email="duplicate@example.com",
        password="StrongPassword123!",
    )

    with pytest.raises(IntegrityError):
        User.objects.create_user(
            email="duplicate@example.com",
            password="AnotherPassword123!",
        )

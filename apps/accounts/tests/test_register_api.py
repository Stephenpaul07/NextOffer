import pytest
from django.urls import reverse

from apps.accounts.models import User


@pytest.mark.django_db
def test_register_endpoint_creates_user_with_201(client):
    url = reverse("accounts-register")
    response = client.post(
        url,
        {
            "email": "new.user@example.com",
            "password": "StrongPassword123!",
            "first_name": "New",
            "last_name": "User",
        },
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.json()["email"] == "new.user@example.com"
    assert User.objects.filter(email="new.user@example.com").exists() is True


@pytest.mark.django_db
def test_register_endpoint_returns_validation_errors_with_400(client):
    url = reverse("accounts-register")
    response = client.post(
        url,
        {"email": "", "password": "123"},
        content_type="application/json",
    )

    assert response.status_code == 400
    assert "email" in response.json()
    assert "password" in response.json()

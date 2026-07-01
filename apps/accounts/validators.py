from django.core.exceptions import ValidationError


def validate_email_address(email: str) -> str:
    """Return a normalized email address or raise a validation error."""
    if not email or not isinstance(email, str):
        raise ValidationError("Email address is required.")

    normalized_email = email.strip().lower()
    if "@" not in normalized_email:
        raise ValidationError("Enter a valid email address.")

    return normalized_email

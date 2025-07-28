from django.core.exceptions import ValidationError


def validate_password_uppercase(value):
    if not any(char.isupper() for char in value):
        raise ValidationError("Password must contain at least one uppercase letter.")

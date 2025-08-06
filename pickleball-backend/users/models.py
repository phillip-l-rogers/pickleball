"""
Models for the users app.

Defines a custom user model (`CustomUser`) based on Django's AbstractUser.
This allows future flexibility for extending user fields or authentication behavior.
"""

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's built-in AbstractUser.

    Currently identical to AbstractUser but acts as a placeholder for future
    customization (e.g., adding profile image, roles, or settings).
    """

    # Add custom fields here if needed in the future
    pass

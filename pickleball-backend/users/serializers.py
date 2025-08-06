"""
Serializers for the users app.

Includes:
- RegisterSerializer: Handles user registration by securely creating users.
- UserSerializer: Serializes basic user data (ID, username, email).
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Accepts username and password and creates a new user with hashed password.
    """

    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Creates a user using Django's built-in `create_user` method
        to ensure the password is hashed.
        """
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user data.

    Used for displaying user information in responses such as user list or profile views.
    """

    class Meta:
        model = User
        fields = ["id", "username", "email"]
        read_only_fields = ["id", "username", "email"]

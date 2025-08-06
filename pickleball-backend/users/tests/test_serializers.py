"""
Unit tests for serializers in the users app.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from users.serializers import RegisterSerializer, UserSerializer

User = get_user_model()


class UserSerializerTest(TestCase):
    """
    Tests for the UserSerializer class.
    """

    def test_user_serializer_output(self):
        """
        Test that the UserSerializer correctly serializes user fields.
        """
        user = User.objects.create_user(
            username="testuser", password="securepass", email="test@example.com"
        )
        serializer = UserSerializer(user)
        data = serializer.data

        self.assertEqual(data["id"], user.id)
        self.assertEqual(data["username"], "testuser")
        self.assertEqual(data["email"], "test@example.com")


class RegisterSerializerTest(TestCase):
    """
    Tests for the RegisterSerializer class.
    """

    def test_register_serializer_creates_user(self):
        """
        Test that the RegisterSerializer creates a new user with hashed password.
        """
        data = {"username": "newuser", "password": "newpass123"}
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        self.assertEqual(user.username, "newuser")
        self.assertTrue(user.check_password("newpass123"))

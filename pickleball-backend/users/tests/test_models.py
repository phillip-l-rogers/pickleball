"""
Unit tests for the CustomUser model.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class CustomUserModelTest(TestCase):
    """
    Tests for creating regular and super users using the CustomUser model.
    """

    def test_create_user(self):
        """
        Test that a regular user can be created with a username and password.
        """
        user = User.objects.create_user(username="testuser", password="securepass")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("securepass"))
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        """
        Test that a superuser can be created with elevated permissions.
        """
        admin = User.objects.create_superuser(username="admin", password="adminpass")
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)

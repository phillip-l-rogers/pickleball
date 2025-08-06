"""
Unit tests for API views in the users app.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

User = get_user_model()


class UserViewsTest(TestCase):
    """
    Tests for user-related API views such as /me/ and /all/.
    """

    def setUp(self):
        """
        Set up a test user and initialize the API client.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="pass123", email="user@example.com"
        )

    def test_me_view_requires_auth(self):
        """
        Test that unauthenticated access to /api/users/me/ returns 401.
        """
        response = self.client.get("/api/users/me/")
        self.assertEqual(response.status_code, 401)

    def test_me_view_returns_current_user(self):
        """
        Test that the /me/ endpoint returns data for the authenticated user.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/users/me/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], self.user.username)

    def test_all_users_view(self):
        """
        Test that the /all/ endpoint returns a list of users for authenticated requests.
        """
        User.objects.create_user(username="user2", password="pass456")
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/users/all/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

"""
Test suite for the tournaments app API.

Covers:
- Listing and creating tournaments
- Signup and cancellation actions
"""

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from tournaments.models import PlayerSignup, Tournament

User = get_user_model()


class TournamentAPITests(APITestCase):
    """Test API endpoints for creating and managing tournaments."""

    def setUp(self):
        """Create a test user and an initial tournament for reuse."""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.tournament = Tournament.objects.create(
            name="Test Tournament", start_date=timezone.now().date()
        )

    def test_list_tournaments(self):
        """Should return a list of tournaments including the seeded one."""
        response = self.client.get("/api/tournaments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_single_day_tournament(self):
        """Should create a valid single-day tournament."""
        data = {
            "name": "New Tournament",
            "start_date": timezone.now().date(),
            "is_league": False,
        }
        response = self.client.post("/api/tournaments/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_create_league_missing_fields(self):
        """Should reject a league tournament missing required fields."""
        data = {
            "name": "Bad League",
            "start_date": timezone.now().date(),
            "is_league": True,
        }
        response = self.client.post("/api/tournaments/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_user_for_tournament(self):
        """Should allow an authenticated user to sign up for a tournament."""
        url = f"/api/tournaments/{self.tournament.id}/signup/"
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            PlayerSignup.objects.filter(
                user=self.user, tournament=self.tournament
            ).exists()
        )

    def test_cancel_signup(self):
        """Should allow a user to cancel a tournament signup."""
        PlayerSignup.objects.create(user=self.user, tournament=self.tournament)
        url = f"/api/tournaments/{self.tournament.id}/cancel_signup/"
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            PlayerSignup.objects.filter(
                user=self.user, tournament=self.tournament
            ).exists()
        )

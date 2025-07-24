"""
Serializer tests for the tournaments app.

Covers:
- TournamentSerializer: Validates league rules and date logic
- PlayerSignupSerializer: Validates signup creation and required fields
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from tournaments.models import Tournament
from tournaments.serializers import PlayerSignupSerializer, TournamentSerializer

User = get_user_model()


class TournamentSerializerTests(TestCase):
    """Tests for validating the TournamentSerializer logic and league constraints."""

    def setUp(self):
        self.today = timezone.now().date()

    def test_valid_single_day_tournament(self):
        """Should accept a single-day tournament with only start_date."""
        data = {
            "name": "Pop-up Tournament",
            "start_date": self.today,
            "is_league": False,
        }
        serializer = TournamentSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_single_day_missing_date(self):
        """Should fail if start_date is missing on a single-day tournament."""
        data = {"name": "Oops Tournament", "is_league": False}
        serializer = TournamentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("start_date", serializer.errors)

    def test_valid_league_tournament(self):
        """Should accept a valid league tournament with required fields."""
        data = {
            "name": "Spring League",
            "start_date": self.today,
            "end_date": self.today + timezone.timedelta(weeks=4),
            "game_day": "Monday",
            "is_league": True,
        }
        serializer = TournamentSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_league_missing_fields(self):
        """Should fail if league tournament is missing end_date or game_day."""
        data = {
            "name": "Incomplete League",
            "start_date": self.today,
            "is_league": True,
        }
        serializer = TournamentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)


class PlayerSignupSerializerTests(TestCase):
    """Tests for the PlayerSignupSerializer to ensure data is valid and serialized."""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.tournament = Tournament.objects.create(
            name="Signup Test", start_date=timezone.now().date()
        )

    def test_valid_signup_data(self):
        """Should serialize and validate a correct player signup."""
        data = {
            "user": self.user.id,
            "tournament": self.tournament.id,
        }
        serializer = PlayerSignupSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_missing_user_field(self):
        """Should fail validation if user field is missing."""
        data = {
            "tournament": self.tournament.id,
        }
        serializer = PlayerSignupSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("user", serializer.errors)

    def test_missing_tournament_field(self):
        """Should fail validation if tournament field is missing."""
        data = {
            "user": self.user.id,
        }
        serializer = PlayerSignupSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("tournament", serializer.errors)

    def test_read_only_fields_ignored(self):
        """Should ignore id and joined_at if provided manually."""
        data = {
            "user": self.user.id,
            "tournament": self.tournament.id,
            "id": 99,
            "joined_at": timezone.now(),
        }
        serializer = PlayerSignupSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn("id", serializer.validated_data)
        self.assertNotIn("joined_at", serializer.validated_data)

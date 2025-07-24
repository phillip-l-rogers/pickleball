"""
Model tests for the tournaments app.

Covers:
- Tournament model logic for league detection and duration
- PlayerSignup model constraints and string representations
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from tournaments.models import PlayerSignup, Tournament
from tournaments.serializers import PlayerSignupSerializer

User = get_user_model()


class TournamentModelTests(TestCase):
    """
    Tests for the Tournament model logic.

    The tests include duration and is_multi_week detection.
    """

    def setUp(self):
        self.today = timezone.now().date()

    def test_single_day_tournament(self):
        """A tournament without end_date or game_day should be treated as single-day."""
        tournament = Tournament.objects.create(
            name="One Day Bash",
            start_date=self.today,
            is_league=False,
        )
        self.assertFalse(tournament.is_league)
        self.assertFalse(tournament.is_multi_week)
        self.assertEqual(tournament.duration_weeks, 1)

    def test_multi_week_tournament_valid(self):
        """A valid league tournament with end_date and game_day should be multi-week."""
        tournament = Tournament.objects.create(
            name="Weekly League",
            start_date=self.today,
            end_date=self.today + timezone.timedelta(weeks=3),
            game_day="Wednesday",
            is_league=True,
        )
        self.assertTrue(tournament.is_league)
        self.assertTrue(tournament.is_multi_week)
        self.assertEqual(tournament.duration_weeks, 3)

    def test_multi_week_tournament_missing_fields(self):
        """Missing end_date or game_day should invalidate multi-week detection."""
        tournament = Tournament.objects.create(
            name="Incomplete League",
            start_date=self.today,
            is_league=True,
        )
        self.assertTrue(tournament.is_league)
        self.assertFalse(tournament.is_multi_week)
        self.assertEqual(tournament.duration_weeks, 1)


class PlayerSignupTests(TestCase):
    """Tests for the PlayerSignup model and serializer validation."""

    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="testpass")
        self.user2 = User.objects.create_user(username="bob", password="testpass")
        self.tournament = Tournament.objects.create(
            name="Signup Test", start_date=timezone.now().date()
        )

    def test_player_can_signup(self):
        """User can sign up for a tournament and str returns readable text."""
        signup = PlayerSignup.objects.create(
            user=self.user1, tournament=self.tournament
        )
        self.assertEqual(str(signup), f"alice signed up for {self.tournament.name}")

    def test_duplicate_signup_prevented(self):
        """User cannot sign up for the same tournament more than once."""
        PlayerSignup.objects.create(user=self.user1, tournament=self.tournament)
        with self.assertRaises(Exception):
            PlayerSignup.objects.create(user=self.user1, tournament=self.tournament)

    def test_signup_serializer_valid(self):
        """PlayerSignupSerializer validates correct signup input."""
        data = {"user": self.user2.id, "tournament": self.tournament.id}
        serializer = PlayerSignupSerializer(data=data)
        self.assertTrue(serializer.is_valid())

"""
Models for managing pickleball tournaments and player signups.

Includes support for both single-day and multi-week (league-style) tournaments.
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

DAYS_OF_WEEK = [
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
]


class Tournament(models.Model):
    """
    Represents a pickleball tournament.

    Supports both single-day tournaments and multi-week leagues.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    game_day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, blank=True)
    is_league = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self) -> str:
        return str(self.name)

    @property
    def duration_weeks(self) -> int:
        """
        Returns the number of weeks the tournament spans.

        - Returns 1 for single-day tournaments.
        - Computes duration based on start_date and end_date for leagues.
        """
        if self.is_multi_week:
            return max(1, ((self.end_date - self.start_date).days + 1) // 7)
        return 1

    @property
    def is_multi_week(self) -> bool:
        """
        Determines if the league spans multiple weeks.

        Returns True if `is_league` and `end_date` and `game_day` are set and
        `end_date` is after `start_date`.
        """
        return bool(
            self.is_league
            and self.game_day
            and self.end_date
            and self.start_date
            and self.end_date > self.start_date
        )


class PlayerSignup(models.Model):
    """
    Links a user to a tournament signup.

    Each user can only sign up once per tournament.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name="signups"
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ensures each user can sign up only once per tournament."""

        unique_together = ("user", "tournament")

    def __str__(self) -> str:
        return f"{self.user.username} signed up for {self.tournament.name}"

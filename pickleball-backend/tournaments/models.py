"""
Models for managing pickleball tournaments, player signups, and organizers.

Supports both single-day and multi-week (league-style) tournaments.
Includes user-to-tournament associations for signups and organizer roles.
"""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Days used for scheduling league games
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

    Can be either a single-day event or a recurring league.
    Organizers are associated per tournament via a many-to-many relationship.
    """

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    game_day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, blank=True)
    is_league = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_tournaments",
    )
    organizers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="organized_tournaments", blank=True
    )

    @property
    def duration_weeks(self) -> int:
        """
        Calculates the number of weeks the tournament spans.

        Returns 1 for single-day events.
        """
        if self.end_date and self.is_multi_week:
            return max(1, ((self.end_date - self.start_date).days + 1) // 7)
        return 1

    @property
    def is_multi_week(self) -> bool:
        """Determines whether the tournament is a multi-week league."""
        return bool(
            self.is_league
            and self.game_day
            and self.end_date
            and self.start_date
            and self.end_date > self.start_date
        )

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        """Adds the creator as an organizer when the tournament is first saved."""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.organizers.add(self.created_by)


class PlayerSignup(models.Model):
    """
    Connects a user to a tournament as a registered player.

    Each user can sign up once per tournament.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name="signups"
    )
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "tournament")
        verbose_name = _("Player Signup")
        verbose_name_plural = _("Player Signups")

    def __str__(self) -> str:
        return f"{self.user.username} signed up for {self.tournament.name}"

"""
Management command to seed the database with sample data.

Creates test users, sample tournaments (single-day and league-style),
and player signups for development or demonstration purposes.
"""

import random
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from tournaments.models import PlayerSignup, Tournament

User = get_user_model()


class Command(BaseCommand):
    """
    Django management command to populate the database with test data.

    This includes:
    - Deleting non-superuser users, tournaments, and player signups
    - Creating 5 test users
    - Creating 2 tournaments (one single-day, one league)
    - Randomly assigning 3 players to each tournament
    """

    help = "Seeds the database with sample tournaments and users"

    def handle(self, *args, **kwargs):
        """
        Entry point for the command. Executes all seed logic:
        clears data, creates users and tournaments, and populates signups.
        """
        self.stdout.write("Seeding data...")

        # Clear existing data
        PlayerSignup.objects.all().delete()
        Tournament.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # Create users
        users = [
            User.objects.create_user(username=f"user{i}", password="testpass")
            for i in range(5)
        ]

        # Create tournaments
        today = timezone.now().date()
        Tournament.objects.create(
            name="One Day Open",
            start_date=today + timedelta(days=7),
            is_league=False,
        )
        Tournament.objects.create(
            name="Summer League",
            start_date=today + timedelta(days=14),
            end_date=today + timedelta(days=70),
            game_day="Wednesday",
            is_league=True,
        )

        # Random signups
        for t in Tournament.objects.all():
            for user in random.sample(users, 3):
                PlayerSignup.objects.create(user=user, tournament=t)

        self.stdout.write(self.style.SUCCESS("✅ Seeding complete."))

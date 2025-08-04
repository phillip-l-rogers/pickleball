import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from tournaments.models import PlayerSignup, Tournament


class Command(BaseCommand):
    help = "Seeds the database with sample tournaments and users"

    def handle(self, *args, **kwargs):
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

        self.stdout.write(self.style.SUCCESS("✅ Seeding complete."))

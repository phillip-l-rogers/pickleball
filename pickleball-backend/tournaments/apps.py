"""App config for the tournaments Django app."""

from django.apps import AppConfig


class TournamentsConfig(AppConfig):
    """AppConfig for tournaments."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "tournaments"

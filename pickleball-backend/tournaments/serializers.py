"""
Serializers for the tournaments app.

Includes serializers for Tournament and PlayerSignup models, with custom
validation logic for league vs. single-day tournaments.
"""

from rest_framework import serializers

from .models import PlayerSignup, Tournament


class TournamentSerializer(serializers.ModelSerializer):
    """
    Serializer for Tournament model.

    Serializes all fields of the Tournament model and includes validation
    for required fields based on whether the tournament is a league or single-day.
    """

    class Meta:
        """
        Meta options for TournamentSerializer.

        - Uses the Tournament model.
        - Serializes all fields.
        """

        model = Tournament
        fields = "__all__"

    def get_players(self, obj):
        """
        Returns a list of player signups associated with the tournament.

        Each player signup will be a dictionary with user ID and username.
        """

        return [
            {"id": ps.user.id, "name": ps.user.username} for ps in obj.signups.all()
        ]

    def validate(self, attrs):
        """
        Validates required fields based on the tournament type.

        - If the tournament is a league, ensures `start_date`, `end_date`, and
          `game_day` are provided.
        - If it is a single-day tournament, ensures only `start_date` is provided.
        """
        is_league = attrs.get("is_league")
        if is_league:
            if (
                not attrs.get("start_date")
                or not attrs.get("end_date")
                or not attrs.get("game_day")
            ):
                raise serializers.ValidationError(
                    "League tournaments must include start date, end date, and game day."
                )
        else:
            if not attrs.get("start_date"):
                raise serializers.ValidationError(
                    "Single-day tournaments must include a start date."
                )
        return attrs


class PlayerSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for PlayerSignup model.

    Handles serialization of player signups with user, tournament, and timestamp.
    `id` and `joined_at` are read-only fields.
    """

    class Meta:
        """
        Meta options for PlayerSignupSerializer.

        - Uses the PlayerSignup model.
        - Includes fields: id, user, tournament, joined_at.
        - Makes id and joined_at read-only.
        """

        model = PlayerSignup
        fields = ["id", "user", "tournament", "joined_at"]
        read_only_fields = ["id", "joined_at"]

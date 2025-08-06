"""
Serializers for the tournaments app.

Includes serializers for Tournament and PlayerSignup models, with custom
validation logic for league vs. single-day tournaments and organizer assignment.
"""

from rest_framework import serializers

from .models import PlayerSignup, Tournament


class PlayerSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for PlayerSignup model.

    Handles serialization of player signups with user, tournament, and timestamp.
    `id` and `joined_at` are read-only fields.
    """

    class Meta:
        model = PlayerSignup
        fields = ["id", "user", "tournament", "joined_at"]
        read_only_fields = ["id", "joined_at"]


class TournamentSerializer(serializers.ModelSerializer):
    """
    Serializer for Tournament model.

    Serializes all fields of the Tournament model.
    Enforces validation rules depending on whether the tournament is a league.
    Adds organizers and creator as read-only fields for clarity.
    """

    organizers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tournament
        fields = "__all__"
        read_only_fields = ["id", "created_at", "created_by", "organizers"]

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

        - League tournaments must include start_date, end_date, and game_day.
        - Single-day tournaments require only start_date.
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

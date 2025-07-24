"""
API views for managing pickleball tournaments and player signups.

Includes endpoints for listing tournaments, creating/updating them, signing up users,
and canceling signups.
"""

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PlayerSignup, Tournament
from .serializers import TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    ViewSet for CRUD operations on Tournament instances.

    Provides standard create, retrieve, update, and delete operations, along with custom
    actions for user signup and canceling signup.
    """

    queryset = Tournament.objects.all().order_by("-created_at")
    serializer_class = TournamentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(
        detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated]
    )
    def signup(self, request, pk=None):  # pylint: disable=unused-argument
        """
        Signs the authenticated user up for the specified tournament.

        Prevents duplicate signups. Returns a success or error response.
        """
        tournament = self.get_object()
        user = request.user

        # Prevent duplicate signups
        if PlayerSignup.objects.filter(user=user, tournament=tournament).exists():
            return Response(
                {"detail": "Already signed up."}, status=status.HTTP_400_BAD_REQUEST
            )

        PlayerSignup.objects.create(user=user, tournament=tournament)
        return Response(
            {"detail": "Signed up successfully!"}, status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=["post"])
    def cancel_signup(self, request, pk=None):  # pylint: disable=unused-argument
        """
        Cancels the authenticated user's signup for the specified tournament.

        Returns 204 if successful, or 400 if the user was not signed up.
        """
        user = request.user
        tournament = self.get_object()

        try:
            signup = PlayerSignup.objects.get(user=user, tournament=tournament)
            signup.delete()
            return Response(
                {"detail": "Signup cancelled."}, status=status.HTTP_204_NO_CONTENT
            )
        except PlayerSignup.DoesNotExist:
            return Response(
                {"detail": "You are not signed up for this tournament."},
                status=status.HTTP_400_BAD_REQUEST,
            )

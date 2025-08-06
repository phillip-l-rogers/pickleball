"""
Views for the users app.

Includes API endpoints for:
- Retrieving the current authenticated user's data.
- Listing all users (useful for assigning tournament organizers or for admin purposes).
"""

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from users.serializers import UserSerializer

User = get_user_model()


class CurrentUserView(generics.RetrieveAPIView):
    """
    API view to retrieve the currently authenticated user's data.

    - Method: GET
    - URL: /api/users/me/
    - Permissions: Requires authentication
    - Response: JSON representation of the current user
    """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    """
    API view to list all registered users.

    - Method: GET
    - URL: /api/users/all/
    - Permissions: Requires authentication
    - Response: List of all users (id, username, email, etc.)
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
URL configuration for the users app.

Defines user-related API endpoints such as:
- /api/users/me/: Returns the currently authenticated user's data.
- /api/users/all/: Lists all registered users (useful for admin or organizer features).

These routes are intended to be included under the /api/users/ namespace
from the project's main URL configuration (config/urls.py).
"""

from django.urls import path
from users import views

urlpatterns = [
    path("me/", views.CurrentUserView.as_view(), name="user-me"),
    path("all/", views.UserListView.as_view(), name="user-list"),
]

"""
Project URL configuration for the Pickleball Tournament App.

- Admin panel at /admin/
- Djoser authentication routes at /auth/
- Tournament API endpoints at /api/ (from tournaments app)
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Djoser auth endpoints (user registration, login/logout)
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    # Tournament API
    path("api/", include("tournaments.urls")),
    # User API
    path("api/users/", include("users.urls")),
]

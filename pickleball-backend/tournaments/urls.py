"""
URL configuration for the tournaments app.

Uses Django REST Framework's DefaultRouter to automatically generate
CRUD endpoints for the TournamentViewSet.

All routes are expected to be included under the /api/ path in the project-level config.
"""

from rest_framework.routers import DefaultRouter
from tournaments.views import TournamentViewSet

# Initialize DRF router and register the TournamentViewSet
router = DefaultRouter()
router.register(r"tournaments", TournamentViewSet)
# Expose the generated URLs as urlpatterns
urlpatterns = router.urls

"""
URL configuration for the tournaments app.

Uses Django REST Framework's DefaultRouter to automatically generate
CRUD routes for the TournamentViewSet.
"""

from rest_framework.routers import DefaultRouter

from .views import TournamentViewSet

# Initialize DRF router and register the TournamentViewSet
router = DefaultRouter()
router.register(r"tournaments", TournamentViewSet)
# Expose the generated URLs as urlpatterns
urlpatterns = router.urls

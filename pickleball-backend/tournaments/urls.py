from rest_framework.routers import DefaultRouter

from .views import TournamentViewSet

router = DefaultRouter()
router.register(r"tournaments", TournamentViewSet)

urlpatterns = router.urls

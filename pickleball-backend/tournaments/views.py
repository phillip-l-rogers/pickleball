from rest_framework import viewsets

from .models import Tournament
from .serializers import TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

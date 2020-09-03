from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, permissions

# Serve Vue Application
from rest_framework.pagination import PageNumberPagination

from backend.api.models import LibraryGame
from backend.api.serializers import LibraryGameSerializer
from backend.api.utils import BggGameUtils


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50


class LibraryGameViewSet(viewsets.ModelViewSet):
    queryset = LibraryGame.objects.order_by('game__name')
    serializer_class = LibraryGameSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        bggid = serializer.data['game_id']
        game = BggGameUtils.find(bggid)

        if game is None:
            game = BggGameUtils.create(bggid)

        serializer.game = game
        serializer.save()

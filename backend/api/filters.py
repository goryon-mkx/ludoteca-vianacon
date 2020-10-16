from django_filters import rest_framework as filters

from backend.api.models import LibraryGame, Player


class LibraryGameFilter(filters.FilterSet):
    location = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LibraryGame
        fields = ['owner']

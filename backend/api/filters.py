from django_filters import rest_framework as filters

from backend.api.models import LibraryGame, Player


class PlayerFilter(filters.FilterSet):
    games_owned_gt = filters.NumberFilter(field_name='librarygame', lookup_expr='gt')

    class Meta:
        model = Player
        exclude = '__all__'


class LibraryGameFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status')

    class Meta:
        model = LibraryGame
        fields = ['owner', 'location']

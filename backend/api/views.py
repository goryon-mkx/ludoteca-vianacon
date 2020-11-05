from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import viewsets, permissions, generics
from rest_framework import filters
from django_filters import rest_framework as django_filters

# Serve Vue Application
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication

from backend.api.filters import LibraryGameFilter, PlayerFilter
from backend.api.models import LibraryGame, Player, Withdraw
from backend.api.serializers import LibraryGameSerializer, UserSerializer, PlayerSerializer, WithdrawSerializer
from backend.api.utils import BggGameUtils


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50


# class OwnerViewSet(viewsets.ModelViewSet):
#     queryset = Player.objects.annotate(num_games=Count('librarygame')).filter(num_games__gt=0)
#     serializer_class = PlayerSerializer
#     authentication_classes = (authentication.JWTAuthentication,)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ['name', 'email']
#     permission_classes = (permissions.IsAdminUser,)
#

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.order_by('name')
    serializer_class = PlayerSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = PlayerFilter
    search_fields = ['name', 'email']
    # permission_classes = (permissions.IsAdminUser,)


class LibraryGameViewSet(viewsets.ModelViewSet):
    queryset = LibraryGame.objects.order_by('game__name')
    serializer_class = LibraryGameSerializer
    search_fields = ['game__name']
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = LibraryGameFilter
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    authentication_classes = [authentication.JWTAuthentication]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        bggid = serializer.initial_data['game_id']
        game = BggGameUtils.find(bggid)

        if game is None:
            game = BggGameUtils.create(bggid)

        serializer.is_valid()
        serializer.save(game=game)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()


class WithdrawViewSet(viewsets.ModelViewSet):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (permissions.IsAdminUser,)


class StatisticsViewSet(APIView):
    def get(self, request, format=None):
        library_games = {
            "total": LibraryGame.objects.all().count(),
            "being_played": LibraryGame.objects.filter(withdraw__date_returned__isnull=True)
        }

        return Response({"library_games": library_games})


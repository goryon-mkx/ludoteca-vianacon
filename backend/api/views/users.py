from datetime import timedelta

from django.utils import timezone
from django_filters import rest_framework as django_filters
from django_rest_passwordreset.models import (
    ResetPasswordToken,
    clear_expired,
    get_password_reset_token_expiry_time,
)
from django_rest_passwordreset.views import (
    HTTP_IP_ADDRESS_HEADER,
    HTTP_USER_AGENT_HEADER,
)
from rest_framework import filters, generics, mixins, permissions, viewsets
from rest_framework_simplejwt import authentication

from backend.api import permissions as custom_permissions
from backend.api.models import Quota, Ticket, TicketUser
from backend.api.serializers.users import (
    PlayerSerializer,
    QuotaSerializer,
    TicketSerializer,
    TicketUserSerializer,
    UserSerializer,
)
from backend.api.signals import user_created
from backend.api.utils.utils import StandardResultsSetPagination
from backend.api.views.games import User


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("first_name", "last_name")
    serializer_class = PlayerSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    search_fields = ["first_name", "last_name", "username", "email"]
    # permission_classes = (permissions.IsAdminUser,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("first_name", "last_name")
    serializer_class = UserSerializer
    authentication_classes = [authentication.JWTAuthentication]
    filter_backends = (
        filters.SearchFilter,
        django_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    search_fields = ["first_name", "last_name", "email"]
    permission_classes = [
        custom_permissions.IsCreate
        | permissions.IsAdminUser
        | permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
    pagination_class = StandardResultsSetPagination

    def get_object(self):
        pk = self.kwargs.get("pk")

        if pk == "current":
            return self.request.user

        return super().get_object()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        print(response.data)
        self.create_token(response.data, request.META)
        return response

    def create_token(self, data, meta):
        """Not proud of this, but there was no other way to do it :("""

        # before we continue, delete all existing expired tokens
        password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # datetime.now minus expiry hours
        now_minus_expiry_time = timezone.now() - timedelta(
            hours=password_reset_token_validation_time
        )

        # delete all tokens where created_at < now - 24 hours
        clear_expired(now_minus_expiry_time)

        user = User.objects.get(email=data["email"])

        # check if the user already has a token
        if user.password_reset_tokens.all().count() > 0:
            # yes, already has a token, re-use this token
            token = user.password_reset_tokens.all()[0]
        else:
            # no token exists, generate a new token
            token = ResetPasswordToken.objects.create(
                user=user,
                user_agent=meta.get(HTTP_USER_AGENT_HEADER, ""),
                ip_address=meta.get(HTTP_IP_ADDRESS_HEADER, ""),
            )
        # send a signal that the password token was created
        # let whoever receives this signal handle sending the email for the password reset
        user_created.send(
            sender=self.__class__, instance=self, reset_password_token=token
        )


class QuotaViewSet(viewsets.ModelViewSet):
    queryset = Quota.objects.all().order_by("year")
    serializer_class = QuotaSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = [
        permissions.IsAdminUser | permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class TicketUserViewSet(viewsets.ModelViewSet):
    queryset = TicketUser.objects.all()
    serializer_class = TicketUserSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = [
        custom_permissions.IsCreate
        | permissions.IsAdminUser
        | permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class TicketUserBulkCreateView(viewsets.ViewSet, generics.CreateAPIView):
    queryset = TicketUser.objects.all()
    serializer_class = TicketUserSerializer

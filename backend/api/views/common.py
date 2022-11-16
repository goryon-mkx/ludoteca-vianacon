from rest_framework import permissions, viewsets
from rest_framework_simplejwt import authentication

from backend.api.models import Event
from backend.api.serializers.common import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.order_by("start")
    serializer_class = EventSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = [
        permissions.IsAdminUser | permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
    search_fields = ["name"]

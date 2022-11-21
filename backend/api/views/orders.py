from django_filters import rest_framework as django_filters
from rest_framework import permissions, viewsets
from rest_framework_simplejwt import authentication

from backend.api.filters import OrderFilter
from backend.api.models import Order, Product
from backend.api.serializers.order import OrderSerializer, ProductPolymorphicSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductPolymorphicSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

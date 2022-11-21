import django.core.exceptions
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from backend.api.models import Order, Product, ProductTicket
from backend.api.signals import new_order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("value",)


class ProductTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTicket
        fields = ("value", "ticket", "name")


class ProductPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Product: ProductSerializer,
        ProductTicket: ProductTicketSerializer,
    }


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.ListSerializer(child=ProductPolymorphicSerializer())

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        orders = Order.objects.filter(user__id=validated_data.get("user").id)
        if len(orders) > 1:
            raise django.core.exceptions.PermissionDenied

        products = validated_data.pop("products")
        order = Order.objects.create(**validated_data)
        for product in products:
            resource_type = product.pop("resourcetype")
            if resource_type == "ProductTicket":
                order.total += product.get("ticket").price
                p = ProductTicket.objects.create(**product)
                order.products.add(p)
                order.save()

        new_order.send(sender=self.__class__, instance=self, order=order)
        return order

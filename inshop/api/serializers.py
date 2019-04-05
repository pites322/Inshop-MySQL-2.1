from rest_framework import serializers
from app1.models import Product, ShoppingList


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = []


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        exclude = []



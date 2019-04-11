from rest_framework import serializers
from app1.models import Product, ShoppingList, User, Color


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        exclude = []


class ProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)
    class Meta:
        model = Product
        exclude = []


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    buyer = UserSerializer()

    class Meta:
        model = ShoppingList
        exclude = []


class BasketAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = ['product', 'price', 'product_name']

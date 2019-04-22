from rest_framework import serializers
from app1.models import Product, ShoppingList, User, Color, Image


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductInBaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'manufacturer', 'type_connector']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class BasketSerializer(serializers.ModelSerializer):
    product = ProductInBaskSerializer()
    buyer = UserSerializer()

    class Meta:
        model = ShoppingList
        fields = '__all__'


class BasketAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = ['product', 'price', 'product_name']


class BasketDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ['id', 'buyer']


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


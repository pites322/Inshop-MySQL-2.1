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


class BasketSerializerAlt(serializers.ModelSerializer):
    product = ProductInBaskSerializer(read_only=True)
    buyer = UserSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    payed_or_not = serializers.BooleanField()

    class Meta:
        model = ShoppingList
        fields = '__all__'

    def create(self, validated_data):
        validated_data.update({'buyer': self.context['request'].user})
        buy = super(BasketSerializerAlt, self).create(validated_data)
        return buy
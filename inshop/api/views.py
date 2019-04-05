from rest_framework import viewsets
from api.serializers import ProductSerializer, BasketSerializer
from app1.models import Product, ShoppingList


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BasketViewSet(viewsets.ModelViewSet):
    serializer_class = BasketSerializer
    queryset = ShoppingList.objects.none()

    def get_queryset(self):
        return ShoppingList.objects.filter(buyer_id=self.request.user.pk)
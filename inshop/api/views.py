from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ProductSerializer, BasketSerializer, BasketAddSerializer
from app1.models import Product, ShoppingList


class ProductViewSet(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({"data": serializer.data})


class BasketViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        queryset = ShoppingList.objects.filter(buyer=request.user.id)
        serializer = BasketSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        add_to_basket = BasketAddSerializer(data=request.data)
        if add_to_basket.is_valid():
            add_to_basket.save(buyer=self.request.user.id, payed_or_not="No")
            return Response({"status": "Add to basket"})
        else:
            return Response({"status": "Error"})
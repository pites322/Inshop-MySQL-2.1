from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ProductSerializer, BasketSerializer, BasketAddSerializer, BasketDeleteSerializer,\
    PictureSerializer
from app1.models import Product, ShoppingList, Image


class ProductView(APIView):
    def get(self, request):
        if "prod" in dict(self.request.GET):
            id = self.request.GET.get("prod")
            queryset = Product.objects.filter(pk=id)
            serializer = ProductSerializer(queryset, many=True)
            img_query = Image.objects.filter(product_photo_connect_id=id)
            img_serializer = PictureSerializer(img_query, many=True)
            return Response({"data": serializer.data, 'img_data': img_serializer.data})
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response({"data": serializer.data})


class BasketView(APIView):
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

    def delete(self, request):
        del_from_basket = BasketDeleteSerializer(data=request.data)
        if self.request.user.id == del_from_basket.buyer:
            dell_pod = ShoppingList.objects.filter(id=del_from_basket.id)
            dell_pod.delite()
            return Response({"status": "Delete"})
        else:
            return Response({"status": "Not delete"})
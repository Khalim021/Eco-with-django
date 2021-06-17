from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from api.serializers import ProductModelSerializer
from products.models import ProductModel


class ProductListAPIView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()




from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SpGurantee,SpProduct,SpProductImage

from .serializers  import SpGuranteeSerializer,SpProductSerializer,SpProductImageSerializer


class SpGuranteeAPIView(generics.ListCreateAPIView):
    queryset = SpGurantee.objects.all()
    serializer_class = SpGuranteeSerializer

class SpProductAPIView(generics.ListCreateAPIView):
    queryset = SpProduct.objects.all()
    serializer_class = SpProductSerializer

class SpProductImageAPIView(generics.ListCreateAPIView):
    queryset = SpProductImage.objects.all()
    serializer_class = SpProductImageSerializer


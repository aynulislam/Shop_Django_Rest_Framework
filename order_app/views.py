from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SpOrder,SpOrderDetail

from .serializers  import SpOrderSerializer,SpOrderDetailSerializer


class SpOrderAPIView(generics.ListCreateAPIView):
    queryset = SpOrder.objects.all()
    serializer_class = SpOrderSerializer

class SpOrderDetailAPIView(generics.ListCreateAPIView):
    queryset = SpOrderDetail.objects.all()
    serializer_class = SpOrderDetailSerializer


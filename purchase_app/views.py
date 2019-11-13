from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import WbCard,SpPurchase
from .serializers  import WbCardSerializer,SpPurchaseSerializer

class WbCardAPIView(generics.ListCreateAPIView):
    queryset = WbCard.objects.all()
    serializer_class = WbCardSerializer

class SpPurchaseAPIView(generics.ListCreateAPIView):
    queryset = SpPurchase.objects.all()
    serializer_class = SpPurchaseSerializer
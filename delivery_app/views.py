from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SpDeliveryOn,SpDeliveryBoy

from .serializers  import SpDeliveryBoySerializer,SpDeliveryOnSerializer


class SpDeliveryOnAPIView(generics.ListCreateAPIView):
    queryset = SpDeliveryOn.objects.all()
    serializer_class = SpDeliveryOnSerializer

class SpDeliveryBoyAPIView(generics.ListCreateAPIView):
    queryset = SpDeliveryBoy.objects.all()
    serializer_class = SpDeliveryBoySerializer


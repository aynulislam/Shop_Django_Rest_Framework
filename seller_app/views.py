from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import ScUser,SpSeller,SpDivision
from .serializers  import ScUserSerializer,SpSellerSerializer,SpDivisionSerializer

class ScUserAPIView(generics.ListCreateAPIView):
    queryset = ScUser.objects.all()
    serializer_class = ScUserSerializer

class SpSellerAPIView(generics.ListCreateAPIView):
    queryset = SpSeller.objects.all()
    serializer_class = SpSellerSerializer

class SpDivisionAPIView(generics.ListCreateAPIView):
    queryset = SpDivision.objects.all()
    serializer_class = SpDivisionSerializer
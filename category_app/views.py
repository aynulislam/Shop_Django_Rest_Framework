from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SpCategory,SpSubCategory

from .serializers  import SpCategorySerializer,SpSubCategorySerializer


class SpCategoryAPIView(generics.ListCreateAPIView):
    queryset = SpCategory.objects.all()
    serializer_class = SpCategorySerializer

class SpSubCategoryAPIView(generics.ListCreateAPIView):
    queryset = SpSubCategory.objects.all()
    serializer_class = SpSubCategorySerializer


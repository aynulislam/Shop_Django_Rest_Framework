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

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Category Api Create

class SpCategoryDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpCategory.objects.get(pk=pk)
        except SpCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spcategory = self.get_object(pk)
        serializer = SpCategorySerializer(spcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spcategory = self.get_object(pk)
        serializer = SpCategorySerializer(spcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spcategory = self.get_object(pk)
        spcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpCategoryList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spcategory = SpCategory.objects.all()
        serializer = SpCategorySerializer(spcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Job Work Status Api create

class SpSubCategoryDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpSubCategory.objects.get(pk=pk)
        except SpSubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spsubcategory = self.get_object(pk)
        serializer = SpSubCategorySerializer(spsubcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spsubcategory = self.get_object(pk)
        serializer = SpSubCategorySerializer(spsubcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spsubcategory = self.get_object(pk)
        spsubcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpSubCategoryList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spsubcategory = SpSubCategory.objects.all()
        serializer = SpSubCategorySerializer(spsubcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpSubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Gurantee Api Create

class SpGuranteeDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpGurantee.objects.get(pk=pk)
        except SpGurantee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spgurantee = self.get_object(pk)
        serializer = SpGuranteeSerializer(spgurantee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spgurantee = self.get_object(pk)
        serializer = SpGuranteeSerializer(spgurantee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spgurantee = self.get_object(pk)
        spgurantee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpGuranteeList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spgurantee = SpGurantee.objects.all()
        serializer = SpGuranteeSerializer(spgurantee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpGuranteeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Product Api create

class SpProductDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpProduct.objects.get(pk=pk)
        except SpProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spproduct = self.get_object(pk)
        serializer = SpProductSerializer(spproduct)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spproduct = self.get_object(pk)
        serializer = SpProductSerializer(spproduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spproduct = self.get_object(pk)
        spproduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpProductList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spproduct = SpProduct.objects.all()
        serializer = SpProductSerializer(spproduct, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Product Image Api create

class SpProductImageDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpProductImage.objects.get(pk=pk)
        except SpProductImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spproductimage = self.get_object(pk)
        serializer = SpProductImageSerializer(spproductimage)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spproductimage = self.get_object(pk)
        serializer = SpProductImageSerializer(spproductimage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spproductimage = self.get_object(pk)
        spproductimage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpProductImageList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spproductimage = SpProductImage.objects.all()
        serializer = SpProductImageSerializer(spproductimage, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
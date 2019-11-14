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

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Gurantee Api Create

class ScUserDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return ScUser.objects.get(pk=pk)
        except ScUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        scuser = self.get_object(pk)
        serializer = ScUserSerializer(scuser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        scuser = self.get_object(pk)
        serializer = ScUserSerializer(scuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        scuser = self.get_object(pk)
        scuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScUserList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        scuser = ScUser.objects.all()
        serializer = ScUserSerializer(scuser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Seller Api create

class SpSellerDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpSeller.objects.get(pk=pk)
        except SpSeller.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spseller = self.get_object(pk)
        serializer = SpSellerSerializer(spseller)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spseller = self.get_object(pk)
        serializer = SpSellerSerializer(spseller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spseller = self.get_object(pk)
        spseller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpSellerList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spseller = SpSeller.objects.all()
        serializer = SpSellerSerializer(spseller, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpSellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpDivisionDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpDivision.objects.get(pk=pk)
        except SpDivision.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spdivision = self.get_object(pk)
        serializer = SpDivisionSerializer(spdivision)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spdivision = self.get_object(pk)
        serializer = SpDivisionSerializer(spdivision, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spdivision = self.get_object(pk)
        spdivision.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpDivisionList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spdivision = SpDivision.objects.all()
        serializer = SpDivisionSerializer(spdivision, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpDivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
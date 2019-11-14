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



from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Delivery Boy Api Create

class SpDeliveryBoyDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpDeliveryBoy.objects.get(pk=pk)
        except SpDeliveryBoy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spdeliveryboy = self.get_object(pk)
        serializer = SpDeliveryBoySerializer(spdeliveryboy)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spdeliveryboy = self.get_object(pk)
        serializer = SpDeliveryBoySerializer(spdeliveryboy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spdeliveryboy = self.get_object(pk)
        spdeliveryboy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpDeliveryBoyList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spdeliveryboy = SpDeliveryBoy.objects.all()
        serializer = SpDeliveryBoySerializer(spdeliveryboy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpDeliveryBoySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Delivery On Api create

class SpDeliveryOnDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpDeliveryOn.objects.get(pk=pk)
        except SpDeliveryOn.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spdeliveryon = self.get_object(pk)
        serializer = SpDeliveryOnSerializer(spdeliveryon)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spdeliveryon = self.get_object(pk)
        serializer = SpDeliveryOnSerializer(spdeliveryon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spdeliveryon = self.get_object(pk)
        spdeliveryon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpDeliveryOnList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spdeliveryon = SpDeliveryOn.objects.all()
        serializer = SpDeliveryOnSerializer(spdeliveryon, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpDeliveryOnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
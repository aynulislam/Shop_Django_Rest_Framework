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


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#WbCard Api Create

class WbCardDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return WbCard.objects.get(pk=pk)
        except WbCard.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        wbcard = self.get_object(pk)
        serializer = WbCardSerializer(wbcard)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        wbcard = self.get_object(pk)
        serializer = WbCardSerializer(wbcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wbcard = self.get_object(pk)
        wbcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WbCardList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        wbcard = WbCard.objects.all()
        serializer = WbCardSerializer(wbcard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WbCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Purchase Details Api create

class SpPurchaseDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpPurchaseDetail.objects.get(pk=pk)
        except SpPurchaseDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sppurchase = self.get_object(pk)
        serializer = SpPurchaseSerializer(sppurchase)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sppurchase = self.get_object(pk)
        serializer = SpPurchaseSerializer(sppurchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sppurchase = self.get_object(pk)
        sppurchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpPurchaseList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        sppurchase = SpPurchase.objects.all()
        serializer = SpPurchaseSerializer(sppurchase, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpPurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
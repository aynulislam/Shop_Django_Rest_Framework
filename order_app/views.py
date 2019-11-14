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


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Order Api Create

class SpOrderDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpOrder.objects.get(pk=pk)
        except SpOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sporder = self.get_object(pk)
        serializer = SpOrderSerializer(sporder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sporder = self.get_object(pk)
        serializer = SpOrderSerializer(sporder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sporder = self.get_object(pk)
        sporder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpOrderList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        sporder = SpOrder.objects.all()
        serializer = SpOrderSerializer(sporder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Order Details Api create

class SpOrderDetailDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpOrderDetail.objects.get(pk=pk)
        except SpOrderDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sporderdetail = self.get_object(pk)
        serializer = SpOrderDetailSerializer(sporderdetail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sporderdetail = self.get_object(pk)
        serializer = SpOrderDetailSerializer(sporderdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sporderdetail = self.get_object(pk)
        sporderdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpOrderDetailList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        sporderdetail = SpOrderDetail.objects.all()
        serializer = SpOrderDetailSerializer(sporderdetail, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpOrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import serializers
from .models import SpOrder,SpOrderDetail
class SpOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpOrder
        fields = "__all__"


class SpOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpOrderDetail
        fields = "__all__"
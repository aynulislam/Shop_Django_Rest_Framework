from rest_framework import serializers
from .models import WbCard,SpPurchase


class WbCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WbCard
        fields = "__all__"


class SpPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpPurchase
        fields = "__all__"



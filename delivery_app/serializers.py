from rest_framework import serializers
from .models import SpDeliveryOn,SpDeliveryBoy
class SpDeliveryOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpDeliveryOn
        fields = "__all__"


class SpDeliveryBoySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpDeliveryBoy
        fields = "__all__"
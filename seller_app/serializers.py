from rest_framework import serializers
from .models import ScUser,SpSeller,SpDivision


class ScUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScUser
        fields = "__all__"


class SpSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpSeller
        fields = "__all__"


class SpDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpDivision
        fields = "__all__"



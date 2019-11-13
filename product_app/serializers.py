from rest_framework import serializers
from .models import SpGurantee,SpProduct,SpProductImage
class SpGuranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpGurantee
        fields = "__all__"


class SpProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpProduct
        fields = "__all__"

class SpProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpProductImage
        fields = "__all__"
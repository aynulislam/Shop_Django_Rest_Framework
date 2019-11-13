from rest_framework import serializers
from .models import SpSubCategory,SpCategory
class SpCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpCategory
        fields = "__all__"


class SpSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpSubCategory
        fields = "__all__"
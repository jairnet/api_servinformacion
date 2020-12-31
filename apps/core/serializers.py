from rest_framework import serializers
from apps.core.models import GeoUser


class GeoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoUser
        fields = '__all__'

from django.shortcuts import render
from rest_framework import viewsets
from .models import GeoUser
from .serializers import GeoUserSerializer


class GeoUserViewset(viewsets.ModelViewSet):
    queryset = GeoUser.objects.all()
    serializer_class = GeoUserSerializer

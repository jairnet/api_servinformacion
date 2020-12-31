from rest_framework import generics
from rest_framework import viewsets
import requests
from .serializers import GeoUserSerializer
from .models import GeoUser


class GeoUserCreateApi(generics.CreateAPIView):
    queryset = GeoUser.objects.all()
    serializer_class = GeoUserSerializer


class GeoUserListApi(generics.ListAPIView):
    queryset = GeoUser.objects.all()
    serializer_class = GeoUserSerializer


class GeoUserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = GeoUser.objects.all()
    serializer_class = GeoUserSerializer


class GeoUserDeleteApi(generics.DestroyAPIView):
    queryset = GeoUser.objects.all()
    serializer_class = GeoUserSerializer


class GeoUserGeocodingApi(viewsets.ModelViewSet):
    queryset = GeoUser.objects.all()
    serializer_class = GeoUserSerializer

    def set_address(self, geo_user):
        API_KEY = 'AIzaSyB5X44haPT-0iBTM6JmjUVJ8Lehihp9u0I'
        city = geo_user.city.replace(" ", "+")
        address = geo_user.address.replace(" ", "+")
        end_point = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}+{address}&key={API_KEY}'

        response = requests.get(end_point)

        if response.status_code == 200:
            result = response.json()
            geo_user.latitude = 0.0 if result['status'] != 'OK' else result['results'][0]['geometry']['location'][
                'lat']
            geo_user.longitude = 0.0 if result['status'] != 'OK' else result['results'][0]['geometry']['location'][
                'lng']
            geo_user.geo_state = False if result['status'] != 'OK' else True
            geo_user.save()

    def get_queryset(self):
        users = GeoUser.objects.filter(longitude__isnull=True, latitude__isnull=True)
        for user in users:
            self.set_address(user)
        return users

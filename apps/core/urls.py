from django.urls import path, include
from apps.core.api import GeoUserCreateApi, GeoUserListApi, GeoUserUpdateApi, GeoUserDeleteApi, GeoUserGeocodingApi

urlpatterns = [
    path('create', GeoUserCreateApi.as_view()),
    path('list', GeoUserListApi.as_view()),
    path('update/<int:pk>', GeoUserUpdateApi.as_view()),
    path('<int:pk>/delete', GeoUserDeleteApi.as_view()),
    path('geocoding_base', GeoUserGeocodingApi.as_view({'get': 'list'})),
]

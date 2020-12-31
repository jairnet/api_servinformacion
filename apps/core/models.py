from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.

class GeoUser(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    address = models.CharField(max_length=100, verbose_name='Direccion')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    longitude = models.FloatField(null=True, verbose_name='Longitud')
    latitude = models.FloatField(null=True, verbose_name='Latitud')
    geo_state = models.BooleanField(default=False, null=True, verbose_name='Estadogeo')

    class Meta:
        verbose_name = 'GeoUsuario'
        verbose_name_plural = 'GeoUsuarios'
        ordering = ['-created']

    def __str__(self):
        return self.name





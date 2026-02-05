
from django.db import models
from apps.taxonomy.models import Taxon
from apps.collections.models import Event

class Specimen(models.Model):
    code = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100, blank=True)
    physical_location = models.CharField(max_length=255, blank=True)
    taxon = models.ForeignKey(Taxon, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.code

class Image(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='specimens/')
    caption = models.CharField(max_length=255, blank=True)

class QRCode(models.Model):
    specimen = models.OneToOneField(Specimen, on_delete=models.CASCADE, related_name='qr')
    png = models.ImageField(upload_to='qr/', blank=True, null=True)

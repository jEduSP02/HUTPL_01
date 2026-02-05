
from django.db import models
from apps.specimens.models import Specimen

class GeneticSample(models.Model):
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE, related_name='genetic_samples')
    sample_type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)

class Sequence(models.Model):
    genetic_sample = models.ForeignKey(GeneticSample, on_delete=models.CASCADE, related_name='sequences')
    marker = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='sequences/', blank=True, null=True)

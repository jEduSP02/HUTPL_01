
from django.db import models
from apps.specimens.models import Specimen

class Loan(models.Model):
    institution = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, blank=True)
    specimens = models.ManyToManyField(Specimen, related_name='loans', blank=True)

    def __str__(self):
        return f"{self.institution} ({self.start_date} - {self.end_date})"

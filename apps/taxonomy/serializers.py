
from rest_framework import serializers
from .models import Taxon

class TaxonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxon
        fields = '__all__'

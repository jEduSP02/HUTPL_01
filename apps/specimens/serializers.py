
from rest_framework import serializers
from .models import Specimen, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image','caption']

class SpecimenSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Specimen
        fields = ['id','code','status','physical_location','taxon','event','images']

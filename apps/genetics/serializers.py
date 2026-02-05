
from rest_framework import serializers
from .models import GeneticSample, Sequence

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = ['id','marker','file','genetic_sample']

class GeneticSampleSerializer(serializers.ModelSerializer):
    sequences = SequenceSerializer(many=True, read_only=True)
    class Meta:
        model = GeneticSample
        fields = ['id','specimen','sample_type','status','sequences']

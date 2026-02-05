
from rest_framework import viewsets, permissions
from .models import GeneticSample, Sequence
from .serializers import GeneticSampleSerializer, SequenceSerializer

class GeneticSampleViewSet(viewsets.ModelViewSet):
    queryset = GeneticSample.objects.all()
    serializer_class = GeneticSampleSerializer
    permission_classes = [permissions.IsAuthenticated]

class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer
    permission_classes = [permissions.IsAuthenticated]

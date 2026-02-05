
from rest_framework import viewsets, permissions, filters
from .models import Taxon
from .serializers import TaxonSerializer

class TaxonViewSet(viewsets.ModelViewSet):
    queryset = Taxon.objects.all().order_by('scientific_name')
    serializer_class = TaxonSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['scientific_name','family','order']

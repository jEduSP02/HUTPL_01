
from rest_framework import viewsets, permissions, decorators
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Specimen
from .serializers import SpecimenSerializer
import qrcode
from io import BytesIO

class SpecimenViewSet(viewsets.ModelViewSet):
    queryset = Specimen.objects.all().select_related('taxon','event')
    serializer_class = SpecimenSerializer
    permission_classes = [permissions.IsAuthenticated]

    @decorators.action(detail=True, methods=['get'], url_path='qr')
    def qr(self, request, pk=None):
        specimen = self.get_object()
        img = qrcode.make(specimen.code)
        buf = BytesIO()
        img.save(buf, format='PNG')
        return HttpResponse(buf.getvalue(), content_type='image/png')

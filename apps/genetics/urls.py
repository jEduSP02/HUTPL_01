
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneticSampleViewSet, SequenceViewSet

router = DefaultRouter()
router.register(r'samples', GeneticSampleViewSet, basename='genetic-sample')
router.register(r'sequences', SequenceViewSet, basename='sequence')

urlpatterns = [
    path('', include(router.urls)),
]

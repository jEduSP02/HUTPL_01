
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaxonViewSet

router = DefaultRouter()
router.register(r'', TaxonViewSet, basename='taxon')

urlpatterns = [
    path('', include(router.urls)),
]

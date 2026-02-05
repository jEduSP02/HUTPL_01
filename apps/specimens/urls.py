
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecimenViewSet

router = DefaultRouter()
router.register(r'', SpecimenViewSet, basename='specimen')

urlpatterns = [
    path('', include(router.urls)),
]

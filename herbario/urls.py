from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from apps.taxonomy.views import TaxonViewSet
from apps.collections.views import EventViewSet
from apps.specimens.views import SpecimenViewSet
from apps.genetics.views import GeneticSampleViewSet, SequenceViewSet
from apps.loans.views import LoanViewSet

router = DefaultRouter()
router.register(r"taxa", TaxonViewSet, basename="taxa")
router.register(r"events", EventViewSet, basename="events")
router.register(r"specimens", SpecimenViewSet, basename="specimens")
router.register(r"genetics/samples", GeneticSampleViewSet, basename="genetic-samples")
router.register(r"genetics/sequences", SequenceViewSet, basename="genetic-sequences")
router.register(r"loans", LoanViewSet, basename="loans")


def home(request):
    return render(request, 'inicio_01.html')

urlpatterns = [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path('admin/', admin.site.urls),
    #path('api/specimens/', include('apps.specimens.urls')),
    #path('api/taxa/', include('apps.taxonomy.urls')),
    #path('api/events/', include('apps.collections.urls')),
    #path('api/genetics/', include('apps.genetics.urls')),
    #path('api/loans/', include('apps.loans.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/', include(router.urls)),
    path('', home),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




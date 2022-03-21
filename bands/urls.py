from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bands.views import BandView

router = DefaultRouter()
router.register(r'bands', BandView)

urlpatterns = [
    path('', include(router.urls)),
]
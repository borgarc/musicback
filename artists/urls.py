from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artists.views import ArtistView

router = DefaultRouter()
router.register(r'artists', ArtistView)

urlpatterns = [
    path('', include(router.urls)),
]
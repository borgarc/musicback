from django.urls import path, include
from rest_framework.routers import DefaultRouter
from albums.views import AlbumView

router = DefaultRouter()
router.register(r'albums', AlbumView)

urlpatterns = [
    path('', include(router.urls)),
]
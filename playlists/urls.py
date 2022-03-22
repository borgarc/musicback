from django.urls import path, include
from rest_framework.routers import DefaultRouter
from playlists.views import PlaylistView

router = DefaultRouter()
router.register(r'playlists', PlaylistView)

urlpatterns = [
    path('', include(router.urls)),
]
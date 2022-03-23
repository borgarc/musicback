from django.urls import path, include
from rest_framework.routers import DefaultRouter
from songs.views import SongView, SongsOnAlbumView, SongsOnPlaylistView

router = DefaultRouter()
router.register(r'songs', SongView)
router.register(r'songs_on_album', SongsOnAlbumView)
router.register(r'songs_on_playlist', SongsOnPlaylistView)

urlpatterns = [
    path('', include(router.urls)),
]
from django.db import models
from django.conf import settings
from albums.models import Album
from playlists.models import Playlist

# Create your models here.
class Song(models.Model):
    song_file = models.FileField(upload_to=settings.MEDIA_ROOT)
    song_title = models.CharField(max_length=100)
    song_duration = models.CharField(max_length= 10)

    songs_on_playlist = models.ManyToManyField(
        Playlist,
        through="SongsOnPlaylist",
        related_name="songs_on_playlist"
    )
    songs_on_album = models.ManyToManyField(
        Album,
        through="SongsOnAlbum",
        related_name="songs_on_album"
    )


class SongsOnPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, related_name="songs", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="playlist", on_delete=models.CASCADE)

class SongsOnAlbum(models.Model):
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="album", on_delete=models.CASCADE)

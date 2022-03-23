from rest_framework import serializers
from albums.models import Album
from songs.serializers import SongSerializer

class AlbumSerializer(serializers.ModelSerializer):
    songs_on_album = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'album_release_date', 'album_band', 'songs_on_album']
        
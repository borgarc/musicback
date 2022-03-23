from rest_framework import serializers
from songs.models import Song, SongsOnAlbum, SongsOnPlaylist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields= ['id', 'song_file', 'song_title', 'song_duration']

class SongsOnAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsOnAlbum
        fields = ['id', 'album', 'song']

class SongsOnPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsOnPlaylist
        fields = ['id', 'playlist', 'song']
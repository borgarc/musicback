from rest_framework import serializers
from playlists.models import Playlist
from songs.serializers import SongSerializer

class PlaylistSerializer(serializers.ModelSerializer):
    full_user_name = serializers.SerializerMethodField()
    songs_on_playlist = SongSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ['id', 'playlist_name', 'user', 'full_user_name', 'songs_on_playlist']

    def get_full_user_name(self, playlist):
        return '%s %s' % (playlist.user.first_name, playlist.user.last_name)
        
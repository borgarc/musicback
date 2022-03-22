from rest_framework import serializers
from playlists.models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
    full_user_name = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ['id', 'playlist_name', 'user', 'full_user_name']

    def get_full_user_name(self, playlist):
        return '%s %s' % (playlist.user.first_name, playlist.user.last_name)
        
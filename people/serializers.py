from rest_framework import serializers
from django.contrib.auth.models import User
from playlists.serializers import PlaylistSerializer

class PersonSerializer(serializers.ModelSerializer):
    playlists = PlaylistSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'playlists']
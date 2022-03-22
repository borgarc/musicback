from django.shortcuts import render
from rest_framework import viewsets
from playlists.models import Playlist
from playlists.serializers import PlaylistSerializer

# Create your views here.
class PlaylistView(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    

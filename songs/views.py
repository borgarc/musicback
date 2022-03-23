from django.shortcuts import render
from rest_framework import viewsets
from songs.models import Song, SongsOnAlbum, SongsOnPlaylist
from songs.serializers import SongSerializer, SongsOnAlbumSerializer, SongsOnPlaylistSerializer

# Create your views here.
class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongsOnAlbumView(viewsets.ModelViewSet):
    queryset = SongsOnAlbum.objects.all()
    serializer_class = SongsOnAlbumSerializer

class SongsOnPlaylistView(viewsets.ModelViewSet):
    queryset = SongsOnPlaylist.objects.all()
    serializer_class = SongsOnPlaylistSerializer
    

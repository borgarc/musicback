from django.shortcuts import render
from rest_framework import viewsets
from albums.models import Album
from albums.serializers import AlbumSerializer

# Create your views here.
class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    

from django.shortcuts import render
from rest_framework import viewsets
from artists.models import Artist
from artists.serializers import ArtistSerializer

# Create your views here.
class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    

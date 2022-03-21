from django.shortcuts import render
from rest_framework import viewsets
from bands.models import Band
from bands.serializers import BandSerializer

# Create your views here.
class BandView(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    

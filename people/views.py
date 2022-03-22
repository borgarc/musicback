from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from people.serializers import PersonSerializer

# Create your views here.
class PersonView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PersonSerializer
    

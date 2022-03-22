from django.db import models
from bands.models import Band

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=20)
    artist_last_name = models.CharField(max_length=30, blank=True, null=True)
    artist_age = models.IntegerField()
    artist_nick = models.CharField(max_length=30, blank=True, null=True)

    artist_band = models.ForeignKey(Band, related_name="artists", on_delete=models.CASCADE)

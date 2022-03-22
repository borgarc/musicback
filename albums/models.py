from django.db import models
from bands.models import Band

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_release_date = models.IntegerField()

    album_band = models.ForeignKey(Band, related_name="albums", on_delete=models.CASCADE)

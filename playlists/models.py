from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    playlist_name = models.CharField(max_length=40)

    user = models.OneToOneField(User, related_name="playlists", on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Band(models.Model):
    band_name = models.CharField(max_length=100)
    creation_date = models.IntegerField()

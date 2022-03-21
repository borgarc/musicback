from rest_framework import serializers
from bands.models import Band

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'band_name', 'creation_date']

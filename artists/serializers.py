from rest_framework import serializers
from artists.models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    band = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ['id', 'artist_name', 'artist_last_name', 'artist_age', 'artist_band', 'band']
    
    def get_band(self, artist):
        return '%s' % artist.artist_band.band_name

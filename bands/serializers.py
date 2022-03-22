from rest_framework import serializers
from bands.models import Band
from albums.serializers import AlbumSerializer
from artists.serializers import ArtistSerializer

class BandSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Band
        fields = ['id', 'band_name', 'creation_date', 'artists', 'albums']

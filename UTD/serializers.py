from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from models import Song, Album, Artist


class SongSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='UTD:song-detail'
    )

    album = HyperlinkedRelatedField(view_name='UTD:album-detail', read_only=True)

    class Meta:
        model = Song
        fields = (
            'url',
            'name',
            'album',
        )


class AlbumSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='UTD:album-detail'
    )

    song_set = HyperlinkedRelatedField(many=True, view_name='UTD:song-detail', read_only=True)

    artist = HyperlinkedRelatedField(view_name='UTD:artist-detail', read_only=True)

    class Meta:
        model = Album
        fields = (
            'url',
            'name',
            'release_date',
            'song_set',
            'artist',
        )


class ArtistSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='UTD:artist-detail'
    )

    album_set = HyperlinkedRelatedField(many=True, view_name='UTD:album-detail', read_only=True)

    related = HyperlinkedRelatedField(many=True, view_name='UTD:artist-detail', read_only=True)

    class Meta:
        model = Artist
        fields = (
            'url',
            'name',
            'album_set',
            'related',
        )
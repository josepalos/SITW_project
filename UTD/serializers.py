from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from models import Song, Album


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

    # artist

    class Meta:
        model = Album
        fields = (
            'url',
            'name',
            'release_date',
            'song_set',
            # 'artist',
        )

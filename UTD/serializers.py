from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from models import Song


class SongSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='UTD:song-detail'
    )

    # album = HyperlinkedRelatedField(view_name='utd:album-detail', read_only=True)

    class Meta:
        model = Song
        fields = (
            'url',
            'name',
            # 'album',
        )

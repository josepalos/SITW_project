from django.conf.urls import url, patterns, include
from UTD.views import ArtistList, ArtistDetails, AlbumList, AlbumDetails, SongList, SongDetails, RelatedArtistList
from UTD.views import APISongDetail, APIAlbumDetail, APIArtistDetail


urlpatterns = [
    url(r'^artists(?P<format>(\.json|\.xml|\.html)?)/$', ArtistList.as_view()),
    url(r'^artists/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', ArtistDetails.as_view()),
    url(r'^artists/(?P<pk>\d+)/albums(?P<format>(\.json|\.xml|\.html)?)/$', AlbumList.as_view()),

    url(r'^albums/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', AlbumDetails.as_view()),
    url(r'^albums/(?P<pk>\d+)/songs(?P<format>(\.json|\.xml|\.html)?)/$', SongList.as_view()),

    url(r'^songs/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', SongDetails.as_view()),
]


# REST API patterns
urlpatterns += patterns(
    '',
    # url(r'^api/artists/$'),
    url(r'^api/artists/(?P<pk>\d+)/$', APIArtistDetail.as_view(), name='artist-detail'),
    # url(r'^api/albums/$'),
    url(r'^api/albums/(?P<pk>\d+)/$', APIAlbumDetail.as_view(), name='album-detail'),
    # url(r'^api/songs/$'),
    url(r'^api/songs/(?P<pk>\d+)/$', APISongDetail.as_view(), name='song-detail'),
)
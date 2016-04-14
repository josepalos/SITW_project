from django.conf.urls import url
from UTD.views import ArtistList, ArtistDetails, AlbumList, AlbumDetails, SongList, SongDetails


urlpatterns = [
    url(r'^artists(?P<format>(\.json|\.xml|\.html)?)/$', ArtistList.as_view()),
    url(r'^artists/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', ArtistDetails.as_view()),
    url(r'^artists/(?P<pk>\d+)/albums(?P<format>(\.json|\.xml|\.html)?)/$', AlbumList.as_view()),

    url(r'^albums/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', AlbumDetails.as_view()),
    url(r'^albums/(?P<pk>\d+)/songs(?P<format>(\.json|\.xml|\.html)?)/$', SongList.as_view()),

    url(r'^songs/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', SongDetails.as_view()),
]
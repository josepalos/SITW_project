from django.conf.urls import url
from UTD.views import ArtistList, ArtistDetails, AlbumList, AlbumDetails, SongList, SongDetails


urlpatterns = [
    url(r'^artists/$', ArtistList.as_view()),
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetails.as_view()),
    url(r'^artists/(?P<pk>\d+)/albums/$', AlbumList.as_view()),

    url(r'^albums/(?P<pk>\d+)/$', AlbumDetails.as_view()),
    url(r'^albums/(?P<pk>\d+)/songs/$', SongList.as_view()),

    url(r'^songs/(?P<pk>\d+)/$', SongDetails.as_view()),
]
from django.conf.urls import url
from UTD.views import album_details
from UTD.views import ArtistList, ArtistDetails, AlbumList


urlpatterns = [
    url(r'^artists/$', ArtistList.as_view()),
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetails.as_view()),
    url(r'^artists/(?P<artist_id>\d)/albums/$', AlbumList.as_view()),
    url(r'^artists/(\d)/albums/(\d)/$', album_details),
]
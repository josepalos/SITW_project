from django.conf.urls import url
from UTD.views import list_artists, list_albums, artist_details, album_details
from UTD.views import ArtistList



urlpatterns = [
    url(r'^artists/$', ArtistList.as_view()),
    url(r'^artists/(\d)/albums/$', list_albums),
    url(r'^artists/(\d)$/', artist_details),
    url(r'^artists/(\d)/albums/(\d)/$', album_details),
]
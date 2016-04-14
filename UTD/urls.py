from django.conf.urls import url
from UTD.views import list_artists, list_albums, artist_details, list_songs, song_details, album_details


urlpatterns = [
    url(r'^artists/$', list_artists),
    url(r'^artists/(\d+)/', artist_details),
    url(r'^artists/(\d+)/albums/$', list_albums),

    url(r'^albums/(\d+)/$', album_details),
    url(r'^albums/(\d+)/songs/$', list_songs),
    # url(r'^songs/', list_songs),
    url(r'^songs/(\d+)/$', song_details),
]
from django.conf.urls import url
<<<<<<< HEAD
from UTD.views import list_artists, list_albums, artist_details, album_details
=======
from UTD.views import list_artists, list_albums, artist_details, list_songs, song_details
>>>>>>> iss-1



urlpatterns = [
    url(r'^artists/$', list_artists),
    url(r'^artists/(\d)/albums/$', list_albums),
    url(r'^artists/(\d)/$', artist_details),
    url(r'^album/(\d)/$', list_songs),
    url(r'^song/(\d)/$', song_details),
]
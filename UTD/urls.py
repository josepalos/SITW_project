from django.conf.urls import url
from UTD.views import list_albums, album_details
from UTD.views import ArtistList, ArtistDetails


urlpatterns = [
    url(r'^artists/$', ArtistList.as_view()),
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetails.as_view()),
    url(r'^artists/(\d)/albums/$', list_albums),
    url(r'^artists/(\d)/albums/(\d)/$', album_details),
]
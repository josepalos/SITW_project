from django.conf.urls import url
from UTD.views import list_artists, list_albums



urlpatterns = [
    url(r'^artists/$', list_artists),
    url(r'^artists/(\d)/albums/$', list_albums),
]
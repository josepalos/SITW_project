from django.conf.urls import url
from UTD.views import list_artists



urlpatterns = [
    url(r'^artists/$', list_artists)
]
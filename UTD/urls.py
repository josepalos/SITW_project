from django.conf.urls import url
from UTD.views import ArtistList, ArtistDetails, AlbumList, AlbumDetails, SongList, SongDetails, RelatedArtistList, Providers, FollowedArtists, follow_artist, unfollow_artist


urlpatterns = [
    url(r'^artists(?P<format>(\.json|\.xml|\.html)?)/$', ArtistList.as_view()),
    url(r'^artists/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', ArtistDetails.as_view()),
    url(r'^artists/(?P<pk>\d+)/albums(?P<format>(\.json|\.xml|\.html)?)/$', AlbumList.as_view()),
    url(r'^artists/(?P<pk>\d+)/follow$', follow_artist, name="artist_follow"),
    url(r'^artists/(?P<pk>\d+)/unfollow$', unfollow_artist, name="artist_unfollow"),

    url(r'^albums/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', AlbumDetails.as_view()),
    url(r'^albums/(?P<pk>\d+)/songs(?P<format>(\.json|\.xml|\.html)?)/$', SongList.as_view()),

    url(r'^songs/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', SongDetails.as_view()),
    url(r'^albums/(?P<pk>\d+)/providers(?P<format>(\.json|\.xml|\.html)?)/$', Providers.as_view()),
    #url(r'^user/(?P<pk>\d+)/providers(?P<format>(\.json|\.xml|\.html)?)/$', ),
    url(r'^user/(?P<username>.+)/following(?P<format>(\.json|\.xml|\.html)?)/$', FollowedArtists.as_view()),
]
from django.conf.urls import url
from UTD.views import ArtistList, ArtistDetails, AlbumList, AlbumDetails, SongList, SongDetails, RelatedArtistList,\
    Providers, FollowedArtists, DisplayPlaylist, ProfileView, follow_artist, unfollow_artist, index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^artists(?P<format>(\.json|\.xml|\.html)?)/$', ArtistList.as_view(), name='artist_list'),
    url(r'^artists/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', ArtistDetails.as_view(), name='artist_detail'),
    url(r'^artists/(?P<pk>\d+)/albums(?P<format>(\.json|\.xml|\.html)?)/$', AlbumList.as_view(), name='artist_albums'),
    url(r'^artists/(?P<pk>\d+)/follow$', follow_artist, name="artist_follow"),
    url(r'^artists/(?P<pk>\d+)/unfollow$', unfollow_artist, name="artist_unfollow"),

    url(r'^albums/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', AlbumDetails.as_view(), name='album_detail'),
    url(r'^albums/(?P<pk>\d+)/songs(?P<format>(\.json|\.xml|\.html)?)/$', SongList.as_view(), name='album_songs'),
    url(r'^albums/(?P<pk>\d+)/providers(?P<format>(\.json|\.xml|\.html)?)/$', Providers.as_view(),
        name='album_providers'),

    url(r'^songs/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$', SongDetails.as_view(), name='song_detail'),

    # url(r'^user/(?P<pk>\d+)/providers(?P<format>(\.json|\.xml|\.html)?)/$', ),
    url(r'^user/(?P<username>.+)(?P<format>(\.json|\.xml|\.html)?)/$', ProfileView.as_view(), name='profile'),
    url(r'^user/(?P<username>.+)/following(?P<format>(\.json|\.xml|\.html)?)/$', FollowedArtists.as_view(),
        name='followed_artists'),
    url(r'^user/(?P<username>.+)/playlist(?P<format>(\.json|\.xml|\.html)?)/$', DisplayPlaylist.as_view()),
]
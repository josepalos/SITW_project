from django.conf.urls import url, patterns

from UTD.views import APISongDetail, APIAlbumDetail, APIArtistDetail, APIArtistList, APIUserDetail, APIUserList, \
    APIPlaylistDetail, APIProviderDetail, ProvidersCreate, ProvidersDelete
from UTD.views import ArtistList, ArtistDetails, AlbumList, AlbumDetails, SongList, SongDetails, ArtistCreate, \
    Providers, FollowedArtists, DisplayPlaylist, ProfileView, follow_artist, unfollow_artist, index, Playlists, \
    PlaylistCreate, PlaylistEdit, PlaylistDelete


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^artists/$', ArtistList.as_view(), name='artist_list'),
    url(r'^artists/(?P<pk>\d+)/$', ArtistDetails.as_view(), name='artist_detail'),
    url(r'^artists/(?P<pk>\d+)/albums/$', AlbumList.as_view(), name='artist_albums'),
    url(r'^artists/(?P<pk>\d+)/follow$', follow_artist, name="artist_follow"),
    url(r'^artists/(?P<pk>\d+)/unfollow$', unfollow_artist, name="artist_unfollow"),
    url(r'^artists/create', ArtistCreate.as_view(), name="artist_create"),

    url(r'^albums/(?P<pk>\d+)/$', AlbumDetails.as_view(), name='album_detail'),
    url(r'^albums/(?P<pk>\d+)/songs/$', SongList.as_view(), name='album_songs'),
    url(r'^albums/(?P<pk>\d+)/providers/$', Providers.as_view(),
        name='album_providers'),
    url(r'^albums/(?P<pk>\d+)/providers/create', ProvidersCreate.as_view(), name='provider_create'),
    url(r'^songs/(?P<pk>\d+)/$', SongDetails.as_view(), name='song_detail'),

    url(r'^providers/(?P<pk>\d+)/delete', ProvidersDelete.as_view(), name='provider_delete'),

    # url(r'^user/(?P<pk>\d+)/providers/$', ),
    url(r'^user/(?P<username>[^/]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^user/(?P<username>[^/]+)/following/$', FollowedArtists.as_view(),
        name='followed_artists'),
    url(r'^user/(?P<username>[^/]+)/playlists/$', Playlists.as_view(), name='playlist_details'),
    url(r'^user/(?P<username>[^/]+)/playlists/(?P<pk>\d+)/$', DisplayPlaylist.as_view(), name='playlist_songs'),
    url(r'^user/(?P<username>[^/]+)/playlists/create/$', PlaylistCreate.as_view(), name= 'create_playlist'),
    url(r'^user/(?P<username>[^/]+)/playlists/(?P<pk>\d+)/modify/$', PlaylistEdit.as_view(), name= 'edit_playlist'),
    url(r'^user/(?P<username>[^/]+)/playlists/(?P<pk>\d+)/delete/$', PlaylistDelete.as_view(), name= 'delete_playlist'),
    #url(r'^user/(?P<username>[^/]+)/playlist/$', DisplayPlaylist.as_view()),
]


# REST API patterns
urlpatterns += patterns(
    'UTD.views',
    url(r'^api/$', 'api_root'),
    url(r'^api/artists/$', APIArtistList.as_view(), name='artist-list'),
    url(r'^api/artists/(?P<pk>\d+)/$', APIArtistDetail.as_view(), name='artist-detail'),

    # url(r'^api/albums/$'),
    url(r'^api/albums/(?P<pk>\d+)/$', APIAlbumDetail.as_view(), name='album-detail'),

    # url(r'^api/songs/$'),
    url(r'^api/songs/(?P<pk>\d+)/$', APISongDetail.as_view(), name='song-detail'),

    url(r'^api/users/$', APIUserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<username>.+)/$', APIUserDetail.as_view(), name='user-detail'),

    url(r'^api/playlists/(?P<pk>\d+)/$', APIPlaylistDetail.as_view(), name='playlist-detail'),

    url(r'^api/providers/(?P<pk>\d+)/$', APIProviderDetail.as_view(), name='provider-detail')
)

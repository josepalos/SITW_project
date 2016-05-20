from UTD.forms import ProviderForm, PlaylistForm
from models import Artist, Album, Song, Provider, Playlist, UserProfile
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request, 'index.html')

# REST API IMPORTS
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from serializers import SongSerializer, AlbumSerializer, ArtistSerializer, UserSerializer, PlaylistSerializer, \
    ProviderSerializer


class FormatResponseMixin(TemplateResponseMixin):

    def render_to_json_response(self, objects, **kwargs):
        return HttpResponse(serializers.serialize('json', objects, **kwargs), content_type='application/json')

    def render_to_xml_response(self, objects, **kwargs):
        return HttpResponse(serializers.serialize('xml', objects, **kwargs), content_type='application/xml')

    def render_to_response(self, context, **kwargs):
        # Look for a 'format=json' GET argument
        if 'format' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list

            if self.kwargs['format'] == '.json':
                return self.render_to_json_response(objects=objects)
            elif self.kwargs['format'] == '.xml':
                return self.render_to_xml_response(objects=objects)
        return super(FormatResponseMixin, self).render_to_response(context)


class ArtistList(ListView, FormatResponseMixin):
    model = Artist
    template_name = 'artistslist.html'
    context_object_name = 'artists_list'  # the name of the object_list used in the template.

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Artists list'
        context['pagetitle'] = 'Artists list'
        return context


class ArtistDetails(DetailView, FormatResponseMixin):
    model = Artist
    template_name = 'artist.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetails, self).get_context_data(**kwargs)
        context['titlehead'] = 'Artist'
        context['pagetitle'] = self.object.name

        try:
            last_album = Album.objects.filter(artist=self.object).order_by('release_date')[0]
        except IndexError:
            last_album = None
        context['album'] = last_album
        return context


class AlbumList(ListView, FormatResponseMixin):
    template_name = 'albumslist.html'
    context_object_name = 'albums_list'  # the name of the object_list used in the template.

    def get_queryset(self):
        self.artist = get_object_or_404(Artist, pk=self.kwargs['pk'])
        return Album.objects.filter(artist=self.artist)

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Albums list'
        context['pagetitle'] = 'Albums list'
        context['artist'] = self.artist
        return context


class AlbumDetails(DetailView, FormatResponseMixin):
    model = Album
    template_name = 'album.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetails, self).get_context_data(**kwargs)
        context['titlehead'] = 'Album %s' % self.object.name
        context['pagetitle'] = 'Album %s' % self.object.name
        return context


class SongList(ListView, FormatResponseMixin):
    template_name = 'songslist.html'
    context_object_name = 'songs_list'

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return Song.objects.filter(album=self.album)

    def get_context_data(self, **kwargs):
        context = super(SongList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Songs list'
        context['pagetitle'] = 'Songs list'
        context['album'] = self.album
        return context


class SongDetails(DetailView, FormatResponseMixin):
    model = Song
    template_name = 'song.html'

    def get_context_data(self, **kwargs):
        context = super(SongDetails, self).get_context_data(**kwargs)
        context['titlehead'] = 'Song %s' % self.object.name
        context['pagetitle'] = 'Song %s' % self.object.name
        return context


class RelatedArtistList(ListView, FormatResponseMixin):
    template_name = 'related_artist_list.html'
    context_object_name = 'artist_list'

    def get_queryset(self):
        self.principal_artist = get_object_or_404(Artist, pk=self.kwargs['pk'])
        return self.principal_artist.related.all()

    def get_context_data(self, **kwargs):
        context = super(RelatedArtistList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Related artists'
        context['pagetitle'] = 'Related artists'
        return context


class Providers(ListView, FormatResponseMixin):
    template_name = 'album_provider.html'
    context_object_name = 'provider_list'

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return Provider.objects.filter(album=self.album)

    def get_context_data(self, **kwargs):
        context = super(Providers, self).get_context_data(**kwargs)
        context['titlehead'] = self.album.name
        context['pagetitle'] = self.album.name
        context['album'] = self.album
        return context

class Playlists(ListView, FormatResponseMixin):
    template_name = 'playlist_list.html'
    context_object_name = 'playlist_list'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Playlist.objects.filter(user = self.user)

    def get_context_data(self, **kwargs):
        context = super(Playlists, self).get_context_data(**kwargs)
        context['titlehead'] = 'Playlists'
        context['pagetitle'] = 'Playlists'
        return context

class ProvidersCreate(CreateView):
    model = Provider
    template_name = 'form.html'
    form_class = ProviderForm

    def form_valid(self, form):
        form.instance.album = Album.objects.get(id=self.kwargs['pk'])
        return super(ProvidersCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('UTD:album_providers', kwargs={'pk': self.kwargs['pk'], 'format': ''})

class PlaylistCreate(CreateView):
    model = Playlist
    template_name = 'form.html'
    form_class = PlaylistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlaylistCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('UTD:playlist_details', kwargs={'username': self.kwargs['username'], 'format': ''})


class FollowedArtists(ListView, FormatResponseMixin):
    template_name = 'followed_artists.html'
    context_object_name = 'followed_artists'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return self.user.userprofile.followed_artist.all()

    def get_context_data(self, **kwargs):
        context = super(FollowedArtists, self).get_context_data(**kwargs)
        context['titlehead'] = 'Followed artists'
        context['pagetitle'] = 'Followed artists by: %s' % self.user
        return context


class DisplayPlaylist(ListView, FormatResponseMixin):
    template_name = 'display_playlist.html'
    context_object_name = 'song_list'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        self.playlist_name = get_object_or_404(Playlist, name=self.kwargs['playlist'])
        play = get_object_or_404(Playlist, user=self.user, name=self.kwargs['playlist'])
        return play.songs.all()

    def get_context_data(self, **kwargs):
        context = super(DisplayPlaylist, self).get_context_data(**kwargs)
        context['titlehead'] = 'Playlist'
        context['pagetitle'] = 'Playlist'
        return context

class PlaylistEdit(UpdateView):
    model = Playlist
    template_name = 'form.html'
    fields = ['name', 'songs']

    def get_success_url(self, **kwargs):
        return reverse_lazy('UTD:playlist_details', kwargs={'username': self.kwargs['username'], 'format': ''})

    def get_object(self, queryset=None):
        instance = Playlist.objects.get(name=self.kwargs.get('playlist', ''))
        return instance

class ProfileView(ListView, FormatResponseMixin):
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_queryset(self):
        self.user = get_object_or_404(User, username = self.kwargs['username'])
        return self.user

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['titlehead'] = self.user.username
        context['pagetitle'] = self.user.username
        return context


@login_required
def follow_artist(request, pk):
    user_following = request.user.userprofile
    artist = Artist.objects.get(pk=pk)

    user_following.followed_artist.add(artist)

    return HttpResponse("Followed.")


@login_required
def unfollow_artist(request, pk):
    user_following = request.user.userprofile
    artist = Artist.objects.get(pk=pk)

    user_following.followed_artist.remove(artist)

    return HttpResponse("Unfollowed.")


# REST views
@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'artists': reverse('UTD:artist-list', request=request),
        'users': reverse('UTD:user-list', request=request)
    })


class APISongDetail(generics.RetrieveAPIView):
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class APIAlbumDetail(generics.RetrieveAPIView):
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class APIArtistDetail(generics.RetrieveAPIView):
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APIArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class APIUserDetail(generics.RetrieveAPIView):
    model = User
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class APIUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class APIPlaylistDetail(generics.RetrieveAPIView):
    model = Playlist
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class APIProviderDetail(generics.RetrieveAPIView):
    model = Provider
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

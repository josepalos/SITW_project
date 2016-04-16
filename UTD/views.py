from models import Artist, Album, Song, Provider, UserArtistsList
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


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
            last_album = 'No albums found.'
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
        return context


class SongDetails(DetailView, FormatResponseMixin):
    model = Song
    template_name = 'songslist.html'

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
        return context


class FollowedArtists(ListView, FormatResponseMixin):
    template_name = 'followed_artists.html'
    context_object_name = 'followed_artists'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return UserArtistsList.objects.get(user=self.user).followed_artist.all()

    def get_context_data(self, **kwargs):
        context = super(FollowedArtists, self).get_context_data(**kwargs)
        context['titlehead'] = 'Followed artists'
        context['pagetitle'] = 'Followed artists by: %s' % self.user
        return context


@login_required
def follow_artist(request, pk):
    user_following = UserArtistsList.objects.get(user=request.user)
    artist = Artist.objects.get(pk=pk)

    user_following.followed_artist.add(artist)

    return HttpResponse("Followed.")


@login_required
def unfollow_artist(request, pk):
    user_following = UserArtistsList.objects.get(user=request.user)
    artist = Artist.objects.get(pk=pk)

    user_following.followed_artist.remove(artist)

    return HttpResponse("Unfollowed.")
from models import Artist, Album, Song
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class ArtistList(ListView):
    model = Artist
    template_name = 'artistslist.html'
    context_object_name = 'artists_list'  # the name of the object_list used in the template.

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Artists list'
        context['pagetitle'] = 'Artists list'
        return context


class ArtistDetails(DetailView):
    model = Artist
    template_name = 'artist.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetails, self).get_context_data(**kwargs)
        context['titlehead'] = 'Artist'
        context['pagetitle'] = self.object.name
        context['album'] = Album.objects.filter(artist=self.object).order_by('release_date')[0]
        return context


class AlbumList(ListView):
    template_name = 'albumslist.html'
    context_object_name = 'albums_list'  # the name of the object_list used in the template.

    def get_queryset(self):
        self.artist = get_object_or_404(Artist, pk=self.kwargs['pk'])
        return Album.objects.filter(artist=self.artist)

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Albums list'
        context['pagetitle'] = 'Albums list'
        return context


class AlbumDetails(DetailView):
    model = Album
    template_name = 'album.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetails, self).get_context_data(**kwargs)
        context['titlehead'] = 'Album %s' % self.object.name
        context['pagetitle'] = 'Album %s' % self.object.name
        return context


class SongList(ListView):
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


class SongDetails(DetailView):
    model = Song
    template_name = 'songslist.html'

    def get_context_data(self, **kwargs):
        context = super(SongDetails, self).get_context_data(**kwargs)
        context['titlehead'] = 'Song %s' % self.object.name
        context['pagetitle'] = 'Song %s' % self.object.name
        return context

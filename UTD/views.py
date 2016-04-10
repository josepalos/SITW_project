from django.shortcuts import render
from models import Artist, Album
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
        self.artist = get_object_or_404(Artist, pk=self.kwargs['artist_id'])
        return Album.objects.filter(artist=self.artist)

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Albums list'
        context['pagetitle'] = 'Albums list'
        return context


def album_details(request, artist_id, album_id):
    album = Album.objects.get(pk=album_id)

    return render(
        request,
        'album.html',
        {
            'titlehead': 'Album %s' % album.name,
            'pagetitle': 'Album %s' % album.name,
            'album': album,
        }
    )


def list_songs(request, album_id):
    pass


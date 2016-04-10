from django.shortcuts import render
from models import Artist, Album
from django.views.generic import ListView


class ArtistList(ListView):
    model = Artist
    template_name = 'artistslist.html'
    context_object_name = 'artists_list'  # the name of the object_list used in the template.

    def get_context_data(self, **kwargs):
        context = super(ArtistList, self).get_context_data(**kwargs)
        context['titlehead'] = 'Artists list'
        context['pagetitle'] = 'Artists list'
        return context


def list_albums(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    albums = Album.objects.filter(artist_id=artist_id)
    return render(
        request,
        'albumslist.html',
        {
            'titlehead': 'Albums list',
            'pagetitle': 'Albums from: %s' % artist.name,
            'albums_list': albums
        }
    )


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


def list_artists(request):
    artists = Artist.objects.all()
    return render(
        request,
        'artistslist.html',
        {
            'titlehead': 'Artists list',
            'pagetitle': 'Artists list',
            'artists_list': artists
        }
    )


def artist_details(request, artist_id):
    artist = Artist.objects.get(pk = artist_id)
    return render(
        request,
        'artist.html',
        {
            'titlehead': 'Artist',
            'pagetitle': artist.name,
            'artist': artist,
            'album': Album.objects.filter(artist=artist).order_by('release_date')[0]
        }
    )


def list_songs(request, album_id):
    pass


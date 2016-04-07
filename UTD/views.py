from django.shortcuts import render
from models import Artist, Album
from django.http import HttpResponse
import datetime
import json


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


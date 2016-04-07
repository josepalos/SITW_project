from django.shortcuts import render
from models import Artist
from models import Album
from django.http import HttpResponse
import json

def list_albums(request, artist_id):
    pass

def list_artists(request):
    artists = Artist.objects.all()
    return render(
        request,
        'artistslist.html',
        {
            'titlehead': 'Artists list',
            'pagetitle': 'Artists list',
            'artists_list': artists
        })

def list_songs(request, album_id):
    pass


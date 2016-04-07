from django.shortcuts import render
from models import Artist
from models import Album
from django.http import HttpResponse
import json

def list_albums(request, artist_id):
    pass

def list_artists(request):
    artists = Artist.objects.all()
    artistsjson = []
    for a in artists:
        artist = dict()
        artist['name'] = a.name
        artistsjson.append(artist)
    return HttpResponse(json.dumps(artistsjson))

def list_songs(request, album_id):
    pass


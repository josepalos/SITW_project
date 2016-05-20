import requests
import json
from datetime import datetime
import models
import thread

baseurl = "https://api.spotify.com/"


def get_albums_for_artist(artist_id):
    url = baseurl+'v1/artists/'+artist_id+'/albums?album_type=album'
    r = requests.get(url)

    return json.loads(r.text)


def get_album(url):
    r = requests.get(url)
    return json.loads(r.text)


def get_songs_for_album(album_id):
    url = baseurl+'v1/albums/'+album_id+'/tracks'
    r = requests.get(url)
    return json.loads(r.text)


def get_song(url):
    r = requests.get(url)
    return json.loads(r.text)


def _load_albums(artist_instance):
    albums = get_albums_for_artist(artist_instance.spotify_id)
    for album in albums['items']:
        album = get_album(album['href'])  # get extended data for album
        if not models.Album.objects.filter(name=album['name']).exists():
            release_date_str = album['release_date']

            if album['release_date_precision'] == 'year':
                date_format = '%Y'
            elif album['release_date_precision'] == 'month':
                date_format = '%Y-%m'
            else:
                date_format = '%Y-%m-%d'
            release_date = datetime.strptime(release_date_str, date_format)
            new_album = models.Album(name=album['name'], artist=artist_instance, release_date=release_date)
            new_album.save()
        else:
            new_album = models.Album.objects.get(name=album['name'])

        songs = get_songs_for_album(album['id'])
        for song in songs['items']:
            song = get_song(song['href'])

            if not models.Song.objects.filter(name=song['name'], album=new_album):
                new_song = models.Song(name=song['name'], album=new_album)
                new_song.save()


def load_albums(artist_instance):
    thread.start_new_thread(_load_albums, (artist_instance,))
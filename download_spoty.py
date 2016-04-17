import requests
import json
from datetime import datetime

import UTD.models

baseurl = "https://api.spotify.com/"


def get_artist_data(id):
    url = baseurl+'v1/artists/'+id
    r = requests.get(url)

    return json.loads(r.text)


def get_albums_for_artist(id):
    url = baseurl+'v1/artists/'+id+'/albums?album_type=album'
    r = requests.get(url)

    return json.loads(r.text)



def get_album(url):
    r = requests.get(url)
    return json.loads(r.text)

def get_songs_for_album(id):
    url = baseurl+'v1/albums/'+id+'/tracks'
    r = requests.get(url)
    return json.loads(r.text)

def get_song(url):
    r = requests.get(url)
    return json.loads(r.text)


def main():
    artists_id = [
        '036IY6CphXdsPiqIXdqvCP',  # la raiz
        '53XhwfbYqKCa1cC15pYq2q',  # imagine dragons
        '0oIls1SE66gDuk4BZObFaN',  # albert pla
        '04gDigrS5kc9YWfZHwBETP',  # maroon 5
    ]

    for id in artists_id:
        artist_json = get_artist_data(id)
        artist_name = artist_json['name']
        if not UTD.models.Artist.objects.filter(name=artist_name).exists():
            new_artist = UTD.models.Artist(name=artist_name)
            new_artist.save()
        else:
            new_artist = UTD.models.Artist.objects.get(name=artist_name)

        albums = get_albums_for_artist(id)
        for album in albums['items']:
            album = get_album(album['href'])  # get extended data for album
            if not UTD.models.Album.objects.filter(name=album['name']).exists():
                release_date_str = album['release_date']

                if album['release_date_precision'] == 'year':
                    format = '%Y'
                elif album['release_date_precision'] == 'month':
                    format = '%Y-%m'
                else:
                    format = '%Y-%m-%d'
                release_date = datetime.strptime(release_date_str, format)
                new_album = UTD.models.Album(name=album['name'], artist=new_artist, release_date=release_date)
                new_album.save()
            else:
                new_album = UTD.models.Album.objects.get(name=album['name'])

            songs = get_songs_for_album(album['id'])
            for song in songs['items']:
                song = get_song(song['href'])

                if not UTD.models.Song.objects.filter(name=song['name'], album=new_album):
                    new_song = UTD.models.Song(name=song['name'], album=new_album)
                    new_song.save()

if __name__ == "__main__":
    main()
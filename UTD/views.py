from django.shortcuts import render
from models import Artist, Album, Song


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
    songs = Song.objects.filter(album= album_id)
    return render(
        request,
        'songslist.html',
        {
            'titlehead': 'List of Songs',
            'pagetitle': 'List of Songs of the album ---> %s <---' % Album.objects.get(pk=album_id).name,
            'songs_list': songs
        }
    )


def song_details(request, song_id):
    song = Song.objects.get(pk= song_id)
    return render(
        request,
        'song.html',
        {
            'titlehead': 'Song details',
            'pagetitle': 'Details of: %s' % song.name,
            'song': song,
        }
    )


from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
import django

# Create your models here.


class Artist(models.Model):
    name = models.TextField()
    related = models.ManyToManyField('self', symmetrical=True, related_name='related', blank=True)
    spotify_id = models.TextField(unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Album(models.Model):
    name = models.TextField(default="Unknown")
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('UTD:album-detail', kwargs={'pkr': self.artist.pk, 'pk': self.pk})


class Song(models.Model):
    name = models.TextField()
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('UTD:song-detail', kwargs={'pkr': self.album.pk, 'pk': self.pk})


class Provider(models.Model):
    provider_name = models.TextField()
    album = models.ForeignKey(Album)
    link = models.URLField()
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u'%s' % self.provider_name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    followed_artist = models.ManyToManyField(Artist, blank=True)


# Create an UserProfile when an user is created.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()


class Playlist(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User)
    songs = models.ManyToManyField(Song, blank=True)
    last_update = models.DateField(default=django.utils.timezone.now)

    class Meta:
        unique_together = ('name', 'user',)

    def __unicode__(self):
        return u'%s' % self.name


# update the playlist.
def update_playlists(sender, user, request, **kwargs):
    print "Updating playlist"
    try:
        playlist = Playlist.objects.get(user=user, name='Following')
        artists = user.userprofile.followed_artist.all()
        for artist in artists:
            albums = Album.objects.filter(artist=artist)

            gen = (album for album in albums if album.release_date > playlist.last_update)
            for album in gen:
                songs = Song.objects.filter(album=album)
                playlist.songs.add(*songs)

        playlist.last_update = django.utils.timezone.now()
        playlist.save()

    except Playlist.DoesNotExist:
        playlist = Playlist(user=user, name='Following')
        playlist.last_update = django.utils.timezone.now()
        playlist.save()

        artists = user.userprofile.followed_artist.all()
        for artist in artists:
            print "Adding albums from artist %s" % artist.name
            albums = Album.objects.filter(artist=artist)
            for album in albums:
                songs = Song.objects.filter(album=album)
                print "Adding songs from algum %s" % album.name
                playlist.songs.add(*songs)


user_logged_in.connect(update_playlists)

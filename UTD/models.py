from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
import django

# Create your models here.


class Artist(models.Model):
    name = models.TextField()
    related = models.ManyToManyField('self', symmetrical=True, related_name='related', blank=True)

    def __unicode__(self):
        return u'%s' % self.name


class Album(models.Model):
    name = models.TextField(default="Unknown")
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()

    def __unicode__(self):
        return u'%s' % self.name


class Song(models.Model):
    name = models.TextField()
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return u'%s' % self.name


class Provider(models.Model):
    provider_name = models.TextField()
    album = models.ForeignKey(Album)
    link = models.TextField()

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
    name = models.TextField(default='Following')
    user = models.ForeignKey(User)
    song = models.ManyToManyField(Song, blank=True)
    last_update = models.DateField(default=django.utils.timezone.now)

    def __unicode__(self):
        return u'Playlist of user %s' % self.user


# update the playlist.
def updatePlaylists(sender, user, request, **kwargs):
    print "Updating playlist"
    try:
        playlist = Playlist.objects.get(user=user)
    except Playlist.DoesNotExist:
        playlist = Playlist(user=user)

    playlist.save()

user_logged_in.connect(updatePlaylists)

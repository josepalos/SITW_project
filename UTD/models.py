from django.db import models
from django.contrib.auth.models import User

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


class UserArtistsList(models.Model):
    user = models.OneToOneField(User)
    followed_artist = models.ManyToManyField(Artist, blank=True)

    def __unicode__(self):
        return u'%s' % self.user

class Playlist(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)

    def __unicode__(self):
        return u'Playlist of user %s' % self.user
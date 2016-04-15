from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Artist(models.Model):
    name = models.TextField()
    related = models.ManyToManyField('self', symmetrical=True, related_name='related')

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

    def get_absolute_url(self):
        return reverse('UTD:song-detail', kwargs={'pkr': self.album.pk, 'pk': self.pk})


class Provider(models.Model):
    provider_name = models.TextField()
    album = models.ForeignKey(Album)
    link = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name


class UserArtistsList(models.Model):
    user_name = models.ForeignKey(User)
    followed_artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return u'%s' % self.user_name

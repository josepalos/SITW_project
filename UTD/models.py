from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.TextField()


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()


class Song(models.Model):
    name = models.TextField()
    album = models.ForeignKey(Album)
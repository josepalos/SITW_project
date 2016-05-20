# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0020_artist_spotify_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='spotify_id',
            field=models.TextField(unique=True),
        ),
    ]
